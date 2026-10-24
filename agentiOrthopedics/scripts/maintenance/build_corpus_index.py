"""Current navigation for legacy citations without treating archived dossiers as papers."""
import csv,json,os,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from repo_paths import resolve_source

def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    corpus=ROOT/'papers/corpus';manifest=rows(corpus/'manifest.csv')
    audit={r['rank']:r for r in rows(ROOT/'data/audit/corpus_audit.csv')}
    registry={r['doi'].lower():r for r in rows(ROOT/'LR/Surveys/survey_registry.csv') if r['doi']}
    catalog=[]
    for m in manifest:
        kind=audit[m['rank']]['document_class'];old=resolve_source(corpus/m['file_name'])
        main=None;reader=None;record=registry.get(m['doi'].lower())
        if record:
            for key in ['pdf_file','xml_file']:
                if record[key] and (ROOT/'LR'/record[key]).exists():main=ROOT/'LR'/record[key];break
            if record['reader_file']:reader=ROOT/'LR'/record['reader_file']
        if main is None:
            xml=resolve_source(ROOT/'data/audit/fulltext_xml'/f"{int(m['rank']):03d}.xml")
            if xml.exists() and m['doi']:
                dois=[(e.text or '').lower() for e in ET.parse(xml).getroot().findall('./front/article-meta/article-id') if e.attrib.get('pub-id-type')=='doi']
                if m['doi'].lower() in dois:main=xml
        if main is None and kind=='publisher_like_pdf_identity_pending' and old.exists():main=old
        catalog.append({'rank':m['rank'],'title':m['title'],'doi':m['doi'],'historical_pdf_class':kind,
                        'current_main_text_status':'available_for_appraisal' if main else 'original_main_text_needed',
                        'main_text_path':main.relative_to(ROOT).as_posix() if main else '',
                        'reader_path':reader.relative_to(ROOT).as_posix() if reader and reader.exists() else '',
                        'original_download_path':old.relative_to(ROOT).as_posix(),
                        'audit_text_path':f"data/audit/page_text/{int(m['rank']):03d}.txt"})
    with (corpus/'catalog.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(catalog[0]));writer.writeheader();writer.writerows(catalog)
    count=sum(bool(r['main_text_path']) for r in catalog)
    def link(target):return os.path.relpath(ROOT/target,corpus).replace('\\','/')
    text=['# Earlier 100-citation collection','',
          'Use this index to locate a citation from the original collection. It reflects the 24 October 2026 cleanup and later source recoveries. File availability does not mean eligibility, quality or peer review has been established.','',
          f'**Current main-text coverage:** {count} of 100 citations have a candidate original main text; {100-count} still need retrieval. Some sources are author/preprint versions or XML rather than publisher PDFs. The survey index points to the same surviving copies.','',
          'The original file audit classified 38 downloads as generated summaries, three as wrong documents and one as supplementary material only. Generated summaries and unique wrong files are now in [archive](../../archive/README.md). One wrong file was an exact copy of another citation’s article; retaining the correct article does not validate the wrong citation.','',
          '[Current source catalog](catalog.csv) | [Historical download manifest](manifest.csv) | [Survey library](../../LR/Surveys/README.md) | [Evidence audit](../../research/audit/AUDIT_REPORT.md)','',
          '| ID | Citation | Current source | Earlier download status |','|---|---|---|---|']
    for r in catalog:
        main=r['main_text_path'];labels=[]
        if main:labels.append('[Main text]('+link(main)+')')
        if r['reader_path'] and not main.endswith('.pdf'):labels.append('[Readable view]('+link(r['reader_path'])+')')
        source=' / '.join(labels) if labels else ('[Original needed](https://doi.org/'+r['doi']+')' if r['doi'] else 'Original needed; DOI unresolved')
        status={'publisher_like_pdf_identity_pending':'Article text; appraisal pending','local_summary_sheet':'Generated summary archived','wrong_document_confirmed':'Wrong document; not evidence for this citation','supplement_only':'Supplement; see main-text column'}[r['historical_pdf_class']]
        text.append('| '+r['rank']+' | '+r['title'].replace('|','/')+' | '+source+' | '+status+' |')
    (corpus/'README.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    print(json.dumps({'citations':len(catalog),'current_main_text_available':count,'originals_needed':100-count},indent=2))

if __name__=='__main__':main()
