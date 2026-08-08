#!/usr/bin/env python3
"""APRIL local PDF quotation search, inspired by MEFinder (sabercomo/MEFinder).

No embeddings / vector DB / LLM. Cascading exact → compact → punctuation → fuzzy.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

CROSS_PAGE_TAIL = 900
CROSS_PAGE_HEAD = 900
SEARCH_MODES = {"auto", "exact", "compact", "punctuation", "fuzzy"}
MIN_PLAIN_CHARS = 20

QUOTE_TRANSLATION = str.maketrans(
    {
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "＂": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "‛": "'",
        "＇": "'",
        "「": '"',
        "」": '"',
        "『": '"',
        "』": '"',
    }
)

PUNCT_TRANSLATION = str.maketrans(
    {
        "。": ".",
        "，": ",",
        "、": ",",
        "；": ";",
        "：": ":",
        "？": "?",
        "！": "!",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "［": "[",
        "］": "]",
        "《": "<",
        "》": ">",
        "〈": "<",
        "〉": ">",
        "〔": "[",
        "〕": "]",
        "—": "-",
        "–": "-",
        "－": "-",
        "―": "-",
        "…": "...",
        "·": ".",
        "　": " ",
    }
)


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text or "")
    normalized = normalized.translate(QUOTE_TRANSLATION).translate(PUNCT_TRANSLATION)
    normalized = re.sub(r"([A-Za-z])-\s+([A-Za-z])", r"\1\2", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized.lower()


def compact_text(text: str) -> str:
    return re.sub(r"\s+", "", normalize_text(text))


def is_ignored_punctuation(ch: str) -> bool:
    if not ch or ch.isspace():
        return True
    category = unicodedata.category(ch)
    return category.startswith("P") or category.startswith("S")


def punctuationless_text(text: str) -> str:
    return "".join(ch for ch in normalize_text(text) if not is_ignored_punctuation(ch))


def normalize_with_map(text: str, mode: str) -> Tuple[str, List[int]]:
    out: List[str] = []
    mapping: List[int] = []
    for source_index, original in enumerate(text or ""):
        chunk = unicodedata.normalize("NFKC", original)
        chunk = chunk.translate(QUOTE_TRANSLATION).translate(PUNCT_TRANSLATION)
        for ch in chunk.lower():
            if mode in {"compact", "plain"} and ch.isspace():
                continue
            if mode == "plain" and is_ignored_punctuation(ch):
                continue
            out.append(ch)
            mapping.append(source_index)
    if mode == "normalized":
        return re.sub(r"\s+", " ", "".join(out)).strip(), mapping
    return "".join(out), mapping


def trim_for_display(text: str, limit: int = 260) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def char_ngrams(text: str, n: int = 2) -> List[str]:
    text = punctuationless_text(text)
    if len(text) <= n:
        return [text] if text else []
    return [text[i : i + n] for i in range(len(text) - n + 1)]


def best_window_ratio(query_plain: str, plain: str) -> Tuple[float, int, int]:
    if not query_plain or not plain:
        return 0.0, 0, 0
    if query_plain in plain:
        start = plain.find(query_plain)
        return 0.91, start, start + len(query_plain) - 1
    q_len = len(query_plain)
    if len(plain) <= q_len + 8:
        return difflib.SequenceMatcher(None, query_plain, plain).ratio(), 0, max(0, len(plain) - 1)
    window_sizes = sorted({q_len, int(q_len * 1.25) + 1, int(q_len * 1.6) + 1, q_len + 8})
    best = (0.0, 0, min(len(plain) - 1, q_len))
    step = max(1, q_len // 3)
    for size in window_sizes:
        if size <= 0:
            continue
        for start in range(0, max(1, len(plain) - size + 1), step):
            window = plain[start : start + size]
            ratio = difflib.SequenceMatcher(None, query_plain, window).ratio()
            if ratio > best[0]:
                best = (ratio, start, start + len(window) - 1)
        tail_start = max(0, len(plain) - size)
        window = plain[tail_start:]
        ratio = difflib.SequenceMatcher(None, query_plain, window).ratio()
        if ratio > best[0]:
            best = (ratio, tail_start, len(plain) - 1)
    return best


@dataclass
class PageRecord:
    pdf_page_index: int  # 0-based
    pdf_page_label: Optional[str]
    text_raw: str


@dataclass
class Unit:
    unit_id: str
    source_path: str
    document_title: str
    text_raw: str
    normalized_text: str
    compact_text: str
    plain_text: str
    pdf_page_start_index: int
    pdf_page_end_index: int
    pdf_page_start_label: Optional[str]
    pdf_page_end_label: Optional[str]
    is_cross_page: bool


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_pages(path: Path) -> List[PageRecord]:
    try:
        import fitz  # type: ignore

        doc = fitz.open(path)
        pages: List[PageRecord] = []
        for i in range(doc.page_count):
            page = doc.load_page(i)
            label = None
            try:
                labels = doc.get_page_labels()
                if labels:
                    label = page.get_label() or None
            except Exception:
                label = None
            text = page.get_text("text") or ""
            pages.append(PageRecord(pdf_page_index=i, pdf_page_label=label or None, text_raw=text))
        doc.close()
        return pages
    except ImportError:
        pass

    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        label = None
        try:
            label = page.page_label  # type: ignore[attr-defined]
        except Exception:
            label = None
        pages.append(PageRecord(pdf_page_index=i, pdf_page_label=str(label) if label else None, text_raw=text))
    return pages


def strip_header_for_cross(text: str) -> str:
    """Remove likely page numbers / running heads from the next-page side."""
    lines = (text or "").splitlines()
    drop = 0
    for line in lines[:8]:
        value = line.strip()
        if not value:
            drop += 1
            continue
        compact = re.sub(r"\s+", "", value)
        alpha = [ch for ch in compact if ch.isalpha()]
        uppercase_ratio = (
            sum(1 for ch in alpha if ch.upper() == ch and ch.lower() != ch) / max(len(alpha), 1)
            if alpha
            else 0.0
        )
        if re.fullmatch(r"\d{1,4}|[ivxlcdmIVXLCDM]{1,8}", compact):
            drop += 1
            continue
        if len(compact) <= 40 and alpha and uppercase_ratio >= 0.75:
            drop += 1
            continue
        break
    return "\n".join(lines[drop:]).strip()


def pages_to_units(path: Path, pages: Sequence[PageRecord]) -> List[Unit]:
    source_id = f"pdf-{file_sha256(path)[:12]}"
    title = path.stem
    units: List[Unit] = []
    for page in pages:
        text = (page.text_raw or "").strip()
        if not text:
            continue
        plain = punctuationless_text(text)
        if len(plain) < MIN_PLAIN_CHARS:
            continue
        units.append(
            Unit(
                unit_id=f"{source_id}-P{page.pdf_page_index:06d}",
                source_path=str(path.resolve()),
                document_title=title,
                text_raw=text,
                normalized_text=normalize_text(text),
                compact_text=compact_text(text),
                plain_text=plain,
                pdf_page_start_index=page.pdf_page_index,
                pdf_page_end_index=page.pdf_page_index,
                pdf_page_start_label=page.pdf_page_label,
                pdf_page_end_label=page.pdf_page_label,
                is_cross_page=False,
            )
        )
    for left, right in zip(pages, pages[1:]):
        left_text = (left.text_raw or "").strip()
        right_text = (right.text_raw or "").strip()
        if not left_text or not right_text:
            continue
        cross = f"{left_text[-CROSS_PAGE_TAIL:]}\n{strip_header_for_cross(right_text)[:CROSS_PAGE_HEAD]}"
        plain = punctuationless_text(cross)
        # MEFinder uses 80; keep a slightly lower floor so short native-text PDFs still bridge.
        if len(plain) < 40:
            continue
        units.append(
            Unit(
                unit_id=f"{source_id}-CROSS-{left.pdf_page_index:06d}-{right.pdf_page_index:06d}",
                source_path=str(path.resolve()),
                document_title=title,
                text_raw=cross,
                normalized_text=normalize_text(cross),
                compact_text=compact_text(cross),
                plain_text=plain,
                pdf_page_start_index=left.pdf_page_index,
                pdf_page_end_index=right.pdf_page_index,
                pdf_page_start_label=left.pdf_page_label,
                pdf_page_end_label=right.pdf_page_label,
                is_cross_page=True,
            )
        )
    return units


def discover_pdfs(path: Path) -> List[Path]:
    path = path.expanduser().resolve()
    if path.is_file():
        if path.suffix.lower() != ".pdf":
            raise SystemExit(f"Not a PDF: {path}")
        return [path]
    if not path.is_dir():
        raise SystemExit(f"Path not found: {path}")
    return sorted(p for p in path.rglob("*.pdf") if p.is_file())


def load_units_from_paths(paths: Sequence[Path]) -> List[Unit]:
    units: List[Unit] = []
    for pdf in paths:
        try:
            pages = extract_pages(pdf)
        except Exception as exc:
            print(f"WARN: failed to extract {pdf}: {exc}", file=sys.stderr)
            continue
        units.extend(pages_to_units(pdf, pages))
    return units


SCHEMA = """
CREATE TABLE IF NOT EXISTS units (
  unit_id TEXT PRIMARY KEY,
  source_path TEXT NOT NULL,
  document_title TEXT NOT NULL,
  text_raw TEXT NOT NULL,
  normalized_text TEXT NOT NULL,
  compact_text TEXT NOT NULL,
  plain_text TEXT NOT NULL,
  pdf_page_start_index INTEGER NOT NULL,
  pdf_page_end_index INTEGER NOT NULL,
  pdf_page_start_label TEXT,
  pdf_page_end_label TEXT,
  is_cross_page INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_units_norm ON units(normalized_text);
CREATE INDEX IF NOT EXISTS idx_units_compact ON units(compact_text);
CREATE INDEX IF NOT EXISTS idx_units_plain ON units(plain_text);
CREATE INDEX IF NOT EXISTS idx_units_path ON units(source_path);
"""


def open_index(index_path: Path, writable: bool = False) -> sqlite3.Connection:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(index_path))
    conn.row_factory = sqlite3.Row
    if writable:
        conn.executescript(SCHEMA)
    return conn


def index_pdfs(corpus: Path, index_path: Path) -> Dict[str, object]:
    pdfs = discover_pdfs(corpus)
    units = load_units_from_paths(pdfs)
    conn = open_index(index_path, writable=True)
    conn.execute("DELETE FROM units")
    for u in units:
        conn.execute(
            """
            INSERT INTO units (
              unit_id, source_path, document_title, text_raw, normalized_text,
              compact_text, plain_text, pdf_page_start_index, pdf_page_end_index,
              pdf_page_start_label, pdf_page_end_label, is_cross_page
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                u.unit_id,
                u.source_path,
                u.document_title,
                u.text_raw,
                u.normalized_text,
                u.compact_text,
                u.plain_text,
                u.pdf_page_start_index,
                u.pdf_page_end_index,
                u.pdf_page_start_label,
                u.pdf_page_end_label,
                1 if u.is_cross_page else 0,
            ),
        )
    conn.commit()
    meta = {
        "pdf_count": len(pdfs),
        "unit_count": len(units),
        "index_path": str(index_path.resolve()),
        "corpus": str(corpus.resolve()),
    }
    conn.close()
    return meta


