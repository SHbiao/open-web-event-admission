# Collection and annotation provenance

This supplement retains the collection and annotation details underlying the concise manuscript dataset description. The public collection contains 1,290 records: 472 human-annotated records (302 primary evaluation, 170 calibration/development) and 818 AI-assisted extension records.

## Human evaluation

The evaluation includes 102 posts collected through Bluesky Public AppView searchPosts between 2026-09-22 and 2026-09-28 UTC using twelve English topic queries, and 200 posts selected from storyline-organized source material. Both parts use the same admission policy, independent A/B annotation, and human resolution of disagreements. Annotators saw displayed text and metadata without model outputs.

| Source subset | Items | Raw A/B agreement | Cohen's kappa | Adjudicated disagreements | Final Admissible | Final Reject |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Original challenge | 102 | 85/102 (83.33%) | 0.6612 | 17 | 57 | 45 |
| Human extension | 200 | 154/200 (77.00%) | 0.3635 | 46 | 152 | 48 |
| Combined evaluation | 302 | 239/302 (79.14%) | Not computed here | 63 | 209 | 93 |

The combined raw agreement is calculated from the two agreement counts. The subset kappa values are not averaged to produce a pooled kappa. Final labels preserve 239 agreements and 63 adjudicated decisions. Data files are `data/human/d2_102.jsonl`, `data/human/human_extension_200.jsonl`, and the extension provenance file.

## Earlier AI-assisted extension: 300 records

Two models agreed on 272/300 labels (90.67%; Cohen's kappa 0.8096). All 28 disagreements were human-adjudicated. A stratified audit reviewed 60 agreements, equally divided by the model-consensus class, before human correction:

| Audit stratum | Agreement with human judgment |
| --- | ---: |
| Consensus Admissible | 30/30 (100%) |
| Consensus Reject | 22/30 (73.33%) |
| Total sampled agreements | 52/60 (86.67%) |

Eight consensus-Reject items were corrected to Admissible. The resulting extension contains 140 Admissible and 160 Reject items. Of the 300 records, 88 received direct human review (28 disagreements plus 60 sampled agreements); 212 retain model-consensus labels. This audit shows class-asymmetric reliability within the sampled agreements.

## Later AI-assisted extension: 518 records

Two independent model passes labeled 800 candidates. They agreed on 518/800 (64.75%; Cohen's kappa 0.2378). The agreement subset contains 415 consensus-Admissible and 103 consensus-Reject items. The 282 disagreements were not included in this extension.

A single human reviewer blindly audited 50 consensus items, sampling 25 per class. Final audit judgments matched 40/50 model-consensus labels (80%): 21/25 in the Admissible stratum and 19/25 in the Reject stratum. Four consensus-Admissible items were judged Reject and six consensus-Reject items were judged Admissible. The equal allocation across classes differs from the class proportions of the 518-item pool, so 40/50 is the unweighted agreement of the audit sample, not a population-weighted estimate.

These extensions provide auxiliary observations and future benchmark resources. Review and selection provenance are retained so that users can distinguish model-consensus and human-reviewed records.

## Evaluation execution record

The original 102-item predictions remain unchanged. The 200-item extension used the same models, prompts, features, and DEV-selected thresholds. Inference consumed displayed evidence without labels. Path and input-count checks were adapted for the extension. The original execution also recorded a read-only reference-label hash check after scoring that exceeded its strict score-only access boundary; that check parsed no labels, changed no prediction, and triggered no rescoring.

The 302-item metrics and descriptive threshold diagnostics are independently reproducible using `python src/analyze_human_302.py --check`. Models and the reported operating points are not reselected by these analyses.
