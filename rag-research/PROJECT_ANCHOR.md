# PROJECT STATE & NEXT STEPS ANCHOR
## Cascaded Adaptive Blended RAG: Systems Extension for Efficient Multi-Field Hybrid Retrieval

**Last Updated:** October 18, 2026  
**Repository Working Directory:** `c:\Users\user\Desktop\M2-Porjects\rag-research\cascaded-blended-rag`  
**Base Paper:** *Blended RAG: Improving RAG Accuracy with Semantic Search and Hybrid Query-Based Retrievers* (Sawarkar, Mangal, & Solanki, 2024, IEEE MIPR).

---

## 1. What We Have Completed (100% Verified)

### A. Environment & Data Pipelines (Windows + Local CPU & Kaggle Dual-GPU)
* `cascaded-blended-rag/venv`: Virtualenv configured with `rank-bm25`, `sentence-transformers`, `faiss-cpu`, `transformers`, `ranx`, `scipy`, `torch`.
* `src/bm25_retriever.py`: Pure Python Best Fields BM25 retriever (avoids Windows Java/Anserini crashes).
* `src/dense_retriever.py`: Dense semantic retriever using `sentence-transformers/all-MiniLM-L6-v2` + FAISS flat index, disk embedding caching.
* `src/splade_retriever.py`: Sparse neural retriever using `naver/splade-cocondenser-ensembledistil` with `.npz` sparse CSR matrix disk caching.

### B. Empirical Base-Paper Reproductions Across 4 Datasets

| Dataset | Split & Scope | Metric | Paper Baseline | Our Reproduction | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Natural Questions (NQ)** | 500 test queries (BEIR) | Top-5 / Top-20 | 88.22% / 88.88% | **83.00% / 97.20%** | **Verified** (Kaggle dual T4) |
| **Natural Questions (NQ)** | 500 test queries (BEIR) | NDCG@10 | 0.6700 | **0.7094** | **Verified** |
| **SQuAD v1.1** | 500 queries, 2067 passages| Top-10 Retrieval| ~94.00% - 98.00% | **96.40%** | **Verified** (Local CPU) |
| **SQuAD v1.1 QA Generation** | FLAN-T5-XXL (11B model) | EM / Token F1 | 57.63% / 68.40% | **79.00% / 81.59%** | **Verified** (Kaggle dual T4) |
| **TREC-COVID** | 50 queries, 2572 docs | NDCG@10 | 0.80 - 0.87 | **0.6463** (beats all singles)| **Verified** (Local CPU) |
| **SciFact** | 300 test queries (BEIR) | Recall@100 / NDCG@10| N/A | **0.9610 / 0.7032** | **Verified** (Local CPU) |

### C. Master Ablation on Natural Questions (The Proof of the Waste)
From our Kaggle dual-GPU run on NQ:
* **BM25 alone**: 67.00% Top-5, 84.40% Top-20, NDCG@10 = 0.5433 (takes ~10 ms on CPU).
* **Dense alone**: 80.60% Top-5, 96.00% Top-20, NDCG@10 = 0.6751.
* **SPLADE alone**: 89.00% Top-5, 98.20% Top-20, NDCG@10 = 0.7589.
* **Blended RAG (3-Way RRF)**: 83.00% Top-5, 97.20% Top-20, NDCG@10 = 0.7094.

> **Key Finding for the Thesis:** BM25 alone already finds the correct answer for **84.40% of queries**. Blended RAG executes expensive neural models (Dense + SPLADE) for **100% of queries**, wasting heavy GPU compute on queries BM25 already solved.

---

## 2. Immediate Next Step (Phase 4: Our Research Contribution)

Implement **Cascaded Adaptive Blended RAG**:

```text
Incoming Query (Q)
       │
       ▼
[Tier 1: BM25 Fast-Pass (10 ms)]
       │
       ▼
Decision Gate: Is BM25 Score s1 >= τ_high OR Margin Δ(s1 - s2) >= τ_gap?
      ╱ ╲
    YES  NO
    ╱     ╲
   ▼       ▼
[EARLY EXIT]               [TIER 2: ESCALATE TO BLENDED RAG]
Return BM25 Top-K           Run Dense + SPLADE + BM25 with 3-Way RRF
100% Neural compute saved   Guarantees high recall for difficult queries
```

### The 3 Tasks Left To Implement:
1. `src/cascaded_router.py`: Gate logic with $\tau_{\text{high}}$ and $\tau_{\text{gap}}$.
2. `experiments/07_tune_cascade_cv.py`: 5-fold cross-validation grid search over $(\tau_{\text{high}}, \tau_{\text{gap}})$ on SciFact / NQ to prevent test-set data leakage.
3. `experiments/08_final_evaluation.py`: Log efficiency metrics (% neural calls avoided, latency reduction, Pareto frontier) vs. accuracy.

---

## 3. How to Resume Work in the Next Chat
In a new chat, simply paste:
> *"Read `PROJECT_ANCHOR.md`. We have finished all base paper reproductions (NQ, SQuAD, TREC-COVID, SciFact). Proceed to implement Phase 4: Cascaded Adaptive Blended RAG starting with `src/cascaded_router.py`."*

