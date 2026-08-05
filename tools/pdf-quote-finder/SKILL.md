---
name: pdf-quote-finder
description: >-
  Locate exact sentences, fragments, or slightly noisy quotes in local PDF
  files without embeddings or LLMs. Use when the user asks to find a quote in
  PDFs, locate原文/原句, search a local literature corpus, or pin a passage to a
  PDF page (MEFinder-style local text search).
---

# PDF Quote Finder

Local-first PDF quote locator inspired by [MEFinder](https://github.com/sabercomo/MEFinder).
Search, extract, and page pinning stay on disk — no vector DB, embeddings, or LLM API.

## When to use

- Find where a sentence / fragment appears in local PDFs
- Recover page numbers for citations from a quote
- Tolerate spacing, punctuation, or minor OCR/copy noise
- Prefer deterministic local search over semantic RAG

## Interpreter

Always run scripts with the skill venv (has PyMuPDF):

```bash
APRIL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/APRIL"
TOOL_ROOT="$APRIL_ROOT/tools/pdf-quote-finder"
PYTHON="$TOOL_ROOT/.venv/bin/python"
SCRIPT="$TOOL_ROOT/scripts/pdf_quote_finder.py"
```

If the venv is missing:

```bash
cd "$TOOL_ROOT"
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

## Workflow

1. Confirm the PDF file or directory path with the user if unclear.
2. **Small corpus / one-off** → `search --path` (extracts on the fly).
3. **Many PDFs / repeated queries** → `index` once, then `search --index`.
4. Present hits with file path, PDF page (1-based), match type/score, and context.
5. Never treat PDF physical page as the printed citation page unless the user
   has calibrated it. Say: `PDF page N; citation page not calibrated`.

## Commands

### Search (on the fly)

```bash
"$PYTHON" "$SCRIPT" search "exact or noisy quote" \
  --path "/path/to/file-or-dir" \
  --mode auto \
  --limit 10
```

### Build index

```bash
"$PYTHON" "$SCRIPT" index \
  --path "/path/to/pdfs" \
  --index "/path/to/pdf-quote-index.sqlite3"
```

### Search an index

```bash
"$PYTHON" "$SCRIPT" search "quote" \
  --index "/path/to/pdf-quote-index.sqlite3" \
  --mode auto \
  --limit 10
```

## Match modes

| Mode | Behavior |
|---|---|
| `auto` | exact → space-insensitive → punctuation-insensitive → fuzzy (stop at first hit tier) |
| `exact` | Raw / NFKC-normalized substring |
| `compact` | Ignore whitespace differences |
| `punctuation` | Ignore whitespace + punctuation/symbol differences |
| `fuzzy` | Char bigram candidate filter + sliding-window `difflib` (≥ 0.58) |

## Result fields to surface

From each JSON hit, report at least:

- `document_title` / `source_path`
- `page_display` (PDF page + optional Page Label)
- `match_type` + `match_score`
- `matched_text` and short `context`
- `is_cross_page` when true
- `copy_text` when the user wants a pasteable citation stub

## Constraints (from MEFinder design)

- Prefer **PyMuPDF** text extraction; `pypdf` is fallback only.
- Scanned / image-only PDFs with no text layer will not match. Tell the user
  OCR/MinerU-style parsing is required; this skill does not call remote OCR.
- Do not invent citation pages from PDF page indices.
- Cross-page quotes are indexed via adjacent-page windows (tail+head).

## Output style

Keep the reply short: ranked list of hits, then offer to open the PDF at the
matched page or refine the query/mode. Prefer JSON tool output as evidence;
do not dump the full page text unless asked.

## Extra detail

See [reference.md](reference.md) for normalization rules and MEFinder mapping.
