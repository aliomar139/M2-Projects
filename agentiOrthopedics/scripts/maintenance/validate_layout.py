"""Validate local navigation, retained source hashes, catalogs and scientific counts."""
import csv, hashlib, json, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from repo_paths import resolve_source

def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    errors=[];checked_links=0
    for p in ROOT.rglob('*.md'):
        for uri in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8-sig')):
            uri=uri.strip('<>')
            if re.match(r'^(?:https?:|mailto:|plugin:|app:|#)',uri):continue
            checked_links+=1
            if not (p.parent/unquote(uri.split('#')[0])).exists():errors.append(f'Broken link: {p.relative_to(ROOT)} -> {uri}')
    log=json.loads((ROOT/'data/maintenance/reorganization.json').read_text(encoding='utf-8'))
    source_hashes=0
    for item in log['items']:
        if Path(item['old']).suffix.lower() not in ('.pdf','.xml','.xlsx'):continue
        p=resolve_source(ROOT/item.get('canonical',item['new']))
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:
            errors.append('Retained source hash differs: '+item['old'])
        source_hashes+=1
    registry=rows(ROOT/'LR/Surveys/survey_registry.csv');dims=rows(ROOT/'LR/Surveys/dimensions.csv')
    for r in registry:
        for k in ('pdf_file','xml_file','reader_file'):
            if r[k] and not (ROOT/'LR'/r[k]).is_file():errors.append('Missing survey source: '+r[k])
        if r['xml_file']:
            doi=[(x.text or '').lower() for x in ET.parse(ROOT/'LR'/r['xml_file']).getroot().findall('./front/article-meta/article-id') if x.attrib.get('pub-id-type')=='doi']
            if r['doi'].lower() not in doi:errors.append('XML identity mismatch: '+r['paper_id'])
    catalog=rows(ROOT/'papers/corpus/catalog.csv');manifest=rows(ROOT/'papers/corpus/manifest.csv')
    for r in manifest:
        if not resolve_source(ROOT/'papers/corpus'/r['file_name']).is_file():errors.append('Unresolved legacy file: '+r['rank'])
    for r in catalog:
        for k in ('main_text_path','reader_path','original_download_path','audit_text_path'):
            if r[k] and not (ROOT/r[k]).is_file():errors.append('Broken catalog path: '+r[k])
    for r in rows(ROOT/'data/audit/second_pass_matrix.csv'):
        if r['source_path'] and not (ROOT/r['source_path']).is_file():errors.append('Broken extraction source: '+r['source_path'])
    expected={('85 library records',len(registry),85),('100 legacy citations',len(catalog),100),('dimension cells',len(dims),3485),('unique dimension cells',len({(r['paper_id'],r['dimension_code']) for r in dims}),3485)}
    for label,actual,wanted in expected:
        if actual!=wanted:errors.append(f'{label}: {actual} != {wanted}')
    counts=json.loads((ROOT/'data/reviews/prisma_counts.json').read_text(encoding='utf-8'))
    if counts['combined_search_occurrences']-counts['duplicate_occurrences_removed']!=counts['combined_search_unique_pmids']:errors.append('PRISMA arithmetic mismatch')
    if counts['combined_search_unique_pmids']!=1839:errors.append('Scientific search total changed')
    syntax=0
    for p in (ROOT/'scripts').rglob('*.py'):
        try:compile(p.read_text(encoding='utf-8'),str(p),'exec');syntax+=1
        except SyntaxError as exc:errors.append(str(exc))
    caches=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.pyc')]
    if caches:errors.append('Unexpected Python caches: '+str(caches))
    report={'date':'2026-10-24','local_links_checked':checked_links,'retained_source_hash_checks':source_hashes,
            'script_syntax_checks':syntax,'survey_records':len(registry),'survey_main_text_available':sum(bool(r['pdf_file'] or r['xml_file']) for r in registry),
            'legacy_citations':len(catalog),'legacy_main_text_available':sum(bool(r['main_text_path']) for r in catalog),
            'dimension_cells':len(dims),'prisma_unique_pmids':counts['combined_search_unique_pmids'],'errors':errors,'status':'passed' if not errors else 'failed'}
    (ROOT/'data/maintenance/validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
