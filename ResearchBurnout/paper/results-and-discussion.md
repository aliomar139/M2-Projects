# Results and Discussion

## Burnout Scores and Survey Associations

The mean primary BAT-S score was 3.125 (SD 0.795), and the mean secondary score was 3.150 (SD 0.765). Seventeen of the 97 students (17.5%) met the High criterion of a primary score of at least 4. Cronbach's alpha was 0.900 for the 12 items in the primary score and 0.944 for the 23 core items. Alpha measures how consistently the items in each set vary together.

Among the 11 questions tested, avoidance or procrastination had the largest Spearman correlation with the primary burnout score (ρ = 0.445). Perceived workload and academic stress had correlations of 0.388 and 0.367, respectively. Of the three GenAI questions in Small B, AI dependence had the largest correlation (0.377), followed by reliance on AI in place of independent thinking (0.331) and frequency of use (0.220). These exploratory estimates describe the association between each question and the burnout score, without adjustment for other questions or for multiple testing.

## Numerical Score Prediction

The ridge regression comparison tested whether the three GenAI questions improved score prediction beyond study conditions. Both input sets were evaluated on the same held-out students. Small A contained five study-condition questions, and Small B added the three GenAI questions. Adding the three questions reduced mean absolute error (MAE) by 0.0300 points for the primary score, from 0.6183 to 0.5883. For the secondary score, MAE decreased from 0.6001 to 0.5528 points. With the same eight Small B inputs, XGBoost produced higher errors than ridge for both the primary score (0.6155 points) and the secondary score (0.5749 points).

Ridge regression with Broad D had a recorded primary-score MAE of 0.5933 points. The matched Broad C result and the training-mean and training-median benchmark errors are unavailable in the study records. The change in prediction error from adding GenAI questions to the broader set of inputs therefore remains undetermined.

Table II compares the primary-score errors for the full sample and the High group. With Small B inputs, weighted ridge reduced High-group MAE from 0.9329 to 0.6649 points and increased overall MAE from 0.5883 to 0.6282 points relative to ordinary ridge.

The fixed blend gave equal weight to ridge and support vector regression (SVR). It achieved lower MAE than either component for the full sample and for the High group. Its overall MAE was higher than that of ordinary ridge with Small B inputs. Selecting the blend weights in the inner folds increased both errors relative to the fixed blend.

*Table II. Recorded Mean Absolute Error for the Primary Burnout Score*

| Score procedure | Overall (points) | High (points) |
| --- | ---: | ---: |
| Ordinary ridge, Small B | 0.5883 | 0.9329 |
| Weighted ridge, Small B | 0.6282 | 0.6649 |
| High-priority SVR, Broad D | 0.6282 | 0.6705 |
| Fixed ridge/SVR blend | 0.6160 | 0.6422 |
| Inner-selected blend | 0.6343 | 0.6664 |

## High-Symptom Warning Performance

At the selected warning thresholds, workload-only logistic regression detected an average of 16.0 of the 17 High students. The random forest used the five study-condition and three GenAI questions and detected 14.8 High students on average. Both models averaged 28.0 false warnings among the 80 Below-high students. Table III reports the results across five cross-validation repetitions on the same 97 students.

The matched random reference gives the expected performance of a rule that selects students at random and issues the same number of warnings as the forest in each test fold. Precision was recorded as zero for the rule that issued no warnings.

*Table III. Warning Performance on Held-Out Real Students*

| Warning rule | High detected /17 | False warnings /80 | Recall (%) | Precision (%) |
| --- | ---: | ---: | ---: | ---: |
| Workload only | 16.0 | 28.0 | 94.1 | 36.4 |
| Selected forest | 14.8 | 28.0 | 87.1 | 34.7 |
| Forest, no augmentation | 14.4 | 29.6 | 84.7 | 32.7 |
| Random, matched count | 7.6 | 35.2 | 44.6 | 17.7 |
| Warn everyone | 17.0 | 80.0 | 100.0 | 17.5 |
| Warn nobody | 0.0 | 0.0 | 0.0 | 0.0 |

