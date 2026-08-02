"""
Evaluation harness. Implements the scoring rules Vartika decided on 2026-07-08:

1. Retrieval hit-rate: a "hit" means a chunk from the expected_source AND one of
   expected_pages appears ANYWHERE in the top-3 retrieved chunks (not just top-1).
2. Faithfulness (first pass): fraction of expected_facts substrings found
   (case-insensitive) in the generated answer. Cheap, no extra API calls.
   KNOWN LIMITATION: this only catches exact-ish phrasing, not paraphrases or
   semantic equivalence -- if this scores lower than answers actually look on
   manual read, that's the known weakness, not a surprise. Upgrading to an
   LLM-as-judge later (Project 7, file 15/20) is the measured fix for that,
   not something to silently patch around now.
3. Refusal accuracy: for unanswerable questions, did it actually decline?

This is boilerplate (the loop, the file I/O) implementing YOUR scoring rules --
if you want the scoring logic itself to work differently, that's your call to
change, not something to silently adjust.
"""

import json
import sys
from pathlib import Path

# Windows console defaults to cp1252, which can't display pi/theta/degree signs
# in question text -- reconfigure so printing never crashes on them (the actual
# results.json/report.md always had correct UTF-8 data; this only affects the
# console summary).
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from generate import answer_question

GOLDEN_SET_PATH = Path(__file__).parent.parent / "evals" / "golden_set.json"
RESULTS_PATH = Path(__file__).parent.parent / "evals" / "results.json"
REPORT_PATH = Path(__file__).parent.parent / "evals" / "report.md"

REFUSAL_PHRASES = [
    "isn't covered", "is not covered", "not covered in the provided material",
    "doesn't cover", "does not cover", "no information", "cannot answer",
]


def check_hit_rate(retrieved_chunks: list[dict], expected_source: str, expected_pages: list[int]) -> bool | None:
    if not expected_pages:
        return None  # not applicable (unanswerable questions have no "right" page)
    for chunk in retrieved_chunks:
        if chunk["source"] == expected_source and chunk["page"] in expected_pages:
            return True
    return False


def check_faithfulness(answer: str, expected_facts: list[str]) -> float | None:
    if not expected_facts:
        return None
    answer_lower = answer.lower()
    hits = sum(1 for fact in expected_facts if fact.lower() in answer_lower)
    return hits / len(expected_facts)


def check_refusal(answer: str) -> bool:
    answer_lower = answer.lower()
    return any(phrase in answer_lower for phrase in REFUSAL_PHRASES)


def run_eval(k: int = 3, min_score: float | None = None, resume: bool = True) -> dict:
    """resume=True (default): if results.json already has a non-failed result for
    a question, reuse it instead of spending another API call -- important given
    Groq's free-tier daily token cap. Only failed/missing questions get re-run."""
    with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as f:
        golden_set = json.load(f)

    previous_by_id = {}
    if resume and RESULTS_PATH.exists():
        try:
            with open(RESULTS_PATH, "r", encoding="utf-8") as f:
                prev = json.load(f)
            previous_by_id = {
                r["id"]: r for r in prev.get("results", [])
                if not r.get("failed") and not str(r.get("answer", "")).startswith("[ERROR:")
            }
        except (json.JSONDecodeError, KeyError):
            previous_by_id = {}

    results = []
    for i, item in enumerate(golden_set, start=1):
        if item["id"] in previous_by_id:
            print(f"[{i}/{len(golden_set)}] Q{item['id']}: reusing previous successful result")
            results.append(previous_by_id[item["id"]])
            continue

        print(f"[{i}/{len(golden_set)}] Q{item['id']}: {item['question'][:60]}")
        try:
            result = answer_question(item["question"], k=k, min_score=min_score)
        except Exception as e:
            # One question failing (rate limit exhausted, API hiccup, etc.) should
            # not lose the other answers already computed -- record it as a
            # failure (excluded from all stats below) and keep going.
            print(f"  !! FAILED after retries: {e}")
            results.append({
                "id": item["id"], "question": item["question"],
                "answerable": item.get("answerable", True), "failed": True,
                "hit_top3": None, "faithfulness": None, "refused": None,
                "answer": f"[ERROR: {e}]", "retrieved": [],
            })
            continue
        answerable = item.get("answerable", True)

        hit = check_hit_rate(
            result["retrieved_chunks"],
            item.get("expected_source"),
            item.get("expected_pages") or [],
        ) if answerable else None

        faithfulness = check_faithfulness(
            result["answer"], item.get("expected_facts") or []
        ) if answerable else None

        refused = check_refusal(result["answer"])

        results.append({
            "id": item["id"],
            "question": item["question"],
            "answerable": answerable,
            "failed": False,
            "hit_top3": hit,
            "faithfulness": faithfulness,
            "refused": refused,
            "answer": result["answer"],
            "retrieved": [(c["source"], c["page"], round(c["score"], 3)) for c in result["retrieved_chunks"]],
        })

    # Failed questions are excluded entirely from every stat below -- they are
    # "unknown", not "miss". Counting them as misses (the old bug) deflates
    # every percentage whenever the API has a bad day.
    scored = [r for r in results if not r.get("failed")]
    n_failed = len(results) - len(scored)

    answerable_results = [r for r in scored if r["answerable"]]
    unanswerable_results = [r for r in scored if not r["answerable"]]

    hit_rate = (
        sum(1 for r in answerable_results if r["hit_top3"]) / len(answerable_results)
        if answerable_results else None
    )
    faith_scores = [r["faithfulness"] for r in answerable_results if r["faithfulness"] is not None]
    avg_faithfulness = sum(faith_scores) / len(faith_scores) if faith_scores else None
    refusal_accuracy = (
        sum(1 for r in unanswerable_results if r["refused"]) / len(unanswerable_results)
        if unanswerable_results else None
    )

    summary = {
        "k": k,
        "min_score": min_score,
        "n_total": len(golden_set),
        "n_failed": n_failed,
        "n_answerable": len(answerable_results),
        "n_unanswerable": len(unanswerable_results),
        "retrieval_hit_rate_top3": hit_rate,
        "avg_faithfulness": avg_faithfulness,
        "refusal_accuracy": refusal_accuracy,
        "results": results,
    }

    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    return summary


