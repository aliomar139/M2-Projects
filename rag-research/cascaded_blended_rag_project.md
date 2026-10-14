# Cascaded Adaptive Blended RAG: Architectural Specification & Implementation Roadmap

## 1. Project Overview & Research Context
* **Base Paper:** *Blended RAG: Improving RAG Accuracy with Semantic Search and Hybrid Query-Based Retrievers* (Sawarkar et al., 2024, IEEE MIPR).
* **Research Goal:** Extend Blended RAG by designing a lightweight, pre-retrieval cascaded routing controller that dynamically routes queries across Lexical (BM25), Sparse Learned (SPLADE), and Dense Vector (MiniLM) retrievers, eliminating redundant compute for simple queries while maintaining or exceeding full hybrid retrieval accuracy.
* **Target Environment:** Laptop/CPU-friendly, reproducible Python environment without requiring costly LLM-as-a-judge APIs or expensive retriever fine-tuning.

---

## 2. Theoretical Flaws Resolved in This Specification
This updated specification addresses four critical flaws present in early post-retrieval gating proposals:
1. **The Latency Paradox (Post-Retrieval vs. Pre-Retrieval Gating):**
   * *Problem:* Evaluating candidate overlap or ranking disagreement between BM25 and Dense search requires running both retrievers first. Doing so saves zero latency or vector search compute.
   * *Solution:* We implement a **Two-Tier Pre-Retrieval Sequential Cascade**. A lightweight pre-retrieval feature check + BM25 Fast Pass evaluates early-exit confidence *before* triggering expensive dense embeddings or SPLADE forward passes.
2. **Inclusion of Sparse Learned Encoders (SPLADE):**
   * *Problem:* Standard hybrid baselines often omit sparse encoders, despite Blended RAG demonstrating that **Sparse Encoders (ELSER) + Best Fields matching** achieved the top retrieval accuracy (88.77% on NQ, 98.0% on TREC-COVID).
   * *Solution:* We integrate **SPLADE** (`naver/splade-cocondenser-ensembledistil`) alongside BM25 and `all-MiniLM-L6-v2`.
3. **Metadata & Multi-Field Query Awareness:**
   * *Problem:* Treating documents as flat text chunks misses Blended RAG's core innovation—multi-match strategies (*Best Fields*, *Cross Fields*) over metadata fields (`title`, `abstract`, `body`).
   * *Solution:* Datasets are indexed with field-level structures, allowing the controller to trigger multi-field query expansion when metadata is present.
4. **End-to-End Generation & Quality-Cost Pareto Evaluation:**
   * *Problem:* Evaluating retrieval metrics alone (Recall, MRR) ignores downstream LLM impact and latency trade-offs.
   * *Solution:* We measure end-to-end Exact Match (EM) and F1 using a small local generator (e.g., Llama-3.2-3B or Qwen-2.5-3B via Ollama) plotted against query latency (ms/query).

---

## 3. Literature Positioning & Novelty (2024–2026 Comparison)

| Approach / Paper | Search Modalities | Routing Decision Point | Saves Vector Search Compute? | Multi-Field Metadata Aware? |
| :--- | :--- | :--- | :---: | :---: |
| **Blended RAG** *(Sawarkar et al., 2024)* | BM25 + ELSER + Dense | Static (Runs all every query) | ❌ No | ✅ Yes |
| **DAT** *(Hsu et al., 2025)* | BM25 + Dense | Per-Query Alpha Weighting | ❌ No | ❌ No |
| **ScoreGate / CA-RAG** *(Mishra et al., 2026)* | Dense | Top-K Truncation / Depth | ✅ Partial | ❌ No |
| **AH-RAG** *(Sun et al., 2025)* | Sparse + Dense | Context Confidence Control | ❌ Partial | ❌ No |
| **Our Cascaded Blended RAG** | **BM25 + SPLADE + Dense** | **Pre-Retrieval & Sequential Cascade** | **✅ Yes (Early Exit)** | **✅ Yes** |

---

## 4. System Architecture & Routing Logic

```text
                           Incoming User Query
                                    │
                       ┌────────────┴────────────┐
                       │  Tier 0: Feature Extraction │
                       │ (Length, IDF, Rare Tokens)│
                       └────────────┬────────────┘
                                    │
                       ┌────────────┴────────────┐
                       │ Tier 1: BM25 Fast-Pass  │
                       └────────────┬────────────┘
                                    │
                  Is BM25 Score s1 > τ_high OR Margin Δ > τ_gap?
                                   ╱ ╲
                                 YES  NO
                                 ╱     ╲
                                ╱       ╲
     ┌─────────────────────────┐         ┌──────────────────────────────┐
     │ Early Exit: Return BM25 │         │ Tier 2: Fallback Blended RAG │
     │  Top-K Results Directly │         │ (SPLADE + Dense + BM25)      │
     └─────────────────────────┘         └──────────────┬───────────────┘
                                                        │
                                         ┌──────────────┴───────────────┐
                                         │  Multi-Field Reciprocal Rank │
                                         │          Fusion (RRF)        │
                                         └──────────────┬───────────────┘
                                                        │
                                         ┌──────────────┴───────────────┐
                                         │ Consolidated Document Context│
                                         └──────────────────────────────┘
```

