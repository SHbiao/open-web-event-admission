# F3 Fixed-Evaluation Audit

- Task: `F3-AUDIT-20260929-v1`
- Status: `F3_AUDIT_PASS`
- Scope: read-only recomputation of the existing F2 blind predictions, scoring audit, fixed metrics, curves, bootstrap intervals, and recorded hashes.
- Evidence level: D2 is a controlled-calibration challenge/confirmation set; it is not a probability sample, independent third-party Gold, or complete three-action linking test.

## Completeness and denominators

The prediction file contains 102 rows and 102 unique item IDs. The fixed class denominators are 57 ADMISSIBLE and 45 REJECT. Every method keeps all 102 items in the audit denominator; missing scores and failures are not removed.

Primary candidate coverage is 79/102. There are 23 NO_CANDIDATE items and 9 parse failures (6 `INVALID_SPANS`, 3 `INVALID_JSON`). Generation, retrieval, and reranking failures are zero. Primary has 79 `OK`, 16 `NO_CANDIDATE`, 4 `INVALID_SPANS`, and 3 `INVALID_JSON` statuses. Coverage and failure categories are not mutually exclusive partitions.

## Independent recomputation

The audit recomputed coverage, decision counts, ROC-AUC, AUPRC, all Retention--FAR curves, and the frozen paired bootstrap from the existing F2 artifacts. The maximum absolute metric error was zero. The bootstrap used the frozen Gold stratification, content clusters, seed `20260928`, 2,000 draws, and the preregistered statistic order; all eight methods matched the F2 intervals.

| Frozen method | Score coverage | Retained / 57 | False admitted / 45 | Full ROC-AUC | Full AUPRC |
|---|---:|---:|---:|---:|---:|
| Admit-all | 102/102 | 57 | 45 | .5000 | .5588 |
| BM25 top-1 | 101/102 | 53 | 27 | NA | NA |
| BGE top-1 | 101/102 | 55 | 40 | NA | NA |
| Validity | 79/102 | 44 | 13 | NA | NA |
| Direct admission | 102/102 | 46 | 10 | .8680 | .9024 |
| Clean linear | 102/102 | 39 | 24 | .5263 | .5460 |
| Clean RBF | 102/102 | 35 | 9 | .7930 | .8308 |
| Primary joint linear | 79/102 | 40 | 10 | NA | NA |

Primary's conditional scores cover 79 rows (50 ADMISSIBLE and 29 REJECT), with conditional ROC-AUC .7697 and AUPRC .8222. They must not be reported as 102-row full-set metrics; full-set values are `NA_NOT_FULL_COVERAGE`.

The paired bootstrap intervals are: Primary Retention [.5789, .8246] and FAR [.1111, .3556]; Direct Retention [.7018, .9123] and FAR [.1111, .3333]; Clean RBF Retention [.4912, .7368] and FAR [.0889, .3111]. Direct minus Primary Retention is +6/57 with 95% CI [-2/57, 14/57], and FAR difference is 0/45 with CI [-7/45, 7/45]. All method differences cross zero.

## Protocol deviation

F2 blind prediction was completed before scoring and Gold access. After scoring, a read-only Gold SHA-256 recomputation was performed during hash registration, exceeding the strict score-only access boundary. The record shows no label parsing, prediction/configuration change, or scoring rerun. This deviation is disclosed and does not change the F2 values.

## Scientific boundary

On this frozen D2 set, Primary did not establish an advantage over direct admission. Direct retained six additional ADMISSIBLE items at the same observed 10/45 false admissions and had complete coverage, but its paired interval crossed zero. The result does not establish Web prevalence, deployment harm, complete NEW/EXISTING/REJECT linking, or the necessity of a dedicated admission model.

F3 is complete. No new experiments, labels, thresholds, model runs, or repairs were authorized.
