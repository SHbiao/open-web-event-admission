"""Reproduce post-hoc diagnostics from saved scores, without fitting or inference."""
import argparse
from collections import Counter
import csv
import io
import json
import math
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = "original_exact_existing_joint_linear"
METHODS = (PRIMARY, "direct_admission", "validity")
NAMES = {PRIMARY: "Primary joint linear", "direct_admission": "Direct admission", "validity": "Validity"}
SEED, DRAWS = 20260930, 2000


def jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def threshold(rows, method):
    positive = sorted(r['scores'][method] for r in rows if r['gold_label'] == 'ADMISSIBLE')
    return positive[len(positive) - math.ceil(0.9 * len(positive))]


def percentile(values, q):
    x = sorted(values)
    at = (len(x) - 1) * q
    lo, hi = math.floor(at), math.ceil(at)
    return x[lo] + (x[hi] - x[lo]) * (at - lo)


def describe(values):
    return dict(min=min(values), p025=percentile(values, 0.025),
                median=percentile(values, 0.5), p975=percentile(values, 0.975), max=max(values))


def operating(predictions, gold, method, cutoff):
    retained = false_admitted = 0
    for row in predictions:
        score = row['methods'][method]['score']
        accepted = score is not None and math.isfinite(score) and score >= cutoff
        if gold[row['item_id']] == 'ADMISSIBLE':
            retained += accepted
        else:
            false_admitted += accepted
    return retained, false_admitted


def ranking_metrics(pairs):
    positive = [s for s, y in pairs if y]
    negative = [s for s, y in pairs if not y]
    auc = sum((a > b) + 0.5 * (a == b) for a in positive for b in negative) / (len(positive) * len(negative))
    grouped = {}
    for score, label in pairs:
        grouped.setdefault(score, []).append(label)
    true_positive = seen = 0
    ap = 0.0
    for score in sorted(grouped, reverse=True):
        labels = grouped[score]
        added = sum(labels)
        true_positive += added
        seen += len(labels)
        ap += added / len(positive) * true_positive / seen
    return auc, ap


def run():
    predictions = jsonl(ROOT / 'results/d2_fixed_predictions.jsonl')
    gold_rows = jsonl(ROOT / 'data/human/d2_102.jsonl')
    gold = {r['item_id']: r['gold_label'] for r in gold_rows}
    assert len(predictions) == len(gold) == 102
    assert {r['item_id'] for r in predictions} == set(gold)
    assert Counter(gold.values()) == {'ADMISSIBLE': 57, 'REJECT': 45}
    dev = jsonl(ROOT / 'data/human/dev30_fixed_scores.jsonl')
    assert len(dev) == 30 and len({r['item_id'] for r in dev}) == 30
    positive = [r for r in dev if r['gold_label'] == 'ADMISSIBLE']
    negative = [r for r in dev if r['gold_label'] == 'REJECT']
    assert len(positive) == 12 and len(negative) == 18
    # Confirm every saved decision, not only the three post-hoc methods.
    for row in predictions:
        for record in row['methods'].values():
            score = record['score']
            assert score is None or math.isfinite(score)
            assert record['accepted'] == (score is not None and score >= record['threshold'])
    saved_metrics = json.loads((ROOT / 'results/d2_fixed_metrics.json').read_text())['methods']
    with (ROOT / 'results/d2_aggregate_metrics.csv').open() as stream:
        aggregate = list(csv.DictReader(stream))
    for metric_row in aggregate:
        name = metric_row['method'].removesuffix('_primary')
        records = [(row['methods'][name], gold[row['item_id']] == 'ADMISSIBLE') for row in predictions]
        pairs = [(r['score'], label) for r, label in records if r['score'] is not None]
        counts = operating(predictions, gold, name, records[0][0]['threshold'])
        assert len(pairs) == int(metric_row['score_coverage']) == saved_metrics[name]['n_valid']
        assert counts == (int(metric_row['admissible_retained']), int(metric_row['reject_false_admitted']))
        ranking = saved_metrics[name].get('conditional_valid_score', saved_metrics[name])
        auc, ap = ranking_metrics(pairs)
        assert abs(auc - ranking['roc_auc']) < 1e-12
        assert abs(ap - ranking['auprc']) < 1e-12
    fixed = json.loads((ROOT / 'protocol/posthoc_input_manifest.json').read_text())['thresholds']
    status_counts = {s: {'ADMISSIBLE': 0, 'REJECT': 0} for s in
                     ('NO_CANDIDATE', 'INVALID_SPANS', 'INVALID_JSON', 'SCORED_NOT_ADMITTED', 'SCORED_ADMITTED')}
    for row in predictions:
        record = row['methods'][PRIMARY]
        status = record['score_status'] if record['score'] is None else (
            'SCORED_ADMITTED' if record['accepted'] else 'SCORED_NOT_ADMITTED')
        status_counts[status][gold[row['item_id']]] += 1
    assert sum(r['ADMISSIBLE'] for r in status_counts.values()) == 57
    assert sum(r['REJECT'] for r in status_counts.values()) == 45
    assert status_counts['SCORED_ADMITTED'] == {'ADMISSIBLE': 40, 'REJECT': 10}
    assert sum(sum(status_counts[s].values()) for s in ('NO_CANDIDATE', 'INVALID_SPANS', 'INVALID_JSON')) == 23
    rng = random.Random(SEED)
    draws = [rng.choices(positive, k=12) + rng.choices(negative, k=18) for _ in range(DRAWS)]
    methods = {}
    for name in METHODS:
        assert abs(threshold(dev, name) - fixed[name]) < 1e-12
        assert all(r['methods'][name]['threshold'] == fixed[name] for r in predictions)
        entry = {'fixed_threshold': fixed[name], 'fixed_operating_counts': operating(predictions, gold, name, fixed[name])}
        for title, samples in [('bootstrap', draws), ('leave_one_out', [dev[:i] + dev[i+1:] for i in range(30)])]:
            cutoffs = [threshold(sample, name) for sample in samples]
            counts = [operating(predictions, gold, name, cutoff) for cutoff in cutoffs]
            entry[title] = {'threshold': describe(cutoffs), 'retained': describe([c[0] for c in counts]),
                            'false_admitted': describe([c[1] for c in counts]), 'distinct_thresholds': len(set(cutoffs))}
        methods[name] = entry
    return {'analysis': 'post-hoc descriptive; no model refitting or operating-point selection',
            'seed': SEED, 'bootstrap_draws': DRAWS, 'positive_denominator': 57, 'negative_denominator': 45,
            'primary_pipeline_counts': status_counts, 'threshold_stability': methods}


