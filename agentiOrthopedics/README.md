# Agentic Orthopedics: AI/ML in Orthopedic Treatment Recommendation

Research exploration and literature curation on the application of **Artificial Intelligence (AI), Machine Learning (ML), and Agentic Decision Systems** to orthopedic surgical decision-making and individualized treatment recommendation.

---

## Project Overview

This repository hosts the data, synthesis documents, and full-text literature corpus examining whether and how historical clinical and patient-reported outcome data can support individualized orthopedic treatment choices (operative vs. non-operative management, surgical technique selection, and recovery pathway optimization).

### Key Themes
- **Clinical Decision Support Systems (CDSS)**: Predictive models for preoperative risk assessment, complication avoidance, and intervention selection.
- **Individualized Treatment Recommendation (ITR)**: Causal and outcome-weighted machine learning models estimating patient-specific treatment benefit.
- **Agentic AI & LLMs in Surgery**: Autonomous and semi-autonomous multi-agent workflows, large language models (ChatGPT-4, Claude, local models) predicting surgeon recommendations, and automated evidence synthesis.

---

## Repository Structure

```text
agentiOrthopedics/
├── README.md                            # Main project overview and directory index
├── top_100_orthopedic_ai_papers.csv     # Master dataset of 100 curated papers (metadata, citations, abstracts)
│
├── top_100_papers/                      # Complete collection of 100 full-text PDFs
│   ├── 001_Closed-Loop_digital_...pdf   # Ranked research papers (PDF format)
│   ├── ...
│   ├── 100_Medicine_&_Treatment_...pdf
│   ├── manifest.csv                     # Detailed manifest with download sources, file sizes, and DOIs
│   └── README.md                        # Complete table index of all 100 papers with direct file links
│
├── archive/                             # Archived exploratory datasets
│   ├── AgenticAi.csv                    # Initial search results on agentic AI in healthcare
│   ├── CrossDomain.csv                  # Initial search results on cross-domain treatment recommendation
│   └── README.md                        # Provenance and archival context
│
├── RESEARCH_PROGRESS.md                 # Methodological progress record and paper deep-dives
├── agentic_orthopedic_ai_review.md      # Literature review on agentic AI architectures in orthopedics
├── orthopedic_ai_papers_summary.md      # Comprehensive thematic summary across the 100 papers
│
├── sync_top100_orthopedic.py            # Automated synchronization and retrieval script
└── downloader_helpers.py                # Multi-API academic scraper and open-access PDF resolver
```

---

## Datasets & Curated Corpus

1. **Active Master Dataset ([`top_100_orthopedic_ai_papers.csv`](./top_100_orthopedic_ai_papers.csv))**:
   - Contains 100 carefully ranked papers based on citation velocity, journal quartile (SJR Q1–Q4), clinical relevance score, and methodology.
   - Fields: `Rank`, `Relevance Score`, `Title`, `Authors`, `Year`, `Journal`, `Journal SJR Quartile`, `Study Type`, `Citations`, `Takeaway`, `Abstract`, `DOI`, `Consensus Link`.

2. **Full-Text Paper Collection ([`top_100_papers/`](./top_100_papers/))**:
   - 100 full-text PDFs successfully indexed and organized with standardized filenames (`001_...pdf` through `100_...pdf`).
   - Accompanied by [`manifest.csv`](./top_100_papers/manifest.csv) and [`top_100_papers/README.md`](./top_100_papers/README.md).

3. **Archived Scoping Datasets ([`archive/`](./archive/))**:
   - Historical CSV files from preliminary exploratory queries (`AgenticAi.csv` and `CrossDomain.csv`) stored for traceability and provenance.

---

## Research Documents & Reviews

- **[`RESEARCH_PROGRESS.md`](./RESEARCH_PROGRESS.md)**: Conceptual investigation analyzing the boundary between predicting historical clinician decisions versus counterfactual, outcome-optimal treatment recommendations.
- **[`agentic_orthopedic_ai_review.md`](./agentic_orthopedic_ai_review.md)**: Synthesis of multi-agent architectures, reinforcement learning from clinical feedback, and LLM orchestration in musculoskeletal medicine.
- **[`orthopedic_ai_papers_summary.md`](./orthopedic_ai_papers_summary.md)**: Comprehensive dossier summarizing clinical findings, model families (XGBoost, deep survival, RL, transformers), and clinical validation metrics across all 100 papers.

---

## Automation Scripts

The repository includes a Python pipeline to verify, download, and index academic papers:

- **[`sync_top100_orthopedic.py`](./sync_top100_orthopedic.py)**: Iterates through [`top_100_orthopedic_ai_papers.csv`](./top_100_orthopedic_ai_papers.csv), maps DOIs to PubMed Central IDs via NCBI's ID converter, verifies existing PDF files, downloads open-access articles across academic APIs, and updates the manifest.
- **[`downloader_helpers.py`](./downloader_helpers.py)**: Modular functions supporting PubMed Central AWS Open Data, Unpaywall, OpenAlex, Semantic Scholar, Europe PMC, and arXiv APIs.

### Running the Sync Pipeline
```bash
python sync_top100_orthopedic.py
```
*(Dependencies: `pandas`, `requests`, `beautifulsoup4`)*
