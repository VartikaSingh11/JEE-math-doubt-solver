"""
Generation: take a question + retrieved chunks -> ask Groq (Llama) for a
grounded, cited answer -- or a refusal if the context doesn't support one.

Boilerplate (Claude's job): the Groq API call, message formatting, .env loading.
PROMPT DESIGN (Vartika's job, per CLAUDE.md division of labor): the actual
instructions below are a FIRST DRAFT / starting point -- review and edit the
wording, refusal condition, and citation format before we trust real eval
numbers to it. This is not final until you've looked at it.

Why the prompt is structured this way (3 things worth understanding, not just
having working):
1. Context is wrapped in clear delimiters (---) separate from the question,
   so the model can't confuse "instructions" with "content to answer from" --
   the same principle behind prompt-injection defenses from your internship.
2. It's told to cite (source, page) for every claim -- this is what makes
   "faithfulness" checkable later: an eval can verify the cited chunk actually
   contains the claim, not just trust the model's word.
3. It's given an explicit refusal instruction rather than a hard similarity-
   score cutoff -- simpler for this first ugly pass. Whether a score threshold
   ALSO helps is a real experiment to run later and log, not assume.
"""

import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq, RateLimitError

from retrieval import retrieve

load_dotenv(Path(__file__).parent.parent / ".env", override=True)

MODEL = "llama-3.3-70b-versatile"

# --- PROMPT v5 (2026-07-31, Vartika's decision): v4 added a standalone "state
# all multi-valued results" rule (old rule 3) after Q38 (p^2=25) dropped one of
# two valid roots. Re-running the full 49-question eval and reading the raw
# text showed that rule BACKFIRED: on Q31 (k^2=36 -> k=+-6, previously a clean
# correct one-liner) the model instead spiralled into second-guessing itself
# against a nonsense self-invented "sum of roots must be zero" tangent, looped
# contradicting itself for ~600 tokens, and got hard-truncated mid-sentence --
# arguably the worst single answer this project has produced, and WORSE than
# the original cos-130 rambling bug that started this whole investigation. It
# also didn't even fix its own target case: Q38 still reported only p=-5.
# v5 = v4 with that standalone rule removed and folded back into rule 2 as one
# short, deliberately non-recursive clause ("state both, do not re-derive or
# second-guess") -- the goal is the same, but phrased to forbid exactly the
# re-checking loop that broke Q31, instead of inviting more deliberation.
# The decimal-approximation hardening (also new in v4) stays: it correctly
# fixed Q46/Q47, though Q48 (sin 200) shows it can also produce a confidently
# WRONG decimal on a case the model can't actually compute -- a known,
# accepted residual risk of a 70B model's arithmetic, not something to chase
# with more prompt engineering (per Vartika's own earlier call on arithmetic
# slop being a documented limitation, not a bug to eliminate).
SYSTEM_PROMPT = """You are a JEE Mathematics doubt-solving assistant. Follow these rules:

1. The METHOD or FORMULA you use must come from the CONTEXT below -- do not invent an approach
   the context doesn't support. But once the method is grounded, COMPLETE the problem yourself:
   apply arithmetic, algebra, and well-known standard values (e.g. sin30deg=1/2, standard angle
   conversions) as needed to reach a final answer. Do not stop partway or refuse just because a
   specific number wasn't restated verbatim in the retrieved text -- if the method is grounded,
   finish the problem.
2. BE DECISIVE ABOUT METHOD, PLAIN ABOUT RESULTS. Pick the best valid identity/reduction, commit
   to it, and STOP. Do not try several different identities in your visible answer and narrate
   which ones fail -- reason through it once, then present exactly one final path. If the final
   step is a squared or otherwise multi-valued condition (e.g. k^2=36), just state both resulting
   values plainly in one sentence (e.g. "k = 6 or k = -6") and move on -- do NOT re-derive,
   re-check, or second-guess a multi-valued result once you have it; picking one method does not
   mean picking only one of its valid outputs. If a value has no simple exact closed form (e.g.
   cos(50 degrees) is not one of the standard angles), reducing it as far as a known identity
   allows (e.g. cos(130 degrees) = -cos(50 degrees)) is the correct reduction -- but you are NOT
   DONE yet: you MUST also state its decimal approximation to at least 2 decimal places (e.g.
   "= -0.64"). A symbolic reduction with no decimal value is an INCOMPLETE answer. Never end a
   numeric "evaluate ..." question on a symbolic form alone. Do not keep searching for a "nicer"
   closed form, and do not apologize for one not existing.
3. Give your final answer in the FIRST sentence. Supporting steps may follow, but the reader must
   never have to reach the end of the response to learn what the answer is.
4. Cite the source and page for the method/formula you used, like: (Source: {source}, p{page}).
5. Refuse ONLY if there is no relevant method for this question at all AND you cannot derive any
   partial reduction yourself. If you already derived a valid reduction earlier in your reasoning,
   that reduction is your answer -- never contradict it by then saying the question "isn't
   covered." In genuine no-method cases, say clearly: "This isn't covered in the provided
   material."
6. Be concise. Exam-prep, not a conversation -- never restate a conclusion, identity, or reasoning
   step you have already given, even in different words. Once you have said the answer once, stop.
"""

