"""Build the neutral public extension views from frozen Stage4 artifacts.

The script intentionally exports evidence and labels, not model rationales or
private annotation sessions.  It keeps the provenance needed to reproduce the
selection rule while leaving the original Stage4 artifacts untouched.
"""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[3]
STAGE4 = PROJECT / "Stage4_数据扩展"
RELEASE = Path(__file__).resolve().parents[1]
DATA = RELEASE / "data"


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at {path}:{line_number}") from exc
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> None:
    opus_items = read_jsonl(STAGE4 / "AI_800_consensus_batch/Opus/items.jsonl")
    opus_labels = read_jsonl(STAGE4 / "AI_800_consensus_batch/Opus/annotations.jsonl")
    astra_labels = read_jsonl(STAGE4 / "AI_800_consensus_batch/Astra/annotations.jsonl")
    human_items = read_jsonl(STAGE4 / "human/fresh_200/A/items.jsonl")
    human_fused = read_jsonl(STAGE4 / "human/fresh_200/fused_human_200.jsonl")

    opus_by_id = {row["item_id"]: row for row in opus_labels}
    astra_by_id = {row["item_id"]: row for row in astra_labels}
    item_by_id = {row["item_id"]: row for row in opus_items}
    common_ids = [row["item_id"] for row in opus_items if row["item_id"] in opus_by_id and row["item_id"] in astra_by_id]
    consensus_ids = [item_id for item_id in common_ids if opus_by_id[item_id]["label"] == astra_by_id[item_id]["label"]]
    if len(consensus_ids) != 518:
        raise ValueError(f"expected 518 consensus items, found {len(consensus_ids)}")

    consensus_rows = []
    consensus_provenance = []
    for item_id in consensus_ids:
        item = item_by_id[item_id]
        label = opus_by_id[item_id]["label"]
        consensus_rows.append({
            "item_id": item_id,
            "evidence": item["evidence"],
            "evidence_sha256": item["evidence_sha256"],
            "label": label,
            "collection_layer": "consensus_extension",
        })
        consensus_provenance.append({
            "item_id": item_id,
            "evidence_sha256": item["evidence_sha256"],
            "opus_label": label,
            "astra_label": label,
            "model_agreement": True,
            "selection_rule": "dual_model_consensus_only",
            "collection_layer": "consensus_extension",
        })

    human_by_id = {row["item_id"]: row for row in human_items}
    fused_by_id = {row["item_id"]: row for row in human_fused}
    if set(human_by_id) != set(fused_by_id) or len(human_by_id) != 200:
        raise ValueError("human extension input and fused labels do not align at 200 unique IDs")

    human_rows = []
    human_provenance = []
    for item in human_items:
        item_id = item["item_id"]
        fused = fused_by_id[item_id]
        human_rows.append({
            "item_id": item_id,
            "evidence": item["evidence"],
            "evidence_sha256": item["evidence_sha256"],
            "label": fused["label"],
            "collection_layer": "human_extension",
        })
        human_provenance.append({
            "item_id": item_id,
            "evidence_sha256": item["evidence_sha256"],
            "label": fused["label"],
            "resolution": fused["resolution"],
            "a_label": fused["a_label"],
            "b_label": fused["b_label"],
            "adjudication_label": fused["adjudication_label"],
            "annotation_source": "independent_human_annotation_with_adjudication",
            "collection_layer": "human_extension",
        })

    DATA.mkdir(exist_ok=True)
    write_jsonl(DATA / "consensus_extension_518.jsonl", consensus_rows)
    write_jsonl(DATA / "consensus_extension_518_provenance.jsonl", consensus_provenance)
    write_jsonl(DATA / "human_extension_200.jsonl", human_rows)
    write_jsonl(DATA / "human_extension_200_provenance.jsonl", human_provenance)

    summary = {
        "consensus_extension": {"items": len(consensus_rows), "source_candidates": 800, "excluded_disagreements": 282},
        "human_extension": {"items": len(human_rows), "source": "fresh_200", "adjudicated_disagreements": 46},
        "total_extension_items": len(consensus_rows) + len(human_rows),
    }
    (DATA / "extension_manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
