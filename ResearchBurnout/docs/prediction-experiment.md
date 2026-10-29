# Prediction experiment

Follow [the root work plan](../work-plan.md) for task order. This file explains the experiment. Settings are recorded in [the configuration](../analysis/experiment-config.json); the workflow is prepared, and the full real-data comparison has not been run.

Updated: 29 October 2026. Reading time: about 8 minutes.

## 1. What we want to test

Do GenAI habits help us estimate current burnout symptoms beyond what study conditions tell us?

Use `data/prepared/burnout-data.sav`, with all 97 students. The planned main target is `burnout_score`, the measured 12-item BAT-S score. Use `burnout_score_23` as a secondary check. Both range from 1 to 5; higher scores mean more frequent symptoms.

During development, compare predictions with measured BAT scores. For a new student, the model would use only the selected non-BAT answers.

All answers were collected at one time. This experiment estimates current symptoms. Testing future burnout would need a later burnout measurement.

## 2. Compare two sets of inputs

We will compare a small questionnaire with a broader questionnaire. Each has a version without GenAI questions and a version with them. An input, also called a feature, is an answer the model uses to make its estimate.

### Small input sets: A and B

These are the original selected questions. They give us a limited starting comparison; they are not proven to be the best inputs.

| Question | Input | Dataset variable | Small A | Small B |
|---|---|---|---|---|
| Q15 | Workload | `workload` | Yes | Yes |
| Q16 | Sleep duration | `sleep_duration_code` | Yes | Yes |
| Q14 | Independent study hours | `study_hours_code` | Yes | Yes |
| Q7 | Financial strain | `financial_strain` | Yes | Yes |
| Q19 | University support | `university_support` | Yes | Yes |
| Q8 | GenAI-use frequency | `ai_frequency` | No | Yes |
| Q10 | Feeling unable to complete assignments without AI | `ai_dependence` | No | Yes |
| Q11 | Relying on AI instead of thinking independently | `ai_offloading` | No | Yes |

Small A uses five study-condition questions. Small B adds three GenAI questions.

### Broad input sets: C and D

Broad C includes all collected background and condition questions: Q1 to Q7 and Q14 to Q19. Broad D adds all GenAI questions, Q8 to Q13. Use ridge regression for this broader comparison to limit the experiment size.

| Questions | Input variables | Broad C | Broad D |
|---|---|---|---|
| Q1 | `enrolled_lebanon` | Yes | Yes |
| Q2 to Q4 | `academic_level_code`, `major_code`, `gpa_code` | Yes | Yes |
| Q5 to Q7 | `electricity_code`, `internet`, `financial_strain` | Yes | Yes |
| Q14 to Q19 | `study_hours_code`, `workload`, `sleep_duration_code`, `academic_stress`, `avoidance`, `university_support` | Yes | Yes |
| Q8 | `ai_frequency` | No | Yes |
| Q9 | `ai_use_concepts`, `ai_use_writing`, `ai_use_coding`, `ai_use_summaries`, `ai_use_solutions` | No | Yes |
| Q10 to Q13 | `ai_dependence`, `ai_offloading`, `ai_verification`, `ai_anxiety` | No | Yes |

Broad C uses 13 questions represented by 13 variables before category encoding. Broad D uses 19 questions represented by 23 variables, because Q9 has five separate selection indicators. Category encoding adds further columns.

Q1 describes enrollment location; including it does not exclude the 10 students identified as studying abroad. It does not identify nationality or public/private universities. Keep all 97 students in every comparison.

Academic stress and avoidance measure difficulties close to current burnout symptoms. They are available as inputs, but their inclusion may make the broad questionnaire less distinct from directly asking about symptoms. Explain that when interpreting results.

### What the comparisons tell us

| Comparison | Question |
|---|---|
| Small A versus Small B, within each algorithm | Do the selected GenAI questions help beyond the selected conditions? |
| Broad C versus Broad D, using ridge | Do all GenAI questions help beyond the broader background and condition set? |
| Small A versus Broad C, using ridge | Does adding the remaining background and condition questions help? |
| Small B versus Broad D, using ridge | Does the broader questionnaire improve on the small questionnaire with GenAI? |

Use the same students and outer validation groups throughout. Tune ridge separately for each set inside training groups, using the same tuning grid. Improvement from GenAI is relative to the condition set being tested; it does not establish an AI effect or cause.

Record all four sets before training. Do not try arbitrary subsets or select inputs from earlier correlation p-values. Report both the small and broad comparisons even if one looks worse.

### Questions excluded from every predictor set

Keep Q20 (`leave_intention`) as a possible separate research outcome. It is not a BAT-derived variable; excluding it is a study-design choice because it describes a related concurrent consequence. Broad D therefore includes Q1 to Q19, not every survey question.

Exclude `Timestamp`, BAT21 to BAT43, every BAT dimension mean, and both BAT totals from inputs. BAT answers define the target; feeding them into the model would give it the answer during evaluation. This is called data leakage. Use numeric copies or original text answers, never both as separate inputs.

## 3. Prepare the inputs

The SPSS numeric recodes are ready. We still need to specify how the model reads them.

| Input type | Proposed handling |
|---|---|
| Existing 1 to 5 responses | Use the numbers initially; state the assumption that a one-point change has a similar meaning across the scale |
| Academic level, GPA, electricity disruption, sleep, and study-hour codes | Treat as categories with reference categories; the codes represent ordered categories, not equal numerical gaps |
| Major in Broad C and D | Treat as categories, with no numerical ranking |
| Enrollment location and AI-use indicators | Keep their existing 0/1 coding |

