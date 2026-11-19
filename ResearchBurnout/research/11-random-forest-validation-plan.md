# Plan: assess whether the selected RF adds useful information

Organization updated 19 November 2026. See [the project README](../README.md) for current folders and commands. Timestamped paths below describe historical runs; the original verified validation namespace is preserved in the local results/99-original-workspace-and-verified-validation.zip archive. [The current readable validation report](../results/25-random-forest-validation-report.md) uses the new filenames.

Drafted and completed 18 November 2026. Read [the verified report](../results/25-random-forest-validation-report.md). The selected RF's 25 real-student evaluation folds reproduce the historical metrics exactly; matched baselines, all 199 full-procedure label permutations, conditional uncertainty, figures and verification are complete. Local audit: `results/25-random-forest-validation/20261118T143652947217Z/`.

## Completion record

| Step | Evidence and outcome |
|---|---|
| 1. Recover/check evidence | `recovery-inventory.json`; no original study outputs/model recovered, only artificial test fixtures. SAV/CSV hashes match. Focused RF regeneration reproduces all seven recorded means. |
| 2. Compare baselines | Held-out predictions, summary/repetition metrics, paired comparisons and confusion figure. Workload-only detects 16/17 with 28 false warnings versus RF 14.8/17 with 28. |
| 3. Chance/uncertainty | 199 complete permutations: corrected p=.005; independent null metrics and p-value verification. Conditional student bootstrap intervals, repetition ranges, warning frequencies and chance plot retained. |
| 4. Warning trade-off | Descriptive curve/figure completed; no outer-result threshold selection or replacement of the recorded .35 final threshold. |
| 5. Freeze/report | Paper-ready report and current project summaries completed. `frozen-recipe.json` preserves the recorded recipe/schema/configuration hash/versions. Original binary/metadata remain missing, so their backup was unavailable; no trained-model hash or recovered artifact is claimed. Future independent validation remains outside this data-limited phase. |

The numbered sections below preserve the agreed plan and its original estimates.

Question: does the selected eight-input Random Forest identify High students better than simple warning strategies, and how many false warnings does that detection require?

Keep the 97 real students, measured primary-score boundary >=4, original eight inputs and selected training procedure. Preserve source data, previous results and the saved-model recipe. Do not optimize against the 970 synthetic profiles or present their 93.5% recall as real-student validation. No new recruitment is available for this phase.

## 1. Recover the evidence and check reproducibility

Estimated hands-on time: 30-60 minutes if a backup is available; transfer time depends on its location.

The current workspace has the raw CSV and prepared SAV with hashes matching the handoff. It lacks the saved classifier/metadata and referenced experiment folders. First check existing local backups and the previous working copy. Keep participant-level files local and excluded from Git.

Required first: selected augmentation run's held-out predictions, folds, tuning records, metrics, configs, manifest and verification. Restore its binary-reference prerequisites if refitting is needed. The final saved classifier is useful for later inference but is not needed to recompute cross-validation metrics.

Recalculate the selected RF results from predictions. Check one prediction per real student per repetition, fold separation, score/label alignment, thresholds and source hashes. Require agreement with recorded 87.1% recall, 34.7% precision and mean FP 28 before drawing new conclusions. If recovery fails, inventory missing dependencies before estimating a regeneration run; do not launch every historical experiment.

Deliverable: an evidence inventory and reproduced metric table, or a precise list of unavailable evidence.

## 2. Compare warnings fairly

Estimated hands-on time: 1-2 hours once predictions are available; new fitting time is separate.

Reuse existing all-flagged and none-flagged references. Add the expected result of randomly choosing the same number of warnings within each outer test fold; compute it analytically rather than choosing a favourable random seed. This equal-volume comparison is descriptive and may use the observed RF warning count; it is not a deployable selection rule or a significance test.

