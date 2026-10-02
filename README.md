# Open-Web Event Admission / Calibration

This repository contains the released data, annotation protocols, evaluation code, and results for **When Candidate Retrieval Is Not Admission: A Coverage-Aware Evaluation Framework for Open-Web Event Organization**.

The public collection contains **1,290 item records**. It is presented in two annotation groups: a human group of 472 records and an AI-assisted group of 818 records. The principal empirical evidence is the 302-item human core, formed by the 102-item D2 challenge set and the 200-item independently annotated extension. The other records provide calibration, controlled diagnostics, annotation analysis, and reusable scale.

## Repository layout

- `src/`: fixed evaluation runner and release-validation scripts.
- `protocol/`: measurement contracts, study records, annotation guides, and post-hoc analysis specifications.
- `results/`: fixed challenge scores, metrics, pipeline diagnostics, and annotation-quality analyses.
- `data/human/`: D2, calibration, controlled-diagnostic, and human-extension records.
- `data/ai/`: AI-assisted extension records and their provenance.

## Reproducibility status

The reported system evaluation uses the fixed 102-item D2 challenge set, thresholds selected on development material, and a single scoring pass followed by verification. The 302-item human core carries the main empirical claims; the AI-assisted group is an additional public resource and does not alter or rescore the fixed D2 comparison.

The D2 release contains all 102 annotation-visible items and their final item labels: 57 `ADMISSIBLE` and 45 `REJECT`. Labels come from 85 A/B agreements and 17 human adjudications. See [the dataset schema](data/README.md) and [the D2 annotation guide](protocol/d2_annotation_guide.md).

Validate the released IDs, label counts, provenance counts, and evidence hashes with Python 3 (standard library only):

```bash
python src/export_d2_release.py
```

`src/run_d2_fixed_evaluation.py` preserves the historical evaluation runner. Its original execution requires the archived Stage2 resources, serialized models, and runtime layout; the cleaned release does not bundle those dependencies.

## Reproduce the reported diagnostics

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
| Eight-system evaluation | `results/d2_fixed_predictions.jsonl` | `results/d2_fixed_metrics.json`, `results/d2_aggregate_metrics.csv`; checked by `src/analyze_posthoc.py`. |
| Pipeline loss decomposition | Fixed D2 method outputs plus released labels | `results/pipeline_loss.csv`. |
| Threshold stability | `data/human/dev30_fixed_scores.jsonl`, `protocol/posthoc_analysis.md` | `results/threshold_stability.csv`, `results/posthoc_analysis.json`. |
| Public collection | `data/human/`, `data/ai/` | Group-level labels, provenance, and the collection manifest. |

The score release is an exact projection of saved outputs, not a rerun. `src/prepare_posthoc_release.py` documents the export and checks source identities; users reproducing the diagnostics need only the files already in this repository. DEV identifiers in the score view are release-local identifiers preserving archived row order; private DEV text and acquisition identifiers are not required by the analysis.

The versioned snapshot is `ipm-evaluation-v1`. The tag is anchored to a Git commit; no archive DOI is claimed. The manuscript's fixed D2 results and post-hoc analyses retain their documented evidence roles.

## Annotation groups

- `data/human/` contains the 102-item D2 challenge set, the P0/DEV30/EVAL60 calibration and diagnostic records, and the 200-item independently annotated extension. The 200-item extension was annotated by two people and adjudicated on 46 disagreements; its fused labels are 152 `ADMISSIBLE` and 48 `REJECT`.
- `data/ai/consensus_extension_518.jsonl` contains 518 items selected from an 800-item frozen candidate pool when two independent model passes produced the same label. The 282 disagreements remain in the private audit ledger and are not silently relabelled.
- `data/ai/ai_extension_300.jsonl` contains the earlier 300-item audited AI-assisted extension, with its item-level provenance. The public release keeps its audit record and uses it as an annotation-quality and resource-scale component.

## Data and ethics

The released JSONL views contain body text, UTC time, reply/quote/media flags, labels, and compact provenance fields matching the information shown during annotation. Direct source identifiers, author records, acquisition responses, model rationales, and private annotation sessions are not included. Text and metadata are preserved as displayed to annotators.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