At the selected thresholds, workload-only logistic regression achieved higher balanced accuracy (79.6% versus 76.0%) and a higher F₂ score (0.714 versus 0.668) than the selected forest. Across warning thresholds, the forest achieved higher average precision (0.527 versus 0.423), and workload-only logistic regression achieved a higher area under the receiver operating characteristic (ROC) curve (0.824 versus 0.809).

With training augmentation available during tuning, the forest detected an average of 0.4 more High students and issued 1.6 fewer false warnings than the forest tuned without augmentation.

The permutation test evaluated the selected forest against chance within the study sample. With the original labels, the forest achieved 76.0% balanced accuracy. Across the 199 shuffled-label evaluations, mean balanced accuracy was 49.6% and the maximum was 63.6%. All shuffled-label results fell below the observed value, yielding a corrected one-sided permutation *p*-value of 0.005.

Table IV gives conditional intervals for the forest and the paired differences between the forest and workload-only logistic regression. The interval calculation resampled students with the fitted predictions held fixed. All three paired intervals included zero. Across the five cross-validation repetitions, the forest's recall ranged from 82.4% to 94.1%, and its false-warning count ranged from 24 to 30.

*Table IV. Conditional 95% Intervals for Warning Performance*

| Metric | Forest (%) | Forest minus workload (percentage points) |
| --- | ---: | ---: |
| Recall | 70.6 to 100.0 | −20.0 to 2.4 |
| Precision | 27.9 to 42.7 | −7.3 to 3.1 |
| Balanced accuracy | 66.4 to 83.8 | −11.1 to 2.3 |

## Earlier Warning Comparisons and Synthetic Check

Earlier experiment records show the trade-off between detecting High students and issuing false warnings. Under F₂ tuning, the 23-input support vector classifier averaged 13.0 High detections and 19.4 false warnings. The forest fitted with inputs selected by Boruta [13] averaged 12.4 High detections and 22.2 false warnings. Both procedures detected fewer High students than the selected forest.

In an earlier comparison using the same eight inputs, TabPFN-2 [14] had higher average precision (0.616) than the selected forest. The TabPFN-2 rule selected using F₂ averaged 13.8 High detections and 24.2 false warnings. The rule tuned to favor recall averaged 15.2 High detections and 44.0 false warnings.

The synthetic check used 970 profiles generated from survey responses already used to fit the model. The model fitted on all 97 students flagged 159 of the 170 profiles assigned a High label (93.5%). This rate measures agreement with the High labels inherited from the source responses.

## Discussion

The measured reduction in ridge regression error applies to the three GenAI questions together. AI dependence had the strongest individual association with the burnout score among those three questions. Plensamai reported a positive association in the same direction among Thai undergraduates using a different burnout measure [3]. An additional matched comparison that adds AI dependence alone would be needed to estimate its individual contribution to prediction.

At the chosen warning thresholds, workload-only logistic regression detected more High cases at the same average false-warning count as the random forest. The warning comparison varied both the classifier and the inputs, so these results compare the two procedures as a whole.

About two of every three warnings from the selected forest went to students with a burnout score below the study cutoff. Of the 80 Below-high students, 39 received at least one false warning across the five repetitions, and 27 received a false warning in at least three repetitions.

The survey measured GenAI habits, study conditions, and symptoms at one time. The order of events therefore remains unresolved. The convenience sample contained 17 High cases, and several model and input choices followed earlier analyses of the same students. The permutation test applies to the selected forest procedure, and the paired intervals apply to its comparison with workload-only logistic regression. Estimating warning performance in a new cohort requires fixing each procedure in advance and evaluating it on independently recruited students with measured BAT-S outcomes.

## References for this section

- [3] Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
- [13] Kursa and Rudnicki (2010). [Feature Selection with the Boruta Package](https://doi.org/10.18637/jss.v036.i11).
- [14] Hollmann et al. (2025). [Accurate Predictions on Small Data with a Tabular Foundation Model](https://doi.org/10.1038/s41586-024-08328-6).
