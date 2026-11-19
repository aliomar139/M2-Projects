# Classification experiments

Organization updated 19 November 2026. See [the project README](../README.md) for current folders and commands. Timestamped paths below describe historical runs; the original verified validation namespace is preserved in the local results/99-original-workspace-and-verified-validation.zip archive. [The current readable validation report](../results/25-random-forest-validation-report.md) uses the new filenames.

## Validation completed (18 November 2026)

The [validation plan](11-random-forest-validation-plan.md) is complete; read [the verified report](../results/25-random-forest-validation-report.md). Local audit: `validation-outputs/20261118T143652947217Z/`. All original selected-RF recall/precision/F2/TP/FP/AP/AUC means reproduce exactly after regenerating its 25 real-student outer folds. The matched workload-only logistic comparator gives **94.1% recall /36.4% precision, 16 High detections and 28 false warnings**, versus RF **87.1% /34.7%, 14.8 detections and 28 false warnings**. This exploratory result challenges a claimed warning advantage for the eight-input RF. Paired conditional RF-minus-workload intervals include zero; this does not isolate AI's incremental value or establish an independently validated replacement. RF average precision remains higher (.527 versus .423).

All 199 full-procedure student-label permutations finished. RF balanced accuracy .760294 exceeded every null evaluation (mean .495704, maximum .636103); corrected p=.005. This fixed-procedure diagnostic cannot account for earlier historical model selection or establish external utility. Verification passed for 5,000 folds/180,000 choices, all 125 regenerated real-training synthetic pools, 25 selected real outer refits, two full search replays and independent null metrics/p-value calculation. Nine relevant tests pass. Conditional student bootstrap tables, paired comparisons, repetition ranges, warning frequencies, confusion matrix and descriptive threshold/chance figures are retained. The final .35 recipe threshold was not changed.

`validate-selected-rf.py` uses the original five repetitions/five outer/four inner folds, existing RF/generation helpers and original selection grid, without depending on missing historical output folders. Configuration: `validation-config.json`. From the root, `--stage real` creates and prints a new timestamped audit directory; resume that directory with `--stage permutations --out <audit-directory>`, then run `report-validation.py <audit-directory>` to verify/report. Existing checkpoints are reused only after source-hash checks. A full fresh permutation run took about 6.7 hours with four single-threaded workers. New checks: `.\.venv\Scripts\python.exe experiments/test_25_random_forest_validation.py`. Participant-level audit outputs stay excluded from Git.

The original saved classifier/metadata and referenced historical output folders were not found in this workspace. Their documentation below records earlier work and is not proof those files are currently available. This validation did not export or replace a final model. `frozen-recipe.json` preserves the documented schema/recipe/configuration hash/versions, with the absent binary and unavailable original-artifact backup stated explicitly.

## Selected classification model

The user selected Small B Random Forest with training-selected augmentation: 87.1% High recall, 34.7% precision, F2 .668 and 28.0 false warnings per 80 Below-high students, averaged over five repetitions. The existing ridge/SVR blend remains the numerical score predictor. A final classifier artifact was saved on 17 November 2026 as described below; the numerical-score blend has not been exported.

## Saved final classifier (17 November 2026)

**Model:** `results/23-selected-random-forest.joblib`. **Metadata:** `results/23-selected-random-forest-metadata.json`. Both are local, ignored files; they are not automatically included in Git pushes. Keep/transfer both files when backing up or sharing the trained artifact. The joblib bundle contains standard sklearn preprocessing and forest objects plus the eight feature names, allowed codes, warning threshold, class names and reference metrics; loading does not require custom project pickle classes.

Runner [23-save-selected-random-forest.py](../experiments/23-save-selected-random-forest.py), frozen [final-fit-config.json](../experiments/23-save-selected-random-forest-settings.json). This applies the previously selected RF procedure to all **97 real students**: four stratified training-validation folds independently fit preprocessing/generation and choose the original RF depth/leaf grid, normalized High weight, ratio 0/.5/1 and .05-step warning threshold. It does not choose the most favourable outer fold. The final fit uses 100 trees, **max_depth 3, min_samples_leaf 10, High weight 2, warning threshold .35**, random seed 271828. Validation selected **ratio 0**, so this final artifact uses 97 real rows and no synthetic rows. Zero augmentation was an allowed choice in the selected procedure, not a new algorithm or a forced change to the old results.

The earlier **87.1% recall/34.7% precision** describe repeated cross-validation of the selected procedure; they are not a new measured performance of this all-data fit. Final-fit training/validation metrics are selection diagnostics. There is no independent test set or calibrated clinical risk estimate. The true label boundary remains measured primary BAT score >=4; .35 is the classifier's warning-score threshold, not a BAT cutoff.

Audit: `results/23-selected-random-forest-fit/20261117T114817911532Z/`, including 36 candidate curves (756 threshold options), final choice, validation folds, generation records, source/package hashes and non-evaluation final-fit scores. Initial fitting: 144 validation forests plus the final forest and an independent control refit using the historical transformation helper. Save/load roundtrip reproduced all 97 scores/labels; a fresh Python process loaded the bundle and reproduced all 97 again. The additional selected-recipe verification independently refits its four validation forests and checks its 21 threshold decisions. Prior result/source hashes are preserved. The exporter refuses to overwrite an existing model/metadata pair; version deliberately before exporting again.

### Load and predict from the project root

Use the recorded dependency versions (especially sklearn 1.9.1, NumPy 2.5.4, pandas 3.1.0, SciPy 1.18.1 and joblib 1.6.0). Example answers below are hypothetical, not a dataset row. Sleep/study values are survey category codes, not hours.

```python
import joblib
import pandas as pd

saved = joblib.load('results/23-selected-random-forest.joblib')
answers = pd.DataFrame([{
    'workload': 4, 'sleep_duration_code': 2, 'study_hours_code': 3,
    'financial_strain': 3, 'university_support': 2, 'ai_frequency': 4,
    'ai_dependence': 4, 'ai_offloading': 3,
}])
answers = answers.loc[:, saved['feature_names']]
for name, allowed in saved['allowed_values'].items():
    if not answers[name].isin(allowed).all():
        raise ValueError(f'Invalid or missing survey code: {name}')
scores = saved['pipeline'].predict_proba(answers)[:, 1]
classes = (scores >= saved['warning_threshold']).astype(int)
labels = [saved['class_names'][int(value)] for value in classes]
print(labels, scores)
```

The saved threshold must be applied to the scores for the intended warning rule. Scores are uncalibrated model outputs; High/Below-high are study-defined groups. No synthetic generation or SPSS dataset is needed to predict from new valid eight-input answers.

## How one synthetic profile is created

Explanation updated **18 November 2026**. The implementation is `pool()` in [11-augment-high-burnout-classifiers.py](../experiments/11-augment-high-burnout-classifiers.py); [24-check-random-forest-on-synthetic-profiles.py](../experiments/24-check-random-forest-on-synthetic-profiles.py) reuses it separately for both classes in the inference-only check. This is constrained same-class interpolation with stochastic rounding, not independently sampled random answers or a fitted generative model.

### 1. Choose two similar real parents

Choose parent A randomly from real students with eligible neighbours, then parent B randomly from A's up to three nearest eligible same-class neighbours. The training experiment uses only real High students inside the current training split. The separate synthetic check uses each class separately. Parents are chosen repeatedly; contributions are not guaranteed to be equal.

For Small B, distance is `(sum of six absolute ordinal differences /4 + number of mismatches in the two category codes) /8`. Parent distance must be <=.35, with no ordinal answer differing by more than 2. Generated distance from A must be <=.25.

### 2. Mix six answers; keep two answers from A

The following is an **illustrative example**, not two identified dataset rows. Suppose A and B both have measured primary burnout score >=4. Draw one mixing fraction uniformly between .2 and .8; here it is .4. For every ordinal answer, calculate `0.6*A + 0.4*B`.

