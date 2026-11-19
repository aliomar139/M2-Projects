"""Check renamed imports/configs, local links, unchanged data and archived evidence."""
import ast
import csv
import hashlib
import json
from pathlib import Path
import re
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(value).hexdigest()


class RepositoryLayoutTests(unittest.TestCase):
    def test_scripts_compile_and_local_import_targets_exist(self):
        for path in sorted((ROOT/'experiments').glob('*.py')):
            text = path.read_text(encoding='utf-8')
            compile(text, str(path), 'exec')
            for node in ast.walk(ast.parse(text)):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'with_name':
                    if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                        self.assertTrue(path.with_name(node.args[0].value).is_file(), (path, node.args[0].value))
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    if node.value.startswith('experiments/') and node.value.endswith(('.py', '.json')):
                        self.assertTrue((ROOT/node.value).is_file(), (path, node.value))

    def test_dataset_bytes_and_settings_are_preserved(self):
        self.assertEqual(digest((ROOT/'data/03-prepared-student-burnout-data.sav').read_bytes()),
                         'ab50404a31ecbc7115b52fe6f0be1328128d45951deca70374e79b8ed4f4ce4a')
        self.assertEqual(digest((ROOT/'data/01-original-student-survey.csv').read_bytes()),
                         'd8d4323901dd5b6f4602c5a3b6850a965e86d1a58ec7f984b59aa05cf369830e')
        record_path = ROOT/'results/99-repository-reorganization-record.json'
        if not record_path.exists():
            self.skipTest('Local preservation archive is intentionally excluded from Git.')
        record = json.loads(record_path.read_text())
        translations = {**record['renames'], **record['output_routes']}
        def translated(value):
            if isinstance(value, str):
                for old in sorted(translations, key=len, reverse=True):
                    value = value.replace(old, translations[old])
                return value
            if isinstance(value, list):
                return [translated(v) for v in value]
            if isinstance(value, dict):
                return {key: translated(v) for key, v in value.items()}
            return value
        with zipfile.ZipFile(ROOT/'results/99-original-workspace-and-verified-validation.zip') as archive:
            for old, new in record['renames'].items():
                if new.startswith('experiments/') and new.endswith('.json'):
                    self.assertEqual(translated(json.loads(archive.read(old))), json.loads((ROOT/new).read_text()), new)
                if new.startswith('data/'):
                    self.assertEqual(digest(archive.read(old)), digest((ROOT/new).read_bytes()), new)

    def test_markdown_file_links_resolve(self):
        files = [ROOT/'README.md', *sorted((ROOT/'research').glob('*.md')), *sorted((ROOT/'results').glob('*.md'))]
        for path in files:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if re.match(r'(?:https?:|mailto:|#)', target):
                    continue
                self.assertTrue((path.parent/target.split('#')[0]).exists(), (path.name, target))

    def test_original_validation_hashes_still_verify_inside_archive(self):
        path = ROOT/'results/99-original-workspace-and-verified-validation.zip'
        if not path.exists():
            self.skipTest('Original local evidence is intentionally excluded from Git.')
        with zipfile.ZipFile(path) as archive:
            prefix = 'classification/validation-outputs/20261118T143652947217Z/'
            manifest = json.loads(archive.read(prefix+'manifest.json'))
            checks = json.loads(archive.read(prefix+'verification.json'))
            self.assertEqual(manifest['status'], 'complete')
            self.assertTrue(checks['passed'])
            self.assertEqual(checks['fold_checkpoints'], 5000)
            for name, expected in manifest['source_sha256'].items():
                self.assertEqual(digest(archive.read(name.replace('\\', '/'))), expected, name)
            for name, expected in checks['artifact_sha256'].items():
                self.assertEqual(digest(archive.read(prefix+name)), expected, name)
            self.assertEqual(digest(archive.read(prefix+'completion-audit.json')), checks['completion_audit_sha256'])
            with (ROOT/'research/12-file-renaming-catalog.csv').open(encoding='utf-8') as handle:
                catalog = list(csv.DictReader(handle))
            for entry in catalog:
                if entry['previous_path'].startswith(prefix) and entry['current_path'].endswith(('.png', '.csv', '.json')):
                    self.assertEqual(digest(archive.read(entry['previous_path'])), digest((ROOT/entry['current_path']).read_bytes()))


if __name__ == '__main__':
    unittest.main()
