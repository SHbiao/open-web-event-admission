# Data release scope

The benchmark has three evidence layers: P0 task-unit calibration, DEV30/EVAL60 controlled diagnostics, and a 102-item D2 challenge confirmation set. They must not be concatenated into one homogeneous test set.

The public package contains the P0 item-level calibration metadata in `p0_item_level_calibration.csv`. It intentionally contains no raw item text, external URLs, source identifiers, A/B annotation packages, human adjudication records, or fused D2 Gold labels. Those artifacts remain in the private research archive.

The aggregate file in `../results/d2_aggregate_metrics.csv` is sufficient to inspect the D2 denominators and headline metrics without reconstructing or identifying individual posts. Researchers who need the withheld item-level text should contact the authors with an ethics, licensing, and data-protection plan.
