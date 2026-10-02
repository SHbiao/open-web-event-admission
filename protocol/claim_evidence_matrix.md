# Claim--Evidence Matrix

This matrix records the claims supported by the public release. It does not add results or upgrade evidence levels.

| ID | Claim | Evidence and denominator | Evidence level | Permitted interpretation |
|---|---|---|---|---|
| C0 | Mention eventness, item admission, and target alignment cannot be propagated directly across units. | P0: 80 items, 124 mentions; item labels 39 YES / 39 NO / 2 UNCERTAIN; 43 aligned mentions used for the two-axis comparison. | Development | Task-unit calibration only; not independent system performance. |
| C1 | Candidate extraction is not sufficient to determine item admission. | EVAL60/Web60: 60 items, 33 ADMISSIBLE / 27 REJECT; candidate and validity funnel recorded. | Controlled diagnostic | Candidate hits are not eligible-target coverage and not Web prevalence. |
| C2 | Retrieval and semantic signals show limited predictive value in controlled diagnostics. | EVAL60 AUC: BM25 0.7632, BGE 0.5466, validity 0.7357, direct 0.7469, joint linear 0.7969, joint RBF 0.8058. | Controlled diagnostic | Development-stage signal behavior only; not independent confirmation. |
| C3 | DEV operating points exhibit a Retention--FAR transfer problem. | DEV30: 12/18; EVAL60: 33/27; thresholds selected on DEV and evaluated on fixed EVAL. | Controlled diagnostic | Report conditional trade-offs; do not claim deployment safety or universal instability. |
| C4 | Candidate and parsing coverage are part of admission measurement. | D2 Primary: 79/102 valid scores; 16 NO_CANDIDATE, 4 INVALID_SPANS, 3 INVALID_JSON. | Challenge confirmation | Failures remain in the denominator; conditional AUC is not full-set performance. |
| C5 | Primary did not establish an advantage over direct admission on D2. | D2: Primary 79/102, 40/57 retained, 10/45 false admitted; Direct 102/102, 46/57, 10/45. | Challenge confirmation | Paired interval crosses zero; do not claim Direct has a confirmed universal advantage. |
| C6 | Dual-model agreement is high in one AI-assisted extension, but agreement quality is asymmetric by class. | Earlier 300-item AI-assisted extension: 272/300 model agreement, kappa 0.8096; all 28 disagreements human-adjudicated; agreement audit 52/60 overall, 30/30 consensus ADMISSIBLE and 22/30 consensus REJECT. | AI-group annotation analysis | Supports scalable extension and annotation-quality analysis; provenance remains explicit. |
| C7 | The protocol does not establish full EXISTING/NEW/REJECT linking, Web prevalence, deployment impact, or model necessity. | D2 is a 102-item controlled-calibration challenge set, not a probability sample and not complete three-action linking. | Scope boundary | These are outside the current paper and require a separate study. |

## Evidence reading rules

`Development` material defines the task or supports model/threshold decisions. `Controlled diagnostic` material contains development or adjudication contact and supports protocol diagnosis rather than untouched generalization. `Challenge confirmation` is the frozen D2 evaluation on a non-overlapping new time window; it is not a probability sample. The 1,290-item collection is organized into a human group and an AI-assisted group, with provenance and disagreement records retained.

## Public release mapping

- Study narrative: `study_overview.md`
- Measurement contract: `F1_measurement_contract.md`
- Fixed evaluation audit: `F3_audit_report_20260929.md`
- Aggregate metrics: `../results/d2_aggregate_metrics.csv`
- Human evidence core and extension: `../data/human/d2_102.jsonl`, `../data/human/human_extension_200.jsonl`
- AI-assisted extensions: `../data/ai/ai_extension_300.jsonl`, `../data/ai/consensus_extension_518.jsonl`
- AI-group audit metrics: `../results/ai_annotation_quality_metrics.json`
