# Experiment Log

Format: date | change tested | result | verdict. Every chunking/prompt/k/threshold change goes here, per CLAUDE.md.

---

## 2026-07-08 — Similarity threshold on retrieval (preliminary, n=3 manual queries — NOT yet eval-harness scale)

**Change tested:** added optional `min_score` filter to `retrieve()` (default OFF). Tried `min_score=0.40` against baseline (no threshold, always top-3).

**Result (3 manual test queries, not yet the full golden set):**
| Query | Baseline | Thresholded @0.40 | Notes |
|---|---|---|---|
| Q1 (on-topic, correct retrieval) | Correct answer | Correct answer (identical) | All 3 chunks scored >0.4 — threshold inert here |
| Q2 (on-topic, WRONG chunk retrieved) | Correctly refuses (given bad context) | Same — no change | Wrong chunk scored 0.639 — *higher* than Q1's correct chunk (0.588). Threshold cannot catch a confidently-wrong retrieval. |
| Q3 (off-topic, calculus) | Correctly refuses, but still spends 1 API call on 3 low-scoring (0.30-0.35) chunks | Zero chunks retrieved, refuses instantly, **no API call spent** | Clean win — real cost saving on genuinely out-of-domain questions |

**Verdict (preliminary — confirm at real eval-harness scale before treating as final):** a similarity threshold appears to help distinguish "nothing relevant exists" (Q3-type) cheaply, but does **not** fix "wrong-chunk-retrieved-with-high-confidence" (Q2-type) — those are different failure modes requiring different fixes (better chunking/reranking, not a score cutoff). Keep `min_score` as an opt-in parameter; do not make it the default yet. Revisit once the 40-question golden set can test this across many more examples than 3.

---

## 2026-07-09 — First baseline eval run (n=5, k=3, no threshold) — AND a golden-set design bug caught

**Raw numbers reported:** retrieval hit-rate 75%, avg faithfulness 83%, refusal accuracy 100%.

**These numbers were partially wrong — not because the harness logic is broken, but because two `expected_facts` entries were too generic to be meaningful keyword checks.** Read the raw answer text behind each score before trusting it:

| Q | Reported | Actual (from raw answer text) | Root cause |
|---|---|---|---|
| Q1 | HIT, 100% faithful | **Correct**, trust it | — |
| Q2 | HIT, 33% faithful | Model **fully refused** ("This isn't covered...") despite the correct page (p2) being retrieved. True faithfulness = 0%. | `expected_facts` included bare `"n"` — matched the letter "n" inside the word "isn't." A **generation failure with correct retrieval** — the opposite failure mode from Q3. |
| Q3 | MISS, 100% faithful | Retrieval genuinely missed (confirmed again) — correctly flagged. But the model's answer **hedged/refused** ("does not provide a clear list of three basic identities"), not a real answer. True faithfulness ≈ 0%, and `refused` should have been True. | `expected_facts` were `["sin","cos","1","sec","cosec"]` — generic enough to match almost any trigonometry answer regardless of correctness. |
| Q4 | HIT, 100% faithful | **Correct**, trust it (top-retrieved page was p9, an unexpected page, but p2 was still in top-3 and the answer is fully accurate) | — |
| Q5 | correct refusal | **Correct**, trust it | — |

**Honest corrected picture:** of 4 answerable questions, only 2 (Q1, Q4) are unambiguously right. The 83% faithfulness headline overstated quality — a false positive is more dangerous here than a false negative, since it hides real problems instead of just raising false alarms.

**Fix applied:** tightened `expected_facts` for Q2 (`"conjugate"`, `"rational coefficient"`) and Q3 (`"cos²"`, `"sec²"`, `"cosec²"`) to more distinctive substrings. Known remaining limitation: these still assume the model outputs unicode `²` rather than `^2` — notation variance is an unsolved gap of pure substring matching, a real argument for the LLM-as-judge upgrade later (Project 7), not something silently patched now.

**Standing rule going forward:** never trust an aggregate eval percentage without spot-checking the raw answer text behind at least the surprising scores. Applies to all future golden-set questions Vartika writes — pick `expected_facts` that are distinctive enough that an irrelevant/wrong answer is unlikely to contain them by accident (avoid single letters, single digits, and common words).

