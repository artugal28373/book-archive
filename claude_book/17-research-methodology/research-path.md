# Path of CS Research — Practical Roadmap

How to go from "CS graduate" → "publishing research." Tailored for ML/AI/DL + SWE focus.

## Phase 1 — Foundations (3–6 months)

You can't read papers without math. Lock these down first:
1. **Linear algebra** — Hefferon (skim) → Mathematics for ML chapters 2–4 (deep)
2. **Probability & statistics** — Think Stats → Think Bayes
3. **Calculus / optimization** — Boyd's *Convex Optimization* (chapters 2, 3, 9)
4. **Algorithms** — Erickson, do at least 60% of the exercises

Concurrent: get fluent in **Python + NumPy + PyTorch**. Implement linear regression, logistic regression, a small MLP from scratch (no autograd). This is non-negotiable.

## Phase 2 — Read papers regularly (ongoing)

Start the habit *now*, not later.

**How to read a paper** — Keshav's three-pass method (in `How-to-Read-a-Paper-Keshav.pdf`):
- Pass 1: title, abstract, intro, headings, conclusion, refs (5–10 min)
- Pass 2: figures, captions, scan related work; understand core idea (1 hour)
- Pass 3: re-implement in your head; question every assumption (4+ hours)

**Where to find papers:**
- arXiv.org — cs.LG (ML), cs.CL (NLP), cs.CV (vision), cs.AI, cs.DC (distributed)
- Conferences: NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, CVPR, ICCV
- Curated lists: paperswithcode.com, arxiv-sanity.com
- Newsletters: The Batch (Andrew Ng), Import AI (Jack Clark), AK on X/Twitter

**Pace:** target 2–3 papers/week minimum. Keep notes (Notion, Obsidian, plain markdown).

## Phase 3 — Build a specialty (6–12 months)

Pick ONE area. Going deep beats breadth at this stage.

**For ML theory:** ESL → Murphy (PML) → recent NeurIPS/ICML papers
**For deep learning systems:** D2L → Karpathy's "Zero to Hero" → implement a transformer from scratch → fine-tune a small LLM
**For NLP/LLMs:** SLP3 (Jurafsky) → Stanford CS224n (lectures on YouTube) → HuggingFace docs/courses → recent ACL papers
**For RL:** Sutton & Barto → Spinning Up in Deep RL (OpenAI, free) → recent NeurIPS RL track
**For computer vision:** Szeliski (Computer Vision: Algorithms & Applications, free PDF online) → Stanford CS231n → recent CVPR papers
**For systems / SWE research:** OSTEP → MIT 6.824 (distributed) → CMU 15-445 (DBs) → OSDI/SOSP/SIGMOD papers

## Phase 4 — Reproduce (3–6 months)

You don't understand a paper until you can reproduce it.

1. Pick a paper with code (paperswithcode.com is great for this)
2. Run their code, verify their numbers
3. Re-implement the core method **yourself** without looking at their code
4. Compare your numbers to theirs
5. Write up what you learned, what was surprising, what was glossed over

**This is the single most underrated skill in CS research.** Most students skip it. Don't.

## Phase 5 — Find a problem (ongoing)

Good research problems are:
- **Specific** — "improve LLM reasoning" is not a problem; "reduce hallucination on multi-step math" is
- **Tractable** — you can make progress in weeks, not years
- **Important** — someone (researchers, industry, open source) cares about the answer
- **Underexplored** — search Google Scholar / arXiv first; if 50 papers exist, the bar is high

How to find them:
- **Read survey papers** — they list open problems in conclusions
- **Reproduce something** — you'll find weak spots, that's a paper
- **Talk to senior researchers** — Twitter DMs, conference Q&A, lab visits
- **Look at recent failures** — when models fail in surprising ways, that's a research opportunity

## Phase 6 — Write & submit (3–9 months for first paper)

1. **Write the paper before you have all the results.** Drafting reveals what experiments you actually need.
2. **Use LaTeX from day 1.** Overleaf is fine. Learn BibTeX.
3. **Get reviews early.** Show drafts to peers, advisors, online communities.
4. **Target a venue.** Workshops are easier than main conferences for first papers.
5. **Expect rejection.** Most first submissions are rejected. Resubmit.

## Anti-patterns to avoid

- ❌ Reading 50 books before writing any code
- ❌ Trying to "master" math before touching ML (you'll never feel ready)
- ❌ Implementing only via copy-paste from tutorials
- ❌ Picking "important-sounding" topics without a personal angle
- ❌ Working alone — find a community (lab, Discord, paper reading group)
- ❌ Confusing "AI engineer" work with "AI research" — they're different careers

## Tools you'll need

- **Code:** Python, PyTorch, JAX (optional), CUDA basics, git
- **Compute:** Google Colab → Kaggle → university cluster → cloud (AWS/GCP)
- **Writing:** LaTeX (Overleaf), Notion/Obsidian for notes, Zotero for refs
- **Tracking:** Weights & Biases (wandb.ai) for experiments
- **Collaboration:** GitHub, HuggingFace Hub
- **Reading:** arxiv-sanity, Connected Papers, Semantic Scholar

## Realistic timeline to first paper

For a CS grad working full-time on this: **18–30 months**, depending on background and supervision. Less if you have an advisor and a lab. More if you're doing it alone.

That timeline is normal. Don't compare to social-media research-speedrunners.
