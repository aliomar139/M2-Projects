"""Fit and serialize the selected RF procedure; preserve its prior CV evidence."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('augmentation',Path(__file__).with_name('11-augment-high-burnout-classifiers.py'))
augmentation=importlib.util.module_from_spec(spec);spec.loader.exec_module(augmentation)
binary,training=augmentation.binary,augmentation.training


def main():
    cp=ROOT/'experiments/23-save-selected-random-forest-settings.json';c=json.loads(cp.read_text());ref=ROOT/c['reference_run']
    rm=json.loads((ref/'manifest.json').read_text());assert rm['status']=='complete'
    model_path,metadata_path=ROOT/c['model_path'],ROOT/c['metadata_path']
    if model_path.exists() or metadata_path.exists():
        raise FileExistsError('A saved selected RF already exists. Version it explicitly before replacing it.')
    assert training.sha256(augmentation.__file__)==rm['script_sha256']
    modules=[augmentation,binary,binary.ensemble,training,augmentation.kernels,augmentation.priority]
    helpers={Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    assert all(helpers[k]==h for k,h in rm['helper_sha256'].items())
    assert all(training.sha256(ROOT/p)==h for p,h in rm['source_sha256'].items())
    assert all(version(p)==v for p,v in rm['packages'].items())
    base=json.loads((ref/'reference-config.json').read_text());search=json.loads((ref/'10-compare-high-burnout-classifiers-settings.json').read_text())
    source=json.loads((ref/'config.json').read_text());data=training.load_data(base)
    cols=base['input_sets'][c['input_set']];X=data[cols];y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert c['input_set']=='small_b' and len(cols)==8 and len(data)==97 and np.bincount(y).tolist()==[80,17]
    assert not any(col.startswith('BAT') or 'burnout' in col or col=='leave_intention' for col in cols)
    old_metrics=pd.read_csv(ref/'metrics-summary.csv')
    evidence=old_metrics[(old_metrics.input_set=='small_b')&(old_metrics.model=='forest')&(old_metrics.augmentation=='inner_selected_ratio')]
    assert len(evidence)==1
    cv_metrics={key:float(evidence.iloc[0][key]) for key in ['recall','precision','f2','tp','fp','fn','tn','average_precision','roc_auc']}
    paths=[cp,Path(__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [Path(m.__file__) for m in modules]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','10-compare-high-burnout-classifiers-settings.json','metrics-summary.csv','held-out-predictions.csv','tuning.json','verification.json']]
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['audit_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',c),('reference-config',base),('search-config',search),('generator-config',source['generator'])]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    packages={p:version(p) for p in [*rm['packages'],'joblib','scipy']}
    manifest={'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,
              'packages':packages,'cv_metrics_reference':cv_metrics,'new_independent_performance_estimate':False}
    mp=out/'manifest.json';mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Audit: {out}',flush=True)
    try:
        with threadpool_limits(limits=1):
            inner=list(StratifiedKFold(4,shuffle=True,random_state=c['validation_seed']).split(X,y))
            pools=[];folds=[];profiles=[];counts=[]
            for number,(tr,va) in enumerate(inner,1):
                assert not set(tr)&set(va)
                gen,provenance,stats=augmentation.pool(X.iloc[tr],y[tr],base,source['generator'],
                    source['generator']['seed']+c['generator_seed_offset']+number)
                assert all(r['parent_a'] in tr+1 and r['parent_b'] in tr+1 for r in provenance)
                pools.append((tr,va,gen));counts.append({'validation_fold':number,**stats})
                profiles.extend({'validation_fold':number,**r} for r in provenance)
                folds.extend({'validation_fold':number,'student_index':int(i+1),'actual_class':int(y[i])} for i in va)
            records=[];choices=[]
            for ratio in [0,*source['ratios']]:
                parts=[]
                for tr,va,gen in pools:
                    Xt,Xv,labels,_=augmentation.prepare(X.iloc[tr],y[tr],X.iloc[va],gen,ratio,base)
                    parts.append((va,Xt,Xv,labels))
                best,candidates=augmentation.search(search,'forest',parts,y,c['model_seed'])
                records.extend({'ratio':ratio,**r} for r in candidates);choices.append((ratio,best))
                print(f'Validated ratio {ratio}: 12 settings x 4 folds',flush=True)
            ratio,chosen=max(choices,key=lambda item:(*augmentation.choice_key(item[1]),-item[0]))
            assert len(records)==36 and chosen['factor'] in [1,2,4]
            # Independently reconstruct all 756 recorded threshold choices and final ties.
            for candidate in records:
                selected=max(candidate['threshold_candidates'],key=lambda r:(r['f2'],r['precision'],r['recall'],r['threshold']))
                assert selected==candidate['chosen_threshold']
            independent=max(records,key=lambda r:(r['chosen_threshold']['f2'],r['chosen_threshold']['precision'],
                r['chosen_threshold']['recall'],r['chosen_threshold']['threshold'],-r['ratio']))
            assert independent=={'ratio':ratio,**chosen}
            gen,provenance,stats=augmentation.pool(X,y,base,source['generator'],
                source['generator']['seed']+c['generator_seed_offset'])
            added=min(len(gen),int(np.ceil(sum(y)*ratio)))
            augmented=pd.concat([X,gen.iloc[:added]],ignore_index=True);labels=np.r_[y,np.ones(added,dtype=int)]
            wrapped,_=training.make_model(base,cols,'ridge');preprocessing=wrapped.estimator[:-1]
            forest=binary.classifier('forest',chosen['parameters'],c['model_seed'])
            pipeline=Pipeline([('preprocessing',preprocessing),('forest',forest)])
            pipeline.fit(augmented,labels,forest__sample_weight=augmentation.priority.weights(labels,chosen['factor'],1))
            scores=binary.probabilities(pipeline,X);threshold=chosen['chosen_threshold']['threshold']
            expected_labels=(scores>=threshold).astype(int)
            # Refit the same final recipe with the historical transformation helper.
            Xt,Xv,expected_y,expected_added=augmentation.prepare(X,y,X,gen,ratio,base)
            control=binary.classifier('forest',chosen['parameters'],c['model_seed']).fit(Xt,expected_y,
                sample_weight=augmentation.priority.weights(expected_y,chosen['factor'],1))
            np.testing.assert_allclose(scores,binary.probabilities(control,Xv),atol=1e-12,rtol=0)
            assert added==expected_added and pipeline.n_features_in_==8
            allowed={col:base['category_levels'].get(col,[1,2,3,4,5]) for col in cols}
            bundle={'schema_version':1,'pipeline':pipeline,'feature_names':cols,'allowed_values':allowed,
                    'warning_threshold':threshold,'decision_rule':'High if warning_score >= warning_threshold',
                    'class_names':{0:'Below-high',1:'High'},'target':'burnout_score >= 4',
                    'selected_recipe':{'ratio':ratio,'factor':chosen['factor'],'parameters':chosen['parameters']},
                    'packages':packages,'cv_metrics_reference':cv_metrics,
                    'performance_note':'CV metrics belong to the earlier selected procedure, not independent validation of this final fitted artifact.'}
            staged=out/'selected-rf.joblib';joblib.dump(bundle,staged,compress=3)
            loaded=joblib.load(staged)
            np.testing.assert_allclose(binary.probabilities(loaded['pipeline'],X),scores,atol=1e-12,rtol=0)
            np.testing.assert_array_equal(binary.probabilities(loaded['pipeline'],X)>=loaded['warning_threshold'],expected_labels)
            assert loaded['feature_names']==cols and loaded['allowed_values']==allowed
            (out/'tuning.json').write_text(json.dumps({'candidates':records,'selected':{'ratio':ratio,**chosen}},indent=2),encoding='utf-8')
            pd.DataFrame(folds).to_csv(out/'validation-folds.csv',index=False)
            pd.DataFrame(profiles+[{'validation_fold':0,**r} for r in provenance]).to_csv(out/'synthetic-profiles.csv',index=False)
            pd.DataFrame(counts+[{'validation_fold':0,**stats}]).to_csv(out/'generation-counts.csv',index=False)
            pd.DataFrame({'student_index':np.arange(1,98),'warning_score':scores,'predicted_class':expected_labels}).to_csv(out/'final-fit-predictions-not-evaluation.csv',index=False)
            metadata={'schema_version':1,'created_utc':datetime.now(timezone.utc).isoformat(),
                'model_path':c['model_path'],'model_sha256':training.sha256(staged),'audit_path':str(out.relative_to(ROOT)),
                'reference_run':c['reference_run'],'input_set':'small_b','feature_names':cols,'allowed_values':allowed,
                'label_definition':{'High':'measured burnout_score >= 4','Below-high':'measured burnout_score < 4'},
                'warning_threshold':threshold,'decision_rule':'>=','selected_recipe':bundle['selected_recipe'],
                'forest_fixed':{'n_estimators':100,'random_state':c['model_seed'],'n_jobs':1},
                'real_students':97,'real_class_counts':{'Below-high':80,'High':17},'synthetic_training_rows_added':added,
                'final_training_rows':len(labels),'packages':packages,'cv_metrics_reference':cv_metrics,
                'fit_validation_metrics_not_independent':chosen['chosen_threshold'],
                'new_independent_performance_estimate':False,'probabilities_calibrated':False,
                'checks':{'historical_transform_control_refit_passed':True,'joblib_roundtrip_scores_labels_passed':True},
                'limitations':['Exploratory selection after many comparisons on the same 97 students.',
                              'Synthetic labels are inferred; scores are not clinical probabilities.',
                              'No independent validation of this all-data final fit.']}
            assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
            model_path.parent.mkdir(parents=True,exist_ok=True)
            # Exclusive creation protects an existing selected artifact from replacement.
            with model_path.open('xb') as destination:destination.write(staged.read_bytes())
            with metadata_path.open('x',encoding='utf-8') as destination:destination.write(json.dumps(metadata,indent=2)+'\n')
            assert training.sha256(model_path)==metadata['model_sha256']
            staged.unlink()
            manifest.update(status='complete',model_path=c['model_path'],metadata_path=c['metadata_path'],
                model_sha256=metadata['model_sha256'],real_training_students=97,synthetic_rows_added=added,
                source_files_unchanged=True,roundtrip_passed=True,control_refit_passed=True,inner_fits=144,final_fits=2)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'model':c['model_path'],'metadata':c['metadata_path'],'threshold':threshold,
                     'ratio':ratio,'parameters':chosen['parameters'],'high_weight':chosen['factor'],'synthetic_added':added},indent=2),flush=True)


if __name__=='__main__':main()
