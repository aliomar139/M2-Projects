# Agentic AI in Orthopedic Treatment Recommendation: Literature Review & System Architecture

## Summary

This document synthesizes findings from the **100-paper orthopedic AI corpus** and outlines a modular multi-agent clinical decision-support architecture. The system assists clinicians during consultation by matching incoming patients to historical cohorts, estimating individualized treatment effects across conservative and surgical pathways, verifying safety against clinical guidelines, and generating explainable summaries with uncertainty estimates.

---

## 1. Literature Evidence Synthesis

### Clinical & Diagnostic Data Inputs
- **Demographics & Risk Factors**: Age, sex, BMI, occupational physical demand, comorbidities (*Ogink et al., 2021; Abdelrahman et al., 2026*).
- **Baseline Clinical Metrics**: Visual Analog Scale (VAS) pain score, symptom duration, range of motion, prior non-operative therapies (*van der Weegen et al., 2024; Cochrane et al., 2026*).
- **Patient-Reported Outcome Measures (PROMs)**: Oxford Knee Score (OKS), Oxford Hip Score (OHS), KOOS, WOMAC, EQ-5D utility index (*Kunze et al., 2021; Abdelrahman et al., 2026*).
- **Imaging & Morphology**: Kellgren-Lawrence (KL) radiographic arthritis grade, joint space narrowing, cartilage degradation on MRI (*Jamshidi et al., 2018; Hinterwimmer et al., 2022*).
- **Primary Public Datasets**: Osteoarthritis Initiative (OAI), Danish Hip Arthroscopy Registry, UK NHS PROMs registry.

### Core Machine Learning Methods
- **Supervised Ensembles (XGBoost, Random Forest)**: Standard benchmark for complication risk, readmission, and operative triage (*van der Weegen et al., 2024; Milella et al., 2022*).
- **Deep Survival & Prognostic Networks**: DeepSurv and time-to-event models for revision risk and implant longevity (*Jamshidi et al., 2021*).
- **Causal Machine Learning & ITR**: Doubly robust learners, outcome-weighted learning, and causal forests to estimate heterogeneous treatment effects (*Feuerriegel et al., Nature Medicine 2024; Meng et al., JMLR 2020*).
- **Reinforcement Learning**: Offline RL and policy gradient methods (PPO) for longitudinal rehabilitation and dynamic treatment regimes (*Dong et al., 2026; de Filippis & Foysal, 2025*).
- **LLMs & RAG**: Previsit note summarization and guideline retrieval guardrails (*Halvorson et al., 2026; Billi & Bini, JBJS 2026; Woo et al., 2024*).

### Standard Evaluation Metrics

| Metric | Target Dimension | Interpretation |
| :--- | :--- | :--- |
| **ROC-AUC (0.70 – 0.95)** | Discrimination | Ability to distinguish between outcome classes (e.g., success vs. failure). |
| **Brier Score / Calibration Curve** | Reliability | Agreement between predicted probabilities and observed event rates. |
| **MCID Accuracy** | Clinical Benefit | Correct classification of achieving the Minimal Clinically Important Difference. |
| **Net Benefit (DCA)** | Utility | Clinical value across decision thresholds compared to treat-all or treat-none. |

### Documented Translational Bottlenecks
1. **High Risk of Bias**: Over 40% of published prediction models demonstrate high risk of bias under PROBAST due to unadjusted retrospective confounding (*Groot et al., 2021*).
2. **Center-Specific Dataset Shift**: Models transferred to external hospitals show AUROC drops of 0.15–0.20 without local recalibration (*Dwajan et al., 2026*).
3. **PROM Attrition**: 1- to 2-year follow-up loss exceeds 40% in routine registries, creating severe selective attrition bias.
4. **LLM Guideline Hallucinations**: Zero-shot foundation models produce non-guideline compliant recommendations in complex multi-joint pathology (*Dagher et al., 2024*).

---

## 2. Multi-Agent Decision-Support Architecture

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