def _fmt_pct(x):
    return f"{x:.0%}" if x is not None else "N/A"


def write_report(summary: dict, golden_set: list[dict]) -> None:
    """Human-readable Markdown version of results.json -- open this instead of
    asking to have JSON pasted back to you. One question per section: the
    question, the full answer, what was expected, what was actually retrieved,
    and the scored verdict."""
    golden_by_id = {item["id"]: item for item in golden_set}
    lines = []
    lines.append("# Evaluation Report\n")
    lines.append(f"Golden set: {summary['n_total']} questions "
                  f"({summary['n_answerable']} answerable, {summary['n_unanswerable']} unanswerable)\n")
    lines.append(f"- Retrieval hit-rate (top-3): **{_fmt_pct(summary['retrieval_hit_rate_top3'])}**")
    lines.append(f"- Avg faithfulness (keyword): **{_fmt_pct(summary['avg_faithfulness'])}**")
    lines.append(f"- Refusal accuracy: **{_fmt_pct(summary['refusal_accuracy'])}**\n")
    lines.append("---\n")

    for r in summary["results"]:
        item = golden_by_id.get(r["id"], {})
        hit_str = "✅ HIT" if r["hit_top3"] else ("❌ MISS" if r["hit_top3"] is False else "n/a (unanswerable)")
        faith_str = _fmt_pct(r["faithfulness"]) if r["faithfulness"] is not None else "n/a"

        lines.append(f"## Q{r['id']}: {r['question']}\n")
        lines.append(f"**Type:** {item.get('type', '?')} | **Difficulty:** {item.get('difficulty', '?')} "
                      f"| **Retrieval:** {hit_str} | **Faithfulness:** {faith_str} | **Refused:** {r['refused']}\n")

        if item.get("answerable", True):
            lines.append(f"**Expected source/page:** {item.get('expected_source')}, page(s) {item.get('expected_pages')}")
            lines.append(f"**Expected facts:** {item.get('expected_facts')}\n")
        else:
            lines.append("**Expected:** should refuse (unanswerable question)\n")

        lines.append("**Answer given:**")
        lines.append(f"> {r['answer']}\n")

        lines.append("**Chunks actually retrieved:**")
        for source, page, score in r["retrieved"]:
            lines.append(f"- {source}, page {page} (score {score})")
        lines.append("\n---\n")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore cached results and re-run every question. "
                              "Use after any prompt/generation change -- resuming "
                              "would otherwise silently mix old-prompt and new-prompt answers.")
    args = parser.parse_args()

    with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as f:
        _golden_set_for_report = json.load(f)

    summary = run_eval(resume=not args.fresh)
    write_report(summary, _golden_set_for_report)
    print(f"Readable report written to: {REPORT_PATH}\n")

    print(f"Golden set: {summary['n_total']} questions ({summary['n_answerable']} answerable, {summary['n_unanswerable']} unanswerable)")
    if summary.get("n_failed"):
        print(f"⚠ {summary['n_failed']} question(s) FAILED (excluded from stats below, not counted as misses) -- re-run later to fill in.")
    print()
    print(f"Retrieval hit-rate (top-3):     {_fmt_pct(summary['retrieval_hit_rate_top3'])}")
    print(f"Avg faithfulness (keyword):     {_fmt_pct(summary['avg_faithfulness'])}")
    print(f"Refusal accuracy (unanswerable): {_fmt_pct(summary['refusal_accuracy'])}")
    print(f"\nFull results saved to {RESULTS_PATH}\n")

    print("Per-question detail:")
    for r in summary["results"]:
        hit_str = "HIT" if r["hit_top3"] else ("MISS" if r["hit_top3"] is False else "n/a")
        faith_str = _fmt_pct(r["faithfulness"]) if r["faithfulness"] is not None else "n/a"
        print(f"  Q{r['id']} [{hit_str}, faithfulness={faith_str}, refused={r['refused']}]: {r['question'][:70]}")
