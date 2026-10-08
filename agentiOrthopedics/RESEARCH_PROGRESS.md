# Research Progress: AI/ML for Orthopedic Treatment Recommendation

## Purpose

This document records literature investigated while refining a possible Master's-level Data Science research topic: using historical orthopedic data to support individualized treatment decisions. It is a progress record, not evidence that the proposed system is feasible or clinically validated.

## Investigated Papers

### 1. Operative or Nonoperative Treatment is Predicted Accurately for Patients Who Have Hip Complaints Consulting an Orthopedic Surgeon Using Machine Learning Algorithms Trained With Prehospital Acquired History-Taking Data

**Research problem.** The study asks whether machine learning can predict, before a consultation, whether a patient referred with hip complaints will have an **operative** or **non-operative** treatment strategy after the consultation. The practical motivation is to improve orthopedic consultation workflow as the demand for hip care increases.

**Patient data and model input.** Adult patients referred for hip complaints completed a computer-assisted history-taking (CAHT) form before their hospital consultation. The answers to that form were the input to the ML algorithm. The paper therefore evaluates predictions based on pre-consultation history-taking data, rather than a full post-consultation clinical assessment.

**Prediction and its relationship to the clinical decision.** The model predicts a binary outcome: **non-operative treatment versus operative treatment**. Its prediction was compared with the treatment strategy recorded as the outcome of the real orthopedic consultation. Thus, the target is the clinician consultation decision, not a direct estimate of which treatment would produce the best patient outcome.

**Main results.** In a prospective cohort of 119 consultations, the overall predicted treatment strategy agreed with the consultation outcome in 101 cases (85%). Predictions labelled non-operative were correct in 97% of cases (71 predictions), whereas predictions labelled operative were correct in 67% of cases (48 predictions). The study reports no statistically significant difference between consultations where clinicians were blinded or unblinded to the prediction.

**Relevance to the proposed project.** This is directly relevant because it is an orthopedic example of using patient information to predict a treatment decision. It also establishes an important boundary for the proposed work: this paper is essentially about predicting **operative vs. non-operative treatment historically chosen in a consultation**. It does not by itself establish that the predicted choice is the treatment that would yield the best outcome for an individual patient.

### 2. Machine learning-based clinical decision support system for treatment recommendation and overall survival prediction of hepatocellular carcinoma: a multi-center study

**Research problem.** Treatment decisions for hepatocellular carcinoma (HCC) depend on many factors, and guideline/staging-system recommendations may differ from actual initial treatment choices. This study developed a multi-centre ML clinical decision-support system that recommends an initial treatment and predicts overall survival after treatment.

**Patient and clinical data.** The system was developed and evaluated using patient data collected from nine institutions in South Korea. It used 20 clinical variables. The paper describes internal and external datasets of 935 and 1,750 patients, respectively.

**Treatment recommendation component.** The first stage uses an ensemble voting model to recommend an initial treatment. It produces ranked treatment options: the option with the highest predicted probability is the first recommendation, and the second-highest is an alternative option. When only the first option was counted, reported recommendation accuracy was 67.27% internally and 55.34% externally; accepting either of the two top options increased this to 87.27% and 86.06%.

**Survival/outcome component.** The second stage uses a random survival forest to predict post-treatment overall survival for the recommended treatment options. This is valuable conceptually because it connects treatment options to a patient outcome rather than treating the treatment label as the only endpoint. The reported concordance index was 0.8381 internally and 0.7767 externally.

**Relevance to the proposed project.** This paper is relevant to the idea of learning from historical treatments **and outcomes**: it combines a treatment-selection component with outcome prediction. However, it is **not an orthopedic study**. Also, its treatment-recommendation evaluation is based on agreement with observed initial treatments; this should not automatically be interpreted as proof of causal, outcome-optimal treatment selection.

### 3. Treatment Recommendations for Clinical Deterioration on the Wards: Development and Validation of Machine Learning Models