**Re-run after fixing Q2/Q3 expected_facts:** hit-rate 75%, faithfulness 75%, refusal 100%.
- Q2 now correctly shows 0% (matches reality — full refusal, no fabricated partial credit).
- Q3 still shows 100%, but this time it's a GENUINE match, not a repeat bug: the model actually stated all three correct Pythagorean identities (sin²θ+cos²θ=1, tan²θ+1=sec²θ, 1+cot²θ=cosec²θ) verbatim-correct, despite retrieval still missing the exact source page (p3) and pulling a related-but-different page (p4, a ratio-conversion table) instead.
- **New, deeper finding, not fixable by better keyword-matching:** the model's answer says these identities are "derived from the given relationships," but sin²θ+cos²θ=1 is also universal pretrained knowledge -- there is no way to tell from the output alone whether this was genuinely grounded in the retrieved page 4 content or leaked from pretraining despite the system prompt's "do not use outside knowledge" instruction. Keyword matching can only check "is X present," never "was X actually grounded in context." This is the concrete, first-hand argument for an eventual LLM-as-judge or explicit context-entailment check -- logged here as a known, named limitation, not something to patch today.

**BASELINE RECORDED (n=5, k=3, no threshold, corrected golden set): hit-rate 75%, faithfulness 75%, refusal accuracy 100%.** Treat as a qualitative first pass, not a statistically meaningful number — revisit once the golden set grows toward 40 questions.

---

## 2026-07-10 — Prompt fix: loosened "no outside knowledge" rule (n=15)

**Change:** SYSTEM_PROMPT v2 — separated "method must come from context" from "completing the calculation may use standard math/values," after the eval harness showed a recurring pattern of refusing/stopping mid-calculation (Q2/Q9/Q12/Q13).

