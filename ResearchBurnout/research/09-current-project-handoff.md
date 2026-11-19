# ResearchBurnout: full handoff for a new chat

Repository organization updated **19 November 2026**. Start with [the project README](../README.md) for the four-folder layout. Scripts/settings now share experiment numbers 00–25 in `experiments/`; [the file catalog](12-file-renaming-catalog.csv) maps previous names. The verified original validation run and original source namespace are preserved in `results/99-original-workspace-and-verified-validation.zip`; readable findings are in [the renamed validation report](../results/25-random-forest-validation-report.md). Earlier timestamped paths below describe historical runs, not available current directories. No scientific results or model settings changed during reorganization.

Updated **18 November 2026**, Asia/Beirut. Read this before continuing. This replaces the October handoff and summarizes the recorded work; it is not a fresh training run or audit of every historical result.

## Validation completed, 18 November 2026

The authorized [model-validation plan](11-random-forest-validation-plan.md) is complete; read [the verified report](../results/25-random-forest-validation-report.md). Local historical model/output folders are absent; raw CSV/SAV hashes match the prior record. Focused regeneration reproduced all seven recorded RF means exactly on the original 25 outer folds. A new workload-only logistic baseline catches 16/17 High students with 28 false warnings (94.1% recall, 36.4% precision), versus RF 14.8/17 with 28 (87.1%, 34.7%). Paired conditional intervals include zero for RF minus workload; this challenges the need for the RF without establishing a validated replacement. Workload-only average precision is lower (.423 versus RF .527), so the warning-rule result does not mean it improves every ranking metric.

All 199 full-procedure student-label permutations finished under `results/25-random-forest-validation/20261118T143652947217Z/`. Mean balanced accuracy .760294 exceeded every null run (mean .495704, max .636103); corrected p=.005. This tests the frozen procedure, not the entire historical many-model search. Verification checked 5,000 folds/180,000 candidate choices, regenerated all 125 real training pools, refitted 25 selected real outer models, replayed one full real/one full null search and independently scored all null procedures/recomputed the p-value. Nine relevant tests pass. Read the report and local manifest/verification for scope. No new experiment is pending or implied by this completed task.

No source dataset, selected recipe, final-model threshold or historical results were replaced. Statements below about the final artifact describe the previous working copy: **`results/23-selected-random-forest.joblib` and metadata are missing here**. The audit preserves a recipe/schema record, not a recovered trained binary or backup. The old 93.5% synthetic inference check remains historical and separate. Keep the RF as the historical research reference; report the simpler comparator before claiming eight inputs are necessary or planning a demo. Further work follows the user's next request.

## 1. Current position and decisions

- This is a potential research paper and presentation about student burnout, GenAI habits and study conditions. **SPSS work and many modelling experiments have already been completed.** Do not restart from old statements that modelling has not begun.
- There are **97 real respondents**. The user cannot add more survey features or collect more samples for this modelling phase. Work with the existing data.
- The user selected the **Small B eight-input Random Forest classifier with training-selected augmentation**. Its means are **87.1% High recall, 34.7% precision, F2 .667848 and 28.0 false warnings per 80 Below-high students**. Keep it as the selected research classifier unless an authorized, verified comparison justifies another choice.
- A separate **fixed 50/50 weighted-ridge / high-priority SVR blend** remains the selected numerical-score research predictor: **.6160 overall MAE / .6422 High-score MAE**. Do not confuse its errors with classifier metrics.
- Latest alternative-input, SVC and Boruta comparisons did not improve the classifier's detection/false-warning priority. The RF was not replaced.
- **A final classifier artifact was documented in the previous working copy, but is missing here:** `results/23-selected-random-forest.joblib` and `selected-rf-metadata.json`. Its recorded fit includes preprocessing and a 100-tree RF, fitted on all 97 real students after training-only selection: depth 3, min leaf 10, High weight 2, threshold .35, augmentation ratio 0. No synthetic rows entered that final fit. The score-regression blend remains unexported. CV metrics describe the research procedure, not an independent evaluation of an all-data artifact.
- PCA/PLS, interaction and dependent mixed loss-tuning artifacts were deliberately deleted on 16 November. Their recorded methods/results remain. Do not restore them without a request.

