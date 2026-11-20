# Student Burnout, Study Conditions, and Generative Artificial Intelligence Use: An Exploratory Prediction Study

Ali Omar and Abdallah Mestrah

*Lebanese University*

## Abstract

We analyzed 97 responses to a cross-sectional survey, including 87 from students who reported attending universities in Lebanon, to test whether questions about generative artificial intelligence (GenAI) use and dependence improved estimates of current burnout. We also compared an eight-question model with a workload-only model for identifying students with high burnout symptoms, defined as a score of at least 4 on the 12-item Burnout Assessment Tool for Students (range 1–5). Both analyses used repeated nested cross-validation. The eight-question model achieved 76.0% balanced accuracy, exceeding all 199 shuffled-label results (permutation p = 0.005). At the selected warning thresholds, the workload-only model detected an average of 16.0 of the 17 high-symptom cases, compared with 14.8 for the eight-question model. Both averaged 28 false warnings among the 80 students below the cutoff. The conditional 95% intervals for paired differences in recall, precision, and balanced accuracy all included zero. In a matched comparison, adding three GenAI questions to five study-condition questions reduced mean absolute error for burnout scores from 0.6183 to 0.5883 points. Both tasks still need validation in an independent student cohort.

## Index Terms

Academic burnout, generative artificial intelligence, logistic regression, random forests, university students.

## Introduction

### Context

Academic burnout in university students includes exhaustion, detachment from studies, and difficulties with thinking and regulating emotions [1]. In a survey of Brazilian university students, taking many courses and managing exams and assignments were among the academic demands associated with burnout [2]. Perceived workload therefore provides a baseline for assessing the value of additional survey responses.

Students use generative artificial intelligence (GenAI) for learning support and to carry out parts of academic tasks. In a survey of Thai undergraduates, academic stress and AI dependence were positively associated with burnout in the same regression model. Evidence of an association was weaker for AI-supported learning [3]. The main goal of this study was to predict current burnout scores and determine whether students' answers about GenAI use, including AI dependence, improve prediction beyond study conditions alone.

### Prediction Tasks and Evaluation Challenges

The analysis used a cross-sectional survey of 97 university students, 87 of whom reported enrollment in Lebanon. Symptoms reported at the time of the survey were measured on a scale of 1 to 5 using 12 items from the student version of the Burnout Assessment Tool (BAT-S).

The study had two objectives.

1. Predict the numerical burnout score and measure the change in prediction error when three GenAI questions are added to five questions about study conditions. The added questions cover GenAI use frequency, dependence on AI to complete academic work, and reliance on AI in place of independent thinking.
2. Identify students with a measured burnout score of at least 4, the study's High group (17 students). Compare a logistic regression model that uses workload alone with a random forest that uses the five study-condition and three GenAI questions. The comparison counts High students detected and warnings issued to students with measured scores below 4.

She et al. developed cutoffs for foreign-language learning burnout and used a separate school for exploratory external validation [4]. We evaluated performance by holding out students within our survey cohort.

### Main Findings

Adding the three GenAI questions modestly improved estimates of current burnout scores. The eight-question warning model performed above its shuffled-label reference. At the selected thresholds, workload alone detected more High cases at the same average false-warning count, and the paired performance differences remained uncertain.

## Related Work

### Measuring Student Burnout

Student burnout studies differ in both measurement instruments and score cutoffs. Carmona-Halty et al. found support for four BAT-S dimensions in 461 Chilean undergraduates [1]. Kiss and Pikó used the Maslach Burnout Inventory–Student Survey with Hungarian medical students and applied separate cutoffs for exhaustion, cynicism, and academic efficacy [5]. In the present study, regression estimates the 12-item BAT-S score. The classification task uses a cutoff of 4 on the same score to define the High group.

### Study Conditions and GenAI Use

