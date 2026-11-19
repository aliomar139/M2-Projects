"""Separate, nested RF comparison of existing and newly selected survey inputs."""
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version
import importlib.util
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import ParameterGrid, StratifiedKFold
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('questions', Path(__file__).with_name('15-select-four-six-or-eight-questions.py'))
questions = importlib.util.module_from_spec(spec); spec.loader.exec_module(questions)
augmentation, binary, training = questions.augmentation, questions.binary, questions.training


def choose(options, minimum=None):
    eligible = [r for r in options if minimum is None or r['recall'] >= minimum]
    assert eligible
    def key(r):
        common = (r['precision'], r['recall'], r['threshold'], -r['ratio'], -r['candidate_index'])
        return (r['f2'], *common) if minimum is None else (
            -r['fp'], r['recall'], r['precision'], r['f2'], r['threshold'], -r['ratio'], -r['candidate_index'])
    return max(eligible, key=key)


def run_job(args):
    c, base, search, generator, data, rep, fold, train, test, old, expected = args
    with threadpool_limits(limits=1):
        warnings.filterwarnings('error', category=ConvergenceWarning)
        y = (data.burnout_score.iloc[train].to_numpy() >= 4).astype(int)
        seed = base['cv']['inner_seed'] + rep*100 + fold
        inner = list(StratifiedKFold(4, shuffle=True, random_state=seed).split(train, y))
        assignments = [{'input_set':'small_b', 'repeat':rep, 'fold':fold, 'inner_fold':number,
                        'student_index':int(train[i]+1)}
                       for number, (_, va) in enumerate(inner, 1) for i in va]
        predictions, tuning, contexts, generated_rows = [], [], [], []
        inner_fits = outer_fits = 0
        for variant in ['current8_control', 'alternative8', 'ranked8_of23']:
            parts, outer = {}, {}
            ranking = None
            for number, (tr, va) in enumerate(inner + [(np.arange(len(train)), np.array([], dtype=int))], 1):
                number = number if number <= 4 else 0
                assert not set(train[tr]) & set(test) and not set(tr) & set(va)
                if variant == 'ranked8_of23':
                    broad = base['input_sets']['broad_d']
                    ranking, strength = questions.ranked_questions(c, base, broad, data[broad].iloc[train[tr]], y[tr])
                    selected = set(ranking[:c['selected_count']])
                    cols = [col for col in broad if col in selected]
                else:
                    cols = base['input_sets']['small_b'] if variant == 'current8_control' else c['alternative_inputs']
                    strength = None
                assert len(cols) == 8 and set(cols) <= set(base['input_sets']['broad_d'])
                X = data[cols].iloc[train[tr]]
                valid = data[cols].iloc[train[va] if number else test]
                gen, provenance, stats = augmentation.pool(X, y[tr], base, generator,
                    generator['seed'] + rep*10000 + fold*100 + number)
                context = {'variant':variant,'repeat':rep,'fold':fold,'inner_fold':number}
                contexts.append({**context, 'training_ids':(train[tr]+1).tolist(), 'columns':cols,
                                 'ranking':ranking, 'strength':strength, 'generation':stats})
                generated_rows.extend({**context, **row} for row in provenance)
                ratios = [old['selected_ratio']] if variant == 'current8_control' else c['ratios']
                for ratio in ratios:
                    Xt, Xv, labels, added = augmentation.prepare(X, y[tr], valid, gen, ratio, base)
                    if number:
                        parts.setdefault(ratio, []).append((va, Xt, Xv, labels))
                    else:
                        outer[ratio] = (Xt, Xv, labels, added)
            minimum = old['chosen']['chosen_threshold']['recall']
            candidates = []
            for ratio in parts:
                factors = [old['chosen']['factor']] if variant == 'current8_control' else search['relative_high_weights']
                grid = [old['chosen']['parameters']] if variant == 'current8_control' else ParameterGrid(search['grids']['forest'])
                for factor in factors:
                    for params in grid:
                        scores = np.full(len(train), np.nan)
                        seen = np.zeros(len(train), dtype=int)
                        for va, Xt, Xv, labels in parts[ratio]:
                            model = binary.classifier('forest', params, seed).fit(Xt, labels,
                                sample_weight=augmentation.priority.weights(labels, factor, 1))
                            scores[va] = binary.probabilities(model, Xv); seen[va] += 1; inner_fits += 1
                        assert np.isfinite(scores).all() and (seen == 1).all()
                        index = len(candidates)
                        options = [{'candidate_index':index,'ratio':ratio,'threshold':t,
                                    **binary.metrics(y, scores >= t)} for t in search['probability_thresholds']]
                        candidates.append({'candidate_index':index,'ratio':ratio,'factor':factor,'parameters':params,
                            'inner_scores':scores.tolist(),'f2_choice':choose(options),'guard_choice':choose(options,minimum)})
            choices = {'f2':choose([r['f2_choice'] for r in candidates])}
            if variant != 'current8_control':
                choices['recall_guard'] = choose([r['guard_choice'] for r in candidates], minimum)
                assert len(candidates) == 36
            else:
                observed = choices['f2']
                assert all(np.isclose(observed[k],v,atol=1e-12,rtol=0)
                           for k,v in old['chosen']['chosen_threshold'].items())
            cache = {}
            for policy, choice in choices.items():
                index = choice['candidate_index']; candidate = candidates[index]
                Xt, Xv, labels, added = outer[candidate['ratio']]
                if index not in cache:
                    model = binary.classifier('forest', candidate['parameters'], seed).fit(Xt, labels,
                        sample_weight=augmentation.priority.weights(labels, candidate['factor'], 1))
                    cache[index] = binary.probabilities(model, Xv); outer_fits += 1
                scores = cache[index]
                if variant == 'current8_control':
                    np.testing.assert_allclose(scores, expected.set_index('student_index').loc[test+1].warning_score,atol=1e-12,rtol=0)
                predictions.extend({'input_set':variant,'model':'forest','augmentation':policy,'repeat':rep,'fold':fold,
                    'student_index':int(i+1),'actual_class':int(data.burnout_score.iloc[i]>=4),
                    'actual_score':float(data.burnout_score.iloc[i]),'warning_score':float(s),
                    'threshold':choice['threshold'],'predicted_class':int(s>=choice['threshold'])} for i,s in zip(test,scores))
            tuning.append({'variant':variant,'repeat':rep,'fold':fold,'training_ids':(train+1).tolist(),
                'minimum_recall':minimum,'candidates':candidates,'choices':choices})
        return predictions, tuning, contexts, generated_rows, assignments, inner_fits, outer_fits


