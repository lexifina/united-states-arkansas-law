# How this repository was made (United States (Arkansas))

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Arkansas Acts of the 2025 Regular Session (arkleg.state.ar.us) | <https://arkleg.state.ar.us/Acts> | 2026-10-30 | *  Allow: /" (only ChatGPT-User and ChatGPT are disallowed). The Bureau's Acts carry no copyright claim; the Arkansas Code and the Constitution are published on a LexisNexis site and are not used. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue-2025r` | Catalogue of Acts 1 to 301 of the Arkansas 2025 Regular Session (number, bill, title and approval date only; no Act text) | 16 | 2025-01-16 to 2025-03-18 |

The build made 16 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 15 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 16 laws in the record.
- 32 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Catalogue entries are dated by the day the Governor approved the Act (the "APPROVED" line printed on the Act). https://arkleg.state.ar.us/Acts

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `1927f543adb872b61172a4b5a3121ff0dc1b0ed56d6c2d79eccdfb9c47878c0b` (187947 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Metadata only, no law text: the Arkansas Code and the Constitution of 1874 are published for free access on a LexisNexis site (advance.lexis.com) under its terms, which this build does not use; the Acts are published as bills in the Legislature's strike-and-underline format, whose deleted and added wording a text extraction cannot tell apart reliably, so no Act text is copied.
- The first 301 Acts of the session (Act numbers 1 to 301) are catalogued; the later Acts are not yet.
- One catalogue entry per Act of the 2025 Regular Session: Act number, bill number, title as printed on the Act, approval date and the official PDF address; each version adds the Acts approved on one date, dated that day.
- The date is the "APPROVED" date printed on the Act, not the day the Act takes effect (most Arkansas Acts take effect later, or on a date they name).
- Acts with no APPROVED line or no readable title are left out: [48].

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
