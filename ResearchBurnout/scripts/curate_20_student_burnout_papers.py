import os
import sys
import json
import re
import urllib.request
import ssl

sys.stdout.reconfigure(line_buffering=True)

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

OUT_DIR = os.path.join(os.getcwd(), "ExplainableAI_Student_Burnout_Papers")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
os.makedirs(PDF_DIR, exist_ok=True)

with open("candidates_dump.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

def clean_title(title):
    return re.sub(r'\s+', ' ', title).strip()

def sanitize_filename(name):
    s = re.sub(r'[\\/*?:"<>|]', "", name)
    s = re.sub(r'\s+', " ", s).strip()
    if len(s) > 100:
        s = s[:100].rstrip()
    return s

# Exact criteria:
# 1. Year >= 2024
# 2. Must be about students (university, college, academic, school, medical/nursing students)
# 3. Must be about burnout (academic burnout, student burnout, learning burnout, exhaustion)
# 4. Must involve AI / Machine Learning / Explainable AI / Predictive Modeling
# 5. Not non-student healthcare staff unless medical/nursing students

curated = []
seen_titles = set()

for p in candidates:
    title = clean_title(p.get("title", ""))
    t_lower = title.lower()
    abstract = p.get("abstract", "").lower()
    full = t_lower + " " + abstract
    
    # Exclude non-student healthcare workforce
    if any(nw in t_lower for nw in ["physicians", "radiology nurses", "workforce burnout", "clinical nurses"]):
        if not ("student" in full or "resident" in full):
            continue
            
    # Student check
    is_student = any(k in full for k in ["student", "academic", "university", "college", "school", "undergraduate", "postgraduate", "resident"])
    # Burnout check
    is_burnout = "burnout" in full or "exhaustion" in full
    # AI/ML/XAI check
    is_aiml = any(k in full for k in ["explainable", "interpret", "shap", "lime", "machine learning", "deep learning", "predict", "decision tree", "c5.0", "random forest", "xgboost", "lightgbm", "neural network"])
    
    if is_student and is_burnout and is_aiml and p.get("year") and p["year"] >= 2024 and p.get("pdf_urls"):
        # Normalize title for uniqueness
        norm_t = re.sub(r'[^a-z0-9]', '', t_lower)
        if norm_t in seen_titles:
            continue
        seen_titles.add(norm_t)
        
        # Calculate specificity score
        score = 0
        if "burnout" in t_lower:
            score += 40
        if "student" in t_lower or "academic" in t_lower or "college" in t_lower:
            score += 30
        if any(x in t_lower for x in ["explainable", "xai", "shap", "interpretable", "c5.0", "lightgbm", "xgboost"]):
            score += 35
        if "predict" in t_lower:
            score += 20
        if any(x in abstract for x in ["explainable", "shap", "feature importance", "interpretability"]):
            score += 20
            
        curated.append((score, p))

curated.sort(key=lambda x: x[0], reverse=True)
print(f"Total curated student burnout AI/ML papers matching criteria: {len(curated)}")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream,*/*"
}

verified_papers = []

for idx, (score, p) in enumerate(curated):
    if len(verified_papers) >= 20:
        break
        
    title = clean_title(p["title"])
    year = p["year"]
    clean_name = sanitize_filename(f"{year} - {title}")
    pdf_filename = f"{clean_name}.pdf"
    target_path = os.path.join(PDF_DIR, pdf_filename)
    
    # Check if file exists and valid
    if os.path.exists(target_path) and os.path.getsize(target_path) > 30000:
        with open(target_path, "rb") as f:
            head = f.read(1024)
            if b"%PDF" in head:
                verified_papers.append({
                    "number": len(verified_papers) + 1,
                    "title": title,
                    "year": year,
                    "source": p.get("source", "Academic Publication"),
                    "authors": p.get("authors", []),
                    "doi": p.get("doi"),
                    "pdf_filename": pdf_filename,
                    "pdf_size_kb": os.path.getsize(target_path) // 1024,
                    "abstract": p.get("abstract", "")
                })
                print(f"[{len(verified_papers)}/20] Cached: {title[:70]}")
                continue
                
    # Download
    success = False
    size = 0
    for url in p.get("pdf_urls", []):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10, context=ssl_ctx) as resp:
                data = resp.read()
                if len(data) > 30000 and (b"%PDF" in data[:1024]):
                    idx_pdf = data.find(b"%PDF")
                    if idx_pdf != -1:
                        data = data[idx_pdf:]
                    with open(target_path, "wb") as f_out:
                        f_out.write(data)
                    success = True
                    size = len(data)
                    break
        except Exception as e:
            pass
            
    if success:
        verified_papers.append({
            "number": len(verified_papers) + 1,
            "title": title,
            "year": year,
            "source": p.get("source", "Academic Publication"),
            "authors": p.get("authors", []),
            "doi": p.get("doi"),
            "pdf_filename": pdf_filename,
            "pdf_size_kb": size // 1024,
            "abstract": p.get("abstract", "")
        })
        print(f"[{len(verified_papers)}/20] Downloaded: {title[:70]} ({size//1024} KB)")

print(f"\nFinal count of verified student burnout papers: {len(verified_papers)}")
with open(os.path.join(OUT_DIR, "verified_papers.json"), "w", encoding="utf-8") as f:
    json.dump(verified_papers, f, indent=2, ensure_ascii=False)
