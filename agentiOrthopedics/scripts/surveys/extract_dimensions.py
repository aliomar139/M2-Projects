"""Dimension inventory with explicit evidence strength and per-paper locators."""
import re,json,xml.etree.ElementTree as ET
from pathlib import Path
from collect_surveys import DATA, resolve_source, LR,SURVEYS,ROOT,rows,write_csv,plain

# Canonical wording is ours; source locators retain where evidence can be checked.
DIMS=[
('D01','Clinical condition and anatomical scope',r'condition|anatomic|clinical focus|clinical domain|types of surgery|patient group'),
('D02','Decision task and care stage',r'decision|application scenario|application.*function|clinical.*task|care pathway|perioperative'),
('D03','Treatment options and comparators',r'treatment option|operative or nonoperative|intervention|comparator|comparison group'),
('D04','Study design and evidence level',r'study design|study type|evidence level|level of evidence'),
('D05','Population and sample size',r'sample|patient number|population|participant'),
('D06','Data source, setting and geography',r'dataset|registry|data source|country|continent|setting|synthetic data'),
('D07','Input features and modalities',r'input|feature|predictor|multimodal|covariate'),
('D08','Outcomes and PROM instruments',r'outcome|PROM|patient.reported|WOMAC|KOOS|HAGOS'),
('D09','Follow-up and assessment horizon',r'time point|follow.up|duration|time horizon|frequency'),
('D10','Model family and LLM backbone',r'algorithm|model|technology|type of AI|AI.*used'),
('D11','Agent architecture, roles and coordination',r'agent architecture|multi.agent|consensus method|team size|agent number'),
('D12','Retrieval, tools and evidence sources',r'retrieval|tool integration|tools integration|tool.call|RAG|evidence retrieval'),
('D13','Historical-choice versus comparative-benefit target',r'imitation|counterfactual|treatment.effect|historical.*choice|causal.*benefit'),
('D14','Causal identification and target trial design',r'causal inference|causal graph|DAG|target trial|identifiab|exchangeability'),
('D15','Confounder selection and adjustment',r'confound|propensity|inverse probability|covariate selection|adjustment set'),
('D16','Treatment overlap and positivity',r'positivity|overlap|extreme weight|weight trimming'),
('D17','Missingness, attrition and selection',r'missing data|missingness|attrition|loss to follow|selection bias'),
('D18','Time zero and information leakage',r'time zero|immortal time|leakage|post.baseline|baseline timing'),
('D19','Frozen model versus redevelopment',r'frozen|model state|redevelop|recalibrat|model updating'),
('D20','External and geographic validation',r'external valid|geographic|multicenter|multicentre|transportability'),
('D21','Temporal validation and drift',r'temporal|data.drift|distribution.*shift|dataset shift'),
('D22','Calibration and proper scoring',r'calibration|Brier|proper scoring'),
('D23','Uncertainty, abstention and unsupported inputs',r'uncertainty|out.of.distribution|abstention|confidence interval|low.confidence'),
('D24','Decision utility and policy value',r'decision curve|net benefit|policy value|off.policy|decision utility'),
('D25','Explanation and interpretability',r'explainab|interpretabil|SHAP|Shapley'),
('D26','Subgroup fairness and equity',r'fairness|equity|subgroup|demographic bias|disparit'),
('D27','Patient preferences and shared decisions',r'patient preference|shared decision|patient value|decision conflict'),
('D28','Workflow, end users and usability',r'workflow|end user|usability|mode of delivery|clinical integration|clinician satisfaction'),
('D29','Prospective impact and patient benefit',r'prospective|patient benefit|clinical impact|implementation success|success of CDS'),
('D30','Costs, latency and resource burden',r'cost|latency|resource|computational burden|efficiency'),
('D31','Reproducibility and availability',r'reproducib|code avail|data avail|protocol|registration'),
('D32','Safety, privacy and accountability',r'safety|privacy|governance|accountab|regulat|ethical|failure mode'),
('D33','Risk of bias and reporting quality',r'risk of bias|quality assessment|methodological quality|TRIPOD|PROBAST|ROBINS|reporting completeness'),
('D34','Review search, selection and synthesis',r'search strategy|study selection|data extraction|data synthesis|eligibility criteria'),
('D35','Patient-state representation and history',r'state representation|state.space|patient state|state definition|longitudinal history'),
('D36','Action space, dose and scheduling',r'action.space|action type|action definition|dose|dosage|treatment schedul'),
('D37','Rewards and multiple clinical/nonclinical objectives',r'reward|multi.objective|objective function|non.clinical objective'),
('D38','Recommendation paradigm and information basis',r'content.based|collaborative filtering|knowledge.based|hybrid.*recommend'),
('D39','Reference standard and comparator validity',r'reference standard|ground truth|expert consensus|surgeon.*compar|baseline comparison'),
('D40','Performance measures and comparison criteria',r'evaluation metric|performance metric|model performance|accuracy|sensitivity|specificity|AUROC|F1|BLEU|ROUGE'),
('D41','Unit of analysis and dependent evidence',r'unit of analysis|program.level|study.level|patient.level|limb.level|cluster|dependent evidence'),
]