def unit_from_row(row: sqlite3.Row | Unit) -> Unit:
    if isinstance(row, Unit):
        return row
    return Unit(
        unit_id=row["unit_id"],
        source_path=row["source_path"],
        document_title=row["document_title"],
        text_raw=row["text_raw"],
        normalized_text=row["normalized_text"],
        compact_text=row["compact_text"],
        plain_text=row["plain_text"],
        pdf_page_start_index=int(row["pdf_page_start_index"]),
        pdf_page_end_index=int(row["pdf_page_end_index"]),
        pdf_page_start_label=row["pdf_page_start_label"],
        pdf_page_end_label=row["pdf_page_end_label"],
        is_cross_page=bool(row["is_cross_page"]),
    )


def page_display(unit: Unit) -> str:
    start = unit.pdf_page_start_index + 1
    end = unit.pdf_page_end_index + 1
    label_bits = []
    if unit.pdf_page_start_label:
        label_bits.append(str(unit.pdf_page_start_label))
    if unit.is_cross_page and unit.pdf_page_end_label and unit.pdf_page_end_label != unit.pdf_page_start_label:
        label_bits.append(str(unit.pdf_page_end_label))
    if start == end:
        base = f"PDF page {start}"
    else:
        base = f"PDF pages {start}-{end}"
    if label_bits:
        return f"{base} (label: {'-'.join(label_bits)}); citation page not calibrated"
    return f"{base}; citation page not calibrated"


