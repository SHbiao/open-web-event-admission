# D2 text-only admission annotation

## Visible evidence and task

Judge the displayed body, publication time, and reply, quote, and media flags. Do not open parent posts, links, images, or videos. Make the initial judgment independently, without AI translation, AI label recommendations, or discussion with the other annotator. Compare answers only after both annotators have completed the full package.

Choose exactly one label:

- **ADMISSIBLE**: the displayed text supports at least one qualified event organization target.
- **REJECT**: the displayed text does not meet that admission requirement. It may lack a target event, contain only background or general discussion, or omit essential referents, context, or media evidence.

REJECT means no admission on the available text. It does not assert that no event exists in the world. Insufficient evidence is not a separate primary label.

## Qualified organization target

At least one identifiable real-world occurrence, action, change, result, institutional act, or explicit event reference must be part of the body's main information. An item may contain multiple events.

Comments, replies, historical events, small events, and personal experiences can qualify. The event must contribute to the main information rather than serve only as an introduction, example, or background. Abstract opinions, general properties, generic advice, and commentary on fictional plots do not automatically constitute an event.

Complete dates, locations, all participants, and a knowledge-base page are not required. Incomplete details alone do not establish insufficient evidence. An explicit actual statement, arrangement, decision, or ongoing action may support admission. A wish or conditional discussion does not automatically establish that an action occurred; neither an `if` clause nor a question determines the label by itself.

Do not verify whether the author's claim is true or whether an event is already in the knowledge base. When the displayed body is sufficient, missing images or parent posts do not justify rejection. Choose REJECT when missing essential content prevents identification of an organization target.

## Annotation and fusion

Each annotator labels all 102 items and records prior exposure. There is no default label. Notes are optional, and a separate rejection subtype is not required. Display problems are reported instead of forcing a semantic label. First complete submissions are preserved before adjudication.

The A/B packages contain identical evidence in independently randomized orders. The first submissions agreed on 85/102 items (83.33%, Cohen's kappa 0.6612). Human C adjudication resolved all 17 disagreements. The final item labels contain 57 ADMISSIBLE and 45 REJECT items. C adjudication included reported Youdao translation assistance and was not a third independent blind annotation pass.

The released `gold_source` field distinguishes `AB_AGREEMENT` (85 items) from `C_ADJUDICATION` (17 items) for compatibility with the fixed evaluation files. Final labels and displayed evidence are in `data/d2_102.jsonl`.

## Collection and evaluation role

D2 was collected through Bluesky Public AppView `searchPosts` with 12 fixed English topic queries in the UTC window from 2026-09-22 inclusive to 2026-09-28 exclusive. The 108 selected records yielded 102 items after six internal duplicate exclusions. Historical overlap checks covered source IDs, normalized bodies, external URLs, near duplicates, and content clusters against 1,029 records.

D2 is the frozen challenge-confirmation layer for the eight-system comparison. It is a query-selected challenge set rather than a probability sample. The measurement and failure rules are specified in `protocol/F1_measurement_contract.md`; aggregate results are in `results/d2_aggregate_metrics.csv`.
