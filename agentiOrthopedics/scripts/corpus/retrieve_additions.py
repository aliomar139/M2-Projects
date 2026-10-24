"""Save PubMed source records and openly available original texts for key additions."""
import json, time, xml.etree.ElementTree as ET
from audit_corpus import OUT, write_csv, resolve_source
from verify_sources import get

IDS=['38007205','34335111','40909853','42757394','42383711','33288388','39521391','41838559','37392619','32144896','42066358']

def main():
    folder=OUT/'additional_sources';folder.mkdir(exist_ok=True)
    cache=folder/'pubmed_records.xml'
    if not cache.exists():
        response=get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',params={'db':'pubmed','id':','.join(IDS),'retmode':'xml'})
        cache.write_bytes(response.content)
    result=[]
    for a in ET.fromstring(cache.read_bytes()).findall('PubmedArticle'):
        plain=lambda e: ' '.join(''.join(e.itertext()).split()) if e is not None else ''
        pmid=plain(a.find('.//PMID'))
        ids={e.attrib.get('IdType'):e.text for e in a.findall('./PubmedData/ArticleIdList/ArticleId')}
        item={'pmid':pmid,'title':plain(a.find('.//ArticleTitle')),'journal':plain(a.find('.//Journal/Title')),'doi':ids.get('doi',''),'pmcid':ids.get('pmc',''),'publication_types':'; '.join(plain(e) for e in a.findall('.//PublicationType')),'abstract': '\n'.join(plain(e) for e in a.findall('.//AbstractText')),'fulltext_status':'not_retrieved','fulltext_url':''}
        if ids.get('pmc'):
            url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/{ids['pmc']}/fullTextXML";item['fulltext_url']=url
            try:
                r=get(url);root=ET.fromstring(r.content)
                xml_dois=[e.text.lower() for e in root.findall('./front/article-meta/article-id') if e.attrib.get('pub-id-type')=='doi' and e.text]
                if ids.get('doi') and ids['doi'].lower() not in xml_dois: raise ValueError('XML DOI does not match PubMed article DOI')
                resolve_source(folder/(pmid+'.xml')).write_bytes(r.content)
                text=[]
                for section in root.findall('.//abstract')+root.findall('.//body'):
                    text.append('\n'.join(plain(el) for el in section.iter() if el.tag in ('title','p','table')))
                (folder/(pmid+'.txt')).write_text('\n\n'.join(text),encoding='utf-8')
                item['fulltext_status']='xml_retrieved'
            except Exception as exc: item['fulltext_status']=str(exc)
            time.sleep(.4)
        result.append(item)
    write_csv(OUT/'additional_source_registry.csv',result)
    print(json.dumps([{k:v for k,v in r.items() if k in ['pmid','pmcid','fulltext_status']} for r in result],indent=2))

if __name__=='__main__': main()
