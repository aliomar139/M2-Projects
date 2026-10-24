"""Assemble a bounded working survey library with verified original-source copies."""
import csv, json, re, shutil, hashlib, html, concurrent.futures, xml.etree.ElementTree as ET
from pathlib import Path
from collect_surveys import DATA, resolve_source, ROOT, LR, SURVEYS, rows, write_csv, get, plain

SELECTED=set('42757394 42791908 42793474 42686880 42824522 41407055 42739558 42597887 42536128 42506117 42529139 42343897 42278988 42245303 42101555 42122313 41973342 41738015 41827166 41490410 41749766 41720113 41174934 41568289 41607969 41103258 41346991 41245724 41088452 41127763 40838224 40405922 39502973 39199775 39204872 38991098 38712416 38466797 37968370 37937083 35491420 35455625 34522738 33288388 33323681 32797983 31994752 42896011 42287372 42383711 33933587 34305383 33198106 21750352 41536317 41614143 41245704 41933417 26667939 42322047 42879167 42851913'.split())
LEGACY=set([2,3,7,8,15,18,19,26,28,32,33,34,35,37,38,43,44,46,47,48,49,52,53,64,68,69,70,85,96,99])
CONTEXT={64,68,69,70,85}
XLINK='{http://www.w3.org/1999/xlink}href'

def normdoi(x):return x.lower().strip().removeprefix('https://doi.org/')
def build_records():
    records=rows(DATA/'pubmed_source_records.csv'); bydoi={normdoi(r['doi']):r for r in records if r['doi']};bypmid={r['pmid']:r for r in records}
    manifest=rows(ROOT/'papers/corpus/manifest.csv');audit={r['rank']:r for r in rows(ROOT/'data/audit/corpus_audit.csv')}
    picked={}
    for pmid in SELECTED:
        if pmid not in bypmid:raise ValueError('Selected PMID not harvested: '+pmid)
        r=dict(bypmid[pmid]);r['legacy_rank']='';r['stream']='orthopedic_review_working_selection';picked['PMID_'+pmid]=r
    for m in manifest:
        if int(m['rank']) not in LEGACY:continue
        key='PMID_'+str(int(float(m['pmid']))) if m['pmid'] and m['pmid'].lower()!='nan' else 'LEGACY_'+m['rank'].zfill(3)
        record=bydoi.get(normdoi(m['doi'])) or bypmid.get(key.removeprefix('PMID_'))
        if not record:
            record={'pmid':key.removeprefix('PMID_') if key.startswith('PMID_') else '', 'pmcid':m['pmcid'],'doi':m['doi'],'title':m['title'],'authors':m['authors'],'journal':m['journal'],'pubdate':m['year'],'publication_types':'legacy_record_type_requires_confirmation','abstract':'','corrections_or_retractions':'','source_queries':'legacy_manifest'}
        record=dict(record);record['legacy_rank']=m['rank'];record['stream']='cross_domain_methodological_context' if int(m['rank']) in CONTEXT else 'orthopedic_review_working_selection'
        # DOI is authoritative for merging an already selected PMID.
        old=next((k for k,v in picked.items() if normdoi(v['doi'])==normdoi(record['doi']) and record['doi']),None)
        picked[old or key]=record
    # Add general clinical-agent review explicitly as methodological context.
    if '40909853' in bypmid:
        r=dict(bypmid['40909853']);r.update(legacy_rank='',stream='cross_domain_methodological_context');picked['PMID_40909853']=r
    return picked,manifest,audit

