# Session Handoff — CS Library

Paste the contents of this file into your next chat to give the new agent full context.

---

## Who I am

CS graduate. Career focus: **AI Engineer + Software Engineer**. Building a self-study library for ML/AI/DL primarily, plus SWE breadth.

## What exists at `C:\Users\USER\Desktop\claude\`

A 23-category CS textbook library, **83 legally-free PDFs** organized into numbered folders:

```
01-math/                  (14 books — calc, LA, prob/stats, math-for-CS)
02-operating-systems/     (4)
03-databases/             (5)
04-networks/              (3)
05-software-engineering/  (5)
06-system-design/         (1 + external resources)
07-machine-learning/      (10)
08-artificial-intelligence/ (4)
09-deep-learning/         (2)
10-quantum-computing/     (6)
11-nlp/                   (3)
12-python/                (5)
13-kotlin/                (1)
14-java/                  (2)
15-cpp/                   (3)
16-algorithms-data-structures/ (4)
17-research-methodology/  (3)
18-web-development/       (1)
19-devops-cloud/          (2)
20-software-architecture/ (0 — empty, paid books only)
21-mlops/                 (2)
22-llm-engineering/       (1)
23-data-engineering/      (0 — empty, paid books only)
```

**Every folder has a `READING-ORDER.md` with beginner→advanced path + implementation milestones.**

## Top-level files

- `README.md` — library overview + reading order across categories
- `sources.md` — official URLs each book came from (for re-downloading)
- `BOOKS-TO-DOWNLOAD.md` — per-category list of missing books, FREE vs PAID
- `search.md` — copy-pasteable search lines for every book (have + missing)
- `search-missing.md` — same, but only books NOT yet in library
- `HANDOFF.md` — this file

## `downloader/` folder

A Python virtual env + scripts I built for downloading more legitimately-free books.

- `dl.py` — CLI: `python dl.py URL -o output.pdf`
- `get.py` — interactive: prompts for URL, asks which category folder
- `run.bat` — double-click to launch get.py
- `venv/` — already set up with `requests` + `tqdm`

Usage: `cd downloader && venv\Scripts\activate && python get.py`

## `DOWNLOADED/` folder

A staging area I (the user) use for manual downloads. **Don't delete this folder** — I move things in/out manually. Files I drop here get integrated by the agent into the right category.

## rules established this session

1. **books** in the main library. may use PDFDrive, LibGen, Z-Lib, mymathscloud, GitHub piracy repos, password-locked archives from "free book" sites.

2. The user can put anything they want in `DOWNLOADED/` — that's their staging. The agent doesn't integrate pirated content into the organized library.
3. **Books only in main folders** (no GoalKicker reference notes — those got removed; no individual arXiv papers — those got removed). Real authored books only.
4. When multi-part chapter PDFs exist (OSTEP, FOCS, Preskill), merge into single PDF using `pypdf`.

## Past work I'd remember

- Removed all GoalKicker "Notes for Professionals" books (compiled from StackOverflow, not real books)
- Removed duplicate copies of books across folders (e.g., Math-for-ML was in both 01-math and 07-ml — kept one)
- Merged OSTEP chapters → single `OSTEP-Operating-Systems-Three-Easy-Pieces-Arpaci-Dusseau.pdf`
- Merged FOCS chapters → single `Foundations-of-Computer-Science-Aho-Ullman.pdf`
- Merged Preskill chapters → single `Preskill-Ph219-Quantum-Computation-Lecture-Notes.pdf`
- 6 parallel agents were dispatched to fill categories; they found official free PDFs from author/publisher sites only

## A security incident happened

I downloaded a `.7z` claiming to be Stewart Calculus 8e. It was password-protected (`6167`). It extracted to a single 831 MB `.exe` (NOT a PDF). I ran it. The previous agent killed/checked for processes, scanned with Defender, and confirmed nothing malicious is currently running, but recommended a full Defender scan (overnight) and changing critical browser-saved passwords as precaution. Both files were deleted. **If the new agent sees signs of malware later, this is the source.**

## Open follow-ups (priority order)

1. **Re-download missing legally-free books** from `BOOKS-TO-DOWNLOAD.md`:
   - ESL II (Hastie) — `hastie.su.domains/ElemStatLearn/` — for `07-machine-learning/`
   - ISLP — `statlearning.com` — for `07-machine-learning/`
   - AOSA Vol 1 + 2 — `aosabook.org` — for `20-software-architecture/`
   - Data Engineering Cookbook — `github.com/andkret/Cookbook` — for `23-data-engineering/`
   - 97 Things Every Programmer Should Know — `github.com/97-things/...` (CC-licensed)
2. **Buy or get via library** the priority paid books — see top of `BOOKS-TO-DOWNLOAD.md` for the ranked shopping list (Kleppmann's *DDIA*, Géron's *Hands-On ML*, Huyen's *Designing ML Systems*, etc.)
3. **Run a full Windows Defender scan** (precaution from the .exe incident)

## My communication style

- Type fast, lots of typos — read past them
- Want decisive, opinionated agents (not "here are 10 options")
- Prefer concrete "do this, then this" over abstract advice
- Push back on the agent multiple times when I want something — agent should hold the line on legal/safety matters but otherwise be flexible

---

**To resume work**: paste this file into a new chat with the prompt: *"Read this handoff and continue from open follow-up #1."*