For category inputs, create indicator columns that tell the model which category a student selected. Choose reference categories and a policy for new categories before evaluation. No student reported more than eight hours of sleep, so this sample cannot estimate an effect for that group.

For ridge regression, scale the input columns using the training students' averages and spread. Learn category handling and scaling inside each training group. Save those steps with the model and keep the input order fixed.

Use one representation of each question. Do not include an original text answer and its numeric copy as separate inputs.

## 4. Compare simple models

The [literature-based review](model-review.md) explains why we include ridge, a limited Random Forest comparison, and constant-score baselines.

| Approach | Input sets | Role |
|---|---|---|
| Mean-score baseline | No inputs | Predict the training students' average |
| Median-score baseline | No inputs | Predict the training median; a reference for absolute error |
| Linear regression | Small A and B | Simple learned comparison |
| Ridge regression | Small A and B; Broad C and D | Limit large weights while comparing input sets |
| Small Random Forest regressor | Small A and B | Test whether nonlinear patterns help |

Compute the baselines on the same outer training groups and report them alongside both comparisons. They do not need duplicate fits for each input set. Keep the broader experiment limited to ridge rather than testing every algorithm with every set.

Inspect predictor overlap, residuals (measured minus predicted scores), unusual cases, and whether straight-line relationships are reasonable. VIF and tolerance help check input overlap. Investigate influential cases; do not remove students automatically. These checks do not replace testing prediction error on students excluded from training.

Linear and ridge predictions can fall outside 1 to 5. Record whether to limit predictions to that range before evaluation, and apply the policy consistently.

Use the 97 real responses for the first experiment. Do not create artificial students, duplicate records, or use SMOTE. More real responses would add information; cross-validation does not increase the sample size. Any later artificial-data experiment must generate records only within training groups and evaluate on untouched real students.

Keep burnout as a continuous score. The project's Low/Moderate/High bands lose information and are not validated diagnostic thresholds for Lebanese students.

## 5. Test predictions on students excluded from training

The proposed design is repeated five-fold cross-validation, with five repetitions and recorded random seeds. A random seed lets someone recreate the same group assignments.

1. Split the 97 students into five groups of about 19 to 20.
2. Train on four groups and predict the remaining group.
3. Repeat until each student has a prediction made without training on their response.
4. Repeat this process with new group assignments, using the same assignments for all compared models.
5. Summarize prediction errors for the planned small and broad comparisons.

Ridge has a tuning setting that controls how strongly it limits large weights. Choose it using another validation step inside each outer training group. This is nested cross-validation: the outer test group stays untouched during tuning.

Fit encoding, scaling, any input selection, and tuning using training students only. Repeatedly changing inputs after seeing validation errors makes the evaluation less trustworthy; record extra experiments separately.

This tests performance within our existing sample. A separate future sample is still needed before real-world use. Repeated folds share students, so their results are not independent. Variation across folds is a stability summary, not automatically a confidence interval.

## 6. How to read the results

| Measure | Meaning |
|---|---|
| MAE, the main measure | Average absolute prediction error in burnout-score points |
| RMSE | An error measure that gives more weight to large mistakes |
| R-squared | A supporting measure of performance relative to score variation; it can be negative on validation data |

Example only: predicting 3.6 when the measured score is 3.1 gives an absolute error of 0.5 points. This is not a study result.

Check whether learned models beat the baselines, whether Small B improves on Small A, and whether Broad D improves on Broad C. Use ridge to compare the small and broader questionnaires. Report how results vary across splits, with uncertainty that fits the evaluation design. Plot predicted against measured scores and check whether the model underestimates higher scores.

No useful improvement size or accuracy threshold has been agreed yet. A small improvement with high uncertainty gives weak evidence. Report honestly if AI inputs do not help or if neither model beats the baseline. Model weights do not establish causes.

Repeat the agreed workflow with the secondary score to check whether conclusions change. Do not choose the target because it gives better results.

## 7. Decisions to record before training

| Decision | Current position |
|---|---|
| Target and input sets | Recorded: both targets and all four sets in `analysis/experiment-config.json` |
| Category encoding | Questionnaire-defined categories, first code as reference; invalid codes stop the run, and categories absent from training have no learned effect |
| Evaluation | Five outer folds, five recorded seeds; four inner folds; fixed small ridge and forest grids; report repetition range and standard deviation without calling them confidence intervals |
| Output range | Clip to 1 to 5 during inner selection and outer evaluation; retain raw predictions |
| What counts as useful improvement | Report paired MAE reductions descriptively; no established practical or clinical threshold |

Save these choices as the experiment specification. SPSS can support regression checks; Python can support repeatable model evaluation.

Expected outputs are an input specification, reproducible preprocessing, comparison tables, validation plots, and a secondary-score analysis. Keep the existing SPSS output in `analysis/outputs/descriptive-statistics.spv`.

## Later: a possible demo

After evaluation, a demo could collect the selected answers and show an estimated current symptom score with its limits. It would be a research prototype, not a diagnosis.

Support suggestions would need separate, clear rules reviewed by student-support professionals. The survey did not test interventions or track improvement, so it cannot tell us which advice reduces burnout.

Possible routes include an academic adviser for workload, reviewed sleep or planning resources, financial-aid services, and counselling support when relevant. Explain which answer prompted a suggestion. Do not infer a diagnosis or automatically recommend changing major or leaving university. Any score-based trigger needs its own justification; the exploratory bands are not clinical cutoffs.

Test suggestions for clarity, relevance, and usefulness separately from prediction accuracy.

Next: follow [the analysis run instructions](../analysis/README.md#run-the-prediction-experiment).
