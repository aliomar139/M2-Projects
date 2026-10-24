"""Try public publisher PDF links; accept only original PDFs with matching identity."""
import io,re,json,hashlib,concurrent.futures,logging
from urllib.parse import quote
from pathlib import Path
from pypdf import PdfReader
from collect_surveys import DATA, resolve_source, ROOT,LR,SURVEYS,rows,write_csv,get
logging.getLogger('pypdf').setLevel(logging.ERROR)

def recover(r):
    r=dict(r);logs=[]
    if r['pdf_file'] or r['xml_file']:return r,logs
    doi=r['doi'];meta=None
    p=ROOT/'data/audit/source_metadata'/f"{int(r['legacy_rank']):03d}.json" if r['legacy_rank'] else None
    try:
        if p and p.exists():meta=json.loads(p.read_text(encoding='utf-8'))['message']
        elif doi:meta=get('https://api.crossref.org/works/'+quote(doi,safe='')).json()['message']
    except Exception as exc:logs.append({'paper_id':r['paper_id'],'url':'Crossref','status':str(exc),'identity':'not_checked'})
    urls=[]
    if meta:
        urls += [x['URL'] for x in meta.get('link',[]) if 'pdf' in x.get('content-type','').lower()]
        urls += [x['URL'] for x in meta.get('link',[]) if 'pdf' in x.get('URL','').lower()]
    if doi.startswith(('10.1007/','10.1186/')):urls.append('https://link.springer.com/content/pdf/'+doi+'.pdf')
    elif doi.startswith('10.1002/'):urls.append('https://onlinelibrary.wiley.com/doi/pdfdirect/'+doi)
    elif doi.startswith('10.1177/'):urls.append('https://journals.sagepub.com/doi/pdf/'+doi)
    for url in list(dict.fromkeys(urls))[:3]:
        try:
            # Short bounded attempt; no authentication or access-control workarounds.
            import requests
            response=requests.get(url,timeout=15,headers={'User-Agent':'OrthopedicThesisReviewAudit/1.1'})
            response.raise_for_status();raw=response.content
            if not raw.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
            reader=PdfReader(io.BytesIO(raw));first=' '.join((p.extract_text() or '') for p in reader.pages[:2]);compact=re.sub(r'\s+','',first).lower()
            if doi.lower() not in compact:raise ValueError('DOI not located in first two pages; manual identity check required')
            if re.search(r'Top\s+100\s+Orthopedic\s+AI',first,re.I):raise ValueError('Generated summary marker')
            dest=SURVEYS/'sources'/(r['paper_id']+'.pdf');dest.write_bytes(raw);r['pdf_file']=str(dest.relative_to(LR)).replace('\\','/')
            r['source_status']='publisher_pdf_doi_verified';r['source_url']=url;r['source_error']=''
            logs.append({'paper_id':r['paper_id'],'url':url,'status':'original_pdf_saved','identity':'DOI in first two PDF pages; SHA256 '+hashlib.sha256(raw).hexdigest()});break
        except Exception as exc:logs.append({'paper_id':r['paper_id'],'url':url,'status':str(exc),'identity':'not_accepted'})
    return r,logs

def main():
    reg=rows(SURVEYS/'survey_registry.csv')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:result=list(pool.map(recover,reg))
    reg=[r for r,_ in result];logs=[x for _,rs in result for x in rs]
    write_csv(SURVEYS/'survey_registry.csv',reg)
    if logs:write_csv(SURVEYS/'publisher_retrieval_log.csv',logs)
    queue=[{'paper_id':r['paper_id'],'title':r['title'],'doi':r['doi'],'pmid':r['pmid'],'publisher_url':'https://doi.org/'+r['doi'],'reason':r['source_error'] or 'No publicly retrievable verified main text; see publisher retrieval log'} for r in reg if not(r['xml_file'] or r['pdf_file'])]
    if queue:write_csv(SURVEYS/'retrieval_queue.csv',queue)
    summary={'working_library_records':len(reg),'orthopedic_stream':sum(r['stream'].startswith('orthopedic') for r in reg),'cross_domain_context':sum(r['stream'].startswith('cross_domain') for r in reg),'original_pdf_copies':sum(bool(r['pdf_file']) for r in reg),'doi_verified_xml_copies':sum(bool(r['xml_file']) for r in reg),'records_with_main_text':sum(bool(r['xml_file'] or r['pdf_file']) for r in reg),'metadata_or_abstract_only':len(queue),'final_systematic_inclusions':'not determined'}
    (DATA/'library_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
