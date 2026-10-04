# Research Project Blueprint

# Project Title

**Predicting Academic Burnout and Academic Continuation Risk in Low-Sample Regimes Using Explainable Machine Learning**

Alternative title:

**An Explainable Machine Learning Framework for Early Detection of Student Burnout Under Limited Data Conditions**

---

# 1. Research Overview

## Purpose and intended output

The research aims to build and evaluate an explainable machine learning model that predicts academic burnout risk from information about students' academic work and daily lives. The intended output is a trained prediction model, accompanied by evidence of its performance and explanations of individual predictions.

The survey supplies the data for model development and evaluation. Its burnout questions provide the outcome the model learns to predict; the academic, lifestyle, psychological and technology questions provide candidate inputs. Separate questions about continuation intentions support an analysis of how predicted burnout relates to considering a break or leaving university.

## Problem Statement

University early-warning systems traditionally rely on administrative indicators such as:

- GPA
- attendance
- course completion
- academic records

However, many important burnout drivers are not captured by institutional data, including:

- perceived workload
- sleep quality
- academic stress
- self-efficacy
- lifestyle habits
- technology usage patterns
- Generative AI reliance

The study will develop candidate models, compare their predictions on held-out responses, and select a model based on predictive performance, stability and the usefulness of its explanations. Limited data availability shapes how the model will be built and evaluated.

---

# 2. Research Objectives

The project aims to:

1. Develop, train and evaluate a machine learning model to predict academic burnout risk from selected student characteristics and habits.

2. Compare candidate models and identify which inputs contribute most to their predictions.

3. Evaluate ML model reliability under small-sample conditions.

4. Produce an understandable explanation alongside each risk prediction, showing which inputs contributed to it.

5. Investigate the relationship between burnout risk and academic continuation intentions.

---

# 3. Research Questions

## Main Research Question

**How can explainable machine learning models be developed and validated to predict academic burnout risk among university students when available data is limited?**

---

## Secondary Questions

### RQ1:
Which machine learning algorithms provide the most reliable predictions in low-sample student datasets?

---

### RQ2:
Which academic, lifestyle, psychological, and technology-related factors contribute most to burnout risk?

---

### RQ3:
Does Generative AI reliance provide additional predictive value beyond traditional academic and lifestyle factors?

---

### RQ4:
Is predicted burnout risk associated with academic continuation intention?

---

# 4. Research Hypotheses

## H1 — Predictive Contribution of AI Usage

Generative AI reliance provides additional predictive information beyond traditional academic workload and lifestyle variables.

---

## H2 — Model Stability in Small Samples

Simpler, low-variance models (regularized logistic regression and explainable models) achieve more stable performance than highly complex models when sample size is limited.

---

## H3 — Explainability Stability

Feature importance rankings remain consistent across validation folds and augmentation strategies.

---

# 5. Data Collection Strategy

The survey is the data collection instrument for the prediction task. Collecting responses prepares the training and evaluation data; the research then uses those data to build and test the model.

## Population

University students.

## Expected Sample Size

Target:

\[
N = 50-150
\]

The study is designed specifically around limited sample availability.

---

## Instrument

A Google Form survey will collect candidate model inputs, burnout measures and separate continuation intentions.

Estimated completion time:

< 5 minutes

---

# 6. Survey Structure

## Section 1 — Academic Profile

Variables:

- Academic year
- Major category
- GPA range
- Course load

---

## Section 2 — Academic Habits and Pressure

Variables:

- Weekly study hours
- Perceived workload
- Academic overwhelm
- Procrastination
- Time management ability

---

## Section 3 — Technology and Lifestyle

Variables:

- Generative AI usage frequency
- AI dependency
- Sleep duration
- Sleep quality
- Screen time

---

## Section 4 — Psychological and Engagement Factors

Variables:

- Academic stress
- Motivation
- Academic belonging
- Self-efficacy

---

## Section 5 — Burnout Measurement (Primary Target)

Burnout indicators:

- Emotional exhaustion
- Academic overload
- Reduced motivation
- Difficulty keeping up with demands

A burnout score will be created:

\[
BurnoutScore =
Average(Burnout\ Items)
\]

Classification:

These categories will serve as the labels the model learns to predict. The burnout items used to calculate the label will stay out of the model inputs, so evaluation tests prediction from other student information.

Binary:

- 0 = Lower burnout risk
- 1 = Higher burnout risk

or:

- Low
- Medium
- High

---

## Section 6 — Academic Continuation Risk

Secondary outcomes:

- Dropout consideration
- Leave of absence consideration
- Continuation likelihood