| Input | Parent A | Parent B | Calculation | Example new C |
|---|---:|---:|---|---:|
| workload | 4 | 5 | 4.4, rounded probabilistically | 4 |
| sleep_duration_code | 2 | 3 | Keep A's category | 2 |
| study_hours_code | 3 | 3 | Keep A's category | 3 |
| financial_strain | 3 | 4 | 3.4, rounded probabilistically | 4 |
| university_support | 2 | 2 | 2, unchanged | 2 |
| ai_frequency | 4 | 5 | 4.4, rounded probabilistically | 5 |
| ai_dependence | 4 | 5 | 4.4, rounded probabilistically | 4 |
| ai_offloading | 4 | 4 | 4, unchanged | 4 |

**"Copy A" means C receives A's exact sleep and study-hours category codes together.** Code 2 is a category identifier, not two hours. We do not average these codes into a nonexistent category such as 2.5. Other answers can change, so the complete C profile can still differ from A.

For 4.4, rounding gives 5 with probability .4 and 4 with probability .6. For 3.4, it gives 4 with probability .4 and 3 with probability .6. Each ordinal input has its own random rounding draw; one shared mixing fraction is used for the profile. These draws are reproducible from the recorded seeds.

In this example, parent distance is `(4/4 + 1)/8 = .25`. C differs from A by one step in financial strain and AI frequency, so its distance from A is `(2/4)/8 = .0625`. Both pass the limits. C is accepted only if its full eight-input profile is also absent from the real data and the relevant generated pool; otherwise another candidate is attempted. The separate 970-profile check additionally enforces uniqueness across all its batches and excludes exact cross-label conflicts.

### 3. Assign an assumed label and use the profile

C inherits an **assumed High label** because both parents are High. We do not generate BAT answers, measure a new person's burnout, or use the model's prediction to choose C's label. Valid codes and nearby parents do not prove that the new combination describes a real student or has the assumed outcome.

Historical augmentation creates pools within training folds only, then selects no/half/full augmentation using inner validation; held-out real students remain untouched. Its **2,720 total instances** span many pools. The **saved final RF uses zero synthetic rows** because its final selection chose no augmentation. The later **970 profiles** were used only to check that frozen model's consistency, without retraining. These are three different sample counts, not one combined dataset.

## Saved model: synthetic-profile check (17 November 2026)

Completed separate simulation results (historical local file, unavailable here: results/24-synthetic-profile-check/20261117T130726203314Z/results.md). **This is agreement with parent-inferred synthetic labels, not validation on new real students or an improvement over the previous 87.1% real held-out recall.** The saved model and threshold .35 were frozen. No training, settings selection or model replacement occurred.

Generated **970 unique profiles: 800 Below-high /170 High**, matching the original class proportions at tenfold scale. For this inference-only simulation, the existing constrained training generator is called separately for each real parent class, remapping its positive class internally. It combines same-class nearby parents, stochastically rounds ordinal inputs and copies the categorical block. All real-profile duplicates and global synthetic duplicates are excluded. Exact cross-label conflicts would be excluded; none occurred. No constraints were relaxed and the requested counts were achieved. Profile labels come from parents' measured classes, never from model predictions; they are not new measured BAT outcomes. This is a different set from the historical 2,720 training-pool instances.

| Measure against assumed synthetic labels | Result |
|---|---:|
| High recall | 93.5% (159/170) |
| High precision | 55.6% (159/286 warnings) |
| F2 | .822981 |
| Accuracy/agreement | 85.8% |
| TP / FN | 159 /11 |
| FP / TN | 127 /673 |
| Average precision /ROC AUC | .698947 /.929324 |

Always predicting Below-high would achieve 82.5% accuracy but zero High recall, so accuracy alone is misleading. All 97 real parents were used to fit the saved forest: interpolation near their labelled profiles can make this simulation favourable. Novel combinations are not independent new students or proof of real generalization. This one-seed simulation cannot replace real held-out evaluation, prove clinical accuracy, or justify changing the reported CV metrics.

Runner [24-check-random-forest-on-synthetic-profiles.py](../experiments/24-check-random-forest-on-synthetic-profiles.py), [settings](../experiments/24-check-random-forest-on-synthetic-profiles-settings.json). Run `.\.venv\Scripts\python.exe experiments/24-check-random-forest-on-synthetic-profiles.py`. Separate ignored output root contains profiles/predictions/parent provenance, candidate-batch logs, generator/config, metrics and hash manifest. Verification passed (historical local file, unavailable here: results/24-synthetic-profile-check/20261117T130726203314Z/verification.json): all 970 profiles' parent labels, valid domains, mixed distances, interpolation/rounding, novelty and class counts checked; independent sklearn metrics match; reloaded CSV scores/labels reproduce; saved model/metadata/source hashes unchanged. There is no synthetic training or new independent test cohort in this experiment.

## Boruta selection from all 23 inputs (16 November 2026)

Completed separate Boruta results (historical local file, unavailable here: results/22-boruta-input-selection/20261116T082517133758Z/results.md). **Keep the selected eight-input RF.** Boruta's two tested rules have lower High recall and F2; its recall-focused rule also has lower precision and more false warnings. Earlier results/source data are preserved.

| Input approach | Rule | High recall | Precision | F2 | Detected /17 | False warnings /80 |
|---|---|---:|---:|---:|---:|---:|
| Selected eight-input RF | Original F2 | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Boruta from 23 | F2 | 72.9% | **36.1%** | .604040 | 12.4 | **22.2** |
| Boruta from 23 | Recall guard | 82.4% | 32.6% | .630103 | 14.0 | 29.0 |

The F2 rule saves 5.8 false warnings but detects 2.4 fewer High students on average. Guard loses .8 detections and adds one warning. Counts average five dependent repetitions of the same 97 real students, not independent cohorts. Boruta selects **2–5 variables in outer training fits** (mean 3.56): workload/academic stress in 25/25, AI dependence 20/25, avoidance 16/25, AI offloading/financial strain/university support each 1/25. These are fold-specific selections, not a globally fitted final input set or proof that omitted variables are useless. Selection counts (historical local file, unavailable here: results/22-boruta-input-selection/20261116T082517133758Z/selection-counts.csv), frequencies (historical local file, unavailable here: results/22-boruta-input-selection/20261116T082517133758Z/selection-frequency.csv).

