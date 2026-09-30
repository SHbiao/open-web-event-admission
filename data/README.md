# Data release

The full benchmark suite has 572 item-level examples across five distinct layers:

- P0 task-unit calibration: 80 items;
- DEV30: 30 development items;
- EVAL60/Web60: 60 controlled-diagnostic items;
- D2: 102 challenge-confirmation items;
- audited Silver extension: 300 items.

The layers serve different evidential roles. They must not be concatenated into one homogeneous test set or described as 572 human-Gold examples.

## Released files

- `p0_item_level_calibration.csv`: item-level P0 calibration metadata.
- `d2_102.jsonl`: the cleaned annotation view and final human Gold labels for all 102 D2 challenge-confirmation items.
- `silver_300.jsonl`: the cleaned annotation view and recommended Silver labels for 300 items.
- `silver_300_provenance.jsonl`: per-item model agreement and human-review provenance.

Each D2 and Silver evidence object contains only `body`, `published_utc`, `is_reply`, `is_quote`, and `has_media`, matching the information available to annotators. The release omits direct source IDs, author records, acquisition payloads, external model scores, model rationales, and private session logs.

The Silver collection remains Silver because 212 items rely on unreviewed dual-model consensus. The other 88 items comprise all 28 model disagreements and a blinded, stratified audit of 60 model agreements. D2 texts and final Gold labels are public; private A/B session records and C adjudication notes are not part of the release.

## D2 schema

| Field | Meaning |
| --- | --- |
| `item_id` | Original stable ID, `D2-0001` through `D2-0102`. |
| `evidence.body` | Exact text shown to the human annotators. |
| `evidence.published_utc` | Displayed publication timestamp. |
| `evidence.is_reply`, `evidence.is_quote`, `evidence.has_media` | Displayed Boolean metadata flags. |
| `evidence_sha256` | Frozen hash of the UTF-8 evidence JSON, with sorted keys, `ensure_ascii=False`, and compact separators. |
| `gold_label` | Final `ADMISSIBLE` or `REJECT` label. |
| `gold_source` | `AB_AGREEMENT` or `C_ADJUDICATION`. |

Rows are ordered by stable ID for release. All evidence fields and labels match the frozen annotation and fusion inputs. Counts are 57 ADMISSIBLE / 45 REJECT, with 85 A/B agreements and 17 human-adjudicated disagreements. The public file intentionally omits individual annotator labels, identities, rationales, and session logs.

Use `evidence` alone as model input and join predictions to `gold_label` by `item_id` for evaluation. Keep D2 separate from development and Silver data. Missing predictions remain in the full 102-item denominator, including the 57-item ADMISSIBLE and 45-item REJECT class denominators.
