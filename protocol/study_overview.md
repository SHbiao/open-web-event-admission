# Study Overview: From Phenomenon Discovery to Experimental Conclusion

## Status

- Date: 2026-09-30
- Route: Open-Web Event Admission / Calibration
- Experimental status: F2 fixed evaluation completed; F3 audit passed; public 1K-scale collection released
- Manuscript type: coverage-aware evaluation framework / protocol paper

This document is the compact English record of the study. It reports completed evidence only and does not add experiments or alter frozen labels, thresholds, or outputs.

## 1. Phenomenon discovery

Conventional event linking usually assumes that an input already expresses an event mention. The system then grounds the mention to a knowledge-base event or returns a NIL-like outcome. Our initial EventLink-NYT audit exposed a different upstream case: a text can contain people, places, topics, or local actions without foregrounding an event that should enter an event-organization workflow.

The audit therefore separated three units:

- **mention**: a span supplied to an event linker;
- **target**: a retrieved knowledge-base candidate;
- **item**: the complete input on which an organization system must decide admission.

Candidate existence, target novelty, and item admission are not interchangeable. The operational `REJECT` state means “do not admit under the current evidence policy”; it does not mean that no real-world event exists and it is not identical to NEW/NIL-EVENT.

Stage1 reconstructed 639 unique released texts from 993 EventLink-NYT NIL mention rows. Its operational overlay contained 599 EVENT-DESCRIBABLE items and 40 REJECT items. The conditional estimate was 6.78% (finite-population interval 6.26–9.39%), and the 40 REJECT items corresponded to 62 original candidate mentions. This is a screened EventLink pool, not an estimate of natural Web prevalence.

The initial evidence established a reproducible admission phenomenon and a task-definition gap. It did not establish Web prevalence, complete LINK/NEW/REJECT labels, downstream deployment harm, universal threshold failure, or a general multimodal solution.

## 2. Benchmark task

Under the frozen `WEB-TEXT-ADMISSION-v2` policy, the benchmark asks whether an item should enter event organization:

- `ADMISSIBLE`: admit under the available evidence and policy;
- `REJECT`: do not admit under the available evidence and policy.

The measured chain is:

```text
item -> candidate extraction -> retrieval -> eligibility scoring -> item admission
```

Each stage can fail. The benchmark therefore keeps every item in the denominator and reports candidate coverage, parse/generation failures, Admission Retention, and REJECT false-acceptance rate (FAR), in addition to ranking metrics.

## 3. Data selection and evidence layers

### P0 task-unit calibration

P0 contains 80 items and 124 mentions: 39 YES, 39 NO, and 2 UNCERTAIN item labels. It tests whether mention, target, and item labels can be propagated across units. It is development evidence, not an independent system test and not a complete three-action linking set.

### DEV30 and EVAL60 controlled diagnostics

DEV30 supports development and threshold selection. EVAL60 (also called Web60) contains 60 items: 33 ADMISSIBLE and 27 REJECT. DEV30 and EVAL60 together contain 90 items. Recovery diagnostics and clean shallow controls reuse this same set and are not additional independent samples. EVAL60 is controlled diagnostic evidence, not prevalence data or an untouched test set.

### D2 challenge confirmation

D2 contains 102 new items collected through Bluesky Public AppView searchPosts between 2026-09-22 and 2026-09-28 UTC using 12 fixed English topic queries. Exact source IDs, normalized bodies, external URLs, near duplicates, and content clusters had zero overlap with the historical 1,029-record audit.

