# Earlier extension annotation protocol

This directory is retained at its historical path so that the earlier 300-item release remains reproducible. The public collection describes that material as the audited extension.

- `model_annotation_guide.md`: admission policy shown to both model annotators.
- `model_annotation_prompt.md`: task instructions used for each independent pass.
- `model_output_schema.json`: required model output schema.
- `human_review_guide.md`: policy used by the human reviewer.
- `human_review_prompt.md`: blinded review instructions.
- `human_output_schema.json`: required human-review output schema.
- `annotator_run_metadata.json`: model/product identifiers, run timestamps, package hashes, and overlap-audit scope.

The model annotators ran independently without access to one another's outputs. Human review covered all 28 model disagreements and a stratified sample of 60 agreement cases. Private rationales, full session records, and reviewer notes are not part of the public release.
