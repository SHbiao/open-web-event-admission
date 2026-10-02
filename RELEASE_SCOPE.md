# Public release scope and exclusions

This file records what is shipped with the 1K-scale collection.

## Included

- fixed evaluation runner source;
- measurement contract and F3 audit report;
- claim/evidence matrix and study overview;
- item-free D2 aggregate metrics;
- exact saved D2 per-method scores, statuses, operating points, and decisions, with private feature records omitted;
- DEV30 labels and saved scores for the declared post-hoc diagnostic methods;
- semantic prompt templates, resource identities, split identifiers, and reproducible post-hoc analysis code;
- all 102 cleaned D2 annotation-visible items, final item labels, and agreement/adjudication provenance;
- the earlier 300-item audited extension and item-level provenance;
- the 518-item consensus extension and its agreement/evidence-hash provenance;
- the 200-item human extension and its A/B/adjudication provenance;
- English annotation and review protocols plus aggregate annotation-quality analyses.

## Excluded

- direct source IDs, author records, acquisition payloads, and media files;
- private A/B session records, individual annotator answers, and adjudication notes;
- model rationales, private annotation sessions, and human review notes;
- private overlap and acquisition manifests;
- restricted model weights, knowledge-base snapshots, runtime caches, and secrets;
- generated PDFs, logs, temporary previews, and local environment files.

The JSONL files preserve the cleaned text-and-metadata views used during annotation. Historical filenames are retained where evaluation scripts depend on them; the public data manifest describes the collection using construction layers and provenance rather than tier labels.