# Checked against the named original tables/method sections in this run.
MANUAL={
'41568289':(['D01','D02','D03','D04','D05','D06','D07','D08','D09','D10','D28','D29','D40'],'Tables 1-3; Methods: data extraction and data items'),
'42383711':(['D01','D03','D04','D05','D06','D07','D08','D14','D15','D33'],'Tables 1-3; Methods: charting the data and risk appraisal'),
'42791908':(['D01','D02','D10','D19','D20','D21','D22','D23','D24','D28','D29','D32','D33','D41'],'Methods 2.5-2.6; Tables 1-6; Discussion 4.3-4.8'),
'41346991':(['D01','D02','D04','D05','D10','D33','D40'],'Tables 1-2; Methods: data extraction and synthesis'),
'41536317':(['D01','D02','D03','D04','D05','D06','D08','D09','D10','D28','D33','D40'],'Methods: Data Extraction; Tables 2-4'),
'42757394':(['D01','D02','D10','D40'],'Methods: Synthesis Approach; Results: three application groups'),
'40909853':(['D01','D02','D04','D05','D06','D10','D11','D12','D20','D39'],'Tables 1-3; cited version is a preprint'),
'41245704':(['D01','D02','D04','D06','D10','D39','D40'],'Table 1; Methods: Screening and data extraction'),
'41614143':(['D01','D02','D04','D05','D06','D10'],'Table 1; Methods: data extraction'),
'LEGACY_064':(['D01','D02','D06','D07','D10','D20','D25','D30','D31','D32','D34','D38','D40'],'PDF pp. 6-9; Tables 4-10; benchmarking and provenance sections'),
'LEGACY_068':(['D01','D02','D03','D06','D07','D08','D10','D24','D27','D32','D34','D35','D36','D37'],'PDF pp. 6-7, 21-22, 25-26; Tables 3-5; state/action/reward and multi-objective sections'),
}

def load_source(r):
    if r['xml_file']:
        root=ET.parse(LR/r['xml_file']).getroot();body=root.find('./body')
        sections=[plain(e.find('title')) for e in body.findall('.//sec') if e.find('title') is not None] if body is not None else []
        tables=[]
        for i,t in enumerate(body.findall('.//table-wrap') if body is not None else [],1):
            heads=[plain(x) for x in t.findall('.//thead//th')]
            if not heads:
                first=t.find('.//table//tr')
                if first is not None:heads=[plain(x) for x in first if x.tag in ('th','td')]
            tables.append((plain(t.find('label')) or f'Table ordinal {i}',heads))
        return plain(body),sections,tables,'fulltext_xml'
    if r['pdf_file']:
        from pypdf import PdfReader
        import logging
        logging.getLogger('pypdf').setLevel(logging.ERROR)
        pdf=PdfReader(LR/r['pdf_file'])
        text='\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(pdf.pages))
        (DATA/'pdf_text').mkdir(exist_ok=True)
        (DATA/'pdf_text'/(r['paper_id']+'.txt')).write_text(text,encoding='utf-8')
        return text,[],[],'fulltext_pdf_text'
    return r['abstract'],[],[],'abstract_only' if r['abstract'] else 'metadata_only'

