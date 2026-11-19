import urllib.request
import urllib.parse
import json
import time

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def search_europe_pmc():
    queries = [
        '("student burnout" OR "academic burnout") AND ("machine learning" OR "explainable" OR "SHAP" OR "XAI") AND (SRC:MED OR SRC:PMC) AND (FIRST_PDATE:[2024-01-01 TO 2026-12-31])',
        'burnout AND ("medical student" OR "nursing student" OR "college student" OR "university student") AND ("machine learning" OR "SHAP" OR "prediction") AND (FIRST_PDATE:[2024-01-01 TO 2026-12-31])'
    ]
    pmc_papers = []
    seen_ids = set()
    for q in queries:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&pageSize=25&resultType=core"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                results = data.get('resultList', {}).get('result', [])
                for r in results:
                    pmcid = r.get('pmcid')
                    title = r.get('title')
                    if not title or title.lower() in seen_ids:
                        continue
                    seen_ids.add(title.lower())
                    year = int(r.get('pubYear', 2024))
                    doi = r.get('doi')
                    author_str = r.get('authorString', '')
                    source = r.get('journalTitle', 'PubMed Central')
                    abstract = r.get('abstractText', '')
                    pdf_urls = []
                    if pmcid:
                        pdf_urls.append(f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf")
                    elif r.get('fullTextUrlList', {}).get('fullTextUrl'):
                        for u in r['fullTextUrlList']['fullTextUrl']:
                            if u.get('documentStyle') == 'pdf':
                                pdf_urls.append(u.get('url'))
                    
                    pmc_papers.append({
                        "id": f"pmc:{pmcid}" if pmcid else f"doi:{doi}",
                        "title": title.rstrip('.'),
                        "year": year,
                        "source": source,
                        "authors": [a.strip() for a in author_str.split(',') if a.strip()],
                        "doi": doi,
                        "pdf_urls": pdf_urls,
                        "oa_url": f"https://europepmc.org/article/PMC/{pmcid}" if pmcid else None,
                        "abstract": abstract
                    })
        except Exception as e:
            print(f"Error querying Europe PMC: {e}")
        time.sleep(0.5)
    print(f"Europe PMC returned: {len(pmc_papers)} papers")
    return pmc_papers

if __name__ == "__main__":
    pmc = search_europe_pmc()
    with open("pmc_dump.json", "w", encoding="utf-8") as f:
        json.dump(pmc, f, indent=2, ensure_ascii=False)
