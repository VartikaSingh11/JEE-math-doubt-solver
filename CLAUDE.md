# CLAUDE.md — Project Charter & Working Rules

> This project belongs to Vartika Singh's job-hunt portfolio. It follows the operating philosophy in
> `../Resume Review and Roadmap/10_Operating_Philosophy.md` (eval-first, skeleton-first, boring tech,
> shipped > perfect). Claude: read this whole file before doing anything, and enforce it — including on her.
>
> Cross-reference: full workflow + interview defense for this exact project lives in
> `../Resume Review and Roadmap/19_Project_Workflows_Defense_Part1.md` ("PROJECT 1 — RAG Doubt-Solver").
> Read that section before writing any pipeline code.

## 1. PROJECT CHARTER

**Project name:** JEE Math Doubt-Solver (RAG + Evaluation Harness)

**One-sentence pitch:** A question-answering system that lets students ask JEE-level math doubts in plain language and get answers grounded in real study material, with citations — plus a public evaluation harness proving how well it actually works.

**Problem it solves:** Students ask math doubts in messy, informal language; generic LLMs confidently hallucinate solutions, which is dangerous for exam prep. This retrieves from real, trusted material first and refuses when it can't find grounding, instead of guessing.

**The JD test:**
- Maps to: Junior AI/GenAI Engineer roles, LLM Engineer roles, GenAI-flavored Data Scientist roles (file 07's Tier 1/2 target list; edtech companies especially — PhysicsWallah, Allen Digital, upGrad).
- **SKIPPED by decision (2026-07-08):** pulling 3 literal JD links was deemed not the bottleneck — prior market research (Naukri RAG/GenAI job counts, hiring-manager guidance) already confirms this stack matches real demand. Real per-JD keyword-matching happens later, per-application, via the "assembly line" workflow in `21_Using_Claude_In_The_Hunt.md` once this project ships and Vartika is actually applying with it.
- Keywords this makes TRUE on the resume: RAG (Retrieval-Augmented Generation), Vector Databases, Embeddings, LLM Evaluation, Prompt Engineering, LLM-as-Judge.

**The resume bullet being built toward (from `15_Project_Ideas_Bank.md`, fill numbers when real):**
> Built and deployed a RAG question-answering system over [X] pages of JEE study material (chunking → FAISS vector search → cited LLM answers via Groq/Llama), refusing out-of-scope questions instead of hallucinating.
> Designed a 40-case evaluation harness measuring retrieval hit-rate and answer faithfulness separately; improved faithfulness from [X]% to [Y]% through [N] logged chunking and prompt experiments.
> Validated the LLM-as-judge scoring against hand-labeled answers ([agreement metric]) before trusting it.

**Definition of DONE:**
- [ ] Deployed at a public URL: Hugging Face Spaces (Streamlit)
- [ ] Evaluation results table with ≥1 before→after comparison (e.g., naive vs. improved chunking)
- [ ] README: problem → demo GIF → architecture diagram → results table → "what I'd do next"
- [ ] One LinkedIn post published about it (build-log format, `06_LinkedIn_Content_Plan.md`)
- [ ] Vartika can answer all 6 project-defense questions (`09_Interview_Prep.md` §4) AND the Project 1 question bank in `19_Project_Workflows_Defense_Part1.md` out loud, unscripted

**Evaluation plan (designed BEFORE the pipeline — non-negotiable, per Philosophy Part 3.1):**
- **Success metrics:** (1) retrieval hit-rate@k — was the chunk containing the needed fact actually retrieved? (2) faithfulness — is every claim in the generated answer grounded in the retrieved context? (3) relevance — does the answer address the question asked? (4) refusal correctness — does it decline on unanswerable questions instead of guessing?
- **Golden set:** 40 hand-written questions with expected key facts, spanning easy/medium/hard difficulty + 5 deliberately unanswerable ones (outside the corpus) to test refusal. Built BY Vartika using her JEE-teaching expertise — this is a genuine unfair advantage, use it.
- **Baseline to beat:** naive fixed-size chunking (500 tokens, 50 overlap), top-k=3, a plain "answer using this context" prompt with no citation requirement. Every later change must beat this, measured, logged — or it's reverted.

**Data:** DECIDED — Vartika's own Allen Career Institute JEE teaching notes (~20-22 topics available). Allen branding/watermarks stripped from any content used in the public repo/demo (Vartika's explicit call — content itself is standard IIT-JEE syllabus material).
- **Topics ingested so far:** (1) Quadratic Equation, Expression & Inequations — 12 pages. (2) Trigonometric Ratios & Identities — 31 pages. Total 43 pages — already exceeds the 30-80 page target; more topics can be added later without blocking Phase 1.
- **CONFIRMED risk, not hypothetical:** both source PDFs have a corrupted/non-standard text layer (custom font encoding common in older Indian coaching-institute typesetting) — standard PyPDF/pymupdf text extraction produces garbage (e.g. "Swcftctke eqwctkqn" instead of "Quadratic equation"). Visually the PDFs render fine; the underlying text layer does not. **Ingestion MUST use OCR (render page → image → Tesseract), not text-layer extraction.** This is systematic across files, confirmed on 2 separate PDFs — one OCR pipeline fixes ingestion for all future topics too.
- **Known secondary risk:** math notation (fractions, √, Greek letters) and hand-drawn graphs (e.g. the 6 trig function graphs in the Trigonometry file) will OCR poorly or not at all. Expect weaker retrieval on formula-heavy/graph-heavy chunks — state this honestly in the README as a limitation, not a bug to hide.

