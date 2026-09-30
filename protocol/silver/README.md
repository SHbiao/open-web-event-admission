# Silver annotation protocol

The 300-item Silver extension used two independent model-annotation passes followed by blinded human review.

- `model_annotation_guide.md`: frozen admission policy shown to both model annotators.
- `model_annotation_prompt.md`: task instructions used for each independent 300-item pass.
- `model_output_schema.json`: required model output schema.
- `human_review_guide.md`: simplified policy used by the human reviewer.
- `human_review_prompt.md`: blinded review instructions.
- `human_output_schema.json`: required human-review output schema.

The model annotators were Codex with GPT-6 and Claude Code with Claude Opus 5. Neither pass had access to the other's output. Human review covered all 28 disagreements and a stratified sample of 60 agreement cases. Private rationales, session records, and reviewer notes are not part of the public release.
