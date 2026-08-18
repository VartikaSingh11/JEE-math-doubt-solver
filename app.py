"""
Streamlit UI for the JEE Math Doubt-Solver (RAG + Evaluation Harness).

Boilerplate (Claude's job per CLAUDE.md) -- the core retrieval/generation/eval
logic this wraps was built and measured separately; this file only presents it.
"""

import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).parent / "src"))

from generate import answer_question  # noqa: E402

st.set_page_config(page_title="JEE Math Doubt-Solver", page_icon="📐", layout="centered")

TOPICS_COVERED = ["Quadratic Equations", "Trigonometric Ratios & Identities"]

EXAMPLE_QUESTIONS = [
    "What is the sum and product of roots of a quadratic equation?",
    "Find sin75° using compound-angle formula.",
    "If D is the discriminant of a quadratic equation, what does D > 0, D = 0, and D < 0 tell us?",
    "Evaluate tan 255°.",
]

# --- Sidebar -----------------------------------------------------------------
with st.sidebar:
    st.header("About this project")
    st.markdown(
        "A RAG (Retrieval-Augmented Generation) system that answers JEE Math "
        "doubts grounded in real study notes -- with citations, and a measured "
        "evaluation harness proving how well it actually works."
    )
    st.markdown("**Topics currently covered:**")
    for t in TOPICS_COVERED:
        st.markdown(f"- {t}")
    st.markdown(
        "Questions outside these topics (e.g. calculus) are correctly declined "
        "rather than guessed at."
    )

    st.divider()
    st.markdown("**Measured performance** (49-question eval set, 48 answerable)")
    st.metric("Retrieval hit-rate (top-3)", "63%")
    st.metric("Answer faithfulness", "73%")
    st.metric("Refusal accuracy", "100%")

    st.divider()
    st.markdown(
        "**Known limitations** (stated honestly, not hidden):\n"
        "- Source PDFs were OCR'd; math notation (fractions, √, Greek letters) "
        "occasionally garbles in the underlying chunks.\n"
        "- Retrieval is stronger on Quadratic Equations (78% hit-rate) than "
        "Trigonometry (48%) -- a few broad trig chunks score moderately-high "
        "against almost any trig question, crowding out the actually-relevant page.\n"
        "- Faithfulness is measured by keyword match against hand-written expected "
        "facts, not an LLM judge -- it can under- or over-score a correct answer "
        "phrased differently than expected (see README for the full discussion).\n"
        "- Citations are not yet independently verified against the cited page's "
        "actual content (a known, logged gap -- see project README).\n"
        "- On problems with two valid final values (e.g. squared conditions), the "
        "model sometimes reports only one -- a known, accepted residual gap.\n"
        "- Hosted on Streamlit Community Cloud's free tier: the app sleeps after a "
        "period of inactivity, so the first visit after idle time shows a "
        "'waking up' screen for ~30-60 seconds."
    )

# --- Main ----------------------------------------------------------------
st.title("📐 JEE Math Doubt-Solver")
st.caption("Ask a JEE-level math doubt. Answers are grounded in real study notes, with citations.")

if "question_input" not in st.session_state:
    st.session_state.question_input = ""

st.markdown("**Try an example:**")
cols = st.columns(2)
for i, q in enumerate(EXAMPLE_QUESTIONS):
    if cols[i % 2].button(q, use_container_width=True):
        st.session_state.question_input = q

# NOTE: key= ties this widget to session_state.question_input directly -- do
# NOT also pass value= here, that combination is what caused the bug where
# clicking "Ask" reset the text back to empty (found via actual UI testing,
# not assumed): on the Ask-click rerun no example button fires that pass, so
# a value= expression referencing button state silently resets to "".
question = st.text_area(
    "Your question",
    key="question_input",
    placeholder="e.g. What are the three basic trigonometric identities?",
    height=80,
)

ask = st.button("Ask", type="primary")

if ask and question.strip():
    with st.spinner("Retrieving relevant notes and generating an answer..."):
        try:
            result = answer_question(question.strip())
        except Exception as e:
            st.error(
                "Something went wrong reaching the language model. "
                "This is often a temporary rate limit -- try again in a minute.\n\n"
                f"Details: {e}"
            )
            result = None

    if result:
        st.markdown("### Answer")
        st.write(result["answer"])

        if result["retrieved_chunks"]:
            with st.expander("📄 Sources retrieved for this answer"):
                for c in result["retrieved_chunks"]:
                    st.markdown(f"**{c['source']}, page {c['page']}** (similarity: {c['score']:.3f})")
                    st.text(c["text"][:400] + ("..." if len(c["text"]) > 400 else ""))
                    st.divider()
        else:
            st.info("No relevant sources were retrieved for this question.")

elif ask:
    st.warning("Please enter a question first.")
