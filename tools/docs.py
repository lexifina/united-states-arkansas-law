"""Writes repo/README.md, LICENSE, jurisdiction.json from corpus.json."""
import json
import os

from state_lib import write_docs

HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(os.path.join(HERE, 'corpus.json'), encoding='utf-8'))
a = c['acts'][0]
n = sum(len(v.get('units') or v.get('changes') or {}) for v in a['versions'])
first, last = a['versions'][0]['from'], a['versions'][-1]['from']
write_docs(HERE, {
    'name': 'United States (Arkansas)', 'state': 'Arkansas', 'code': 'US-AR', 'slug': 'arkansas',
    'domain': 'arkleg.state.ar.us',
    'acts_table': [('catalogue-2025r/', f'Catalogue of Acts 1 to {a["title"].split(" to ")[1].split(" ")[0]} of the 2025 Regular Session (metadata only, no Act text)', len(a['versions']),
                    f'{n} Acts, approved {first} to {last}')],
    'source': 'The Acts pages of the [Arkansas State Legislature](https://arkleg.state.ar.us/Acts) (Bureau of Legislative Research). English. **This repository holds metadata only, no law text.** For each catalogued Act of the 2025 Regular Session it records the Act number, the bill number, the title printed on the Act, the approval date and the address of the official PDF.',
    'dates': 'Each version adds the Acts approved on one date and is dated that day (the "APPROVED" date printed on the Act). That is the approval date, not the day the Act takes effect; most Arkansas Acts take effect later or on a date they name. The history is real but it is a history of approvals, not of the Code.',
    'limits': 'Metadata only. The Arkansas Code and the Constitution of 1874 are published for free access on a LexisNexis site under its terms, which this build does not use, and the Acts are published as bills in the Legislature\'s strike-and-underline format, whose deleted and added words a text extraction cannot reliably tell apart, so no Act text is copied. Only the first Acts of the 2025 Regular Session are catalogued (the table above says how many); the later Acts, the 2026 fiscal session and earlier sessions are not.',
    'license': """Source: Arkansas State Legislature, Bureau of Legislative Research, https://arkleg.state.ar.us/Acts (retrieved 2026-10-30).

Only facts are copied (Act number, bill number, title, approval date, address): facts are not copyrightable, and the Acts
pages state no copyright claim. arkleg.state.ar.us robots.txt reads "User-agent: *  Allow: /" and disallows only ChatGPT-User
and ChatGPT. No Act text, no Arkansas Code text and no annotation is used.""",
    'publisher': 'Arkansas State Legislature, Bureau of Legislative Research', 'build': 'built (metadata only)', 'date': '2026-10-30',
})
