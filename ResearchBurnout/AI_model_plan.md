# AI model plan

Date: 29 October 2026

**Status: proposed plan, before training.** SPSS data preparation and initial analyses are complete. No predictive model has been trained or evaluated. This document explains the proposed first experiment so the team can agree on it before implementation.

## 1. What we want to build

Build a preliminary model that estimates a student's **current burnout symptoms** from answers about study conditions and GenAI use.

The main research question is:

> Does knowing a student's GenAI habits improve burnout predictions beyond knowing their study conditions?

The intended flow is:

**Non-BAT questionnaire answers → prediction model → estimated burnout score on the 1–5 scale.**

All responses were collected at one time. This supports investigation of current symptoms, not proof that the model can warn about future burnout. A future early-warning study would collect predictors now and measure burnout again later.

## 2. Data and prediction targets

Use **`spss_import/data_prepared.sav`**, containing 97 students. Keep students studying in Lebanon and the 10 students identified by the researcher as studying abroad. Q1 is not an exclusion rule.

| Item | Planned use |
|---|---|
| Non-BAT questions | Candidate inputs, also called features |
| `burnout_score` | Primary outcome: measured 12-item BAT-S score |
| `burnout_score_23` | Secondary outcome: equal-weight mean of the four full-core dimension means |
| Original text columns | Retained for traceability; use the appropriate numeric copies for modeling |

Both outcomes range from 1 to 5. Higher values mean more frequent symptoms. The primary/secondary choice follows the current study plan. Confirm the cited scoring definitions and freeze this choice before model comparisons; do not choose an outcome because it produces better performance.

The actual BAT score is available during development so we can compare predictions with measured symptoms. When making a prediction for a new student, the model uses only its selected non-BAT inputs.

**Never include BAT21–BAT43, any BAT dimension mean, or either overall BAT score among the predictors.** Those variables define the outcome; using them as inputs would make evaluation misleading. Exclude `Timestamp` as an input too.

See [SPSS_Analysis_Review.md](SPSS_Analysis_Review.md) for the completed tests, score formulas, coding, and final data checks.

## 3. First experiment: compare two input sets

Start with a limited, clearly defined comparison. These are proposed inputs to confirm before fitting, rather than predictors already proven useful.

| Question | Feature | Variable | Model A | Model B |
|---|---|---|---|---|
| Q15 | Perceived workload | `workload` | Yes | Yes |
| Q16 | Sleep duration | `sleep_duration_code` | Yes | Yes |
| Q14 | Independent study hours | `study_hours_code` | Yes | Yes |
| Q7 | Financial strain | `financial_strain` | Yes | Yes |
| Q19 | University support | `university_support` | Yes | Yes |
| Q8 | Academic GenAI-use frequency | `ai_frequency` | No | Yes |
| Q10 | Feeling unable to complete assignments without AI | `ai_dependence` | No | Yes |
| Q11 | Relying on AI instead of independent thinking | `ai_offloading` | No | Yes |

- **Model A: study context.** Tests what the five context questions can predict.
- **Model B: study context + GenAI.** Adds the three AI questions to test their additional predictive value.

Use the same students, algorithms, and validation splits for both sets. The key comparison is the difference in prediction error after adding the AI questions.

Other collected variables remain available, including academic level, major, GPA, electricity, internet, academic stress, avoidance, AI verification/anxiety, AI use cases, and enrollment location. We are not discarding them. Limit the first experiment to avoid trying many combinations and choosing a result that happens to look good in this small sample.

The first experiment also leaves out `leave_intention`: it describes a related concurrent consequence of academic stress, and may be more useful as a separate research outcome. Any later inclusion should have a clear purpose and be reported as an additional experiment.

Do not choose inputs solely from the earlier correlation p-values. A significant association does not guarantee useful predictions, and a nonsignificant individual association does not rule them out.

## 4. How we will prepare model inputs

The SPSS recodes are already complete. Modeling still requires explicit encoding decisions:

| Input type | Proposed treatment |
|---|---|
| Existing 1–5 items | Initially use their numeric responses, documenting the assumption of a roughly equal-step trend |
| Sleep and study-hour categories | Encode as categories with a reference group; their codes are ranges, not exact hours |
| Any nominal categories added later, such as major | Encode as separate category indicators, not a continuous numerical rank |
| Binary AI-use indicators, if examined later | Keep 0 = Not selected, 1 = Selected |

Standardize predictor columns for ridge regression using training-data statistics. Fit category encoders and scaling inside training folds. Define how an unseen category will be handled; an unobserved category such as more than eight hours of sleep has no effect estimate supported by this sample.

Do not use both the original text variable and its numeric copy as separate inputs. Keep a fixed input order and retain the preprocessing steps with the final model so new responses are treated consistently.

## 5. Will we use fake data or oversampling?

**No synthetic students, duplication, or oversampling in the first experiment. Use the 97 real responses.**

| Method | Initial decision | Explanation |
|---|---|---|
| Artificially generated student records | Do not use | They do not add independent observations and can reproduce sample-specific patterns |
| Duplicating students | Do not use | Repetition does not create additional information |
| Standard SMOTE | Do not use | It addresses categorical outcomes; our initial target is a continuous score |
| More real responses | Valuable if feasible | They add actual information and can support stronger evaluation |

