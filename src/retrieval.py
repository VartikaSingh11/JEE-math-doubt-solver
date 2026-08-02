"""
Retrieval: embed chunks with a local model, build a FAISS index, expose
retrieve(query, k) -> top-k most relevant chunks.

Model: sentence-transformers/all-MiniLM-L6-v2 -- small (~90MB), fast, free,
runs locally (no API key, no internet needed after the first download).

Similarity: cosine similarity, computed as inner product on L2-normalized
vectors (a standard equivalence) -- so embeddings are normalized before
indexing and before querying.
"""

import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = Path(__file__).parent.parent / "evals" / "chunks.json"
MODEL_NAME = "all-MiniLM-L6-v2"

_model = None
_index = None
_chunks = None


def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def _normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1e-10
    return vectors / norms


def build_index():
    """Loads chunks.json, embeds every chunk, builds an in-memory FAISS index.
    Trivial cost at this corpus size (52 chunks) -- a couple seconds on CPU."""
    global _index, _chunks
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        _chunks = json.load(f)

    model = _load_model()
    texts = [c["text"] for c in _chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    embeddings = _normalize(embeddings).astype("float32")

    dim = embeddings.shape[1]
    _index = faiss.IndexFlatIP(dim)  # inner product on normalized vectors == cosine similarity
    _index.add(embeddings)
    return _index, _chunks


def retrieve(query: str, k: int = 3, min_score: float | None = None) -> list[dict]:
    """Returns the top-k chunks for a query: text, source, page, similarity score.

    min_score is OPTIONAL and OFF by default (None = baseline behavior, always
    returns k chunks regardless of score). When set, chunks scoring below it are
    dropped -- which can mean fewer than k chunks, including zero.

    This is not yet decided to be better -- it's here so the eval harness can
    A/B "always top-k" vs "thresholded" once there are enough golden questions
    to measure it on, instead of us guessing a cutoff from 3 examples.

    PAGE-DIVERSIFIED (2026-07-31): reading raw retrieval misses in results.json
    showed a concrete, repeated pattern -- a handful of chunks (e.g. pages 13,
    17, 18 of Trigonometric_Ratios_and_Identities) are broad enough to score
    moderately-high against almost ANY trig query, and were winning 2 of the 3
    top-k slots on questions like Q11/Q21/Q24/Q33/Q40 (e.g. retrieved pages
    [12, 13, 13] instead of [12, 13, <the actually relevant page>]) -- wasting
    a slot on a near-duplicate instead of surfacing a different, more specific
    page. Fix: search a wider candidate pool, then greedily keep only the
    single best-scoring chunk per distinct (source, page) until k slots are
    filled, falling back to duplicates only if there aren't enough distinct
    pages in the pool. Ranking preference is otherwise untouched."""
    if _index is None:
        build_index()

    model = _load_model()
    query_vec = model.encode([query], convert_to_numpy=True)
    query_vec = _normalize(query_vec).astype("float32")

    pool_size = min(_index.ntotal, max(k * 5, k + 10))
    scores, indices = _index.search(query_vec, pool_size)

    candidates = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue
        if min_score is not None and score < min_score:
            continue
        chunk = _chunks[idx]
        candidates.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "page": chunk["page"],
            "score": float(score),
        })

    seen_pages = set()
    diversified = []
    leftover = []
    for c in candidates:
        key = (c["source"], c["page"])
        if key not in seen_pages:
            seen_pages.add(key)
            diversified.append(c)
        else:
            leftover.append(c)
        if len(diversified) == k:
            break

    if len(diversified) < k:
        diversified.extend(leftover[: k - len(diversified)])

    return diversified[:k]


if __name__ == "__main__":
    build_index()
    print(f"Indexed {len(_chunks)} chunks.\n")

    test_queries = [
        "What is the sum and product of roots of a quadratic equation?",
        "What are the three basic trigonometric identities?",
        "How do you find the derivative of sin(x)?",  # should NOT match well -- not in corpus
    ]
    for q in test_queries:
        print(f"Query: {q}")
        for r in retrieve(q, k=3):
            preview = r["text"][:120].replace("\n", " ")
            print(f"  [{r['score']:.3f}] {r['source']} p{r['page']}: {preview}...")
        print()