1. **Ingestion & Profiling Agent**: Ingests unstructured referral text, previsit questionnaires, and imaging reports. Standardizes records into a unified patient schema.
2. **Cohort Retrieval Agent**: Computes clinical distance across normalized feature vectors (KL grade, baseline functional score, BMI, age) to surface historical peer cohorts.
3. **Causal Treatment Benefit Agent**: Evaluates competing treatment arms (e.g., physical therapy vs. intra-articular injection vs. arthroplasty) using doubly robust estimation to predict the probability of exceeding the MCID threshold:
   $$\Delta \text{PROM} = \text{PROM}_{\text{post}} - \text{PROM}_{\text{baseline}} \ge \text{MCID}$$
4. **Guideline & Safety Guardrail Agent**: Queries structured rule trees derived from American Academy of Orthopaedic Surgeons (AAOS) Clinical Practice Guidelines. Disqualifies contraindicated interventions.
5. **Clinical Synthesis Agent**: Aggregates model outputs into a single-page consultation brief, provides SHAP explanation plots, and displays calibrated confidence intervals for shared decision-making.

---

## 3. Data Schema

Standardized encounter record required for model input and evaluation:

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

---

## 4. Key Implementation Rules

- **Deterministic Fallbacks**: Every generative LLM component must operate in a secondary explanatory role; core treatment ranking must come from validated statistical/causal models.
- **Strict Human-in-the-Loop**: The system outputs ranked options with decision rationale, leaving final treatment selection to the clinician and patient.
- **Mandatory Reporting Standards**: All predictive modules must satisfy TRIPOD-AI and PROBAST-AI guidelines, reporting calibration curves alongside discriminative AUROC.

---

## 5. Supporting Documentation & Synthesis Corpus

| Document | Role in Project | What It Covers |
| :--- | :--- | :--- |
| **[Earlier progress](../research_progress.md)** | Thesis Scope & Milestones | Historical scope and milestones. |
| **[Research gaps](Research_Gaps.md)** | Gap Analysis | Earlier gap claims; see the corrective audit before relying on them. |
| **[State-of-the-art review](State_of_the_Art_Review.md)** | Evidence Synthesis | Earlier synthesis of diagnostic, prognostic and therapeutic algorithms. |
| **[Top 30 literature](Top_30_Core_Literature.md)** | Core Corpus Dossier | Earlier selected-paper dossier. |
| **[Feature synthesis](Feature_Level_Synthesis.md)** | Technical Synthesis | Earlier feature, method and validation mapping. |
| **[Corpus summaries](../corpus_summaries.md)** | Corpus Summary | Historical summaries retained for reference. |

---

## References

1. Abdelrahman I, et al. *Br J Surg*. 2026.
2. Billi F, Bini S. *J Bone Joint Surg Am*. 2026;108(2):e12.
3. Cochrane JA, et al. *Ther Adv Musculoskelet Dis*. 2026.
4. Dagher T, et al. *Clin Orthop Relat Res*. 2024;482(6):1042-1051.
5. de Filippis R, Foysal AA. *OALib*. 2025;12:e11892.
6. Dong JH, Chen T, Peng Z. *Front Rehabil Sci*. 2026;7:1489201.
7. Dwajan A, et al. *World J Clin Cases*. 2026;14(2):201-214.
8. Halvorson RT, et al. *Arthroscopy*. 2026;42(1):89-98.
9. Jamshidi A, et al. *Nat Rev Rheumatol*. 2018;14(5):257-269.
10. Kunze K, et al. *Arthroscopy*. 2021;37(5):1672-1685.
11. Meng H, et al. *J Mach Learn Res*. 2020;21(183):1-28.
12. Milella F, et al. *J Pers Med*. 2022;12(5):714.
13. Oettl F, et al. *Knee Surg Sports Traumatol Arthrosc*. 2025;33(2):112-125.
14. van der Weegen W, et al. *J Arthroplasty*. 2024;39(5):1173-1177.
