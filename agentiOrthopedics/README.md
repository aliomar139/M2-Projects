# Agentic Orthopedics: AI/ML in Orthopedic Treatment Recommendation

Research exploration and literature review evaluating whether historical clinical records and Patient-Reported Outcome Measures (PROMs) can guide individualized orthopedic treatment decisions (conservative vs. operative, surgical technique selection, and recovery tracking).

---

## Quick Navigation

- [Research Progress & Thesis Direction](./RESEARCH_PROGRESS.md)
- [100-Paper PDF Corpus & Table Index](./top_100_papers/README.md)
- [Evidence Synthesis & Research Gaps](./Orthopedic_AI_Literature_Review/Research_Gaps.md)
- [Agentic AI Architecture Review](./agentic_orthopedic_ai_review.md)

---

## Repository Structure

```text
agentiOrthopedics/
├── README.md                                # Project overview and repository navigation
├── RESEARCH_PROGRESS.md                     # Thesis focus, methodological anchors, and milestone tracking
├── Orthopedic_AI_Literature_Review_Master.xlsx # Master workbook of all 100 reviewed papers
├── agentic_orthopedic_ai_review.md          # Multi-agent systems and LLM orchestration review
│
├── top_100_papers/                          # Complete full-text PDF collection (100 papers)
│   ├── 001_Closed-Loop_digital_...pdf       # Standardized indexed PDFs (001 to 100)
│   ├── manifest.csv                         # DOIs, download sources, file sizes, verification flags
│   ├── orthopedic_ai_papers_summary.md      # Summary of clinical findings and models
│   └── README.md                            # Table index with direct PDF links
│
├── Orthopedic_AI_Literature_Review/         # In-depth synthesis and gap analyses
│   ├── Paper_Processing_Status.md           # Full corpus verification registry
│   ├── Research_Gaps.md                     # Methodological and clinical translation gap analysis
│   ├── State_of_the_Art_Review.md           # Benchmark performance and clinical evidence
│   ├── Complete_Paper_Analysis.md           # Detailed analysis per paper
│   ├── Feature_Level_Synthesis.md           # Inputs, algorithms, and outcome metrics
│   └── Top_30_Core_Literature.md            # In-depth dossier of top 30 ranked papers
│
└── archive/                                 # Historical search datasets
    ├── top_100_orthopedic_ai_papers.csv     # Scored and ranked dataset
    ├── AgenticAi.csv                        # Initial search on agentic healthcare systems
    └── CrossDomain.csv                      # Initial search on cross-domain treatment recommendation
```

---

## Core Focus Areas

1. **Individualized Treatment Recommendation (ITR)**: Moving past predicting historical surgeon choices (imitation) to estimate counterfactual, patient-specific treatment benefit (optimization).
2. **Clinical Decision Support Systems (CDSS)**: Preoperative risk assessment, complication avoidance, and surgical triage using tabular clinical registries and PROMs.
3. **Agentic Workflows & LLMs**: Evaluating autonomous clinical agents, Retrieval-Augmented Generation (RAG) for clinical guidelines, and automated note extraction.

---

## Markdown Documentation Guide

| File | Scope | What It Contains |
| :--- | :--- | :--- |
| **[`README.md`](./README.md)** | Root | Project overview, navigation map, core focus areas, and file index. |
| **[`RESEARCH_PROGRESS.md`](./RESEARCH_PROGRESS.md)** | Root | Master's thesis trajectory, causal ITR formulation, 4 anchor papers, consensus, gaps, and milestones. |
| **[`agentic_orthopedic_ai_review.md`](./agentic_orthopedic_ai_review.md)** | Root | 100-paper evidence synthesis, 5-agent CDSS architecture, data schemas, and deployment guardrails. |
| **[`top_100_papers/README.md`](./top_100_papers/README.md)** | Corpus | Direct links to all 100 full-text PDFs with author and year metadata. |
| **[`top_100_papers/orthopedic_ai_papers_summary.md`](./top_100_papers/orthopedic_ai_papers_summary.md)** | Corpus | Detailed summaries of clinical aims, model architectures, and performance metrics per paper. |
| **[`Orthopedic_AI_Literature_Review/Paper_Processing_Status.md`](./Orthopedic_AI_Literature_Review/Paper_Processing_Status.md)** | Review | Complete audit tracking 100% full-text PDF verification, DOIs, and extraction state. |
| **[`Orthopedic_AI_Literature_Review/Literature_Review_Abstract.md`](./Orthopedic_AI_Literature_Review/Literature_Review_Abstract.md)** | Review | Formal academic abstract summarizing findings and critical gaps across the 100 papers. |
| **[`Orthopedic_AI_Literature_Review/State_of_the_Art_Review.md`](./Orthopedic_AI_Literature_Review/State_of_the_Art_Review.md)** | Review | Deep synthesis of state-of-the-art predictive and decision-support models in orthopedics. |
| **[`Orthopedic_AI_Literature_Review/Research_Gaps.md`](./Orthopedic_AI_Literature_Review/Research_Gaps.md)** | Review | Granular breakdown of 5 methodological gaps (e.g. imitation vs. ITR) and 5 translation barriers. |
| **[`Orthopedic_AI_Literature_Review/Top_30_Core_Literature.md`](./Orthopedic_AI_Literature_Review/Top_30_Core_Literature.md)** | Review | Comprehensive dossiers on the top 30 ranked papers in the corpus. |
| **[`Orthopedic_AI_Literature_Review/Top_30_Core_Papers.md`](./Orthopedic_AI_Literature_Review/Top_30_Core_Papers.md)** | Review | Quick-reference index classifying the top 30 papers by clinical subspecialty. |
| **[`Orthopedic_AI_Literature_Review/Complete_Paper_Analysis.md`](./Orthopedic_AI_Literature_Review/Complete_Paper_Analysis.md)** | Review | Individual analysis of all 100 papers detailing clinical task, dataset size, and key finding. |
| **[`Orthopedic_AI_Literature_Review/Complete_Paper_Feature_Extraction.md`](./Orthopedic_AI_Literature_Review/Complete_Paper_Feature_Extraction.md)** | Review | Full data extraction matrix covering inputs, ML algorithms, and target outcomes. |
| **[`Orthopedic_AI_Literature_Review/Feature_Level_Synthesis.md`](./Orthopedic_AI_Literature_Review/Feature_Level_Synthesis.md)** | Review | Comparative analysis of feature categories, model families, and clinical validation metrics. |
| **[`Orthopedic_AI_Literature_Review/Quick_Read_Analysis.md`](./Orthopedic_AI_Literature_Review/Quick_Read_Analysis.md)** | Review | Condensed high-yield summary for fast reading of corpus themes and metrics. |
| **[`archive/README.md`](./archive/README.md)** | Archive | Documentation of exploratory search datasets (`AgenticAi.csv`, `CrossDomain.csv`). |