## 2. How to continue with the user

Explain in simple words, short sections and concrete examples. Define metrics before interpreting them. The user repeatedly requested step-by-step, ADHD-friendly explanations.

Explain the plan before substantial new experiments. Preserve current results and place authorized comparisons in separate folders. Report actual results and trade-offs. Reproducing the existing 87.1% RF is not a new improvement. Do not guarantee better metrics or describe synthetic profiles as independent real students.

The user wants to discuss unsuccessful experiments honestly in the paper and presentation. Keep important methods/results documented, while grouping repetitive parameter trials. Do not run another experiment, delete more files, commit or push just because this handoff mentions possible future work. Follow the next user request and applicable repository instructions.

## 3. Read these files

Current repository root: `C:\Users\user\Desktop\M2-Porjects\ResearchBurnout`. Older paths below belong to the previous working copy.

| Path relative to root | Purpose |
|---|---|
| `research/09-current-project-handoff.md` | This current summary |
| `research/06-data-analysis-and-experiment-history.md` | Detailed scoring, SPSS/coding review, experiments, exact tables and deletion history |
| `research/07-classification-experiments-and-methods.md` | Classifier comparisons, methods, local outputs and verification |
| `research/08-score-prediction-experiments-and-methods.md` | Regression instructions and historical summaries of removed experiments |
| `research/10-project-work-and-decision-history.md` | Current decisions and chronological work history; older entries are historical |
| `research/02-student-survey-questionnaire.md` | Exact questions/options and Google Forms code |
| `research/03-burnout-assessment-source-questionnaire.md` | Instrument reference |
| `research/13-dataset-preparation-and-corrections.md` | Data history and rebuild cautions |
| `research/14-literature-search-records.csv`, `research/15-literature-dblp-records.xlsx` | Literature metadata; original papers still require verification |
| `research/01-study-goals-and-design.md`, `research/04-original-prediction-experiment-plan.md` | Earlier design/planning context, not necessarily latest status |

The root README now reflects the current modelling status. The work plan retains an explicitly labelled October historical checklist; its pending statuses are not current tasks. Former paths mentioned in deletion-marked historical sections are not available files or current commands.

## 4. Data and study scope

The survey has **20 non-BAT questions and 23 BAT-S items**, Q1-Q43. It is cross-sectional. Models estimate/classify current measured symptoms; there is no later outcome validating future burnout or early warning, and no causal design proving that AI use causes burnout.

Keep **all 97 students**. Q1 has 87 Yes and 10 No responses about enrollment in Lebanon. The researcher identified the No group as Lebanese students studying abroad and explicitly said not to exclude them. Q1 alone does not establish nationality or private/public university status.

- Working data: `data/03-prepared-student-burnout-data.sav`, **97 rows / 66 variables**.
- Original reconstruction source: `data/01-original-student-survey.csv`.
- SPSS output: `results/00-spss-descriptive-statistics.spv`.
- Python loaders reconstruct **three missing AI-summary-use indicators from original answers in memory**, without changing the SAV or guessing values.
- Required Google Form answers do not guarantee correct imported/derived variables. Preparation/recode corrections are documented in the progress record.
- Do not overwrite raw exports or run the older SPSS rebuild over the current SAV; read `research/13-dataset-preparation-and-corrections.md` first.

Recorded SHA-256:

```text
burnout-data.sav:
ab50404a31ecbc7115b52fe6f0be1328128d45951deca70374e79b8ed4f4ce4a
survey-export-spss.csv:
d8d4323901dd5b6f4602c5a3b6850a965e86d1a58ec7f984b59aa05cf369830e
```

## 5. Outcomes and labels

### Primary: `burnout_score`, 12 specified items