Câmara and Carlotto found that taking many courses and managing exams and assignments were among the stressors associated with burnout in Brazilian university students [2]. The present survey measures perceived workload with one question asking how heavy and overwhelming students find their academic workload. This item is the only input to the logistic regression baseline for the warning task.

Measures of GenAI use can describe frequency, purpose, or dependence. Plensamai found a positive association between AI dependence and burnout after adjusting for academic stress and AI-supported learning [3]. In a survey of Chinese university students, Wang et al. found positive correlations between academic stress, AI dependence, and burnout scores [6]. Both surveys measured these variables at one point in time. The present score prediction experiments compare prediction errors for held-out students with and without GenAI items, using the same model family within each comparison.

### Comparing Burnout Prediction Models

Some burnout classifiers use symptom scores as predictors. Rahmadani and Sriani used burnout dimension scores as inputs to a decision tree that classified Indonesian university students into three burnout levels [7]. In the present study, BAT-S responses define the outcomes, and the prediction models use answers from the other parts of the survey.

Saklani et al. used a 23-item BAT-S mean to define three groups in an analysis of 113 Indian engineering students [8]. With the full set of predictors, their logistic regression and random forest models performed better than in the corresponding runs with shuffled labels. The uncertainty intervals for the gains from adding interaction terms included zero. The present study evaluates the selected random forest against runs with shuffled labels to assess performance relative to chance. The comparison with workload-only logistic regression examines High detections and false warnings at the selected thresholds.

### Interpreting Model Outputs

She et al. used Shapley additive explanations (SHAP) to interpret their model. Foreign-language enjoyment and academic stress contributed most to its predictions [4].

Predictor rankings can depend on how the outcome is defined. In a preprint, Dehghan and Ashrafi found that trait anxiety fell from first to sixth in a model with a combined burnout and depression outcome after they removed the variance it shared with the depression subscale [9]. Our study compares performance across sets of survey questions and examines prediction errors by symptom level.

## Study Design and Evaluation

[Fig. 1. Input sets for score estimation and high-symptom warnings](../tex/figures/study-design.pdf)

### Participants and Questionnaire


We used convenience sampling to recruit Lebanese undergraduate and graduate students from multiple universities for an online cross-sectional survey. The survey link circulated primarily through WhatsApp among student contacts and their peers. We assessed eligibility using recruitment information and self-reported answers.

We analyzed all 97 survey submissions received from 4 to 18 October 2026. Of the respondents, 87 reported attending a university in Lebanon. Based on recruitment information, we identified the other 10 as Lebanese students studying abroad. After data collection, we revised the original location-based eligibility rule to include them.

The opening pages of the Google Forms survey explained the study and stated that participation was voluntary. Respondents indicated consent by choosing to continue. The form did not ask for names, contact information, or other direct identifiers. The study was not submitted for formal ethics review.

The questionnaire contained 20 questions on student background, study conditions, GenAI use, and intention to continue studying. It then presented the 23 core items of the English student version of the Burnout Assessment Tool (BAT-S) [10], [11]. Short explanations clarified the word *cynical* in BAT-S item Q33 and *procrastinate* in the separate study-conditions item Q18.

### Outcomes and Data Preparation

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

### Input Sets and Score Prediction

To test whether GenAI questions improved score prediction, we compared input sets using the same model family and evaluation splits within each comparison. Small A used five study-condition questions on perceived workload, sleep duration category, independent study-hours category, financial strain, and university support. Small B added three questions on GenAI use frequency, self-reported dependence on AI to complete academic work, and reliance on AI in place of independent thinking, for eight inputs.

Broad C used 13 inputs on background and study conditions (Q1–Q7 and Q14–Q19). It added eight questions to Small A, covering enrollment location, academic level, major, GPA range, electricity outages, internet quality, academic stress, and avoidance or procrastination.

