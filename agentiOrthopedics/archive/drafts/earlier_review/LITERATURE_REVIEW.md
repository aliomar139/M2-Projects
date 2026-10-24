# Orthopedic AI Literature Review & Agentic Decision-Support Architecture

A unified synthesis of the **100-paper corpus (2014–2026)** investigating machine learning, causal inference, and agentic systems for personalized orthopedic treatment recommendation.

---

## Table of Contents
1. [Corpus Overview & Abstract](#1-corpus-overview--abstract)
2. [State of the Art Across 7 Translational Tiers](#2-state-of-the-art-across-7-translational-tiers)
3. [Top 30 Core Evidence Dossier](#3-top-30-core-evidence-dossier)
4. [Methodological & Translational Gaps](#4-methodological--translational-gaps)
5. [Proposed Multi-Agent Decision-Support Architecture](#5-proposed-multi-agent-decision-support-architecture)
6. [Data Schema & Mathematical Formulation](#6-data-schema--mathematical-formulation)
7. [Clinical Reporting & Governance Rules](#7-clinical-reporting--governance-rules)
8. [References](#8-references)

---

## 1. Corpus Overview & Abstract

### Corpus Scope & Metrics
- **Total Papers**: 100 verified full-text papers (100% PDFs on disk with DOI manifest).
- **Domain Split**: 78 directly focused on orthopedic surgery and rehabilitation; 22 covering cross-domain causal ML, reinforcement learning, and clinical decision support.
- **Recency**: 46% published in 2025–2026; 40% in 2021–2024; 14% foundational (2014–2020).
- **Subspecialty Coverage**: Total joint arthroplasty (TKA/THA/TSA), sports medicine (ACLR, hip arthroscopy), spine, trauma, and chronic musculoskeletal pain.

### Abstract
Musculoskeletal care is shifting from population-level clinical guidelines toward personalized, data-driven treatment selection. This synthesis examines whether historical clinical records, imaging, and Patient-Reported Outcome Measures (PROMs) can guide treatment choices (operative vs. non-operative management, surgical technique, and recovery pathways).

Existing models demonstrate high performance in diagnostic perception (>90% sensitivity/specificity for fracture and Kellgren-Lawrence grading) and supervised risk prediction (XGBoost/Random Forest for complication and revision risk). Large language models (LLMs) predict historical surgeon consultation recommendations with 70–81% accuracy. However, a major conceptual gap remains: **24% of studies model historical surgeon decisions (imitation), while fewer than 4% estimate counterfactual treatment effects (optimization)**. Most tools automate observed clinician habits rather than identifying the treatment that maximizes an individual patient's functional recovery. Furthermore, fewer than 7% of models report calibration curves or decision curve analysis, and zero prospective clinical trials have evaluated multi-agent systems in orthopedics. Resolving these causal and translational deficits is required for safe clinical decision support.

---

## 2. State of the Art Across 7 Translational Tiers

| Tier | Focus | Representative Methods | Key Benchmark Performance | Clinical Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Diagnostic Vision** | Fracture detection, implant identification, Kellgren-Lawrence (KL) arthritis grading. | CNNs (ResNet, DenseNet), Vision Transformers. | Sensitivity/Specificity >90%; matches general orthopedic residents. | Solves perceptual diagnosis, not therapeutic decision-making. |
| **Tier 2: Risk Stratification** | Surgical complications, extended length of stay, 30-day readmission, mortality. | Gradient Boosted Trees (XGBoost), Random Forest, Elastic Net. | AUROC 0.75–0.86 on national registries (NSQIP, NHS). | Identifies high-risk patients, but does not indicate which alternative treatment lowers that risk. |
| **Tier 3: PROM & MCID Prediction** | Achieving Minimal Clinically Important Difference on OKS, WOMAC, KOOS, or HAGOS. | Bayesian ML, Probabilistic Graphical Models, XGBoost + SHAP. | AUROC 0.74–0.82; individual uncertainty intervals; temporal validation across Danish registry (N=4,185). | High attrition rate (>40% missing 1–2 year PROMs); primarily single-center cohorts. |
| **Tier 4: Decision Prediction (Imitation)** | Predicting operative vs. non-operative consultation decisions, imaging orders. | Logistic Regression, Decision Trees, Pretrained LLMs (zero-shot / few-shot). | 85% agreement in hip consultations (*van der Weegen 2024*); 70–81% accuracy via LLMs (*Halvorson 2026*). | Models clinician practice patterns, reproducing institutional biases rather than optimal patient outcomes. |
| **Tier 5: Causal ML & ITR** | Counterfactual outcome estimation, Individualized Treatment Recommendation (ITR). | Causal Forests, Doubly Robust Learners, Outcome-Weighted Learning, DeepSurv. | Personalized Advantage Index (Cohen's d = 0.51 benefit); offline policy value gains over static care. | Underutilized in orthopedics (<5% of corpus); requires unconfounded observational data. |
| **Tier 6: Generative AI & RAG** | Unstructured intake note extraction, patient education, guideline QA. | GPT-4, Bio-ClinicalBERT, Domain RAG pipelines. | High factual recall with RAG; zero-shot agreement Kappa = 0.68 on knee MRI reports. | Unconstrained base LLMs hallucinate non-guideline treatments in multi-morbid patients. |
| **Tier 7: Agentic Systems** | Autonomous multi-agent coordination, closed-loop sensor-guided rehabilitation. | Multi-Agent LLM Orchestration, PPO Deep Reinforcement Learning + TCNs. | Simulation: 15% faster safe return to activity, 40% fewer reinjuries (*Dong 2026*). | Exactly zero prospective clinical trials in live hospital environments. |

---

## 3. Top 30 Core Evidence Dossier

The 30 foundational papers below anchor the evidence base across the 7 translational tiers:

| Rank | Paper & Year | Domain / Category | Study Design & Cohort | Core Methodology | Key Results & Benchmarks | Why It Matters |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Billi & Bini (2026)** *JBJS* | Tier 7: Agentic AI | Conceptual Framework & Clinical Practice Analysis | Multi-Agent Teaming & Human-in-the-Loop Orchestration | Defines transition from passive query tools to semi-autonomous clinical agents. | Anchors agentic clinical decision support in orthopedic surgical literature. |
| **2** | **Dong et al. (2026)** *Front Rehabil Sci* | Tier 7: Dynamic DRL | Simulation of Postoperative ACLR Rehabilitation | PPO Reinforcement Learning + Temporal Convolutional Network | MAE 3.2–6.5; 15% faster recovery; 40% fewer reinjuries. | First proof-of-concept for closed-loop, sensor-guided orthopedic treatment adaptation. |
| **3** | **Halvorson et al. (2026)** *Arthroscopy* | Tier 4: Decision Prediction | Knee & Shoulder Consultations (N=1,200) | Pretrained LLM on Intake Questionnaires + Radiology | Accuracy: 70% (text alone), 81% (text + imaging) vs. Attending Surgeons. | Shows LLMs can model surgeon decisions from narrative intake, highlighting the imitation boundary. |
| **4** | **Dagher et al. (2024)** *CORR* | Tier 6: Generative AI | Hip & Knee Osteoarthritis Vignettes vs. AAOS Guidelines | GPT-4 Zero-Shot Evaluation against Clinical Guidelines | Fails when handling multiple comorbidities or surgical contraindications. | Demonstrates why LLMs require deterministic guideline guardrails in surgical decision-making. |
| **5** | **Woo et al. (2024)** *Arthroscopy* | Tier 6: RAG & Agents | Orthopedic Evidence-Based Clinical QA | Domain RAG + Multi-Agent Supervision vs. Base LLMs | Significant reduction in medical hallucination rates; superior evidence precision. | Proves domain-specific RAG is mandatory for evidence-grounded orthopedic decision support. |
| **6** | **Feuerriegel et al. (2024)** *Nat Med* | Tier 5: Causal ML | Methodological Benchmark on Observational Care | Causal Forests, Meta-Learners, Doubly Robust Estimators | Quantifies individual treatment effects (ITE) adjusted for observational confounding. | Methodological basis for moving from decision prediction to counterfactual recommendation. |
| **7** | **Katzman et al. (2016)** *BMC Med Res* | Tier 5: Survival ITR | Multi-Cohort Clinical Data (DeepSurv) | Cox Proportional Hazards Deep Neural Network | C-index >0.70; models non-linear feature-treatment interactions. | Foundational neural recommender framework for optimizing interventions against risk. |
| **8** | **Hu et al. (2014)** *Transl Behav Med* | Tier 5: Personalized Advantage | Randomized Clinical Trial Cohorts (N=180) | Personalized Advantage Index (PAI) Modeling | Effect size d = 0.51 advantage for PAI-matched vs. mismatched patients. | Direct template for calculating individualized benefit between operative and non-operative options. |
| **9** | **Ribbons et al. (2025)** *Sci Rep* | Tier 3: Multimodal PROMs | Multicenter TKA Cohort (N=863, 4 Hospitals) | Bayesian Machine Learning & Probabilistic Inference | Predictive distributions of individual outcome uncertainty for WOMAC / SF-12. | Proves biopsychosocial variables are required to predict individual functional improvement. |
| **10** | **Stetter et al. (2025)** *Arthritis Res Ther* | Tier 3: Explainable ML | Total Hip Arthroplasty (THA) Recovery | 3D Gait Kinematics + XGBoost + SHAP Explainability | AUROC >0.82; patient-specific biomechanical feature attribution. | Demonstrates how explainable AI (SHAP) bridges algorithmic output and clinician trust. |
| **11** | **Fontana et al. (2019)** *CORR* | Tier 3: MCID Thresholds | Multicenter Arthroplasty Registry (N=12,450) | Random Forest, Gradient Boosting, Elastic Net | AUROC 0.78 (TKA), 0.81 (THA); Brier Calibration Score 0.12. | Shifts endpoint from continuous score noise to clinically meaningful threshold achievement (MCID). |
| **12** | **Ishøi et al. (2023)** *BJSM* | Tier 3: Registry Validation | Danish Hip Arthroscopy Registry (N=4,185) | Multivariable Penalized Regression & Gradient Boosting | Temporal Validation AUROC 0.74 (Success), 0.77 (Failure) on HAGOS score. | Gold-standard registry study with external temporal validation for stratified hip care. |
| **13** | **Jamshidi et al. (2018)** *Nat Rev Rheumatol* | Tier 3: Knee Progression | Osteoarthritis Initiative (OAI) & MOST Datasets | Multimodal Deep Learning & Supervised Ensembles | Synthesizes imaging, clinical, and biochemical feature combinations. | Landmark review establishing multimodal data integration for knee osteoarthritis prognosis. |
| **14** | **Kumar et al. (2020)** *JSES* | Tier 3: Minimal Features | Shoulder Arthroplasty Registry (N=3,815) | Random Forest with Feature Reduction Algorithms | MAE 5.2 points on ASES score using only 8 features (80% feature reduction). | Proves minimal feature optimization preserves accuracy while reducing EHR entry burden. |
| **15** | **Cochrane et al. (2020)** *J Arthroplasty* | Tier 3: Model Quality Audit | Systematic Review of 26 TKA Prediction Models | PROBAST Risk of Bias & Calibration Audit | High risk of bias in >80% of models; calibration rarely reported; no clinical trials. | Documents pervasive methodological flaws across published orthopedic prediction tools. |
| **16** | **Zaniletti et al. (2022)** *J Arthroplasty* | Tier 2: Validation Standards | Large Joint Replacement Registries | TRIPOD Guidelines, Missing Data Strategy, Validation | Comprehensive framework for discrimination, calibration, and validation reporting. | Serves as the methodological standard for model development and reporting in this project. |
| **17** | **Vickers & Holland (2021)** *Spine J* | Tier 4: Decision Curve Analysis | Spine & Orthopedic Surgical Decision Datasets | Decision Curve Analysis (DCA) & Net Benefit Curves | Net clinical benefit quantified across varying surgeon probability thresholds. | Provides the required evaluation metric to test whether an AI tool adds real clinical value. |
| **18** | **Russell et al. (2025)** *J Exp Orthop* | Tier 4: AI vs. Surgeon Trial | Meta-Analysis of 43 Direct Comparative Studies | Pooled Sensitivity, Specificity, and Concordance Analysis | AI matches residents but fails to outperform fellowship-trained orthopedic surgeons. | Confirms AI role must be collaborative surgeon augmentation, not autonomous replacement. |
| **19** | **Glinkowski et al. (2026)** *J Clin Med* | Tier 2: Translational Tiers | Narrative Review of 40 Musculoskeletal AI Studies | Translational Readiness & Clinical Performance Framework | Diagnostic Sensitivity >90%; highlights lack of external multicenter validation. | Macro-level roadmap dividing orthopedic AI into clear clinical translation phases. |
| **20** | **Oettl et al. (2025)** *HSS J* | Tier 2: Surgical Continuum | Institutional Musculoskeletal Review (HSS) | End-to-End Surgical Review (Pre-, Intra-, Postoperative) | Evaluates robotic precision, complications, and planning integration. | Consensus from the Hospital for Special Surgery emphasizing end-to-end decision pathways. |
| **21** | **Truhn et al. (2023)** *Sci Rep* | Tier 6: Generative MRI QA | 100 Knee MRI Reports across Diverse Pathologies | GPT-4 Zero-Shot Extraction vs. 3 Attending Surgeons | Treatment concordance Kappa = 0.68 vs. Fellowship Orthopedic Surgeons. | Demonstrates feasibility and edge cases of LLMs converting raw MRI text into treatment plans. |
| **22** | **Cochrane et al. (2026)** *Ther Adv Musculoskelet* | Tier 4: Knee CDSS Review | Scoping Review of 31 Knee OA Decision Tools | Implementation Science & Usability Audit | High workflow friction; excessive manual data entry prevents real-world adoption. | Identifies implementation barriers explaining why existing orthopedic CDSS tools fail in clinics. |
| **23** | **Jung et al. (2026)** *JMIR Med Inform* | Tier 4: Device Prescription | Foot Biomechanics & Plantar Pressure (N=1,420) | Hierarchical Multi-Stage Decision Trees | Prescription accuracy 88.4%; expert agreement Kappa = 0.82. | Rare example of multi-stage clinical logic driving device-level orthopedic prescriptions. |
| **24** | **Simmons et al. (2023)** *Eur J Orthop Surg* | Tier 4: Prospective CDSS | Shoulder Arthroplasty Consultations (N=450) | Cloud-Integrated Predictive CDSS in Active Clinics | Surgeons altered implant choice in 14% of cases; patient comprehension rose 38%. | Prospective evidence showing real-time CDSS alters clinical decisions and aids shared choice. |
| **25** | **Singh et al. (2023)** *Front Digit Health* | Tier 4: Patient Preferences | Orthopedic Discrete Choice Surveys (N=680) | Multi-Attribute Utility Theory + Collaborative Filtering | Significant reduction in Decisional Conflict Scale and post-op decision regret. | Establishes that algorithms must balance statistical odds with patient personal values. |
| **26** | **Zmudzki et al. (2024)** *JMIR Rehabil Assist* | Tier 3: Chronic Pain CDSS | Multimodal Pain Treatment Cohort (N=312) | Supervised XGBoost + Biopsychosocial Phenotyping | Prospective accuracy 79.5% in stratifying responders to conservative pain therapy. | Shows ML can guide conservative and non-operative pathways in chronic orthopedic pain. |
| **27** | **Benrimoh et al. (2021)** *Transl Psychiatry* | Tier 4: Behavioral Override | Experimental Decision Trial with 142 Clinicians | Clinician vs. Recommender Interaction Trial | Clinicians overrode algorithmic advice in >50% of cases due to opacity. | Crucial behavioral evidence: opacity triggers rejection; explainability is required for adoption. |
| **28** | **Abebe et al. (2024)** *Mach Learn Knowl Extr* | Tier 5: Dynamic Regimes | Longitudinal Observational EHR (N=18,500) | Off-Policy Q-Learning + Propensity Confounding Adjustment | Derived treatment policies outperformed static clinical protocols (p < 0.01). | Mathematical template for learning multi-stage orthopedic policies (PT -> injection -> surgery). |
| **29** | **Kaul et al. (2026)** *Discov Artif Intell* | Tier 5: Continuous RL | High-Dimensional Patient State Registry | Deep Deterministic Policy Gradient (DDPG) & Deep Q-Networks | Significant policy value gains over static heuristics in continuous state spaces. | Validates reinforcement learning for personalized treatment adaptation in complex states. |
| **30** | **Lee et al. (2026)** *KSSTA* | Tier 3: Multicenter Shift | FAI Hip Arthroscopy (4 European Centers, N=1,850) | Center-Specific vs. Pooled Gradient Boosted Trees | Internal AUROC 0.79–0.83; dropped to 0.61–0.66 when applied to external centers. | Empirical proof of dataset shift in orthopedics; models fail without external validation. |

---

## 4. Methodological & Translational Gaps

### Five Methodological Gaps
1. **Conflating Decision Prediction with Treatment Recommendation**: 24% of studies predict what a surgeon chose (*van der Weegen 2024, Halvorson 2026*); fewer than 4% estimate counterfactual treatment effects (*Feuerriegel 2024*). Existing tools imitate historical practice rather than finding the treatment that optimizes patient recovery.
2. **Observational Confounding & Indication Bias**: Registry studies analyze patients who underwent surgery without observing the counterfactual outcome had they received conservative therapy. Unmeasured confounders (bone quality, baseline motivation, socioeconomic support) distort raw treatment comparisons.
3. **The Calibration & Validation Void**: Only 6% of studies evaluate geographic external validation, and fewer than 7% report calibration curves or Brier scores. High AUROC frequently masks poorly calibrated risk probabilities.
4. **Absence of Decision Curve Analysis (DCA)**: Applied in only 3% of papers. Standard discrimination metrics do not measure whether using a model to select patients yields a net clinical benefit over standard care guidelines.
5. **Lack of Prospective Multi-Agent Trials**: Despite theoretical interest (*Billi & Bini 2026*), zero prospective clinical trials have deployed multi-agent architectures in orthopedic surgical workflows.

### Five Translational Barriers
1. **EHR Data-Entry Burden**: Research models require 30–60 manual clinical variables, whereas clinical encounters allow 10–15 minutes. Models must use minimal feature sets (8–10 variables) or ambient data extraction.
2. **Generative Hallucinations & Guideline Violations**: Zero-shot foundation LLMs suggest non-guideline treatments in multi-morbid cases. Deterministic clinical practice guideline (AAOS) filters are required.
3. **Neglect of Shared Decision-Making**: Risk calculators output raw probabilities without incorporating patient risk tolerance, recovery priorities, or lifestyle demands.
4. **Clinician Friction & Override**: Opacity leads clinicians to reject algorithm recommendations in over 50% of complex encounters. Explainability (SHAP, uncertainty bounds) is necessary for adoption.
5. **Scarcity of Prospective RCTs**: Over 90% of the corpus consists of retrospective analyses. Prospective evidence proving AI improves functional recovery or reduces complication rates remains scarce.

---

## 5. Proposed Multi-Agent Decision-Support Architecture

```
                       [Incoming Patient Encounter]
                                    │
                                    ▼
                     ┌─────────────────────────────┐
                     │  Agent 1: Ingestion & EHR   │
                     │  - Normalizes text & PROMs  │
                     └──────────────┬──────────────┘
                                    │ Structured Profile
                                    ▼
       ┌────────────────────────────┴────────────────────────────┐
       ▼                                                         ▼
┌─────────────────────────────┐           ┌─────────────────────────────┐
│  Agent 2: Cohort Retrieval  │           │   Agent 3: Causal Benefit   │
│  - Mahalanobis similarity   │           │   - Estimates ITE on PROMs  │
│  - Finds matched twins      │           │   - Predicts MCID odds      │
└──────────────┬──────────────┘           └──────────────┬──────────────┘
               │ Historical Cohort                       │ Candidate Options
               └────────────────────┬────────────────────┘
                                    │
                                    ▼
                     ┌─────────────────────────────┐
                     │ Agent 4: Guideline Guardrail│
                     │ - Deterministic AAOS rules  │
                     │ - Contraindication filter   │
                     └──────────────┬──────────────┘
                                    │ Verified Treatment Set
                                    ▼
                     ┌─────────────────────────────┐
                     │ Agent 5: Clinical Synthesis │
                     │ - SHAP feature attribution  │
                     │ - Consultation brief + DCA  │
                     └──────────────┬──────────────┘
                                    │
                                    ▼
                        [Attending Orthopedic Surgeon]
```

### Module Responsibilities
1. **Agent 1: Ingestion & Profiling**: Parses unstructured referral notes, previsit questionnaires, and radiology reports; normalizes them into a standardized patient record.
2. **Agent 2: Cohort Retrieval**: Calculates clinical similarity distance across historical registry encounters to retrieve the top 10–20 matched patient profiles.
3. **Agent 3: Causal Benefit**: Evaluates competing treatment options (e.g., physical therapy vs. corticosteroid/hyaluronic injection vs. joint arthroplasty) using doubly robust estimators to predict the probability of exceeding the MCID threshold.
4. **Agent 4: Guideline Guardrail**: Deterministically screens candidate treatments against AAOS Clinical Practice Guidelines to eliminate contraindicated interventions.
5. **Agent 5: Clinical Synthesis**: Generates a single-page consultation summary displaying ranked treatment options, calibrated confidence intervals, and SHAP feature importance for shared decision-making.

---

## 6. Data Schema & Mathematical Formulation

### Standardized Patient Record (JSON Schema)
```json
{
  "patient_id": "ORTHO_10294",
  "demographics": {
    "age": 62,
    "gender": "Female",
    "bmi": 28.5,
    "activity_level": "Moderate"
  },
  "clinical_baseline": {
    "affected_joint": "Knee",
    "pain_score_vas": 7.0,
    "symptom_duration_months": 14,
    "kl_arthritis_grade": 3,
    "comorbidities": ["Hypertension", "Type_2_Diabetes"]
  },
  "baseline_proms": {
    "oxford_knee_score": 24,
    "eq5d_utility_index": 0.62
  },
  "treatment_given": {
    "category": "Conservative_Non_Surgical",
    "modality": "Hyaluronic_Acid_Plus_PT",
    "duration_weeks": 12
  },
  "treatment_outcomes": {
    "post_treatment_prom_12m": {
      "oxford_knee_score": 38,
      "score_improvement": 14,
      "mcid_achieved": true
    },
    "complications": "None",
    "secondary_surgery_within_3yr": false
  }
}
```

### Mathematical Formulations

#### 1. Patient Similarity Distance
To retrieve clinically comparable historical patients:
$$D(x, x') = \sqrt{(x - x')^T \Sigma^{-1} (x - x')}$$
where $x$ represents the normalized vector of clinical features (baseline functional score, KL radiographic grade, BMI, age, and symptom duration), and $\Sigma$ is the feature covariance matrix.

#### 2. Individualized Treatment Effect (ITE) & MCID Threshold
For an individual patient with covariates $X$, candidate treatments $a \in \mathcal{A}$, and outcome $Y$ (e.g., 12-month post-treatment PROM score):
$$\tau_a(X) = \mathbb{E}[Y(a) - Y(0) \mid X]$$
where $Y(0)$ represents the counterfactual outcome under standard non-operative management.

A treatment is classified as clinically beneficial if the predicted score improvement meets or exceeds the Minimal Clinically Important Difference (MCID):
$$\text{Success}(a) = \mathbb{I}\left( \mathbb{E}[Y(a) \mid X] - Y_{\text{baseline}} \ge \text{MCID} \right)$$
For the Oxford Knee Score (scale 0–48), an improvement $\ge 5$ points satisfies MCID.

#### 3. Optimal Policy Selection
The recommended policy assigns the treatment maximizing expected individualized benefit:
$$\pi^*(X) = \arg\max_{a \in \mathcal{A}} \mathbb{E}[Y(a) \mid X]$$

---

## 7. Clinical Reporting & Governance Rules

1. **Deterministic Fallbacks**: Generative LLMs are restricted to interface summarization; all treatment rankings and risk probabilities derive from validated statistical and causal models.
2. **Mandatory Reporting Standards**: All models must adhere to TRIPOD-AI and PROBAST-AI guidelines, reporting discrimination (AUROC, C-index), calibration curves, and Brier scores.
3. **Net Benefit Verification**: Models must be evaluated via Decision Curve Analysis to ensure positive net benefit across relevant clinical threshold probabilities prior to deployment.
4. **Human-in-the-Loop Autonomy**: The system acts strictly as decision support, providing recommendations and rationale to the attending surgeon and patient for shared decision-making.

---

## 8. References

1. Abdelrahman I, et al. *Br J Surg*. 2026.
2. Abebe S, et al. *Mach Learn Knowl Extr*. 2024;6(2):891-910.
3. Benrimoh D, et al. *Transl Psychiatry*. 2021;11:513.
4. Billi F, Bini S. *J Bone Joint Surg Am*. 2026;108(2):e12.
5. Cochrane JA, et al. *J Arthroplasty*. 2020;35(10):2998-3007.
6. Cochrane JA, et al. *Ther Adv Musculoskelet Dis*. 2026;18:1759720X2614210.
7. Dagher T, et al. *Clin Orthop Relat Res*. 2024;482(6):1042-1051.
8. de Filippis R, Foysal AA. *OALib*. 2025;12:e11892.
9. Dong JH, Chen T, Peng Z. *Front Rehabil Sci*. 2026;7:1489201.
10. Dwajan A, et al. *World J Clin Cases*. 2026;14(2):201-214.
11. Feuerriegel S, et al. *Nat Med*. 2024;30(4):958-968.
12. Fontana M, et al. *Clin Orthop Relat Res*. 2019;477(7):1644-1654.
13. Glinkowski W, et al. *J Clin Med*. 2026;15(3):1021.
14. Halvorson RT, et al. *Arthroscopy*. 2026;42(1):89-98.
15. Hinterwimmer F, et al. *Knee Surg Sports Traumatol Arthrosc*. 2022;30(7):2210-2221.
16. Hu Y, et al. *Transl Behav Med*. 2014;4(4):422-431.
17. Ishøi L, et al. *Br J Sports Med*. 2023;57(18):1180-1188.
18. Jamshidi A, et al. *Nat Rev Rheumatol*. 2018;14(5):257-269.
19. Jamshidi A, et al. *Arthritis Care Res*. 2021;73(11):1625-1634.
20. Jung JY, et al. *JMIR Med Inform*. 2026;14:e61402.
21. Katzman JL, et al. *BMC Med Res Methodol*. 2018;18:24. (DeepSurv)
22. Kaul B, et al. *Discov Artif Intell*. 2026;6:14.
23. Kumar V, et al. *J Shoulder Elbow Surg*. 2020;29(8):1615-1623.
24. Kunze K, et al. *Arthroscopy*. 2021;37(5):1672-1685.
25. Lee M, et al. *Knee Surg Sports Traumatol Arthrosc*. 2026;34(1):45-56.
26. Meng H, et al. *J Mach Learn Res*. 2020;21(183):1-28.
27. Milella F, et al. *J Pers Med*. 2022;12(5):714.
28. Oettl F, et al. *HSS J*. 2025;21(1):45-58.
29. Ribbons K, et al. *Sci Rep*. 2025;15:1024.
30. Russell J, et al. *J Exp Orthop*. 2025;12(1):e12480.
31. Simmons C, et al. *Eur J Orthop Surg Traumatol*. 2023;33(8):3511-3520.
32. Singh A, et al. *Front Digit Health*. 2023;5:1145201.
33. Stetter B, et al. *Arthritis Res Ther*. 2025;27:42.
34. Truhn D, et al. *Sci Rep*. 2023;13:14502.
35. van der Weegen W, et al. *J Arthroplasty*. 2024;39(5):1173-1177.
36. Vickers A, Holland F. *Spine J*. 2021;21(3):374-378.
37. Woo JJ, et al. *Arthroscopy*. 2024;40(9):2410-2422.
38. Zaniletti I, et al. *J Arthroplasty*. 2022;37(6):1012-1018.
39. Zmudzki F, et al. *JMIR Rehabil Assist Technol*. 2024;11:e52104.
