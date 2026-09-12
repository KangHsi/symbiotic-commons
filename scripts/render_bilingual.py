#!/usr/bin/env python3
"""生成或核对完整中英配对文档。 / Render or check complete Chinese–English pairs."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'translations/aligned-source.json'

def validate_pair(pair):
    for language in ('zh', 'en'):
        if not isinstance(pair.get(language), str) or not pair[language].strip():
            raise ValueError(f'Missing paired text: {language}')

def render():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert data['locales'] == ['zh-Hans', 'en']
    wp = data['whitepaper']
    assert len(wp['sections']) == 8
    for key in ('title', 'subtitle', 'status'):
        validate_pair(wp[key])
    seen = set()
    for section in wp['sections']:
        validate_pair(section['title'])
        assert section['id'] not in seen
        seen.add(section['id'])
        assert section['paragraphs']
        for paragraph in section['paragraphs']:
            validate_pair(paragraph)
            assert paragraph['id'] not in seen
            seen.add(paragraph['id'])
    outputs = {}
    for locale, lang in (('zh-Hans', 'zh'), ('en', 'en'), ('bilingual', None)):
        paired = lang is None
        title = wp['title']['zh'] + ' · ' + wp['title']['en'] if paired else wp['title'][lang]
        content = [f'# {title}']
        for key in ('subtitle', 'status'):
            if paired:
                content.extend([wp[key]['zh'], wp[key]['en']])
            else:
                content.append(wp[key][lang])
        for n, section in enumerate(wp['sections'], 1):
            content.append(f'<a id="{section["id"]}"></a>')
            heading = section['title']['zh'] + ' / ' + section['title']['en'] if paired else section['title'][lang]
            content.append(f'### {n}. {heading}')
            for paragraph in section['paragraphs']:
                content.append(f'<a id="{paragraph["id"]}"></a>')
                content.extend([paragraph['zh'], paragraph['en']] if paired else [paragraph[lang]])
        nav_zh = '[中英对照](bilingual.md) · [中文全文](zh-Hans.md) · [英文全文](en.md) · [项目首页](../README.md)'
        nav_en = '[Parallel view](bilingual.md) · [Full Chinese](zh-Hans.md) · [Full English](en.md) · [Project home](../README.md)'
        content.extend([nav_zh, nav_en] if paired else [nav_zh if lang == 'zh' else nav_en])
        outputs[f'whitepaper/{locale}.md'] = '\n\n'.join(content) + '\n'
    for name, document in data['documents'].items():
        path = Path(name)
        assert not path.is_absolute() and '..' not in path.parts
        validate_pair(document['title'])
        content = []
        if document.get('frontmatter'):
            content.append('---\n' + '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in document['frontmatter'].items()) + '\n---')
        content.append(f'# {document["title"]["zh"]} · {document["title"]["en"]}')
        ids = set()
        for block in document['blocks']:
            validate_pair(block)
            assert block['id'] not in ids
            ids.add(block['id'])
            content.extend([f'<a id="{block["id"]}"></a>', block['zh'], block['en']])
        outputs[name] = '\n\n'.join(content) + '\n'
    manifest = {
        'schema_version': 2,
        'whitepaper_version': wp['version'],
        'date': wp['date'],
        'active_locales': ['zh-Hans', 'en'],
        'language_editions': 2,
        'parallel_view': 'whitepaper/bilingual.md',
        'population_coverage_target_status': 'superseded_by_D15',
        'population_coverage_claim': None,
        'review': {'zh': 'AI 辅助逐块校对；独立人工审校待完成。', 'en': 'AI-assisted block-by-block checking; independent human review pending.'},
        'source': 'translations/aligned-source.json',
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'whitepaper_paragraph_pairs': sum(len(s['paragraphs']) for s in wp['sections']),
        'documentation_block_pairs': sum(len(d['blocks']) for d in data['documents'].values()),
        'generated_files': [{'path': path, 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()} for path, text in sorted(outputs.items())]
    }
    outputs['translations/manifest.json'] = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    return outputs

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = render()
    errors = []
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != content.encode('utf-8'):
                errors.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    if errors:
        raise SystemExit('不同步 / Out of sync: ' + ', '.join(errors))
    print(f'{len(outputs)} 文件一致 / files consistent' if args.check else f'{len(outputs)} 文件已生成 / files generated')

if __name__ == '__main__':
    main()
