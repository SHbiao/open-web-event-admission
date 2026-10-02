# Annotation Task

Work only inside this package. Do not inspect the sibling annotator package, `private/`, prior labels, model scores, or project result files.

1. Read `GUIDELINE.md` and `OUTPUT_SCHEMA.json` completely.
2. Label every item in `batches/batch_01.jsonl` through `batch_06.jsonl`, in package order.
3. Do not browse, open URLs, inspect parent posts, or use the other annotator's outputs.
4. Write exactly one JSON object per item to `annotations.jsonl`; produce no labels anywhere else.
5. Each item ID must occur exactly once. Allowed labels are `ADMISSIBLE` and `REJECT`; allowed clause codes are `A1`, `A2`, `R1`, `R2`, and `R3`.
6. Use a short evidence span and a reason of at most 40 words. Do not provide chain-of-thought.
7. Write `session.json` with the exact model/product name, model version if exposed, annotator role, start/end UTC times, item count, and whether any external assistance was used.
8. Validate that all 300 IDs are present before stopping. Do not compare results or adjudicate disagreements.