| Dimension | Items averaged |
|---|---|
| `exhaustion` | BAT21, BAT23, BAT24 |
| `mental_distance` | BAT29, BAT31, BAT33 |
| `cognitive_impairment` | BAT34, BAT37, BAT38 |
| `emotional_impairment` | BAT39, BAT40, BAT43 |
| `burnout_score` | The four dimension means |

Each dimension requires its three items (`MEAN.3`); the overall score requires four dimensions (`MEAN.4`). Because each dimension has three items, this is also the mean of those 12 items. Scores range from 1 to 5.

### Secondary: `burnout_score_23`

| Dimension | Items averaged |
|---|---|
| `exhaustion_23` | BAT21-BAT28, eight items, `MEAN.8` |
| `mental_distance_23` | BAT29-BAT33, five items, `MEAN.5` |
| `congnitive_impairement_23` | BAT34-BAT38, five items, `MEAN.5` |
| `emotional_impairment_23` | BAT39-BAT43, five items, `MEAN.5` |
| `burnout_score_23` | Mean of these four means, `MEAN.4` |

The cognitive misspelling is the recorded SAV variable name; check callers before renaming. The secondary score **is not the simple mean of all 23 items**: it gives the four dimensions equal weight. It also ranges from 1 to 5.

### Current binary target

```text
High       = measured primary burnout_score >= 4 : 17 students
Below-high = measured primary burnout_score <  4 : 80 students
```

These are study-defined score groups, **not clinical diagnoses**. Below-high does not mean symptom-free or no risk.

Do not confuse the measured-score **label boundary 4** with the model's **warning threshold**, selected from inner training predictions and applied to an uncalibrated classifier output. The selected RF learns the class directly; it does not first predict a numerical BAT score. Some regression-blend reference procedures do threshold predicted scores, which is a different method.

## 6. SPSS work already completed

Reviewed transformations, numeric recodes, labels/measures and calculated scores. Ran reliability, frequencies/descriptive output, Explore plots and exploratory correlations. Exact tables/caveats remain in `research/06-data-analysis-and-experiment-history.md`.

| Item set | Short-form alpha | Full-core alpha |
|---|---:|---:|
| Exhaustion | .781 | .909 |
| Mental distance | .733 | .820 |
| Cognitive impairment | .876 | .919 |
| Emotional impairment | .775 | .839 |
| All items | .900 (12 items) | .944 (23 items) |

All designated items were retained. Small alpha gains after deleting items did not justify changing scales. Alpha measures consistency, not prediction accuracy, validity or unidimensionality. The 23-item alpha is not exactly the reliability of the dimension-weighted secondary score.

Exploratory Spearman correlations with the primary score: avoidance **.445**, workload **.388**, AI dependence **.377**, academic stress **.367**, offloading **.331**, AI-accusation anxiety **.278**, AI frequency **.220**, financial strain **.196**, support **-.148**, internet **-.059**, AI verification **-.010**. Workload/stress correlate **.672**. Pearson AI dependence/burnout was **.361**.

These same-sample associations were not adjusted for multiple testing. They do not establish causes or incremental predictive value. Do not select inputs using full-sample p-values and call subsequent validation independent. The AI items have not been established as one validated combined scale.

Value labels are not transformations: recoding strings and describing numeric codes are different operations. Sleep/study codes are categories, not actual hours; model encoding follows the saved config, not just SPSS's Measure field.

Q9 is one multi-select AI-use question expanded into five 0/1 indicators (concepts, writing, coding, summaries, direct solutions), not five Likert questions.

## 7. Input sets

### Selected Small B: eight inputs, saved order

| Question | Variable | Meaning |
|---|---|---|
| Q15 | `workload` | Heavy/overwhelming workload |
| Q16 | `sleep_duration_code` | Nightly sleep category |
| Q14 | `study_hours_code` | Independent weekly study category |
| Q7 | `financial_strain` | Financial strain |
| Q19 | `university_support` | Institutional/instructor support |
| Q8 | `ai_frequency` | Academic AI-use frequency |
| Q10 | `ai_dependence` | Dependence on AI to complete work |
| Q11 | `ai_offloading` | Reliance on AI instead of independent thinking |

