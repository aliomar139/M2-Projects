# Study Design and Evaluation

[Fig. 1. Input sets for score estimation and high-symptom warnings](../tex/figures/study-design.pdf)

## Participants and Questionnaire


We used convenience sampling to recruit Lebanese undergraduate and graduate students from multiple universities for an online cross-sectional survey. The survey link circulated primarily through WhatsApp among student contacts and their peers. We assessed eligibility using recruitment information and self-reported answers.

We analyzed all 97 survey submissions received from 4 to 18 October 2026. Of the respondents, 87 reported attending a university in Lebanon. Based on recruitment information, we identified the other 10 as Lebanese students studying abroad. After data collection, we revised the original location-based eligibility rule to include them.

The opening pages of the Google Forms survey explained the study and stated that participation was voluntary. Respondents indicated consent by choosing to continue. The form did not ask for names, contact information, or other direct identifiers. The study was not submitted for formal ethics review.

The questionnaire contained 20 questions on student background, study conditions, GenAI use, and intention to continue studying. It then presented the 23 core items of the English student version of the Burnout Assessment Tool (BAT-S) [10], [11]. Short explanations clarified the word *cynical* in BAT-S item Q33 and *procrastinate* in the separate study-conditions item Q18.

## Outcomes and Data Preparation

Responses to every BAT-S item used a scale from 1 (never) to 5 (always), with higher values indicating more frequent symptoms. For both scores, the calculation first averaged the items within each of the four dimensions. The four dimension means then contributed equally to the overall score.

The primary score used the 12 items marked as the short form in the English questionnaire. The secondary score used all 23 core items. The table below lists the survey question numbers for both scores. Each calculation required responses to all of its items, and both scores were complete for all 97 students.

*Survey Items Used to Calculate the BAT-S Scores*

| Dimension | Primary items | Core items |
| --- | --- | --- |
| Exhaustion | Q21, Q23, Q24 | Q21–Q28 |
| Mental distance | Q29, Q31, Q33 | Q29–Q33 |
| Cognitive impairment | Q34, Q37, Q38 | Q34–Q38 |
| Emotional impairment | Q39, Q40, Q43 | Q39–Q43 |

The warning task used the measured primary score to assign each student to one of two groups. A score of 4 or above defined the High group (17 students). Scores below 4 defined the Below-high group (80 students). Both groups describe symptom levels at the time of the survey.

Data preparation included checking the prepared data against the original export and recalculating the scores. One imported internet rating was corrected from the original answer, and one emotional-impairment mean was recalculated from its component items. When data were loaded for model fitting, three missing indicators of AI use for summarization were reconstructed from the original selections. The recoding completed the model inputs and left the prepared data file unchanged.

IBM SPSS Statistics 23 was used to summarize responses and scores and to calculate Cronbach's alpha for each dimension and for the 12-item and 23-item sets. Two-sided Spearman correlations examined 11 separate associations with the primary score without adjustment for multiple testing. A Pearson correlation was also calculated between AI dependence and the primary score.

## Input Sets and Score Prediction

To test whether GenAI questions improved score prediction, we compared input sets using the same model family and evaluation splits within each comparison. Small A used five study-condition questions on perceived workload, sleep duration category, independent study-hours category, financial strain, and university support. Small B added three questions on GenAI use frequency, self-reported dependence on AI to complete academic work, and reliance on AI in place of independent thinking, for eight inputs.

Broad C used 13 inputs on background and study conditions (Q1–Q7 and Q14–Q19). It added eight questions to Small A, covering enrollment location, academic level, major, GPA range, electricity outages, internet quality, academic stress, and avoidance or procrastination.

Broad D added all six GenAI questions (Q8–Q13) to Broad C, covering frequency, use cases, dependence, reliance in place of independent thinking, verification of AI outputs, and concerns about being flagged for AI use. Q9 supplied separate yes-or-no inputs for concept explanations, writing, coding, summaries, and direct solutions, so 19 questions yielded 23 inputs before categorical encoding. All input sets excluded BAT-S responses and scores, submission timestamps, and the item on intention to continue studying.

We compared Small A with Small B using linear regression, ridge regression, and a shallow random forest. We used ridge for Broad C and Broad D as well. Ridge is linear regression with a penalty that discourages large weights on the inputs. The two benchmarks predicted the training group's mean or median score for every test student.

For each repetition, we split the 97 students into five groups. We trained on four groups and tested on the fifth, taking turns until every student had one test prediction. We ran this process with five different shuffles. Within each training set, we used four smaller groups to choose settings by mean absolute error (MAE), the average distance between predicted and measured scores. We kept predictions within 1 to 5 during tuning and testing and calculated MAE for all students and for those with measured scores of at least 4.

We represented categorical answers such as sleep-duration bands as yes-or-no indicators, leaving the first category as the reference. We used training data to put the ridge inputs on a common scale and tested penalties from 0.01 to 1000 in tenfold steps. For the 200-tree regression forest, we tried maximum depths of 2 or 3 and minimum leaf sizes of 5 or 10.