**Before → After:**
| Metric | Before | After |
|---|---|---|
| Retrieval hit-rate | 50% | 50% (unchanged, expected — prompt doesn't touch retrieval) |
| Avg faithfulness | 52% | **79%** |
| Refusal accuracy | 100% | 100% |

**Per-question:** Q9 (0%→100%, refused True→False) and Q12 (0%→100%, refused True→False) — **fully fixed.** Q13 (0%→50%) — improved, not complete. **Q2 unchanged (still refuses)** — different root cause: it's a "why" conceptual/proof question where the source states the rule without proving it, not a pure calculation the model was blocked from finishing. The prompt fix targeted calculation-completion; Q2's gap is something else, still open.

**Verdict: real, measured win. Keep this prompt.** Retrieval (50% hit-rate) is now the clearly larger remaining bottleneck vs. generation.

---

## 2026-07-11 — Chunking strategy: section-header-based vs. naive fixed-size

**Change:** added `chunk_by_section()` to `ingest.py` — splits each page at the notes' own numbered headers ("3. RELATION BETWEEN ROOTS...") instead of a fixed 2000-char window, so each concept becomes one coherent chunk. 52 naive chunks vs. 60 section-based chunks from the same 2 PDFs.

**Retrieval-only comparison (isolated, no generation, via `compare_chunking.py`):**
| Strategy | Hit-rate (top-3) |
|---|---|
| Naive (baseline) | 50% |
| Section-header | **64%** |

**Fixed: Q3 and Q8 — zero regressions.** Q3 (the three basic trig identities) was the very first retrieval failure found at the start of this project — section-based chunking fixed it, because the identity statement is short and was previously getting buried inside a much larger fixed-size chunk full of unrelated surrounding text.

**Full pipeline re-run (retrieval + generation) confirms it holds end-to-end:** hit-rate 64%, faithfulness 76%, refusal 100%. Q3's answer is now genuinely correct content (states 2 of the 3 identities correctly, honestly notes the third "isn't explicitly stated as a third" — a faithful reflection of what's actually in that chunk, not a hallucination).

**Decision: promoted section-based chunking to the default.** `chunks.json` now holds the section-based chunks; naive is archived as `chunks_naive_baseline.json` for future reference. `ingest.py`'s default `--strategy` changed from `naive` to `section` so future re-ingestion (adding more topics) uses the winning strategy automatically.

**Still open (unchanged by this fix):** Q9, Q11, Q12, Q14, Q15 remain MISS on retrieval — but most still get correct final answers because the model can complete the computation from general math skill once the *type* of method is grounded (per the 2026-07-10 prompt fix). Retrieval hit-rate has more room to improve, but generation is now compensating well for partial misses on computational questions specifically — this compensation does NOT apply to pure recall questions, where a miss is still a miss.

**Bug found + fixed (unrelated to chunking):** `evaluate.py`'s console print crashed on Unicode (π, θ, °) due to Windows' default cp1252 console encoding. Data was never affected (`results.json`/`report.md` write UTF-8 correctly) — only the terminal summary crashed. Fixed via `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`.

---

## 2026-07-11 — Deep-dive on remaining retrieval misses (Q9, Q11, Q12, Q14, Q15)

Read the actual full chunk content (not just page-number guesses) for every page involved. Three distinct outcomes, not one:

1. **Q9, Q11 — genuine, confirmed retrieval misses.** Verified the expected pages (3, and 6/7) really do contain the right material; retrieval simply isn't surfacing them. Real, unresolved gap for a future chunking/embedding iteration.
2. **Q14 — not a retrieval miss, a golden-set labeling error.** Page 15 (my original guess) has the direct formula, but page 4 *also* legitimately supports deriving it (sec²A=1+tan²A path) — which is exactly what the model used. Fixed: `expected_pages` widened to `[4, 15]`.
3. **Q15 — a more serious finding: likely citation hallucination, not a retrieval miss.** The model consistently cites "Page 17" for sec²θ−tan²θ=1 across multiple runs. Read page 17's full content directly — it does not contain this identity anywhere (it has unrelated cosec/sec worked examples and a half-angle note). The final numeric answer (1/5) is correct, but the citation appears fabricated -- likely the model stating well-known pretrained knowledge and attaching a plausible-looking page number rather than a genuinely grounded one. **Not fixed by adding page 17 to expected_pages** -- that would reward a false citation. Left as an open, named limitation: the current eval only checks whether an answer is correct and whether a plausible-sourced page was *retrieved* -- it never verifies the *cited* page actually entails the claim. Closing this gap properly needs a groundedness/citation-verification check, not a chunking fix -- a natural extension of the eval harness, not attempted yet.
4. **Q12 — inconclusive.** Did not find clear evidence in the retrieved pages either way; left unresolved rather than guessed at.

---

## 2026-07-11 — Golden set completed to 45 questions; DEFINITIVE baseline (n=44 answerable)

Added all 30 remaining questions from the practice-questions PDF (verified every answer by hand before entering it). Golden set: 45 total (44 answerable, 1 refusal-test).

**Real infrastructure problems hit and fixed along the way (not retrieval/prompt issues):**
- Groq free tier has both a per-minute AND a per-day (100,000 token) cap. First full 45-question run died at Q12 when the daily cap hit -- every question after failed. Added retry-with-backoff to `generate.py` (handles the per-minute case) and made `evaluate.py`'s loop resilient (one failed question no longer kills the whole run -- recorded and skipped instead of crashing).
- **Bug in my own fix:** the aggregate stats were counting failed questions as automatic MISSES (deflating hit-rate to a meaningless 18%). Fixed: failed questions are now fully excluded from every stat's denominator via an explicit `failed` flag.
- **Second bug in my own fix:** added a "resume" mode to reuse previous successful answers instead of re-spending quota -- but the *first* broken run's `results.json` had no `failed` key at all (written before that field existed), so resume silently treated all 34 real failures as "successful" and reused their `[ERROR: ...]` text. Fixed by also detecting the legacy `[ERROR:` prefix. Re-ran after the fix: all 45 processed for real, 0 failures.

**DEFINITIVE BASELINE (n=45, k=3, no threshold, section-header chunking):**
| Metric | Result |
|---|---|
| Retrieval hit-rate (top-3) | **64%** |
| Avg faithfulness (keyword) | **82%** |
| Refusal accuracy | 100% |

Matches the earlier 64% hit-rate found on the 15-question set almost exactly -- strong confirmation the chunking win was real, not small-sample noise. This is the number to use in the resume bullet.

**New finding: Quadratic Equations questions hit far more reliably than Trigonometry ones (~75% vs ~50%).** Quadratic_Equations.pdf is shorter (12 pages) and more cleanly/consistently numbered; Trigonometric_Ratios_and_Identities.pdf (31 pages) has messier sub-numbering (e.g. "D(iii)") that the simple section-header regex handles less reliably. Concrete, specific lead for a future chunking-regex improvement, not investigated further yet.

---

## 2026-07-19 — Streamlit UI built and verified end-to-end (real bug found via actual testing)

Built `app.py`: title, sidebar (project description, measured metrics, honest limitations), example-question buttons, question input, answer display with an expandable "sources retrieved" section.

**A genuine bug was caught only because the UI was actually tested (headless browser + Playwright), not just read over:** the example-button "click to prefill the question" feature used `st.text_area(..., value=clicked_example or "")`. This worked on the FIRST rerun (button click sets the value) but silently reset the textbox to empty on the VERY NEXT rerun (clicking "Ask" itself) -- because `clicked_example` is recomputed at the top of every script run, and no button fires on the Ask-click pass, so `value=""` won. Fixed using the correct Streamlit pattern: `st.session_state` bound to the widget's `key`, updated inside the button's if-block, no `value=` parameter competing with it.

**Verification also caught two flaws in my own TEST script, not the app** -- worth recording since they're instructive: (1) `page.click("text=Answer")`-style assertions were false-positives, matching "Answer**s** are grounded..." already present in the page caption before anything was even clicked; (2) `page.click("text=Ask")` likely matched the caption's "**Ask** a JEE-level math doubt..." text instead of the real button. Fixed by using Playwright's role-based selector (`get_by_role("button", name="Ask", exact=True)`) and by checking actual answer CONTENT substrings rather than trusting a text-selector match existed.

**End-to-end confirmed working:** example click -> populates question -> Ask -> spinner -> real grounded answer with correct page citation ("Quadratic_Equations, Page 2") -> expandable sources panel. Takes up to ~30s for a response under today's heavy rate-limit load; normal usage should be faster.

---

## 2026-07-22 — Live failure found by Vartika using the deployed app ("evaluate cos 130 degree"), and what actually fixing it (vs. patching it) required

**The failure:** asked live, not part of the golden set. The model correctly derived cos(130)=-cos(50) mid-answer, then abandoned it -- chased irrelevant identities (half-angle into cos25, unrelated pentagon angles 18/36), and ended with "this isn't covered," directly contradicting its own earlier derivation. ~2000+ chars of rambling for what should be a 2-sentence answer.

**Vartika's pushback (correct and important):** adding this one question to the golden set would only give a permanent measurement, not a fix -- any new arbitrary question with the same shape (an angle that reduces via identity but has no "nice" exact value, e.g. most angles that aren't multiples of 15 or the 18/36/54/72 family) would keep failing the same way. Asked for a solution that generalizes.