**Corpus file-naming convention (mandatory, caught 2026-07-08):** the citation `source` field is derived directly from the PDF filename (`pdf_path.stem`), NOT from inside the OCR'd text — so the NOISE_PATTERNS branding-stripper in `ingest.py` never touches it. **Every PDF placed in `corpus/` must be renamed to a clean, topic-based name before ingestion** (e.g. `Quadratic_Equations.pdf`, not the original file's internal name) — original Allen source files often contain faculty nicknames/initials (e.g. "HR Sir, RN Sir") in their filenames, which is a real consent/privacy issue distinct from institutional branding (Vartika caught this — good catch, now a standing rule).

**Stack (boring by default):** Python + PyPDF/pymupdf (ingestion) + sentence-transformers (embeddings, free/local) + FAISS (vector store) + Groq API (Llama, generation — Vartika already has hands-on Groq experience from the internship) + Streamlit (UI) + Hugging Face Spaces (deploy).
**ONE allowed new tool this project:** FAISS (if Chroma was used in a prior project) — otherwise this stack is entirely tools Vartika has already touched. No second new tool without discussing against the resume bullet above.

**Timebox:** 3–4 weeks, ~10–12 hrs/week (per the grind plan's Week 1–2 slot, or adjusted if running on the 90-day pace).
**Milestones — TODO (Vartika, set real dates):**
- Golden set + corpus finalized by: [ ]
- Ugly end-to-end skeleton (ingest → retrieve → generate, no evals yet) running by: [ ]
- Baseline eval numbers recorded by: [ ]
- Shipped (deployed + README + LinkedIn post) by: [ ]

**Learning goals — must UNDERSTAND, not just have working, by the end:**
1. Why retrieval and generation fail differently, and how to diagnose which one broke on a given wrong answer (this is Q-GEN-2 / A-GEN-2 — the single most-asked RAG interview question).
2. The chunking/top-k/context-window trade-off as ONE budget, not three independent knobs.
3. Why an LLM-as-judge needs validation against human labels before you trust it, and what "faithfulness" precisely means as a measured property, not a vibe.

## 2. HOW CLAUDE WORKS ON THIS PROJECT

**Division of labor:**
- **Vartika writes:** the golden-set questions and expected answers (nobody else can — this is her domain expertise), the eval scoring logic, chunking-strategy decisions, prompt design, the experiment log entries and their interpretation.
- **Claude writes:** PDF-parsing boilerplate, FAISS/embedding plumbing, Streamlit UI scaffolding, requirements.txt, README formatting, HF Spaces deployment config.
- **Grey zone:** if Claude writes retrieval-scoring or prompt-template code (core-adjacent), Claude explains it in 3–5 lines and asks Vartika 2–3 questions before moving on. If she can't answer, stop and teach it properly first.

**Teach-while-building protocol:** before any non-trivial implementation (e.g., choosing a chunking strategy, picking an embedding model, designing the judge prompt), Claude gives the why/alternative/failure-mode in 3–5 lines, pitched at "strong math, newer to ML engineering." When Vartika is stuck >45 minutes, she says so and Claude debugs WITH her, asking what's been checked first — never just handing over a fix, except for pure boilerplate.

**Enforcement (Claude must push back, citing this file):**
- No pipeline code until the two TODOs above (JD postings, corpus choice) are filled.
- No Streamlit polish or extra features before the ugly ingest→retrieve→generate skeleton runs end to end.
- No chunking/prompt/model change is kept unless the golden-set eval shows it beats the previous logged run.
- Any proposed second new tool gets challenged against the resume bullet.
- If the timebox is breached, Claude proposes cuts (e.g., ship with 20 golden-set cases instead of 40) — never silent extensions.
- Every experiment (chunking change, prompt change, k change) goes in `log.md`: date, change, hit-rate before/after, faithfulness before/after, one-line verdict.

**Standing quality rules:** requirements.txt from commit 1 · seeded/reproducible retrieval · one-command run in README · small frequent commits · API keys in `.env`, never committed.

## 3. SHIP-WEEK CHECKLIST

1. Freeze features — fix only bugs.
2. Finalize the results table from `log.md`; drop real numbers into the resume bullet above.
3. README: problem → demo GIF → architecture diagram (Excalidraw, one page) → results table → limitations → next step.
4. Deploy to HF Spaces; test the public URL from a phone.
5. Demo GIF via ScreenToGif into the README.
6. Same day: update resume (`02_Resume_Vartika_Singh.html` — this replaces the Spam Screener slot), LinkedIn, Naukri. "RAG" and "vector database" appear verbatim.
7. LinkedIn build-log post (`06_LinkedIn_Content_Plan.md` format).
8. Self-run the full Project 1 question bank in `19_Project_Workflows_Defense_Part1.md` out loud — bring fumbles to Claude for grading against the file's model answers.

---

## CURRENT STATUS — read this first if resuming cold (updated 2026-07-08)

**Phase: 1 (corpus + golden set), transitioning toward Phase 2 (ingestion).**

Done so far:
- Corpus decided: Vartika's own Allen JEE notes, 2 topics uploaded and read (Quadratic Equation — 12pg, Trigonometric Ratios & Identities — 31pg).
- Confirmed both PDFs have a corrupted text layer → OCR-based ingestion is mandatory (not text-layer extraction).
- `src/ingest.py` written (PyMuPDF renders pages → images → Tesseract OCR → naive fixed-size chunks with overlap → saves to `evals/chunks.json`). `requirements.txt` written.
- `evals/golden_set.json` started: 5 of ~40 golden questions written by Claude+Vartika together as a template (recall / conceptual / applied / should-refuse types demonstrated). Vartika continues writing the rest between sessions — nobody else can, this is her domain expertise.
- Vartika has installed Tesseract OCR locally (UB-Mannheim build).

**Immediate next steps (in order):**
1. Vartika places the 2 PDF files into `corpus/` folder (not yet done as of this log entry).
2. Vartika runs `pip install -r requirements.txt` then `python src/ingest.py` in this project folder.
3. Report back what the OCR output looks like (readable text vs. still garbled) — debug together if needed.
4. Once chunks look clean: move to retrieval (FAISS + embeddings) — Phase 3 of the workflow in `19_Project_Workflows_Defense_Part1.md`.
5. In parallel, anytime: Vartika keeps adding golden-set questions toward 40 total.

**Not blocking anything, can happen anytime:** more topic PDFs added to corpus (20+ available); Groq API key into `.env`.

## Session log (Claude appends a one-line entry here at the end of each work session)

- 2026-07-08 — Charter created. Corpus and JD-links decisions resolved (see above). ingest.py + golden_set.json (5/40) written. Waiting on Vartika: PDFs into corpus/, then run ingestion.
