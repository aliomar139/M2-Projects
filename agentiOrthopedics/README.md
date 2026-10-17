# Agentic Orthopedics: AI/ML in Orthopedic Treatment Recommendation

Research exploration and literature review evaluating whether historical clinical records, imaging, and Patient-Reported Outcome Measures (PROMs) can guide individualized orthopedic treatment decisions (conservative vs. operative, surgical technique selection, and recovery tracking).

---

## Quick Navigation

- [Master Literature Review & System Design](./LITERATURE_REVIEW.md)
- [Research Progress & Thesis Milestones](./RESEARCH_PROGRESS.md)
- [100-Paper Full-Text PDF Corpus](./top_100_papers/README.md)
- [Paper Processing & Verification Registry](./Orthopedic_AI_Literature_Review/Paper_Processing_Status.md)

---

## Streamlined Repository Structure

```text
agentiOrthopedics/
├── README.md                                # Project overview and repository navigation
├── LITERATURE_REVIEW.md                     # Master Deliverable: Abstract, 7 SOTA tiers, Top 30 dossier, Gaps, 5-Agent CDSS
├── RESEARCH_PROGRESS.md                     # Thesis focus, causal ITR formulation, and milestone tracking
├── Orthopedic_AI_Literature_Review_Master.xlsx # Master workbook of all 100 reviewed papers
│
├── top_100_papers/                          # Complete full-text PDF collection (100 papers)
│   ├── 001_Closed-Loop_digital_...pdf       # Standardized indexed PDFs (001 to 100)
│   ├── manifest.csv                         # DOIs, download sources, file sizes, verification flags
│   ├── README.md                            # Table index with direct PDF links
│   └── orthopedic_ai_papers_summary.md      # Comprehensive summaries of all 100 papers
│
├── Orthopedic_AI_Literature_Review/         # Audit logs and historical review archive
│   ├── Paper_Processing_Status.md           # Full corpus verification registry
│   └── archive_raw_reports/                 # Preserved raw paper extraction drafts and synthesis sheets
│
└── archive/                                 # Historical search datasets (CSV)
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

## Deliverables Summary

| Deliverable | Location | What It Contains |
| :--- | :--- | :--- |
| **Unified Master Review** | [`LITERATURE_REVIEW.md`](./LITERATURE_REVIEW.md) | Single master document containing the full 100-paper synthesis: abstract, 7 translational tiers, Top 30 core dossier, 10 evidence gaps, and the 5-agent CDSS architecture. |
| **Research Progress Tracker** | [`RESEARCH_PROGRESS.md`](./RESEARCH_PROGRESS.md) | Problem formulation ($X \to \hat{A}$ vs $\arg\max_a \mathbb{E}[Y(a)\|X]$), 4 foundational anchor papers, and active Master's thesis milestones. |
| **Corpus PDF Library** | [`top_100_papers/README.md`](./top_100_papers/README.md) | Directory table linking all 100 full-text PDFs on disk with metadata. |
| **Corpus Paper Dossier** | [`top_100_papers/orthopedic_ai_papers_summary.md`](./top_100_papers/orthopedic_ai_papers_summary.md) | Ranked technical summaries for all 100 papers. |
| **Verification Registry** | [`Orthopedic_AI_Literature_Review/Paper_Processing_Status.md`](./Orthopedic_AI_Literature_Review/Paper_Processing_Status.md) | 100% full-text PDF verification audit and DOI cross-references. |
| **Preserved Raw Archive** | [`Orthopedic_AI_Literature_Review/archive_raw_reports/`](./Orthopedic_AI_Literature_Review/archive_raw_reports/) | Subfolder preserving the 10 raw decomposed drafts and feature matrices for complete auditability. |
