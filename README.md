# JEE Math Doubt-Solver — RAG + Evaluation Harness

A Retrieval-Augmented Generation system that answers JEE-level math doubts, grounded in real
(OCR'd, handwritten-style) study notes, with page citations on every answer — and a measured
evaluation harness instead of vibes-based claims about how well it works.

**Live demo:** [link added once deployed]

## Problem

Students hit doubts while self-studying and don't have a teacher on hand. A plain LLM will answer
confidently from its own pretrained knowledge whether or not it actually matches *this student's*
notes/method — and won't tell you when it doesn't know. This project answers strictly from a small
corpus of real study material, cites the source page for every claim, and explicitly declines
questions the material doesn't cover rather than guessing.

## Architecture

```
PDF notes (scanned, OCR'd)
        │  pytesseract + PyMuPDF
        ▼
Section-aware chunking  ──►  sentence-transformers (all-MiniLM-L6-v2) embeddings
        │                                   │
        ▼                                   ▼
   evals/chunks.json  ──────────────►  FAISS IndexFlatIP (cosine similarity)
                                              │
                        query ──────────────► top-k retrieval (page-diversified,
                                               no duplicate-page slots)
                                              │
                                              ▼
                              Groq (Llama-3.3-70B) generation,
                              grounded strictly in retrieved chunks,
                              cited (source, page), temperature=0
                                              │
                                              ▼
                                    Streamlit UI (this app)
```

Every step above was chosen and swapped based on a measured before/after, logged in `log.md` —
not assumed. See that file for the full experiment history, including two failure modes that were
found live, diagnosed from raw model output (not just the aggregate score), and fixed.

## Results (49-question hand-verified golden set, 48 answerable)

| Metric | Score |
|---|---|
| Retrieval hit-rate (top-3) | 63% |
| Answer faithfulness (keyword-matched against hand-written expected facts) | 73% |
| Refusal accuracy (correctly declines out-of-scope questions) | 100% |

Retrieval is notably stronger on Quadratic Equations (78%) than Trigonometry (48%) — a handful of
broad trig chunks score moderately-high against almost any trig query, crowding out the actually
relevant page. Confirmed via a page-deduplication fix that this isn't simple duplication (that part's
fixed); the correct page genuinely isn't ranking competitively for a meaningful fraction of trig
questions, which needs a stronger embedding model or hybrid keyword+vector search to fix properly.

## What I'd do next

- **Retrieval:** try a stronger embedding model or hybrid (keyword + vector) search — the ~62%
  hit-rate ceiling is the main thing capping faithfulness right now, more than generation quality.
- **Faithfulness scoring:** replace/supplement the keyword-match check with an LLM-as-judge, since
  keyword matching produces both false negatives (a correct answer phrased differently, e.g. "k = ±6"
  not matching a checker looking for "k = 6" and "k = -6" as separate substrings) and can't verify
  whether a citation actually grounds the claim it's attached to.
- **Multi-valued answers:** on problems with two valid final values (e.g. squared conditions), the
  model sometimes reports only one. A first prompt fix for this actually made things worse elsewhere
  (see `log.md`, 2026-07-31 entry) before a safer version landed — the remaining gap is a known,
  accepted limitation rather than something to re-attempt without a clear new angle.
- **Corpus:** currently 2 topics (Quadratic Equations, Trigonometric Ratios & Identities). Expanding
  coverage is straightforward with the existing ingestion pipeline.

## Stack

Python · sentence-transformers (embedding model pulled from the Hugging Face model hub) · FAISS ·
Groq (Llama-3.3-70B) · Streamlit · pytesseract/PyMuPDF (OCR ingestion) · deployed on Streamlit
Community Cloud

## Running locally

```
pip install -r requirements.txt
# create a .env with GROQ_API_KEY=your_key_here
streamlit run app.py
```

Deployed at Streamlit Community Cloud, which reads `GROQ_API_KEY` from its own Secrets manager
(Settings → Secrets in the app dashboard) rather than a committed `.env` file.

To re-run the evaluation harness: `python src/evaluate.py --fresh` (full re-run) or without `--fresh`
to resume/fill in only failed questions from the last run.