Broad D added all six GenAI questions (Q8–Q13) to Broad C, covering frequency, use cases, dependence, reliance in place of independent thinking, verification of AI outputs, and concerns about being flagged for AI use. Q9 supplied separate yes-or-no inputs for concept explanations, writing, coding, summaries, and direct solutions, so 19 questions yielded 23 inputs before categorical encoding. All input sets excluded BAT-S responses and scores, submission timestamps, and the item on intention to continue studying.

We compared Small A with Small B using linear regression, ridge regression, and a shallow random forest. We used ridge for Broad C and Broad D as well. Ridge is linear regression with a penalty that discourages large weights on the inputs. The two benchmarks predicted the training group's mean or median score for every test student.

For each repetition, we split the 97 students into five groups. We trained on four groups and tested on the fifth, taking turns until every student had one test prediction. We ran this process with five different shuffles. Within each training set, we used four smaller groups to choose settings by mean absolute error (MAE), the average distance between predicted and measured scores. We kept predictions within 1 to 5 during tuning and testing and calculated MAE for all students and for those with measured scores of at least 4.

We represented categorical answers such as sleep-duration bands as yes-or-no indicators, leaving the first category as the reference. We used training data to put the ridge inputs on a common scale and tested penalties from 0.01 to 1000 in tenfold steps. For the 200-tree regression forest, we tried maximum depths of 2 or 3 and minimum leaf sizes of 5 or 10.

Follow-up experiments gave more weight to errors on high scores. The selected follow-up predictor averaged two estimates equally, one from weighted ridge on Small B and one from high-priority support vector regression on Broad D.

### High-Symptom Warning Models

The selected random forest classifier used Small B to predict the High label directly. The classifier used 100 trees, with candidate maximum depths of 2 and 3, minimum leaf sizes of 5 and 10, and relative training weights for the High group of 1, 2, and 4. The weights were rescaled within each fit to have a mean of 1.

The warning threshold determined when the classifier output triggered a warning. Candidate thresholds ranged from 0 to 1 in increments of 0.05. The separate cutoff of 4 applied to the measured BAT-S score and determined the student's group.

The augmentation procedure tested three quantities of synthetic profiles. It added zero, half as many, or as many profiles as there were real High students in the current training split. Fractional target counts were rounded up. Each synthetic profile was based on two High students from that split.

The distance between two students was the average of eight values. These were the six absolute differences in ordered responses, each divided by four, and two indicators of category mismatch. Eligible pairs had a distance of at most 0.35, and each ordered response differed by at most two points. The first student was selected at random from those with an eligible neighbor. The second was selected at random from up to three of the closest eligible neighbors.

The six ordered responses were interpolated using one shared fraction drawn uniformly from 0.2 to 0.8. Each resulting value was rounded probabilistically to a valid response value. The new profile inherited the first student's sleep and study-hours categories and was assigned a High label. To be accepted, a profile had to fall within 0.25 of the first student. Duplicates of real training profiles or previously accepted synthetic profiles in that split were rejected.

The comparison on real students included an eight-input forest tuned without augmentation. A logistic regression baseline using standardized perceived workload alone was added after the earlier model comparisons. It used L₂ regularization with *C* = 1. The class weights and warning thresholds were selected from the same candidate values as for the forest.

Two fixed reference rules warned everyone or nobody. For the random reference, expected detections and false warnings were calculated for random selection of the same number of students as the forest warned in each outer test fold.

Earlier exploratory comparisons included support vector classifiers with a radial basis function kernel, using Small B or Broad D. These classifiers used real training data and tuned their settings and warning thresholds in the inner folds.

A separate historical fit used all 97 students. Its forest settings were depth 3, a minimum leaf size of 10, a relative High weight of 2, a warning threshold of 0.35, and zero synthetic training rows. The simulation applied this fitted model to 970 interpolated profiles. The profile labels were inherited from the students in the training data. The estimates for real students were obtained from the outer test folds described below.

### Warning Evaluation and Performance Measures

