"""Reconcile search counts and draw a clearly incomplete PRISMA working figure."""
import json,re,textwrap
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from collect_surveys import DATA, resolve_source, ROOT,LR,SURVEYS,rows,write_csv

def main():
    prior=rows(ROOT/'data/audit/new_pubmed_candidates.csv');new=rows(DATA/'review_search_candidates.csv');allr=rows(DATA/'pubmed_source_records.csv');library=rows(SURVEYS/'survey_registry.csv')
    old_ids={r['pmid'] for r in prior};new_ids={r['pmid'] for r in new};union=old_ids|new_ids
    pcount=sum(int(r['exported_records']) for r in rows(ROOT/'data/audit/pubmed_search_log.csv'))
    rcount=sum(int(r['exported_records']) for r in rows(DATA/'review_search_log.csv'))
    selected={r['pmid'] for r in library if r['pmid']};triage=[]
    source_count=sum(bool(r['pdf_file'] or r['xml_file']) for r in library)
    missing_count=len(library)-source_count
    for r in allr:
        title=r['title'];text=title+' '+r['abstract'];types=set(r['publication_types'].split('; '))
        if r['pmid'] in selected:state='retained_in_working_library';reason='Prioritized by domain relevance; final full-text eligibility remains pending'
        elif re.search('retracted',title,re.I) or 'Retracted Publication' in types:state='set_aside_retracted_record';reason='Retraction flag; retained in metadata log, not the working library'
        elif not(types&{'Review','Systematic Review','Scoping Review'}) and not re.search(r'review|survey|guide|primer|perspective',title,re.I):state='nonreview_candidate';reason='Review status requires confirmation; primary studies belong in a different stream'
        elif not re.search(r'orthop|arthroplast|osteoarth|musculoskel|spine|spinal|hip |knee |joint replacement|back pain',text,re.I):state='outside_orthopedic_scope_candidate';reason='No domain signal in the harvested title/abstract; context relevance still requires judgment'
        elif re.search(r'fracture detection|implant identification|segmentation|radiographic grading|image classification',title,re.I) and not re.search(r'treatment|decision|planning|rehabilit',title,re.I):state='adjacent_diagnostic_candidate';reason='Diagnosis-only title; check actual decision link before excluding'
        else:state='manual_scope_check_required';reason='Potentially relevant; screening and prioritization incomplete'
        triage.append({'pmid':r['pmid'],'doi':r['doi'],'title':title,'source_queries':r['source_queries'],'triage_state':state,'triage_reason':reason,'method':'rules-assisted navigation; not final eligibility adjudication','final_eligibility':'pending'})
    write_csv(DATA/'review_triage.csv',triage)
    summary={'prior_occurrences':pcount,'prior_unique_pmids':len(old_ids),'review_occurrences':rcount,'review_unique_pmids':len(new_ids),'cross_pool_overlap':len(old_ids&new_ids),'combined_search_occurrences':pcount+rcount,'combined_search_unique_pmids':len(union),'duplicate_occurrences_removed':pcount+rcount-len(union),'extra_targeted_metadata_pmids':sorted({r['pmid'] for r in allr}-union),'working_library_records':len(library),'final_included_studies':'not determined'}
    (DATA/'prisma_counts.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    fig,ax=plt.subplots(figsize=(12,11),dpi=160);fig.patch.set_facecolor('#f6f8f8');ax.set(xlim=(0,12),ylim=(0,11));ax.axis('off')
    def box(x,y,w,h,label,fill='#ffffff',edge='#77909a',size=10):
        rect=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.03,rounding_size=0.10',linewidth=1.1,edgecolor=edge,facecolor=fill);ax.add_patch(rect)
        ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size,color='#17323d',linespacing=1.5)
    def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,color='#476772',lw=1.2))
    ax.text(.4,10.65,'Literature selection | PRISMA working draft',fontsize=19,fontweight='bold',color='#17323d')
    ax.text(.4,10.25,'Search cutoff: 23 October 2026. Final eligibility and inclusion remain incomplete.',fontsize=10,color='#49616b')
    box(.6,8.8,5,.9,'Earlier PubMed searches P1-P4\n814 occurrences; 803 distinct PMIDs','#e7f0f3')
    box(6.4,8.8,5,.9,'Added review searches R1-R3\n1,196 occurrences; 1,189 distinct PMIDs','#e7f0f3')
    arrow((3.1,8.77),(4.8,8.2));arrow((8.9,8.77),(7.2,8.2))
    box(3.6,7.35,4.8,.85,'Combined database occurrences\nn = 2,010')
    arrow((8.45,7.77),(9,7.77));box(9.05,7.2,2.5,1.15,'Repeat occurrences\nremoved: 171\n(11 + 7 + 153)','#f5eee3')
    arrow((6,7.32),(6,6.95));box(3.6,6.05,4.8,.85,'Distinct database records available\nfor screening: n = 1,839')
    arrow((6,6.02),(6,5.65));box(3.6,4.75,4.8,.85,'Completed title/abstract decisions\nPending; no final exclusion total','#fff3d8')
    arrow((6,4.72),(6,4.35));box(3.6,3.45,4.8,.85,'Reports sought, retrieved and\nassessed for eligibility: pending','#fff3d8')
    arrow((6,3.42),(6,3.05));box(3.6,2.15,4.8,.85,'Studies / reports finally included\nNot determined','#fff3d8')
    box(.45,3.0,2.55,2.0,'Other-source reconciliation\nLegacy citations: 100\nTargeted anchors: 4 PMIDs\nNovelty probes: separate\nReconciliation pending','#edf0f1',size=9)
    box(8.95,3.0,2.6,2.0,f'Working survey library\n{len(library)} prioritized records\n{source_count} with main text\n{missing_count} awaiting retrieval\nFinal inclusion pending','#edf0f1',size=9)
    ax.text(.5,1.45,'Accounting: 803 + 1,189 - 153 = 1,839 distinct PMIDs.',fontsize=10,color='#17323d')
    ax.text(.5,1.05,'The 171 repeats comprise 11 within earlier queries, 7 within added queries and 153 across pools.',fontsize=9,color='#49616b')
    ax.text(.5,.55,'Independent screening, source retrieval and study/report grouping are unfinished. Unknown counts are not zero.',fontsize=9,color='#49616b')
    fig.savefig(LR/'prisma.png',dpi=160,facecolor=fig.get_facecolor(),bbox_inches='tight');fig.savefig(LR/'prisma.svg',facecolor=fig.get_facecolor(),bbox_inches='tight');plt.close(fig)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
