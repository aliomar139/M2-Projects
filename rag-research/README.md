# Cascaded Adaptive Blended RAG: Research Repository

A systems-level extension of IBM's Blended RAG (*Sawarkar et al., IEEE MIPR 2024*), introducing sequential early-exit routing to eliminate redundant neural computation while preserving hybrid retrieval accuracy.

---

## 📁 Repository Directory Structure

```text
rag-research/
├── README.md                                  # Repository overview and quick start (this file)
├── PROJECT_ANCHOR.md                          # Live research telemetry, completed milestones, and data
│
├── docs/                                      # Research reports, publications, and presentation guides
│   ├── Cascaded_Blended_RAG_Research_Report.docx  # Formal academic report (Word format)
│   ├── Cascaded_Blended_RAG_Research_Report.md    # Formal academic report (Markdown format)
│   ├── cascaded_blended_rag_report.html       # Visual standalone HTML report
│   ├── cascaded_blended_rag_report.pdf        # Standalone PDF research report
│   ├── how_to_explain_the_project.md          # 30-second elevator pitch & oral defense guide
│   ├── cascaded_blended_rag_project.md        # Architectural roadmap & prior art comparison
│   ├── Blended-Rag.pdf                        # Base paper (Sawarkar et al., IBM Research, IEEE MIPR 2024)
│   └── proposal_brief.pdf                     # Original M2 proposal brief
│
├── notebooks/                                 # GPU execution and evaluation notebooks
│   └── reproduction.ipynb                     # Kaggle Dual T4 notebook (FLAN-T5-XXL QA & NQ Cascaded sweep)
│
├── cascaded-blended-rag/                      # Core implementation & experiment pipelines
│   ├── src/                                   # Production retrieval and routing modules
│   │   ├── bm25_retriever.py                  # Multi-field (Best Fields) BM25 indexer (CPU)
│   │   ├── dense_retriever.py                 # MiniLM-L6-v2 + FAISS FlatIP indexer
│   │   ├── splade_retriever.py                # SPLADE sparse neural encoder + CSR matrix cache
│   │   └── cascaded_router.py                 # Sequential decision gate (s1, delta, MaxIDF)
│   ├── experiments/                           # Reproducible evaluation scripts
│   │   ├── 01_baseline_bm25.py                # BM25 Single vs. Best Fields on SciFact
│   │   ├── 02_baseline_dense.py               # Dense vector evaluation on SciFact
│   │   ├── 03_baseline_splade.py              # SPLADE evaluation on SciFact
│   │   ├── 04_baseline_blended_rag.py         # 3-Way Reciprocal Rank Fusion on SciFact
│   │   ├── 05_replicate_squad.py              # SQuAD v1.1 Top-10 retrieval evaluation
│   │   ├── 06_replicate_trec_covid.py         # TREC-COVID NDCG@10 evaluation
│   │   └── 07_tune_cascade_cv.py              # 5-Fold Cross-Validation threshold grid search
│   ├── data_loader.py                         # BEIR SciFact data loading utility
│   ├── squad_loader.py                        # SQuAD v1.1 data extraction utility
│   ├── trec_covid_fast_loader.py              # Fast TREC-COVID loader with caching
│   ├── data/                                  # Preprocessed corpora, queries, and qrels
│   └── results/                               # Cached runs, predictions, and evaluation telemetry
│
├── Blended-RAG/                               # Official IBM Research repository clone
└── Similar-Papers/                            # Comparative literature datasets (DBLP & Consensus)
```

---

## 🔬 Core Empirical Results

### 1. Base Paper Reproduction Across Benchmarks

| Benchmark Dataset | Scope | Metric | Paper Baseline | Our Reproduction |
| :--- | :--- | :--- | :--- | :--- |
| **Natural Questions (NQ)** | 500 Queries (BEIR) | Top-20 Retrieval | 88.88% | **97.20% (Verified)** |
| **Natural Questions (NQ)** | 500 Queries (BEIR) | NDCG@10 | 0.6700 | **0.7094 (Verified)** |
| **SQuAD v1.1 Retrieval** | 500 Queries, 2067 Docs | Top-10 Retrieval | 94.49% | **96.40% (Verified)** |
| **SQuAD QA Generation** | FLAN-T5-XXL (11B) | Exact Match (EM) | 57.63% | **79.00% (Verified)** |
| **SQuAD QA Generation** | FLAN-T5-XXL (11B) | Token F1 Score | 68.40% | **81.59% (Verified)** |
| **TREC-COVID** | 50 Queries, 2572 Docs | NDCG@10 | 0.8000 - 0.8700 | **0.6463 (Beats all singles)** |

### 2. Cascaded Adaptive Extension on Natural Questions (Dual Nvidia T4 GPUs)

| Configuration | Thresholds ($\tau_{\text{high}}, \tau_{\text{gap}}$) | Neural Avoidance (%) | Average Latency | Top-20 Recall |
| :--- | :--- | :--- | :--- | :--- |
| **Static Blended RAG** | N/A (100% neural execution) | 0.0% | 67.0 ms | **97.20%** |
| **Cascaded - Conservative** | $\tau=28.0, \Delta=6.0, \text{IDF}=3.5$ | **73.2%** | **25.3 ms (62.2% cut)** | **91.80%** |
| **Cascaded - Balanced** | $\tau=25.0, \Delta=5.0, \text{IDF}=3.5$ | **84.2%** | **19.0 ms (71.6% cut)** | **89.40%** |
| **Cascaded - Moderate** | $\tau=23.0, \Delta=4.0, \text{IDF}=3.0$ | **90.0%** | **15.7 ms (76.6% cut)** | **88.40%** |
| **Pure BM25 Baseline** | Pure Lexical | 100.0% | **10.0 ms** | 84.40% |

---

## 🚀 Quick Execution Guide

Activate the environment from the repository root:

```powershell
# Activate Python Virtual Environment
.\cascaded-blended-rag\venv\Scripts\Activate.ps1

# Run 5-Fold Cross-Validation on SciFact
python cascaded-blended-rag/experiments/07_tune_cascade_cv.py

# Run Multi-Field BM25 Baseline
python cascaded-blended-rag/experiments/01_baseline_bm25.py

# Run 3-Way Blended RAG Baseline
python cascaded-blended-rag/experiments/04_baseline_blended_rag.py
```

For GPU end-to-end question answering and full NQ Pareto sweeps, run [notebooks/reproduction.ipynb](file:///c:/Users/user/Desktop/M2-Porjects/rag-research/notebooks/reproduction.ipynb) on Kaggle with dual T4 GPUs.