def mapped_span(raw: str, query: str, mode: str) -> Tuple[int, int]:
    normalized, mapping = normalize_with_map(raw, mode)
    pos = normalized.find(query)
    if pos < 0 or not mapping:
        return 0, 0
    end_pos = min(pos + len(query) - 1, len(mapping) - 1)
    return mapping[pos], mapping[end_pos] + 1


def format_hit(unit: Unit, match_type: str, score: float, start: int, end: int) -> Dict[str, object]:
    raw = unit.text_raw
    start = max(0, min(start, len(raw)))
    end = max(start, min(end, len(raw)))
    matched = raw[start:end] if end > start else trim_for_display(raw, 80)
    ctx_start = max(0, start - 80)
    ctx_end = min(len(raw), end + 80)
    context = raw[ctx_start:ctx_end]
    return {
        "unit_id": unit.unit_id,
        "source_path": unit.source_path,
        "document_title": unit.document_title,
        "match_type": match_type,
        "match_score": round(float(score), 4),
        "matched_text": matched,
        "context": context,
        "paragraph_text": trim_for_display(raw, 400),
        "pdf_page_start_1based": unit.pdf_page_start_index + 1,
        "pdf_page_end_1based": unit.pdf_page_end_index + 1,
        "pdf_page_start_index": unit.pdf_page_start_index,
        "pdf_page_end_index": unit.pdf_page_end_index,
        "pdf_page_start_label": unit.pdf_page_start_label,
        "pdf_page_end_label": unit.pdf_page_end_label,
        "is_cross_page": unit.is_cross_page,
        "page_display": page_display(unit),
        "copy_text": f"{unit.document_title}，{page_display(unit)}：{matched}",
        "char_start": start,
        "char_end": end,
    }


