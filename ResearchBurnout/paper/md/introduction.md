# Introduction

## Context

Academic burnout in university students includes exhaustion, detachment from studies, and difficulties with thinking and regulating emotions [1]. In a survey of Brazilian university students, taking many courses and managing exams and assignments were among the academic demands associated with burnout [2]. Perceived workload therefore provides a baseline for assessing the value of additional survey responses.

Students use generative artificial intelligence (GenAI) for learning support and to carry out parts of academic tasks. In a survey of Thai undergraduates, academic stress and AI dependence were positively associated with burnout in the same regression model. Evidence of an association was weaker for AI-supported learning [3]. The main goal of this study was to predict current burnout scores and determine whether students' answers about GenAI use, including AI dependence, improve prediction beyond study conditions alone.

## Prediction Tasks and Evaluation Challenges

The analysis used a cross-sectional survey of 97 university students, 87 of whom reported enrollment in Lebanon. Symptoms reported at the time of the survey were measured on a scale of 1 to 5 using 12 items from the student version of the Burnout Assessment Tool (BAT-S).

The study had two objectives.

1. Predict the numerical burnout score and measure the change in prediction error when three GenAI questions are added to five questions about study conditions. The added questions cover GenAI use frequency, dependence on AI to complete academic work, and reliance on AI in place of independent thinking.
2. Identify students with a measured burnout score of at least 4, the study's High group (17 students). Compare a logistic regression model that uses workload alone with a random forest that uses the five study-condition and three GenAI questions. The comparison counts High students detected and warnings issued to students with measured scores below 4.

She et al. developed cutoffs for foreign-language learning burnout and used a separate school for exploratory external validation [4]. We evaluated performance by holding out students within our survey cohort.

## Main Findings

Adding the three GenAI questions modestly improved estimates of current burnout scores. The eight-question warning model performed above its shuffled-label reference. At the selected thresholds, workload alone detected more High cases at the same average false-warning count, and the paired performance differences remained uncertain.

## References for this section

1. Carmona-Halty et al. (2024). [Burnout Assessment Tool for Students (BAT-S): Evidence of Validity in a Chilean Sample of Undergraduate University Students](https://doi.org/10.3389/fpsyg.2024.1434412).
2. Câmara and Carlotto (2024). [Academic Stressors as Predictors of Burnout Syndrome in University Students](https://doi.org/10.1590/S1413-24782024290021).
3. Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
4. She et al. (2026). [Identifying Foreign Language Learning Burnout: Latent Profiles, Cutoff Points, and an Explainable Web-Based Calculator](https://doi.org/10.3389/fpsyg.2026.1836626).
