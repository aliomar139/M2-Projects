# Results and Discussion

## Burnout Scores and Survey Associations

The mean primary BAT-S score was 3.125 (SD 0.795), and the mean secondary score was 3.150 (SD 0.765). Seventeen of the 97 students (17.5%) met the High criterion of a primary score of at least 4. Cronbach's alpha was 0.900 for the 12 items in the primary score and 0.944 for the 23 core items. Alpha measures how consistently the items in each set vary together.

Among the 11 questions tested, avoidance or procrastination had the largest Spearman correlation with the primary burnout score (ρ = 0.445). Perceived workload and academic stress had correlations of 0.388 and 0.367, respectively. Of the three GenAI questions in Small B, AI dependence had the largest correlation (0.377), followed by reliance on AI in place of independent thinking (0.331) and frequency of use (0.220). These exploratory estimates describe the association between each question and the burnout score, without adjustment for other questions or for multiple testing.

## Numerical Score Prediction

GenAI questions modestly improved estimates of current burnout scores. With the same model type and test students, adding three GenAI questions to Small A reduced the average error for the primary score from 0.6183 to 0.5883 points on the 1-to-5 scale. Adding all the GenAI questions to Broad C reduced error from 0.6145 to 0.5933 points. Table II shows these matched ridge comparisons. Across five repetitions on the same students, the reductions ranged from 0.020 to 0.037 points for Small A/B and from 0.007 to 0.039 for Broad C/D.

Errors for the secondary score also fell, from 0.6001 to 0.5528 points for Small A versus Small B and from 0.5874 to 0.5578 points for Broad C versus Broad D. Broad D also had lower secondary-score error than Broad C in each repetition. The training-mean and training-median benchmarks gave primary-score errors of 0.6291 and 0.6262 points. With Small B, XGBoost gave larger errors than ridge for the primary (0.6155 points) and secondary (0.5749 points) scores.

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

## High-Symptom Warning Performance

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

## Earlier Warning Comparisons and Synthetic Check

The Broad D support vector classifier and the forest using Boruta-selected questions [13] issued fewer false warnings than the Small B forest and caught fewer High cases. TabPFN-2 [14] had higher average precision (0.616 versus 0.527). Its setting that favored recall caught 15.2 High cases and issued 44.0 false warnings on average.

In the separate simulation, the forest flagged 159 of 170 synthetic profiles that inherited a High label (93.5%). All 970 synthetic profiles came from survey responses already used to train the forest.

## Discussion

The score comparisons suggest that the GenAI questions added some information about current burnout severity beyond study conditions in this sample. We tested the added questions together. AI dependence had the strongest individual association with the burnout score among the three Small B questions. Plensamai reported a positive association among Thai undergraduates using a different burnout measure [3]. A matched comparison that adds AI dependence alone would estimate its individual contribution.

The warning comparison tested two complete procedures. The workload-only model and the Small B forest differ in both the type of model and the questions they use. To estimate how much the GenAI questions contribute to warnings, a matched comparison would use the same classifier and test groups with and without those questions.

About two in three forest warnings went to students with a measured score below 4. Of the 80 students in that group, 39 received at least one false warning across the five repetitions, and 27 received a false warning in at least three repetitions.

The survey measured GenAI use, study conditions, and symptoms at one time, so the direction of any relationship remains unclear. The convenience sample included 17 High cases, and we made several modeling choices after earlier analyses of these same students. The permutation result describes the selected forest procedure. A new cohort with measured BAT-S scores and procedures specified in advance would provide an independent test.

## References for this section

- [3] Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
- [13] Kursa and Rudnicki (2010). [Feature Selection with the Boruta Package](https://doi.org/10.18637/jss.v036.i11).
- [14] Hollmann et al. (2025). [Accurate Predictions on Small Data with a Tabular Foundation Model](https://doi.org/10.1038/s41586-024-08328-6).
