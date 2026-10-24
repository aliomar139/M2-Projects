"""Prospective, reproducible PubMed search. Counts belong to this run only."""
import json, time, xml.etree.ElementTree as ET
from urllib.parse import urlencode
from audit_corpus import ROOT, OUT, write_csv
from verify_sources import get, DATE

ORTHO='(orthop*[Title/Abstract] OR arthroplast*[Title/Abstract] OR osteoarthritis[Title/Abstract] OR "musculoskeletal"[Title/Abstract])'
CUTOFF='("1800/01/01"[Date - Publication] : "2026/10/23"[Date - Publication])'
QUERIES={
 'P1_reviews_decision': ORTHO+' AND ("decision support"[Title/Abstract] OR "treatment selection"[Title/Abstract] OR "treatment recommendation"[Title/Abstract]) AND (review[Publication Type] OR review[Title] OR survey[Title])',
 'P2_reviews_causal': ORTHO+' AND ("causal inference"[Title/Abstract] OR "causal machine learning"[Title/Abstract] OR "individualized treatment"[Title/Abstract] OR "individualised treatment"[Title/Abstract]) AND (review[Publication Type] OR review[Title] OR survey[Title])',
 'P3_reviews_agents': '("agentic"[Title/Abstract] OR "multi-agent"[Title/Abstract] OR "AI agents"[Title/Abstract]) AND (clinical[Title/Abstract] OR medicine[Title/Abstract] OR healthcare[Title/Abstract]) AND (review[Publication Type] OR review[Title] OR survey[Title])',
 'P4_primary_treatment_effects': ORTHO+' AND ("causal forest"[Title/Abstract] OR "doubly robust"[Title/Abstract] OR "individualized treatment effect"[Title/Abstract] OR "individualised treatment effect"[Title/Abstract] OR "heterogeneous treatment effect"[Title/Abstract] OR "optimal treatment regime"[Title/Abstract])',
}

def main():
    folder=ROOT/'data/searches/first_pass';folder.mkdir(exist_ok=True)
    log=[]; by_id={}
    for key,query in QUERIES.items():
        full=f'({query}) AND {CUTOFF}'
        params={'db':'pubmed','term':full,'retmode':'json','retmax':1000,'sort':'pub date'}
        base='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
        cache=folder/(key+'_esearch.json')
        if cache.exists(): data=json.loads(cache.read_text(encoding='utf-8'))
        else:
            response=get(base+'esearch.fcgi',params=params)
            cache.write_text(response.text,encoding='utf-8');data=response.json()
        d=data['esearchresult']; ids=d['idlist']
        log.append({'search_id':key,'date':DATE,'source':'PubMed via NCBI E-utilities','query':full,'filters':'Publication date through 2026-10-23; no language filter','total_hits':d['count'],'exported_records':len(ids),'status':'executed','url':base+'esearch.fcgi?'+urlencode(params)})
        time.sleep(.4)
        if ids:
            root=ET.Element('PubmedArticleSet')
            for offset in range(0,len(ids),100):
                chunk=folder/f'{key}_efetch_{offset:04d}.xml'
                if not chunk.exists():
                    response=get(base+'efetch.fcgi',params={'db':'pubmed','id':','.join(ids[offset:offset+100]),'retmode':'xml'})
                    chunk.write_bytes(response.content);time.sleep(.4)
                part=ET.fromstring(chunk.read_bytes())
                for article in part: root.append(article)
            for article in root.findall('.//PubmedArticle'):
                val=lambda p: ' '.join(''.join(article.find(p).itertext()).split()) if article.find(p) is not None else ''
                pmid=val('.//PMID')
                if pmid in by_id: by_id[pmid]['search_ids']+='; '+key; continue
                authors=[' '.join(filter(None,[a.findtext('ForeName'),a.findtext('LastName'),a.findtext('CollectiveName')])) for a in article.findall('.//Author')]
                abstract=' '.join(' '.join(''.join(e.itertext()).split()) for e in article.findall('.//AbstractText'))
                doi='; '.join(e.text or '' for e in article.findall('./PubmedData/ArticleIdList/ArticleId') if e.attrib.get('IdType')=='doi')
                by_id[pmid]={'pmid':pmid,'search_ids':key,'title':val('.//ArticleTitle'),'authors':'; '.join(authors),'journal':val('.//Journal/Title'),'year':val('.//JournalIssue/PubDate/Year') or val('.//PubDate/MedlineDate'),'doi':doi,'publication_types':'; '.join(e.text or '' for e in article.findall('.//PublicationType')),'abstract':abstract,'url':f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/','screening_decision':'pending','exclusion_reason':''}
        time.sleep(.4)
    write_csv(OUT/'pubmed_search_log.csv',log)
    write_csv(OUT/'new_pubmed_candidates.csv',list(by_id.values()))
    print(json.dumps({'searches':[{k:r[k] for k in ['search_id','total_hits','exported_records']} for r in log],'unique_candidates':len(by_id)},indent=2))

if __name__=='__main__': main()