Add one workload-only logistic baseline if existing results do not contain it. Use a fixed, small specification and the same nested evaluation folds, with threshold/weight selection confined to inner training validation. Use original real-only eight-input RF results to separate augmentation from the benefit of modelling at all. Reuse existing helpers and write new outputs separately.

Report recall, precision, TP/FN/FP/TN, warning rate, F2, balanced accuracy, ROC AUC and average precision, with paired per-repetition comparisons. Show detected High students and false warnings per 97 students. Retain unrounded values for calculations.

Deliverable: one main comparison table and a confusion-matrix figure. No model replacement based on this table.

## 3. Check chance performance and describe uncertainty

Estimated hands-on time: 2-4 hours for implementation/checks; benchmark computation before promising a completion time.

Use a label-permutation diagnostic for the frozen selected training procedure, with balanced accuracy as the predeclared primary statistic. Shuffle labels at the student level while preserving overall class counts. Repeat preprocessing, inner hyperparameter/weight/threshold/augmentation selection and outer evaluation under each permutation. Rebuild stratified folds consistently from each permuted target using fixed seeds. Synthetic parents, when selected, must come only from the permuted training groups. Never test chance performance by scoring an already fitted model on shuffled training labels.

Run a small runtime pilot, then plan 199 permutations if feasible, using the finite-permutation p-value correction (1 + number at least as good)/(1 + number of permutations). Save seeds and all scores. This tests the now-fixed procedure; it does not account for every algorithm and human decision previously tried on these students, and it cannot establish external validity.

Report per-repetition ranges and student-level miss/false-warning frequencies. Do not count 485 repeated predictions as independent students or use a standard error across folds as an independent-sample interval. If reporting bootstrap intervals from existing predictions, resample students with all their repetitions together and explicitly label those intervals conditional on existing fits; they omit refitting and model-selection uncertainty.

Deliverable: a chance-comparison plot, runtime record and uncertainty explanation, with the historical selection limitation visible.

## 4. Describe the warning trade-off without choosing on test results

Estimated hands-on time: 1-2 hours.

Use existing held-out scores to illustrate how detection and false warnings change with the trigger. Label this as descriptive. Do not replace the .35 saved-model threshold by choosing the best-looking point on those results. A new operational rule needs a stated warning consequence and an acceptable false-warning/detection trade-off, followed by selection inside training validation.

Keep the current research task focused on reporting the chosen RF. Avoid further classifier searches, automatic advice, clinical probability claims and additional synthetic test sets. If the RF offers little advantage over the simple baseline, report that result and prefer the simpler method for any future comparison.

Deliverable: one trade-off figure and a plain-language explanation of approximately 15 detections with 28 false warnings.

## 5. Freeze the report and define future validation

Estimated hands-on time: 2-3 hours for the methods/results summary after checks finish.

Write the methods, baseline comparisons, uncertainty and unsuccessful-experiment summary. Put the 970-profile simulation in a separate section with assumed-label and training-parent limitations. Record the frozen model/schema, threshold, hashes and package versions; back up model and metadata outside Git.

No untouched real test cohort exists here: the final model used all 97 students and earlier experiments repeatedly inspected this sample. A new random split cannot create an untouched cohort retrospectively. Future evaluation should use new real students with measured BAT outcomes after freezing the approach, once recruitment becomes possible. Until then, call the findings exploratory.

Deliverable: a paper-ready validation summary and an explicit list of claims the evidence supports.

## Timing and first action

Allow about 1-2 working days of hands-on analysis/reporting if backups are available, plus data transfer and permutation/refitting computation. These are planning estimates, not measured runtimes. First action: inventory local backups for the selected augmentation run; do not begin by retraining or tuning.

## Method references

- [scikit-learn: permutation testing of cross-validated scores](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html).
- [scikit-learn: nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html).

The initial drafting step ran no experiments. Subsequent execution completed the evaluation and verification recorded above. Missing original model/output artifacts and the absence of an independent real cohort remain explicit limits.
