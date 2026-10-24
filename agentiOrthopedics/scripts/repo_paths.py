"""Shared workspace paths and aliases for consolidated source copies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def resolve_source(path):
    candidate=Path(path)
    if not candidate.is_absolute():candidate=ROOT/candidate
    candidate=candidate.resolve()
    if not candidate.is_relative_to(ROOT):raise ValueError('Source path outside repository')
    aliases_file=ROOT/'data/source_aliases.json'
    aliases=json.loads(aliases_file.read_text(encoding='utf-8')) if aliases_file.exists() else {}
    seen=set()
    while not candidate.exists():
        key=candidate.relative_to(ROOT).as_posix()
        if key in seen:raise ValueError('Cyclic source alias: '+key)
        seen.add(key)
        if key not in aliases:return candidate
        candidate=(ROOT/aliases[key]).resolve()
        if not candidate.is_relative_to(ROOT):raise ValueError('Source alias outside repository')
    return candidate
