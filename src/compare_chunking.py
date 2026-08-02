"""
Compare retrieval hit-rate between the naive (fixed-size) and section-header
chunking strategies -- isolated to retrieval only, no generation/API calls,
so it's fast and directly targets the metric in question (per the "change one
thing, measure it" rule). Reuses retrieval.py's embedding model/normalization
so both strategies are scored identically.
"""

import json
from pathlib import Path

import faiss
import numpy as np

from retrieval import _load_model, _normalize

EVALS_DIR = Path(__file__).parent.parent / "evals"
GOLDEN_SET_PATH = EVALS_DIR / "golden_set.json"

STRATEGIES = {
    "naive (baseline)": EVALS_DIR / "chunks.json",
    "section-header (experiment)": EVALS_DIR / "chunks_section.json",
}


def build_index_from_file(chunks_path: Path):
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    model = _load_model()
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    embeddings = _normalize(embeddings).astype("float32")
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    return index, chunks


def retrieve_from(index, chunks, model, query, k=3):
    q = model.encode([query], convert_to_numpy=True)
    q = _normalize(q).astype("float32")
    scores, indices = index.search(q, k)
    return [chunks[i] for i in indices[0] if i != -1]


def hit(retrieved, expected_source, expected_pages):
    if not expected_pages:
        return None
    return any(c["source"] == expected_source and c["page"] in expected_pages for c in retrieved)


def main():
    with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as f:
        golden_set = json.load(f)
    answerable = [q for q in golden_set if q.get("answerable", True)]

    model = _load_model()
    results = {}

    for label, path in STRATEGIES.items():
        if not path.exists():
            print(f"Skipping '{label}' -- {path.name} not found yet.")
            continue
        index, chunks = build_index_from_file(path)
        print(f"{label}: {len(chunks)} chunks indexed")

        hits = []
        per_q = []
        for q in answerable:
            retrieved = retrieve_from(index, chunks, model, q["question"], k=3)
            h = hit(retrieved, q.get("expected_source"), q.get("expected_pages") or [])
            if h is not None:
                hits.append(h)
            per_q.append((q["id"], h))

        hit_rate = sum(hits) / len(hits) if hits else None
        results[label] = {"hit_rate": hit_rate, "per_q": per_q}

    print("\n=== HIT-RATE COMPARISON (top-3, same golden set) ===")
    for label, r in results.items():
        rate = f"{r['hit_rate']:.0%}" if r["hit_rate"] is not None else "N/A"
        print(f"{label}: {rate}")

    if len(results) == 2:
        labels = list(results.keys())
        print(f"\nPer-question ({labels[0]} vs {labels[1]}):")
        a = dict(results[labels[0]]["per_q"])
        b = dict(results[labels[1]]["per_q"])
        for qid in a:
            va = "HIT" if a[qid] else "MISS"
            vb = "HIT" if b.get(qid) else "MISS"
            flag = "  <-- DIFFERS" if a[qid] != b.get(qid) else ""
            print(f"  Q{qid}: {va} -> {vb}{flag}")


if __name__ == "__main__":
    main()
