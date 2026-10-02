"""Export immutable score views for the IPM post-hoc diagnostics; no inference."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHOD_MAP = {"original_exact_existing_joint_linear": "existing_joint_linear",
              "direct_admission": "direct_admission", "validity": "validity"}


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value, lines=False):
    with path.open("x", encoding="utf-8", newline="\n") as f:
        if lines:
            for row in value:
                f.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")
        else:
            json.dump(value, f, indent=2, ensure_ascii=False, allow_nan=False)
            f.write("\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--runtime", required=True, type=Path)
    p.add_argument("--development", required=True, type=Path)
    args = p.parse_args()
    pred_path = args.runtime / "predictions.jsonl"
    manifest = read(args.runtime / "predictions_manifest.json")
    assert sha(pred_path) == manifest["sha256"]
    source = [json.loads(s) for s in pred_path.read_text().splitlines()]
    assert len(source) == len({r['item_id'] for r in source}) == 102
    predictions = [{"item_id": r["item_id"], "methods": r["methods"]} for r in source]
    historical = args.development / "item_predictions.csv"
    calibration_path = args.development / "calibration.json"
    assert sha(calibration_path) == manifest["calibration_sha256"]
    calibration = read(calibration_path)
    with historical.open(encoding="utf-8-sig", newline="") as f:
        dev = [r for r in csv.DictReader(f) if r["split"] == "DEV"]
    assert len(dev) == 30 and sum(r['label'] == 'ADMISSIBLE' for r in dev) == 12
    assert set(r["item_id"] for r in dev) == set(calibration["dev_ids"])
    scores = [{"item_id": f"DEV-{i:04d}", "split": "DEV30", "gold_label": r["label"],
               "scores": {name: float(r["score_" + old]) for name, old in METHOD_MAP.items()}}
              for i, r in enumerate(dev, 1)]
    thresholds = {name: calibration["thresholds"][old] for name, old in METHOD_MAP.items()}
    for name in METHOD_MAP:
        positives = sorted(r['scores'][name] for r in scores if r['gold_label'] == 'ADMISSIBLE')
        assert abs(positives[1] - thresholds[name]) < 1e-12
    write(ROOT / "results/d2_fixed_predictions.jsonl", predictions, lines=True)
    write(ROOT / "data/human/dev30_fixed_scores.jsonl", scores, lines=True)
    write(ROOT / "results/d2_fixed_metrics.json", read(args.runtime / "fixed_metrics.json"))
    protocol_path = args.development / "protocol.json"
    protocol = read(protocol_path)
    write(ROOT / "protocol/fixed_model_prompts.json", protocol["prompts"])
    resources = {"source_prediction_sha256": sha(pred_path),
                 "source_development_predictions_sha256": sha(historical),
                 "source_calibration_sha256": sha(calibration_path),
                 "source_protocol_sha256": sha(protocol_path),
                 "source_resource_hashes": manifest,
                 "thresholds": thresholds,
                 "dev_class_counts": {"ADMISSIBLE": 12, "REJECT": 18},
                 "dev_ids": [r['item_id'] for r in scores],
                 "d2_ids": sorted(r['item_id'] for r in predictions),
                 "dev_order": "Archived DEV row order, with release-local identifiers; no text released.",
                 "analysis_status": "Post-hoc; models and D2 predictions unchanged."}
    write(ROOT / "protocol/posthoc_input_manifest.json", resources)
    assert sha(pred_path) == manifest['sha256']
    print("Exported exact D2 method outputs, DEV30 score view, prompts, and resource identity.")


if __name__ == "__main__":
    main()
