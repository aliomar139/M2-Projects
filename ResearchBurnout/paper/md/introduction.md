# Introduction

## Context

Academic burnout in university students includes exhaustion, detachment from studies, and difficulties with thinking and regulating emotions [1]. In a survey of Brazilian university students, taking many courses and managing exams and assignments were among the academic demands associated with burnout [2]. Perceived workload therefore provides a baseline for assessing the value of additional survey responses.

Students use generative artificial intelligence (GenAI) for learning support and to carry out parts of academic tasks. In a survey of Thai undergraduates, academic stress and AI dependence were positively associated with burnout in the same regression model. Evidence of an association was weaker for AI-supported learning [3]. The main goal of this study was to predict current burnout scores and determine whether students' answers about GenAI use, including AI dependence, improve prediction beyond study conditions alone.

## Prediction Tasks and Evaluation Challenges

The analysis used a cross-sectional survey of 97 university students, 87 of whom reported enrollment in Lebanon. Symptoms reported at the time of the survey were measured on a scale of 1 to 5 using 12 items from the student version of the Burnout Assessment Tool (BAT-S).

The study had two objectives.

1. Predict the numerical burnout score and measure the change in prediction error when three GenAI questions are added to five questions about study conditions. The added questions cover GenAI use frequency, dependence on AI to complete academic work, and reliance on AI in place of independent thinking.
2. Identify students with a measured burnout score of at least 4, the study's High group (17 students). Compare a logistic regression model that uses workload alone with a random forest that uses the five study-condition and three GenAI questions. The comparison counts High students detected and warnings issued to students with measured scores below 4.

Prior studies illustrate how the choice of outcome and evaluation sample shapes a prediction study. She et al. defined cutoffs for burnout specific to foreign-language learning and evaluated their models on students from a separate school [4]. In a preprint on a combined burnout and depression outcome, Dehghan and Ashrafi showed how overlap between a predictor and part of the outcome can dominate model explanations [5]. In the present study, the predictor sets excluded all BAT-S responses and derived scores. Performance was evaluated on students held out from model fitting within the survey sample.

## Study Contributions and Main Findings

Adding the three GenAI questions as a set reduced mean absolute error from 0.6183 to 0.5883 points on the 1-to-5 scale. This comparison used ridge regression and identical evaluation splits for both input sets. Even with the added questions, the model averaged 0.9329 points of error in the High group and tended to underestimate scores there.

At the selected warning thresholds, workload-only logistic regression detected an average of 16.0 of the 17 High cases (94.1%). The eight-input random forest detected 14.8 cases (87.1%). Both models averaged 28 false warnings among the 80 students below the cutoff. Warning precision, the percentage of warnings that identified High cases, was 36.4% for workload-only logistic regression and 34.7% for the random forest. These figures are averages from five cross-validation repetitions on the same 97 students.

Across warning thresholds, the random forest achieved higher average precision than workload-only logistic regression (0.527 versus 0.423). With the original labels, the random forest achieved 76.0% balanced accuracy, the mean of the correct classification rates for the two groups. This value exceeded the balanced accuracy of all 199 runs of the selected forest procedure with shuffled labels (permutation *p* = 0.005).

In an earlier comparison, the 23-input support vector classifier averaged 19.4 false warnings and detected 13.0 of the 17 High cases. The classifier generated fewer false warnings than the random forest and detected fewer High cases.

## Paper Structure

Related Work reviews student burnout measurement, GenAI use, and model interpretation. Study Design and Evaluation describes the survey, outcomes, models, and validation procedure. Results and Discussion presents the model comparisons and their limitations. The conclusion summarizes what the survey results support.

## References for this section

1. Carmona-Halty et al. (2024). [Burnout Assessment Tool for Students (BAT-S): Evidence of Validity in a Chilean Sample of Undergraduate University Students](https://doi.org/10.3389/fpsyg.2024.1434412).
2. Câmara and Carlotto (2024). [Academic Stressors as Predictors of Burnout Syndrome in University Students](https://doi.org/10.1590/S1413-24782024290021).
3. Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
4. She et al. (2026). [Identifying Foreign Language Learning Burnout: Latent Profiles, Cutoff Points, and an Explainable Web-Based Calculator](https://doi.org/10.3389/fpsyg.2026.1836626).
5. Dehghan and Ashrafi (2026). [Auditing Construct Overlap in Explainable Machine Learning: Evidence from Burnout-Depression Prediction Across Student Cohorts](https://doi.org/10.48550/arXiv.2607.10633). arXiv preprint.
