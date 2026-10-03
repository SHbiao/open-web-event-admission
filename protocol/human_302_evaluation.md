# Human-302 fixed evaluation

The primary evaluation consists of 302 human-annotated items (209 ADMISSIBLE, 93 REJECT): the original 102-item challenge cohort and a 200-item extension drawn from storyline-organized source material. Two independent annotators labeled each cohort, and a human adjudicator resolved disagreements. The public data retain cohort provenance and the displayed evidence.

The 200-item inference used the same Qwen2.5-7B-Instruct configuration, BM25 catalog, BGE reranker, feature definitions, serialized classifiers, and DEV-selected thresholds as the original evaluation. Only resource paths and input-count checks were adapted. Predictions consumed no label fields. The original 102 predictions were reused unchanged and concatenated with the 200 new predictions after inference. No model, prompt, feature, or threshold was chosen from the 302 labels.

All 302 IDs remain in Coverage. Admission Retention uses 209 admissible items and Reject FAR uses 93 Reject items. A missing score produces non-admission. Full-set AUC/AUPRC require complete score coverage; otherwise the available-score metrics are explicitly conditional. AUPRC is average precision.

Primary's 47 unscored cases consist of 18 NO_CANDIDATE, 12 INVALID_SPANS, and 17 INVALID_JSON method states. Their reference-class breakdown is in `results/human_302/pipeline_loss.csv`. Generator warnings with a usable final method score remain scored.

The pooled uncertainty calculation retains 2,000 paired, class-stratified bootstrap draws (seed 20260928), using original URL/body cluster keys for the first cohort and displayed-evidence keys for the extension. These intervals characterize the sampled collection; they do not add storyline-level clustering.

The post-hoc threshold analysis applies the existing DEV rule and the same bootstrap schedule as the earlier analysis: 12 positive and 18 negative development scores; 2,000 stratified draws with Python `random.Random(20260930)`; plus leave-one-out deletion of each DEV row. The resulting thresholds are applied only diagnostically to saved 302-item scores. No diagnostic threshold replaces a published operating point. Reported percentile ranges describe sensitivity conditional on fitted scores.

## Reproduction

```bash
python src/analyze_human_302.py --check
```

The independent standard-library implementation verifies the saved eight-system decisions and ranking metrics, then reproduces the loss and threshold diagnostics. Input labels remain in their existing human data files; the joined evaluation does not create additional dataset records. The source-prediction manifest is `results/human_302/manifest.json`.
