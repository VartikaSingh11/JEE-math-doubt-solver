"""
Ingestion: PDF -> OCR'd text -> naive fixed-size chunks with metadata.

WHY OCR instead of PyMuPDF's normal text extraction (page.get_text()):
our source PDFs have a corrupted/non-standard text layer (confirmed on 2 files) --
extracting it directly gives garbage. Rendering each page to an image and running
Tesseract over it reads what a human actually sees, so it works regardless of the
broken text layer underneath.

Baseline chunking (per the eval-first rule in CLAUDE.md): fixed-size, naive.
Do not "improve" this without an eval run proving the change helps -- that
comparison IS the project.
"""

import argparse
import json
import re
from pathlib import Path

import fitz  # pymupdf
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
EVALS_DIR = Path(__file__).parent.parent / "evals"

CHUNK_SIZE_CHARS = 2000   # ~roughly 500 tokens
CHUNK_OVERLAP_CHARS = 200 # ~roughly 50 tokens

# A numbered section header looks like "3. RELATION BETWEEN ROOTS..." -- digit(s),
# period, then real content, short enough to be a heading not a sentence.
SECTION_HEADER_RE = re.compile(r"^\s*\d{1,2}\.\s+\S")


def ocr_pdf_to_pages(pdf_path: Path, dpi: int = 300) -> list[str]:
    """Render each page to an image and OCR it. Returns one string per page."""
    doc = fitz.open(pdf_path)
    page_texts = []
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        text = pytesseract.image_to_string(img)
        page_texts.append(text)
    doc.close()
    return page_texts


NOISE_PATTERNS = [
    r"D:\\Data\\TARGET-201\s*2\\?\s*TEACHING NOTES\\?[^\.]*",
    r"ALLEN\b",
    r"CAREER INSTITUTE",
    r"Path t[oe] Success",
    r"MATHEMATICS\b",
    r"KOTA\s*\(?RAJASTHAN\)?",
]


def clean_ocr_text(text: str) -> str:
    """Strip Allen-branding/watermark noise picked up by OCR (headers/footers/file paths).
    Content itself (standard IIT-JEE syllabus material) is kept -- only institutional branding is removed."""
    for pattern in NOISE_PATTERNS:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)
    return text


def chunk_text(text: str, source: str, page_num: int) -> list[dict]:
    """Fixed-size chunking with overlap. Naive baseline -- see module docstring."""
    text = clean_ocr_text(text)
    text = re.sub(r"\s+", " ", text).strip()
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE_CHARS
        chunk_text_piece = text[start:end]
        if chunk_text_piece.strip():
            chunks.append({
                "text": chunk_text_piece,
                "source": source,
                "page": page_num,
            })
        start = end - CHUNK_OVERLAP_CHARS
    return chunks


def chunk_by_section(text: str, source: str, page_num: int) -> list[dict]:
    """EXPERIMENT (2026-07-11): split at the notes' own numbered section headers
    (e.g. '3. RELATION BETWEEN ROOTS...') instead of a fixed character count, so
    each concept stays one coherent chunk. Only within a page -- a section that
    spans a page boundary is still split there, same limitation as before.

    Not yet proven better than the naive baseline -- compare hit-rate via
    compare_chunking.py before treating this as the default (CLAUDE.md rule:
    no chunking change is kept unless the eval shows it wins)."""
    text = clean_ocr_text(text)
    lines = text.split("\n")

    chunks = []
    current = []

    def flush():
        piece = re.sub(r"\s+", " ", " ".join(current)).strip()
        if piece:
            chunks.append({"text": piece, "source": source, "page": page_num})

    for line in lines:
        stripped = line.strip()
        if SECTION_HEADER_RE.match(stripped) and len(stripped) < 90 and current:
            flush()
            current = [line]
        else:
            current.append(line)
    flush()

    return chunks


def ingest_all(strategy: str = "section") -> None:
    # DEFAULT CHANGED 2026-07-11: section-based chunking measured 64% hit-rate vs
    # naive's 50% on the golden set (2 fixed, 0 regressions) -- see log.md. It's
    # now the default; "naive" is kept only for future comparison experiments.
    chunk_fn = chunk_by_section if strategy == "section" else chunk_text
    output_path = EVALS_DIR / ("chunks.json" if strategy == "section" else "chunks_naive_baseline.json")

    all_chunks = []
    pdf_files = sorted(CORPUS_DIR.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDFs found in {CORPUS_DIR}. Place your topic PDFs there first.")
        return

    for pdf_path in pdf_files:
        print(f"OCR'ing {pdf_path.name} ...")
        page_texts = ocr_pdf_to_pages(pdf_path)
        for i, page_text in enumerate(page_texts, start=1):
            all_chunks.extend(chunk_fn(page_text, source=pdf_path.stem, page_num=i))
        print(f"  -> {len(page_texts)} pages OCR'd")

    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"\nStrategy: {strategy}")
    print(f"Total chunks: {len(all_chunks)}")
    print(f"Saved to {output_path}")
    print("\nSpot-check chunk 0:")
    print(all_chunks[0]["text"][:300] if all_chunks else "(no chunks)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", choices=["naive", "section"], default="section")
    args = parser.parse_args()
    ingest_all(strategy=args.strategy)
