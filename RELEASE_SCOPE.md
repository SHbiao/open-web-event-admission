# Public release scope and exclusions

This file is a release gate, not a scientific result.

## Included

- fixed evaluation runner source;
- measurement contract and F3 audit report;
- claim/evidence matrix and study overview;
- item-free D2 aggregate metrics;
- all 102 cleaned D2 annotation-visible items, final human Gold labels, and agreement/adjudication provenance;
- cleaned 300-item Silver dataset and item-level provenance;
- English D2 human-annotation, Silver model-annotation, and Silver human-review protocols;
- aggregate Silver quality-audit metrics.

## Excluded

- direct source IDs, author records, acquisition payloads, and media files;
- private A/B session records, individual annotator answers, and C adjudication notes;
- model rationales, private annotation sessions, and human review notes;
- private overlap and acquisition manifests;
- restricted model weights, knowledge-base snapshots, runtime caches, and secrets;
- generated PDFs, logs, temporary previews, and local environment files.

The D2 and Silver JSONL files preserve the cleaned text-and-metadata views used for annotation. D2 final Gold labels are public in `data/d2_102.jsonl`; the richer internal fusion file and its private annotation records remain archived. The releases retain their separate challenge-confirmation and audited Silver evidence roles.
