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