We used the same train-and-test approach for high-symptom warnings. We split the students into five groups with similar proportions of High cases, trained on four groups, and tested on the fifth. Each student was tested once per repetition, and we averaged results across five repetitions. Only real students contributed test predictions. We used training data to encode and standardize the forest inputs and to generate any synthetic profiles.

Within each training set, we formed four smaller groups in the same way to choose model settings, how much extra weight to give High cases, how many synthetic profiles to add, and when a model score should trigger a warning. We combined the four groups' validation predictions and used F₂ to score the settings. This score gives more weight to recall, the share of High students detected, than to precision, the share of warnings that correctly flagged High students. Ties favored higher precision, higher recall, a higher warning threshold, and then fewer synthetic profiles where applicable.

Balanced accuracy gives the High and Below-high groups equal weight by averaging the share correctly identified in each group. Average precision and the area under the receiver operating characteristic curve (ROC AUC) summarize how well a model ranks High students across warning thresholds. We used scikit-learn 1.9.1 to reproduce the ridge and warning evaluations and drew the other comparisons from their analysis records.

To estimate performance by chance, we shuffled the High and Below-high labels 199 times, keeping the group sizes fixed. Each student kept the same shuffled label across the five repetitions of a run. We rebuilt the splits and repeated the full forest procedure, including setting selection and training-only augmentation. We compared mean balanced accuracy across the shuffled runs with the value from the measured labels. The one-sided permutation *p*-value was (*b* + 1) / 200, where *b* counts shuffled runs that reached or exceeded the observed value [12].

To estimate uncertainty, we drew 2,000 bootstrap samples by resampling students with replacement within each outcome group. Each sampled student carried all five test predictions for both warning models. The resulting 95% intervals describe variation with the same group sizes and fitted predictions.

## Results and Discussion

### Burnout Scores and Survey Associations

The mean primary BAT-S score was 3.125 (SD 0.795), and the mean secondary score was 3.150 (SD 0.765). Seventeen of the 97 students (17.5%) met the High criterion of a primary score of at least 4. Cronbach's alpha was 0.900 for the 12 items in the primary score and 0.944 for the 23 core items. Alpha measures how consistently the items in each set vary together.

Among the 11 questions tested, avoidance or procrastination had the largest Spearman correlation with the primary burnout score (ρ = 0.445). Perceived workload and academic stress had correlations of 0.388 and 0.367, respectively. Of the three GenAI questions in Small B, AI dependence had the largest correlation (0.377), followed by reliance on AI in place of independent thinking (0.331) and frequency of use (0.220). These exploratory estimates describe the association between each question and the burnout score, without adjustment for other questions or for multiple testing.

### Numerical Score Prediction

GenAI questions modestly improved estimates of current burnout scores. With the same model type and test students, adding three GenAI questions to Small A reduced the average error for the primary score from 0.6183 to 0.5883 points on the 1-to-5 scale. Adding all the GenAI questions to Broad C reduced error from 0.6145 to 0.5933 points. Table II shows these matched ridge comparisons.

Errors for the secondary score also fell, from 0.6001 to 0.5528 points for Small A versus Small B and from 0.5874 to 0.5578 points for Broad C versus Broad D. Broad D had lower error than Broad C in all five repetitions for both outcomes. The training-mean and training-median benchmarks gave primary-score errors of 0.6291 and 0.6262 points. With Small B, XGBoost gave larger errors than ridge for the primary (0.6155 points) and secondary (0.5749 points) scores.

Estimating scores for the High group was harder. Ordinary ridge with Small B tended to predict scores that were too low. Giving High cases more weight reduced their error from 0.9329 to 0.6649 points, while increasing overall error from 0.5883 to 0.6282 points.

The selected follow-up score predictor averaged the weighted ridge and high-priority support vector regression (SVR) estimates. This equal-weight blend had lower error than either of its components and the blend whose weights were tuned (Table II). Its overall error was 0.6160 points, higher than ordinary ridge with Small B, while its High-group error fell to 0.6422 points. The warning task below tested whether a model could flag High students directly.

