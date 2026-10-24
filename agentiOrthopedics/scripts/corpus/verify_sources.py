"""Retrieve public bibliographic records and available PMC XML; never overwrite corpus."""
import csv, json, time, re, concurrent.futures, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote
import requests
from audit_corpus import rows, write_csv, ROOT, OUT, resolve_source

DATE='2026-10-23'
HEADERS={'User-Agent':'OrthopedicThesisEvidenceAudit/1.0 (academic literature verification)'}

def get(url, **kwargs):
    response=requests.get(url, headers=HEADERS, timeout=35, **kwargs)
    response.raise_for_status()
    return response

def verify(record):
    rank=record['rank']; doi=record['doi']; pmcid=record['pmcid']
    item={'rank':rank,'manifest_title':record['title'],'manifest_doi':doi,'verification_date':DATE,
          'metadata_status':'not_checked','verified_title':'','verified_authors':'','verified_venue':'',
          'crossref_type':'','published_date':'','online_date':'','print_date':'','title_similarity':'',
          'metadata_url':'','xml_status':'not_available','xml_url':'','xml_title':'','xml_doi':'','notes':''}
    if doi:
        url='https://api.crossref.org/works/'+quote(doi,safe='')
        item['metadata_url']=url
        try:
            response=get(url); data=response.json(); d=data['message']
            (OUT/'source_metadata'/f'{int(rank):03d}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
            date=lambda k: '-'.join(map(str,d.get(k,{}).get('date-parts',[[]])[0]))
            title='; '.join(d.get('title',[]))
            from difflib import SequenceMatcher
            norm=lambda s: re.sub(r'[^a-z0-9]','',s.lower())
            item.update(metadata_status='crossref_record_retrieved',verified_title=title,
                        verified_authors='; '.join(' '.join([a.get('given',''),a.get('family','')]).strip() for a in d.get('author',[])),
                        verified_venue='; '.join(d.get('container-title',[])),crossref_type=d.get('type',''),
                        published_date=date('published'), online_date=date('published-online'),print_date=date('published-print'),
                        title_similarity=round(SequenceMatcher(None,norm(title),norm(record['title'])).ratio(),3))
        except Exception as exc: item.update(metadata_status='crossref_unavailable',notes=str(exc))
    else: item.update(metadata_status='missing_doi')
    if pmcid and pmcid.startswith('PMC'):
        url=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML'
        item['xml_url']=url
        try:
            response=get(url); root=ET.fromstring(response.content)
            title=' '.join(''.join(root.find('.//article-title').itertext()).split())
            dois=[e.text for e in root.findall('.//article-id') if e.attrib.get('pub-id-type')=='doi']
            resolve_source(OUT/'fulltext_xml'/f'{int(rank):03d}.xml').write_bytes(response.content)
            text=[]
            for section in root.findall('.//abstract')+root.findall('.//body'):
                text.append('\n'.join(' '.join(''.join(el.itertext()).split()) for el in section.iter() if el.tag in ('title','p','table')))
            (OUT/'fulltext_xml'/f'{int(rank):03d}.txt').write_text('\n\n'.join(text),encoding='utf-8')
            item.update(xml_status='retrieved_identity_pending',xml_title=title,xml_doi='; '.join(dois))
        except Exception as exc: item.update(xml_status='unavailable',notes=(item['notes']+' | '+str(exc)).strip(' |'))
    return item

def main():
    for folder in ['source_metadata','fulltext_xml']: (OUT/folder).mkdir(exist_ok=True)
    manifest=rows(ROOT/'papers/corpus/manifest.csv')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        result=list(pool.map(verify,manifest))
    write_csv(OUT/'source_verification.csv',result)
    from collections import Counter
    print(json.dumps({'metadata':dict(Counter(x['metadata_status'] for x in result)),
                      'xml':dict(Counter(x['xml_status'] for x in result)),
                      'title_discrepancies':[x['rank'] for x in result if x['title_similarity']!='' and x['title_similarity']<.85]},indent=2))

if __name__=='__main__': main()