### Full eligible Broad D pool: 23 variables / 37 encoded columns

```text
enrolled_lebanon, academic_level_code, major_code, gpa_code,
electricity_code, internet, financial_strain, study_hours_code,
workload, sleep_duration_code, academic_stress, avoidance,
university_support, ai_frequency, ai_use_concepts, ai_use_writing,
ai_use_coding, ai_use_summaries, ai_use_solutions, ai_dependence,
ai_offloading, ai_verification, ai_anxiety
```

Twenty-three variables does not mean 23 independent questions because Q9 supplies five indicators. Q20 `leave_intention` is excluded. BAT items and BAT-derived scores/dimensions must not be predictors of the BAT-derived target.

Earlier score experiments used Small A (the five Small B study-condition inputs without its three AI inputs), Small B (eight), Broad C (the first 13 variables above, without AI variables), and Broad D (23). Not every algorithm ran on every set; check actual run settings.

## 8. Selected classifier: exact run and method

```text
results/11-classifier-training-augmentation/20261112T125001425382Z/
input_set = small_b
model = forest
augmentation = inner_selected_ratio
```

Runner: `experiments/11-augment-high-burnout-classifiers.py`; config: `experiments/11-augment-high-burnout-classifiers-settings.json`. Its real-only reference is `results/10-high-burnout-classifiers/20261112T115553112588Z/`. Use the saved run's `binary-config.json`, `reference-config.json` and `tuning.json` as the exact specification.

RF search: **100 trees**, max depth 2/3, min leaf 5/10. Relative High weights 1/2/4 normalized to mean one per fit; augmentation ratios 0/.5/1. Warning thresholds 0..1 by .05. These settings can differ across cross-validation folds. The separately saved final fit now has one fixed recipe, described below.

Inner selection maximizes F2, then precision, recall and higher threshold; augmentation ties prefer smaller ratios. F2 = `5TP/(5TP+4FN+FP)` emphasizes recall while penalizing false warnings.

Five stratified outer folds repeated with seeds **104729, 130363, 155921, 181081, 205019**; four inner folds with seeds derived from base **271828** plus repetition/fold. All preprocessing, selection, generation and tuning use the relevant training group. Only excluded real students evaluate.

These are **97 people evaluated repeatedly**, not 485 independent people. Report mean repetition metrics. Earlier regression/three-class folds differ; use matched comparisons. Inner recall guards in later experiments are not guarantees of outer recall.

| Selected RF metric | Mean |
|---|---:|
| Recall | .8705882353 |
| Precision | .3465639230 |
| F2 | .6678476490 |
| Average precision | .5268606663 |
| ROC AUC | .8089705882 |
| TP / FN out of 17 | 14.8 / 2.2 |
| FP / TN out of 80 | 28.0 / 52.0 |

Fractional counts are averages, not a literal single confusion matrix. Precision means roughly one in three warnings is correct; recall means roughly 15/17 High students are detected. Outputs are not calibrated clinical probabilities.

Matched real-only Small B RF: **84.7% recall, 32.7% precision, F2 .642644, TP 14.4, FP 29.6**. Selected augmentation improved these recorded means modestly, not independently proven general performance.

### Saved final fit, 17 November 2026

`experiments/23-save-selected-random-forest.py`, configured by `experiments/23-save-selected-random-forest-settings.json`, applies the selected procedure to all 97 real students with four stratified validation folds. It selects the original forest/weight/ratio/threshold options, then refits preprocessing and forest on all data. It does not pick the best-performing old outer fold or tune on saved outer predictions.

