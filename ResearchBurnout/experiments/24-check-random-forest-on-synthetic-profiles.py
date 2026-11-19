"""Check a frozen saved RF against parent-inferred synthetic labels, not real truth."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, fbeta_score, accuracy_score, average_precision_score, roc_auc_score

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('augmentation',Path(__file__).with_name('11-augment-high-burnout-classifiers.py'))
augmentation=importlib.util.module_from_spec(spec);spec.loader.exec_module(augmentation)
training=augmentation.training


def generate(c,X,y,base,generator):
    selected={};blocked=set();logs=[];duplicates=conflicts=0
    requested={int(k):v for k,v in c['requested_counts'].items()}
    for batch in range(1,c['max_batches']+1):
        for cls in [0,1]:
            count=sum(r['assumed_class']==cls for r in selected.values())
            if count>=requested[cls]:continue
            seed=c['seed']+batch*100+cls
            # The existing helper generates its positive class; remap that to each parent class.
            mapped=(y==cls).astype(int)
            gen,provenance,stats=augmentation.pool(X,mapped,base,generator,seed)
            logs.append({'batch':batch,'assumed_class':cls,'seed':seed,'candidate_count':len(gen),
                         'attempts':stats['attempts'],'eligible_anchors':stats['eligible_anchors']})
            for row in provenance:
                key=tuple(int(row[col]) for col in X)
                if key in blocked:continue
                if key in selected:
                    if selected[key]['assumed_class']!=cls:
                        del selected[key];blocked.add(key);conflicts+=1
                    else:duplicates+=1
                    continue
                if sum(r['assumed_class']==cls for r in selected.values())>=requested[cls]:break
                assert y[row['parent_a']-1]==y[row['parent_b']-1]==cls
                selected[key]={**{col:int(row[col]) for col in X},'assumed_class':cls,
                    'label_inferred':True,'parent_a':row['parent_a'],'parent_b':row['parent_b'],
                    'fraction':row['fraction'],'parent_distance':row['parent_distance'],
                    'anchor_distance':row['anchor_distance'],'generation_batch':batch,'generation_seed':seed}
        counts={cls:sum(r['assumed_class']==cls for r in selected.values()) for cls in [0,1]}
        if all(counts[cls]>=requested[cls] for cls in [0,1]):break
    result=pd.DataFrame(list(selected.values()))
    if result.empty or result.assumed_class.nunique()!=2:raise ValueError('Unable to generate both classes without relaxing constraints.')
    result=result.iloc[np.random.default_rng(c['seed']).permutation(len(result))].reset_index(drop=True)
    result.insert(0,'synthetic_id',[f'S{i:04}' for i in range(1,len(result)+1)])
    return result,logs,{'same_class_duplicates_rejected':duplicates,'cross_label_profiles_excluded':conflicts,
        'requested_counts':requested,'generated_counts':{int(k):int(v) for k,v in result.assumed_class.value_counts().items()}}


def verify_profiles(profiles,X,y,base,generator):
    cols=list(X);categorical=[i for i,col in enumerate(cols) if col in base['category_levels']]
    ordinal=[i for i,col in enumerate(cols) if col not in base['category_levels']]
    known={tuple(row) for row in X.to_numpy(dtype=int)};seen=set()
    def distance(a,b):return (np.abs(a[ordinal]-b[ordinal]).sum()/4+(a[categorical]!=b[categorical]).sum())/len(cols)
    for record in profiles.to_dict('records'):
        row=np.array([record[col] for col in cols],dtype=int);key=tuple(row)
        assert key not in known and key not in seen;seen.add(key)
        a=X.iloc[record['parent_a']-1].to_numpy(dtype=int);b=X.iloc[record['parent_b']-1].to_numpy(dtype=int)
        assert record['parent_a']!=record['parent_b'] and y[record['parent_a']-1]==y[record['parent_b']-1]==record['assumed_class']
        assert np.array_equal(row[categorical],a[categorical]) and np.isin(row[ordinal],[1,2,3,4,5]).all()
        assert np.max(np.abs(a[ordinal]-b[ordinal]))<=generator['max_ordinal_gap']
        assert distance(a,b)<=generator['max_parent_distance'] and distance(row,a)<=generator['max_anchor_distance']
        assert np.isclose(distance(a,b),record['parent_distance']) and np.isclose(distance(row,a),record['anchor_distance'])
        fraction=record['fraction'];assert generator['fraction_range'][0]<=fraction<=generator['fraction_range'][1]
        z=(1-fraction)*a[ordinal]+fraction*b[ordinal]
        assert np.all((row[ordinal]==np.floor(z))|(row[ordinal]==np.ceil(z)))


def main():
    cp=ROOT/'experiments/24-check-random-forest-on-synthetic-profiles-settings.json';c=json.loads(cp.read_text())
    metadata=json.loads((ROOT/c['metadata_path']).read_text());model_path=ROOT/c['model_path']
    assert training.sha256(model_path)==metadata['model_sha256']
    assert all(version(p)==v for p,v in metadata['packages'].items())
    bundle=joblib.load(model_path);cols=bundle['feature_names'];threshold=bundle['warning_threshold']
    audit=ROOT/metadata['audit_path'];base=json.loads((audit/'reference-config.json').read_text())
    generator=json.loads((audit/'generator-config.json').read_text());data=training.load_data(base)
    X=data[cols];y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert len(cols)==8 and len(X)==97 and np.bincount(y).tolist()==[80,17] and threshold==metadata['warning_threshold']
    paths=[cp,Path(__file__),Path(augmentation.__file__),ROOT/c['metadata_path'],model_path,
           ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv'],audit/'reference-config.json',audit/'generator-config.json']
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    mp=out/'manifest.json';manifest={'status':'running','source_sha256':hashes,'model_retrained':False,
        'threshold_changed':False,'independent_validation':False,'labels_measured':False,'started_utc':datetime.now(timezone.utc).isoformat()}
    mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    try:
        profiles,logs,stats=generate(c,X,y,base,generator)
        verify_profiles(profiles,X,y,base,generator)
        for col,allowed in bundle['allowed_values'].items():assert profiles[col].isin(allowed).all()
        scores=bundle['pipeline'].predict_proba(profiles[cols])[:,1]
        assert np.isfinite(scores).all() and ((scores>=0)&(scores<=1)).all()
        predicted=(scores>=threshold).astype(int);assumed=profiles.assumed_class.to_numpy()
        profiles['warning_score']=scores;profiles['predicted_class']=predicted;profiles['matches_assumed_label']=predicted==assumed
        metrics=augmentation.binary.metrics(assumed,predicted)
        tn,fp,fn,tp=confusion_matrix(assumed,predicted,labels=[0,1]).ravel()
        independent={'tn':int(tn),'fp':int(fp),'fn':int(fn),'tp':int(tp),'precision':precision_score(assumed,predicted,zero_division=0),
            'recall':recall_score(assumed,predicted),'f2':fbeta_score(assumed,predicted,beta=2,zero_division=0),'accuracy':accuracy_score(assumed,predicted)}
        assert all(np.isclose(metrics[k],v,atol=1e-12,rtol=0) for k,v in independent.items())
        metrics.update(average_precision=float(average_precision_score(assumed,scores)),roc_auc=float(roc_auc_score(assumed,scores)))
        profiles.to_csv(out/'synthetic-profiles-with-predictions.csv',index=False)
        # Roundtrip the exact persisted rows and decisions without changing the saved forest.
        restored=pd.read_csv(out/'synthetic-profiles-with-predictions.csv')
        restored_scores=bundle['pipeline'].predict_proba(restored[cols])[:,1]
        np.testing.assert_allclose(restored_scores,restored.warning_score,atol=1e-12,rtol=0)
        np.testing.assert_array_equal(restored_scores>=threshold,restored.predicted_class)
        verify_profiles(restored,X,y,base,generator)
        result={'experiment_kind':'synthetic neighborhood consistency check','assumed_label_metrics':metrics,
                'warning_threshold':threshold,'generation':stats,'sample_size':len(profiles),
                'all_below_high_accuracy':float(np.mean(assumed==0)),
                'interpretation':c['interpretation']}
        for name,value in [('config',c),('metrics',result),('generation-batches',logs),('generator-config',generator)]:
            (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
        lines=['# Saved RF: synthetic profile consistency check','',
            '**These are agreement scores against assumed synthetic labels, not accuracy on new real students.**',
            'The frozen saved RF trained on all 97 real parents. New answer combinations do not make their synthetic descendants independent test subjects.',
            'Generate both classes with the original constrained neighbor interpolation/stochastic rounding, copying categorical blocks. Labels are inherited from same-class parents without consulting model predictions.',
            'Reject all real-profile duplicates, global synthetic duplicates and exact cross-label conflicts. Keep the original generator constraints; shortfalls are not filled with random rows.',
            f'Generated {len(profiles)} unique synthetic profiles: {sum(assumed==0)} Below-high and {sum(assumed==1)} High. Requested 800/170 matches original class proportions.',
            f'Original saved model and threshold {threshold} are frozen; no retraining, tuning or replacement of previous real-only CV results.','',
            '| Synthetic assumed-label measure | Value |','|---|---:|',
            f'| High recall | {metrics["recall"]:.1%} |',f'| High precision | {metrics["precision"]:.1%} |',
            f'| F2 | {metrics["f2"]:.6f} |',f'| Accuracy/agreement | {metrics["accuracy"]:.1%} |',
            f'| TP / FN | {metrics["tp"]} / {metrics["fn"]} |',f'| FP / TN | {metrics["fp"]} / {metrics["tn"]} |',
            f'| Average precision / AUC | {metrics["average_precision"]:.6f} / {metrics["roc_auc"]:.6f} |','',
            f'Always predicting Below-high would have {result["all_below_high_accuracy"]:.1%} accuracy and zero High recall; accuracy alone is misleading.',
            'Agreement can look favourable because generation follows labelled parents already seen during fitting. The results cannot establish or improve clinical validity, real generalization or the reported 87.1% real held-out recall.',
            'See metrics.json and generation-batches.json for counts/shortfalls/conflicts and the CSV for full parent provenance. No true BAT responses or measured new labels exist for synthetic profiles.']
        (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        verification={'status':'passed','unique_novel_profiles_checked':len(profiles),'parent_labels_domains_distances_rounding_checked':True,
            'independent_sklearn_metrics_match':True,'persisted_scores_decisions_reproduced':True,'model_metadata_sources_unchanged':True,
            'independent_real_validation':False}
        (out/'verification.json').write_text(json.dumps(verification,indent=2)+'\n',encoding='utf-8')
        manifest.update(status='complete',synthetic_rows=len(profiles),generation=stats,source_files_unchanged=True)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Results: {out}\n'+json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
