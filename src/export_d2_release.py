"""Export the frozen D2 annotation view and final Gold, without private records."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


FROZEN_INPUTS = {
    "A_package/items.json": "1139a8f2d88096a053abee1ba125c39b92aa424d5e4ad170d7a78fbe263f21e4",
    "B_package/items.json": "b37af7fe699d89b0ec2486493e4f4f2313b308bc12a6410deabe2e2b6bdbbc64",
    "private/fused_gold_20260929.jsonl": "6cbd8fec4b39bf61af31fb593769b91e53c2ad89b9f9396bb5aaf11d1d410348",
}
EVIDENCE_FIELDS = {"body", "published_utc", "is_reply", "is_quote", "has_media"}
RELEASE_FIELDS = {"item_id", "evidence", "evidence_sha256", "gold_label", "gold_source"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(rows):
    require(len(rows) == 102, "Expected 102 items")
    require({r["item_id"] for r in rows} == {f"D2-{i:04d}" for i in range(1, 103)},
            "D2 IDs must be unique and complete")
    require(Counter(r["gold_label"] for r in rows) == {"ADMISSIBLE": 57, "REJECT": 45},
            "Gold label counts differ from the frozen set")
    require(Counter(r["gold_source"] for r in rows) == {"AB_AGREEMENT": 85, "C_ADJUDICATION": 17},
            "Gold provenance counts differ from the frozen set")
    for row in rows:
        require(set(row) == RELEASE_FIELDS, "Unexpected release field")
        require(set(row["evidence"]) == EVIDENCE_FIELDS, "Unexpected evidence field")
        canonical = json.dumps(row["evidence"], ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")).encode("utf-8")
        require(hashlib.sha256(canonical).hexdigest() == row["evidence_sha256"],
                f"Evidence changed: {row['item_id']}")


def export(source, output):
    for relative, expected in FROZEN_INPUTS.items():
        require(hashlib.sha256((source / relative).read_bytes()).hexdigest() == expected,
                f"Frozen input changed: {relative}")
    a = json.loads((source / "A_package/items.json").read_text(encoding="utf-8"))
    b = json.loads((source / "B_package/items.json").read_text(encoding="utf-8"))
    require({r["item_id"]: r for r in a} == {r["item_id"]: r for r in b},
            "A/B evidence differs")
    gold = [json.loads(line) for line in
            (source / "private/fused_gold_20260929.jsonl").read_text(encoding="utf-8").splitlines()]
    by_id = {r["item_id"]: r for r in gold}
    require(len(gold) == len(by_id) == 102 and set(by_id) == {r["item_id"] for r in a},
            "Gold IDs do not match the evidence")
    rows = []
    for item in sorted(a, key=lambda row: row["item_id"]):
        label = by_id[item["item_id"]]
        require(item["evidence_sha256"] == label["evidence_sha256"], "Gold evidence mismatch")
        if label["gold_source"] == "AB_AGREEMENT":
            require(label["gold_label"] == label["A_label"] == label["B_label"], "Agreement mismatch")
        else:
            require(label["A_label"] != label["B_label"] and label["gold_label"] == label["C_label"],
                    "Adjudication mismatch")
        rows.append({"item_id": item["item_id"], "evidence": item["evidence"],
                     "evidence_sha256": item["evidence_sha256"],
                     "gold_label": label["gold_label"], "gold_source": label["gold_source"]})
    validate(rows)
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    require([json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()] == rows,
            "Export round-trip mismatch")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Frozen D2 archive root; omit to validate the public file")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data/d2_102.jsonl")
    args = parser.parse_args()
    if args.source:
        export(args.source, args.output)
    else:
        validate([json.loads(line) for line in args.output.read_text(encoding="utf-8").splitlines()])
    print("PASS: 102 unique D2 items; 57 ADMISSIBLE / 45 REJECT; 85 agreements / 17 adjudications.")
