# Related Work

## Measuring Student Burnout

Student burnout studies differ in both measurement instruments and score cutoffs. Carmona-Halty et al. found support for four BAT-S dimensions in 461 Chilean undergraduates [1]. Kiss and Pikó used the Maslach Burnout Inventory–Student Survey with Hungarian medical students and applied separate cutoffs for exhaustion, cynicism, and academic efficacy [5]. In the present study, regression estimates the 12-item BAT-S score. The classification task uses a cutoff of 4 on the same score to define the High group.

## Study Conditions and GenAI Use

Câmara and Carlotto found that taking many courses and managing exams and assignments were among the stressors associated with burnout in Brazilian university students [2]. The present survey measures perceived workload with one question asking how heavy and overwhelming students find their academic workload. This item is the only input to the logistic regression baseline for the warning task.

Measures of GenAI use can describe frequency, purpose, or dependence. Plensamai found a positive association between AI dependence and burnout after adjusting for academic stress and AI-supported learning [3]. In a survey of Chinese university students, Wang et al. found positive correlations between academic stress, AI dependence, and burnout scores [6]. Both surveys measured these variables at one point in time. The present score prediction experiments compare prediction errors for held-out students with and without GenAI items, using the same model family within each comparison.

## Comparing Burnout Prediction Models

Some burnout classifiers use symptom scores as predictors. Rahmadani and Sriani used burnout dimension scores as inputs to a decision tree that classified Indonesian university students into three burnout levels [7]. In the present study, BAT-S responses define the outcomes, and the prediction models use answers from the other parts of the survey.

Saklani et al. used a 23-item BAT-S mean to define three groups in an analysis of 113 Indian engineering students [8]. With the full set of predictors, their logistic regression and random forest models performed better than in the corresponding runs with shuffled labels. The uncertainty intervals for the gains from adding interaction terms included zero. The present study evaluates the selected random forest against runs with shuffled labels to assess performance relative to chance. The comparison with workload-only logistic regression examines High detections and false warnings at the selected thresholds.

## Interpreting Model Outputs

She et al. used Shapley additive explanations (SHAP) to interpret their model. Foreign-language enjoyment and academic stress contributed most to its predictions [4].

Predictor rankings can depend on how the outcome is defined. In a preprint, Dehghan and Ashrafi found that trait anxiety fell from first to sixth in a model with a combined burnout and depression outcome after they removed the variance it shared with the depression subscale [9]. Our study compares performance across sets of survey questions and examines prediction errors by symptom level.

## References for this section

1. Carmona-Halty et al. (2024). [Burnout Assessment Tool for Students (BAT-S): Evidence of Validity in a Chilean Sample of Undergraduate University Students](https://doi.org/10.3389/fpsyg.2024.1434412).
2. Câmara and Carlotto (2024). [Academic Stressors as Predictors of Burnout Syndrome in University Students](https://doi.org/10.1590/S1413-24782024290021).
3. Plensamai (2026). [AI-Supported Learning, AI Dependency, and Academic Stress as Predictors of Student Burnout](https://ph02.tci-thaijo.org/index.php/jtir/article/view/266804).
4. She et al. (2026). [Identifying Foreign Language Learning Burnout: Latent Profiles, Cutoff Points, and an Explainable Web-Based Calculator](https://doi.org/10.3389/fpsyg.2026.1836626).
5. Kiss and Pikó (2025). [Risk and Protective Factors of Student Burnout Among Medical Students: A Multivariate Analysis](https://doi.org/10.1186/s12909-025-06956-8).
6. Wang et al. (2026). [When Cognitive Offloading Becomes Dependence: How AI Dependence Mediates the Pathway from Academic Stress to Burnout and Anxiety](https://doi.org/10.1186/s40359-026-04911-w).
7. Rahmadani and Sriani (2026). [Prediction of Burnout Syndrome Risk in University Students Using the C5.0 Algorithm](https://doi.org/10.30865/jurikom.v13i2.9550).
8. Saklani et al. (2026). [Low-Dimensional Burnout Risk Classification in Engineering Students: The Role of Demand-Recovery Interaction Features](https://doi.org/10.3389/fpsyg.2026.1934021).
9. Dehghan and Ashrafi (2026). [Auditing Construct Overlap in Explainable Machine Learning: Evidence from Burnout-Depression Prediction Across Student Cohorts](https://doi.org/10.48550/arXiv.2607.10633). arXiv preprint.
