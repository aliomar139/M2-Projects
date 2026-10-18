import os
import json
import csv
import ssl
import urllib.request
import zipfile
from typing import Dict, Tuple

TREC_COVID_URL = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/trec-covid.zip"

def download_and_load_trec_covid(data_dir: str = "data/raw") -> Tuple[Dict[str, dict], Dict[str, str], Dict[str, Dict[str, int]]]:
    """
    Downloads BEIR TREC-COVID dataset.
    Extracts 50 official test queries and creates a candidate pool corpus:
      - All ground-truth relevant documents in qrels (relevance > 0)
      - Top documents per query for high-coverage benchmarking
    """
    os.makedirs(data_dir, exist_ok=True)
    tc_dir = os.path.join(data_dir, "trec-covid")
    zip_path = os.path.join(data_dir, "trec-covid.zip")

    if not os.path.exists(tc_dir):
        print(f"Downloading TREC-COVID dataset from {TREC_COVID_URL}...")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(TREC_COVID_URL, context=ctx) as response, open(zip_path, "wb") as f:
            f.write(response.read())
        print("Extracting TREC-COVID...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(data_dir)
        os.remove(zip_path)
        print("TREC-COVID download complete.")

    # 1. Load Qrels (Ground Truth)
    qrels = {}
    relevant_doc_ids = set()
    qrels_path = os.path.join(tc_dir, "qrels", "test.tsv")
    with open(qrels_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        for row in reader:
            if len(row) < 3:
                continue
            qid, did, score = str(row[0]), str(row[1]), int(row[2])
            if score > 0:
                qrels.setdefault(qid, {})[did] = score
                relevant_doc_ids.add(did)

    # 2. Load Queries (50 official test queries)
    queries = {}
    queries_path = os.path.join(tc_dir, "queries.jsonl")
    with open(queries_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            qid = str(item["_id"])
            if qid in qrels:
                queries[qid] = item["text"].strip()

    # 3. Load Corpus (Stream and keep all relevant docs + sample non-relevant up to ~10,000 docs for fast CPU evaluation)
    corpus = {}
    corpus_path = os.path.join(tc_dir, "corpus.jsonl")
    print(f"Streaming TREC-COVID corpus: targeting relevant docs ({len(relevant_doc_ids)}) + negative samples...")
    
    with open(corpus_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            did = str(item["_id"])
            # Always include all gold relevant docs, and fill up to 12,000 docs for a realistic retrieval pool
            if did in relevant_doc_ids or len(corpus) < 12000:
                corpus[did] = {
                    "title": item.get("title", "").strip(),
                    "abstract": item.get("text", "").strip()
                }

    print(f"Loaded TREC-COVID: {len(corpus)} pooled docs | {len(queries)} queries | {len(relevant_doc_ids)} gold relevant docs.")
    return corpus, queries, qrels

if __name__ == "__main__":
    download_and_load_trec_covid()