**Fix v1 (prompt only):** rewrote SYSTEM_PROMPT (v3) adding explicit decisiveness ("pick one identity, commit, stop -- an imperfect reduction IS a complete answer") and answer-first structure ("state the answer in sentence one").

**Generalization test (the right way to validate this, not just re-testing the original question):** ran 4 different never-before-seen questions sharing the same failure-prone shape -- cos130 (original), cos100, sin200, tan160.

Result: 2/4 (cos130, tan160) fully fixed -- short, decisive, correct. 1/4 (cos100) improved but still underselling its own correct answer. **1/4 (sin200) revealed a DIFFERENT failure mode the v3 prompt didn't anticipate: instead of trying multiple different identities, it looped on the SAME correct conclusion ~8 times across 4577 characters.** Proved the pushback right -- a single prompt tweak does not reliably generalize.

**Fix v2 (prompt + code-level guardrail):** added an explicit anti-repetition rule ("never restate a conclusion, even in different words") AND a hard `max_tokens=400` cap on the Groq call. Rationale: prompt instructions are probabilistic and can fail (just proven); a token cap is deterministic and safe to combine with the answer-first rule, since the real answer already appears before any cap would cut in.

**Re-test result:** sin200 dropped from 4577 -> 452 chars, decisive, correct, no repetition -- clear win. cos100 still shows a narrower version of the original problem: derives -cos(80) correctly, then gets distracted by the sum-to-product identity (page 13) which structurally needs TWO angles and cannot apply to a single-angle question. Suspected root cause: retrieval keeps surfacing that page because it lexically matches "cos" + an angle, not because it's relevant -- i.e. this specific residual failure is likely a retrieval problem wearing a generation costume, not fixable by prompting alone.

**Added all 4 questions to the golden set (ids 46-49) as regression tests for this fix -- correctly framed as measurement, not a substitute for the fix itself,** per Vartika's original, correct objection. cos100 (id 47) is left open/unresolved with its root cause noted, not patched over.

**Honest general lesson, worth remembering for interviews:** no single prompt change perfectly generalizes to all future inputs -- LLM behavior is probabilistic, and fixing one observed failure mode can leave a sibling failure mode (repetition vs. multi-path rambling) undiscovered until tested separately. The fix that actually holds up combines a soft instruction (prompt) with a hard constraint (token cap) precisely because the soft one alone was empirically shown to fail on a case the hard one then caught.

---

## 2026-07-31 to 2026-08-02 — Prompt v4 -> v5, retrieval de-duplication, and a self-inflicted regression caught before shipping