Files: `results/23-selected-random-forest.joblib` and `results/23-selected-random-forest-metadata.json`. Audit: `results/23-selected-random-forest-fit/20261117T114817911532Z/`. Final recipe: 100 trees, max_depth 3, min_samples_leaf 10, normalized relative High weight 2, threshold .35, random seed 271828, augmentation ratio 0 (97 real rows, no added synthetic rows). The saved joblib object is a dictionary: use `saved['pipeline'].predict_proba(valid_eight_input_dataframe)[:, 1]`, then compare with `saved['warning_threshold']`; `saved['feature_names']` and `saved['allowed_values']` define the schema. See classification README for a complete loading example.

The model and audit folders are ignored by Git; a new clone will not automatically contain the trained file. Back up/transfer model and metadata together if needed. The exporter refuses to overwrite an existing pair. Saving this all-data fit creates no new independent performance estimate; keep the original CV results and their limitations separate. Checks include a historical-transform control refit, serialization roundtrip, fresh-process loading of all 97 scores/labels and selected-recipe validation refits; read the audit verification records for their exact scope.

### Synthetic inference-only check, 17 November 2026

The user requested generating fake data to test the saved model separately. Runner `experiments/24-check-random-forest-on-synthetic-profiles.py`, config `experiments/24-check-random-forest-on-synthetic-profiles-settings.json`, outputs `results/24-synthetic-profile-check/20261117T130726203314Z/`. Created **970 unique synthetic profiles: 800 Below-high, 170 High**. Existing constrained generation is applied separately to each same-class real-parent group; labels are inherited assumptions, not model-assigned labels or measured BAT responses. Profiles differ from all 97 real profiles and each other. This set is separate from the earlier 2,720 training-pool instances.

At the frozen .35 threshold: **TP 159, FN 11, FP 127, TN 673; synthetic assumed-label recall 93.5%, precision 55.6%, F2 .822981, accuracy 85.8%, AP .698947, AUC .929324**. Always-Below-high accuracy would be 82.5% with zero High recall. All parent students were used in fitting the saved RF, so the generated profiles are dependent neighbourhood simulations and scores can look favourable. **Do not describe these numbers as improved real-student performance, independent validation or replacement for the original 87.1% CV recall.** No retraining, threshold change or model replacement occurred.

Verification checked every profile's parent labels/domains/constraints/rounding/novelty, independent sklearn metrics, persisted scores and unchanged model/metadata/source hashes. This is one deterministic simulated dataset, not a real test cohort. Do not append these rows to the real SAV or SPSS analyses.

## 9. Synthetic training data: exact idea and limitations

