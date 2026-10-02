# Data release

The public collection contains **1,290 item-level records** organized into two annotation groups. The human group contains 472 records, including the 302-item primary evidence core; the AI-assisted group contains 818 extension records.

## Group contents

### Human group

- `human/d2_102.jsonl`: the cleaned annotation view and final item labels for all 102 D2 challenge-confirmation items.
- `human/p0_item_level_calibration.csv`: item-level P0 calibration metadata.
- `human/dev30_fixed_scores.jsonl`: the 30 archived development labels and fixed scores used only for the declared post-hoc threshold analysis.
- `human/eval60_fixed_labels.jsonl`: the 60 archived evaluation labels used in the controlled comparisons.
- `human/human_extension_200.jsonl`: 200 items with independent human A/B annotation and adjudication.
- `human/human_extension_200_provenance.jsonl`: A/B labels, resolution type, and evidence-hash provenance.

### AI-assisted group

- `ai/consensus_extension_518.jsonl`: 518 dual-model-consensus items from the new 800-item extension.
- `ai/consensus_extension_518_provenance.jsonl`: model agreement and evidence-hash provenance for those items.
- `ai/ai_extension_300.jsonl`: the earlier 300-item audited AI-assisted extension.
- `ai/ai_extension_300_provenance.jsonl`: item-level provenance for the earlier extension.

The root `extension_manifest.json` records collection counts and fixed extension-selection rules. The 302-item human core carries the main empirical claims; the AI-assisted group expands resource scale and supports annotation-quality analysis.

Each extension evidence object contains only `body`, `published_utc`, `is_reply`, `is_quote`, and `has_media`, matching the information available to annotators. The release omits direct source IDs, author records, acquisition payloads, external model scores, model rationales, and private session logs.

## Common schema

| Field | Meaning |
| --- | --- |
| `item_id` | Stable release identifier. |
| `evidence` | The exact body and displayed UTC/reply/quote/media fields shown during annotation. |
| `evidence_sha256` | Frozen hash of the UTF-8 evidence JSON. |
| `label` | Final `ADMISSIBLE` or `REJECT` item label. |
| `collection_group` | `human` or `ai_assisted`. |

Rows are ordered by stable ID within each generated extension file. Use `evidence` alone as model input and join predictions to `label` by `item_id` for extension analyses. Keep the D2 challenge data separate from development data and extensions when reproducing the fixed system comparison. Missing predictions remain in the declared denominator for the group being evaluated.

## D2 compatibility schema

`human/d2_102.jsonl` retains the historical field names `gold_label` and `gold_source` so that the published evaluation scripts reproduce the fixed D2 results without modification. They denote the final item label and its annotation provenance in that file. Counts are 57 `ADMISSIBLE` / 45 `REJECT`, with 85 A/B agreements and 17 human adjudications.
