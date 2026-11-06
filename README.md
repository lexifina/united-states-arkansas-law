# United States (Arkansas): law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Arkansas, United States, which global-law reads at `united-states/arkansas/acts/`.

The law of Arkansas as a git history: one file per provision, with `git blame` and `git log` working line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `catalogue-2025r/` | Catalogue of Acts 1 to 301 of the 2025 Regular Session (metadata only, no Act text) | 16 | 300 Acts, approved 2025-01-16 to 2025-03-18 |

**Source.** The Acts pages of the [Arkansas State Legislature](https://arkleg.state.ar.us/Acts) (Bureau of Legislative Research). English. **This repository holds metadata only, no law text.** For each catalogued Act of the 2025 Regular Session it records the Act number, the bill number, the title printed on the Act, the approval date and the address of the official PDF.

## Dates

Each version adds the Acts approved on one date and is dated that day (the "APPROVED" date printed on the Act). That is the approval date, not the day the Act takes effect; most Arkansas Acts take effect later or on a date they name. The history is real but it is a history of approvals, not of the Code.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; the results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@arkleg.state.ar.us.invalid`). In this first build no dated history is available, so every commit is credited to the publisher as "oldest version available". The committer is always Lexifina.

## Limits

Metadata only. The Arkansas Code and the Constitution of 1874 are published for free access on a LexisNexis site under its terms, which this build does not use, and the Acts are published as bills in the Legislature's strike-and-underline format, whose deleted and added words a text extraction cannot reliably tell apart, so no Act text is copied. Only the first Acts of the 2025 Regular Session are catalogued (the table above says how many); the later Acts, the 2026 fiscal session and earlier sessions are not.
