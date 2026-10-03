"""Reproduce the 302-item evaluation and post-hoc diagnostics from public scores."""
import argparse
import json
import random
from collections import Counter
from pathlib import Path

from analyze_posthoc import (METHODS, SEED, DRAWS, describe, jsonl, operating,
                             outputs, ranking_metrics, threshold)

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'results/human_302'


def run():
    predictions = jsonl(DEST / 'predictions.jsonl')
    references = jsonl(ROOT / 'data/human/d2_102.jsonl') + jsonl(ROOT / 'data/human/human_extension_200.jsonl')
    labels = {r['item_id']: r.get('label', r.get('gold_label')) for r in references}
    assert len(predictions) == len(labels) == 302
    assert len({r['item_id'] for r in predictions}) == 302
    assert {r['item_id'] for r in predictions} == set(labels)
    assert Counter(labels.values()) == {'ADMISSIBLE': 209, 'REJECT': 93}
    saved = json.loads((DEST / 'fixed_metrics.json').read_text())['methods']
    summary = []
    for name, metric in saved.items():
        records = [r['methods'][name] for r in predictions]
        cutoff = records[0]['threshold']
        assert all(r['threshold'] == cutoff for r in records)
        assert all(r['accepted'] == (r['score'] is not None and r['score'] >= cutoff) for r in records)
        pairs = [(r['methods'][name]['score'], labels[r['item_id']] == 'ADMISSIBLE') for r in predictions if r['methods'][name]['score'] is not None]
        retained, falsely = operating(predictions, labels, name, cutoff)
        auc, ap = ranking_metrics(pairs)
        rank = metric.get('conditional_valid_score', metric)
        assert len(pairs) == metric['n_valid']
        assert abs(retained / 209 - metric['admission_retention']) < 1e-12
        assert abs(falsely / 93 - metric['reject_far']) < 1e-12
        assert abs(auc - rank['roc_auc']) < 1e-12
        assert abs(ap - rank['auprc']) < 1e-12
        summary.append({'method': name, 'coverage_count': len(pairs), 'retained': retained,
                        'false_admitted': falsely, 'auc': auc, 'auprc': ap,
                        'ranking_population': 'full' if len(pairs) == 302 else 'conditional'})
    counts = {s: {'ADMISSIBLE': 0, 'REJECT': 0} for s in
              ('NO_CANDIDATE', 'INVALID_SPANS', 'INVALID_JSON', 'SCORED_NOT_ADMITTED', 'SCORED_ADMITTED')}
    for row in predictions:
        record = row['methods'][METHODS[0]]
        status = record['score_status'] if record['score'] is None else ('SCORED_ADMITTED' if record['accepted'] else 'SCORED_NOT_ADMITTED')
        counts[status][labels[row['item_id']]] += 1
    dev = jsonl(ROOT / 'data/human/dev30_fixed_scores.jsonl')
    positive = [r for r in dev if r['gold_label'] == 'ADMISSIBLE']
    negative = [r for r in dev if r['gold_label'] == 'REJECT']
    assert (len(positive), len(negative)) == (12, 18)
    rng = random.Random(SEED)
    draws = [rng.choices(positive, k=12) + rng.choices(negative, k=18) for _ in range(DRAWS)]
    methods = {}
    for name in METHODS:
        fixed = threshold(dev, name)
        assert all(r['methods'][name]['threshold'] == fixed for r in predictions)
        entry = {'fixed_threshold': fixed, 'fixed_operating_counts': operating(predictions, labels, name, fixed)}
        for title, samples in [('bootstrap', draws), ('leave_one_out', [dev[:i] + dev[i+1:] for i in range(30)])]:
            cutoffs = [threshold(sample, name) for sample in samples]
            actions = [operating(predictions, labels, name, c) for c in cutoffs]
            entry[title] = {'threshold': describe(cutoffs), 'retained': describe([a for a, _ in actions]),
                            'false_admitted': describe([b for _, b in actions]), 'distinct_thresholds': len(set(cutoffs))}
        methods[name] = entry
    return {'analysis': 'post-hoc descriptive; no refitting or operating-point selection',
            'seed': SEED, 'bootstrap_draws': DRAWS, 'positive_denominator': 209, 'negative_denominator': 93,
            'main_results': summary, 'primary_pipeline_counts': counts, 'threshold_stability': methods}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = run()
    for name, content in outputs(result).items():
        path = DEST / name
        if args.check:
            assert path.read_text(encoding='utf-8') == content, f'Mismatch: {name}'
        else:
            path.write_text(content, encoding='utf-8')
    print('PASS: 302 IDs, all eight fixed decisions and ranking metrics, loss decomposition and threshold diagnostics.')
