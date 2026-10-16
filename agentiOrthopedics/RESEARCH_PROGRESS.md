# Research Progress: AI & Causal Decision Support in Orthopedics

## Project Status at a Glance

- **Focus**: Master's thesis research evaluating whether historical clinical and PROM data can support individualized orthopedic treatment decisions (conservative vs. operative, surgical technique selection).
- **Corpus**: 100 verified full-text papers (78 orthopedic clinical/predictive, 22 cross-domain causal inference, RL, and CDSS methodology).
- **Core Challenge**: Shifting from predicting clinician habits (imitation) to estimating patient-specific treatment benefit (counterfactual optimization).

---

## 1. Current Research Direction

### Problem Statement
Most orthopedic predictive models address:
$$\text{Patient Characteristics } (X) \longrightarrow \text{Predicted Clinician Choice } (\hat{A})$$

This answers what a surgeon historically chose, not what will produce the best outcome for the patient. A clinically valuable system must address:
$$\text{Patient Characteristics } (X) + \text{Candidate Treatment } (A) \longrightarrow \text{Estimated Outcome } (\hat{Y})$$
$$\pi^*(X) = \arg\max_{a \in \mathcal{A}} \mathbb{E}[Y(a) \mid X]$$

### Research Objective
Develop and benchmark an Individualized Treatment Recommendation (ITR) framework for orthopedic cohorts that:
1. Evaluates treatment options (e.g., non-operative therapy vs. surgical intervention, or total vs. unicompartmental arthroplasty).
2. Adjusts for confounding and indication bias in observational registry data.
3. Quantifies individual treatment effect (ITE) on validated Patient-Reported Outcome Measures (PROMs: KOOS, WOMAC, OKS, HAGOS).
4. Evaluates net clinical benefit via Decision Curve Analysis (DCA), not just AUROC or accuracy.

---

## 2. Foundational Anchor Literature

The initial literature investigation identified four core methodological anchors, now expanded across the full 100-paper corpus:

### Anchor 1: Orthopedic Decision Prediction (Imitation Baseline)
- **Paper**: van der Weegen et al. (*J Arthroplasty*, 2024)
- **Target**: Operative vs. non-operative strategy for 119 prospective hip consultations using pre-hospital history-taking data.
- **Finding**: 85% overall agreement with surgeon choices (97% accuracy for non-operative, 67% for operative).
- **Takeaway**: Demonstrates pre-consultation feature utility, but models surgeon behavior rather than patient benefit. Replicated at scale by Halvorson et al. (*Arthroscopy*, 2026; LLMs predicting surgeon choices with 70–81% accuracy).

### Anchor 2: Two-Stage Recommendation and Survival Modeling
- **Paper**: Lee et al. (*npj Digit Med*, 2023)
- **Target**: Multi-center hepatocellular carcinoma decision support across 2,685 patients.
- **Finding**: Stage 1 recommends ranked treatment options (voting ensemble; top-2 accuracy 86–87%). Stage 2 estimates post-treatment survival (random survival forest; C-index 0.78–0.84).
- **Takeaway**: Demonstrates coupling treatment selection with outcome prediction, though treatment ranking remains anchored to observed practice.

### Anchor 3: Multilabel Clinical Action Prediction
- **Paper**: Pulick et al. (*JMIR AI*, 2026)
- **Target**: Predicting 10 distinct lifesaving interventions for 2,480 deteriorating ward encounters using EHR time series.
- **Finding**: Gradient boosting (XGBoost) and stacking ensembles achieved AUROCs of 0.70–0.90 across diverse interventions.
- **Takeaway**: Clinical decision support often requires multi-action recommendation rather than isolated binary choices. Expert chart review provides gold-standard labels that reduce documentation noise.

