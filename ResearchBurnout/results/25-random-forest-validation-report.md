# Selected RF: validation report

Completed: 2026-11-18T23:27:38.563751+02:00 (Asia/Beirut)

File layout updated **19 November 2026**. This readable copy uses the new filenames; its numerical findings are unchanged. Original source files, report, manifests and verified hashes remain together in `results/99-original-workspace-and-verified-validation.zip`, under their original paths. Current renamed scripts have new source hashes and should not be substituted into the old hash checks.

## Finding

The regenerated selected procedure detects 14.8 of 17 High students and produces 28.0 false warnings among 80 Below-high students per repetition. Recall is 87.1%; precision is 34.7%. A warning remains uncertain for an individual student.

The workload-only logistic baseline detects 16.0/17 with 28.0 false warnings: recall 94.1%, precision 36.4%. It has higher mean recall, precision, balanced accuracy and F2 than the selected RF at the same mean false-warning count in this comparison. This challenges a claim that the eight-input RF is needed for the warning task. Workload-only average precision is lower (0.423 versus RF 0.527); performance at the chosen warning rule and ranking across all thresholds are different properties.

## Methods and evidence recovery

The historical prediction/model folders were absent and no copy was found in the local Desktop, Documents, Downloads or OneDrive searches, including Git-ignored files. The search found two 20-row artificial software fixtures; those are not study results. Some unrelated build and temporary folders were inaccessible. Original model files were not recovered or replaced. The raw CSV and prepared SAV hashes matched the recorded inputs. This run regenerated only the selected eight-input RF procedure and required baselines using the existing helpers and pinned main-package versions; it did not recreate every historical experiment.

High means measured primary burnout_score >=4 (17 students), versus 80 Below-high students. These study-defined groups are not clinical diagnoses. All five original stratified five-fold repetitions and four inner folds were retained. Each training group selected depth 2/3, leaf size 5/10, normalized relative High weight 1/2/4, augmentation ratio 0/.5/1 and warning threshold 0..1 in .05 steps by inner F2, with original tie rules. Each forest has 100 trees. Only excluded real students contributed evaluation predictions; all synthetic parents and learned transformations stayed in training. The final all-data model recipe was not changed.

The workload-only comparator used logistic regression with fixed C=1, training-only standardized workload and inner-selected relative High weight 1/2/4 and threshold from the same grid. The random comparator analytically selects the same warning count within each outer test fold. Its counts are expectations, and its nonlinear metrics are calculated from expected counts; it is a descriptive reference rather than a deployable rule or inferential test.

## Matched comparisons

| Procedure | Recall | Precision | High detected /17 | False warnings /80 | Balanced accuracy |
|---|---:|---:|---:|---:|---:|
| Selected eight-input RF | 87.1% | 34.7% | 14.80 | 28.00 | 76.0% |
| Eight-input RF without augmentation | 84.7% | 32.7% | 14.40 | 29.60 | 73.9% |
| Workload-only logistic | 94.1% | 36.4% | 16.00 | 28.00 | 79.6% |
| Random, same warning count | 44.6% | 17.7% | 7.58 | 35.22 | 50.3% |
| Warn everyone | 100.0% | 17.5% | 17.00 | 80.00 | 50.0% |
| Warn nobody | 0.0% | 0.0% | 0.00 | 0.00 | 50.0% |

All seven recorded RF means reproduce: recall, precision, F2, true positives, false positives, average precision and ROC AUC. Counts and metrics average five repetitions of the same 97 people, not 485 independent students.

| Learned procedure | F2 | ROC AUC | Average precision | Warnings /97 |
|---|---:|---:|---:|---:|
| Selected eight-input RF | 0.668 | 0.809 | 0.527 | 42.8 |
| Eight-input RF without augmentation | 0.643 | 0.799 | 0.482 | 44.0 |
| Workload-only logistic | 0.714 | 0.824 | 0.423 | 44.0 |

## Chance diagnostic

The predeclared statistic was mean repetition balanced accuracy. All 199 shuffles preserved overall class counts and assigned one shuffled label per student, shared across repetitions. Each null run rebuilt stratified folds and repeated the full RF preprocessing, augmentation and inner selection procedure. Real-label statistic: 0.760294. Null mean: 0.495704; null range: 0.410441 to 0.636103. Corrected one-sided permutation p-value: 0.0050.

0 of 199 shuffled-label evaluations reached or exceeded the real-label statistic. The finite-permutation correction gives (1+0)/(1+199) = 0.0050; a finite run cannot establish a zero p-value. This diagnostic concerns the fixed procedure in this dataset. It does not reproduce the entire historical search across algorithms, features and human decisions, so it cannot remove earlier selection optimism or establish useful precision, external performance, causality or clinical utility.