### 4.1 Tier 0 & Tier 1 Early-Exit Mathematics
1. **Query Difficulty / Specificity Signals:**
   $$	ext{MaxIDF}(Q) = \max_{q \in Q} \log \left( rac{N - n(q) + 0.5}{n(q) + 0.5} + 1 ight)$$
   $$	ext{RareTokenRatio}(Q) = rac{|\{q \in Q \mid 	ext{IDF}(q) > 	heta_{	ext{rare}}\}|}{|Q|}$$
2. **BM25 Score Gap Confidence ($\Delta$):**
   Given BM25 candidate scores $s_1 \ge s_2 \ge \dots \ge s_k$:
   $$\Delta_{	ext{BM25}} = s_1 - s_2$$
3. **Decision Rule:**
   $$	ext{Route}(Q) = egin{cases} 	ext{BM25\_Only}, & 	ext{if } s_1 \ge 	au_{	ext{high}} \lor (\Delta_{	ext{BM25}} \ge 	au_{	ext{gap}} \land 	ext{MaxIDF}(Q) \ge 	au_{	ext{idf}}) \ 	ext{Full\_Blended\_RAG}, & 	ext{otherwise} \end{cases}$$

---

## 5. Technology Stack & Directory Layout

### 5.1 Tech Stack
* **Language:** Python 3.12
* **Lexical Search:** `rank-bm25` / `pyserini`
* **Sparse Learned Search:** `splade` (`naver/splade-cocondenser-ensembledistil` via HuggingFace/Transformers)
* **Dense Search:** `sentence-transformers` (`all-MiniLM-L6-v2`) + `faiss-cpu`
* **Evaluation Framework:** `ranx` or `ir_measures`
* **Local Generator (Optional End-to-End):** `ollama` or `transformers` with `Qwen/Qwen2.5-3B-Instruct` / `meta-llama/Llama-3.2-3B-Instruct`

### 5.2 Project Structure
```text
cascaded_blended_rag/
├── data/                       # Datasets (SciFact, NQ subset)
│   ├── raw/
│   └── processed/
├── src/                        # Modular Source Code
│   ├── __init__.py
│   ├── feature_extractor.py    # Tier 0 Query Feature Extraction
│   ├── bm25_retriever.py       # Tier 1 BM25 Indexing & Fast-Pass
│   ├── splade_retriever.py     # Tier 2 SPLADE Sparse Encoder
│   ├── dense_retriever.py      # Tier 2 FAISS Dense Indexing
│   ├── fusion.py               # Reciprocal Rank Fusion (RRF) & Multi-Field
│   └── controller.py           # Cascaded Adaptive Router
├── experiments/                # Experiment Notebooks / Scripts
│   ├── 01_baseline_bm25.py
│   ├── 02_baseline_dense.py
│   ├── 03_baseline_blended_rag.py
│   └── 04_cascaded_adaptive_rag.py
├── results/                    # CSVs, Latency Logs, and Plotting Figures
├── requirements.txt
└── README.md
```

---

## 6. Step-by-Step Implementation Roadmap

### Phase 1: Environment & Dataset Ingestion (Days 1–2)
1. Set up a virtual environment and install core packages (`rank-bm25`, `sentence-transformers`, `faiss-cpu`, `pyserini` or `torch`, `ranx`, `pandas`).
2. Download **SciFact** from BEIR (contains 5,183 documents with `title` and `abstract` fields, and 300 test queries).

### Phase 2: Implement Single-Strategy Baselines (Days 3–4)
1. Build `bm25_retriever.py` over SciFact title + abstract fields.
2. Build `dense_retriever.py` using `all-MiniLM-L6-v2` + FAISS IndexFlatIP.
3. Build `splade_retriever.py` to extract sparse term expansions.

### Phase 3: Implement Static Blended RAG Baseline (Days 5–6)
1. Implement Multi-Field *Best Fields* query matching across `title` and `abstract`.
2. Implement 3-way Reciprocal Rank Fusion (RRF):
   $$RRF\_Score(d) = \sum_{m \in \{	ext{BM25}, 	ext{SPLADE}, 	ext{Dense}\}} rac{w_m}{k + 	ext{rank}_m(d)}$$
3. Measure baseline Recall@5, Recall@10, MRR, nDCG@10, and average query latency (ms).

### Phase 4: Implement & Calibrate Cascaded Controller (Days 7–9)
1. Implement `feature_extractor.py` to extract $MaxIDF$, $RareTokenRatio$, and query length.
2. Build `controller.py` executing the Tier 1 BM25 Fast-Pass check.
3. Perform grid search on thresholds ($	au_{	ext{high}}, 	au_{	ext{gap}}$) on a validation split to find the optimal trade-off point where **80%+ of dense/sparse calls are saved for simple queries with < 1% drop in overall Recall@10**.

### Phase 5: End-to-End Evaluation & Thesis Figures (Days 10–12)
1. Generate comparative plots:
   * **Recall@10 vs. Latency (ms/query)** across all baselines and adaptive thresholds.
   * **% Vector Searches Avoided vs. Retrieval Accuracy**.
2. (Optional) Run 500 queries through a local 3B LLM to compute downstream **Exact Match (EM)** and **F1** consistency scores.

---

## 7. Expected Thesis Outcomes & Deliverables
1. **Primary Finding:** Proving that a pre-retrieval cascaded router reduces average query latency by **30–50%** while preserving **>98%** of static Blended RAG's retrieval accuracy.
2. **Methodological Contribution:** Demonstrating that discrete pre-retrieval routing overcomes the noise instability of continuous $lpha$-tuning methods identified in 2026 literature.
3. **Software Artifact:** A modular, reproducible Python codebase suitable for open-source publication alongside your Master's thesis.