### Anchor 4: Formal Individualized Treatment Recommendation (ITR)
- **Paper**: Meng et al. (*JMLR*, 2020)
- **Target**: Methodological framework for near-optimal treatment regimes using outcome-weighted learning.
- **Finding**: Identifies a subset of near-optimal treatments when multiple choices yield statistically comparable expected patient benefits, avoiding forced arbitrary choices.
- **Takeaway**: Addresses the fundamental counterfactual problem: each historical patient received only one treatment. Causal estimators (e.g., doubly robust learners, causal forests) are mandatory to estimate unobserved counterfactual outcomes.

---

## 3. Evidence-Based Consensus Across the 100-Paper Corpus

| Domain | Established Finding | Key Limitation |
| :--- | :--- | :--- |
| **Diagnostic Imaging** | Deep learning matches or exceeds residents (>90% sensitivity/specificity for fractures and Kellgren-Lawrence grading). | Solves perception, not therapeutic decision-making. |
| **Risk Stratification** | Supervised ML (XGBoost, Random Forest) predicts complications, revision risk, and readmission from registries. | High risk of complication does not indicate which alternative treatment reduces that risk. |
| **Multimodal Inputs** | Combining imaging, comorbidities, physical exam, and PROMs consistently outperforms unimodal models. | High feature burden (30–60 variables) impedes real-world clinic workflows. |
| **Generative AI & LLMs** | LLMs parse unstructured previsit notes and achieve 70–81% agreement with surgeon plans. | Zero-shot LLMs hallucinate treatment guidelines in complex multimorbid cases without RAG. |
| **Causal Inference & RL** | Offline RL, bandit algorithms, and doubly robust estimators can optimize sequential treatment policies. | Less than 5% of orthopedic AI literature applies formal causal methods; observational confounding is rarely addressed. |

---

## 4. Key Gaps Directly Addressing the Thesis

1. **The Imitation vs. Optimization Gap**: 24% of the corpus predicts historical surgeon decisions, but fewer than 4% estimate counterfactual treatment effects.
2. **Indication Bias & Treatment Selection**: Retrospective registries suffer from unmeasured confounders (bone quality, patient motivation, socioeconomic factors) that bias raw outcome comparisons.
3. **The Validation & Calibration Void**: Less than 7% of studies report calibration curves or Brier scores; external geographic validation is below 10%.
4. **Lack of Net Clinical Benefit**: Decision Curve Analysis (DCA) is applied in only 3% of papers, leaving real clinical utility unmeasured against standard-of-care guidelines.
5. **No Clinical Multi-Agent Deployment**: While agentic workflows are discussed conceptually, zero prospective clinical trials have deployed autonomous multi-agent systems in orthopedic clinics.

---

## 5. Repository Markdown Documentation Map