*Table II. Recorded Mean Absolute Error for the Primary Burnout Score*

| Score procedure | Overall (points) | High (points) |
| --- | ---: | ---: |
| Ordinary ridge, Small A | 0.6183 | 1.0842 |
| Ordinary ridge, Small B | 0.5883 | 0.9329 |
| Ordinary ridge, Broad C | 0.6145 | 1.0237 |
| Ordinary ridge, Broad D | 0.5933 | 0.9281 |
| Weighted ridge, Small B | 0.6282 | 0.6649 |
| High-priority SVR, Broad D | 0.6282 | 0.6705 |
| Fixed ridge/SVR blend | 0.6160 | 0.6422 |
| Inner-selected blend | 0.6343 | 0.6664 |

### High-Symptom Warning Performance

At the selected warning thresholds, workload-only logistic regression detected an average of 16.0 of the 17 High students across five repetitions. The Small B forest detected 14.8 on average. Both issued an average of 28 false warnings among the 80 students below the cutoff (Fig. 2). Recall was 94.1% for workload alone and 87.1% for the forest. Precision was 36.4% and 34.7%, respectively.

[Fig. 2. Mean detections and false warnings per repetition on held-out students](../tex/figures/warning-counts.pdf)

At those thresholds, workload alone also had higher balanced accuracy (79.6% versus 76.0%) and a higher F₂ score (0.714 versus 0.668). When we assessed ranking across thresholds, the forest had higher average precision (0.527 versus 0.423), and workload alone had higher ROC AUC (0.824 versus 0.809).

When tuning could add synthetic profiles during training, the forest averaged 0.4 more High detections and 1.6 fewer false warnings than the forest tuned without them.

The forest performed better with the measured labels than with any of the 199 shuffled label assignments. Its balanced accuracy was 76.0%, compared with a mean of 49.6% and a maximum of 63.6% across the shuffled runs (Fig. 3). The one-sided permutation *p*-value was 0.005.

[Fig. 3. Balanced accuracy of the Small B forest with observed and shuffled labels](../tex/figures/permutation-accuracy.pdf)

The intervals for differences between the forest and workload alone all included zero (Table III). The observed workload advantage at the selected thresholds therefore remains uncertain. Across the five repetitions, the forest's recall ranged from 82.4% to 94.1%, and its false-warning count ranged from 24 to 30.

*Table III. Conditional 95% Intervals for Warning Performance*

| Metric | Forest (%) | Forest minus workload (percentage points) |
| --- | ---: | ---: |
| Recall | 70.6 to 100.0 | −20.0 to 2.4 |
| Precision | 27.9 to 42.7 | −7.3 to 3.1 |
| Balanced accuracy | 66.4 to 83.8 | −11.1 to 2.3 |

### Earlier Warning Comparisons and Synthetic Check

Some earlier warning models issued fewer false warnings and detected fewer High students than the Small B forest. The Broad D support vector classifier, tuned using F₂, averaged 13.0 detections and 19.4 false warnings. The forest using questions selected by Boruta [13] averaged 12.4 detections and 22.2 false warnings.

TabPFN-2 [14] used the Small B questions and had higher average precision (0.616) than the selected forest. Its F₂-tuned rule averaged 13.8 detections and 24.2 false warnings. A rule that placed more weight on recall detected 15.2 and issued 44.0 false warnings on average.

In a separate simulation, we generated 970 profiles from the same 97 survey responses used to train the forest. The model flagged 159 of the 170 synthetic profiles that inherited a High label (93.5%). This measures agreement with labels inherited from the training data.

### Discussion