Runner [22-select-random-forest-inputs-with-boruta.py](../experiments/22-select-random-forest-inputs-with-boruta.py), fixed [settings](../experiments/22-select-random-forest-inputs-with-boruta-settings.json). Official [BorutaPy](https://github.com/scikit-learn-contrib/boruta_py) 0.4.3 added without changing existing package versions; install in the existing environment with `.\.venv\Scripts\python.exe -m pip install --no-deps -r experiments/dependencies-boruta.txt`. Run `.\.venv\Scripts\python.exe experiments/22-select-random-forest-inputs-with-boruta.py`. Original five repetitions of five outer/four inner stratified folds; High remains primary score >=4 (17 High/80 Below-high). No BAT predictors, new questionnaire features or observed respondents.

Boruta runs on 37 encoded columns of all 23 eligible variables, fitted on real training members only, independently in every inner/outer training group. Fixed selector RF: 100 trees, depth 5, min leaf 2, balanced classes; Boruta max_iter 50 (at most 49 forest iterations), perc 100, alpha .05, two-step correction, deterministic per-context seeds. Keep whole variables having any confirmed encoded column, including all their categorical dummies. Tentative support is saved but excluded; no fixed count. A zero-confirmed context would use a weighted training-class prior rather than silently forcing another input; **none occurred** in this run. Column-level Boruta followed by whole-variable expansion is not a group-level significance test.

After selection, original constrained synthetic pools are generated on all 23 real training variables and projected onto selected variables; projected duplicates can occur. Synthetic labels remain assumptions. This complete selection/augmentation procedure is compared with the current reference; it does not isolate Boruta's effect from the change in the generation domain. Independently tune original RF depth/leaf grid, High weights 1/2/4, ratios 0/.5/1 and .05-step thresholds. F2 and recall-guard ties reuse the prior input-comparison rules; guard constrains recorded current RF inner recall, not outer recall. Only real held-out students evaluate. Reference scores are copied after matching original folds/hashes.

Initial run: 125 selector fits comprising 5,894 selector-forest iterations, 3,600 inner/40 outer prediction-model fits, 900 candidate score sets and 50 choices. Separate ignored output folder saves 1,455 predictions, selector support/tentative/ranking/importance histories and training memberships, synthetic pools/parents, original folds, metrics/paired changes and hashes. Verification command: `.\.venv\Scripts\python.exe experiments/22-verify-boruta-feature-selection.py results/22-boruta-input-selection/20261116T082517133758Z`; verification record (historical local file, unavailable here: results/22-boruta-input-selection/20261116T082517133758Z/verification.json).

**Verification passed:** all 18,900 threshold candidates/50 choices, 125 training contexts and saved selector group mappings, generated profiles/parent memberships, original folds/copied RF reference scores, core metrics/AP/AUC, summaries/paired differences and source/package/implementation hashes checked. Independently refitted all 160 selected inner/40 outer prediction models, reproducing saved scores; replayed Boruta itself for two predeclared first-group contexts and reproduced support/rankings/importance histories. The other 123 selectors and unselected prediction candidates were not refitted during verification. These checks verify computation, not independent-cohort performance.

This tests one fixed Boruta configuration; the iteration cap, small sample and impurity-based importance limit conclusions about relevance. Repeated same-sample exploration remains exploratory; no independent cohort, calibrated clinical probability or deployment model. The existing selected RF remains unchanged.

## Alternative input combinations (16 November 2026)

Completed separate input-comparison results (historical local file, unavailable here: results/21-random-forest-input-comparison/20261116T075921907598Z/results.md). **Keep the current eight-input RF.** Neither new approach retains its High recall or improves F2. The two recall-focused alternatives also have lower precision and slightly more false warnings.

| Input approach | Selection rule | High recall | Precision | F2 | Detected /17 | False warnings /80 |
|---|---|---:|---:|---:|---:|---:|
| Current eight RF, reproduced control | Original F2 | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Alternative eight | F2 | 72.9% | 37.3% | .610528 | 12.4 | 21.2 |
| Alternative eight | Recall guard | 81.2% | 32.5% | .624508 | 13.8 | 28.6 |
| Eight selected from 23 | F2 | 72.9% | **37.9%** | .612559 | 12.4 | **20.8** |
| Eight selected from 23 | Recall guard | 83.5% | 33.5% | .642739 | 14.2 | 28.2 |

The fixed alternative replaces AI frequency/study hours with academic stress/avoidance: workload, sleep duration, financial strain, university support, AI dependence, AI offloading, academic stress and avoidance. Automatic selection ranks all 23 eligible variables using the existing grouped standardized L2 logistic C=1 selector; it selects eight whole variables independently inside every inner/outer training group, retaining categorical dummy groups together. It does not produce one globally selected final eight. Selection frequencies (historical local file, unavailable here: results/21-random-forest-input-comparison/20261116T075921907598Z/selection-frequency.csv) describe the 25 outer fits, not proven population relevance.

Runner [21-compare-random-forest-input-combinations.py](../experiments/21-compare-random-forest-input-combinations.py), settings [input-comparison-config.json](../experiments/21-compare-random-forest-input-combinations-settings.json). Original 5x5 stratified outer/four inner folds, 97 real students, primary score >=4 (17 High/80 Below-high). Each new approach independently tunes the original 36 combinations: depth 2/3, leaf size 5/10, High weight 1/2/4, synthetic ratio 0/.5/1, with thresholds 0..1 by .05. Synthetic pools and preprocessing use selected training inputs only; validation/test students remain real and excluded from generation and fitting. Ranking uses real training students only. Synthetic labels remain inferred assumptions. F2 ties prefer precision/recall/threshold/lower ratio/stable grid. Guard requires the recorded current RF inner recall, minimizes FP, then favors recall/precision/F2/threshold/lower ratio/stable grid. It is not an outer recall guarantee. The current control refits its frozen original recipe and reproduces original inner metrics, thresholds and held-out scores.

Run `.\.venv\Scripts\python.exe experiments/21-compare-random-forest-input-combinations.py`. Initial run: 7,300 inner/104 outer fits; 1,825 candidate score sets, 125 choices, 2,425 predictions, 375 training contexts, selected input lists, synthetic pools/provenance, original folds, repetition metrics, paired changes, configs and hashes. Verification command: `.\.venv\Scripts\python.exe experiments/21-verify-random-forest-input-comparisons.py results/21-random-forest-input-comparison/20261116T075921907598Z`. The verification record (historical local file, unavailable here: results/21-random-forest-input-comparison/20261116T075921907598Z/verification.json) records checks and selected-model refits.

**Verification passed:** independently reconstructed all 38,325 threshold candidates and 125 choices with sklearn metrics, reproduced rankings/generation contexts and parent memberships, verified reference folds/scores, core metrics/AP/AUC, summaries/paired changes and source hashes. Independently refitted 416 selected inner and 104 outer forests, reproducing saved scores. Unselected candidate models were not refitted; this is computational verification, not independent-population validation.

The F2 alternatives save 6.8/7.2 false warnings but miss 2.4 additional High students on average. Guard alternatives lose 1.0/.6 High detections and add .6/.2 warnings. Counts average five dependent repetitions of the same 97 students. Prior full-sample SPSS exploration motivated the fixed alternative, and repeated experiments limit independent claims. The logistic selector can miss nonlinear relevance; this does not prove all possible subsets fail. No new survey features, source-data changes, previous-result overwrites, package changes or deployment artifact.

## RBF SVC with 23 existing inputs (16 November 2026)

Completed separate 23-input results (historical local file, unavailable here: results/20-twenty-three-input-svc/20261116T072730431772Z/results.md). More inputs improve the SVC recall-focused procedure compared with eight inputs, but neither new procedure retains the selected RF's recall/F2. **Keep the RF for the current High-detection priority.** Earlier results are unchanged.

| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Selected RF (eight inputs) | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Eight-input SVC, F2 | 78.8% | 36.2% | .637154 | 13.4 | 23.6 |
| 23-input SVC, F2 | 76.5% | **40.4%** | .646090 | 13.0 | **19.4** |
| Eight-input SVC, recall guard | 80.0% | 33.4% | .624572 | 13.6 | 27.2 |
| 23-input SVC, recall guard | 83.5% | 35.4% | .655506 | 14.2 | 26.2 |

The 23-input guard gains .6 High detections and removes one false warning on average versus eight-input guard; F2 improves in three of five dependent repetitions. Compared with RF, it still loses .6 detections while saving 1.8 warnings. The 23-input F2 rule saves 8.6 warnings versus RF but loses 1.8 detections. This is a useful trade-off comparison, not a validated replacement or evidence that more inputs improve every metric.

Run `.\.venv\Scripts\python.exe experiments/20-compare-twenty-three-input-svc-warnings.py`; [settings](../experiments/20-compare-twenty-three-input-svc-warnings-settings.json). The runner reuses the frozen eight-input SVC helpers and exactly the same 36-setting C/gamma/High-weight grid, independently tuning all settings/thresholds on Broad D's 23 existing variables (37 columns after encoding). Original five repetitions of five stratified outer/four inner folds; encoding/scaling fit on real training members only. Same exact inner-margin threshold/F2/recall-guard policies and current RF inner minimum recall. No synthetic rows, BAT inputs, new questionnaire features, probability calibration or endpoint-reference retraining. Uncalibrated margins are ranking scores. Initial run: 3,600 inner and 35 outer fits, all converged. Only the known probability-parameter future-deprecation notice is filtered; convergence failures remain fatal.

Separate ignored output root `results/20-twenty-three-input-svc/` saves 2,425 predictions, 25 repetition rows, five summaries, confusion matrices, 20 paired comparisons against RF/matched eight-input rules, input columns, all 900 candidate score sets and 50 final choices, original folds, configs and source/package hashes. Independent verification passed (historical local file, unavailable here: results/20-twenty-three-input-svc/20261116T072730431772Z/verification.json): all 62,758 reconstructed threshold candidates/metrics/ties, fold/training memberships, copied reference scores, counts/AP/AUC/summaries/paired changes and unchanged hashes. Independently refitted 140 selected inner and 35 selected outer models, reproducing margins/labels and encoded dimensions. No separate software test suite, package installation, deployment fit or independent cohort. Repeated same-sample exploration remains a limitation.

## RBF Support Vector Classifier (16 November 2026)

Completed separate SVC results (historical local file, unavailable here: results/19-eight-input-svc/20261116T070622236133Z/results.md). **Keep the selected RF.** Neither SVC rule retains its High recall while improving the warning balance. This is classification with SVC, distinct from the earlier numerical-score SVR experiments.

| Procedure | High recall | Precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Selected RF + selected augmentation | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Real-only RBF SVC, inner F2 | 78.8% | **36.2%** | .637154 | 13.4 | **23.6** |
| Real-only RBF SVC, inner recall guard | 80.0% | 33.4% | .624572 | 13.6 | 27.2 |

F2 selection removes 4.4 false warnings but detects 1.4 fewer High students on average. Guard selection detects 1.2 fewer for .8 fewer false warnings, with lower mean precision/F2. F2 improves over RF in one repetition and declines in four; guarded F2 declines in all five. Means reuse the same 97 students over five dependent repetitions. This specified grid does not establish a ceiling for SVC or other methods.

Run `.\.venv\Scripts\python.exe experiments/19-compare-eight-input-svc-warnings.py`; [settings](../experiments/19-compare-eight-input-svc-warnings-settings.json). Same eight Small B inputs, original primary BAT >=4 target (17 High, 80 Below-high), original five-times-five stratified outer/four inner folds. No synthetic rows, BAT inputs or extra features. Existing one-hot encoding/scaling fits separately on each real training group. Jointly tune C .1/1/10/100, gamma .01/.1/1 and normalized relative High weights 1/2/4 (36 candidates per outer group). Thresholds are all unique pooled inner decision margins plus 0 and the next float above the maximum for an all-negative decision; prediction uses >=. Margins are not probabilities; no probability calibration is fit. RBF kernel, tol .001, max_iter 100000; convergence warnings/failures stop execution. Installed scikit-learn 1.9.1 emits a future-deprecation notice for explicitly passing probability=False; all fits use decision margins and converge.

F2 selection maximizes inner F2, precision, recall, higher threshold and earlier stable candidate. The guard requires at least the selected RF's recorded inner recall, minimizes FP, then maximizes recall, precision, F2, threshold and earlier candidate. These settings and threshold decisions use inner predictions only. The guard is not an outer-recall guarantee. Two procedures share a final model when they select the same candidate. Initial experiment fitted 3,600 inner and 37 outer SVCs. RF reference predictions are copied exactly, without fitting or changing the RF. AP/AUC pool raw margins across different fold fits and are ranking diagnostics, not calibrated risk estimates.

Separate ignored output root `results/19-eight-input-svc/` contains 1,455 predictions, 15 repetition metric rows, three summaries, confusion matrices, ten paired changes, original fold memberships, all 900 candidate inner score sets and their two selected threshold records, 50 final choices, configs and source/helper/package hashes. Independent verification passed (historical local file, unavailable here: results/19-eight-input-svc/20261116T070622236133Z/verification.json): reconstruct all 71,604 thresholds and metrics/ties/choices, original folds/training membership, copied RF controls, score/class alignment, all metrics/AP/AUC and paired changes. It also independently refitted the 148 selected inner and 37 selected outer models, reproducing saved margins and labels. Old outputs/source data/selected models remain unchanged. No separate software test suite, package installation or deployment model. Repeated experiment selection on these 97 students remains exploratory.

## Precise TabPFN thresholds and RF mixture (14 November 2026)

Completed two separate experiments: exact thresholds (historical local file, unavailable here: results/18-tabpfn-threshold-refinement/20261114T125820967153Z/results.md) and RF–TabPFN mixtures (historical local file, unavailable here: results/18-tabpfn-voting-refinement/20261114T125820967153Z/results.md). **Keep the selected RF for the current detection/false-warning balance.** The new rules offer trade-offs rather than a clear replacement.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Selected RF | 87.1% | 34.7% | **.667848** | 14.8 | 28.0 |
| TabPFN exact threshold, F2 | 74.1% | 35.2% | .605718 | 12.6 | **23.2** |
| TabPFN exact threshold, recall guard | **88.2%** | 31.2% | .645250 | **15.0** | 33.2 |
| RF–TabPFN mixture, F2 | 81.2% | **36.8%** | .653446 | 13.8 | 23.8 |
| RF–TabPFN mixture, recall guard | 83.5% | 36.8% | .665290 | 14.2 | 24.6 |
| RF-only exact threshold, either rule | 83.5% | 35.8% | .659129 | 14.2 | 25.6 |

Precise threshold selection improves the original TabPFN guard's false-warning count from 44.0 to 33.2 and F2 from .598623 to .645250, while recall decreases from 89.4% to 88.2%. Compared with selected RF, this still adds 5.2 false warnings for .2 more High detections on average. Mixture guard removes 3.4 false warnings but loses .6 High detections; its F2 remains slightly lower. The exact-threshold F2 rule worsens TabPFN held-out performance despite non-decreasing selected inner F2. Better inner optimization does not guarantee better held-out results on these small folds. All counts average five dependent repetitions of the same 97 people.

**Method:** runner [18-refine-tabpfn-thresholds-and-voting.py](../experiments/18-refine-tabpfn-thresholds-and-voting.py), settings [tabpfn-refinement-config.json](../experiments/18-refine-tabpfn-thresholds-and-voting-settings.json). Run `.\.venv\Scripts\python.exe experiments/18-refine-tabpfn-thresholds-and-voting.py`. Both stages reuse complete, verified frozen endpoint scores from the original TabPFN run (historical local file, unavailable here: results/17-tabpfn-comparison/20261114T124506935366Z/results.md) and RF/logistic run (historical local file, unavailable here: results/13-random-forest-logistic-voting/20261113T203744495093Z/results.md), taking only its RF endpoint. No endpoint is retrained; matching training IDs, inner/outer folds, labels and reference inner metrics are asserted. Thresholds are all unique inner scores plus boundary decisions; High prediction uses `score >= threshold`. Stage one selects a TabPFN threshold. Stage two independently selects among RF shares 1/.75/.5/0, with pure-RF exact-threshold controls. F2 ties favor precision, recall, higher threshold, then RF share. Recall guard requires at least the current RF's recorded inner recall, minimizes false positives, then favors recall, precision, F2, higher threshold and RF share. The guard is not an outer guarantee. Both endpoint recipes and further decisions reuse the original inner folds; outer students stay excluded from selection.

No calibration, new inputs, survey rows, synthetic generation, package installation or deployment fit. The RF endpoint retains its original selected training-only augmentation; TabPFN retains real-only contexts and public v2 weights. Scores are uncalibrated warning scores, not clinical probabilities. Mixture F2 selected pure RF in 18/25 groups (RF shares .75/.5/0 in 3/1/3); guard selected pure RF in 20/25 (.75/.5 in 4/1). This conditional four-share comparison does not test every possible mixture, nor establish that two endpoints have identical information.

Exact-threshold outputs contain 2,425 predictions, 25 repetition rows, five summaries, 2,014 threshold candidates and 50 decisions. Mixture outputs contain 3,395 predictions, 35 repetition rows, seven summaries, 8,047 candidates and 100 decisions. Both save configs, source hashes, original folds, all inner scores, selected shares/thresholds, confusion matrices and paired changes. Independent verification passed for thresholds (historical local file, unavailable here: results/18-tabpfn-threshold-refinement/20261114T125820967153Z/verification.json) and mixtures (historical local file, unavailable here: results/18-tabpfn-voting-refinement/20261114T125820967153Z/verification.json): complete candidate boundaries, arithmetic, ties, decisions, training membership, immutable endpoint scores, reconstructed outer mixtures, all prediction labels/metrics/AP/AUC, copied controls and unchanged hashes. Earlier data/results and selected models are unchanged. No software test suite or second endpoint-fitting run was performed. Repeated experiments on the same students remain exploratory.

## Local TabPFN-2 comparison (14 November 2026)

Completed separate results (historical local file, unavailable here: results/17-tabpfn-comparison/20261114T124506935366Z/results.md). **Keep the selected Random Forest.** TabPFN improves ranking metrics, but neither tested warning rule improves the detection/false-warning balance enough to replace the RF.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Selected RF + selected augmentation | 87.1% | 34.7% | **.667848** | 14.8 | 28.0 |
| TabPFN-2, inner F2 threshold | 81.2% | **36.5%** | .651386 | 13.8 | **24.2** |
| TabPFN-2, inner recall guard | **89.4%** | 26.1% | .598623 | **15.2** | 44.0 |

The F2 rule detects one fewer High student on average while saving 3.8 false warnings. The guarded rule detects .4 more while adding 16 false warnings. Average precision increases from .526861 to .615797 and ROC AUC from .808971 to .846176: this model orders students more effectively in aggregate, but that does not establish a better operational warning rule. These are five dependent repetitions of the same 97 students, not an independent confirmation or calibrated clinical risk probabilities.

**Design:** public original TabPFN-2 checkpoint (the Nature 2025 model), not current gated TabPFN-3.5. Eight Small B inputs; real training students only; original five repeats of five outer folds and four inner folds. 125 context fits in total. Fixed eight estimators, CPU, fixed per-fold seeds; sleep/study codes explicitly categorical. Raw inputs go through TabPFN's own preprocessing. No added survey features, synthetic survey rows, fine-tuning or parameter search. High remains primary BAT score >=4. Thresholds 0..1 by .05 are selected inside training only: maximize F2, or retain at least the selected RF's recorded inner recall and minimize false positives. Inner recall is not an outer guarantee. Reference RF predictions are copied exactly from the selected experiment, not fitted again in the new environment.

Run `.\.venv-tabpfn\Scripts\python.exe experiments/17-compare-tabpfn-high-burnout-warnings.py`; settings: [tabpfn-config.json](../experiments/17-compare-tabpfn-high-burnout-warnings-settings.json), dependencies: [requirements-tabpfn.txt](../experiments/dependencies-tabpfn.txt). The separate `.venv-tabpfn` can access existing system packages; new installs and matching NumPy/pandas versions were placed only in this environment. The original `.venv` was unchanged. A full environment freeze is saved with results. For a fresh setup, create this separate environment and install its requirements, then download the public checkpoint and license:

```powershell
.\.venv-tabpfn\Scripts\python.exe -c "from huggingface_hub import hf_hub_download; [hf_hub_download('Prior-Labs/TabPFN-v2-clf', name, revision='275f19d2add9c2c0de38f9ebaded3856599fa2e7', local_dir='results/17-tabpfn-local-cache') for name in ['tabpfn-v2-classifier-v2_default.ckpt','LICENSE.txt']]"
```

Checkpoint SHA-256: `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49`. Inference runs locally with Hugging Face offline mode and no survey upload. **Built with PriorLabs-TabPFN**; [official model and license](https://huggingface.co/Prior-Labs/TabPFN-v2-clf), [Nature paper](https://www.nature.com/articles/s41586-024-08328-6). Prior Labs License 1.1 has attribution requirements for distribution; a copy and model provenance are saved locally.

Separate ignored outputs contain 1,455 predictions (two new rules + RF reference), 15 repetition metric rows, three summaries, original fold assignments, 525 inner threshold candidates, 50 selections, ten paired comparisons, configs, source/checkpoint hashes and package versions. Independent verification passed (historical local file, unavailable here: results/17-tabpfn-comparison/20261114T124506935366Z/verification.json) for all prediction labels, counts, metrics/AP/AUC, candidates, tie rules, threshold decisions, original inner/outer folds, training membership, unchanged hashes and exact copied RF predictions. No models were refitted during verification, separate software test suite was run or deployment model saved. Earlier results and source data remain unchanged. Further threshold/calibration work would need training-only evaluation; it is not part of these results.

## Backward question selection (14 November 2026)

Completed separate results (historical local file, unavailable here: results/16-backward-question-selection/20261114T122443497555Z/results.md). **Keep the current eight-question RF.** Backward selection reduced High detection and F2 under both tested stopping rules. Earlier experiments and source data were preserved; the selected model was not replaced.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Current eight-question RF | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Backward selection, strict F2 improvement | 82.4% | 34.2% | .641302 | 14.0 | 27.2 |
| Backward selection, recall guard / fewer FP | 82.4% | 34.9% | .647200 | 14.0 | 26.2 |

These average five dependent repetitions of the same 97 real students. Both new rules detect .8 fewer High students per evaluation; false warnings decrease by .8/1.8 respectively. Each rule has lower F2 in four repetitions and ties the current RF in one. Better selected inner scores did not transfer to better held-out performance. This is one conditional greedy search, not proof that every subset or selection method fails.

Run `.\.venv\Scripts\python.exe experiments/16-remove-questions-by-backward-selection.py`; settings: [backward-selection-config.json](../experiments/16-remove-questions-by-backward-selection-settings.json). Start at all eight questions, evaluate every one-question removal on the original four inner folds and original .05-step warning thresholds. The F2 path accepts a removal only if inner F2 strictly improves (>1e-12). The recall-guard path requires at least the current RF's inner recall and accepts only strictly fewer false positives. Threshold ties follow the recorded metric order; child ties follow original question order. Stop when no removal improves the objective or one question remains. Identical subsets are cached across paths within each outer training group.

The search evaluated 345 subsets across 25 outer training groups. F2 selection retained 8/7/6/5 questions in 12/10/2/1 groups; guarded selection retained 8/7/6/5 in 16/7/1/1. Workload was retained in all selections under both paths. These are descriptive frequencies, not rules for selecting one global subset. The current RF settings, High weights and augmentation ratios are retained per outer training group; original full-eight generated pools are projected onto subsets, where duplicate projected profiles may occur. All path/stopping/threshold decisions use training data only. The existing recipe selection and new path selection reuse inner folds; excluded outer students evaluate the complete procedure. Inner recall constraints are not outer guarantees.

Outputs are separate under `results/16-backward-question-selection/`, excluded from Git. They include 1,940 predictions, 20 repetition metric rows, four summaries, confusion matrices, 345 saved inner score sets with 7,245 threshold rows, 79 recorded backward steps, 75 final decisions, selected questions/counts, ten paired changes, fold assignments, generation counts, configs and hashes. A full-eight control exactly reproduces the current RF. Independent verification passed (historical local file, unavailable here: results/16-backward-question-selection/20261114T122443497555Z/verification.json) for metrics/AP/AUC, every candidate and sibling removal, ties, strict stopping decisions, selected questions, original folds/recipes, training membership, generation counts and unchanged source/code hashes. No second RF-fitting run, separate software test suite or deployment fit occurred. Results remain exploratory on the same 97 students.

## Training-only question selection (14 November 2026)

Completed separate results (historical local file, unavailable here: results/15-four-six-eight-question-selection/20261113T220427919147Z/results.md). The UTC run folder is dated 13 November; the run completed on 14 November in Beirut. Comparing 4/6/8 existing questions did not improve the selected model's High detection or F2.

| Procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Current eight-question RF | **87.1%** | 34.7% | **.667848** | **14.8** | 28.0 |
| Training-selected 4/6/8 questions, F2 | 85.9% | 35.2% | .666235 | 14.6 | 27.0 |
| Training-selected 4/6/8 questions, recall guard | 85.9% | 35.2% | .666386 | 14.6 | 27.0 |

Means average five dependent repetitions of the same real students. Question selection removes one false warning per evaluation on average, at a cost of .2 fewer High detections. The two new procedures have similar rounded means but different selected settings/predictions. F2 selection kept all eight questions in 20/25 training groups (four in three, six in two); recall-guard selection kept all eight in 23/25 (four in one, six in one). Keep the current selected eight-question RF. This is one specified selector conditional on the existing RF recipe, not proof that all feature-selection methods fail.

Reproduce with `.\.venv\Scripts\python.exe experiments/15-select-four-six-or-eight-questions.py`; settings: [question-selection-config.json](../experiments/15-select-four-six-or-eight-questions-settings.json). Each training group independently ranks whole original questions using fixed unweighted L2 logistic regression (C=1) on standardized real training answers only. Question strength is grouped coefficient L2 norm divided by sqrt(encoded-column count); ties use questionnaire order. All dummy columns belonging to a chosen categorical question are retained. The ranking is refitted inside each inner training group and then on outer training data; no questions are globally chosen from the previous error table.

The current RF's original outer-training-selected parameters, High weight and augmentation ratio are retained, isolating question selection. The same full-eight generated pools are projected onto subsets; projected duplicates may occur. Candidate sizes 4/6/8 and the original .05 threshold grid are selected by inner F2 or by minimizing inner false positives while retaining the current RF's inner recall. This guard is not an outer-recall guarantee. Existing RF recipe selection and new question selection reuse the original inner folds; outer students remain excluded throughout. A full-eight control reproduces the current RF exactly. Original five-times-five stratified outer/four inner folds and real-only evaluation are retained.

Independent verification passed (historical local file, unavailable here: results/15-four-six-eight-question-selection/20261113T220427919147Z/verification.json): all 1,940 predictions, 20 repetition rows, four summaries, 1,575 candidate-threshold rows, 75 decisions and ten paired comparisons were checked. All 125 ranking models were independently refitted on their verified real training IDs; coefficients, ranking order, original RF recipe, whole-question lists, folds and source hashes matched. Saved outputs also include all rankings/strengths, inner scores and selected questions. No second RF-fitting run, separate software test suite or deployment fit occurred. Previous data/results and selected models remain unchanged; all results remain exploratory on 97 students.

## Selected RF error inspection (13 November 2026)

Completed descriptive findings (historical local file, unavailable here: results/14-random-forest-false-warnings/20261113T215342740935Z/findings.md). **No model was trained or changed; current metrics are unchanged.** Of 80 real Below-high students, 39 were falsely warned at least once across five repetitions, 27 in at least three repetitions and 41 never. Of 17 High students, 16 were detected at least once and one was never detected. These are unique-student counts; the 140 false-warning events reuse the same students (28 per repetition on average).

False warnings were not mainly near the boundary: only 6/39 falsely warned students scored 3.5..<4, accounting for 26/140 false-warning events (18.6%). Sixteen scored below 3 (57 events), while 17 scored 3..<3.5 (57 events). Thus 81.4% of false-warning events involved scores below 3.5. This does not establish clinical status; the model's target is the study-defined measured score >=4.

| Existing input (1-5) | Falsely warned Below-high students (39) | Correctly warned High students (16) |
|---|---:|---:|
| Workload, mean | 3.79 | 4.62 |
| AI dependence, mean | 3.08 | 3.81 |
| University support, mean | 2.31 | 1.81 |

The full report compares all eight inputs, sleep/study category distributions, persistent warnings and closest High profiles. Each student is counted once in feature comparisons. Differences are descriptive, not validated feature importance or causal effects. The RF already uses these questions. The always-missed High student scored 4.083, reported workload 4 and AI dependence 2, so a universal high-AI-dependence requirement would not cover every High student. No exact eight-answer pattern in this dataset had students on both sides of the class boundary; approximate similarity does not establish an unavoidable error floor.

Next proposed experiment: compare a small set of subsets of the existing eight questions, with subset selection learned inside training validation and the full eight-question RF retained as a reference. Do not select questions globally from this error table, exclude hard students or redefine High. Error inspection uses the same 97 students and any follow-up remains exploratory. This experiment has not been run.

Reproduce with `.\.venv\Scripts\python.exe experiments/14-inspect-random-forest-false-warnings.py`. Separate ignored output root: `results/14-random-forest-false-warnings/`. Saved files include all 97 student warning summaries and eight inputs, 485 selected held-out predictions, score bands, all answer distributions, ordinal summaries, 117 nearest-peer rows, 78 paired input rows, exact-pattern checks, hashes and independent verification (historical local file, unavailable here: results/14-random-forest-false-warnings/20261113T215342740935Z/verification.json). The existing fixed mixed-feature distance helper was reused. All counts, summaries, distances and source hashes passed; no software test suite, model fitting or deployment change was performed.

## Current RF plus logistic regression (13 November 2026)

Completed separate ensemble experiment (historical local file, unavailable here: results/13-random-forest-logistic-voting/20261113T203744495093Z/results.md). This uses the user's **current 87.1%-recall RF**, not the expanded forest from the later tuning experiment. Original data, endpoints and earlier results were preserved.

| Procedure | High recall | High precision | F2 | False warnings /80 |
|---|---:|---:|---:|---:|
| Current selected RF | **87.1%** | 34.7% | .667848 | 28.0 |
| Same RF, finer threshold only (both rules identical) | **87.1%** | 34.8% | .669090 | 27.8 |
| RF/logistic mixture with inner recall guard | 85.9% | 35.7% | **.669893** | 26.4 |
| RF/logistic mixture selected by F2 | 83.5% | **37.2%** | .666125 | **24.4** |

These average five dependent repetitions of the same students. The guarded mixture removes 1.6 false warnings while detecting .2 fewer High students per evaluation than the current RF. It selects pure RF in 19/25 training groups. Finer RF-only threshold tuning preserves the observed mean recall but removes just one false warning across all five repetitions (28.0 to 27.8 on average). This is a tiny change, not a substantial upgrade. Keep the current RF as the user's selected procedure; record the threshold refinement and mixtures as exploratory alternatives.

The initial error comparison used matched real held-out predictions: across five repetitions, logistic was correct on 56 of the RF's 140 false warnings, but it missed nine High cases the RF caught and rescued only two High cases it missed. Such disagreement motivated the experiment but is not a rule for correcting individual evaluation labels. Only training data selected mixtures and thresholds.

Run `.\.venv\Scripts\python.exe experiments/13-blend-random-forest-and-logistic-warnings.py`; settings: [voting-config.json](../experiments/13-blend-random-forest-and-logistic-warnings-settings.json). It retains Small B, the original >=4 outcome, identical 5x5 outer/4 inner stratified folds, recorded RF augmentation/parameters/High weights and real-only logistic settings. Endpoints are refitted inside the original inner training groups to form score combinations, and on outer training groups for evaluation. The original endpoint outer predictions and selected inner confusion metrics must reproduce. Endpoint settings and mixture selection reuse the same inner folds; excluded outer students evaluate the full process. RF weights are 1/.9/.75/.5, with thresholds 0..1 by .025. A training recall guard requires at least the current RF's recorded inner recall and minimizes false positives; it does not guarantee outer recall. Matched RF-only threshold controls distinguish score mixing from threshold adjustment. Raw weighted outputs are uncalibrated warning scores, not personal risk probabilities.

Independent verification passed (historical local file, unavailable here: results/13-random-forest-logistic-voting/20261113T203744495093Z/verification.json) for all 3,395 predictions, 35 repetition metric rows, seven summaries, 485 endpoint error comparisons, 4,100 inner candidate-threshold rows, 100 rule selections and 50 paired comparisons. It reconstructed mixed outer scores directly from the original endpoint predictions and checked source/code hashes and original folds. No software test suite, calibration or deployment model was run. This remains exploratory after inspecting and repeatedly evaluating the same 97 students.

## Focused Random Forest tuning (13 November 2026)

Completed separate run: results (historical local file, unavailable here: results/12-random-forest-tuning/20261113T154534173272Z/results.md). Expanded F2 tuning reduced false warnings but also reduced High detection. Keep the user's current selected RF as the High-detection reference; this is a new trade-off, not a clear improvement on every metric.

| Small B RF procedure | High recall | High precision | F2 | Detected /17 | False warnings /80 |
|---|---:|---:|---:|---:|---:|
| Current selected augmentation | **87.1%** | 34.7% | .668 | **14.8** | 28.0 |
| Expanded F2 tuning | 84.7% | 37.1% | **.673** | 14.4 | 24.6 |
| Inner recall >=85%, then minimum false positives | 82.4% | **38.0%** | .668 | 14.0 | **22.8** |

These average five dependent repetitions of the same 97 students. Expanded F2 tuning gained .0055 mean F2 and removed 3.4 false warnings at a cost of .4 fewer detected High students per evaluation. Its F2 improved in three repetitions and declined in two; false warnings fell in all five. The constrained rule removed 5.2 false warnings at a cost of .8 fewer High detections; it did not achieve its training recall target on outer evaluation. Average precision declined from .527 for the selected procedure to .484/.493 for the two new rules, so the warning results do not establish a uniform improvement in ranking. Do not select a final threshold or parameter set by reading outer results. Given the user's priority of High detection, retain the current procedure unless accepting fewer detections for fewer false warnings is an explicit choice.

Independent verification passed (historical local file, unavailable here: results/12-random-forest-tuning/20261113T154534173272Z/verification.json): all 2,425 predictions, 25 repetition rows, five summaries, 2,700 candidate models' saved inner scores, 110,700 threshold metric rows, 50 outer training selections and 30 paired comparisons were checked. All 125 original synthetic pools (1,360 profile instances) reproduced; training-only parents, constraints, novelty, original folds, selected reference candidate metrics and source hashes were verified. One generated instance coincidentally matched an excluded real profile, as in the retained reference; evaluation inputs were not consulted during generation. No separate software test suite, second fitting run or deployment model was run.

Run `.\.venv\Scripts\python.exe experiments/12-tune-high-burnout-random-forest.py` from the repository root. Settings: [forest-tuning-config.json](../experiments/12-tune-high-burnout-random-forest-settings.json). Each run creates a separate timestamped folder under `results/12-random-forest-tuning/`, excluded from Git. Only interpret a complete manifest; previous results and source datasets remain read-only.

This uses the selected eight Small B inputs and the same primary score >=4 High boundary, five repetitions of five stratified outer/four inner folds, real-only evaluation and synthetic generator as the retained augmentation run. Generated training pools must reproduce the previous saved profiles exactly. No new questionnaire inputs or forced 50/50 balancing are introduced.

Each outer training group compares 108 candidates: depth 2/3/5, minimum leaf 5/10, encoded inputs considered per split `sqrt`/all, High weight 1/2/4 and augmentation none/half/full. Each forest has 100 trees with the original deterministic seed. One native computational thread per worker is used, with two worker processes. Preprocessing and augmentation occur independently within each inner training group. The same 108 sets of real inner out-of-fold scores support both selection rules, using 41 warning thresholds from 0 to 1 in .025 steps.

`expanded_f2` jointly selects settings, High weight, augmentation and threshold by maximum inner F2; ties favor precision, recall, a higher threshold, less augmentation and stable grid order. `recall85_min_fp` requires pooled real inner recall >=85%, then minimizes false positives; ties favor recall, precision, F2, a higher threshold, less augmentation and stable order. Threshold zero makes the constraint feasible. With only 13/14 High students in an outer training group, the inner constraint requires detecting at least 12 of them: 92.3%/85.7%. It does not guarantee 85% recall on excluded outer students.

The report compares both rules with unchanged matched-fold predictions from the currently selected RF, real-only RF and threshold-tuned blend. Saved artifacts include all candidate inner scores and threshold metrics, selected settings, outer predictions, repetition/summary metrics, confusion matrices, paired comparisons, generated profiles/counts, fold assignments, configs and hashes. The expanded search contains the previous grid and thresholds, and runtime assertions require its best inner F2 to be at least the previous selected procedure's; that is not an outer-performance guarantee. No deployment model is saved. Repeated use of 97 students remains exploratory; synthetic labels are assumptions and weighted outputs are uncalibrated.

## Unique synthetic-data binary experiment (12 November 2026)

Completed run, reviewed 13 November: full results (historical local file, unavailable here: results/11-classifier-training-augmentation/20261112T125001425382Z/results.md). All four classifier families were trained on both existing input sets with half/full synthetic batches, plus a procedure that chooses no/half/full augmentation using training validation only. Evaluation used only the 97 real students. High still means measured score >=4.

| Procedure | High students detected (recall) | Correct warnings (precision) | F2 | False warnings /80 |
|---|---:|---:|---:|---:|
| Small B XGBoost, training-selected augmentation | 85.9% | 35.8% | .670 | 26.4 |
| Small B forest, training-selected augmentation | 87.1% | 34.7% | .668 | 28.0 |
| Broad D logistic, training-selected augmentation | 82.4% | 37.1% | .661 | 24.0 |
| Existing blend, training-selected warning threshold | 80.0% | 37.8% | .653 | 22.4 |
| Small B XGBoost, real-only | 83.5% | 33.4% | .642 | 28.4 |

These average five repetitions of the same students. Synthetic augmentation modestly helped some classifiers; it did not help every procedure. The leading mean F2 was Small B XGBoost with the training-selected batch size. Compared with real-only XGBoost, it detected 14.6 rather than 14.2 of 17 High students and reduced false warnings from 28.4 to 26.4. Compared with the blend, it detected one extra High student but added four false warnings on average. Its F2 exceeded the blend in three of five repetitions, so this remains an exploratory trade-off, not an established winner. No numeric score MAE improvement is claimed. Keep the selected regression blend for score prediction; retain augmented XGBoost as a warning candidate for comparison.

All 2,720 requested profile instances were generated across 250 separate training pools (3,087 attempts, no shortfalls). This is not 2,720 additional students: pools recur across validation fits. Independent checks reproduced all 180 repetition rows and 36 summaries from 17,460 predictions, checked all 600 tuning records, training-only parents, profile domains/interpolation/novelty and unchanged source hashes. See verification.json (historical local file, unavailable here: results/11-classifier-training-augmentation/20261112T125001425382Z/verification.json). One generated profile coincidentally matched an excluded real profile; generation never consulted excluded profiles, and uniqueness is guaranteed relative to its own training pool only. Synthetic labels remain assumptions, and most warnings are false relative to the study's >=4 boundary. No final model was saved.

Run `.\.venv\Scripts\python.exe experiments/11-augment-high-burnout-classifiers.py` from the repository root. Settings: [augmentation-config.json](../experiments/11-augment-high-burnout-classifiers-settings.json). Uses the existing environment and no new dependency. New timestamped folders are written under `results/11-classifier-training-augmentation/`, excluded from Git. Preserve prior results and only interpret a complete manifest.

All four binary classifier families (logistic, forest, XGBoost, histogram boosting) retain both input sets, exact grids, High weights 1/2/4, F2/threshold tuning, seeds and stratified folds from the completed binary run. Real-only predictions and training-validation choices are reused from that pinned, unchanged reference. Both augmented procedures retrain every family with their settings/thresholds tuned inside each outer training group. Two worker processes fit independent input/fold jobs, with one native computational thread per worker.

Only High training students generate examples. For each training fit, the full pool requests one new profile per real High student. The half batch uses a prefix of size ceil(half the real High count); the full batch uses the available pool. Inner and outer training pools are regenerated independently with fixed seeds. A separate inner-selected-ratio procedure chooses 0/.5/1 by training F2, precision, recall, threshold and finally lower ratio; outer evaluation never selects a batch size.

The mixed-feature distance is the mean of ordinal absolute differences divided by 4 and nominal/binary mismatches. Each High anchor has up to three nearest High neighbors with distance <=.35 and maximum ordinal gap 2. A generated profile copies the entire categorical/binary block from the anchor (including academic categories, enrollment and AI-use indicators); it stochastically rounds ordinal interpolation using a fraction .2..8. The resulting distance from its anchor must be <=.25. Every answer stays in its allowed domain. Exact matches to any real training profile or previously accepted generated profile are rejected. Generation stops after 200 attempts per requested example; shortfalls are reported without weakening constraints. No held-out profile is consulted or used to filter generated examples.

These are assumptions about local response patterns. Neither legal values, proximity nor uniqueness establishes real human plausibility or correct High labels. The binary synthetic label is inherited from two High parents, not observed from BAT answers; no numerical burnout scores are invented. Augmentation also changes training emphasis; no matched-extra-weight control isolates that mechanism. Only real students enter evaluation. Original SAV, Google Forms data and SPSS analyses remain unchanged.

Saved outputs include `synthetic-profiles.csv` with parents, interpolation fraction, distances and training-fold provenance; `generation-counts.csv` with attempted/requested/accepted counts; all inner/outer assignments; predictions, repetition/summary metrics, confusion matrices, paired changes against matched real-only models and tuned blend, all tuning records, configs and hashes. The profile CSV contains the columns relevant to its input set; other-set fields are blank by design. Profiles may recur across separate training folds, but are unique within each training pool. Raw profile counts across repeated fits are not additional independent students. Runtime assertions check uniqueness, domains, parent labels, finite predictions, original fold equality, score/threshold alignment and unchanged sources. No deployment artifact or separate software test suite is run.

## Binary High / Below-high warning experiment (12 November 2026)

Completed run: `results/10-high-burnout-classifiers/20261112T115553112588Z/`. The refitted ridge/SVR blend with an inner-selected warning threshold had the highest mean F2 (.653), with 80.0% recall, 37.8% precision and 22.4 false warnings per 80 Below-high students. Small B logistic regression was effectively close (.651 F2, 78.8% recall, 39.0% precision, 21.4 false warnings). Small B forest caught 84.7% but precision was only 32.7%. Histogram boosting did not lead. The blend at fixed score threshold 4 caught 25.9% with 62.1% precision: lowering the warning trigger improved detection while increasing false warnings. The measured High label remains >=4; the warning threshold changes neither that label nor numerical score accuracy. See [analysis progress](06-data-analysis-and-experiment-history.md) for all tuned procedures and checks. No deployment threshold or model has been fitted/saved on all students.

Run `.\.venv\Scripts\python.exe experiments/10-compare-high-burnout-classifiers.py` from the repository root. Settings: [binary-config.json](../experiments/10-compare-high-burnout-classifiers-settings.json). Each run creates a separate folder in `results/10-high-burnout-classifiers/`, excluded from Git. Earlier regression and three-class outputs remain unchanged. Require `status: complete` in the manifest before interpreting results.

Use the existing project environment, including the already-used XGBoost dependency in [requirements-xgboost.txt](../experiments/dependencies-xgboost.txt). No new dependency is introduced. Exact installed package versions are recorded in each manifest.

The target is primary `burnout_score >=4` (17 High students) versus `<4` (80 Below-high students). These are study-defined score groups; Below-high does not mean no risk. The input sets remain Small B (8 existing answers) and Broad D (23), with no BAT predictors, additional questions or synthetic records.

Logistic regression, Random Forest, XGBoost and scikit-learn histogram gradient boosting share five stratified outer folds repeated with the five original seeds, and four stratified inner folds. These splits differ from the old regression and three-class experiments. Preprocessing reuses existing one-hot encoding and standard scaling, fitted in each training group. Native histogram categorical handling is disabled because categories are already encoded. All fits use one computational thread. Solvers stop on convergence warnings.

Classifiers jointly tune parameters, normalized High weights 1/2/4 and probability thresholds 0 to 1 in .05 steps. Logistic C is .1/1/10. Random Forest has 100 trees, depth 2/3, minimum leaf 5/10. XGBoost has 100 trees, depth 1/2, learning rate .03/.1, minimum child weight 5 and lambda 10, using histogram trees and full row/column sampling. Histogram boosting has 100 iterations, learning rate .05, leaf limit 3/7, minimum leaf 10 and L2 penalty 1/10; early stopping is disabled.

The objective is pooled inner F2 = `5TP/(5TP+4FN+FP)`, prioritizing recall while accounting for false warnings. Ties favor precision, recall, larger threshold, then stable grid order. Settings and thresholds reuse the same inner out-of-fold predictions; only excluded outer students evaluate the complete procedure. The same selected fitted model is also reported at threshold .5 as a diagnostic, not as an independently tuned .5 model. Classifier probabilities are uncalibrated model outputs, not established individual clinical risk estimates.

For a matched comparison, the selected 50/50 Small B weighted-ridge / Broad D high-priority SVR blend is refitted and retuned on these same new folds using its saved endpoint selection rules. Its mixing share stays fixed. Its warning threshold is chosen by inner F2 from the configured score grid (including always-positive/always-negative extremes), with a separate score-threshold-4 reference. Blend scores are continuous burnout estimates, not probabilities. Old saved predictions from different folds are not substituted.

Two baselines flag everyone or no one. Report precision, recall, F2, false-positive rate, TP/FP/FN/TN, specificity, accuracy, balanced accuracy, ROC AUC and average precision. ROC/AP are discrimination diagnostics; they do not establish probability calibration. Metrics and counts average five repetitions of the same students, not five independent datasets. Counts in the summary may be fractional.

Outputs include held-out scores/labels/thresholds, outer and inner validation assignments, per-repetition and summary metrics, confusion matrices, repetition spread, paired differences against both blend warning procedures, all tuning candidates/choices, configs and source hashes. Runtime assertions check label boundaries, prediction completeness, probability bounds, score alignment, fold separation and unchanged sources. No separate software test suite or deployment model is run. A model's best-looking outer score remains exploratory after prior inspection of these students; acceptable recall, precision and clinical utility thresholds are not established.

## Historical three-class experiment

## First completed run

Run `results/09-three-group-classification/20261102T151940669629Z/` completed on 2 November 2026. Its manifest confirms unchanged source files. Four software checks passed before fitting. The table below averages five repetition metrics; this is not five independent samples.

| Inputs / method | Accuracy | Macro F1 | Low recall | High recall | High precision |
|---|---:|---:|---:|---:|---:|
| Majority baseline | 76.3% | .288 | 0.0% | 0.0% | 0.0% |
| Small B logistic | 68.5% | .441 | 6.7% | 50.6% | 48.5% |
| Small B forest | 55.1% | .430 | 26.7% | 72.9% | 38.9% |
| Broad D logistic | 70.1% | .449 | 10.0% | 45.9% | 44.8% |
| Broad D forest | 57.9% | .445 | 23.3% | 76.5% | 38.7% |

Broad D forest captured more High cases, but flagged 25.8% of non-High cases as High, and most High flags were incorrect. Low detection remained poor. Broad D logistic had the highest mean macro F1 by a small margin; that alone does not establish a definitive winner. No model exceeded the majority baseline's accuracy, although all learned models had higher macro F1/balanced accuracy and detected some minority cases. This illustrates why ordinary accuracy is insufficient for this problem. Read the full report and confusion matrices before choosing a research application.

This is separate from every regression experiment. Existing data, scores and results are preserved.

## Outcome

Use the primary 12-item `burnout_score` to define **study-created symptom bands**:

| Code | Label | Score | Students |
|---|---|---|---:|
| 0 | Low | 1 <= score < 2 | 6 |
| 1 | Middle | 2 <= score < 4 | 74 |
| 2 | High | 4 <= score <= 5 | 17 |

These are not published clinical cutoffs. Exactly 2 belongs to Middle and exactly 4 to High. We do not change boundaries to improve performance or balance classes. Only six Low students means substantial uncertainty in its performance.

## What is compared

A shared training-majority baseline and regularized logistic regression / constrained Random Forest on Small B and Broad D. Use the input lists and category definitions recorded in the reference regression configuration; no BAT-derived predictors or Q20 enter the models. Broad D has many encoded columns for only 97 students, so its stability is an important limitation.

Logistic C is .1/1/10. Forest has 100 trees, depth 2/3, minimum leaf size 3/5. Both compare no class weighting with balanced weights. Learned preprocessing and automatic class weights use the current training group only. No augmentation or oversampling.

Three stratified outer folds are repeated with five fixed seeds, with two-fold inner selection by macro F1. Three outer folds put two Low students in every evaluation group. All classifiers use identical splits. These are different splits from the earlier regression; accuracy cannot be directly compared with regression MAE. Final predictions are probability argmax; no threshold tuning occurs in this run.

## Run

From the repository root, using the existing project environment:

```powershell
.\.venv\Scripts\python.exe experiments/test_09_three_group_classification.py
.\.venv\Scripts\python.exe experiments/09-classify-low-middle-high-burnout.py
```

No extra dependencies beyond the existing modeling environment are required.

Each run writes `results/09-three-group-classification/<UTC timestamp>/`, excluded from Git because it contains individual results. Open `results.md` and confirm `manifest.json` says `complete`. CSVs include class counts, individual scores/predictions/probabilities, group assignments, per-repetition metrics, stability summaries and confusion matrices. Tuning records and exact configurations are retained. No deployment model is saved.

## Interpretation

Macro F1 is the tuning metric, giving all three classes equal importance; this is not an exclusively High-recall objective. Report every class's precision, recall and F1, balanced accuracy, ordinary accuracy, and High false-positive rate. The baseline accuracy is already 74/97 = 76.3%, despite zero Low or High recall. Undefined precision/F1 is set to zero explicitly.

Metrics average five repetitions. Students are reused, not multiplied; the sample remains 97. Each confusion matrix represents one repetition with 97 predictions, not a new sample. This follow-up was chosen after seeing prior results and is exploratory. Clinical validity and external performance are not established. Preserve all results even if the classification experiment performs poorly.