## Uncertainty

Repetition ranges describe split sensitivity. Conditional 95% percentile bootstrap intervals use 2,000 class-stratified student resamples, preserving all five predictions for each sampled student and using paired samples across methods. They condition on observed class counts and fitted predictions; they omit model refitting, historical selection and external-population uncertainty. They are not definitive confidence intervals for deployment performance.

| RF metric | Conditional 95% interval |
|---|---:|
| Recall | 70.6% to 100.0% |
| Precision | 27.9% to 42.7% |
| Balanced accuracy | 66.4% to 83.8% |

| RF minus workload-only | Conditional 95% interval, percentage points |
|---|---:|
| Recall | -20.0 to 2.4 |
| Precision | -7.3 to 3.1 |
| Balanced accuracy | -11.1 to 2.3 |

RF recall ranges from 82.4% to 94.1% across repetitions; false warnings range from 24 to 30. Every paired RF-minus-workload interval above includes zero. The observed workload advantage therefore remains uncertain under this conditional analysis.


## Warning trade-off and synthetic check

The threshold curve is descriptive: it applies common triggers to saved outer scores. The marked selected procedure used fold-specific inner-selected thresholds and need not lie on that common-threshold curve. No new threshold was selected from outer outcomes; the separately documented saved-model threshold remains .35.

The historical 970-profile simulation (159/170 assumed High profiles detected, recall 93.5%) used profiles derived from training students and inherited labels. It remains a separate simulation, not new measured students, independent validation or a replacement for the reproduced 87.1% real cross-validation recall. Its missing historical outputs were not regenerated in this task.

## Interpretation and remaining limits

Recommendation: retain the historical RF artifact/recipe and report the workload-only comparator prominently. This evaluation provides no demonstrated warning advantage for the eight-input RF over workload alone. The baseline was proposed after inspecting historical results and remains exploratory; do not promote it to an independently validated replacement. Comparing different algorithms/input sets does not isolate the incremental value of AI inputs. Use the paired conditional intervals to describe uncertainty, not to claim definitive superiority.

Only 17 real High students support these estimates, and many exploratory comparisons have reused all 97 respondents. New random splits cannot create an untouched cohort retrospectively. Freeze the chosen procedure before any future evaluation on new real students with measured BAT outcomes. This phase has no new recruitment, independent validation, calibrated clinical probabilities or validated intervention.

## Historical comparisons to retain in the paper

The project record describes SVC with eight/23 inputs, TabPFN and its threshold/mixture refinements, RF/logistic mixtures, expanded forest tuning, question-subset/backward selection and Boruta. These did not establish a uniform improvement for the chosen detection/false-warning priority. Some improved precision or ranking while losing detections or adding false warnings; group these trade-offs in the paper instead of presenting every unsuccessful parameter trial as a separate contribution.

This validation regenerated the selected RF and simple baselines only. The earlier comparison outputs remain unavailable here, so their detailed tables are historical documentation rather than newly reverified evidence. Preserve their recorded methods/results in `research/07-classification-experiments-and-methods.md` and `research/06-data-analysis-and-experiment-history.md`; inspect original outputs before making new exact claims about them. Numerical-score regression remains a separate task and should not be ranked against classifier recall.

## Verification and artifacts

Checks passed for all 5,000 fold checkpoints and 180,000 candidate selections. Verification independently scored all 199 null procedures and recomputed the p-value, regenerated all 125 real-training synthetic pools, refitted the 25 selected real outer models and replayed one full real and one full null search. It did not refit every null model. Source hashes remained unchanged.

Elapsed time from the first audit attempt to completed primary computation: 6.70 hours, using four single-threaded workers for the full permutation stage. The pilot fold took 10.8 seconds alone; folds took longer under concurrent load. Runtime records are retained in every checkpoint.

Original local audit: archive `99-original-workspace-and-verified-validation.zip`, entry `classification/validation-outputs/20261118T143652947217Z/`. Readable figures beside this report are `25-real-model-versus-shuffled-labels.png`, `25-detections-versus-false-warnings.png` and `25-random-forest-confusion-matrix.png`. Supporting files beginning with `25-` contain comparison metrics, uncertainty, stability and threshold data. Participant-level files remain excluded from Git.

The readable `23-recorded-random-forest-recipe-and-schema.json` copies the original audit's `frozen-recipe.json`: the eight-input schema, allowed codes, recorded 100-tree/depth-3/leaf-10/High-weight-2/.35-threshold/zero-augmentation recipe, configuration hash and package versions. The original model binary and metadata remain missing, so an original-artifact backup was not possible and no model-file hash is claimed. The recipe record is not a trained model.

Methods references: [scikit-learn permutation testing](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html); [nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html).