These are not merged with burnout.

---

# 7. Data Processing Pipeline

## Data Cleaning

Steps:

- Remove incomplete responses
- Detect unrealistic completion times
- Handle missing values
- Encode categorical variables
- Normalize numerical features

---

# Feature Engineering

Because:

\[
N < 150
\]

feature count will be controlled.

Target:

\[
N/p \geq 10
\]

Possible engineered features:

## Workload-Sleep Strain Index

\[
\frac{Workload}{Sleep}
\]


## Digital Distraction Index

Combination of:

- Screen time
- AI dependency
- Procrastination


## Academic Stress Index

Combination of:

- Workload
- Stress
- Time management

---

# 8. Statistical Analysis

Before ML:

## Group Comparison

High burnout vs low burnout groups.

Tests:

### Mann-Whitney U Test

For:

- workload
- stress
- sleep
- AI reliance

---

### Fisher Exact Test

For categorical relationships:

Examples:

- GPA category vs burnout
- AI frequency vs burnout

---

### Logistic Regression Analysis

Purpose:

- Odds ratios
- Confidence intervals
- Baseline statistical model

---

# 9. Machine Learning Pipeline

The pipeline will produce a trained model that accepts the selected student inputs and returns a burnout risk prediction with an explanation. Candidate models will learn from training responses and predict labels for held-out responses during evaluation. Model comparison will determine which candidate to retain; no model has demonstrated reliable performance yet.

Workflow:

```
Survey Dataset
       |
       ↓
Data preprocessing
       |
       ↓
Feature selection
       |
       ↓
Repeated Stratified Cross Validation
       |
       ↓
Model Training
       |
       ↓
Performance Evaluation
       |
       ↓
Explainability Analysis
```

---

# 10. Candidate Models

## Baseline

### Logistic Regression

Regularized:

- Ridge
- LASSO


---

## Machine Learning Models

### Support Vector Machine

### Random Forest

Constraints:

- shallow depth
- limited complexity


### Gaussian Naive Bayes


### Explainable Boosting Machine (EBM)

Important because:

- interpretable
- suitable for tabular data

---

# 11. Small Sample Validation Strategy

Avoid:

- single train/test split

Use:

## Repeated Stratified K-Fold Cross Validation

Example:

5 folds × 20 repeats

---

## Bootstrap Confidence Intervals

Estimate:

- ROC-AUC
- PR-AUC
- Recall
- F1-score

---

# 12. Data Augmentation (Optional Experiment)

Only if dataset size/class imbalance requires it.

Methods:

- SMOTE
- CTGAN

Rules:

- Applied only inside training folds
- Never applied before splitting data

Purpose:

Evaluate whether augmentation improves stability.

---

# 13. Evaluation Metrics

Because burnout datasets may be imbalanced:

Primary metrics:

- PR-AUC
- ROC-AUC
- Recall
- F1-score

Avoid relying on:

- Accuracy only

---

# 14. Explainable AI (XAI)

Methods:

- SHAP
- Feature importance
- EBM explanations

Outputs:

Global:

"Which inputs contribute most to the model's burnout predictions?"

Individual:

"Why was this student classified as high risk?"

Illustrative output only, not a measured result or a diagnosis:

```
Prediction:
High burnout risk (82%)

Main contributors:
+ High workload
+ Poor sleep quality
+ High stress
- Strong academic belonging
```

---

# 15. Expected Contributions

## Prediction Model

A trained, evaluated machine learning model for academic burnout risk, with a documented input format and explanations of its predictions. Evaluation will establish how well it performs and where its predictions remain uncertain.

The target comes from reported burnout at the time of the survey. Predicting future burnout or actual dropout would require later outcome data; the current study examines continuation intentions separately.

## Methodological Contribution

A documented workflow for training, comparing and evaluating explainable models under limited data conditions, including the observed performance and uncertainty.

---

## Practical Contribution

A model and explanation format that academic advisers could use to guide conversations about support. Its practical usefulness remains a question for evaluation.

---

# 16. Current Status

Completed:

✅ Research direction  
✅ Research questions  
✅ Hypotheses  
✅ Survey design  
✅ Google Forms generation script  
✅ ML methodology plan  

Next steps:

The model still needs to be built and evaluated. Survey deployment and collection provide the data for that work.

1. Deploy survey
2. Collect responses
3. Export dataset
4. Perform EDA
5. Statistical testing
6. Train ML models
7. Compare performance
8. Select the final model and document its inputs, predictions and explanations
9. Report evaluation results and limitations in the research paper

---
