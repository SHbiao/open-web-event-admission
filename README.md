# Open-Web Event Admission / Calibration

This repository contains the released benchmark data, annotation protocols, evaluation code, and aggregate results for **When Candidate Retrieval Is Not Admission: A Coverage-Aware Diagnostic Benchmark for Open-Web Event Organization**.

The benchmark suite contains 572 item-level examples across distinct evidence layers: 80 P0 calibration items, 30 development items, 60 controlled-diagnostic items, 102 challenge-confirmation items, and a 300-item audited Silver extension. These layers have different evidential roles and must not be treated as one homogeneous test set or a 572-item Gold set.

## Repository layout

- `src/`: fixed evaluation runner used for the D2 evaluation.
- `protocol/`: measurement contracts, study records, and English D2 and Silver annotation protocols.
- `results/`: aggregate D2 metrics, the Silver audit report, and Silver quality-audit metrics.
- `data/`: P0 metadata, the 102-item D2 challenge set with human Gold labels, the cleaned 300-item Silver release, and item-level Silver provenance.

## Reproducibility status

The reported system evaluation used the frozen 102-item D2 challenge set, fixed thresholds selected on development material, and a single scoring pass followed by verification. The Silver extension is a separate scale and annotation-quality layer; it is not used to tune or rescore D2.

The public D2 release contains all 102 annotation-visible items and their frozen final Gold labels: 57 ADMISSIBLE and 45 REJECT. Labels come from 85 A/B agreements and 17 human adjudications. See [the dataset schema](data/README.md) and [the D2 annotation guide](protocol/d2_annotation_guide.md).

Validate the released IDs, label counts, provenance counts, and evidence hashes with Python 3 (standard library only):

```bash
python src/export_d2_release.py
```

`src/run_d2_fixed_evaluation.py` preserves the historical evaluation runner. Its original execution requires the archived Stage2 resources, serialized models, and runtime layout; releasing the cleaned D2 data does not bundle those dependencies.

For the Silver tier, two independent models agreed on 272/300 items (90.67%, Cohen's kappa 0.8096). All 28 disagreements were human-adjudicated. A blinded human audit of 60 agreement cases confirmed 52/60: 30/30 consensus-ADMISSIBLE cases and 22/30 consensus-REJECT cases. The eight corrections all changed REJECT to ADMISSIBLE. The frozen release contains 140 ADMISSIBLE and 160 REJECT items.

## Data and ethics

`data/d2_102.jsonl` and `data/silver_300.jsonl` contain the cleaned views shown during annotation: body text, UTC time, reply/quote/media flags, the released labels, and compact provenance fields. D2 retains human Gold labels; the extension remains audited Silver. Direct source identifiers, author records, acquisition responses, model rationales, and private annotation sessions are not included. Text and metadata are preserved as displayed to annotators.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
