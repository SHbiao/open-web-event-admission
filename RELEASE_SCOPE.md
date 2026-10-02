# Public release scope and exclusions

This file records what is shipped with the 1,290-item collection.

## Included

- fixed evaluation runner source;
- measurement contract and F3 audit report;
- claim/evidence matrix and study overview;
- item-free D2 aggregate metrics;
- exact saved D2 per-method scores, statuses, operating points, and decisions, with private feature records omitted;
- DEV30 labels and saved scores for the declared post-hoc diagnostic methods;
- semantic prompt templates, resource identities, split identifiers, and reproducible post-hoc analysis code;
- all 102 cleaned D2 annotation-visible items, final item labels, and agreement/adjudication provenance;
- the human group: calibration/diagnostic records and the 200-item human extension with its provenance;
- the AI-assisted group: the 300-item audited extension and the 518-item agreement-selected extension with provenance;
- English annotation and review protocols plus aggregate annotation-quality analyses.

## Excluded

- direct source IDs, author records, acquisition payloads, and media files;
- private A/B session records, individual annotator answers, and adjudication notes;
- model rationales, private annotation sessions, and human review notes;
- private overlap and acquisition manifests;
- restricted model weights, knowledge-base snapshots, runtime caches, and secrets;
- generated PDFs, logs, temporary previews, and local environment files.

The JSONL files preserve the cleaned text-and-metadata views used during annotation. The public narrative uses two annotation groups, while compatibility fields required by the historical D2 runner remain unchanged inside the D2 data and scripts.