def source_for(pair,manifest,audit):
    pid,r=pair;r=dict(r);folder=SURVEYS/'sources';r.update(paper_id=pid,pdf_file='',xml_file='',reader_file='',source_status='abstract_or_metadata_only',source_url='',source_error='',xml_identity='not_checked')
    rank=r['legacy_rank'];m=next((m for m in manifest if m['rank']==rank),None)
    existing_pdf=folder/(pid+'.pdf')
    if existing_pdf.exists():
        from pypdf import PdfReader
        first=' '.join((p.extract_text() or '') for p in PdfReader(existing_pdf).pages[:2])
        if r['doi'].lower() in re.sub(r'\s+','',first).lower():
            r['pdf_file']=str(existing_pdf.relative_to(LR)).replace('\\','/')
            r['source_status']='existing_original_pdf_doi_verified'
    if rank and audit[rank]['document_class']=='publisher_like_pdf_identity_pending':
        p=resolve_source(ROOT/'papers/corpus'/m['file_name']);dest=folder/(pid+'.pdf');
        if p.resolve()!=dest.resolve():shutil.copy2(p,dest)
        r['pdf_file']=str(dest.relative_to(LR)).replace('\\','/');r['source_status']='original_pdf_candidate_identity_from_prior_audit'
    # Prefer archived original XML and validate the main article DOI, not reference-list DOIs.
    candidates=[]
    if rank:candidates.append(ROOT/'data/audit/fulltext_xml'/f'{int(rank):03d}.xml')
    if r['pmid']:candidates.append(ROOT/'data/audit/additional_sources'/(r['pmid']+'.xml'))
    dest=folder/(pid+'.xml');candidates.append(dest)
    raw=None
    for p in candidates:
        p=resolve_source(p)
        if p.exists():raw=p.read_bytes();break
    if raw is None and r['pmcid']:
        url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/{r['pmcid']}/fullTextXML";r['source_url']=url
        try:raw=get(url).content
        except Exception as exc:r['source_error']=str(exc)
    if raw:
        try:
            root=ET.fromstring(raw)
            doi=[normdoi(e.text or '') for e in root.findall('./front/article-meta/article-id') if e.attrib.get('pub-id-type')=='doi']
            if r['doi'] and normdoi(r['doi']) not in doi:raise ValueError('Main article DOI mismatch')
            r['xml_identity']='main_article_doi_match' if r['doi'] else 'no_doi_title_check_pending'
            if r['doi']:
                dest.write_bytes(raw);r['xml_file']=str(dest.relative_to(LR)).replace('\\','/');r['source_status']='original_xml_doi_verified'+('_and_pdf' if r['pdf_file'] else '')
                if not r['source_url'] and r['pmcid']:r['source_url']=f"https://www.ebi.ac.uk/europepmc/webservices/rest/{r['pmcid']}/fullTextXML"
                render_reader(root,folder/(pid+'.html'),r);r['reader_file']=str((folder/(pid+'.html')).relative_to(LR)).replace('\\','/')
        except Exception as exc:r['source_error']=str(exc)
    return r

