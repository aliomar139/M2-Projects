"""Targeted novelty checks: a zero hit is not proof of novelty."""
import json,time,xml.etree.ElementTree as ET
from urllib.parse import urlencode
from collect_surveys import DATA, resolve_source, ROOT,LR,DATE,DOMAIN,CUTOFF,get,parse,write_csv

QUERIES={
 'N1_identification_gate': '(causal[Title/Abstract] OR counterfactual[Title/Abstract]) AND (agentic[Title/Abstract] OR "large language model"[Title/Abstract] OR "large language models"[Title/Abstract]) AND (positivity[Title/Abstract] OR overlap[Title/Abstract] OR identifiability[Title/Abstract])',
 'N2_dual_provenance': '(treatment[Title/Abstract] OR recommendation[Title/Abstract]) AND (provenance[Title/Abstract] OR traceability[Title/Abstract] OR citation[Title/Abstract]) AND (causal[Title/Abstract] OR "treatment effect"[Title/Abstract])',
 'N3_equivalence_uncertainty': '(treatment[Title/Abstract]) AND ("near-optimal"[Title/Abstract] OR equivalence[Title/Abstract] OR "equivalent treatments"[Title/Abstract]) AND (preferences[Title/Abstract] OR uncertainty[Title/Abstract] OR abstention[Title/Abstract])',
 'N4_extraction_stability': '("language model"[Title/Abstract] OR "language models"[Title/Abstract] OR agentic[Title/Abstract]) AND (extraction[Title/Abstract] OR handoff[Title/Abstract]) AND (robustness[Title/Abstract] OR perturbation[Title/Abstract] OR stability[Title/Abstract])',
 'N5_orchestration_controls': '("multi-agent"[Title/Abstract] OR "multiagent"[Title/Abstract]) AND (ablation[Title/Abstract] OR "single-agent"[Title/Abstract] OR "single agent"[Title/Abstract])',
 'N6_update_stability': '(policy[Title/Abstract] OR recommendation[Title/Abstract]) AND ("temporal drift"[Title/Abstract] OR "model update"[Title/Abstract] OR "guideline update"[Title/Abstract] OR "guideline updates"[Title/Abstract])',
 'N7_override_feedback': '("treatment decision"[Title/Abstract] OR "decision support"[Title/Abstract]) AND (override[Title/Abstract] OR "feedback loop"[Title/Abstract])',
}

def main():
    folder=ROOT/'data/searches/novelty';folder.mkdir(exist_ok=True);log=[];records={};base='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    for key,q in QUERIES.items():
        query=f'({DOMAIN}) AND ({q}) AND {CUTOFF}';params={'db':'pubmed','term':query,'retmode':'json','retmax':9999}
        p=folder/(key+'_esearch.json')
        if not p.exists():p.write_text(get(base+'esearch.fcgi',params=params).text,encoding='utf-8');time.sleep(.4)
        d=json.loads(p.read_text(encoding='utf-8'))['esearchresult'];ids=d['idlist']
        if int(d['count'])!=len(ids):raise ValueError('Incomplete search export')
        log.append({'query_id':key,'date':DATE,'database':'PubMed via E-utilities','query':query,'hits':d['count'],'pmids':'; '.join(ids),'interpretation':'Targeted terminology check only; zero hits do not prove no prior study','url':base+'esearch.fcgi?'+urlencode(params)})
        for off in range(0,len(ids),50):
            p=folder/f'{key}_{off:04d}.xml'
            if not p.exists():p.write_bytes(get(base+'efetch.fcgi',params={'db':'pubmed','id':','.join(ids[off:off+50]),'retmode':'xml'}).content);time.sleep(.4)
            for a in ET.fromstring(p.read_bytes()).findall('PubmedArticle'):
                r=parse(a);r['source_queries']=key
                if r['pmid'] not in records:records[r['pmid']]=r
                else:records[r['pmid']]['source_queries']+='; '+key
    write_csv(DATA/'novelty_search_log.csv',log)
    if records:write_csv(DATA/'novelty_search_matches.csv',list(records.values()))
    print(json.dumps([{k:r[k] for k in ['query_id','hits','pmids']} for r in log],indent=2))

if __name__=='__main__':main()
