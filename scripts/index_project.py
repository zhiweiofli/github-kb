"""Issue -> public repository evidence -> DeepSeek -> Markdown catalogue."""
import base64
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('summary', 'use_cases', 'strengths', 'limitations', 'when_to_revisit', 'topics')


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)


def api(path):
    return json.loads(gh('api', path))


def parse(body):
    match = re.search(r'### GitHub repository\s+https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/?\s*(?=###|$)', body)
    if not match:
        raise ValueError('Use the Add project issue form with one GitHub repository URL')
    name = match[1].removesuffix('.git')
    if any(part in ('.', '..') for part in name.split('/')):
        raise ValueError('Invalid repository')
    reason = body.split('### Why I care', 1)[-1].strip() if '### Why I care' in body else ''
    return name, reason[:4000]


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected JSON object')
    for key in FIELDS:
        value = data.get(key)
        if key == 'summary':
            valid = isinstance(value, str) and bool(value.strip())
        else:
            valid = isinstance(value, list) and 1 <= len(value) <= 10 and all(isinstance(x, str) and x.strip() for x in value)
        if not valid:
            raise ValueError('Invalid model field: ' + key)
    return data


def analyze(evidence):
    key = os.environ.get('DEEPSEEK_API_KEY')
    if not key:
        raise ValueError('Configure the DEEPSEEK_API_KEY Actions secret')
    payload = {
        'model': os.environ.get('DEEPSEEK_MODEL', 'deepseek-v4-flash'),
        'thinking': {'type': 'disabled'},
        'messages': [
            {'role': 'system', 'content': (ROOT / 'rules/analysis.md').read_text()},
            {'role': 'user', 'content': json.dumps(evidence, ensure_ascii=False)},
        ],
        'response_format': {'type': 'json_object'},
        'max_tokens': 4000,
    }
    req = urllib.request.Request('https://api.deepseek.com/chat/completions',
        data=json.dumps(payload).encode(), headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=180) as response:
        result = json.load(response)
    choice = result['choices'][0]
    if choice.get('finish_reason') != 'stop':
        raise ValueError('Model output incomplete')
    return validate(json.loads(choice['message']['content'])), result.get('model', payload['model'])


def line(value):
    # Plain text prevents model-generated HTML/images/links in the catalogue.
    import html
    return html.escape(' '.join(str(value).split())).replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;')


def write_card(root, metadata, analysis, reason, issue_url, model, readme_sha, truncated):
    folder = root / 'projects'
    folder.mkdir(exist_ok=True)
    name = metadata['full_name']
    filename = name.lower().replace('/', '--') + '.md'
    path = folder / filename
    if path.exists():
        return path
    header = {'status': 'indexed', 'source': metadata['html_url'], 'repository': name,
              'summary': analysis['summary'], 'topics': analysis['topics'], 'assessment': 'not-tested'}
    text = '---\n' + '\n'.join(k + ': ' + json.dumps(v, ensure_ascii=False) for k, v in header.items()) + '\n---\n\n'
    text += f'# {name}\n\n- GitHub: {metadata["html_url"]}\n- Local: not cloned\n- Status: LATER（初评，未试用）\n'
    text += f'- 来源 Issue: {issue_url}\n- 评估日期: {datetime.date.today().isoformat()}\n- 模型: {line(model)}\n'
    text += f'- README blob: {readme_sha}；输入截断: {truncated}\n- License: {line((metadata.get("license") or {}).get("spdx_id", "UNKNOWN"))}\n'
    text += '\n## 我关注的原因\n\n' + line(reason or '未提供，不推测个人偏好') + '\n\n## 一句话说明\n\n' + line(analysis['summary']) + '\n'
    for field, title in [('use_cases', '适用场景'), ('strengths', '项目宣称的能力'), ('limitations', '限制与待验证'), ('when_to_revisit', '什么情况下重新考虑'), ('topics', '检索关键词')]:
        text += '\n## ' + title + '\n\n' + '\n'.join('- ' + line(x) for x in analysis[field]) + '\n'
    path.write_text(text)
    return path


def build_index(root):
    rows = ['# 自动项目索引', '', '初步评估，不代表已试用或已采用。历史项目另见 [原索引](../INDEX.md)。', '', '| 项目 | 用途 | 关键词 |', '|---|---|---|']
    for path in sorted((root / 'projects').glob('*.md')):
        if path.name == 'INDEX.md':
            continue
        front = path.read_text().split('---', 2)[1]
        meta = {k: json.loads(v) for k, v in (s.split(': ', 1) for s in front.strip().splitlines())}
        rows.append(f'| [{line(meta["repository"])}]({path.name}) | {line(meta["summary"])} | {line(", ".join(meta["topics"]))} |')
    (root / 'projects/INDEX.md').write_text('\n'.join(rows) + '\n')


def main():
    repo = os.environ['GITHUB_REPOSITORY']
    number = int(os.environ['ISSUE_NUMBER'])
    issue = api(f'repos/{repo}/issues/{number}')
    if issue['user']['login'].lower() != repo.split('/')[0].lower() or 'pull_request' in issue:
        raise ValueError('Only repository owner project issues are supported')
    requested, reason = parse(issue.get('body') or '')
    metadata = api('repos/' + requested)
    if metadata['private']:
        raise ValueError('Only public source repositories may be sent to DeepSeek')
    canonical = metadata['full_name']
    path = ROOT / 'projects' / (canonical.lower().replace('/', '--') + '.md')
    if not path.exists():
        readme = api('repos/' + canonical + '/readme')
        raw = base64.b64decode(readme['content']).decode('utf-8', errors='replace')
        evidence = {'repository': canonical, 'description': metadata.get('description'),
                    'license': metadata.get('license'), 'archived': metadata['archived'],
                    'pushed_at': metadata['pushed_at'], 'interest': reason,
                    'readme': raw[:40000], 'readme_truncated': len(raw) > 40000}
        data, model = analyze(evidence)
        path = write_card(ROOT, metadata, data, reason, issue['html_url'], model, readme['sha'], len(raw) > 40000)
    build_index(ROOT)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write('card=' + path.relative_to(ROOT).as_posix() + '\n')


if __name__ == '__main__':
    main()
