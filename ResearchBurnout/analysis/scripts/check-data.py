from __future__ import print_function
import ctypes as c
import os, struct, json, collections, csv

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_FILES = {
    'burnout-before-corrections.sav': os.path.join(ROOT, 'archive', 'data', 'burnout-before-corrections.sav'),
    'burnout-data.sav': os.path.join(ROOT, 'data', 'prepared', 'burnout-data.sav'),
}
os.chdir(r'C:\Program Files\IBM\SPSS\Statistics\23')
d = c.CDLL('spssio64.dll')
d.spssSetInterfaceEncoding(1)

def read(name):
    h=c.c_int()
    rc=d.spssOpenRead(DATA_FILES[name].encode('utf-8'),c.byref(h))
    if rc: raise RuntimeError(('open',rc))
    n=c.c_int(); names=c.POINTER(c.c_char_p)(); types=c.POINTER(c.c_int)()
    rc=d.spssGetVarNames(h,c.byref(n),c.byref(names),c.byref(types))
    if rc: raise RuntimeError(('dictionary',rc))
    fields=[(names[i].decode('utf-8'),types[i]) for i in range(n.value)]
    size=c.c_long(); rc=d.spssGetCaseSize(h,c.byref(size))
    if rc: raise RuntimeError(('case size',rc))
    buf=c.create_string_buffer(size.value); rows=[]
    while True:
        rc=d.spssWholeCaseIn(h,buf)
        if rc == -5: break
        if rc: raise RuntimeError(('read',rc))
        pos=0; row={}
        for var,t in fields:
            if t:
                row[var]=buf.raw[pos:pos+t].decode('utf-8').rstrip(' \x00')
                pos+=((t+7)//8)*8
            else:
                row[var]=struct.unpack_from('d',buf.raw,pos)[0]; pos+=8
        rows.append(row)
    metadata={}
    for var,t in fields:
        vb=var.encode('utf-8'); level=c.c_int(); fmt=c.c_int(); width=c.c_int(); decimals=c.c_int()
        rc=d.spssGetVarMeasureLevel(h,vb,c.byref(level))
        if rc: raise RuntimeError(('measure',var,rc))
        rc=d.spssGetVarPrintFormat(h,vb,c.byref(fmt),c.byref(decimals),c.byref(width))
        if rc: raise RuntimeError(('format',var,rc))
        item={'type':t,'measure':level.value,'decimals':decimals.value}
        if not t:
            vals=c.POINTER(c.c_double)(); labels=c.POINTER(c.c_char_p)(); count=c.c_int()
            rc=d.spssGetVarNValueLabels(h,vb,c.byref(vals),c.byref(labels),c.byref(count))
            if rc not in (0,-8): raise RuntimeError(('labels',var,rc))
            item['value_labels']={str(vals[j]):labels[j].decode('utf-8') for j in range(count.value)}
        metadata[var]=item
    d.spssCloseRead(h)
    if name=='burnout-data.sav':
        with open(os.path.join(ROOT,'analysis','checks','variable-metadata.json'),'w', encoding='utf-8') as f:
            f.write(json.dumps(metadata,indent=2,ensure_ascii=True))
    return fields,rows

af,a=read('burnout-before-corrections.sav'); bf,b=read('burnout-data.sav')
out={'original_rows':len(a),'prepared_rows':len(b),'original_variables':len(af),'prepared_variables':len(bf)}
out['changed_original_cells']=[(i+1,k) for i,(x,y) in enumerate(zip(a,b)) for k in x if x[k]!=y[k]]
out['new_variables']=[k for k,t in bf if k not in a[0]]
out['mappings']={}
for old,new in [('eligible','enrolled_lebanon'),('academic_level','academic_level_code'),('major','major_code'),('GPA','gpa_code'),('electricity','electricity_code'),('study_hours','study_hours_code'),('sleep_duration','sleep_duration_code')]:
    counts=collections.Counter((r[old],r[new]) for r in b)
    out['mappings'][new]=[{'answer':x,'code':y,'n':n} for (x,y),n in sorted(counts.items())]
uses={'ai_use_concepts':'Concept explanation & brainstorming','ai_use_writing':'Essay writing, grammar polishing, or drafting','ai_use_coding':'Coding, debugging, or technical problem solving','ai_use_summaries':'Summarizing articles / lecture slides','ai_use_solutions':'Direct solution generation for assignments/homework'}
out['ai_indicator_errors']=[(i+1,k) for i,r in enumerate(b) for k,v in uses.items() if r[k]!=int(v in r['ai_use_cases'].split(';'))]
out['ai_indicator_counts']={k:sum(r[k] for r in b) for k in uses}
out['ai_selection_count_distribution']=dict(collections.Counter(sum(r[k] for k in uses) for r in b))
groups={'exhaustion':[21,23,24],'mental_distance':[29,31,33],'cognitive_impairment':[34,37,38],'emotional_impairment':[39,40,43],'exhaustion_23':list(range(21,29)),'mental_distance_23':list(range(29,34)),'congnitive_impairement_23':list(range(34,39)),'emotional_impairment_23':list(range(39,44))}
out['score_errors']=[]
for i,r in enumerate(b):
    for k,items in groups.items():
        expected=sum(r['BAT'+str(j)] for j in items)/float(len(items))
        if abs(r[k]-expected)>1e-10: out['score_errors'].append((i+1,k))
    for score,ks in [('burnout_score',['exhaustion','mental_distance','cognitive_impairment','emotional_impairment']),('burnout_score_23',['exhaustion_23','mental_distance_23','congnitive_impairement_23','emotional_impairment_23'])]:
        if all(r[k]>-1e300 for k in ks) and abs(r[score]-sum(r[k] for k in ks)/4)>1e-10: out['score_errors'].append((i+1,score))
    expected12=sum(r['BAT'+str(j)] for j in [21,23,24,29,31,33,34,37,38,39,40,43])/12.0
    if abs(r['burnout_score']-expected12)>1e-10: out['score_errors'].append((i+1,'burnout_score_vs_items'))
out['numeric_missing']={k:sum(r[k]<-1e300 for r in b) for k,t in bf if not t and any(r[k]<-1e300 for r in b)}
out['affected_rows']=[{'row':i+1,'timestamp':r['Timestamp'],'internet':r['internet'],'BAT39':r['BAT39'],'BAT40':r['BAT40'],'BAT43':r['BAT43'],'emotional_impairment':r['emotional_impairment'],'burnout_score':r['burnout_score'],'expected_burnout':sum(r['BAT'+str(j)] for j in [21,23,24,29,31,33,34,37,38,39,40,43])/12.0} for i,r in enumerate(b) if r['internet'] < -1e300 or r['emotional_impairment'] < -1e300]
with open(os.path.join(ROOT,'data','raw','survey-export-spss.csv'),'r', encoding='utf-8-sig', newline='') as f:
    raw=list(csv.reader(f)); headers=raw.pop(0)
out['raw_numeric_differences']=[]
for i,(r,source) in enumerate(zip(b,raw)):
    assert r['Timestamp']==source[0]
    for j,(k,t) in enumerate(af[:44]):
        if not t and r[k]!=float(source[j]):
            out['raw_numeric_differences'].append({'row':i+1,'variable':k,'raw_answer':source[j]})
with open(os.path.join(ROOT,'analysis','checks','data-checks.json'),'w', encoding='utf-8') as f:
    f.write(json.dumps(out,indent=2,ensure_ascii=True))
print(json.dumps(out,indent=2,ensure_ascii=True))
