"""One-time, workspace-contained repository reorganization with a saved move log."""
import argparse, csv, hashlib, io, json, os, re, shutil
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / 'data/maintenance/reorganization.json'

def safe(path):
    resolved=path.resolve()
    if not resolved.is_relative_to(ROOT.resolve()) or resolved==ROOT.resolve():
        raise ValueError('Path outside workspace or workspace root: '+str(path))
    if path.is_symlink():raise ValueError('Refusing symlink: '+str(path))
    return resolved

def target(rel, classes):
    s=rel.as_posix()
    special={
      'LITERATURE_REVIEW.md':'archive/drafts/literature_review.md',
      'RESEARCH_PROGRESS.md':'archive/drafts/research_progress.md',
      'Top_30_Paper_Summaries.md':'archive/drafts/top_30_summaries.md',
      'pdf_audit_results.csv':'archive/audits/initial_pdf_audit.csv',
      'archive/README.md':'data/searches/initial/README.md',
      'top_100_papers/orthopedic_ai_papers_summary.md':'archive/drafts/corpus_summaries.md',
    }
    if s in special:return special[s]
    if len(rel.parts)==1 and rel.suffix=='.xlsx':return 'archive/workbooks/'+rel.name
    if s.startswith('archive/') and rel.suffix=='.csv':return 'data/searches/initial/'+rel.name
    if s.startswith('Orthopedic_AI_Literature_Review/'):
        if rel.suffix=='.xlsx':return 'archive/workbooks/earlier_'+rel.name
        if 'archive_raw_reports' in rel.parts:return 'archive/drafts/raw_reports/'+rel.name
        return 'archive/drafts/earlier_review/'+rel.name
    if s.startswith('top_100_papers/'):
        kind=classes.get(rel.name)
        if kind=='local_summary_sheet':return 'archive/generated_summaries/'+rel.name
        if kind=='wrong_document_confirmed':return 'archive/rejected_sources/'+rel.name
        return 'papers/corpus/'+rel.name
    if s.startswith('review_revision/'):
        rest=Path(*rel.parts[1:])
        if rest.parts[0]=='search_exports':return 'data/searches/first_pass/'+Path(*rest.parts[1:]).as_posix()
        if rel.suffix=='.py':return 'scripts/corpus/'+rel.name
        if len(rest.parts)==1 and rel.suffix=='.md':return 'research/audit/'+rel.name
        return 'data/audit/'+rest.as_posix()
    if s.startswith('LR/search_exports/'):return 'data/searches/reviews/'+Path(*rel.parts[2:]).as_posix()
    if s.startswith('LR/novelty_exports/'):return 'data/searches/novelty/'+Path(*rel.parts[2:]).as_posix()
    if s.startswith('LR/tools/'):return 'scripts/surveys/'+rel.name
    if s.startswith('LR/Surveys/source_text/'):return 'data/reviews/pdf_text/'+rel.name
    if len(rel.parts)==2 and rel.parts[0]=='LR' and rel.suffix in ('.csv','.json'):
        return 'data/reviews/'+rel.name
    return s

def priority(old,new):
    if new.startswith('LR/Surveys/sources/'):return (0,new)
    if new.startswith('papers/'):return (1,new)
    if new.startswith('data/'):return (2,new)
    return (3,new)

