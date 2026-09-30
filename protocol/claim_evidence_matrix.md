# Claim--Evidence Matrix

This matrix records the claims supported by the public release. It does not add results or upgrade evidence levels.

| ID | Claim | Evidence and denominator | Evidence level | Permitted interpretation |
|---|---|---|---|---|
| C0 | Mention eventness, item admission, and target alignment cannot be propagated directly across units. | P0: 80 items, 124 mentions; item labels 39 YES / 39 NO / 2 UNCERTAIN; 43 aligned mentions used for the two-axis comparison. | Development | Task-unit calibration only; not independent performance or NEW Gold. |
| C1 | Candidate extraction is not sufficient to determine item admission. | EVAL60/Web60: 60 items, 33 ADMISSIBLE / 27 REJECT; candidate and validity funnel recorded. | Controlled diagnostic | Candidate hits are not eligible-target coverage and not Web prevalence. |
| C2 | Retrieval and semantic signals show limited predictive value in controlled diagnostics. | EVAL60 AUC: BM25 .7632, BGE .5466, validity .7357, direct .7469, joint linear .7969, joint RBF .8058. | Controlled diagnostic | Development-stage signal behavior only; not independent confirmation. |
| C3 | DEV operating points exhibit a Retention--FAR transfer problem. | DEV30: 12/18; EVAL60: 33/27; thresholds selected on DEV and evaluated on fixed EVAL. | Controlled diagnostic | Report conditional trade-offs; do not claim deployment safety or universal instability. |
| C4 | Candidate and parsing coverage are part of admission measurement. | D2 Primary: 79/102 valid scores; 16 NO_CANDIDATE, 4 INVALID_SPANS, 3 INVALID_JSON. | Challenge confirmation | Failures remain in the denominator; conditional AUC is not full-set performance. |
| C5 | Primary did not establish an advantage over direct admission on D2. | D2: Primary 79/102, 40/57 retained, 10/45 false admitted; Direct 102/102, 46/57, 10/45. | Challenge confirmation | Paired interval crosses zero; do not claim Direct has a confirmed universal advantage. |
| C6 | Dual-model agreement is high in the Silver tier, but agreement quality is asymmetric by class. | Silver: 272/300 model agreement, kappa .8096; all 28 disagreements human-adjudicated; agreement audit 52/60 overall, 30/30 consensus ADMISSIBLE and 22/30 consensus REJECT. | Audited Silver | Supports scalable extension and annotation-quality analysis; the 300 items are not human Gold. |
| C7 | The protocol does not establish full EXISTING/NEW/REJECT linking, Web prevalence, deployment impact, or model necessity. | D2 is a 102-item controlled-calibration challenge set, not a probability sample and not complete three-action Gold. | Scope boundary | These are outside the current paper and require a separate study. |

## Evidence reading rules

`Development` material defines the task or supports model/threshold decisions. `Controlled diagnostic` material contains development or adjudication contact and supports protocol diagnosis rather than untouched generalization. `Challenge confirmation` is the frozen D2 evaluation on a non-overlapping new time window; it is not a probability sample. `Audited Silver` extends scale with dual-model consensus, complete human adjudication of disagreements, and a stratified agreement audit. The 572-item total is a layered suite, not one homogeneous Gold pool.

## Public release mapping

- Study narrative: `study_overview.md`
- Measurement contract: `F1_measurement_contract.md`
- Fixed evaluation audit: `F3_audit_report_20260929.md`
- Aggregate metrics: `../results/d2_aggregate_metrics.csv`
- Silver dataset: `../data/silver_300.jsonl`
- Silver provenance: `../data/silver_300_provenance.jsonl`
- Silver audit metrics: `../results/silver_quality_metrics.json`
