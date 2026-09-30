# Public release scope and exclusions

This file is a release gate, not a scientific result.

## Included

- fixed evaluation runner source;
- measurement contract and F3 audit report;
- claim/evidence matrix and study overview;
- item-free D2 aggregate metrics;
- cleaned 300-item Silver dataset and item-level provenance;
- English model-annotation and human-review protocols;
- aggregate Silver quality-audit metrics.

## Excluded

- D2 item text, direct source IDs, author records, acquisition payloads, and media files;
- A/B packages, annotator answers, C adjudication records, and fused Gold;
- model rationales, private annotation sessions, and human review notes;
- private overlap and acquisition manifests;
- restricted model weights, knowledge-base snapshots, runtime caches, and secrets;
- generated PDFs, logs, temporary previews, and local environment files.

The released Silver JSONL is the cleaned text-and-metadata view used for annotation, not the raw acquisition response. Any additional data release requires a separate privacy, license, and venue-policy review.