def plan():
    if LOG.exists():raise RuntimeError('This migration already ran; inspect its log rather than repeat it.')
    with (ROOT/'review_revision/corpus_audit.csv').open(encoding='utf-8-sig',newline='') as f:
        classes={r['file_name']:r['document_class'] for r in csv.DictReader(f)}
    items=[];groups=defaultdict(list)
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or '.git' in p.relative_to(ROOT).parts:continue
        safe(p);rel=p.relative_to(ROOT);old=rel.as_posix()
        cache='__pycache__' in rel.parts or rel.suffix=='.pyc'
        generated=old.startswith('LR/Surveys/source_text/')
        item={'old':old,'new':target(rel,classes),'bytes':p.stat().st_size,
              'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'action':'remove_cache' if cache else 'remove_regenerable_text' if generated else 'keep'}
        items.append(item)
        if not cache and not generated and p.suffix.lower() in ('.pdf','.xml','.xlsx'):
            groups[item['sha256']].append(item)
    for group in groups.values():
        if len(group)<2:continue
        keep=min(group,key=lambda x:priority(x['old'],x['new']))
        for item in group:
            if item is keep:continue
            item['action']='remove_exact_duplicate';item['canonical']=keep['new']
    destinations=[i['new'] for i in items if i['action']=='keep']
    if len(destinations)!=len(set(destinations)):raise ValueError('Destination collision')
    for item in items:safe(ROOT/item['old']);safe(ROOT/item.get('canonical',item['new']))
    return items

def update_links(text,old,new,mapping):
    def replace(m):
        raw=m.group(1);target_text=raw.strip('<>')
        if re.match(r'^(?:https?:|mailto:|plugin:|app:|#)',target_text):return m.group(0)
        base,mark,fragment=target_text.partition('#')
        try:
            resolved=(ROOT/old).parent.joinpath(unquote(base)).resolve()
            if not resolved.is_relative_to(ROOT):return m.group(0)
            key=resolved.relative_to(ROOT).as_posix()
        except (ValueError,OSError):return m.group(0)
        if key not in mapping:return m.group(0)
        dest=ROOT/mapping[key]
        rel=os.path.relpath(dest,(ROOT/new).parent).replace('\\','/')
        if mark:rel+='#'+fragment
        if ' ' in rel:rel='<'+rel+'>'
        return ']('+rel+')'
    return re.sub(r'\]\(([^)]+)\)',replace,text)

def rewrite_value(value,mapping):
    if isinstance(value,str):
        norm=value.replace('\\','/')
        return mapping.get(norm,value)
    if isinstance(value,list):return [rewrite_value(x,mapping) for x in value]
    if isinstance(value,dict):return {k:rewrite_value(v,mapping) for k,v in value.items()}
    return value

def apply(items):
    mapping={i['old']:i.get('canonical',i['new']) for i in items if i['action'] not in ('remove_cache','remove_regenerable_text')}
    aliases={k:v for k,v in mapping.items() if k!=v}
    for i in items:
        if i['action']=='remove_exact_duplicate':aliases[i['new']]=i['canonical']
        if i['old'].startswith('top_100_papers/'):
            fallback='papers/corpus/'+Path(i['old']).name
            if fallback!=mapping.get(i['old']):aliases[fallback]=mapping[i['old']]
    # Move first; every delete must still have a byte-identical surviving copy.
    for i in items:
        if i['action']!='keep' or i['old']==i['new']:continue
        src=safe(ROOT/i['old']);dst=safe(ROOT/i['new'])
        if dst.exists():raise FileExistsError(dst)
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(src),str(dst))
    for i in items:
        if i['action']=='keep':continue
        src=safe(ROOT/i['old'])
        if i['action']=='remove_exact_duplicate':
            kept=safe(ROOT/i['canonical'])
            if not kept.is_file() or hashlib.sha256(kept.read_bytes()).hexdigest()!=i['sha256']:
                raise ValueError('Surviving duplicate failed verification: '+i['old'])
        src.unlink()
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'data/source_aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2),encoding='utf-8')
    for i in items:
        if i['action']!='keep' or i['new'].startswith('scripts/maintenance/'):continue
        path=ROOT/i['new']
        if path.suffix=='.md':
            text=path.read_text(encoding='utf-8-sig')
            path.write_text(update_links(text,i['old'],i['new'],mapping),encoding='utf-8')
        elif path.suffix=='.csv':
            with path.open(encoding='utf-8-sig',newline='') as f:
                reader=csv.DictReader(f);fields=reader.fieldnames;records=list(reader)
            if fields:
                with path.open('w',encoding='utf-8-sig',newline='') as f:
                    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rewrite_value(records,mapping))
        elif path.suffix=='.json':
            try:data=json.loads(path.read_text(encoding='utf-8-sig'))
            except ValueError:continue
            path.write_text(json.dumps(rewrite_value(data,mapping),ensure_ascii=False,indent=2),encoding='utf-8')
    # Prune only verified empty directories inside the workspace.
    for d in sorted((p for p in ROOT.rglob('*') if p.is_dir()),key=lambda p:len(p.parts),reverse=True):
        if '.git' in d.relative_to(ROOT).parts:continue
        safe(d)
        if not any(d.iterdir()):d.rmdir()
    LOG.parent.mkdir(parents=True,exist_ok=True)
    report={'date':'2026-10-24','root':str(ROOT),'items':items,
            'files_moved':sum(i['action']=='keep' and i['old']!=i['new'] for i in items),
            'exact_duplicate_copies_removed':sum(i['action']=='remove_exact_duplicate' for i in items),
            'cache_files_removed':sum(i['action']=='remove_cache' for i in items),
            'regenerable_text_files_removed':sum(i['action']=='remove_regenerable_text' for i in items),
            'bytes_removed':sum(i['bytes'] for i in items if i['action']!='keep')}
    LOG.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='items'},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    items=plan()
    if args.apply:apply(items)
    else:
        print(json.dumps({'files':len(items),'moves':sum(i['old']!=i['new'] and i['action']=='keep' for i in items),
                          'duplicate_copies':sum(i['action']=='remove_exact_duplicate' for i in items),
                          'cache_files':sum(i['action']=='remove_cache' for i in items),
                          'regenerable_text_files':sum(i['action']=='remove_regenerable_text' for i in items),
                          'bytes_removable':sum(i['bytes'] for i in items if i['action']!='keep')},indent=2))
