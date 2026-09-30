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
- `silver_300.jsonl`: the cleaned annotation view and recommended Silver labels for 300 items.
- `silver_300_provenance.jsonl`: per-item model agreement and human-review provenance.

Each Silver evidence object contains only `body`, `published_utc`, `is_reply`, `is_quote`, and `has_media`, matching the information available to annotators. The release omits direct source IDs, author records, acquisition payloads, external model scores, model rationales, and private session logs.

The Silver collection remains Silver because 212 items rely on unreviewed dual-model consensus. The other 88 items comprise all 28 model disagreements and a blinded, stratified audit of 60 model agreements. D2 texts, A/B annotation packages, C adjudication records, and fused D2 Gold labels remain in the private research archive.
