# Prediction experiment

Follow [the root work plan](../work-plan.md) for task order. This file gives the proposed experiment details; no model has been trained.

Updated: 29 October 2026. Reading time: about 6 minutes.

## 1. What we want to test

Do GenAI habits help us estimate current burnout symptoms beyond what study conditions tell us?

Use `data/prepared/burnout-data.sav`, with all 97 students. The planned main target is `burnout_score`, the measured 12-item BAT-S score. Use `burnout_score_23` as a secondary check. Both range from 1 to 5; higher scores mean more frequent symptoms.

During development, compare predictions with measured BAT scores. For a new student, the model would use only the selected non-BAT answers.

All answers were collected at one time. This experiment estimates current symptoms. Testing future burnout would need a later burnout measurement.

## 2. Compare two sets of inputs

An input, also called a feature, is an answer the model uses to make its estimate.

| Question | Input | Dataset variable | Set A | Set B |
|---|---|---|---|---|
| Q15 | Workload | `workload` | Yes | Yes |
| Q16 | Sleep duration | `sleep_duration_code` | Yes | Yes |
| Q14 | Independent study hours | `study_hours_code` | Yes | Yes |
| Q7 | Financial strain | `financial_strain` | Yes | Yes |
| Q19 | University support | `university_support` | Yes | Yes |
| Q8 | GenAI-use frequency | `ai_frequency` | No | Yes |
| Q10 | Feeling unable to complete assignments without AI | `ai_dependence` | No | Yes |
| Q11 | Relying on AI instead of thinking independently | `ai_offloading` | No | Yes |

Set A uses five study-condition questions. Set B adds the three AI questions. Compare both sets with the same students, algorithms, and validation groups. The difference in prediction error tells us whether the AI questions help in this experiment.

Keep the other collected answers for possible later analyses. Trying many combinations on 97 students increases the chance of choosing a result that looks good by accident. Earlier correlation p-values alone should not decide which inputs we use.

The first experiment leaves out `leave_intention`, which may work better as a separate research outcome. It also leaves out enrollment location. Record any later additions as separate experiments.

Exclude `Timestamp`, BAT21 to BAT43, every BAT dimension mean, and both BAT totals from inputs. BAT answers define the target; feeding them into the model would give it the answer during evaluation. This is called data leakage.

## 3. Prepare the inputs

The SPSS numeric recodes are ready. We still need to specify how the model reads them.

| Input type | Proposed handling |
|---|---|
| Existing 1 to 5 responses | Use the numbers initially; state the assumption that a one-point change has a similar meaning across the scale |
| Sleep and study-hour codes | Treat as categories, with one reference category; code 3 means a range, not three hours |
| Major, if added later | Treat as categories, with no numerical ranking |
| AI-use indicators, if added later | Keep 0 = Not selected and 1 = Selected |

For category inputs, create indicator columns that tell the model which category a student selected. Choose reference categories and a policy for new categories before evaluation. No student reported more than eight hours of sleep, so this sample cannot estimate an effect for that group.

For ridge regression, scale the input columns using the training students' averages and spread. Learn category handling and scaling inside each training group. Save those steps with the model and keep the input order fixed.

Use one representation of each question. Do not include an original text answer and its numeric copy as separate inputs.

## 4. Compare simple models

A [literature-based review](model-review.md) recommends adding one limited Random Forest regression comparison and a median baseline. These remain proposed additions; the comparison below records the original plan.

| Approach | What it does |
|---|---|
| Mean-score baseline | Predicts the training students' average burnout for everyone |
| Linear regression | Learns a weight for each input to estimate the score |
| Ridge regression | Learns weights while limiting very large weights, which can help reduce fitting to chance patterns |

Run linear and ridge regression for both input sets. The baseline shows whether using questionnaire answers improves on predicting the average.

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
5. Summarize prediction errors and compare the two input sets.

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

Check whether the learned models beat the baseline and whether Set B improves on Set A. Report how results vary across splits, with uncertainty that fits the evaluation design. Plot predicted against measured scores and check whether the model underestimates higher scores.

No useful improvement size or accuracy threshold has been agreed yet. A small improvement with high uncertainty gives weak evidence. Report honestly if AI inputs do not help or if neither model beats the baseline. Model weights do not establish causes.

Repeat the agreed workflow with the secondary score to check whether conclusions change. Do not choose the target because it gives better results.

## 7. Decisions to record before training

| Decision | Current position |
|---|---|
| Target and input sets | Proposed above; confirm and record before comparisons |
| Category encoding | Proposed above; choose reference groups and unseen-category handling |
| Evaluation | Five folds repeated five times proposed; record seeds, ridge tuning choices, and uncertainty method |
| Output range | Decide whether to limit predictions to 1 to 5 |
| What counts as useful improvement | Not yet agreed; decide before interpreting results |

Save these choices as the experiment specification. SPSS can support regression checks; Python can support repeatable model evaluation.

Expected outputs are an input specification, reproducible preprocessing, comparison tables, validation plots, and a secondary-score analysis. Keep the existing SPSS output in `analysis/outputs/descriptive-statistics.spv`.

## Later: a possible demo

After evaluation, a demo could collect the selected answers and show an estimated current symptom score with its limits. It would be a research prototype, not a diagnosis.

Support suggestions would need separate, clear rules reviewed by student-support professionals. The survey did not test interventions or track improvement, so it cannot tell us which advice reduces burnout.

Possible routes include an academic adviser for workload, reviewed sleep or planning resources, financial-aid services, and counselling support when relevant. Explain which answer prompted a suggestion. Do not infer a diagnosis or automatically recommend changing major or leaving university. Any score-based trigger needs its own justification; the exploratory bands are not clinical cutoffs.

Test suggestions for clarity, relevance, and usefulness separately from prediction accuracy.

Next: review the proposed input table in Section 2, which takes about 2 minutes.
