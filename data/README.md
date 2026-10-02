# Data release

The public collection contains 1,290 item-level records across seven documented layers:

- P0 task-unit calibration: 80 items;
- DEV30: 30 development items;
- EVAL60/Web60: 60 controlled-diagnostic items;
- D2: 102 challenge-confirmation items;
- audited extension: 300 items;
- consensus extension: 518 items from an 800-item frozen candidate pool;
- human extension: 200 newly annotated items.

These layers have distinct construction and evaluation roles. They are released together as a 1K-scale collection, while system comparisons remain tied to their declared input layer and denominator.

## Released files

- `p0_item_level_calibration.csv`: item-level P0 calibration metadata.
- `d2_102.jsonl`: the cleaned annotation view and final item labels for all 102 D2 challenge-confirmation items.
- `dev30_fixed_scores.jsonl`: the 30 archived development labels and fixed scores used only for the declared post-hoc threshold analysis.
- `consensus_extension_518.jsonl`: 518 dual-model-consensus items from the new 800-item extension.
- `consensus_extension_518_provenance.jsonl`: model agreement and evidence-hash provenance for those items.
- `human_extension_200.jsonl`: 200 items with independent human A/B annotation and adjudication.
- `human_extension_200_provenance.jsonl`: A/B labels, resolution type, and evidence-hash provenance.
- `extension_manifest.json`: counts and fixed selection rules for the two new extensions.
- `silver_300.jsonl`: historical filename for the earlier 300-item audited extension; retained for reproducibility.
- `silver_300_provenance.jsonl`: historical provenance filename for that extension.

Each extension evidence object contains only `body`, `published_utc`, `is_reply`, `is_quote`, and `has_media`, matching the information available to annotators. The release omits direct source IDs, author records, acquisition payloads, external model scores, model rationales, and private session logs.

## Common schema

| Field | Meaning |
| --- | --- |
| `item_id` | Stable release identifier. |
| `evidence` | The exact body and displayed UTC/reply/quote/media fields shown during annotation. |
| `evidence_sha256` | Frozen hash of the UTF-8 evidence JSON. |
| `label` | Final `ADMISSIBLE` or `REJECT` item label. |
| `collection_layer` | Construction layer such as `consensus_extension` or `human_extension`. |

Rows are ordered by stable ID within each generated extension file. Use `evidence` alone as model input and join predictions to `label` by `item_id` for extension analyses. Keep the D2 challenge data separate from development data and extensions when reproducing the fixed system comparison. Missing predictions remain in the declared denominator for the layer being evaluated.

## D2 compatibility schema

`d2_102.jsonl` retains the historical field names `gold_label` and `gold_source` so that the published evaluation scripts reproduce the fixed D2 results without modification. They denote the final item label and its annotation provenance in that file. Counts are 57 `ADMISSIBLE` / 45 `REJECT`, with 85 A/B agreements and 17 human adjudications.
