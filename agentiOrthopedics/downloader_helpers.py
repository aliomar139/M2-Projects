import os
import sys
import re
import time
import json
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.parse import quote

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

def sanitize_filename(name, max_len=60):
    clean = re.sub(r'[\\/*?:"<>|]', '', name)
    clean = re.sub(r'\s+', '_', clean.strip())
    return clean[:max_len].strip('._')

def is_valid_pdf_file(filepath):
    if not os.path.exists(filepath):
        return False
    if os.path.getsize(filepath) < 5000:  # less than 5KB is likely an error page
        return False
    try:
        with open(filepath, 'rb') as f:
            header = f.read(10)
            return header.startswith(b'%PDF')
    except Exception:
        return False

def try_download_pdf(url, output_path, timeout=20):
    if not url:
        return False
    try:
        r = requests.get(url, headers=HEADERS, stream=True, timeout=timeout, allow_redirects=True)
        if r.status_code != 200:
            return False
        
        # Check first chunk
        chunk = next(r.iter_content(1024), b'')
        if not chunk.startswith(b'%PDF'):
            # Some servers send leading whitespace or BOM
            if b'%PDF' not in chunk[:50]:
                return False
        
        with open(output_path, 'wb') as f:
            f.write(chunk)
            for chunk in r.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
                    
        return is_valid_pdf_file(output_path)
    except Exception as e:
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except Exception:
                pass
        return False

# 1. Batch NCBI ID Converter
def get_pmc_ids_batch(dois):
    doi_to_pmc = {}
    doi_to_pmid = {}
    
    # Process in chunks of 50
    for i in range(0, len(dois), 50):
        chunk = dois[i:i+50]
        ids_str = ','.join(chunk)
        url = f"https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={quote(ids_str)}&format=json&email=academic_bot@research.org&tool=agentic_ortho"
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                records = r.json().get('records', [])
                for rec in records:
                    d = rec.get('doi', '').lower().strip()
                    pmcid = rec.get('pmcid')
                    pmid = rec.get('pmid')
                    if d:
                        if pmcid:
                            doi_to_pmc[d] = pmcid
                        if pmid:
                            doi_to_pmid[d] = pmid
        except Exception as e:
            print(f"Error fetching batch PMC IDs: {e}")
        time.sleep(0.5)
    return doi_to_pmc, doi_to_pmid

# 2. Try PMC S3 Open Data
def try_pmc_s3(pmcid, output_path):
    if not pmcid:
        return False
    prefix = f"{pmcid}."
    list_url = f"https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix={prefix}"
    try:
        r = requests.get(list_url, timeout=10)
        if r.status_code == 200 and '<Key>' in r.text:
            root = ET.fromstring(r.text)
            pdf_keys = []
            for elem in root.iter('{http://s3.amazonaws.com/doc/2006-03-01/}Key'):
                if elem.text and elem.text.lower().endswith('.pdf'):
                    pdf_keys.append(elem.text)
            
            # Prioritize main article PDF (e.g., PMCxxxx.1.pdf)
            main_pdfs = [k for k in pdf_keys if f"{pmcid}." in k and not ('sm' in k.lower() or 'supp' in k.lower())]
            target_key = main_pdfs[0] if main_pdfs else (pdf_keys[0] if pdf_keys else None)
            
            if target_key:
                pdf_url = f"https://pmc-oa-opendata.s3.amazonaws.com/{target_key}"
                if try_download_pdf(pdf_url, output_path):
                    return True
    except Exception as e:
        pass
    return False

# 3. Try Unpaywall
def try_unpaywall(doi, output_path):
    if not doi:
        return False
    url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_access@research.edu"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # Try best_oa_location
            best = data.get('best_oa_location') or {}
            pdf_url = best.get('url_for_pdf')
            if pdf_url and try_download_pdf(pdf_url, output_path):
                return True
            
            # Try all oa_locations
            for loc in data.get('oa_locations', []):
                pdf_url = loc.get('url_for_pdf')
                if pdf_url and try_download_pdf(pdf_url, output_path):
                    return True
    except Exception:
        pass
    return False

# 4. Try OpenAlex
def try_openalex(doi, output_path):
    if not doi:
        return False
    url = f"https://api.openalex.org/works/https://doi.org/{doi.lower()}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # Check best_oa_location
            best = data.get('best_oa_location') or {}
            if best.get('pdf_url') and try_download_pdf(best.get('pdf_url'), output_path):
                return True
            
            # Check primary_location
            primary = data.get('primary_location') or {}
            if primary.get('pdf_url') and try_download_pdf(primary.get('pdf_url'), output_path):
                return True
            
            # Check locations
            for loc in data.get('locations', []):
                if loc.get('pdf_url') and try_download_pdf(loc.get('pdf_url'), output_path):
                    return True
    except Exception:
        pass
    return False

# 5. Try Semantic Scholar (arXiv & OA PDF)
def try_semantic_scholar(doi, output_path):
    if not doi:
        return False
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf,externalIds"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()
            ext = data.get('externalIds', {})
            # Check ArXiv
            arxiv_id = ext.get('ArXiv')
            if arxiv_id:
                arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                if try_download_pdf(arxiv_url, output_path):
                    return True
            
            # Check openAccessPdf
            oa_pdf = data.get('openAccessPdf') or {}
            pdf_url = oa_pdf.get('url')
            if pdf_url and try_download_pdf(pdf_url, output_path):
                return True
    except Exception:
        pass
    return False

# 6. Try Europe PMC
def try_europe_pmc(doi, output_path):
    if not doi:
        return False
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"{doi}\"&resultType=core&format=json"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            results = r.json().get('resultList', {}).get('result', [])
            if results:
                ft_list = results[0].get('fullTextUrlList', {}).get('fullTextUrl', [])
                for ft in ft_list:
                    if ft.get('documentStyle') == 'pdf':
                        pdf_url = ft.get('url')
                        if pdf_url and try_download_pdf(pdf_url, output_path):
                            return True
    except Exception:
        pass
    return False

# 7. Try arXiv search by Title
def try_arxiv_by_title(title, output_path):
    clean_title = re.sub(r'[^a-zA-Z0-9 ]', ' ', title).strip()
    words = clean_title.split()[:8]
    query = ' '.join(words)
    url = f"https://export.arxiv.org/api/query?search_query=ti:\"{quote(query)}\"&max_results=1"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and '<entry>' in r.text:
            root = ET.fromstring(r.text)
            for entry in root.iter('{http://www.w3.org/2005/Atom}entry'):
                t_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                id_elem = entry.find('{http://www.w3.org/2005/Atom}id')
                if t_elem is not None and id_elem is not None:
                    found_title = t_elem.text.strip().lower()
                    if clean_title.lower()[:30] in found_title or found_title[:30] in clean_title.lower():
                        arxiv_id = id_elem.text.split('/abs/')[-1]
                        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                        if try_download_pdf(pdf_url, output_path):
                            return True
    except Exception:
        pass
    return False

print("Helper functions ready.")

