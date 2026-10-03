# Open-Web Event Admission / Calibration

This repository contains the released data, annotation protocols, evaluation code, and results for **When Candidate Retrieval Is Not Admission: A Coverage-Aware Evaluation Framework for Open-Web Event Organization**.

The public collection contains **1,290 item records** in two annotation groups: **472 human-annotated records** and **818 AI-assisted records**. The primary system evaluation uses **302 human-annotated items**, with 209 `ADMISSIBLE` and 93 `REJECT` labels. The remaining 170 human records support calibration and controlled diagnostics; the AI-assisted group provides broader phenomenon observations and future extension resources.

## Repository layout

- `src/`: fixed evaluation runner and release-validation scripts.
- `protocol/`: measurement contracts, study records, annotation guides, and post-hoc analysis specifications.
- `results/`: fixed challenge scores, metrics, pipeline diagnostics, and annotation-quality analyses.
- `data/human/`: D2, calibration, controlled-diagnostic, and human-extension records.
- `data/ai/`: AI-assisted extension records and their provenance.

## Reproducibility status

The reported system evaluation pools 102 earlier challenge items and 200 independently human-annotated extension items. The same eight systems, prompts, features, and development-selected thresholds are applied to both cohorts. Earlier predictions remain unchanged; inference on the extension consumed displayed evidence without labels. `results/human_302/` contains the complete score projection, fixed metrics, and post-hoc diagnostics.

The D2 release contains all 102 annotation-visible items and their final item labels: 57 `ADMISSIBLE` and 45 `REJECT`. Labels come from 85 A/B agreements and 17 human adjudications. See [the dataset schema](data/README.md) and [the D2 annotation guide](protocol/d2_annotation_guide.md).

Validate the released IDs, label counts, provenance counts, and evidence hashes with Python 3 (standard library only):

```bash
python src/export_d2_release.py
```

`src/run_d2_fixed_evaluation.py` preserves the historical evaluation runner. Its original execution requires the archived Stage2 resources, serialized models, and runtime layout; the cleaned release does not bundle those dependencies.

## Reproduce the 302-item evaluation

```bash
python src/analyze_human_302.py --check
```

This standard-library script independently verifies 302 unique IDs, all eight systems' saved decisions, full/conditional AUC and AUPRC, Coverage, Admission Retention, Reject FAR, pipeline loss counts, and development-score threshold sensitivity. It reads the two existing human data files and joins labels to predictions by stable ID. It performs no inference or model fitting.

| Method | Coverage | Retained / 209 | False admitted / 93 | AUC |
| --- | ---: | ---: | ---: | ---: |
| Admit-all | 302/302 | 209 | 93 | 0.500 |
| BM25 | 301/302 | 188 | 60 | conditional 0.738 |
| BGE | 301/302 | 192 | 80 | conditional 0.637 |
| Validity | 255/302 | 168 | 24 | conditional 0.895 |
| Direct admission | 302/302 | 175 | 23 | 0.875 |
| Clean linear | 302/302 | 136 | 44 | 0.582 |
| Clean RBF | 302/302 | 124 | 27 | 0.712 |
| Primary joint linear | 255/302 | 153 | 17 | conditional 0.844 |

Primary and Direct occupy different operating points: Direct retains 22 more admissible items and falsely admits six more Reject items. Full-set ranking metrics remain unavailable for paths with incomplete score coverage.

## Reproduce the original subset diagnostics

The IPM revision adds descriptive analysis of existing outputs, with no inference, model refitting, or replacement of the original thresholds. Reproduce it with Python 3.9 or later and no third-party packages:

```bash
python src/analyze_posthoc.py --check
```

This checks all eight saved fixed operating points and AUC/AUPRC values, then reproduces the class-by-stage loss decomposition, 2,000 development-score bootstrap draws, and leave-one-out threshold diagnostics. Resampling intervals describe sensitivity of the saved fitted scores; they are not population-performance confidence intervals or newly selected operating points.

| Manuscript component | Released input / configuration | Reproduction or output |
| --- | --- | --- |
| Item policy and D2 labels | `data/human/d2_102.jsonl`, `protocol/d2_annotation_guide.md` | `src/export_d2_release.py` validates IDs, labels, and evidence hashes. |
| Exact semantic prompts | `protocol/fixed_model_prompts.json` | Extractor, validity, salience, and admission templates from the archived protocol. |
| Fixed thresholds and resource identity | `protocol/posthoc_input_manifest.json` | Original prediction, calibration, prompt, model, and catalog hashes; saved DEV and D2 split IDs. |
| Primary eight-system evaluation | `results/human_302/predictions.jsonl`, both human evaluation data files | `results/human_302/fixed_metrics.json`; checked by `src/analyze_human_302.py`. |
| Pipeline loss decomposition | Saved 302-item scores/statuses plus human labels | `results/human_302/pipeline_loss.csv`. |
| Threshold stability | `data/human/dev30_fixed_scores.jsonl`, `protocol/human_302_evaluation.md` | `results/human_302/threshold_stability.csv`, `results/human_302/posthoc_analysis.json`. |
| Original subset evaluation | `results/d2_fixed_predictions.jsonl` | Original results and `src/analyze_posthoc.py` remain unchanged. |
| Public collection | `data/human/`, `data/ai/` | Group-level labels, provenance, and the collection manifest. |

The score release is an exact projection of saved outputs, not a rerun. `src/prepare_posthoc_release.py` documents the export and checks source identities; users reproducing the diagnostics need only the files already in this repository. DEV identifiers in the score view are release-local identifiers preserving archived row order; private DEV text and acquisition identifiers are not required by the analysis.

The original subset's versioned snapshot is `ipm-evaluation-v1`. Expanded results are under `results/human_302/`; their manifest preserves the two source cohorts and saved prediction identities.

## Annotation groups

- `data/human/` contains the 102-item D2 challenge set, the P0/DEV30/EVAL60 calibration and diagnostic records, and the 200-item independently annotated extension. The 200-item extension was annotated by two people and adjudicated on 46 disagreements; its fused labels are 152 `ADMISSIBLE` and 48 `REJECT`.
- `data/ai/consensus_extension_518.jsonl` contains 518 items selected from an 800-item frozen candidate pool when two independent model passes produced the same label. The 282 disagreements remain in the private audit ledger and are not silently relabelled.
- `data/ai/ai_extension_300.jsonl` contains the earlier 300-item AI-assisted extension, with its item-level provenance. The public release keeps its audit record and uses it as an auxiliary observation and resource component.

## Data and ethics

The released JSONL views contain body text, UTC time, reply/quote/media flags, labels, and compact provenance fields matching the information shown during annotation. Direct source identifiers, author records, acquisition responses, model rationales, and private annotation sessions are not included. Text and metadata are preserved as displayed to annotators.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
