"""Adapt the existing research utilities to the organized repository layout."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]

def main():
    for folder in ['corpus','surveys']:
        for path in (ROOT/'scripts'/folder).glob('*.py'):
            t=path.read_text(encoding='utf-8')
            if 'from repo_paths import resolve_source' in t or 'from collect_surveys import DATA, resolve_source,' in t:
                continue
            t=t.replace("ROOT/'top_100_papers", "ROOT/'papers/corpus")
            t=t.replace("ROOT/'review_revision/search_exports", "ROOT/'data/searches/first_pass")
            t=t.replace("ROOT/'review_revision/", "ROOT/'data/audit/")
            if folder=='corpus':
                t=t.replace("ROOT/'archive'", "ROOT/'data/searches/initial'")
                t=t.replace("folder=OUT/'search_exports'", "folder=ROOT/'data/searches/first_pass'")
                if path.name=='audit_corpus.py':
                    t=t.replace('ROOT = Path(__file__).resolve().parents[1]', 'ROOT = Path(__file__).resolve().parents[2]')
                    t=t.replace('OUT = Path(__file__).resolve().parent', "OUT = ROOT/'data/audit'")
                    t=t.replace('from pypdf import PdfReader', 'from pypdf import PdfReader\nimport sys\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom repo_paths import resolve_source')
                    t=t.replace("path = ROOT/'papers/corpus'/record['file_name']", "path = resolve_source(ROOT/'papers/corpus'/record['file_name'])")
                if path.name=='verify_sources.py':
                    t=t.replace('from audit_corpus import rows, write_csv, ROOT, OUT', 'from audit_corpus import rows, write_csv, ROOT, OUT, resolve_source')
                    t=t.replace("(OUT/'fulltext_xml'/f'{int(rank):03d}.xml').write_bytes", "resolve_source(OUT/'fulltext_xml'/f'{int(rank):03d}.xml').write_bytes")
                if path.name=='retrieve_additions.py':
                    t=t.replace('from audit_corpus import OUT, write_csv', 'from audit_corpus import OUT, write_csv, resolve_source')
                    t=t.replace("(folder/(pmid+'.xml')).write_bytes", "resolve_source(folder/(pmid+'.xml')).write_bytes")
            else:
                t=re.sub(r"LR/'([^/']+\.(?:csv|json))'", r"DATA/'\1'", t)
                t=t.replace("folder=LR/'novelty_exports'", "folder=ROOT/'data/searches/novelty'")
                if path.name=='check_novelty.py':t=t.replace('from collect_surveys import LR,', 'from collect_surveys import ROOT,LR,')
                if path.name=='collect_surveys.py':
                    t=t.replace("LR=ROOT/'LR'; SURVEYS=LR/'Surveys'; RAW=LR/'search_exports'", "LR=ROOT/'LR'; SURVEYS=LR/'Surveys'; DATA=ROOT/'data/reviews'; RAW=ROOT/'data/searches/reviews'")
                    t=t.replace('import requests', 'import requests\nimport sys\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom repo_paths import resolve_source')
                    t=t.replace("RAW.mkdir(parents=True,exist_ok=True);SURVEYS.mkdir(exist_ok=True)", "RAW.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=True);SURVEYS.mkdir(parents=True,exist_ok=True)")
                else:
                    t=t.replace('from collect_surveys import ', 'from collect_surveys import DATA, resolve_source, ')
                if path.name=='extract_dimensions.py':
                    t=t.replace("SURVEYS/'source_text'", "DATA/'pdf_text'")
                if path.name=='build_survey_library.py':
                    t=t.replace("p=ROOT/'papers/corpus'/m['file_name'];dest=folder/(pid+'.pdf');shutil.copy2(p,dest);", "p=resolve_source(ROOT/'papers/corpus'/m['file_name']);dest=folder/(pid+'.pdf');\n        if p.resolve()!=dest.resolve():shutil.copy2(p,dest)\n        ")
                    t=t.replace('for p in candidates:\n        if p.exists()', 'for p in candidates:\n        p=resolve_source(p)\n        if p.exists()')
            compile(t,str(path),'exec')
            path.write_text(t,encoding='utf-8')
    print('Updated research script paths; syntax checked without running network operations.')

if __name__=='__main__':main()
