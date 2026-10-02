# Post-hoc pipeline and operating-point diagnostics

Defined on 2026-09-30, after the fixed D2 evaluation. These descriptive analyses do not alter a D2 prediction or select a replacement model, feature, prompt, or operating point.

## Inputs and scope

- The 102 released D2 labels and exact saved per-method scores, statuses, thresholds, and decisions.
- The 30 archived development labels and saved scores for Primary joint linear, Direct admission, and Validity. These three pre-specified paths contrast joint candidate dependence, direct item-level scoring, and a high-discrimination candidate signal.
- Trained models and score directions remain fixed. There is no inference, refitting, hyperparameter search, or D2-based threshold choice.

## Pipeline loss decomposition

For Primary joint linear, cross-tabulate the saved score status by reference class. Partition each class into unavailable score, scored but not admitted, and scored and admitted. Resolve unavailable scores into NO_CANDIDATE, INVALID_SPANS, and INVALID_JSON using the saved method status. Partial extraction warnings that still yield a legal score are not counted as unavailable.

## Threshold stability

Reapply the original rule to saved DEV scores: the highest threshold retaining at least 90% of the positive development items. On the original 12 positives this is the second-lowest positive score (11/12 retained, or more if tied).

1. Delete each of the 30 development rows in turn, recalculate the threshold, and apply it to the unchanged D2 scores. Report the complete leave-one-out ranges.
2. Draw 2,000 stratified bootstrap development samples with replacement (12 positives and 18 negatives per draw), using Python `random.Random(20260930)` and a common draw schedule for all three methods. Recalculate the threshold and apply it to D2. Missing D2 scores remain non-admissions at every diagnostic threshold.
3. Report empirical 2.5th, 50th, and 97.5th percentiles using linear interpolation. These are descriptive resampling ranges, not confidence intervals for population performance. No diagnostic threshold replaces a published operating point.

Negative DEV scores do not determine this positive-retention threshold; sampling them preserves the original class sizes and makes that property explicit. The analysis is conditional on the trained models and saved DEV scores. It does not estimate uncertainty from model fitting or the causal share of temporal degradation attributable to threshold estimation. The archived development scoring convention is preserved; D2 missing scores are never replaced with numeric sentinels.

## Reproduction

Run `python src/analyze_posthoc.py` from the repository root. It uses the Python standard library and the released data, without local model weights or acquisition caches. Run `python src/analyze_posthoc.py --check` to recompute and compare against the released results without rewriting them.

Outputs are `results/posthoc_analysis.json`, `results/pipeline_loss.csv`, and `results/threshold_stability.csv`. The fixed eight-method results remain in `results/d2_aggregate_metrics.csv` and are checked against the saved decisions during analysis.