**Starting point:** a fresh (non-resumed) full 49-question eval on prompt v3 came back at 62% hit-rate / 72% faithfulness -- lower than the earlier n=45 baseline (64%/82%). Read every changed answer instead of trusting the aggregate. Found the drop was NOT one thing: (a) false negatives in keyword faithfulness (e.g. Q31 answered "k = ±6," correct, but the checker looks for the literal substrings "k = 6" / "k = -6"), (b) a genuine new bug -- "be decisive" was causing the model to silently drop one of two valid final values on multi-valued problems (Q38: p²=25 -> stated only p=-5), (c) confirmed real max_tokens=400 truncation (Q12, tan 255, cut off mid-token after a retrieval miss forced a from-scratch derivation), (d) genuine LLM arithmetic mistakes unrelated to any prompt wording (Q32, Q33, Q20).

**Retrieval diagnosis (before touching any code):** read every MISS against its expected page. Found pages 13/17/18 of the trig doc acting as "attractor" chunks -- broad enough to score moderately-high against almost any trig query, and confirmed occupying 2 of 3 top-k slots as near-duplicates on 5 questions (e.g. Q11 retrieved `[12, 13, 13]` instead of a third, different page).

**Fix — retrieval (`src/retrieval.py`):** search a wider candidate pool, greedily keep only the best-scoring chunk per distinct (source, page) until k slots are filled. Confirmed via before/after diff that all 5 duplicate-page cases were fixed exactly as designed. **Honest result: it did NOT move the aggregate hit-rate (61.7% vs 62%)** -- the freed slot was filled by yet another wrong-but-different page in every case. Duplicate-page waste was real but was not the dominant cause of misses; the deeper issue (correct page not ranking competitively at all against the embedding model) needs a bigger intervention (better embedding model / smaller chunks / hybrid search) not attempted here.

**Fix — prompt v4 (`src/generate.py`):** added a standalone rule requiring multi-valued results to all be stated (targeting the Q38 bug) + hardened the decimal-approximation instruction from optional-sounding to mandatory + raised `max_tokens` 400->600 (targeting the Q12 truncation).

**v4 regression, caught by reading raw answers, not by the aggregate score:** the new multi-valued rule backfired on Q31 -- a previously clean, correct "k = ±6" answer turned into a ~600-token self-contradictory loop, inventing a nonsense "sum of roots must be zero" tangent and hard-truncating mid-sentence. Worse than the original cos-130 bug that started this whole investigation. It also didn't even fix its own target: Q38 still reported only p=-5.

**Fix v5:** reverted the standalone multi-valued rule; folded a much shorter version back into the main decisiveness rule, explicitly forbidding re-deriving/re-checking a multi-valued result once found (the exact behavior that broke Q31), rather than inviting more deliberation.

**Final, clean, fully fresh 49-question eval on v5 (n=48 answerable, 0 failed):**
| Metric | v3 (pre-regression baseline) | v5 (final) |
|---|---|---|
| Retrieval hit-rate @3 | 62% | 62.5% |
| Faithfulness (keyword) | 72% | 72.9% |
| Refusal accuracy | 100% | 100% |

Aggregate is flat -- but the composition matters more than the headline here:
- Q31 (the v4-caused regression): fixed, clean, correct, 100% faithful.
- Q46 (cos130), Q47 (cos100), Q48 (sin200): all now short, decisive, and land on a **correct** decimal (-0.64, -0.17, -0.34) -- the original complaint this whole cycle was about is confirmed fixed on a full eval run, not just the 4 hand-picked test cases.
- Q49 (tan160): correct method, minor arithmetic imprecision (-0.387 vs. true ~-0.36) -- benign LLM arithmetic noise, not a structural bug.
- Q38: still incomplete (only states p=-5, not p=+5) -- known, accepted, unresolved. Lower severity than Q31 was and not worth further prompt engineering right now given the risk just demonstrated (chasing this exact class of bug is what caused Q31).

**Process lesson:** hit two separate Groq free-tier daily-quota (100k TPD) exhaustions getting here, each from repeated full-49-question re-runs plus retries. It's a rolling window, not a fixed daily reset -- "try again in Xm" estimates are not reliable countdowns. A single full 49-question run on v5 (more verbose due to max_tokens=600) uses very close to the entire daily allowance by itself, which is a real constraint on how many full re-evals are practical per day on the free tier.

**Verdict:** v5 is the version to ship. Not because the aggregate improved (it didn't, meaningfully) but because the two things that actually mattered -- the original rambling/contradiction bug, and the regression this project's own fix cycle introduced -- are both confirmed fixed on the full golden set, and the remaining gaps (retrieval ceiling ~62%, Q38's dropped root, occasional arithmetic imprecision) are honestly small, understood, and documented rather than hidden.