**Research problem.** The study investigates whether ML can help clinicians respond to deteriorating general-ward patients by predicting needed lifesaving interventions, rather than only identifying that deterioration risk is high.

**Patient information.** The researchers used a chart-reviewed, multicentre dataset of 2,480 general-ward deterioration encounters identified as high risk by the electronic Cardiac Arrest Risk Triage (eCART) score. Inputs were electronic health-record measurements available at the elevated-risk time point. For non-sequential models, these included the latest values and summary information over the preceding 24 hours; LSTM models used sequences of time-stamped measurements. Manual chart review supplied gold-standard intervention labels.

**Multiple interventions, not one binary choice.** This is not a single "treat versus do not treat" task. The models predict the need for each of 10 possible clinical interventions: antimicrobial treatment, fluid bolus, antiarrhythmic treatment, diuretic, inhaled bronchodilator, transfusion, invasive ventilation, vasoactive treatment, anticoagulant, and steroid. A patient encounter can have more than one intervention label.

**ML approaches and performance.** The study compared elastic-net logistic regression, gradient-boosted machines (XGBoost), long short-term memory (LSTM) models—including single-label and multilabel variants—and a stacking ensemble that combines individual-model predictions. Models were trained at three health systems and externally validated at a fourth. AUROCs generally ranged from 0.7 to 0.9, varying by intervention; gradient boosting tended to be the strongest individual approach, while the stacking ensemble typically matched or exceeded the best individual model for a task.

**Relevance to the proposed project.** The paper is relevant because it frames treatment planning as a set of possible, patient-specific interventions instead of only a binary treatment category. Its use of clinician chart review also highlights that raw historical records may reflect what happened, whereas carefully defined labels are needed when the goal is a high-quality recommendation. It is **not an orthopedic study**.

### 4. Near-optimal Individualized Treatment Recommendations

**Individualized Treatment Recommendation (ITR).** ITR is a precision-medicine framework in which a recommendation rule maps a patient's characteristics to a treatment option. Its aim is to assign the treatment expected to provide the greatest benefit for that particular patient, recognising that patients may respond differently to the same treatment.

**Prediction versus recommendation.** Predicting the treatment a clinician historically chose answers: *"What treatment is likely to be selected?"* An ITR instead seeks to answer: *"Which available treatment is expected to give this patient the best outcome?"* These are different objectives. Historical clinician choices may be influenced by availability, clinician preference, patient preference, and factors not represented in a dataset.

**Role of characteristics, treatments, and outcomes.** An ITR method uses patient characteristics together with historical treatment assignments and observed outcomes to estimate the expected outcome under each possible treatment. It then selects the treatment with the best estimated expected outcome. This paper develops an alternative ITR (A-ITR) framework that can recommend a *set* of treatments that are sufficiently close to optimal, rather than forcing a single choice when options have similar estimated outcomes.

**Counterfactual problem.** For each historical patient, we observe the outcome under the treatment they actually received. We do not directly observe what would have happened to that same patient under another treatment. These unobserved potential outcomes are counterfactuals. Estimating them from observational historical data is the core difficulty in moving from treatment-decision prediction to outcome-based treatment recommendation.

**Near-optimal recommendation.** The paper uses outcome-weighted learning to estimate recommendations. Its central idea is to estimate expected outcomes for available treatments conditional on patient characteristics, then select the optimal treatment or all treatments whose expected outcomes are close enough to the best one according to a clinically chosen near-optimality threshold.

