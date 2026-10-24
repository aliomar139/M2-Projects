"""Search review literature and preserve source metadata. Does not claim eligibility."""
import csv, json, re, time, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlencode
import requests
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from repo_paths import resolve_source

ROOT=Path(__file__).resolve().parents[2]
LR=ROOT/'LR'; SURVEYS=LR/'Surveys'; DATA=ROOT/'data/reviews'; RAW=ROOT/'data/searches/reviews'
DATE='2026-10-23'
CUTOFF='("1800/01/01"[Date - Publication] : "2026/10/23"[Date - Publication])'
DOMAIN='("Orthopedics"[MeSH Terms] OR "Orthopedic Procedures"[MeSH Terms] OR "Arthroplasty"[MeSH Terms] OR "Osteoarthritis"[MeSH Terms] OR orthop*[Title/Abstract] OR arthroplast*[Title/Abstract] OR osteoarthritis[Title/Abstract] OR musculoskeletal[Title/Abstract] OR "spine surgery"[Title/Abstract] OR "spine care"[Title/Abstract] OR "hip arthroscopy"[Title/Abstract])'
REVIEW='(Review[Publication Type] OR "systematic review"[Title] OR "scoping review"[Title] OR "narrative review"[Title] OR survey[Title] OR "literature review"[Title])'
QUERIES={
 'R1_ai_treatment_reviews': f'{DOMAIN} AND ("Artificial Intelligence"[MeSH Terms] OR "Machine Learning"[MeSH Terms] OR "artificial intelligence"[Title/Abstract] OR "machine learning"[Title/Abstract] OR "large language model"[Title/Abstract] OR "large language models"[Title/Abstract] OR "clinical decision support"[Title/Abstract]) AND (treatment[Title/Abstract] OR intervention*[Title/Abstract] OR decision*[Title/Abstract] OR rehabilitation[Title/Abstract] OR "surgical planning"[Title/Abstract] OR outcome*[Title/Abstract]) AND {REVIEW}',
 'R2_causal_reviews': f'{DOMAIN} AND ("causal inference"[Title/Abstract] OR "causal machine learning"[Title/Abstract] OR "target trial"[Title/Abstract] OR "treatment effect heterogeneity"[Title/Abstract] OR "individualized treatment rule"[Title/Abstract] OR "individualised treatment rule"[Title/Abstract]) AND {REVIEW}',
 'R3_orthopedic_agent_reviews': f'{DOMAIN} AND (agentic[Title/Abstract] OR "multi-agent"[Title/Abstract] OR "AI agents"[Title/Abstract] OR "artificial intelligence agents"[Title/Abstract]) AND {REVIEW}',
}

def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write_csv(p,data):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
def get(url,**kw):
    for attempt in range(3):
        try:
            r=requests.get(url,timeout=55,headers={'User-Agent':'OrthopedicThesisReviewAudit/1.1'},**kw)
            if r.status_code not in (429,500,502,503) or attempt==2: r.raise_for_status();return r
        except requests.RequestException:
            if attempt==2:raise
        time.sleep(1+attempt)
def plain(e):return ' '.join(''.join(e.itertext()).split()) if e is not None else ''
def parse(a):
    ids={e.attrib.get('IdType'):e.text for e in a.findall('./PubmedData/ArticleIdList/ArticleId')}
    pubdate=plain(a.find('./MedlineCitation/Article/Journal/JournalIssue/PubDate'))
    authors=[' '.join(filter(None,[x.findtext('ForeName'),x.findtext('LastName'),x.findtext('CollectiveName')])) for x in a.findall('./MedlineCitation/Article/AuthorList/Author')]
    notes=[x.attrib.get('RefType','')+': '+plain(x) for x in a.findall('./MedlineCitation/CommentsCorrectionsList/CommentsCorrections')]
    return {'pmid':a.findtext('./MedlineCitation/PMID',''),'pmcid':ids.get('pmc',''),'doi':ids.get('doi',''),
            'title':plain(a.find('./MedlineCitation/Article/ArticleTitle')),'authors':'; '.join(authors),
            'journal':plain(a.find('./MedlineCitation/Article/Journal/Title')),'pubdate':pubdate,
            'publication_types':'; '.join(plain(x) for x in a.findall('./MedlineCitation/Article/PublicationTypeList/PublicationType')),
            'abstract':'\n'.join((x.attrib.get('Label','')+': ' if x.attrib.get('Label') else '')+plain(x) for x in a.findall('./MedlineCitation/Article/Abstract/AbstractText')),
            'corrections_or_retractions':'; '.join(notes),'source_queries':''}

def main():
    RAW.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=True);SURVEYS.mkdir(parents=True,exist_ok=True)
    log=[]; found={};base='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    for key,q in QUERIES.items():
        query=f'({q}) AND {CUTOFF}'
        params={'db':'pubmed','term':query,'retmode':'json','retmax':9999,'sort':'pub date'}
        path=RAW/(key+'_esearch.json')
        if not path.exists():path.write_text(get(base+'esearch.fcgi',params=params).text,encoding='utf-8');time.sleep(.4)
        result=json.loads(path.read_text(encoding='utf-8'))['esearchresult'];ids=result['idlist']
        if int(result['count'])!=len(ids):raise ValueError('Search exceeds export limit; pagination required')
        log.append({'search_id':key,'date':DATE,'database':'PubMed','platform':'NCBI E-utilities','query':query,'total_hits':result['count'],'exported_records':len(ids),'filter':'Publication date through 2026-10-23; no language filter','url':base+'esearch.fcgi?'+urlencode(params)})
        for start in range(0,len(ids),75):
            path=RAW/f'{key}_efetch_{start:04d}.xml'
            if not path.exists():path.write_bytes(get(base+'efetch.fcgi',params={'db':'pubmed','id':','.join(ids[start:start+75]),'retmode':'xml'}).content);time.sleep(.4)
            for a in ET.fromstring(path.read_bytes()).findall('PubmedArticle'):
                r=parse(a)
                if r['pmid'] in found:found[r['pmid']]['source_queries']+='; '+key
                else:r['source_queries']=key;found[r['pmid']]=r
    write_csv(DATA/'review_search_log.csv',log)
    write_csv(DATA/'review_search_candidates.csv',list(found.values()))
    # Parse earlier saved PubMed records to retain native types, PMC IDs and corrections.
    all_records=dict(found)
    for p in (ROOT/'data/searches/first_pass').glob('*efetch_*.xml'):
        for a in ET.fromstring(p.read_bytes()).findall('PubmedArticle'):
            r=parse(a)
            if r['pmid'] not in all_records:r['source_queries']='prior_'+p.name.split('_efetch')[0];all_records[r['pmid']]=r
    p=ROOT/'data/audit/additional_sources/pubmed_records.xml'
    for a in ET.fromstring(p.read_bytes()).findall('PubmedArticle'):
        r=parse(a)
        if r['pmid'] not in all_records:r['source_queries']='prior_targeted_source';all_records[r['pmid']]=r
    write_csv(DATA/'pubmed_source_records.csv',list(all_records.values()))
    summary={'date':DATE,'new_search_occurrences':sum(int(x['total_hits']) for x in log),'new_search_unique_pmids':len(found),'new_search_repeat_occurrences':sum(int(x['total_hits']) for x in log)-len(found),'merged_pubmed_metadata_records':len(all_records),'new_queries':[{k:r[k] for k in ['search_id','total_hits']} for r in log]}
    (DATA/'search_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
