"""Build evidence tables; pending fields remain explicit, never inferred as absent."""
import json, re, csv
from collections import Counter, defaultdict
from pathlib import Path
from audit_corpus import ROOT, OUT, rows, write_csv

# Focused assistant reading of indicated pages, not independent dual-reviewer appraisal.
# Each value: task class, population, treatment/comparator, inputs, methods,
# outcome, validation/results, limitation, source locator.
CHECKED={
1: ['simulated_dynamic_policy','Virtual ACL reconstruction rehabilitation; no enrolled patient cohort','Adaptive rehabilitation vs static conservative/aggressive protocols','Simulated movement quality, intensity, adherence, pain; wearable-sensing concept','PPO policy coupled with a temporal convolutional prognostic model','Simulated recovery, reinjury events and functional-score forecasts','Simulation reports 15% shorter return time against conservative protocol and 40% fewer reinjuries against aggressive protocol; these are different comparators','Simulation cannot demonstrate patient benefit; article-type label says systematic review despite simulation methods','PDF pp. 1-2; methods and simulation results'],
7: ['systematic_review','16 included studies; 419 identified records','AI performance vs orthopedic surgeons','Clinical tasks and assessment materials vary','OVID Medline search; task-based narrative synthesis','Concordance, knowledge, management and communication performance','Search through 2025-08-13; task-dependent findings','Repository calls this a 43-study meta-analysis, which is unsupported by this paper','PDF pp. 1-3'],
14: ['outcome_prediction','863 TKA patients from four NSW hospitals','Post-TKA prognosis; no nonoperative comparator','Baseline PROMs and biopsychosocial/physical measures','ML and Bayesian predictive models including DCC-Tree','Three-month change in SF-12 PCS and WOMAC','80:20 random split; predictive distributions; PCS test RMSE 8.01 for DCC-Tree','Short follow-up and response bias; multicenter recruitment does not itself establish external-center validation','PDF pp. 1, 4-5, 7, 9'],
20: ['gait_phenotyping_and_outcome_description','109 preoperative hip OA patients; 63 reassessed after replacement; 56 healthy controls','Before/after THR and healthy controls','3D gait angle and moment waveforms','k-means clustering, SVM, SHAP and waveform analyses','Gait subgroups and postoperative biomechanical changes','SVM uses 10-fold CV; group-specific recovery patterns','No causal surgical-versus-conservative benefit estimate; repository incorrectly describes XGBoost','PDF pp. 1, 4, 10-11'],
23: ['outcome_prediction','130945 NHS observations, 2015-2017','Hip/knee replacement recipients; not a surgery-versus-conservative trial','Baseline VAS, Oxford joint scores and associated covariates','Eight supervised classifiers including boosting, forests, elastic net and linear model','Binary PROM improvement','Repeated five-fold CV; abstract reports best training AUROCs around 0.87/0.78 for hip VAS/Q score and 0.86/0.70 for knee','These quoted training results must not be relabeled external validation or treatment-effect evidence','PDF pp. 1-3, 11'],
27: ['outcome_prediction','Orthopedic surgical cohort; sample count not transcribed in focused reading','Postoperative MCID nonachievement; no untreated comparator established','Baseline PROM and patient features','Cost-sensitive, SMOTE and undersampled XGBoost; assessment trees','Six-month SF-12 physical MCID nonachievement','Moderate classification performance described; no numeric metric transcribed','Predicting poor surgical response alone does not identify a better alternative treatment','PDF p. 1; full appraisal pending'],
35: ['scoping_review','14 studies plus one citation-search addition; ten decision aids','Personalized KOA intervention decision aids','Individual patient predictors and personalized outcome estimates','Six-database search; independent reviewers; implementation-focused charting','Tool implementation, treatment coverage and model transparency','Search through 2024-05-17; fewer than half of aids cover nonsurgical alternatives','Directly overlaps thesis review scope; not evidence that causal ITR is absent','PDF pp. 1-3; abstract and methods'],
50: ['expert_rated_llm_treatment_plans','20 anonymized knee/shoulder MRI reports','GPT-4 proposals rated by two senior orthopedic surgeons','MRI report text','Retrospective pilot; semiquantitative expert ratings','Accuracy and clinical usefulness of proposals','Expert evaluation; no patient-outcome experiment','Limited context and urgency handling; repository incorrectly states 100 reports and three surgeons','PDF pp. 1-3; abstract and methods'],
57: ['offline_policy_learning','41328 unique CAD patients; cross-domain methodology','PCI, CABG and medical therapy','Angiography and linked clinical history','Off-policy RL with weighted importance sampling','Composite cardiovascular-event reward','Offline estimated reward gains up to 32% over physician policy','Observational off-policy value is not a prospective clinical effect; transfer to orthopedics needs new validation','PDF p. 1; methods and evaluation sections'],
59: ['imitation_plus_outcome_models','Clinical gait-analysis center; exact training counts vary by model','12 common surgeries and treatment/natural-history outcome scenarios','Clinical gait-analysis features','BART standard-of-practice recommendation models plus outcome models; Shapley explanations','More than 20 outcome measures including Gait Deviation Index','Counterfactual simulations illustrate possible use of combined models','BART model choice alone does not establish causal identification; simulated improvements are not observed deployment benefits','PDF pp. 1-2; methods and simulation sections'],
69: ['causal_methods_perspective','Methodological perspective; no single orthopedic cohort','General alternative-treatment potential outcomes','Trial and observational clinical data','Causal ML discussion, individualized effect estimation and identification assumptions','Treatment outcomes and benefit heterogeneity','Methodological synthesis; not an orthopedic treatment trial','No estimator guarantees identification without appropriate assumptions and data','PDF pp. 1-2 and causal-assumptions sections'],
73: ['imitation_plus_survival_prediction','935 internal and 1750 external patients; nine Korean institutions','HCC initial treatment choices; cross-domain methodology','20 clinical variables plus treatment for survival prediction','Voting ensemble for treatment; random survival forest for prognosis','Observed treatment agreement and post-treatment survival','External top-1 accuracy 55.34%; top-2 86.06%; survival C-index 0.7767','Treatment-conditioned survival predictions do not by themselves identify comparative causal benefit; published 2024 despite 2023 DOI suffix','PDF pp. 1-3, 5-7'],
75: ['prospective_prognostic_cdss_pilot','17 new IMPT patients in the Netherlands, November 2023','Prognostic profiles added to chronic musculoskeletal pain assessment','Biopsychosocial patient assessment; seven outcome measures','ML prognostic profiles and summary indicators','Clinician-profile consistency, usefulness and patient discussion','14/17 profiles consistent with clinician assessment; clinicians found 15/17 useful','Small pilot; concordance is not comparative treatment efficacy; repository N=312 and 79.5% claim unsupported','PDF pp. 1-2, 9'],
78: ['survival_prediction_with_treatment_ranking','Simulations and several clinical survival datasets','Alternative treatments ranked by modeled log-risk','Baseline covariates, treatment, event times and censoring','Neural Cox proportional-hazards model','Survival risk and treatment recommendations','Predictive benchmarks and retrospective recommendation analyses','Survival discrimination alone does not establish causal policy value; journal publication is 2018','PDF pp. 1-2, 10; treatment recommender sections'],
79: ['randomized_trial_personalized_treatment_comparison','154 major depression trial participants: medication 104, CBT 50','Antidepressants vs cognitive behavioral therapy','Five prerandomization differential-response variables','Regression with treatment interactions and leave-one-out predictions; PAI','Post-treatment HRSD and personalized advantage','For patients with predicted advantage >=3 HRSD units, optimal-vs-nonoptimal assignment d=0.58, 95% CI 0.17-1.01','Cross-domain retrospective analysis of an RCT; original summary misattributes authors, venue and sample size','PDF pp. 1-2'],
80: ['clinician_behavior_experiment','220 clinicians','Vignettes with/without ML advice and explanation formats','Patient vignettes and model explanations','Within-subject factorial experiment','Clinician treatment selections','Experiment on response to advice; no patient efficacy estimate transcribed','Repository attribution to Benrimoh and N=142 conflicts with first-page authors Jacobs et al. and N=220','PDF p. 1; abstract'],
86: ['drug_response_ranking_method','Cancer cell-line/drug screening data; exact counts not transcribed','Drug rankings per cell line/patient concept','Molecular features and drug-response data','Proximal Policy Optimization Ranking (PPORank)','Drug-response ranking','Methodological development; not an orthopedic clinical trial','Identical PDF is misfiled at rank 61 under a different DOI; count this document once','PDF p. 1; DOI 10.1002/sim.9491'],
97: ['outcome_prediction','210 patients at one Chinese institution','Hip arthroscopy recipients with mixed FAIS','Preoperative symptoms, PROMs, joint space and alpha angle','LASSO selection; LR, SVM, random forest; SHAP','MCID achievement at at least two years','Reported LR/SVM/RF AUROCs 0.76/0.89/0.99; authors acknowledge lack of external validation','Repository describes a four-European-center N=1850 shift study, inconsistent with this paper','PDF pp. 1-2, 9'],
}

