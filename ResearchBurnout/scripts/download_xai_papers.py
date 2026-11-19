import json
import os
import re
import urllib.request
import urllib.parse
import ssl
import time

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
OUT_DIR = os.path.join(ROOT_DIR, "ExplainableAI_Student_Burnout_Papers")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
os.makedirs(PDF_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Load candidates
candidates = []
with open(os.path.join(ROOT_DIR, "candidates_dump.json"), "r", encoding="utf-8") as f:
    candidates.extend(json.load(f))

pmc_file = os.path.join(ROOT_DIR, "pmc_dump.json")
if os.path.exists(pmc_file):
    with open(pmc_file, "r", encoding="utf-8") as f:
        candidates.extend(json.load(f))

print(f"Total candidates across dumps: {len(candidates)}")

def clean_title(title):
    return re.sub(r'\s+', ' ', title).strip()

def sanitize_filename(name):
    s = re.sub(r'[\\/*?:"<>|]', "", name)
    s = re.sub(r'\s+', " ", s).strip()
    if len(s) > 100:
        s = s[:100].rstrip()
    return s

# Deduplicate candidates
seen_titles = set()
unique_candidates = []
for c in candidates:
    t = clean_title(c.get("title", ""))
    tl = t.lower()
    if not t or tl in seen_titles:
        continue
    seen_titles.add(tl)
    c["title"] = t
    unique_candidates.append(c)

print(f"Unique candidates: {len(unique_candidates)}")

def score_paper(p):
    text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
    score = 0
    year = p.get("year")
    if not year or year < 2024:
        return -500
    
    # Target topic keywords
    title_lower = p.get("title", "").lower()
    
    # Direct matches in title
    if "burnout" in title_lower:
        score += 80
    if "student" in title_lower or "academic" in title_lower or "college" in title_lower or "adolescent" in title_lower:
        score += 60
    if "explainable" in title_lower or "xai" in title_lower or "interpretable" in title_lower or "shap" in title_lower or "lime" in title_lower:
        score += 70
    if "predict" in title_lower or "prediction" in title_lower or "detection" in title_lower or "warning" in title_lower or "modeling" in title_lower or "machine learning" in title_lower:
        score += 50
        
    # Matches in text / abstract
    if "burnout" in text:
        score += 40
    if any(k in text for k in ["student", "academic", "university", "college", "school", "medical student", "undergraduate"]):
        score += 30
    if any(k in text for k in ["explainable", "interpretability", "interpretable", "shap", "lime", "xai", "feature importance", "decision tree"]):
        score += 40
    if any(k in text for k in ["predict", "prediction", "predicting", "machine learning", "deep learning", "xgboost", "random forest", "lightgbm"]):
        score += 30
        
    # Check if PDF URLs are present
    if p.get("pdf_urls") and len(p["pdf_urls"]) > 0:
        score += 50
    else:
        score -= 20
        
    return score

scored = []
for p in unique_candidates:
    s = score_paper(p)
    if s > 0:
        scored.append((s, p))

scored.sort(key=lambda x: x[0], reverse=True)
print(f"Candidates with score > 0: {len(scored)}")

def try_download_pdf(url, dest_path):
    # Try direct download with custom headers
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/pdf,application/octet-stream,*/*",
        "Referer": "https://scholar.google.com/"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25, context=ssl_context) as resp:
            content = resp.read()
            if len(content) < 25000:
                return False, f"File too small ({len(content)} bytes)"
            
            # Check for PDF signature
            idx = content.find(b"%PDF-")
            if idx == -1 or idx > 500:
                return False, "No valid %PDF- magic bytes found"
            
            # Trim prefix if any
            if idx > 0:
                content = content[idx:]
                
            with open(dest_path, "wb") as f:
                f.write(content)
            return True, len(content)
    except Exception as e:
        return False, str(e)

downloaded_papers = []

for idx, (score, p) in enumerate(scored):
    if len(downloaded_papers) >= 20:
        break
    
    title = p["title"]
    year = p["year"]
    pdf_urls = p.get("pdf_urls", [])
    
    # If no direct pdf_url, check if doi can be converted or if arxiv
    if not pdf_urls and p.get("doi"):
        doi = p["doi"]
        if "arxiv" in doi.lower():
            arxiv_id = doi.split("arXiv.")[-1]
            pdf_urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
            
    if not pdf_urls:
        continue
        
    clean_name = sanitize_filename(f"{year} - {title}")
    pdf_filename = f"{clean_name}.pdf"
    target_path = os.path.join(PDF_DIR, pdf_filename)
    
    success = False
    downloaded_size = 0
    used_url = ""
    
    for url in pdf_urls:
        print(f"Attempting download for #{len(downloaded_papers)+1}: {title[:60]}... from {url[:50]}...")
        ok, res = try_download_pdf(url, target_path)
        if ok:
            success = True
            downloaded_size = res
            used_url = url
            print(f" -> SUCCESS ({downloaded_size // 1024} KB)")
            break
        else:
            print(f" -> Failed: {res}")
            
    if success:
        downloaded_papers.append({
            "number": len(downloaded_papers) + 1,
            "title": title,
            "year": year,
            "source": p.get("source", "Academic Publication"),
            "authors": p.get("authors", []),
            "doi": p.get("doi"),
            "pdf_filename": pdf_filename,
            "pdf_relpath": f"./pdfs/{pdf_filename}",
            "pdf_size_kb": downloaded_size // 1024,
            "pdf_url": used_url,
            "oa_url": p.get("oa_url"),
            "abstract": p.get("abstract", "")
        })
    time.sleep(0.5)

print(f"\nSuccessfully downloaded {len(downloaded_papers)} / 20 papers!")

# Save downloaded metadata
metadata_path = os.path.join(OUT_DIR, "papers_metadata.json")
with open(metadata_path, "w", encoding="utf-8") as f:
    json.dump(downloaded_papers, f, indent=2, ensure_ascii=False)

print(f"Saved metadata to {metadata_path}")
