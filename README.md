# Open-Web Event Admission / Calibration

This repository contains the released benchmark data, annotation protocols, evaluation code, and results for **When Candidate Retrieval Is Not Admission: A Coverage-Aware Evaluation Framework for Open-Web Event Organization**.

The benchmark suite contains 572 item-level examples across distinct evidence layers: 80 P0 calibration items, 30 development items, 60 controlled-diagnostic items, 102 challenge-confirmation items, and a 300-item audited Silver extension. These layers have different evidential roles and must not be treated as one homogeneous test set or a 572-item Gold set.

## Repository layout

- `src/`: fixed evaluation runner used for the D2 evaluation.
- `protocol/`: measurement contracts, study records, and English D2 and Silver annotation protocols.
- `results/`: fixed D2 scores and metrics, descriptive post-hoc diagnostics, and Silver quality-audit results.
- `data/`: P0 metadata, the 102-item D2 challenge set with human Gold labels, the cleaned 300-item Silver release, and item-level Silver provenance.

## Reproducibility status

The reported system evaluation used the frozen 102-item D2 challenge set, fixed thresholds selected on development material, and a single scoring pass followed by verification. The Silver extension is a separate scale and annotation-quality layer; it is not used to tune or rescore D2.

The public D2 release contains all 102 annotation-visible items and their frozen final Gold labels: 57 ADMISSIBLE and 45 REJECT. Labels come from 85 A/B agreements and 17 human adjudications. See [the dataset schema](data/README.md) and [the D2 annotation guide](protocol/d2_annotation_guide.md).

Validate the released IDs, label counts, provenance counts, and evidence hashes with Python 3 (standard library only):

```bash
python src/export_d2_release.py
```

`src/run_d2_fixed_evaluation.py` preserves the historical evaluation runner. Its original execution requires the archived Stage2 resources, serialized models, and runtime layout; releasing the cleaned D2 data does not bundle those dependencies.

## Reproduce the reported diagnostics

The IPM revision adds descriptive analysis of existing outputs, with no inference, model refitting, or replacement of the original thresholds. Reproduce it with Python 3.9 or later and no third-party packages:

```bash
python src/analyze_posthoc.py --check
```

This checks all eight saved fixed operating points and AUC/AUPRC values, then reproduces the class-by-stage loss decomposition, 2,000 DEV-score bootstrap draws, and leave-one-out threshold diagnostics. Running without `--check` regenerates the three post-hoc result files. Resampling intervals describe sensitivity of the saved fitted scores; they are not population-performance confidence intervals or newly selected operating points.

| Manuscript component | Released input / configuration | Reproduction or output |
| --- | --- | --- |
| Item policy and D2 Gold | `data/d2_102.jsonl`, `protocol/d2_annotation_guide.md` | `src/export_d2_release.py` validates IDs, labels, and evidence hashes. |
| Exact semantic prompts | `protocol/fixed_model_prompts.json` | Extractor, validity, salience, and admission templates from the archived protocol. |
| Fixed thresholds and resource identity | `protocol/posthoc_input_manifest.json` | Original prediction, calibration, prompt, model, and catalog hashes; saved DEV and D2 split IDs. |
| Eight-system evaluation | `results/d2_fixed_predictions.jsonl` | `results/d2_fixed_metrics.json`, `results/d2_aggregate_metrics.csv`; checked by `src/analyze_posthoc.py`. |
| Pipeline loss decomposition | Fixed D2 method outputs plus released Gold | `results/pipeline_loss.csv`. |
| Threshold stability | `data/dev30_fixed_scores.jsonl`, `protocol/posthoc_analysis.md` | `results/threshold_stability.csv`, `results/posthoc_analysis.json`. |
| Audited Silver | `data/silver_300.jsonl`, `data/silver_300_provenance.jsonl`, `protocol/silver/` | `results/silver_quality_metrics.json`, `results/silver_audit_report.md`. |

The score release is an exact projection of saved outputs, not a rerun. `src/prepare_posthoc_release.py` documents the export and checks source identities; users reproducing the diagnostics need only the files already in this repository. DEV identifiers in the score view are release-local identifiers preserving archived row order; private DEV text and acquisition identifiers are not required by the analysis.

The versioned snapshot is `ipm-evaluation-v1`. The tag is anchored to a Git commit; no archive DOI is claimed. The manuscript's original D2 results and the new post-hoc analyses retain separate evidence status.

For the Silver tier, two independent models agreed on 272/300 items (90.67%, Cohen's kappa 0.8096). All 28 disagreements were human-adjudicated. A blinded human audit of 60 agreement cases confirmed 52/60: 30/30 consensus-ADMISSIBLE cases and 22/30 consensus-REJECT cases. The eight corrections all changed REJECT to ADMISSIBLE. The frozen release contains 140 ADMISSIBLE and 160 REJECT items.

## Data and ethics

`data/d2_102.jsonl` and `data/silver_300.jsonl` contain the cleaned views shown during annotation: body text, UTC time, reply/quote/media flags, the released labels, and compact provenance fields. D2 retains human Gold labels; the extension remains audited Silver. Direct source identifiers, author records, acquisition responses, model rationales, and private annotation sessions are not included. Text and metadata are preserved as displayed to annotators.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
