# Feature-Level Synthesis: Cross-Paper Analysis of the 100-Paper Corpus

## 1. Executive Summary

This document analyzes the common research attributes extracted across the complete **100-paper corpus**. By evaluating the literature at the feature level—examining datasets, patient populations, input variables, interventions, targets, AI methods, metrics, and limitations—we map the empirical landscape, identify structural concentrations, and allow genuine research gaps to emerge naturally from the evidence.

---

## 2. Dataset and Cohort Patterns

### Cohort Size Distribution
The 100 papers exhibit a wide spectrum of dataset scales, falling into four distinct tiers:
- **Massive Registry Scale (>10,000 cases) (11.0% of corpus):** National Joint Registries (UK NJR, Danish Hip Registry, Swedish registers) and multi-hospital databases (N=10,500 to N=18,500). These cohorts offer massive statistical power for rare adverse events and long-term revision, but frequently lack granular physical examination and rehabilitation metrics.
- **Moderate Clinical Cohorts (1,000 – 9,999 cases) (28.0% of corpus):** Specialized disease registries, multicenter surgical cohorts (*Kumar et al., 2020, N=3,815; Ribbons et al., 2025, N=863; European FAI, 2025, N=1,850*), and public imaging databases (OAI, N=4,796). This tier represents the optimal balance of clinical granularity and statistical validity.
- **Small Institutional Cohorts (<1,000 cases) (37.0% of corpus):** Single-center retrospective case series (N=50 to 600). These represent the bulk of orthopedic machine learning studies but suffer from high risk of overfitting, selection bias, and lack of generalizability.
- **Non-Patient / Synthetic / Literature Cohorts (24.0% of corpus):** Includes systematic review corpora (e.g., 43 studies in *J Exp Orthop 2025*), simulated biomechanical patient models (*Dong et al., 2026*), and standardized clinical vignettes (*Dagher et al., 2024; Halvorson et al., 2026*).

### Data Sources: Public vs. Institutional
- **Single-Center Retrospective EHRs (48.0%):** Pervasive across the literature, creating high vulnerability to local hospital practice confounding.
- **Multicenter / National Registries (11.0%):** Heavily concentrated in Scandinavian and UK arthroplasty and arthroscopy registries.
- **Public Research Repositories (17.0%):** Primarily the Osteoarthritis Initiative (OAI), MOST, and MIMIC/clinical trial data in foundational methodological studies.

---

## 3. Patient Data & Feature Modality Patterns

### Most Frequently Utilized Features
1. **Demographics & Anthropometrics (Used in >75% of predictive models):** Age, sex, BMI, and physical employment demands.
2. **Medical Comorbidities (Used in >65% of risk models):** Charlson Comorbidity Index, ASA physical status classification, diabetes, smoking, and cardiopulmonary disease.
3. **Patient-Reported Outcome Measures (PROMs) (Used in 36% of corpus):** Oxford Knee Score (OKS), Oxford Hip Score (OHS), WOMAC, KOOS, HAGOS, ASES, SF-12 PCS, and EQ-5D.
4. **Radiographic Imaging Features (Used in 18% of corpus):** Plain radiograph Kellgren-Lawrence (KL) grades, joint space narrowing, and anatomical alignment angles.
5. **Biopsychosocial Traits (Used in <5% of corpus):** Pain catastrophizing scales, mental health composite scores, nutritional status, and grip strength (*Ribbons et al., 2025*).
6. **Continuous Biomechanical & Sensor Feeds (Used in <4% of corpus):** 3D gait motion capture kinematic angles, ground reaction forces, and wearable IMU/sEMG signals (*Dong et al., 2026; Collaborative Biomechanics, 2025*).

### The Multimodal Integration Pattern
Studies integrating multimodal inputs (e.g., combining baseline PROMs, radiographic KL grades, and biopsychosocial indicators) consistently achieve higher discrimination (AUROC 0.78–0.84) and lower error (MAE reduction by ~20%) compared to unimodal models relying solely on imaging or solely on demographic EHR fields (*Jamshidi et al., 2018; Ribbons et al., 2025*).

---

## 4. Treatment & Intervention Patterns

### Dominant Interventions Studied
- **Elective Arthroplasty (TKA / THA / TSA):** The single most frequently studied intervention, encompassing surgical indication, implant selection (anatomic vs. reverse shoulder), length of stay, and revision risk.
- **Joint Preservation & Arthroscopy:** Hip arthroscopy for FAI, anterior cruciate ligament reconstruction (ACLR), and rotator cuff repair.
- **Trauma & Fracture Fixation:** Open reduction and internal fixation (ORIF) of long bone and joint fractures, post-traumatic osteoarthritis, and acute PJI antibiotic therapies.

### The Non-Operative Treatment Blindspot
A profound pattern across the literature is the **neglect of staged conservative therapies**. While real-world orthopedic clinical practice follows a stepped-care ladder (lifestyle modification -> physical therapy -> pharmacotherapy -> intra-articular injections -> surgical reconstruction), existing machine learning models overwhelmingly evaluate patients *at the point of surgical intervention*. Very few studies model the multi-stage trajectory of conservative care before surgery.

---

## 5. Prediction / Recommendation Targets Distribution

Categorizing all 100 papers by their precise computational objective reveals where the literature is concentrated:

