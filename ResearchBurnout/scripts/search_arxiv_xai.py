import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

queries = [
    'all:"student burnout"',
    'all:"academic burnout"',
    'all:"burnout" AND (all:"explainable" OR all:"SHAP")',
    'all:"burnout prediction"',
    '(all:"student" OR all:"students") AND all:"burnout" AND all:"machine learning"',
    'all:"student mental health" AND (all:"explainable" OR all:"SHAP")',
    'all:"academic stress" AND (all:"explainable" OR all:"SHAP" OR all:"interpretable")',
    'all:"burnout" AND (all:"interpretable" OR all:"feature importance")',
    'all:"student well-being" AND all:"machine learning" AND all:"explainable"',
    'all:"dropout prediction" AND all:"burnout"'
]

papers = []
seen = set()

for q in queries:
    url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending'
    req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            tree = ET.fromstring(resp.read())
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in tree.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                if title.lower() in seen:
                    continue
                seen.add(title.lower())
                pub_elem = entry.find('atom:published', ns)
                pub_year = int(pub_elem.text[:4]) if pub_elem is not None else 2024
                id_elem = entry.find('atom:id', ns)
                arxiv_id = id_elem.text.split('/abs/')[-1] if id_elem is not None else ''
                summary_elem = entry.find('atom:summary', ns)
                summary = summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else ''
                authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns) if a.find('atom:name', ns) is not None]
                
                # Check year (2024 - 2026)
                if pub_year >= 2024:
                    papers.append({
                        'title': title,
                        'year': pub_year,
                        'arxiv_id': arxiv_id,
                        'pdf_url': f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                        'abstract': summary,
                        'authors': authors,
                        'source': 'arXiv'
                    })
    except Exception as e:
        print(f"Error querying {q}: {e}")
    time.sleep(0.3)

print(f"Found {len(papers)} candidate papers from 2024-2026 on arXiv.")
with open("arxiv_candidates.json", "w", encoding="utf-8") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)
