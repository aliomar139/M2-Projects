"""Read-only source audit; writes reproducible review artifacts in this folder."""
import csv, hashlib, json, re, logging
from collections import Counter
from pathlib import Path
from pypdf import PdfReader
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from repo_paths import resolve_source

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'data/audit'

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(path, data):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]))
        w.writeheader(); w.writerows(data)

def main():
    logging.getLogger('pypdf').setLevel(logging.ERROR)
    manifest = rows(ROOT/'papers/corpus/manifest.csv')
    audit = []
    (OUT/'page_text').mkdir(exist_ok=True)
    for record in manifest:
        path = resolve_source(ROOT/'papers/corpus'/record['file_name'])
        item = dict(record)
        item.update(file_exists=path.exists(), pages='', sha256='', document_class='', doi_in_text='', extraction_error='')
        try:
            raw = path.read_bytes()
            reader = PdfReader(path)
            pages = [p.extract_text() or '' for p in reader.pages]
            content = '\n'.join(pages)
            first = '\n'.join(pages[:2])
            # Corpus-specific markers of locally generated dossiers, not publisher originals.
            summary = bool(re.search(r'Top 100 Orthopedic AI|SJR Quartile|Relevance Score|Simple Summary.*Project Context',re.sub(r'\s+',' ',first),re.I))
            item.update(pages=len(pages), sha256=hashlib.sha256(raw).hexdigest(),
                        document_class='local_summary_sheet' if summary else 'publisher_like_pdf_identity_pending',
                        doi_in_text=bool(record['doi'] and record['doi'].lower() in re.sub(r'\s+','',content).lower()))
            item['doi_in_first_two_pages']=bool(record['doi'] and record['doi'].lower() in re.sub(r'\s+','',first).lower())
            if record['rank'] in ('22','44','61'):
                item['document_class']='wrong_document_confirmed'
            if record['rank']=='29': item['document_class']='supplement_only'
            (OUT/'page_text'/f"{int(record['rank']):03d}.txt").write_text('\n\n'.join(f'=== PDF PAGE {i+1} ===\n{t}' for i,t in enumerate(pages)),encoding='utf-8')
        except Exception as exc:
            item['document_class']='unreadable_or_missing'; item['extraction_error']=str(exc)
        audit.append(item)
    write_csv(OUT/'corpus_audit.csv',audit)
    raw_counts={}
    for p in (ROOT/'data/searches/initial').glob('*.csv'):
        r=rows(p)
        raw_counts[p.name]={'rows':len(r),'columns':list(r[0]) if r else []}
    summary={'audit_date':'2026-10-23','manifest_rows':len(manifest),'pdf_files':len(list((ROOT/'papers/corpus').glob('*.pdf'))),
             'document_classes':dict(Counter(a['document_class'] for a in audit)),
             'duplicate_dois':{k:v for k,v in Counter(r['doi'].lower().strip() for r in manifest if r['doi']).items() if v>1},
             'duplicate_file_hashes':{k:v for k,v in Counter(r['sha256'] for r in audit if r['sha256']).items() if v>1},
             'missing_doi_ranks':[r['rank'] for r in manifest if not r['doi']],
             'archive_inventory':raw_counts}
    (OUT/'audit_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
