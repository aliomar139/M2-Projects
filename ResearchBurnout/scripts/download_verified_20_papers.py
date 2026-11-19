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

# Filter papers from 2024 to 2026
recent = [c for c in candidates if c.get("year") and c["year"] >= 2024 and c.get("pdf_urls")]

print(f"Candidates with PDF URLs from 2024-2026: {len(recent)}")

# Rank by relevance
def relevance(p):
    text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
    score = 0
    t = p.get("title", "").lower()
    
    if "burnout" in t:
        score += 50
    if "student" in t or "academic" in t or "college" in t:
        score += 40
    if "explainable" in t or "xai" in t or "shap" in t or "lime" in t or "interpretable" in t:
        score += 40
    if "predict" in t or "machine learning" in t or "deep learning" in t:
        score += 20
        
    if "burnout" in text:
        score += 20
    if "student" in text or "academic" in text:
        score += 15
    if "explainable" in text or "interpret" in text or "shap" in text or "lime" in text:
        score += 20
    if "predict" in text:
        score += 10
        
    return score

recent.sort(key=relevance, reverse=True)

downloaded = []

# Check existing downloaded files
for fname in os.listdir(PDF_DIR):
    if fname.endswith(".pdf"):
        fpath = os.path.join(PDF_DIR, fname)
        if os.path.getsize(fpath) > 30000:
            print(f"Already existing valid PDF: {fname} ({os.path.getsize(fpath)//1024} KB)")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream,*/*"
}

for i, p in enumerate(recent):
    title = clean_title(p["title"])
    year = p["year"]
    clean_name = sanitize_filename(f"{year} - {title}")
    pdf_filename = f"{clean_name}.pdf"
    target_path = os.path.join(PDF_DIR, pdf_filename)
    
    # Check if already downloaded
    if os.path.exists(target_path) and os.path.getsize(target_path) > 30000:
        downloaded.append((p, pdf_filename, os.path.getsize(target_path)))
        print(f"[{len(downloaded)}/20] Cached: {title[:70]}")
        if len(downloaded) >= 20:
            break
        continue
        
    # Try downloading
    success = False
    size = 0
    for url in p.get("pdf_urls", []):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8, context=ssl_ctx) as resp:
                data = resp.read()
                if len(data) > 30000 and (b"%PDF" in data[:1024]):
                    idx = data.find(b"%PDF")
                    if idx != -1:
                        data = data[idx:]
                    with open(target_path, "wb") as out_f:
                        out_f.write(data)
                    success = True
                    size = len(data)
                    break
        except Exception as e:
            # print error briefly
            pass
            
    if success:
        downloaded.append((p, pdf_filename, size))
        print(f"[{len(downloaded)}/20] Downloaded: {title[:70]} ({size//1024} KB)")
        if len(downloaded) >= 20:
            break

print(f"\nTotal verified downloaded papers: {len(downloaded)}")