For the latest plain-language explanation and numerical example, read [how one synthetic profile is created](07-classification-experiments-and-methods.md#how-one-synthetic-profile-is-created). In Small B, **"copy A" means keep both sleep and study-hours category codes exactly as recorded for parent A**. Only the other six ordinal answers are interpolated and rounded. A is chosen again for each attempt; it is not one fixed student for the whole experiment. Eligible parents need not contribute equally.

Keep these three objects separate when explaining the project:

| Object | What its sample count means |
|---|---|
| Original augmentation experiment | 2,720 generated profile instances across many training pools; not one forest trained on 2,720 extra rows. Real held-out students supplied the evaluation. |
| Saved final RF | 97 real students, zero synthetic training rows, because final training-validation selection chose ratio 0. Its artifact is still the selected saved model. |
| Separate synthetic consistency check | 970 generated profiles (800 Below-high /170 High) used only as inputs to the frozen saved RF. Labels are parent-inferred assumptions. No retraining occurred. |

Latest work on 18 November was documentation and explanation only. No new experiment, model replacement, deletion or change to data was requested. Continue from the next user instruction; do not automatically retrain to match the synthetic-check scores.

The selected classifier's training generator uses **High real training parents only**. It does not append fake respondents to the SAV/SPSS analyses or evaluate training-procedure performance on synthetic students. It does not necessarily balance classes. The separate inference-only simulation above additionally generates Below-high profiles; that does not change this historical training procedure.

1. Mixed distance averages ordinal absolute differences divided by 4 and categorical/binary mismatches. Parents must have distance <=.35 and no ordinal gap >2. Choose among up to three nearest eligible High neighbors.
2. Draw fraction `lambda` uniformly from .2 to .8; interpolate ordinal input `z=(1-lambda)*A+lambda*B`.
3. Stochastically round each ordinal input: ceiling with probability `z-floor(z)`, otherwise floor. Copy the complete categorical/binary block from parent A.
4. Require generated-to-anchor distance <=.25. Reject full-profile duplicates of real training or accepted generated rows in that pool. Fixed seeds/bounded attempts; keep shortfalls rather than relax constraints.
5. Request a full pool equal to the real High training count. Half/full ratios use prefixes; zero adds none. Labels are inferred, not measured BAT responses.

Example: 64 Below-high and 13 High training students can request 13 extra High profiles, giving 64/26 if all succeed, not balance. Patterns/labels remain assumptions. Legal codes and uniqueness do not prove realistic psychology or independent information; augmentation also changes training emphasis.

The recorded **2,720 profile instances** belong to the original multi-input-set experiment across its inner/outer training contexts. They are not 2,720 independent people or one combined dataset. Uniqueness is enforced within a pool; profiles can recur across contexts.

## 10. Modelling history and results

### Score prediction

Tried training-mean/median baselines, linear regression, Ridge, shallow RF, XGBoost, High-score weighting, synthetic regression training, SVR/kernel ridge, grouped input selection and blends. A baseline predicts the training target mean/median, not the mean of input fields.

Predictions often clustered near the middle and underestimated high measured scores. More complex algorithms did not automatically fix this. Selected fixed 50/50 blend: **.6160 overall/.6422 High MAE**, `results/07-ridge-and-svr-score-blend/20261102T163006135317Z/`, combining weighted Small B Ridge and high-priority Broad D SVR. No final deployment artifact.

### Binary comparisons relevant to the current choice

| Procedure | Recall | Precision | F2 | FP /80 |
|---|---:|---:|---:|---:|
| Selected eight-input RF | 87.1% | 34.7% | .667848 | 28.0 |
| SVC eight, F2 | 78.8% | 36.2% | .637154 | 23.6 |
| SVC eight, recall guard | 80.0% | 33.4% | .624572 | 27.2 |
| SVC 23, F2 | 76.5% | 40.4% | .646090 | 19.4 |
| SVC 23, recall guard | 83.5% | 35.4% | .655506 | 26.2 |
| Alternative fixed eight, F2 | 72.9% | 37.3% | .610528 | 21.2 |
| Alternative fixed eight, guard | 81.2% | 32.5% | .624508 | 28.6 |
| Logistic-ranked eight from 23, F2 | 72.9% | 37.9% | .612559 | 20.8 |
| Logistic-ranked eight from 23, guard | 83.5% | 33.5% | .642739 | 28.2 |
| Boruta from 23, F2 | 72.9% | 36.1% | .604040 | 22.2 |
| Boruta from 23, guard | 82.4% | 32.6% | .630103 | 29.0 |

The alternative eight replaced AI frequency/study hours with stress/avoidance. Logistic ranking selected eight whole variable groups inside each real inner/outer training group. Boruta selected **2-5** per outer fit (mean 3.56): workload/stress 25/25, AI dependence 20/25, avoidance 16/25, offloading/strain/support 1/25 each. These are fold-specific selections, not one final input set or proof omitted inputs are irrelevant.

Other binary experiments included logistic/RF/XGBoost/histogram gradient boosting on Small B/Broad D, 4/6/8 selection within the original eight, backward removal within those eight, focused RF tuning, RF/logistic mixtures, TabPFN and threshold/mixture refinements. Detailed results are in `research/07-classification-experiments-and-methods.md`; do not invent missing metrics.

TabPFN originally improved ranking (AP .615797, AUC .846176) but not the selected warning balance: F2 recall/precision **81.2%/36.5%**; original guard **89.4%/26.1%**, 44 warnings. Exact-threshold guard: **88.2%/31.2%**, 33.2 warnings. RF/TabPFN mixture guard: **83.5%/36.8%**, F2 .665290, 24.6 warnings. These are trade-offs, not uniform improvement.

Three-class labels were [1,2), [2,4), [4,5], with counts **6/74/17**, using different three-outer/two-inner folds repeated five times. Low detection was weak. Balanced augmentation and additional diagnostics were also explored; check the record for retention/deletion status rather than assuming every artifact remains.

### Recent local run locations

```text
results/19-eight-input-svc/20261116T070622236133Z/
results/20-twenty-three-input-svc/20261116T072730431772Z/
results/21-random-forest-input-comparison/20261116T075921907598Z/
results/22-boruta-input-selection/20261116T082517133758Z/
```

Input-comparison verification passed: **38,325 thresholds, 125 choices, 375 contexts**, independently refitting **416 selected inner/104 outer forests** and reproducing the current RF controls. Boruta verification passed: **18,900 thresholds, 50 choices, 125 contexts**, **160 selected inner/40 outer prediction-model refits**, and two predeclared Boruta selector replays (not all 125). Read each `verification.json` for scope. Computational checks are not independent-population validation.

BorutaPy 0.4.3 used 100-tree depth-5 min-leaf-2 balanced selector forests, max_iter 50, perc 100, alpha .05, two-step correction. Confirmed columns retain whole source variables; tentative columns are saved but excluded. No context selected zero inputs. Boruta generated full-23 training synthetic pools before projection; the alternative-input experiment generated pools on selected inputs. Do not attribute all differences solely to selection.

## 11. Deletions: keep reporting notes, do not recreate artifacts

User-requested cleanup on 16 November removed:

```text
analysis/extraction-config.json
analysis/scripts/train-extraction.py
analysis/outputs/extraction-experiments/
analysis/interaction-config.json
analysis/scripts/train-interactions.py
analysis/scripts/test-interactions.py
analysis/outputs/interaction-experiments/
analysis/loss-tuning-config.json
analysis/scripts/train-loss-tuning.py
analysis/outputs/loss-tuning-experiments/
```

PCA shared its runner with PLS. The mixed loss-tuning bundle contained refined PCA and depended on the deleted extraction code/outputs, so it was removed too, including its boosting/Huber/median artifacts. Their recorded tables remain in `research/06-data-analysis-and-experiment-history.md`. Removed matching bytecode/obsolete instructions; **412 unrelated files were fingerprinted unchanged**. Selected RF/data/other experiments were preserved; no retraining.

Historical findings to preserve:

- Ordinary Broad D PCA + Ridge: **.5748 overall/.8991 High MAE**, an improvement in ordinary overall error. Do not say PCA failed every metric.
- High-priority PCA + Ridge: Broad D **.6026/.6638**, Small B **.6339/.6274**; neither improved both errors over the blend **.6160/.6422**.
- Refined Broad D PCA + Ridge: **.5755/.8969**; Broad D Huber boosting: **.6102/1.0514**.
- Actual interaction terms were `(workload-3)` times sleep-category indicators 2/3/4, and `(ai_dependence-3)*(ai_offloading-3)`, retaining main effects. We did not collect a new sleep-deprivation scale.
- Primary linear overall/High MAE **.6155/.7622 -> .6131/.8356**; Ridge **.5883/.9329 -> .5872/.9011**. Overall gains were tiny and linear High error worsened.

These deleted runs cannot be reopened/rerun from remaining files. Historical paths are former locations. Earlier user-requested deletions also included CatBoost follow-up artifacts and recent generalization/learning-curve diagnostics (`diagnose-forest-generalization.py`, `diagnose-learning-curve.py`, their configs/outputs). Do not restore them unasked.

## 12. Literature and paper/presentation

Metadata is a discovery aid, not verified evidence. Previously examined primary papers include:

- [Computing-student supervised ML](https://pmc.ncbi.nlm.nih.gov/articles/PMC12691878/): administrative predictors/algorithm comparison/Boruta; best exhaustion F1 68.4%, with different labels from our BAT task.
- [Psychology-student risk profiles](https://pmc.ncbi.nlm.nih.gov/articles/PMC12023935/): groups created by clustering psychological/lifestyle measurements then classified; high accuracy is not directly comparable with our separately BAT-derived labels.
- [Adolescent burnout and feature selection](https://doi.org/10.1016/j.actpsy.2026.106995): top-10/full-28 AUC .820/.828, different population/measures; does not validate our exact eight.
- [Morningness, procrastination and burnout](https://pmc.ncbi.nlm.nih.gov/articles/PMC12211126/): association to investigate, not guaranteed ML improvement or causal evidence.

Reopen primary methods/results before a new exact citation. Do not quote impressive metadata accuracy without checking target construction, splits, leakage and population.

Main presentation priorities: score-prediction limitations, binary target decision, matched real-only versus augmentation, eight versus 23/selected inputs, a compact classifier-family comparison, and selected RF trade-offs. Group lower-priority refinements or use supplementary material. Preserve the unsuccessful-experiment inventory and disclose the many comparisons on the same sample.

No recommendation intervention was implemented/validated. Do not infer that changing majors, extra courses or treatment would improve outcomes from these correlations or predictions.

## 13. Environment and Git

Windows/PowerShell; Python environment reported **3.12.10**. Root-relative interpreter: `.\.venv\Scripts\python.exe`.

Recorded main versions: NumPy 2.5.4, pandas 3.1.0, scikit-learn 1.9.1, XGBoost 3.4.1, pyreadstat 1.3.7, threadpoolctl 3.7.0. Boruta 0.4.3 was added without changing those versions; SciPy recorded as 1.18.1. Read manifests/current environment before upgrading. Requirements are in `analysis/requirements*.txt`, `experiments/dependencies-xgboost.txt` and `experiments/dependencies-boruta.txt`.

TabPFN uses separate `.venv-tabpfn`, requirements and an original public TabPFN-2 checkpoint, not a claim to use a newer gated model. Its license/checkpoint provenance is in the classification README. Inference ran locally; survey records were not uploaded for TabPFN training.

### Code dependencies

Selected `train-augmentation.py` imports `train-binary.py`, which imports regression ensemble helpers connected to `train-models.py`, `train-kernels.py` and `train-high-score.py`. New input/Boruta scripts reuse earlier question-selection/feature-selection helpers; verification scripts also share helpers. **Inspect imports before deleting a script just because its experiment lost.**

### Push and missing-artifact caveat

`.gitignore` excludes environments, caches/weights, temporary files, bytecode and participant-level experiment outputs. `.gitignore` itself is tracked and can appear modified; stage/commit changes if sharing them. Ignore rules do not remove already tracked files.

The user reported pushing changes, then discussed `.gitignore`; recheck actual Git status rather than assuming staging/push state. Do not commit/push without authorization.

Many runners require specific prior output folders/manifests that are ignored. A fresh clone may have scripts/configs/docs but not the referenced artifacts. Do not claim every `results.md` link is available remotely or every script runs from a clean clone. If prerequisites are missing, explain them; obtain/regenerate only when authorized. Do not force-add participant-level outputs just to repair links.

## 14. Safe continuation checklist

1. Read this handoff and recent classification/progress sections; inspect exact code/configs for the requested task.
2. Check Git status, local files/manifests and environment permissions. Respect applicable skills and repository instructions.
3. Establish whether the request concerns classification, score prediction or paper/presentation; do not mix their metrics/labels.
4. Preserve selected RF/source data and user-requested deletions. Explain substantial new experiments first and store authorized comparisons separately.
5. State what was actually verified and its limits. Many same-sample comparisons can inflate apparent success despite correct inner tuning; no improvement is guaranteed.

No pending training job or automatic next experiment is authorized by this handoff. A final classifier has been fitted and saved, but independent-cohort/prospective validation, application deployment, calibrated probabilities, an exported score-regression blend and a validated intervention system have **not** been completed. Do not invent ethics/institutional approval, recruitment/retention details or population generalizability from these files.
