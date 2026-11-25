#!/usr/bin/env python3
"""Validate a translation file against it.json.  usage: python3 validate.py <lang> [<lang> ...]"""
import json, re, sys, os
B = os.path.dirname(os.path.abspath(__file__))
IT = json.load(open(os.path.join(B, 'i18n', 'it.json'), encoding='utf-8'))
PH = re.compile(r'\{[a-z]+\}')
TAG = re.compile(r'<[^>]+>')
def walk(a, b, path, errs, warns):
    if type(a) != type(b):
        errs.append(f'{path}: type {type(b).__name__} != {type(a).__name__}'); return
    if isinstance(a, dict):
        for k in a:
            if k not in b: errs.append(f'{path}.{k}: missing')
            else: walk(a[k], b[k], f'{path}.{k}', errs, warns)
        for k in b:
            if k not in a: errs.append(f'{path}.{k}: extra key')
    elif isinstance(a, list):
        if len(a) != len(b): errs.append(f'{path}: list length {len(b)} != {len(a)}')
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f'{path}[{i}]', errs, warns)
    elif isinstance(a, str):
        if not b.strip(): errs.append(f'{path}: empty')
        if sorted(PH.findall(a)) != sorted(PH.findall(b)): errs.append(f'{path}: placeholders {PH.findall(b)} != {PH.findall(a)}')
        if sorted(TAG.findall(a)) != sorted(TAG.findall(b)): errs.append(f'{path}: html tags differ: {TAG.findall(b)} vs {TAG.findall(a)}')
        if len(a) > 25 and a == b and path not in ('.js.lbl[5]',): warns.append(f'{path}: identical to Italian')
def check(code):
    p = os.path.join(B, 'i18n', code + '.json')
    try: d = json.load(open(p, encoding='utf-8'))
    except Exception as e: return [f'cannot load: {e}'], []
    errs, warns = [], []
    walk(IT, d, '', errs, warns)
    if d.get('_lang') != code: errs.append(f'_lang must be "{code}"')
    try:
        slugs = [v['slug'] for v in d['pages'].values()]
        for s in slugs:
            if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', s): errs.append(f'bad slug {s!r} (ascii a-z 0-9 and hyphens only)')
        if len(set(slugs)) != len(slugs): errs.append('duplicate slugs')
        if code in d['pages'] and False: pass
        st = d['home']['h025']
        if st.count('*') < 2: errs.append('home.h025 must keep at least two *marked* words')
        if len(d['js']['avail']) > 12: errs.append('js.avail longer than 12 characters')
        if len(d['meta']['title']) > 70: warns.append(f'meta.title is {len(d["meta"]["title"])} chars (aim <= 65)')
        if len(d['meta']['desc']) > 175: warns.append(f'meta.desc is {len(d["meta"]["desc"])} chars (aim <= 160)')
        for k, v in d['pages'].items():
            if len(v['title']) > 75: warns.append(f'pages.{k}.title is {len(v["title"])} chars (aim <= 65)')
    except Exception as e: errs.append(f'structure: {e}')
    return errs, warns
ok = True
for code in sys.argv[1:]:
    e, w = check(code)
    print(f'== {code}: {"OK" if not e else str(len(e)) + " ERRORS"}, {len(w)} warnings')
    for x in e[:60]: print('  ERROR', x)
    for x in w[:30]: print('  warn ', x)
    ok = ok and not e
sys.exit(0 if ok else 1)
