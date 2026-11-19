import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError

OUT_DIR = os.path.join(os.getcwd(), "ExplainableAI_Student_Burnout_Papers")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
os.makedirs(PDF_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (mailto:researcher@academic-library.org)"

def sanitize_filename(name):
    # remove invalid filename characters
    s = re.sub(r'[\\/*?:"<>|]', "", name)
    s = re.sub(r'\s+', " ", s).strip()
    if len(s) > 120:
        s = s[:120].rstrip()
    return s

def test_download_pdf(url, output_path):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/pdf,application/octet-stream,*/*"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "")
            data = response.read()
            if len(data) < 15000:
                # too small, probably an error page
                return False, f"File too small ({len(data)} bytes)"
            if not data.startswith(b"%PDF"):
                # sometimes there are leading bytes or html
                idx = data.find(b"%PDF")
                if idx == -1 or idx > 100:
                    return False, f"Not a valid PDF header (got {content_type})"
                data = data[idx:]
            
            with open(output_path, "wb") as f:
                f.write(data)
            return True, len(data)
    except Exception as e:
        return False, str(e)

def search_openalex():
    queries = [
        "explainable AI student burnout",
        "predicting student burnout machine learning",
        "academic burnout explainable machine learning SHAP",
        "interpretable machine learning student burnout",
        "predicting academic burnout machine learning",
        "explainable AI burnout prediction",
        "student burnout prediction SHAP LIME",
        "burnout prediction explainable artificial intelligence",
        "student mental health burnout prediction explainable AI",
        "academic stress burnout prediction machine learning interpretability",
        "student exhaustion prediction machine learning",
        "early detection student burnout explainable"
    ]
    
    candidates = []
    seen_dois = set()
    seen_titles = set()
    
    for q in queries:
        print(f"Searching OpenAlex for: {q}")
        encoded = urllib.parse.quote(q)
        url = f"https://api.openalex.org/works?search={encoded}&filter=is_oa:true,from_publication_date:2024-01-01&per_page=25"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                results = data.get("results", [])
                for item in results:
                    title = item.get("title")
                    if not title:
                        continue
                    clean_t = title.lower().strip()
                    if clean_t in seen_titles:
                        continue
                    seen_titles.add(clean_t)
                    
                    doi = item.get("doi")
                    if doi and doi in seen_dois:
                        continue
                    if doi:
                        seen_dois.add(doi)
                    
                    # Gather PDF URLs
                    pdf_urls = []
                    best_oa = item.get("best_oa_location") or {}
                    if best_oa.get("pdf_url"):
                        pdf_urls.append(best_oa["pdf_url"])
                    
                    pri_loc = item.get("primary_location") or {}
                    if pri_loc.get("pdf_url") and pri_loc["pdf_url"] not in pdf_urls:
                        pdf_urls.append(pri_loc["pdf_url"])
                        
                    for loc in item.get("locations", []):
                        p = loc.get("pdf_url")
                        if p and p not in pdf_urls:
                            pdf_urls.append(p)
                            
                    # OpenAlex landing page or oa_url
                    oa_url = best_oa.get("landing_page_url") or pri_loc.get("landing_page_url")
                    
                    year = item.get("publication_year")
                    source = (best_oa.get("source") or pri_loc.get("source") or {}).get("display_name", "Unknown Source")
                    authors = [a.get("author", {}).get("display_name", "") for a in item.get("authorships", [])]
                    authors = [a for a in authors if a]
                    
                    abstract_inverted = item.get("abstract_inverted_index")
                    abstract = ""
                    if abstract_inverted:
                        # reconstruct abstract
                        word_positions = []
                        for word, positions in abstract_inverted.items():
                            for pos in positions:
                                word_positions.append((pos, word))
                        word_positions.sort()
                        abstract = " ".join(w for _, w in word_positions)
                        
                    candidates.append({
                        "id": item.get("id"),
                        "title": title,
                        "year": year,
                        "source": source,
                        "authors": authors,
                        "doi": doi,
                        "pdf_urls": pdf_urls,
                        "oa_url": oa_url,
                        "abstract": abstract
                    })
        except Exception as e:
            print(f"Error searching OpenAlex: {e}")
        time.sleep(0.3)
    
    return candidates

def search_arxiv():
    queries = [
        'all:"explainable" AND (all:"student burnout" OR all:"academic burnout")',
        'all:"burnout" AND (all:"SHAP" OR all:"explainable AI" OR all:"XAI") AND (all:"student" OR all:"students" OR all:"academic" OR all:"education")',
        'all:"predicting burnout" AND (all:"explainable" OR all:"interpretable")',
        'all:"student mental health" AND all:"burnout" AND all:"explainable"'
    ]
    arxiv_candidates = []
    seen = set()
    for q in queries:
        print(f"Searching arXiv for: {q}")
        url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                xml_data = resp.read().decode("utf-8")
                import xml.etree.ElementTree as ET
                root = ET.fromstring(xml_data)
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                for entry in root.findall("atom:entry", ns):
                    title_elem = entry.find("atom:title", ns)
                    title = title_elem.text.strip().replace("\n", " ") if title_elem is not None else ""
                    if not title or title.lower() in seen:
                        continue
                    seen.add(title.lower())
                    published = entry.find("atom:published", ns)
                    pub_year = int(published.text[:4]) if published is not None else 2024
                    if pub_year < 2024:
                        continue
                    summary_elem = entry.find("atom:summary", ns)
                    abstract = summary_elem.text.strip().replace("\n", " ") if summary_elem is not None else ""
                    id_elem = entry.find("atom:id", ns)
                    arxiv_id = id_elem.text.split("/abs/")[-1] if id_elem is not None else ""
                    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                    authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns) if a.find("atom:name", ns) is not None]
                    
                    arxiv_candidates.append({
                        "id": f"arxiv:{arxiv_id}",
                        "title": title,
                        "year": pub_year,
                        "source": "arXiv",
                        "authors": authors,
                        "doi": f"10.48550/arXiv.{arxiv_id}",
                        "pdf_urls": [pdf_url],
                        "oa_url": f"https://arxiv.org/abs/{arxiv_id}",
                        "abstract": abstract
                    })
        except Exception as e:
            print(f"Error querying arXiv: {e}")
        time.sleep(0.5)
    return arxiv_candidates

if __name__ == "__main__":
    print("Gathering candidates from OpenAlex and arXiv...")
    oa_cands = search_openalex()
    arxiv_cands = search_arxiv()
    all_cands = oa_cands + arxiv_cands
    print(f"Total collected candidate records: {len(all_cands)}")
    
    with open("candidates_dump.json", "w", encoding="utf-8") as f:
        json.dump(all_cands, f, indent=2, ensure_ascii=False)