**Scope and implementation.** This is a methodological machine-learning/statistical paper, not an orthopedic clinical study. Its empirical illustration uses type 2 diabetes patients receiving injectable antidiabetic treatments. The authors report an R implementation, the [`aitr`](https://github.com/menghaomiao/aitr) package.

## Common Idea Across the Papers

All four papers use patient-level information to support treatment-related decisions, but they address different targets:

| Paper type | Main target | Key interpretation |
| --- | --- | --- |
| Hip orthopedic study | Operative vs. non-operative consultation outcome | Predicts the treatment strategy selected in practice. |
| HCC decision-support study | Initial treatment options and post-treatment survival | Links treatment selection with an outcome-prediction component. |
| Ward-deterioration study | Need for several possible interventions | Predicts multiple treatment actions for high-risk patients. |
| ITR methodology study | Treatment expected to be most beneficial | Formalizes outcome-based, individualized recommendation under counterfactual uncertainty. |

Together, they suggest a progression from predicting a historical clinical decision, through predicting several possible actions or outcomes, toward individualized treatment recommendation. The papers also show that a clinically useful system needs a precisely defined treatment target, appropriate input data, meaningful outcome definitions, and careful validation.

## My Current Research Direction

Current working hypothesis:

Historical orthopedic patient data:

* Patient metadata
* Symptoms
* Diagnosis/clinical characteristics
* Treatment received
* Treatment outcome

→ ML/AI model

→ For a new patient:

* Analyze the patient's characteristics
* Consider possible treatment options
* Estimate which treatment is likely to provide the best outcome
* Produce an individualized treatment recommendation

This is currently a **research direction/hypothesis**, **not a finalized methodology**. The data source, eligible conditions and treatments, outcome definition, causal assumptions, model design, and validation strategy must be decided only after identifying a suitable orthopedic dataset and refining the research question.

## Two Possible Research Directions

### Direction 1 — Treatment Decision Prediction

**Patient characteristics → predict the treatment that was historically chosen by clinicians.**

This direction is similar to the hip-complaints study. It can be useful for workflow support, triage, and describing historical clinical decision patterns. However, agreement with a historical decision does not demonstrate that the predicted treatment is best for the patient.

### Direction 2 — Individualized Treatment Recommendation

**Patient characteristics + historical treatment/outcome data → estimate expected outcomes for possible treatments → recommend the treatment expected to be most beneficial.**

This direction is more scientifically interesting because it focuses on patient benefit rather than decision imitation. It is also more difficult. It must address the counterfactual/causal-inference problem, potential treatment-selection bias and confounding, and the need for an appropriate dataset with sufficiently detailed pre-treatment characteristics, treatment information, and clinically meaningful outcomes.

## Research Progress

- [x] Investigated existing work on orthopedic treatment prediction.
- [x] Investigated ML-based treatment recommendation.
- [x] Investigated individualized treatment recommendation.
- [x] Identified the difference between treatment prediction and treatment optimization/recommendation.
- [x] Identified the importance of treatment outcomes.
- [x] Identified the counterfactual problem as a major methodological challenge.
- [x] Identified the need to find a suitable orthopedic dataset before finalizing the research question.

## References

1. van der Weegen W, Warren T, Das D, et al. [*Operative or Nonoperative Treatment is Predicted Accurately for Patients Who Have Hip Complaints Consulting an Orthopedic Surgeon Using Machine Learning Algorithms Trained With Prehospital Acquired History-Taking Data*](https://doi.org/10.1016/j.arth.2023.11.022). *The Journal of Arthroplasty*. 2024;39(5):1173-1177.e6.
2. Lee KH, Choi GH, Yun J, et al. [*Machine learning-based clinical decision support system for treatment recommendation and overall survival prediction of hepatocellular carcinoma: a multi-center study*](https://doi.org/10.1038/s41746-023-00976-8). *npj Digital Medicine*. 2023.
3. Pulick E, Carey KA, Oyli T, et al. [*Treatment Recommendations for Clinical Deterioration on the Wards: Development and Validation of Machine Learning Models*](https://doi.org/10.2196/81642). *JMIR AI*. 2026;5:e81642.
4. Meng H, Zhao Y-Q, Fu H, Qiao X. [*Near-optimal Individualized Treatment Recommendations*](https://www.jmlr.org/papers/v21/20-334.html). *Journal of Machine Learning Research*. 2020;21(183):1-28.