| File Path | Document Type | Core Contents |
| :--- | :--- | :--- |
| **[`README.md`](./README.md)** | Project Overview | High-level repository guide, architecture pillars, and quick links. |
| **[`RESEARCH_PROGRESS.md`](./RESEARCH_PROGRESS.md)** | Research Progress | Thesis framing, causal ITR formulation, anchor papers, and milestone tracking. |
| **[`agentic_orthopedic_ai_review.md`](./agentic_orthopedic_ai_review.md)** | System Architecture | Literature synthesis on agentic AI, LLM orchestration, and 5-agent clinical CDSS design. |
| **[`archive/README.md`](./archive/README.md)** | Archival Context | Data provenance for exploratory datasets (`AgenticAi.csv`, `CrossDomain.csv`). |
| **[`top_100_papers/README.md`](./top_100_papers/README.md)** | PDF Index | Master table linking all 100 verified full-text PDFs with author and year metadata. |
| **[`top_100_papers/orthopedic_ai_papers_summary.md`](./top_100_papers/orthopedic_ai_papers_summary.md)** | Literature Dossier | Technical summary of models, clinical tasks, and validation metrics across the 100 papers. |
| **[`Orthopedic_AI_Literature_Review/Paper_Processing_Status.md`](./Orthopedic_AI_Literature_Review/Paper_Processing_Status.md)** | Corpus Verification | Audit log confirming 100% full-text PDF retrieval, DOI mapping, and extraction status. |
| **[`Orthopedic_AI_Literature_Review/Literature_Review_Abstract.md`](./Orthopedic_AI_Literature_Review/Literature_Review_Abstract.md)** | Academic Abstract | Formal conference/journal abstract summarizing findings across the 100-paper corpus. |
| **[`Orthopedic_AI_Literature_Review/State_of_the_Art_Review.md`](./Orthopedic_AI_Literature_Review/State_of_the_Art_Review.md)** | Evidence Synthesis | In-depth review of diagnostic, prognostic, and therapeutic algorithms in musculoskeletal care. |
| **[`Orthopedic_AI_Literature_Review/Research_Gaps.md`](./Orthopedic_AI_Literature_Review/Research_Gaps.md)** | Gap Analysis | Detailed audit of 5 methodological gaps and 5 clinical translation barriers. |
| **[`Orthopedic_AI_Literature_Review/Top_30_Core_Literature.md`](./Orthopedic_AI_Literature_Review/Top_30_Core_Literature.md)** | Core Literature Dossier | Deep-dive critical analysis of the 30 highest-ranked papers in the corpus. |
| **[`Orthopedic_AI_Literature_Review/Top_30_Core_Papers.md`](./Orthopedic_AI_Literature_Review/Top_30_Core_Papers.md)** | Core Quick Reference | Compact listing and clinical focus categorization of the top 30 papers. |
| **[`Orthopedic_AI_Literature_Review/Complete_Paper_Analysis.md`](./Orthopedic_AI_Literature_Review/Complete_Paper_Analysis.md)** | Granular Analysis | Individual paper breakdown covering clinical setting, sample size, and core takeaway. |
| **[`Orthopedic_AI_Literature_Review/Complete_Paper_Feature_Extraction.md`](./Orthopedic_AI_Literature_Review/Complete_Paper_Feature_Extraction.md)** | Feature Matrix | Tabular extraction of patient features, inputs, algorithms, and target outcomes per paper. |
| **[`Orthopedic_AI_Literature_Review/Feature_Level_Synthesis.md`](./Orthopedic_AI_Literature_Review/Feature_Level_Synthesis.md)** | Cross-Study Synthesis | Thematic aggregation of input variables, ML model families, and clinical outcome metrics. |
| **[`Orthopedic_AI_Literature_Review/Quick_Read_Analysis.md`](./Orthopedic_AI_Literature_Review/Quick_Read_Analysis.md)** | Executive Briefing | High-impact takeaways and condensed patterns for rapid clinical and technical reference. |

---

## 6. Milestone Progress Tracker

### Completed
- [x] Curated and verified 100-paper full-text corpus (100% PDFs on disk with metadata manifest).
- [x] Completed systematic feature-level synthesis and state-of-the-art gap analysis.
- [x] Defined methodological boundary: decision prediction (supervised imitation) vs. individualized treatment recommendation (causal optimization).
- [x] Identified 4 core methodological anchor papers and contextualized them within the broader 100-paper corpus.
- [x] Documented critical data requirements (pre-treatment covariates, intervention labels, longitudinal PROMs).

### In Progress
- [ ] Identifying candidate open/consortium datasets with linked treatments and longitudinal PROMs (e.g., Osteoarthritis Initiative [OAI], National Joint Registries, or institutional arthroplasty cohorts).
- [ ] Formalizing mathematical framework for ITR comparison (Supervised Classifier vs. Causal Forest / Doubly Robust Learner).

### Next Actions
1. Download and inspect candidate dataset schemas (focus on OAI knee osteoarthritis cohort: clinical baseline + conservative vs. surgical interventions + 12/24-month KOOS/WOMAC).
2. Define inclusion criteria, primary treatment arms, and target PROM outcome thresholds (MCID).
3. Draft Master's thesis methodology section comparing decision prediction with doubly robust ITR.
