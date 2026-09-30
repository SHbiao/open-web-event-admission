# Open-Web Event Admission / Calibration

This repository contains the released benchmark data, annotation protocols, evaluation code, and aggregate results for **When Candidate Retrieval Is Not Admission: A Coverage-Aware Diagnostic Benchmark for Open-Web Event Organization**.

The benchmark suite contains 572 item-level examples across distinct evidence layers: 80 P0 calibration items, 30 development items, 60 controlled-diagnostic items, 102 challenge-confirmation items, and a 300-item audited Silver extension. These layers have different evidential roles and must not be treated as one homogeneous test set or a 572-item Gold set.

## Repository layout

- `src/`: fixed evaluation runner used for the D2 evaluation.
- `protocol/`: measurement contracts, study records, and the English Silver annotation protocols.
- `results/`: aggregate D2 metrics, the Silver audit report, and Silver quality-audit metrics.
- `data/`: P0 metadata, the cleaned 300-item Silver release, and item-level Silver provenance.

## Reproducibility status

The reported system evaluation used the frozen 102-item D2 challenge set, fixed thresholds selected on development material, and a single scoring pass followed by verification. The Silver extension is a separate scale and annotation-quality layer; it is not used to tune or rescore D2.

For the Silver tier, two independent models agreed on 272/300 items (90.67%, Cohen's kappa 0.8096). All 28 disagreements were human-adjudicated. A blinded human audit of 60 agreement cases confirmed 52/60: 30/30 consensus-ADMISSIBLE cases and 22/30 consensus-REJECT cases. The eight corrections all changed REJECT to ADMISSIBLE. The frozen release contains 140 ADMISSIBLE and 160 REJECT items.

## Data and ethics

`data/silver_300.jsonl` contains the cleaned view shown during annotation: body text, UTC time, reply/quote/media flags, the released label, and compact provenance fields. Direct source identifiers, author records, acquisition responses, model rationales, and private annotation sessions are not included. The D2 item texts and fused Gold remain outside this repository.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