def csv_text(rows, fields):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    return stream.getvalue()


def outputs(result):
    loss = [{'status': k, **v, 'total': sum(v.values())} for k, v in result['primary_pipeline_counts'].items()]
    stability = []
    for name, entry in result['threshold_stability'].items():
        for resampling in ('bootstrap', 'leave_one_out'):
            for quantity in ('threshold', 'retained', 'false_admitted'):
                stability.append({'method': name, 'resampling': resampling, 'quantity': quantity,
                                  **entry[resampling][quantity]})
    return {'posthoc_analysis.json': json.dumps(result, indent=2, allow_nan=False) + '\n',
            'pipeline_loss.csv': csv_text(loss, ['status', 'ADMISSIBLE', 'REJECT', 'total']),
            'threshold_stability.csv': csv_text(stability, ['method', 'resampling', 'quantity', 'min', 'p025', 'median', 'p975', 'max'])}


def tex_tables(result, folder):
    folder.mkdir(parents=True, exist_ok=True)
    loss = [r'\begin{tabular}{@{}lrrr@{}}', r'\toprule',
            r'Primary outcome & Admissible / 57 & Reject / 45 & Total \\', r'\midrule']
    names = {'NO_CANDIDATE': 'No candidate', 'INVALID_SPANS': 'Invalid spans', 'INVALID_JSON': 'Invalid JSON',
             'SCORED_NOT_ADMITTED': 'Scored, not admitted', 'SCORED_ADMITTED': 'Scored, admitted'}
    for status, counts in result['primary_pipeline_counts'].items():
        loss.append(f"{names[status]} & {counts['ADMISSIBLE']} & {counts['REJECT']} & {sum(counts.values())} " + r'\\')
    loss.extend([r'\midrule', r'Total & 57 & 45 & 102 \\', r'\bottomrule', r'\end{tabular}'])
    (folder/'pipeline_loss.tex').write_text('\n'.join(loss)+'\n')
    stability = [r'\begin{tabular}{@{}lrrrr@{}}', r'\toprule',
                 r'System & Fixed $\tau$ & DEV-bootstrap $\tau$ range & D2 retained / 57 & D2 false admitted / 45 \\', r'\midrule']
    for name, record in result['threshold_stability'].items():
        b = record['bootstrap']; t = b['threshold']; a = b['retained']; r = b['false_admitted']
        stability.append(f"{NAMES[name]} & {record['fixed_threshold']:.4f} & [{t['p025']:.4f}, {t['p975']:.4f}] & "
                         f"[{a['p025']:.0f}, {a['p975']:.0f}] & [{r['p025']:.0f}, {r['p975']:.0f}] " + r'\\')
    stability.extend([r'\bottomrule', r'\end{tabular}'])
    (folder/'threshold_stability.tex').write_text('\n'.join(stability)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--tex-dir', type=Path)
    args = parser.parse_args()
    result = run()
    for name, content in outputs(result).items():
        path = ROOT / 'results' / name
        if args.check:
            assert path.read_text(encoding='utf-8') == content, f'Reproduction mismatch: {name}'
        else:
            path.write_text(content, encoding='utf-8')
    if args.tex_dir:
        tex_tables(result, args.tex_dir)
    print('PASS: all eight fixed point metrics, AUC/AUPRC, loss counts, and threshold diagnostics reproduced.')