Cross-validation evaluates the available data; it does not increase the sample size. If augmentation is investigated later, make it a separate comparison, generate records only inside training folds, and evaluate on untouched real students. Never create artificial records before dividing data for evaluation.

We will not start by labeling students low/moderate/high: this loses score information, and the current project bands are not validated diagnostic thresholds for this population.

## 6. Models to compare

| Approach | What it does | Why include it? |
|---|---|---|
| Mean-score baseline | Always predicts the training students' average burnout score | Shows whether learning from questionnaire answers adds value |
| Linear regression | Learns weights for the inputs | Simple initial reference model |
| Ridge regression | Learns weights while restraining excessively large coefficients | A reasonable starting approach for limiting overfitting in a small sample |

Run linear and ridge regression for both input sets. Begin here rather than testing a large collection of complex algorithms. Ridge has a tuning setting controlling how strongly weights are restrained; select it using only training data.

Inspect the initial regression for predictor overlap, residual patterns, functional form, and influential cases. VIF/tolerance can help examine overlap. Investigate influential students rather than automatically deleting them. Diagnostics support understanding; predictive performance must still be evaluated separately.

Linear and ridge predictions can fall outside 1–5 even though the measured outcome cannot. Decide and document any clipping to that range before evaluation, and apply the same policy consistently. Do not promise a bounded application output without implementing that policy.

## 7. Evaluate on students excluded from training

Use **repeated five-fold cross-validation** rather than a single small train/test split. A practical starting design is five repetitions, using fixed, recorded random seeds.

For each repetition:

1. Divide the 97 students into five groups of approximately 19–20.
2. Train on four groups and predict the group excluded from training.
3. Repeat until every group has been predicted.
4. Use the same group assignments for all compared approaches.
5. Record errors and compare results across repetitions.

For ridge, choose the tuning setting using an additional cross-validation step **inside each outer training set**. This is nested cross-validation: the outer group remains untouched while tuning and preprocessing are fitted on the training students.

Keep encoders, scaling, any data-driven feature selection, and tuning inside the training process. Do not use outer validation results repeatedly to redesign inputs and still describe the final result as an untouched evaluation. Record additional experiments clearly.

This is **internal validation**. Performance on a separate future student sample remains necessary before real-world use. Repeated folds share students, so their scores are not independent; their spread is a stability summary, not automatically a confidence interval.

## 8. How we will judge success

| Measure | Plain-language meaning |
|---|---|
| MAE: primary metric | Average absolute distance between predicted and measured burnout, in 1–5 score points |
| RMSE | Error measure that penalizes large mistakes more strongly |
| R-squared: supporting metric | Performance relative to a reference based on score variation; it can be negative on validation data |

Example only: a predicted score of 3.6 and measured score of 3.1 gives an absolute error of 0.5 points. An MAE of 0.4 would mean predictions are off by 0.4 points on average. **These are illustrations, not study results.**

We will examine:

- Whether either learned model beats the mean-score baseline.
- Whether Model B improves on Model A under the same evaluation design.
- How stable the results are across splits, with error summaries and uncertainty appropriate to the validation design.
- Predicted-versus-measured plots and whether higher measured scores are systematically underestimated.
- The secondary-outcome results under the same agreed workflow.

No accuracy threshold or useful improvement size has been established yet. A small apparent improvement with substantial uncertainty is not strong evidence that GenAI adds value. If GenAI does not help, or no model beats the baseline, report that finding honestly. Do not interpret coefficients as proof of causes.

## 9. Optional application: estimate plus support suggestions

After evaluating the model, a demonstration could collect the selected answers and show an estimated current symptom score, its limitations, and relevant support resources. It is a research prototype, not a diagnosis.

Support suggestions would use a **separate, transparent set of rules reviewed by student-support professionals**. The survey did not track interventions or later improvement, so it cannot teach us which action will reduce burnout.

Examples of proposed rules:

| Reported difficulty | Possible support route |
|---|---|
| Overwhelming workload | Discuss priorities and deadlines with an academic adviser |
| Short sleep or difficulty organizing | Offer reviewed sleep-routine and study-planning resources |
| Financial strain | Show financial-aid or student-services information |
| Difficulty coping or persistent disruption to daily functioning | Offer counselling or professional-support information |

Explain which reported answer prompted each suggestion. Do not infer a diagnosis from an estimated score or automatically recommend changing major, taking extra courses, or leaving university. Those decisions require personal context and appropriate human advice. Any score-based support trigger would need a documented justification; the exploratory risk bands are not clinical cutoffs.

Evaluate the suggestions separately for clarity, relevance, and usefulness. Prediction accuracy alone does not establish that recommendations help.

## 10. Deliverables and immediate next step

The planned deliverables are:

1. A fixed input/target specification and reproducible preprocessing workflow.
2. A comparison of the baseline, linear regression, and ridge regression for Models A and B.
3. Error tables, validation plots, and a clear account of uncertainty and limitations.
4. A secondary analysis using the full-core burnout score.
5. Optionally, a demonstration interface with reviewed support suggestions after model evaluation.

SPSS can support regression diagnostics; Python can support the reproducible preprocessing and cross-validation workflow. Existing SPSS output remains in `Outputs/Descriptive_statistics.spv`.

**Next action: confirm the target and the two input sets in Sections 2–3, document the encoding and evaluation decisions, and freeze the first experiment before fitting.**
