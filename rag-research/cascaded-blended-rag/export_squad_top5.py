import os
import sys
import json
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from squad_loader import download_and_load_squad
from src.bm25_retriever import BM25Retriever
from src.dense_retriever import DenseRetriever
from src.splade_retriever import SPLADERetriever

def rrf(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank)

def export_squad_top5(num_queries: int = 500, output_path: str = "results/squad_top5_for_colab.json"):
    corpus, queries, qrels = download_and_load_squad()

    # Load raw SQuAD JSON to extract exact ground-truth answers for EM and F1
    with open("data/raw/squad_dev_v1.1.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)["data"]

    ground_truth_answers = {}
    for article in raw_data:
        for p in article["paragraphs"]:
            for qa in p["qas"]:
                qid = qa["id"]
                answers = [a["text"] for a in qa["answers"]]
                ground_truth_answers[qid] = answers

    eval_qids = list(queries.keys())[:num_queries]
    eval_queries = {qid: queries[qid] for qid in eval_qids}
    print(f"Exporting top-5 Blended RAG passages for {len(eval_queries)} queries...")

    # Load models & cached indexes
    bm25 = BM25Retriever(corpus)
    dense = DenseRetriever(corpus, cache_dir="data/processed_squad")
    splade = SPLADERetriever(corpus, cache_dir="data/processed_squad")

    export_records = []

    for qid in eval_queries:
        query_text = eval_queries[qid]

        res_bm25 = bm25.retrieve_best_fields(query_text, top_k=20)
        res_dense = dense.retrieve(query_text, top_k=20)
        res_splade = splade.retrieve(query_text, top_k=20)

        # 3-Way RRF
        fused = defaultdict(float)
        for rank, (d, _) in enumerate(res_bm25, start=1):
            fused[d] += rrf(rank)
        for rank, (d, _) in enumerate(res_dense, start=1):
            fused[d] += rrf(rank)
        for rank, (d, _) in enumerate(res_splade, start=1):
            fused[d] += rrf(rank)

        top_5_dids = [d for d, _ in sorted(fused.items(), key=lambda x: x[1], reverse=True)[:5]]

        top_5_passages = [
            {
                "doc_id": did,
                "title": corpus[did]["title"],
                "text": corpus[did]["abstract"]
            }
            for did in top_5_dids
        ]

        export_records.append({
            "query_id": qid,
            "question": query_text,
            "ground_truth_answers": ground_truth_answers.get(qid, []),
            "retrieved_top5": top_5_passages
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(export_records, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully exported {len(export_records)} records to {output_path}")

if __name__ == "__main__":
    export_squad_top5()

