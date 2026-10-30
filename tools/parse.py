"""Build corpus.json (a facts-only catalogue of the Acts of the Arkansas 2025 Regular Session) from the cached Act facts. No network."""
import json
import os
import re
import sys
from pathlib import Path

from state_lib import norm, sha, write_corpus  # noqa: F401

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = Path(HERE) / '.cache'
RETRIEVED = '2026-10-30'
SITE = 'https://arkleg.state.ar.us/'


def iso(s):
    m = re.match(r'(\d{1,2})/(\d{1,2})/(\d{2,4})$', s)
    y = int(m.group(3))
    y = y + 2000 if y < 100 else y
    return f'{y:04d}-{int(m.group(1)):02d}-{int(m.group(2)):02d}'


def main():
    recs = []
    for p in CACHE.glob('act*.json'):
        r = json.loads(p.read_text('utf8'))
        if not r.get('missing'):
            recs.append(r)
    recs.sort(key=lambda r: r['n'])
    skipped = [r['n'] for r in recs if not r.get('approved') or not r.get('title')]
    recs = [r for r in recs if r.get('approved') and r.get('title')]
    laws, by = {}, {}
    for r in recs:
        d = iso(r['approved'])
        lk = f'catalogue-{d}'
        laws.setdefault(lk, {'label': f'Acts approved {d}', 'title': f'Acts of the 2025 Regular Session approved on {d}', 'kind': 'law',
                             'enacted': d, 'published': d, 'url': SITE + 'Acts/SearchByRange?ddBienniumSession=2025%2F2025R',
                             'temporary_until': None, 'restores': None,
                             'note': 'Acts entered in this catalogue on the day the Governor approved them (or they became law); metadata only.'})
        text = '\n'.join([f"# Act {r['n']} of the 2025 Regular Session", f"Bill: {r['bill'] or 'not recorded'}", f"Title: {norm(r['title'])}",
                          f"Approved: {d}", f"Official PDF: {r['url'].replace('/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT', '/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2F&file=').replace('.pdf', '.pdf')}"]) + '\n'
        by.setdefault(d, []).append((f"act-2025r-{r['n']:04d}", {'label': f"Act {r['n']} (2025 Regular Session)", 'kind': 'law', 'text': text}, r))
    versions = []
    for i, d in enumerate(sorted(by)):
        items = sorted(by[d], key=lambda t: t[0])
        v = {'from': d, 'source_url': SITE + 'Acts/SearchByRange?ddBienniumSession=2025%2F2025R',
             'sha256': sha(json.dumps([t[2]['sha256'] for t in items]).encode()), 'credits': {k: [f'catalogue-{d}'] for k, _, _ in items}}
        body = {k: u for k, u, _ in items}
        v['units' if i == 0 else 'changes'] = body
        versions.append(v)
    act = {'slug': 'catalogue-2025r', 'short': 'Acts 2025R catalogue',
           'title': f'Catalogue of Acts 1 to {recs[-1]["n"]} of the Arkansas 2025 Regular Session (number, bill, title and approval date only; no Act text)',
           'url': SITE + 'Acts/SearchByRange?ddBienniumSession=2025%2F2025R', 'first_law': f'catalogue-{sorted(by)[0]}', 'earlier_laws': [], 'versions': versions}
    country = {'code': 'US-AR', 'name': 'United States (Arkansas)', 'slug': 'united-states-arkansas', 'lang': 'en',
               'tz': 'America/Chicago', 'future_branch': 'future',
               'publisher': {'name': 'Arkansas State Legislature, Bureau of Legislative Research', 'email': 'acts@arkleg-state-ar-us.invalid'},
               'default_in_force_rule': {'text': 'Catalogue entries are dated by the day the Governor approved the Act (the "APPROVED" line printed on the Act).',
                                         'source': SITE + 'Acts'},
               'licence_note': 'Facts about Acts (number, bill, title, approval date) only; no Act text. Source: Arkansas State Legislature, Bureau of Legislative Research.'}
    sources = [{'name': 'Arkansas Acts of the 2025 Regular Session (arkleg.state.ar.us)', 'url': SITE + 'Acts', 'retrieved': RETRIEVED,
                'licence': 'Only facts are copied. arkleg.state.ar.us robots.txt: "User-agent: *  Allow: /" (only ChatGPT-User and ChatGPT are disallowed). The Bureau\'s Acts carry no copyright claim; the Arkansas Code and the Constitution are published on a LexisNexis site and are not used.',
                'notes': f'{len(recs)} Acts catalogued.'}]
    decisions = [
        'Metadata only, no law text: the Arkansas Code and the Constitution of 1874 are published for free access on a LexisNexis site (advance.lexis.com) under its terms, which this build does not use; the Acts are published as bills in the Legislature\'s strike-and-underline format, whose deleted and added wording a text extraction cannot tell apart reliably, so no Act text is copied.',
        f'The first {recs[-1]["n"]} Acts of the session (Act numbers 1 to {recs[-1]["n"]}) are catalogued; the later Acts are not yet.',
        'One catalogue entry per Act of the 2025 Regular Session: Act number, bill number, title as printed on the Act, approval date and the official PDF address; each version adds the Acts approved on one date, dated that day.',
        'The date is the "APPROVED" date printed on the Act, not the day the Act takes effect (most Arkansas Acts take effect later, or on a date they name).',
        f'Acts with no APPROVED line or no readable title are left out: {skipped if skipped else "none"}.']
    c = {'country': country, 'sources': sources, 'laws': laws, 'acts': [act], 'applies': [], 'decisions': decisions, 'ai_use': ['none']}
    out = os.path.join(HERE, 'corpus.json')
    with open(out + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(c, f, ensure_ascii=False, indent=1)
        f.write('\n')
    os.replace(out + '.tmp', out)
    print(len(recs), 'acts', len(versions), 'versions', 'skipped', skipped)


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    main()
