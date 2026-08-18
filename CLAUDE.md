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

**The resume bullet being built toward (SHIPPED — real numbers as of 2026-08-06):**
> Built and deployed a RAG question-answering system over 43 pages of JEE study material (OCR ingestion → section-aware chunking → FAISS vector search → cited LLM answers via Groq/Llama-3.3-70B), refusing out-of-scope questions instead of hallucinating.
> Designed a 49-question hand-verified evaluation harness measuring retrieval hit-rate (63%) and answer faithfulness (73%) separately, plus 100% refusal accuracy on unanswerable questions; iterated through 5 prompt/retrieval versions, each change measured and logged, including catching and reverting a self-introduced regression before shipping.
> Deployed live on Streamlit Community Cloud: [live URL].

**Definition of DONE:**
- [x] Deployed at a public URL: Streamlit Community Cloud (changed from the original Hugging Face Spaces plan — HF now requires a paid PRO plan for any Python-backed Space; Streamlit Community Cloud is free and purpose-built for this)
- [x] Evaluation results table with ≥1 before→after comparison (naive vs. section chunking; v3 vs. v4 vs. v5 prompt cycle, see `log.md`)
- [x] README: problem → architecture diagram → results table → "what I'd do next" (demo GIF still pending)
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

**Stack (boring by default):** Python + PyPDF/pymupdf (ingestion) + sentence-transformers (embeddings, free/local, pulled from the Hugging Face model hub) + FAISS (vector store) + Groq API (Llama, generation — Vartika already has hands-on Groq experience from the internship) + Streamlit (UI) + **Streamlit Community Cloud** (deploy — changed 2026-08-06 from the original Hugging Face Spaces plan; HF Spaces now requires paid PRO for a Python-backed app, discovered live during deployment).
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

## CURRENT STATUS — read this first if resuming cold (updated 2026-08-06)

**Phase: SHIPPED and live. Remaining work is promotion (demo GIF, LinkedIn post) and interview-defense prep, not engineering.**

Done:
- Full pipeline built: OCR ingestion (Tesseract + PyMuPDF) → section-aware chunking (beat naive chunking, measured: 50%→64% hit-rate on the retrieval-only comparison) → FAISS retrieval (page-diversified, no duplicate-page slots) → Groq (Llama-3.3-70B) generation, prompt at v5 → Streamlit UI.
- 49-question hand-verified golden set (grew from the original 40-question target). Final clean eval (0 failures): retrieval hit-rate 63%, faithfulness 73%, refusal accuracy 100%. Full experiment history — including a v4 regression that was caught by reading raw output and reverted before shipping, not just trusting the aggregate score — is in `log.md`.
- **Deployed live** on Streamlit Community Cloud (not HF Spaces — that plan changed mid-deployment when it turned out HF now requires paid PRO for any Python-backed Space; discovered live, pivoted same session). Public GitHub repo pushed and connected. Confirmed working from a fresh/incognito browser session, not just Vartika's own logged-in one.
- README written: problem, architecture diagram, results table, honest limitations, "what I'd do next." Sidebar in `app.py` shows live, current metrics (not stale numbers from an earlier eval run) and an honest limitations list, including the free-tier "app sleeps after inactivity" behavior.

**Not yet done:**
1. Demo GIF (ScreenToGif or similar) into the README.
2. LinkedIn build-log post (`06_LinkedIn_Content_Plan.md` format) — this is the actual trigger for "post it on LinkedIn," the original ask that restarted this project.
3. Resume (`02_Resume_Vartika_Singh.html`) not yet updated with the live link + final numbers — was intentionally held until deployment + a trustworthy eval were both real, per the earlier honesty-first call.
4. Self-run the full project-defense question bank (`19_Project_Workflows_Defense_Part1.md`) out loud before relying on this in an interview.
5. Known, accepted, NOT blocking shipping: retrieval hit-rate plateaus ~62% (needs a stronger embedding model or hybrid search to move, not attempted); one class of question (two valid final values, e.g. ± roots) sometimes only reports one value.

## Session log (Claude appends a one-line entry here at the end of each work session)

- 2026-07-08 — Charter created. Corpus and JD-links decisions resolved. ingest.py + golden_set.json (5/40) written. Waiting on Vartika: PDFs into corpus/, then run ingestion.
- 2026-07-08 to 2026-07-22 — Full pipeline built (ingestion, retrieval, generation, eval harness), golden set grown to 45, section-chunking proven over naive, live bug found and fixed through 3 prompt iterations (v1→v3), Streamlit UI built and Playwright-tested.
- 2026-07-31 to 2026-08-02 — Full re-eval cycle: found and fixed a retrieval duplicate-page issue, iterated prompt v4→v5 after v4 introduced then had a caught-and-fixed self-regression, golden set grew to 49. Final clean numbers: 63% hit-rate / 73% faithfulness / 100% refusal.
- 2026-08-04 to 2026-08-06 — Deployed. Pivoted from planned HF Spaces to Streamlit Community Cloud mid-deployment (HF free tier no longer supports Python Spaces). Git installed, GitHub repo created and pushed, app connected and confirmed publicly reachable. README, CLAUDE.md, and app.py sidebar updated with real current numbers and the live URL.
