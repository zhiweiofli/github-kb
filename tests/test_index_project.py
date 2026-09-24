import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('worker', Path(__file__).resolve().parents[1] / 'scripts/index_project.py')
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


class CatalogueTests(unittest.TestCase):
    def test_issue_contract(self):
        self.assertEqual(w.parse('### GitHub repository\n\nhttps://github.com/acme/tool\n\n### Why I care\n\n做采集'), ('acme/tool', '做采集'))
        with self.assertRaises(ValueError):
            w.parse('### GitHub repository\n\nhttps://evil.example/acme/tool')

    def test_card_index_and_replay(self):
        data = w.validate(dict(summary='内容采集', **{k: ['待核验'] for k in w.FIELDS if k != 'summary'}))
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            meta = {'full_name': 'acme/tool', 'html_url': 'https://github.com/acme/tool'}
            args = (root, meta, data, '用于新项目', 'https://github.com/me/kb/issues/1', 'deepseek-v4-flash', 'abc', False)
            card = w.write_card(*args)
            original = card.read_text()
            w.build_index(root)
            self.assertIn('acme--tool.md', (root / 'projects/INDEX.md').read_text())
            self.assertIn('not-tested', original)
            self.assertIn('用于新项目', original)
            data['summary'] = '不应覆盖'
            w.write_card(*args)
            self.assertEqual(card.read_text(), original)

    def test_deepseek_contract_and_invalid_result(self):
        data = dict(summary='摘要', **{k: ['测试'] for k in w.FIELDS if k != 'summary'})
        from io import BytesIO
        response = BytesIO(json.dumps({'model': 'deepseek-flash', 'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps(data)}}]}).encode())
        with patch.dict(w.os.environ, {'DEEPSEEK_API_KEY': 'fake-test-key'}), patch.object(w.urllib.request, 'urlopen', return_value=response) as request:
            result, model = w.analyze({'readme': 'example'})
            payload = json.loads(request.call_args.args[0].data)
            self.assertEqual(payload['model'], 'deepseek-v4-flash')
            self.assertEqual(payload['response_format']['type'], 'json_object')
            self.assertEqual(result, data)
            self.assertEqual(model, 'deepseek-flash')
        with self.assertRaises(ValueError):
            w.validate({'summary': '缺少必要字段'})


if __name__ == '__main__':
    unittest.main()
