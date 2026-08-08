# APRIL local PDF quote search

Use APRIL's integrated local locator to find exact sentences, fragments, or slightly noisy quotations in PDFs and pin them to physical PDF pages. Search and extraction remain on disk; the tool does not use embeddings, a vector database, or an LLM API.

## When to use

- Locate the source PDF for a remembered sentence or fragment.
- Recover a physical PDF page for citation verification.
- Search through spacing, punctuation, hyphenation, or minor OCR/copy noise.
- Verify a quotation before using it in a literature review or Discussion.

Do not use quotation search as a substitute for reading the source, checking whether it supports the surrounding claim, or verifying bibliographic metadata.

## Interpreter

Run the internal APRIL script with its bundled environment:

```bash
APRIL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/APRIL"
TOOL_ROOT="$APRIL_ROOT/tools/pdf-quote-finder"
PYTHON="$TOOL_ROOT/.venv/bin/python"
SCRIPT="$TOOL_ROOT/scripts/pdf_quote_finder.py"
```

If the environment is missing:

```bash
cd "$TOOL_ROOT"
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

## Workflow

1. Confirm the PDF file or directory when its location is unclear.
2. For one PDF or a small corpus, search directly with `--path`.
3. For repeated searches across many PDFs, build an index once and search with `--index`.
4. Report the source path, physical PDF page, page label when available, match type and score, matched text, and short context.
5. Check that the located passage supports the manuscript claim before quoting or paraphrasing it.
6. Distinguish the physical PDF page from the printed citation page unless page calibration has been verified.

Default page wording:

```text
PDF page N; citation page not calibrated
```

## Commands

Search directly:

```bash
"$PYTHON" "$SCRIPT" search "exact or noisy quote" \
  --path "/path/to/file-or-directory" \
  --mode auto \
  --limit 10
```

Build and search an index:

```bash
"$PYTHON" "$SCRIPT" index \
  --path "/path/to/pdfs" \
  --index "/path/to/pdf-quote-index.sqlite3"

"$PYTHON" "$SCRIPT" search "quote" \
  --index "/path/to/pdf-quote-index.sqlite3" \
  --mode auto \
  --limit 10
```

## Match modes

| Mode | Behaviour |
|---|---|
| `auto` | Try exact, compact, punctuation-insensitive, then fuzzy matching; stop at the first successful tier |
| `exact` | Raw or Unicode-normalised substring |
| `compact` | Ignore whitespace differences |
| `punctuation` | Ignore whitespace, punctuation, and symbol differences |
| `fuzzy` | Use character-bigram filtering and sliding-window similarity |

## Constraints

- Prefer PyMuPDF extraction; use `pypdf` only as fallback.
- Image-only PDFs without a text layer require a separate OCR or MinerU step.
- Never invent printed citation pages from physical PDF indices.
- Adjacent-page windows may identify quotations split across pages; report that explicitly.
- Keep returned context short unless the user asks for a longer passage.

Implementation and normalisation details remain with the internal tool at `../../tools/pdf-quote-finder/reference.md`.