def main():
    reg=rows(SURVEYS/'survey_registry.csv');long=[];wide=[];inventory=[]
    output=['# Dimensions reported in the working survey library','',
            'Updated 23 October 2026. A dimension is a study characteristic, comparison axis, model/evaluation property or implementation theme that a review charts or discusses. Review methodology is recorded separately from clinical/model dimensions. This inventory covers every paper in the working library, including explicitly marked cross-domain context.', '',
            '**Evidence levels:** `confirmed_charted_or_compared` = checked in the named original table or method section; `candidate_table_field` and `candidate_section_theme` = machine-mapped structure requiring adjudication; `discussion_mention_only` = a text mention, not proof of systematic extraction; `abstract_mention_only` = abstract evidence only; `not_located_in_available_text` = no match found, not demonstrated absence; `unknown_fulltext_unavailable` = original text unavailable. These labels must not be collapsed into present/absent prevalence estimates.','',
            'Eleven close comparators have focused assistant checks. None has independent second-reviewer confirmation. Supplementary extraction forms and image-only tables can contain dimensions not recovered from the available XML/PDF text; no semantically exhaustive “all dimensions” claim is made.','',
            '## Dimension codebook','', '| Code | Dimension |','|---|---|']
    output += [f'| {d} | {label} |' for d,label,_ in DIMS]
    output += ['','## Paper-by-paper inventory','']
    for r in reg:
        text,sections,tables,basis=load_source(r);pid=r['paper_id'];wide_row={'paper_id':pid,'title':r['title'],'stream':r['stream'],'source_basis':basis};paper_rows=[]
        manual=MANUAL.get(pid) or MANUAL.get(r['pmid'])
        for d,label,pattern in DIMS:
            loc='';status='unknown_fulltext_unavailable' if basis in ('abstract_only','metadata_only') else 'not_located_in_available_text'
            for table,headers in tables:
                if any(re.search(pattern,h,re.I) for h in headers):status='candidate_table_field';loc=table;break
            if not loc:
                match=next((s for s in sections if re.search(pattern,s,re.I)),None)
                if match:status='candidate_section_theme';loc='Section: '+match
            if not loc and re.search(pattern,text,re.I):
                status='abstract_mention_only' if basis=='abstract_only' else 'discussion_mention_only';loc='Abstract' if basis=='abstract_only' else 'Text search; specific claim not yet adjudicated'
            if manual and d in manual[0]:status='confirmed_charted_or_compared';loc=manual[1]
            item={'paper_id':pid,'title':r['title'],'dimension_code':d,'dimension':label,'evidence_status':status,'locator':loc,'source_basis':basis,'independent_review':'pending'}
            long.append(item);paper_rows.append(item);wide_row[d]=status
        wide.append(wide_row)
        inventory.append({'paper_id':pid,'source_basis':basis,'section_headings':sections,'table_fields':[{'table':t,'fields':h} for t,h in tables],'coverage_limit':'Structural extraction; supplementation and semantic adjudication pending'})
        links=[]
        for field,label in [('pdf_file','PDF'),('reader_file','readable original text'),('xml_file','XML')]:
            if r[field]:links.append(f"[{label}]({Path(r[field]).relative_to('Surveys').as_posix()})")
        output += [f'<a id="{pid.lower()}"></a>',f'### {pid}: {r["title"]}','',
                   f"[Citation record](records/{pid}.md) | "+' | '.join(links or ['Original main text still needed']), '',
                   f"Stream: {r['stream']}. Source basis: {basis}. Publication category: {r['review_class']}.",'']
        confirmed=[x for x in paper_rows if x['evidence_status']=='confirmed_charted_or_compared']
        candidate=[x for x in paper_rows if x['evidence_status'] in ('candidate_table_field','candidate_section_theme')]
        mentions=[x for x in paper_rows if x['evidence_status']=='abstract_mention_only']
        if confirmed:output+=['Checked charting/comparison dimensions: '+ '; '.join(x['dimension'] for x in confirmed)+'.','', 'Evidence locator: '+manual[1]+'.','']
        if candidate:output+=['Additional structure-mapped candidates requiring confirmation: '+'; '.join(x['dimension'] for x in candidate)+'.','']
        if not confirmed and not candidate:
            output += [('Abstract signals only: '+'; '.join(x['dimension'] for x in mentions)+'.') if mentions else 'Dimension extraction remains pending original-source assessment.','']
        if basis in ('abstract_only','metadata_only'):output+=['**Incomplete:** full-text dimensions cannot be established from metadata or an abstract. See the retrieval queue.','']
        else:output+=['Full cell-level statuses and locators are in [dimensions.csv](dimensions.csv); source section/table inventories are retained in `dimension_evidence_structure.json`. Discussion mentions alone are not charted dimensions.','']
    write_csv(SURVEYS/'dimensions.csv',long);write_csv(SURVEYS/'dimension_coverage.csv',wide)
    (SURVEYS/'dimension_evidence_structure.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
    (SURVEYS/'dimensions.md').write_text('\n'.join(output)+'\n',encoding='utf-8')
    print(json.dumps({'papers':len(reg),'dimensions':len(DIMS),'cells':len(long),'focused_checked_reviews':len(MANUAL),'checked_cells':sum(x['evidence_status']=='confirmed_charted_or_compared' for x in long)},indent=2))

if __name__=='__main__':main()