Follow-up experiments gave more weight to errors on high scores. The selected follow-up predictor averaged two estimates equally, one from weighted ridge on Small B and one from high-priority support vector regression on Broad D.

## High-Symptom Warning Models

The selected random forest classifier used Small B to predict the High label directly. The classifier used 100 trees, with candidate maximum depths of 2 and 3, minimum leaf sizes of 5 and 10, and relative training weights for the High group of 1, 2, and 4. The weights were rescaled within each fit to have a mean of 1.

The warning threshold determined when the classifier output triggered a warning. Candidate thresholds ranged from 0 to 1 in increments of 0.05. The separate cutoff of 4 applied to the measured BAT-S score and determined the student's group.

The augmentation procedure tested three quantities of synthetic profiles. It added zero, half as many, or as many profiles as there were real High students in the current training split. Fractional target counts were rounded up. Each synthetic profile was based on two High students from that split.

The distance between two students was the average of eight values. These were the six absolute differences in ordered responses, each divided by four, and two indicators of category mismatch. Eligible pairs had a distance of at most 0.35, and each ordered response differed by at most two points. The first student was selected at random from those with an eligible neighbor. The second was selected at random from up to three of the closest eligible neighbors.

The six ordered responses were interpolated using one shared fraction drawn uniformly from 0.2 to 0.8. Each resulting value was rounded probabilistically to a valid response value. The new profile inherited the first student's sleep and study-hours categories and was assigned a High label. To be accepted, a profile had to fall within 0.25 of the first student. Duplicates of real training profiles or previously accepted synthetic profiles in that split were rejected.

The comparison on real students included an eight-input forest tuned without augmentation. A logistic regression baseline using standardized perceived workload alone was added after the earlier model comparisons. It used L₂ regularization with *C* = 1. The class weights and warning thresholds were selected from the same candidate values as for the forest.

Two fixed reference rules warned everyone or nobody. For the random reference, expected detections and false warnings were calculated for random selection of the same number of students as the forest warned in each outer test fold.

Earlier exploratory comparisons included support vector classifiers with a radial basis function kernel, using Small B or Broad D. These classifiers used real training data and tuned their settings and warning thresholds in the inner folds.

For a separate simulation, we trained a forest on all 97 real survey responses and applied it to synthetic profiles derived from those same responses. Each profile inherited its label from the source data.

## Warning Evaluation and Performance Measures

We used the same train-and-test approach for high-symptom warnings. We split the students into five groups with similar proportions of High cases, trained on four groups, and tested on the fifth. Each student was tested once per repetition, and we averaged results across five repetitions. Only real students contributed test predictions. We used training data to encode and standardize the forest inputs and to generate any synthetic profiles.

Within each training set, we formed four smaller groups in the same way to choose model settings, how much extra weight to give High cases, how many synthetic profiles to add, and when a model score should trigger a warning. We combined the four groups' validation predictions and used F₂ to score the settings. This score gives more weight to recall, the share of High students detected, than to precision, the share of warnings that correctly flagged High students. Ties favored higher precision, higher recall, a higher warning threshold, and then fewer synthetic profiles where applicable.

Balanced accuracy gives the High and Below-high groups equal weight by averaging the share correctly identified in each group. Average precision and the area under the receiver operating characteristic curve (ROC AUC) summarize how well a model ranks High students across warning thresholds. We used scikit-learn 1.9.1 to reproduce the ridge and warning evaluations and drew the other comparisons from their analysis records.

To estimate performance by chance, we shuffled the High and Below-high labels 199 times, keeping the group sizes fixed. Each student kept the same shuffled label across the five repetitions of a run. We rebuilt the splits and repeated the full forest procedure, including setting selection and training-only augmentation. We compared mean balanced accuracy across the shuffled runs with the value from the measured labels. The one-sided permutation *p*-value was (*b* + 1) / 200, where *b* counts shuffled runs that reached or exceeded the observed value [12].

To estimate uncertainty, we drew 2,000 bootstrap samples by resampling students with replacement within each outcome group. Each sampled student carried all five test predictions for both warning models. The resulting 95% intervals describe variation with the same group sizes and fitted predictions.

## References for this section

10. Schaufeli, Desart, and De Witte (2020). [Burnout Assessment Tool (BAT): Development, Validity, and Reliability](https://doi.org/10.3390/ijerph17249495).
11. Burnout Assessment Tool. [English student questionnaire](https://burnoutassessmenttool.be/wp-content/uploads/2024/02/BAT-S_ENG.pdf).
12. Phipson and Smyth (2010). [Permutation P-Values Should Never Be Zero: Calculating Exact P-Values When Permutations Are Randomly Drawn](https://doi.org/10.2202/1544-6115.1585).
