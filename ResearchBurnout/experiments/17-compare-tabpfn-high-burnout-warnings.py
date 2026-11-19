"""Local public TabPFN-2; original nested folds, real training students only."""
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
import os
from pathlib import Path

os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TABPFN_NO_BROWSER'] = '1'
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from tabpfn import TabPFNClassifier
from tabpfn.constants import ModelVersion
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('binary', Path(__file__).with_name('10-compare-high-burnout-classifiers.py'))
binary = importlib.util.module_from_spec(spec); spec.loader.exec_module(binary)
training = binary.training


def choose(rows, minimum_recall=None):
    if minimum_recall is None:
        return max(rows, key=lambda r: (r['f2'], r['precision'], r['recall'], r['threshold']))
    eligible = [r for r in rows if r['recall'] >= minimum_recall]
    assert eligible
    return max(eligible, key=lambda r: (-r['fp'], r['recall'], r['precision'], r['f2'], r['threshold']))


def main():
    config_path = ROOT/'experiments/17-compare-tabpfn-high-burnout-warnings-settings.json'
    c = json.loads(config_path.read_text()); ref = ROOT/c['reference_run']
    base = json.loads((ref/'reference-config.json').read_text())
    data = training.load_data(base); cols = base['input_sets'][c['input_set']]
    X = data[cols].to_numpy(dtype=float); y = (data.burnout_score.to_numpy() >= c['high_boundary']).astype(int)
    assert X.shape == (97, 8) and np.isfinite(X).all() and np.bincount(y).tolist() == [80,17]
    assert c['model_version'] == 'v2' and not c['augmentation'] and c['high_boundary'] == 4
    reference = pd.read_csv(ref/'held-out-predictions.csv')
    current = reference[(reference.input_set=='small_b') & (reference.model=='forest') & (reference.augmentation=='inner_selected_ratio')].copy()
    assert len(current) == 485
    recipes = json.loads((ref/'tuning.json').read_text())
    paths = [config_path, Path(__file__), ROOT/c['checkpoint'], ROOT/base['dataset'],
             ROOT/base['derived_indicator_reconstruction']['raw_csv'], Path(binary.__file__), Path(training.__file__)]
    paths += [ref/name for name in ['reference-config.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv','manifest.json']]
    hashes = {str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out = ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'); out.mkdir(parents=True)
    (out/'config.json').write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8')
    manifest = {'status':'running','started_utc':datetime.now(timezone.utc).isoformat(), 'source_sha256':hashes,
        'packages':{p:version(p) for p in ['tabpfn','torch','numpy','pandas','scikit-learn','scipy','pyreadstat','threadpoolctl']},
        'model_version':'TabPFN-2','device':'cpu','real_participants':97,'synthetic_rows':0,'deployment_model_saved':False}
    def save_manifest():
        (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    save_manifest(); torch.set_num_threads(c['torch_threads'])
    predictions, tuning, assignments, outer_rows = [], [], [], []
    try:
        with threadpool_limits(limits=c['torch_threads']):
            for rep, seed in enumerate(base['cv']['outer_seeds'],1):
                for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(X,y),1):
                    assert not set(train)&set(test)
                    inner_seed = base['cv']['inner_seed']+rep*100+fold
                    inner = list(StratifiedKFold(4,shuffle=True,random_state=inner_seed).split(train,y[train]))
                    oof = np.full(len(train),np.nan)
                    for number,(tr,va) in enumerate(inner+[(np.arange(len(train)),np.array([],dtype=int))],1):
                        is_inner = number <= 4; valid = train[va] if is_inner else test
                        assert not set(train[tr])&set(valid)
                        model = TabPFNClassifier.create_default_for_version(ModelVersion.V2,
                            model_path=ROOT/c['checkpoint'],device='cpu',n_estimators=c['n_estimators'],
                            auto_scale_n_estimators=False,random_state=inner_seed,
                            categorical_features_indices=c['categorical_features_indices'],n_preprocessing_jobs=1)
                        model.fit(X[train[tr]],y[train[tr]])
                        scores = binary.probabilities(model,X[valid]); del model
                        if is_inner:
                            oof[va] = scores
                            assignments.extend({'input_set':c['input_set'],'repeat':rep,'fold':fold,'inner_fold':number,
                                'student_index':int(i+1)} for i in valid)
                        else: outer_scores = scores
                    assert np.isfinite(oof).all()
                    previous = next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest' and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                    minimum = previous['chosen']['chosen_threshold']['recall']
                    candidates = [{'threshold':t,**binary.metrics(y[train],oof>=t)} for t in c['thresholds']]
                    choices = {'tabpfn_f2':choose(candidates),'tabpfn_recall_guard':choose(candidates,minimum)}
                    tuning.append({'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),'oof_scores':oof.tolist(),
                        'minimum_recall':minimum,'candidates':candidates,'choices':choices})
                    for method,chosen in choices.items():
                        predictions.extend({'input_set':c['input_set'],'model':'tabpfn_v2','augmentation':method,
                            'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i]),
                            'actual_score':float(data.burnout_score.iloc[i]),'warning_score':float(s),
                            'threshold':chosen['threshold'],'predicted_class':int(s>=chosen['threshold'])} for i,s in zip(test,outer_scores))
                    outer_rows.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
                    pd.DataFrame(predictions).to_csv(out/'held-out-predictions-partial.csv',index=False)
                    (out/'tuning.json').write_text(json.dumps(tuning,indent=2),encoding='utf-8')
                    print(f'Completed {len(tuning)}/25 outer groups: TabPFN-2, four inner fits + one outer fit',flush=True)
        outer = pd.DataFrame(outer_rows); inner_table = pd.DataFrame(assignments)
        pd.testing.assert_frame_equal(outer,pd.read_csv(ref/'outer-folds.csv'))
        expected = pd.read_csv(ref/'inner-folds.csv'); expected = expected[expected.input_set=='small_b']
        order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner_table.sort_values(order).reset_index(drop=True),expected.sort_values(order).reset_index(drop=True))
        result = pd.concat([pd.DataFrame(predictions),current],ignore_index=True)
        assert len(result)==1455 and not result.duplicated(['augmentation','repeat','student_index']).any()
        assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
        assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv',index=False)
        outer.to_csv(out/'outer-folds.csv',index=False); inner_table.to_csv(out/'inner-folds.csv',index=False)
        rows=[]
        for (method,rep),g in result.groupby(['augmentation','repeat']):
            assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
            rows.append({'procedure':method,'repeat':rep,**binary.metrics(g.actual_class,g.predicted_class),
                'average_precision':float(average_precision_score(g.actual_class,g.warning_score)),
                'roc_auc':float(roc_auc_score(g.actual_class,g.warning_score))})
        repeats=pd.DataFrame(rows); repeats.to_csv(out/'repeat-metrics.csv',index=False)
        summary=repeats.groupby('procedure').mean(numeric_only=True).drop(columns='repeat'); summary.to_csv(out/'metrics-summary.csv')
        lines=['# Local TabPFN-2 classification comparison','',
            '97 real students; High means primary BAT score >=4 (17 High, 80 Below-high). Same eight Small B inputs and original 5x5 outer / four inner folds.',
            'Public original v2 checkpoint, not current gated v3.5. Eight estimators, CPU, fixed seeds, raw inputs with sleep/study treated categorically. No synthetic rows, external scaling, one-hot encoding or parameter search.',
            'Thresholds 0..1 by .05 are chosen on excluded inner students: maximize F2, or require current RF inner recall then minimize false warnings. Inner recall is not an outer guarantee.', '',
            '| Procedure | Recall | Precision | F2 | Detected /17 | False warnings /80 | AP | ROC AUC |',
            '|---|---:|---:|---:|---:|---:|---:|---:|']
        for method,r in summary.iterrows():
            lines.append(f'| {method} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.4f} | {r.roc_auc:.4f} |')
        lines += ['', 'Five repetitions reuse the same 97 people. This comparison is exploratory after multiple experiments; no independent cohort or clinical calibration. Source data, prior outputs and selected RF remain unchanged. No deployment fit.',
            '', 'Model: https://huggingface.co/Prior-Labs/TabPFN-v2-clf ; paper: https://www.nature.com/articles/s41586-024-08328-6 .']
        (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,outer_groups=25,context_fits=125)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc)); raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat(); save_manifest()
    print(f'Complete: {out}',flush=True)


if __name__=='__main__':main()