USER_TEMPLATE = """CONTEXT:
---
{context}
---

QUESTION: {question}

Answer using only the context above, with citations."""


def _format_context(chunks: list[dict]) -> str:
    parts = []
    for c in chunks:
        parts.append(f"[Source: {c['source']}, Page {c['page']}]\n{c['text']}")
    return "\n\n".join(parts)


def _call_groq_with_retry(client, **kwargs):
    """Groq's free tier has a tokens-per-minute limit (hit this at ~40+ questions
    in one eval run). Retry on 429 instead of crashing the whole run -- parse the
    server's suggested wait time out of the error message when present, else back
    off with a safe fixed pause."""
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            return client.chat.completions.create(**kwargs)
        except RateLimitError as e:
            if attempt == max_attempts - 1:
                raise
            match = re.search(r"try again in ([\d.]+)s", str(e))
            wait = float(match.group(1)) + 0.5 if match else 5.0
            print(f"  [rate limited -- waiting {wait:.1f}s, attempt {attempt + 1}/{max_attempts}]")
            time.sleep(wait)


def answer_question(question: str, k: int = 3, min_score: float | None = None) -> dict:
    """Retrieves top-k chunks, asks Groq to answer grounded in them.
    Returns the answer text plus the chunks used, so eval code can check
    faithfulness against exactly what the model saw.

    If min_score filters out every chunk, skips the LLM call entirely and
    returns an immediate refusal -- no point spending an API call when we
    already know there's zero retrieved context to answer from."""
    chunks = retrieve(question, k=k, min_score=min_score)

    if not chunks:
        return {
            "question": question,
            "answer": "This isn't covered in the provided material.",
            "retrieved_chunks": [],
        }

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    context = _format_context(chunks)

    response = _call_groq_with_retry(
        client,
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_TEMPLATE.format(context=context, question=question)},
        ],
        temperature=0,  # deterministic for eval reproducibility
        max_tokens=600,  # HARD guardrail (2026-07-22, raised 2026-07-31): prompt
        # instructions to "be concise" are probabilistic -- a live test (sin 200
        # degrees) showed the model can still loop, restating one correct
        # conclusion ~8 times across 4500+ chars, despite explicit anti-rambling
        # rules. 400 caps that damage but was confirmed (Q12, tan 255) to truncate
        # genuine multi-step derivations mid-expression when retrieval misses force
        # a from-scratch derivation. 600 gives more legitimate room while still far
        # below the runaway-rambling length.
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content,
        "retrieved_chunks": chunks,
    }


if __name__ == "__main__":
    test_questions = [
        "What is the sum and product of roots of a quadratic equation?",
        "What are the three basic trigonometric identities?",
        "How do you find the derivative of sin(x)?",  # should refuse
    ]

    # THRESHOLD_TO_TRY is just an experiment value based on the score gap we
    # observed manually (on-topic ~0.5-0.65, off-topic ~0.30-0.35) -- NOT a
    # decided/final cutoff. The eval harness will tell us the real answer.
    THRESHOLD_TO_TRY = 0.40

    for q in test_questions:
        print(f"Q: {q}")

        baseline = answer_question(q)  # min_score=None -- current default behavior
        print(f"  [baseline, no threshold]   A: {baseline['answer']}")
        print(f"    chunks retrieved: {[(c['source'], c['page'], round(c['score'], 3)) for c in baseline['retrieved_chunks']]}")

        thresholded = answer_question(q, min_score=THRESHOLD_TO_TRY)
        print(f"  [thresholded >= {THRESHOLD_TO_TRY}]        A: {thresholded['answer']}")
        print(f"    chunks retrieved: {[(c['source'], c['page'], round(c['score'], 3)) for c in thresholded['retrieved_chunks']]}")
        print()