The A/B packages showed the same content in independently randomized order and exposed only text, time, and reply/quote/media metadata. They contained no labels, candidates, scores, model outputs, or recommendations. The first complete submissions agreed on 85/102 items (83.33%; Cohen's kappa .6612). Seventeen disagreements were adjudicated by a human C pass, yielding 57 ADMISSIBLE and 45 REJECT labels. Some adjudication used machine translation assistance; it was not a third independent annotator.

D2 is a controlled-calibration challenge set, not a probability sample, Web prevalence sample, or complete EXISTING/NEW/REJECT event-linking set.

### Audited extension

The extension contains 300 unique items: 158 previously unexposed legacy items and 142 items from a later temporal collection. Two independently run model annotators agreed on 272/300 labels (90.67%; Cohen's kappa .8096). A human reviewer adjudicated all 28 disagreements and blindly audited 60 agreement cases.

The agreement audit confirmed 52/60 labels. All 30 sampled consensus-ADMISSIBLE cases were confirmed; 22/30 sampled consensus-REJECT cases were confirmed, and the other eight were corrected to ADMISSIBLE. The public release therefore contains 140 ADMISSIBLE and 160 REJECT items, with model and human provenance recorded in the accompanying manifest.

Across P0, DEV30, EVAL60, D2, and the extensions, the suite contains 1,290 item-level records. This 1K-scale total is a layered benchmark collection; each layer retains its construction and evaluation role.

### Materials that are not pooled into the test set

The earlier capped 300-item retrieval pool was not itself a fully labeled independent test set. The 300-item audited extension is a separately constructed and frozen resource, although 158 of its items come from the previously unexposed legacy pool. Historical mention-level labels (including the 1,762 legacy mention rows) are not equivalent to item-level admission labels. P0, DEV/EVAL, D2, and the extensions serve different roles and should remain identifiable when results are reported.

### Additional public extensions

The public collection also includes a 518-item extension selected from an 800-item frozen candidate pool when two independent model passes produced the same item label; the 282 disagreements remain in the private audit ledger. A separate 200-item extension was annotated independently by two people, with 46 disagreements adjudicated, yielding 152 ADMISSIBLE and 48 REJECT labels. Together with the earlier layers, these releases contain 1,290 item-level records. The added records expand resource scale and annotation analysis without changing the fixed D2 system comparison.

## 4. Frozen experimental protocol

The one-pass D2 evaluation included BM25 top-1, BGE top-1, validity, direct admission, clean linear, clean RBF, the original exact-existing joint-linear Primary system, and an admit-all reference. Thresholds and model choices came from development material; D2 labels were not used for model, prompt, feature, threshold, or hyperparameter selection.

Every D2 item remained in the audit denominator. Missing candidates, invalid spans, invalid JSON, missing scores, and abstentions were retained as named states; no zero or sentinel score replaced missing data.

Primary metrics were score coverage, candidate coverage, Admission Retention, REJECT FAR, full-set ROC-AUC/AUPRC when coverage was 102/102, and frozen 2,000-draw paired bootstrap intervals. Intervals are conditional on the challenge set.

## 5. Controlled diagnostic results

On the controlled DEV30/EVAL60 material, the original EVAL60 AUCs were BM25 .7632, BGE .5466, validity .7357, direct admission .7469, joint linear .7969, and joint RBF .8058. Joint linear retained 19/33 ADMISSIBLE items and falsely admitted 3/27 REJECT items at its frozen operating point. These are controlled diagnostics, not independent confirmation results.

## 6. D2 fixed evaluation results

| Method | Score coverage | Retained / 57 | False admitted / 45 | ROC-AUC / AUPRC |
|---|---:|---:|---:|---|
| Admit-all reference | 102/102 | 57 | 45 | .500 / .559 |
| BM25 top-1 | 101/102 | 53 | 27 | full NA; conditional .741 / .747 |
| BGE top-1 | 101/102 | 55 | 40 | full NA; conditional .672 / .723 |
| Validity | 79/102 | 44 | 13 | full NA; conditional .870 / .894 |
| Direct admission | 102/102 | 46 | 10 | .868 / .902 |
| Clean linear | 102/102 | 39 | 24 | .526 / .546 |
| Clean RBF | 102/102 | 35 | 9 | .793 / .831 |
| Primary joint linear | 79/102 | 40 | 10 | full NA; conditional .770 / .822 |

Primary had 79 valid scores, 16 NO_CANDIDATE items, 4 INVALID_SPANS items, and 3 INVALID_JSON items. Thus 23/102 items failed before a complete Primary score existed. Its full-set AUC/AUPRC are `NA_NOT_FULL_COVERAGE`; conditional values are diagnostics only.

At the same observed 10/45 REJECT false admissions, Direct admission retained 46/57 ADMISSIBLE items while Primary retained 40/57. The paired difference interval crossed zero, so the result does not establish a statistically confirmed overall advantage for Direct admission. The safe finding is that the frozen joint signal did not establish a general advantage over direct admission on the new time window.

## 7. F3 audit

F3 independently rechecked 102/102 unique IDs, the 57/45 class denominators, all eight methods, curves, bootstrap intervals, and the recorded input/output hashes. All values reproduced exactly. The post-scoring read-only label hash registration exceeded the strict score-only access boundary, but did not parse labels, modify predictions/configuration, or rerun scoring; it is recorded as a protocol deviation.

## 8. Final contribution and conclusion

The defensible contribution is a diagnostic Open-Web Event Admission / Calibration benchmark with:

1. an item/target/mention task definition;
2. a measurement contract separating extraction, retrieval, eligibility, and admission;
3. coverage-aware metrics that retain failures in the denominator;
4. a 1K-scale evidence collection separating development, controlled diagnostics, challenge confirmation, and public extensions;
5. a 300-item extension whose audit exposes asymmetric reliability between consensus ADMISSIBLE and consensus REJECT labels;
6. empirical diagnosis of candidate-admission mismatch, threshold transfer, and measurement-chain failure.

The evaluation does not support a complete three-action event-linking benchmark, Web prevalence, deployment impact, or universal superiority of the Primary model. It supports the narrower conclusion that candidate retrieval is not equivalent to item admission, and that coverage and calibration must be measured as part of the downstream decision.
