"""Write human-readable index and citation export without inventing missing metadata."""
import re,json
from pathlib import Path
from collect_surveys import DATA, resolve_source, LR,SURVEYS,rows

def main():
    reg=rows(SURVEYS/'survey_registry.csv');summary=json.loads((DATA/'library_summary.json').read_text(encoding='utf-8'))
    out=['# Surveys: review-paper working library','',
         f"Updated 23 October 2026. {len(reg)} records: {summary['orthopedic_stream']} orthopedic and {summary['cross_domain_context']} cross-domain context. Original main text is available for {summary['records_with_main_text']} records; {summary['metadata_or_abstract_only']} still need retrieval. The {summary['original_pdf_copies']} PDF copies and {summary['doi_verified_xml_copies']} XML copies overlap, so they must not be added to count papers.",'',
         'This is a prioritized working library assembled from the legacy corpus and expanded PubMed searches, not an exhaustive or final included set. The broader search exports remain available for screening. Conceptual/method guides and the explicitly marked preprint are separated by publication category in the registry. No known retracted record is retained in this working library.','',
         '[Dimensions per paper](dimensions.md) | [Dimension table](dimensions.csv) | [Comparison matrix](dimension_coverage.csv) | [Full registry](survey_registry.csv) | [Missing originals](retrieval_queue.csv) | [RIS citations](surveys.ris)','',
         '## Source formats','',
         '`sources/*.pdf` are original publisher/author article candidates with provenance recorded in the registry; locally generated legacy summary PDFs and known wrong files were not copied. Newly recovered publisher PDFs require a DOI match in the first two pages. `sources/*.xml` retains original article XML with a matching main-article DOI. The corresponding `.html` files provide readable text/tables; they may omit figures, mathematical layout or references. Use the original XML and publisher version for complete appraisal.','',
         'Citation records without main text remain useful discovery records but cannot support a complete list of that review’s dimensions. Publication date, peer-review status, corrections and study eligibility still need final adjudication. Cross-domain context does not enter orthopedic-study prevalence denominators.','']
    for stream,label in [('orthopedic_review_working_selection','Orthopedic review and methods records'),('cross_domain_methodological_context','Cross-domain methodological context')]:
        out += ['## '+label,'','| Paper / citation | Date / venue | Source files |','|---|---|---|']
        for r in reg:
            if r['stream']!=stream:continue
            links=[]
            for k,label2 in [('pdf_file','PDF'),('reader_file','readable text'),('xml_file','XML')]:
                if r[k]:links.append(f"[{label2}]({Path(r[k]).relative_to('Surveys').as_posix()})")
            title=r['title'].replace('|','/');venue=r['journal'].replace('|','/')
            out.append(f"| [{title}](records/{r['paper_id']}.md) | {r['pubdate']}; {venue} | "+(' / '.join(links) if links else '[Original needed](retrieval_queue.csv)')+' |')
    (SURVEYS/'README.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    ris=[]
    for r in reg:
        ris+=['TY  - '+('UNPB' if r['review_class']=='preprint_review' else 'JOUR'),'ID  - '+r['paper_id'],'TI  - '+r['title']]
        ris+=['AU  - '+name.strip() for name in r['authors'].split(';') if name.strip()]
        if r['journal']:ris+=['JO  - '+r['journal']]
        year=re.search(r'\b(?:19|20)\d{2}\b',r['pubdate'])
        if year:ris+=['PY  - '+year.group()]
        if r['doi']:ris+=['DO  - '+r['doi'],'UR  - https://doi.org/'+r['doi']]
        ris+=['N1  - Working-library record; dates and eligibility require final verification.','ER  - ','']
    (SURVEYS/'surveys.ris').write_text('\n'.join(ris),encoding='utf-8')
    # Refresh citation records after optional publisher recovery.
    for r in reg:
        lines=[f"# {r['title']}",'',f"Paper ID: {r['paper_id']}",'',f"Authors: {r['authors']}",'',f"Journal/date: {r['journal']}; {r['pubdate']}",'',f"DOI: https://doi.org/{r['doi']}",'',f"PMID: {r['pmid'] or 'unavailable'}; PMC: {r['pmcid'] or 'unavailable'}",'',f"Stream: {r['stream']}. Publication category: {r['review_class']}.",'',f"Source status: {r['source_status']}",'', 'Working-library selection; final eligibility, appraisal and independent reviewer checks pending.','']
        for k,label in [('pdf_file','Original PDF candidate'),('xml_file','DOI-verified original XML'),('reader_file','Readable original text/tables')]:
            if r[k]:lines+=['['+label+'](../sources/'+Path(r[k]).name+')','']
        lines+=['Metadata publication types: '+r['publication_types'],'','Correction/retraction links: '+(r['corrections_or_retractions'] or 'None in harvested metadata; not an exhaustive integrity check'),'',f"[Dimension inventory](../dimensions.md#{r['paper_id'].lower()})",'']
        (SURVEYS/'records'/(r['paper_id']+'.md')).write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
