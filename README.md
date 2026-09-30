# Open-Web Event Admission / Calibration

This repository contains the reproducibility materials for the study **When Candidate Retrieval Is Not Admission: A Coverage-Aware Diagnostic Benchmark for Open-Web Event Organization**.

The repository is intentionally a **public-safe release**. It contains the evaluation code, paper source, frozen measurement contract, audit summary, and aggregate results. It does **not** contain raw Bluesky posts, annotator identities, A/B annotation packages, fused Gold labels, private overlap audits, model weights, restricted caches, or other material that may be private, licensed, or personally identifying.

## Repository layout

- `src/`: fixed evaluation runner used for the D2 evaluation.
- `protocol/`: measurement contract, evidence matrix, F3 audit report, and study overview.
- `results/`: aggregate, item-free metrics from the frozen D2 evaluation.
- `data/`: data-access and release-scope statement.

## Reproducibility status

The reported evaluation used a frozen 102-item challenge set, fixed thresholds selected on development material, and a single scoring pass followed by verification. Re-running the complete item-level evaluation requires restricted source packages and Gold labels that are not distributed in this public repository. The aggregate results are provided so that the paper's claims and tables can be checked without exposing raw social-media content.

## Data and ethics

The D2 items were collected from a public platform, but public availability does not by itself grant redistribution rights. Raw posts, URLs, annotator records, and label-level files are therefore withheld. A future release may provide an approved derived or access-controlled package after licensing, privacy, and venue requirements are checked.

## License

No license is granted for withheld raw data or third-party materials. Add an explicit software license before redistributing the code.