class SearchEngine:
    def __init__(self, units: Sequence[Unit]) -> None:
        self.units = list(units)
        self.ngram_index: Dict[str, List[int]] = defaultdict(list)
        for idx, unit in enumerate(self.units):
            for gram in set(char_ngrams(unit.plain_text)):
                self.ngram_index[gram].append(idx)

    @classmethod
    def from_index(cls, index_path: Path) -> "SearchEngine":
        conn = open_index(index_path)
        rows = conn.execute("SELECT * FROM units").fetchall()
        conn.close()
        return cls([unit_from_row(r) for r in rows])

    @classmethod
    def from_corpus(cls, corpus: Path) -> "SearchEngine":
        return cls(load_units_from_paths(discover_pdfs(corpus)))

    def search(self, query: str, mode: str = "auto", limit: int = 10) -> Dict[str, object]:
        query = (query or "").strip()
        if mode not in SEARCH_MODES:
            mode = "auto"
        limit = max(1, min(int(limit or 10), 200))
        if not query:
            return {"query": query, "mode": mode, "total": 0, "results": []}

        q_norm = normalize_text(query)
        q_compact = compact_text(query)
        q_plain = punctuationless_text(query)
        candidates: Dict[str, Dict[str, object]] = {}

        if mode in {"auto", "exact"}:
            self._exact_pass(query, q_norm, candidates)
        if mode in {"auto", "compact"} and (mode != "auto" or not candidates):
            self._mapped_pass(q_compact, "compact", "space_insensitive", 0.96, candidates)
        if mode in {"auto", "punctuation"} and (mode != "auto" or not candidates):
            self._mapped_pass(q_plain, "plain", "punctuation_insensitive", 0.92, candidates)
        if mode in {"auto", "fuzzy"} and (mode != "auto" or not candidates):
            self._fuzzy_pass(q_plain, candidates)

        ranked = sorted(
            candidates.values(),
            key=lambda item: (-float(item["match_score"]), item.get("is_cross_page", False), item["source_path"]),
        )
        merged = self._merge(ranked)
        return {
            "query": query,
            "mode": mode,
            "total": len(merged),
            "results": merged[:limit],
        }

    def _add(self, unit: Unit, match_type: str, score: float, start: int, end: int, candidates: Dict[str, Dict[str, object]]) -> None:
        existing = candidates.get(unit.unit_id)
        if existing is not None and float(existing["match_score"]) >= score:
            return
        candidates[unit.unit_id] = format_hit(unit, match_type, score, start, end)

    def _exact_pass(self, query: str, q_norm: str, candidates: Dict[str, Dict[str, object]]) -> None:
        for unit in self.units:
            raw_pos = unit.text_raw.find(query)
            if raw_pos >= 0:
                self._add(unit, "exact", 1.0, raw_pos, raw_pos + len(query), candidates)
                continue
            if q_norm and q_norm in unit.normalized_text:
                start, end = mapped_span(unit.text_raw, q_norm, "normalized")
                self._add(unit, "normalized_exact", 0.985, start, end, candidates)

    def _mapped_pass(
        self,
        query: str,
        mode: str,
        match_type: str,
        score: float,
        candidates: Dict[str, Dict[str, object]],
    ) -> None:
        if not query:
            return
        field = "compact_text" if mode == "compact" else "plain_text"
        for unit in self.units:
            haystack = getattr(unit, field)
            pos = haystack.find(query)
            if pos < 0:
                continue
            _, mapping = normalize_with_map(unit.text_raw, mode)
            if pos >= len(mapping):
                continue
            end_pos = min(pos + len(query) - 1, len(mapping) - 1)
            self._add(unit, match_type, score, mapping[pos], mapping[end_pos] + 1, candidates)

    def _fuzzy_pass(self, q_plain: str, candidates: Dict[str, Dict[str, object]]) -> None:
        if not q_plain:
            return
        grams = char_ngrams(q_plain)
        counts: Counter[int] = Counter()
        for gram in grams:
            counts.update(self.ngram_index.get(gram, []))
        search_space = [idx for idx, _ in counts.most_common(700)] if counts else list(range(min(len(self.units), 800)))
        for idx in search_space:
            unit = self.units[idx]
            ratio, start, end = best_window_ratio(q_plain, unit.plain_text)
            if ratio < 0.58:
                continue
            _, mapping = normalize_with_map(unit.text_raw, "plain")
            if not mapping:
                continue
            start = max(0, min(start, len(mapping) - 1))
            end = max(start, min(end, len(mapping) - 1))
            score = min(0.9, max(0.58, ratio))
            self._add(unit, "ngram_fuzzy", score, mapping[start], mapping[end] + 1, candidates)

    def _merge(self, ranked: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
        merged: List[Dict[str, object]] = []
        seen = set()
        for item in ranked:
            if item.get("is_cross_page") and self._cross_page_duplicate(item, ranked):
                continue
            key = (
                item.get("source_path"),
                punctuationless_text(str(item.get("matched_text") or ""))[:180],
                item.get("pdf_page_start_index"),
            )
            if key in seen:
                continue
            seen.add(key)
            merged.append(item)
        return merged

    @staticmethod
    def _cross_page_duplicate(cross_item: Dict[str, object], ranked: Sequence[Dict[str, object]]) -> bool:
        matched = punctuationless_text(str(cross_item.get("matched_text") or ""))
        if not matched:
            return False
        for item in ranked:
            if item is cross_item or item.get("is_cross_page"):
                continue
            if item.get("source_path") != cross_item.get("source_path"):
                continue
            other = punctuationless_text(str(item.get("matched_text") or ""))
            if matched and matched in other:
                return True
        return False


def skill_python() -> Path:
    return Path(__file__).resolve().parents[1] / ".venv" / "bin" / "python"


def cmd_index(args: argparse.Namespace) -> int:
    meta = index_pdfs(Path(args.path), Path(args.index))
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    if args.index:
        engine = SearchEngine.from_index(Path(args.index))
    elif args.path:
        engine = SearchEngine.from_corpus(Path(args.path))
    else:
        raise SystemExit("Provide --path (PDF/dir) or --index")
    result = engine.search(args.query, mode=args.mode, limit=args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search and page-pin quotations in local PDFs.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="Build a SQLite index from a PDF or directory")
    p_index.add_argument("--path", required=True, help="PDF file or directory to index")
    p_index.add_argument("--index", required=True, help="Output SQLite path")
    p_index.set_defaults(func=cmd_index)

    p_search = sub.add_parser("search", help="Search a corpus or an existing index")
    p_search.add_argument("query", help="Exact sentence, fragment, or slightly noisy text")
    p_search.add_argument("--path", help="PDF file or directory (on-the-fly extract)")
    p_search.add_argument("--index", help="Existing SQLite index from `index`")
    p_search.add_argument("--mode", default="auto", choices=sorted(SEARCH_MODES))
    p_search.add_argument("--limit", type=int, default=10)
    p_search.set_defaults(func=cmd_search)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