The score comparisons suggest that the GenAI questions added some information about current burnout severity beyond study conditions in this sample. We tested the added questions together. AI dependence had the strongest individual association with the burnout score among the three Small B questions. Plensamai reported a positive association among Thai undergraduates using a different burnout measure [3]. A matched comparison that adds AI dependence alone would estimate its individual contribution.

The warning comparison tested two complete procedures. The workload-only model and the Small B forest differ in both the type of model and the questions they use. To estimate how much the GenAI questions contribute to warnings, a matched comparison would use the same classifier and test groups with and without those questions.

About two in three forest warnings went to students with a measured score below 4. Of the 80 students in that group, 39 received at least one false warning across the five repetitions, and 27 received a false warning in at least three repetitions.

The survey measured GenAI use, study conditions, and symptoms at one time, so the direction of any relationship remains unclear. The convenience sample included 17 High cases, and we made several modeling choices after earlier analyses of these same students. The permutation result describes the selected forest procedure. A new cohort with measured BAT-S scores and procedures specified in advance would provide an independent test.

## Conclusion

Adding GenAI questions modestly improved estimates of current burnout scores in both matched comparisons. The Small B forest performed above its shuffled-label reference. At the selected warning thresholds, workload alone detected more High cases at the same average false-warning count, and the paired intervals for the differences included zero. An independent evaluation should specify the prediction procedures in advance and test them in a new cohort with measured BAT-S scores.

## References

1. Carmona-Halty et al. (2024). [Burnout Assessment Tool for Students (BAT-S): Evidence of Validity in a Chilean Sample of Undergraduate University Students](https://doi.org/10.3389/fpsyg.2024.1434412).
2. Câmara and Carlotto (2024). [Academic Stressors as Predictors of Burnout Syndrome in University Students](https://doi.org/10.1590/S1413-24782024290021).
3. Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
4. She et al. (2026). [Identifying Foreign Language Learning Burnout: Latent Profiles, Cutoff Points, and an Explainable Web-Based Calculator](https://doi.org/10.3389/fpsyg.2026.1836626).
5. Kiss and Pikó (2025). [Risk and Protective Factors of Student Burnout Among Medical Students: A Multivariate Analysis](https://doi.org/10.1186/s12909-025-06956-8).
6. Wang et al. (2026). [When Cognitive Offloading Becomes Dependence: How AI Dependence Mediates the Pathway from Academic Stress to Burnout and Anxiety](https://doi.org/10.1186/s40359-026-04911-w).
7. Rahmadani and Sriani (2026). [Prediction of Burnout Syndrome Risk in University Students Using the C5.0 Algorithm](https://doi.org/10.30865/jurikom.v13i2.9550).
8. Saklani et al. (2026). [Low-Dimensional Burnout Risk Classification in Engineering Students: The Role of Demand-Recovery Interaction Features](https://doi.org/10.3389/fpsyg.2026.1934021).
9. Dehghan and Ashrafi (2026). [Auditing Construct Overlap in Explainable Machine Learning: Evidence from Burnout-Depression Prediction Across Student Cohorts](https://doi.org/10.48550/arXiv.2607.10633). arXiv preprint.
10. Schaufeli, Desart, and De Witte (2020). [Burnout Assessment Tool (BAT): Development, Validity, and Reliability](https://doi.org/10.3390/ijerph17249495).
11. Burnout Assessment Tool. [English student questionnaire](https://burnoutassessmenttool.be/wp-content/uploads/2024/02/BAT-S_ENG.pdf).
12. Phipson and Smyth (2010). [Permutation P-Values Should Never Be Zero: Calculating Exact P-Values When Permutations Are Randomly Drawn](https://doi.org/10.2202/1544-6115.1585).
13. Kursa and Rudnicki (2010). [Feature Selection with the Boruta Package](https://doi.org/10.18637/jss.v036.i11).
14. Hollmann et al. (2025). [Accurate Predictions on Small Data with a Tabular Foundation Model](https://doi.org/10.1038/s41586-024-08328-6).
