import json
import os
import re
import urllib.request
import urllib.parse
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

OUT_DIR = os.path.join(os.getcwd(), "ExplainableAI_Student_Burnout_Papers")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
os.makedirs(PDF_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

with open("candidates_dump.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

def score_paper(p):
    text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
    score = 0
    
    # Year check (last 2 years: 2024, 2025, 2026)
    year = p.get("year")
    if not year or year < 2024:
        return -100
    
    # Core terms: burnout
    if "burnout" in text:
        score += 30
    if "student" in text or "academic" in text or "university" in text or "school" in text or "education" in text or "undergraduate" in text or "medical student" in text:
        score += 25
    if "explainable" in text or "xai" in text or "shap" in text or "lime" in text or "interpretable" in text or "interpretability" in text:
        score += 30
    if "predict" in text or "prediction" in text or "forecasting" in text or "machine learning" in text or "deep learning" in text:
        score += 20
        
    # Extra boost for title matches
    title_lower = p.get("title", "").lower()
    if "burnout" in title_lower:
        score += 25
    if "explainable" in title_lower or "xai" in title_lower or "interpretable" in title_lower or "shap" in title_lower:
        score += 25
    if "student" in title_lower or "academic" in title_lower:
        score += 20
    if "predict" in title_lower:
        score += 15
        
    return score

# Score all candidates
scored = []
for p in candidates:
    s = score_paper(p)
    scored.append((s, p))

scored.sort(key=lambda x: x[0], reverse=True)

print(f"Top 30 candidates by relevance score:")
for i, (score, p) in enumerate(scored[:30], 1):
    print(f"{i}. [Score: {score}] [{p.get('year')}] {p.get('title')}")
    print(f"   PDFs available: {len(p.get('pdf_urls', []))} | Source: {p.get('source')}")