def render_reader(root,path,r):
    parts=[]
    for abstract in root.findall('./front/article-meta/abstract'):
        parts.append('<h2>Abstract</h2>');parts.append('<p>'+html.escape(plain(abstract))+'</p>')
    body=root.find('./body')
    if body is not None:
        for el in body.iter():
            if el.tag=='title':parts.append('<h2>'+html.escape(plain(el))+'</h2>')
            elif el.tag=='p':parts.append('<p>'+html.escape(plain(el))+'</p>')
            elif el.tag=='table':
                parts.append('<table>')
                for tr in el.findall('.//tr'):
                    parts.append('<tr>'+''.join('<td>'+html.escape(plain(c))+'</td>' for c in tr if c.tag in ('td','th'))+'</tr>')
                parts.append('</table>')
    license_el=root.find('./front/article-meta/permissions/license')
    notice='Readable text/table view of the DOI-verified original XML. Figures, mathematical layout and references may be incomplete here; consult the original XML and publisher version. This is not a newly authored paper.'
    path.write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>'+html.escape(r['title'])+'</title><style>body{max-width:1000px;margin:40px auto;padding:0 24px;font:17px/1.6 Georgia,serif;color:#202d34}aside{font:14px/1.5 system-ui;background:#edf4f4;padding:18px}h1,h2{font-family:system-ui}table{border-collapse:collapse;font:13px/1.4 system-ui}td{border:1px solid #bbb;padding:7px;vertical-align:top}</style><h1>'+html.escape(r['title'])+'</h1><p>'+html.escape(r['authors'])+'</p><aside>'+html.escape(notice)+'<br>Source: <a href="https://doi.org/'+html.escape(r['doi'],quote=True)+'">'+html.escape(r['doi'])+'</a><br>'+html.escape(plain(license_el))+'</aside>'+''.join(parts)+'</html>',encoding='utf-8')

def main():
    (SURVEYS/'sources').mkdir(parents=True,exist_ok=True);(SURVEYS/'records').mkdir(exist_ok=True)
    picked,manifest,audit=build_records()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        result=list(pool.map(lambda x:source_for(x,manifest,audit),sorted(picked.items())))
    for r in result:
        r['review_class']='preprint_review' if r['pmid']=='40909853' else 'systematic_review' if re.search('systematic review',r['title'],re.I) else 'scoping_review' if re.search('scoping review',r['title'],re.I) else 'conceptual_or_methods_guide' if re.search('guide|primer|introduction|application of agentic',r['title'],re.I) else 'narrative_or_other_review_pending_full_method_check'
        r['selection_status']='working_library_not_final_systematic_inclusion'
        pdf=('[PDF](../'+Path(r['pdf_file']).name+')') if False else ''
        links=[]
        for k,label in [('pdf_file','Original PDF candidate'),('xml_file','DOI-verified original XML'),('reader_file','Readable source text/tables')]:
            if r[k]:links.append(f"[{label}](../sources/{Path(r[k]).name})")
        text=f"# {r['title']}\n\nPaper ID: {r['paper_id']}\n\nAuthors: {r['authors']}\n\nJournal/date: {r['journal']}; {r['pubdate']}\n\nDOI: https://doi.org/{r['doi']}\n\nPMID: {r['pmid'] or 'not available'}; PMC: {r['pmcid'] or 'not available'}\n\nStream: {r['stream']}. Type: {r['review_class']}.\n\nStatus: working library; eligibility and appraisal not finalized.\n\nSource status: {r['source_status']}.\n\n"+' | '.join(links)+'\n\nMetadata publication types: '+r['publication_types']+'\n\nCorrection/retraction links: '+(r['corrections_or_retractions'] or 'None in harvested metadata; not an exhaustive integrity check')+'\n\nSee [dimensions](../dimensions.md#'+r['paper_id'].lower()+') for extracted review structure and dimensions.\n'
        (SURVEYS/'records'/(r['paper_id']+'.md')).write_text(text,encoding='utf-8')
    write_csv(SURVEYS/'survey_registry.csv',result)
    summary={'working_library_records':len(result),'orthopedic_stream':sum(r['stream'].startswith('orthopedic') for r in result),'cross_domain_context':sum(r['stream'].startswith('cross_domain') for r in result),'original_pdf_copies':sum(bool(r['pdf_file']) for r in result),'doi_verified_xml_copies':sum(bool(r['xml_file']) for r in result),'records_with_main_text':sum(bool(r['xml_file'] or r['pdf_file']) for r in result),'metadata_or_abstract_only':sum(not(r['xml_file'] or r['pdf_file']) for r in result),'final_systematic_inclusions':'not determined'}
    (DATA/'library_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary,indent=2))
    queue=[{'paper_id':r['paper_id'],'title':r['title'],'doi':r['doi'],'pmid':r['pmid'],'publisher_url':'https://doi.org/'+r['doi'],'reason':r['source_error'] or 'No accessible original main text in current sources'} for r in result if not(r['xml_file'] or r['pdf_file'])]
    if queue:write_csv(SURVEYS/'retrieval_queue.csv',queue)

if __name__=='__main__':main()