def passage(text, pattern):
    for match in re.finditer(pattern,text,re.I):
        if match.start()>len(text)*.85: continue
        prefix=text[:match.start()]
        loc=re.findall(r'=== PDF PAGE (\d+) ===',prefix)
        return ('PDF p. '+loc[-1]+': ' if loc else 'XML section passage: ')+re.sub(r'\s+',' ',text[max(0,match.start()-70):match.start()+330])
    return 'Not located automatically; requires source review'

def main():
    audit=rows(OUT/'corpus_audit.csv'); verification={x['rank']:x for x in rows(OUT/'source_verification.csv')}
    matrix=[]; snippets=[]; retrieval=[]
    for a in audit:
        rank=int(a['rank']);v=verification[a['rank']]
        pdf=OUT/'page_text'/f'{rank:03}.txt'; xml=OUT/'fulltext_xml'/f'{rank:03}.txt'
        usable_pdf=a['document_class']=='publisher_like_pdf_identity_pending'
        xml_matches=bool(v['xml_doi'] and a['doi'].lower() in v['xml_doi'].lower())
        source=pdf if usable_pdf else xml if xml.exists() and xml_matches else None
        source_status='matching_main_text_candidate' if source else 'original_main_text_needed'
        paper_type='preprint' if a['doi'].lower().startswith('10.48550/') else 'conference_or_abstract' if v['crossref_type']=='proceedings-article' or rank==98 else 'journal_record_not_peer_review_audit' if v['crossref_type']=='journal-article' else 'unresolved'
        item={'rank':rank,'title':v['verified_title'] or a['title'],'authors':v['verified_authors'] or a['authors'],'doi':a['doi'],'journal':v['verified_venue'] or a['journal'],
              'manifest_year':a['year'],'verified_online_date':v['online_date'],'verified_print_date':v['print_date'],'publication_status':paper_type,
              'local_pdf_class':a['document_class'],'source_status':source_status,'source_path':str(source.relative_to(ROOT)).replace('\\','/') if source else '',
              'reading_status':'source_passages_only_not_adjudicated' if source else 'blocked_original_text',
              'task_class':'pending','population_and_sample':'Not extracted','treatments_comparators':'Not extracted','input_features':'Not extracted','methods':'Not extracted','outcomes':'Not extracted','validation_and_results':'Not extracted','limitations':'Not appraised','evidence_locator':'Not assessed',
              'independent_second_reviewer':'pending','final_eligibility':'pending','risk_of_bias':'not_assessed','jif_value':'not_verified','jif_year':'unknown','jif_source':''}
        if rank in CHECKED:
            checked=CHECKED[rank]
            for key,val in zip(['task_class','population_and_sample','treatments_comparators','input_features','methods','outcomes','validation_and_results','limitations','evidence_locator'],checked): item[key]=val
            item['reading_status']='assistant_focused_second_pass_completed'
        matrix.append(item)
        if source:
            text=source.read_text(encoding='utf-8')
            snippets.append({'rank':rank,'source':item['source_path'],'status':'automatically located passages; not validated extraction','population_candidate':passage(text,r'\b(?:patients|participants|sample size|cohort)\b'),
                             'methods_candidate':passage(text,r'\b(?:methods|algorithm|regression|learning)\b'),'validation_candidate':passage(text,r'\b(?:validation|test set|training|cross.validation)\b'),
                             'limitations_candidate':passage(text,r'\b(?:limitations?|confounding|bias)\b')})
        else:
            retrieval.append({'rank':rank,'title':item['title'],'doi':a['doi'],'reason':a['document_class'],'doi_url':'https://doi.org/'+a['doi'] if a['doi'] else '', 'action':'Obtain original article main text; verify title and DOI before appraisal'})
    write_csv(OUT/'second_pass_matrix.csv',matrix);write_csv(OUT/'source_passage_candidates.csv',snippets);write_csv(OUT/'fulltext_retrieval_queue.csv',retrieval)
    lineage=[]
    norm=lambda s: re.sub('[^a-z0-9]','',s.lower())
    for name in ['AgenticAi.csv','CrossDomain.csv']:
        for i,r in enumerate(rows(ROOT/'data/searches/initial'/name),1):
            doi=r.get('DOI','').lower().strip();title=r.get('Title','')
            key='doi:'+doi if doi else 'title:'+norm(title)
            lineage.append({'archive_file':name,'source_row':i,'title':title,'doi':doi,'dedup_key':key,'matched_manifest_ranks':'; '.join(a['rank'] for a in audit if (doi and a['doi'].lower().strip()==doi) or norm(a['title'])==norm(title))})
    write_csv(OUT/'archive_lineage.csv',lineage)
    c=Counter(x['dedup_key'] for x in lineage)
    summary={'archive_rows':len(lineage),'archive_unique_exact_keys':len(c),'duplicate_export_rows':len(lineage)-len(c),
             'manifest_records_linked_to_archives':len(set(r for x in lineage for r in x['matched_manifest_ranks'].split('; ') if r)),
             'matrix_rows':len(matrix),'assistant_focused_reads':len(CHECKED),'matching_main_text_candidates':sum(x['source_status']=='matching_main_text_candidate' for x in matrix),
             'original_text_retrieval_queue':len(retrieval),'independent_review_complete':0,'final_included_studies':'not_determined'}
    (OUT/'table_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