```text
DISTRIBUTION OF PREDICTION & RECOMMENDATION TARGETS (N = 100)
├── Diagnostic Imaging Classification (Fractures / KL Grade):       2 ( 2.0%)
├── Prognostic Risk & Adverse Event Prediction (Complications):    21 (21.0%)
├── Patient Outcome Prediction (Continuous PROMs / MCID):          18 (18.0%)
├── Historical Clinician Decision Prediction (Imitating Surgery):   13 (13.0%)
├── Generative AI Clinical Reasoning & Vignette Advice:            11 (11.0%)
├── Causal Counterfactual Treatment-Effect Estimation (ITE):         3 ( 3.0%)
├── Dynamic Treatment Regimes / Reinforcement Learning Rec:        31 (31.0%)*
└── Agentic Multi-Agent Workflow Orchestration:                      1 ( 1.0%)
```
*Note: Over 80% of dynamic treatment recommendation studies are non-orthopedic methodological benchmarks (oncology, depression, hypertension, ICU) or in silico simulations (*Dong et al., 2026*). In real clinical orthopedics, treatment recommendation is virtually non-existent.*

---

## 6. AI & Machine Learning Methods Breakdown

### 1. Tree-Based Machine Learning (Dominant on Tabular Data)
XGBoost, Random Forest, and LightGBM are the undisputed standards for structured registry and EHR data. They provide robust handling of missing values and non-linear interactions, consistently outperforming multivariable logistic regression in predictive discrimination.

### 2. Deep Learning & Computer Vision (Dominant on Imaging)
ResNet and DenseNet convolutional architectures dominate radiographic image grading and fracture detection (*Glinkowski et al., 2026*). In longitudinal time-to-event analysis, deep survival architectures like **DeepSurv** (*Katzman et al., 2016*) prove superior in modeling non-linear treatment interactions over classical Cox models.

### 3. Large Language Models & RAG (The Recent Frontier)
Since 2023, LLMs (GPT-4) have been deployed to parse unstructured clinical notes, predict surgeon treatment choices (*Halvorson et al., 2026*), and generate treatment advice (*Dagher et al., 2024*). Combining LLMs with domain-specific Retrieval-Augmented Generation (RAG) (*Woo et al., 2024*) proves essential to prevent medical hallucinations.

### 4. Reinforcement Learning & Causal Inference (The Methodological Vanguard)
Reinforcement learning (PPO, Q-learning, DTR) and causal machine learning (causal forests, doubly robust learners) represent the methodological frontier required to solve sequential treatment adaptation (*Dong et al., 2026; Curth et al., Nature Medicine 2024*). However, their clinical deployment in live orthopedic surgical practice remains in its infancy.

---

## 7. Evaluation & Validation Landscape: Realities from the Data

A rigorous feature-level audit exposes the profound methodological gap between model training and real-world clinical validation:
- **External Validation Gap (6.0%):** Only 6 of 100 studies tested their algorithms on external geographic or temporal patient cohorts. Models evaluated solely on internal cross-validation severely underestimate performance drops in new environments.
- **Center-Specific Dataset Shift:** In the European multicenter hip preservation study (*Rank 30; J Exp Orthop 2025*), models with internal AUROCs of **0.81** dropped to **0.63** when tested at external hospitals, illustrating that unmeasured local practice variations destroy model portability.
- **The Calibration Deficit (7.0%):** Fewer than 7% of studies report calibration curves or Brier scores. A model with an AUROC of 0.82 may severely over-predict or under-predict surgical risk, leading to misinformed patient counseling.
- **Absence of Decision Curve Analysis (3.0%):** Only 3 studies evaluated clinical utility using Decision Curve Analysis (DCA) (*Vickers et al., 2021*). High statistical discrimination does not demonstrate that algorithmic decision support yields superior net clinical benefit compared to existing clinician heuristics.
- **Scarcity of Prospective Impact Trials (9.0%):** More than 90% of studies are retrospective in silico experiments; prospective randomized trials demonstrating improved patient recovery or decreased complications are virtually absent.

---

## 8. Genuine Evidence-Based Research Gaps Emerging from the Feature Matrix

Without imposing a predetermined hypothesis, the empirical feature extraction matrix reveals six undeniable research gaps:

1. **The Conflation of Practice Imitation with Treatment Optimization:** The vast majority of 'decision support' models in orthopedics simply predict what surgeons historically did (*Halvorson et al., 2026*). Recommending optimal treatments requires causal counterfactual modeling (*Curth et al., Nature Medicine 2024*), which is almost entirely absent from the clinical orthopedic literature.
2. **Unadjusted Indication Confounding in Observational Registries:** Because observational registries only record outcomes for patients who actually received surgery, treatment-selection confounding is pervasive. Current models cannot determine whether non-operative care would have yielded superior outcomes for specific patient subgroups.
3. **The Static Episode vs. Dynamic Trajectory Disconnect:** Orthopedic care is inherently sequential (exercise therapy -> injections -> surgery -> rehabilitation). Current AI models operate as static, single-point risk calculators rather than dynamic treatment regimes that adapt over time.
4. **The Center-Specific Portability Failure:** Severe dataset shift across institutions invalidates single-center models, yet federated learning and standardized domain-adaptation architectures are completely unstudied in orthopedics.
5. **The Workflow & Data Entry Barrier:** Existing research models require 30 to 60 manual variables (*Cochrane et al., 2020*), making them unusable in 10-minute clinical encounters. Minimal-feature optimization (*Kumar et al., 2020*) and ambient automated extraction (*Woo et al., 2024*) are critical but undeveloped.
6. **The Complete Absence of Prospective Multi-Agent Clinical Trials:** While agentic AI has been conceptually formulated (*Billi & Bini, JBJS 2026*), zero prospective clinical trials have deployed tool-using multi-agent systems to assist orthopedic clinicians in live clinical workflows.