# KEA — Work Sample

**We're not trying to extract free labor** — we want a clear signal on how you think, structure, and communicate. If you go a bit over the time budget, that's fine. If you find yourself heading toward double, stop and write up what you have. Knowing when to ship is part of what we're evaluating.

## What We Care About (Read This First)

The same principles apply to both tasks below. Internalize them before you start — they shape how we'll read your submission.

**Methodology over results.** A high score can be luck — someone happens to pick a strong embedding model, someone happens to stumble on an obvious bug. Solid methodology is not luck. We weight a clearly reasoned approach much higher than a strong number with no trace of how you got there. We'd rather read *"I tried A, it failed because X, so I moved to B, validated it like this, here's where it still struggles"* than *"I used sentence-transformers and got 0.84."* Dead ends are evidence of thinking — show them.

**Structure is non-negotiable.** Your report has to be ruthlessly structured, stringent, and immediately understandable. Remember: you're not sitting next to us to explain anything. Everything has to be self-explanatory on the page. Clear hierarchy, sensible spacing, readable tables, logical flow. We don't care about fancy design — but sloppy layout signals sloppy thinking, and we'll bounce off a messy document fast.

**Highly structured working style is what we're hiring for.** More than anything, we want to see that you approach problems methodically and present your work in a way that respects the reader's time. That signal matters more to us than any individual subtask score.

---

## Task 1 — Black-Box Audit of KEA (~1.5 hours)

You'll receive login credentials for https://kea.iotadp.com/ in the email. KEA is a Q&A system for market researchers: users ask natural-language questions, and the system routes them to SQL (structured market data), internal documents, web, email archives, and conversational memory. Under the hood: LLM-based query understanding, NL-to-SQL, RAG retrieval, and a synthesis layer.

**Your job:** test it systematically — different question types, sources, edge cases, workflows.

### Deliverable — Audit Report (PDF or HTML, max 3 pages)

1. **Methodology** — How did you approach testing? What categories of inputs did you try and why? What did you deliberately *not* test?
2. **Findings** — For each issue: steps to reproduce, expected vs. actual, severity (critical/major/minor/cosmetic), root-cause hypothesis (retrieval? SQL gen? synthesis? routing? UI?).
3. **Top 5 Fixes** — Ordered by impact. For each: what, why it matters most, rough how.

Page limit is tight on purpose — prioritize ruthlessly.

---

## Task 2 — Build a Retrieval System (~2.5 hours)

Build a small document retrieval system. Given a query, return the most relevant passages across a mixed file collection.

### The Files

`test_files/` contains:

| File | Type |
|------|------|
| `research_proposal.pdf` | Research proposal |
| `phase2_findings.pptx` | Presentation slides |
| `Stocked_questionnaire_s.docx` | Survey questionnaire |
| 5 `.eml` files | Project correspondence |
| `glossary_partial.json` | Partial variable glossary (180 of 451 variables) |

### What to Build

Implement `retrieve()` in `retrieve.py`:

```python
def retrieve(query: str) -> list[dict]:
    """
    Return top-5 most relevant passages.
    Each dict must have:
      - "text": str       — the passage content
      - "source": str     — source filename or "glossary"
      - "score": float    — relevance score (higher = better)
    """
```

Handle two query types:

- **Broad:** *"What was the main finding of the brand study?"*
- **Narrow:** *"What does the variable `frm_brand_awareness` measure?"*

A good system handles both. Scan `test_files/` at runtime — don't hardcode filenames. The evaluation uses queries and documents beyond your starter package.

### Live Feedback Portal (Optional)

A scoring portal is available at **https://kea.iotadp.com/submission**. Treat it as a sanity check, not ground truth — it confirms your code runs end-to-end on our infra. **Do not optimize against it.** Build your own evaluation. Upload `retrieve.py` (required) and `requirements.txt` (optional). Max 10 submissions, results in 1-2 minutes.

### Local Testing

```bash
pip install -r requirements.txt
python test_local.py
```

Runs 10 sample queries with a basic keyword scorer. Don't over-optimize for it.

### Report (PDF or HTML, max 2 pages)

1. **Approach** — How you framed the problem. Options you considered *and discarded* — including ones that failed.
2. **Methodology** — How you measured quality. What queries did you build yourself? How did you decide one approach was actually better than another?
3. **Results** — Structured comparison. Tables, numbers, examples — not vibes.
4. **Recommendation** — What works best, why, and where it falls short. Every system has weaknesses; if you can't name yours, you haven't looked hard enough.

---

## Rules (Both Tasks)

- Any Python libraries allowed (add to `requirements.txt`)
- **No external LLM APIs in `retrieve()`** — must run locally
- Embedding models fine (HuggingFace, sentence-transformers, etc.)
- LLM coding assistants fine
- Eval server: **Python 3.12 on Linux**

---

## Final Submission

Reply to the email you received the tasks from with:

1. **Task 1 report** — `yourname_task1.pdf` or `.html`
2. **Task 2 report** — `yourname_task2.pdf` or `.html`
3. **Task 2 code** — `yourname_task2.zip` containing your full Git repo (include `.git/`)

### Zip structure

```
yourname_task2/
├── retrieve.py
├── requirements.txt
├── test_local.py
├── test_files/
├── README.md
└── .git/
```

### Reproducibility

We must be able to run your code with exactly:

```bash
pip install -r requirements.txt
python test_local.py
```

No extra steps, no hardcoded paths, no credentials. If we can't get it running within 15 minutes, we'll only evaluate the report and do a static code review.

---

Good luck — have fun with it.