def report(result, out):
    rows = []
    for (variant, policy, rep), g in result.groupby(['input_set','augmentation','repeat']):
        assert len(g)==97 and g.student_index.nunique()==97 and g.actual_class.sum()==17
        rows.append({'variant':variant,'policy':policy,'repeat':rep,**binary.metrics(g.actual_class,g.predicted_class),
            'average_precision':float(augmentation.average_precision_score(g.actual_class,g.warning_score)),
            'roc_auc':float(augmentation.roc_auc_score(g.actual_class,g.warning_score))})
    repeats=pd.DataFrame(rows); repeats.to_csv(out/'repeat-metrics.csv',index=False)
    summary=repeats.groupby(['variant','policy']).mean(numeric_only=True).drop(columns='repeat')
    summary.to_csv(out/'metrics-summary.csv')
    repeats[['variant','policy','repeat','tp','fp','fn','tn']].to_csv(out/'confusion-matrices.csv',index=False)
    pairs=[]
    for row in repeats[repeats.variant!='current8_control'].itertuples():
        ref=repeats[(repeats.variant=='current8_control')&(repeats['repeat']==row.repeat)].iloc[0]
        pairs.append({'variant':row.variant,'policy':row.policy,'repeat':row.repeat,
                      **{k:getattr(row,k)-ref[k] for k in ['recall','precision','f2','tp','fp']}})
    pd.DataFrame(pairs).to_csv(out/'paired-comparisons.csv',index=False)
    lines=['# Random Forest: alternative existing input combinations','',
        '97 real students; primary BAT score >=4: 17 High, 80 Below-high. Five repeats of five outer/four inner stratified folds.',
        'Current eight control refits its frozen original selected recipe and must reproduce original scores/thresholds.',
        'Alternative eight replaces AI frequency/study hours with academic stress/avoidance. Ranked eight uses grouped L2 logistic C=1 coefficients from the 23 existing variables, fitted on real training members only.',
        'Ranking refits within each inner training group and outer training group; selected categorical questions retain all dummy columns. No globally selected final eight.',
        'Each new input procedure independently tunes original RF depth 2/3, leaf size 5/10, High weight 1/2/4, synthetic ratio 0/.5/1, thresholds 0..1 by .05.',
        'Synthetic pools use only selected training inputs and High training parents; labels are inferred. Source data and evaluation remain real-only.',
        'F2 selection maximizes inner F2/precision/recall/threshold, then lower ratio/stable grid. Guard requires recorded original RF inner recall, minimizes FP, then recall/precision/F2/threshold/lower ratio/stable grid.',
        'Inner recall guards are not outer guarantees. Same training-only preprocessing and fixed seeds as original RF.','',
        '| Inputs | Rule | Recall | Precision | F2 | Detected /17 | False warnings /80 | AP | AUC |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for (variant,policy),r in summary.iterrows():
        lines.append(f'| {variant} | {policy} | {r.recall:.1%} | {r.precision:.1%} | {r.f2:.6f} | {r.tp:.1f} | {r.fp:.1f} | {r.average_precision:.6f} | {r.roc_auc:.6f} |')
    lines+=['','All counts average five dependent repetitions of the same people. Many earlier experiments and exploratory full-sample SPSS findings motivated this comparison; results are exploratory.',
        'The fixed logistic ranking can miss nonlinear relevance. Synthetic novelty does not establish realistic responses or correct labels. This is not an exhaustive feature search.',
        'No source/previous output modification, deployment artifact, calibrated clinical probabilities, or independent cohort validation.']
    (out/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return summary


def main():
    cp=ROOT/'experiments/21-compare-random-forest-input-combinations-settings.json';c=json.loads(cp.read_text());ref=ROOT/c['reference_run']
    rm=json.loads((ref/'manifest.json').read_text()); assert rm['status']=='complete'
    base=json.loads((ref/'reference-config.json').read_text());search=json.loads((ref/'10-compare-high-burnout-classifiers-settings.json').read_text())
    generator=json.loads((ref/'config.json').read_text())['generator']
    assert training.sha256(augmentation.__file__)==rm['script_sha256']
    modules=[questions,augmentation,binary,binary.ensemble,training,augmentation.kernels,augmentation.priority,questions.selection]
    helpers={Path(m.__file__).name:training.sha256(m.__file__) for m in modules}
    assert all(helpers[k]==h for k,h in rm['helper_sha256'].items())
    packages={p:version(p) for p in rm['packages']};assert packages==rm['packages']
    assert all(training.sha256(ROOT/p)==h for p,h in rm['source_sha256'].items())
    data=training.load_data(base);y=(data.burnout_score.to_numpy()>=4).astype(int)
    assert len(data)==97 and np.bincount(y).tolist()==[80,17]
    assert len(base['input_sets']['broad_d'])==23 and c['selected_count']==8
    assert len(set(c['alternative_inputs']))==8 and set(c['alternative_inputs'])<=set(base['input_sets']['broad_d'])
    assert not any(col.startswith('BAT') or 'burnout' in col or col=='leave_intention' for col in base['input_sets']['broad_d'])
    old=pd.read_csv(ref/'held-out-predictions.csv')
    current=old[(old.input_set=='small_b')&(old.model=='forest')&(old.augmentation=='inner_selected_ratio')]
    recipes=json.loads((ref/'tuning.json').read_text())
    paths=[cp,Path(__file__),ROOT/base['dataset'],ROOT/base['derived_indicator_reconstruction']['raw_csv']]
    paths += [Path(m.__file__) for m in modules]
    paths += [ref/name for name in ['manifest.json','config.json','reference-config.json','10-compare-high-burnout-classifiers-settings.json','held-out-predictions.csv','tuning.json','outer-folds.csv','inner-folds.csv']]
    hashes={str(p.relative_to(ROOT)):training.sha256(p) for p in paths}
    out=ROOT/c['output_root']/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');out.mkdir(parents=True,exist_ok=False)
    for name,value in [('config',c),('reference-config',base),('search-config',search),('generator-config',generator)]:
        (out/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    manifest={'status':'running','started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashes,
              'packages':packages,'deployment_model_saved':False}
    mp=out/'manifest.json';mp.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(f'Output: {out}',flush=True)
    try:
        jobs=[];folds=[]
        for rep,seed in enumerate(base['cv']['outer_seeds'],1):
            for fold,(train,test) in enumerate(StratifiedKFold(5,shuffle=True,random_state=seed).split(data,y),1):
                previous=next(r for r in recipes if r['input_set']=='small_b' and r['model']=='forest'
                    and r['augmentation']=='inner_selected_ratio' and r['repeat']==rep and r['fold']==fold)
                expected=current[(current['repeat']==rep)&(current.fold==fold)]
                jobs.append((c,base,search,generator,data,rep,fold,train,test,previous,expected))
                folds.extend({'repeat':rep,'fold':fold,'student_index':int(i+1),'actual_class':int(y[i])} for i in test)
        outer=pd.DataFrame(folds);pd.testing.assert_frame_equal(outer,pd.read_csv(ref/'outer-folds.csv'))
        predictions=[];tuning=[];contexts=[];synthetic=[];assignments=[];inner_fits=outer_fits=0
        with ProcessPoolExecutor(max_workers=c['workers']) as executor:
            futures=[executor.submit(run_job,job) for job in jobs]
            for count,future in enumerate(as_completed(futures),1):
                p,t,x,g,a,ni,no=future.result()
                predictions.extend(p);tuning.extend(t);contexts.extend(x);synthetic.extend(g);assignments.extend(a)
                inner_fits+=ni;outer_fits+=no
                print(f'Completed {count}/25 outer groups; {inner_fits} inner fits',flush=True)
        inner=pd.DataFrame(assignments);expected=pd.read_csv(ref/'inner-folds.csv');expected=expected[expected.input_set=='small_b']
        order=['repeat','fold','inner_fold','student_index']
        pd.testing.assert_frame_equal(inner.sort_values(order).reset_index(drop=True),expected.sort_values(order).reset_index(drop=True))
        result=pd.DataFrame(predictions).sort_values(['input_set','augmentation','repeat','fold','student_index']).reset_index(drop=True)
        assert len(result)==2425 and not result.duplicated(['input_set','augmentation','repeat','student_index']).any()
        assert np.array_equal(result.predicted_class,(result.warning_score>=result.threshold).astype(int))
        assert np.allclose(result.actual_score,data.burnout_score.iloc[result.student_index.to_numpy()-1])
        result.to_csv(out/'held-out-predictions.csv',index=False);outer.to_csv(out/'outer-folds.csv',index=False)
        inner.to_csv(out/'inner-folds.csv',index=False);pd.DataFrame(synthetic).to_csv(out/'synthetic-pools.csv',index=False)
        tuning.sort(key=lambda r:(r['repeat'],r['fold'],r['variant']))
        contexts.sort(key=lambda r:(r['repeat'],r['fold'],r['variant'],r['inner_fold']))
        for name,value in [('tuning',tuning),('training-contexts',contexts)]:
            (out/f'{name}.json').write_text(json.dumps(value,indent=2),encoding='utf-8')
        selected=pd.DataFrame([{'repeat':r['repeat'],'fold':r['fold'],'variant':r['variant'],'variable':col}
            for r in contexts if r['inner_fold']==0 for col in r['columns']])
        selected.to_csv(out/'selected-inputs.csv',index=False)
        selected.groupby(['variant','variable']).size().rename('outer_fits_selected').to_csv(out/'selection-frequency.csv')
        summary=report(result,out)
        assert all(training.sha256(ROOT/p)==h for p,h in hashes.items())
        manifest.update(status='complete',source_files_unchanged=True,reference_folds_reproduced=True,
                        current8_scores_reproduced=True,inner_fits=inner_fits,outer_fits=outer_fits,
                        candidate_settings=sum(len(r['candidates']) for r in tuning),real_participants=97)
    except Exception as exc:
        manifest.update(status='failed',error=str(exc));raise
    finally:
        manifest['finished_utc']=datetime.now(timezone.utc).isoformat();mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(f'Complete: {out}\n{summary[["recall","precision","f2","tp","fp"]].to_string()}',flush=True)


if __name__=='__main__':main()
