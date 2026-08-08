# APRIL local PDF quote search

Use APRIL's integrated local script to find exact sentences, fragments, or slightly noisy quotations in PDFs and pin them to physical PDF pages. Search and extraction remain on disk; the script does not use embeddings, a vector database, or an LLM API.

## Contents

1. When to use
2. Interpreter
3. Workflow
4. Commands
5. Match modes
6. Constraints
7. Implementation design
8. Normalisation and fuzzy matching
9. Index placement

## When to use

- Locate the source PDF for a remembered sentence or fragment.
- Recover a physical PDF page for citation verification.
- Search through spacing, punctuation, hyphenation, or minor OCR/copy noise.
- Verify a quotation before using it in a literature review or Discussion.

Do not use quotation search as a substitute for reading the source, checking whether it supports the surrounding claim, or verifying bibliographic metadata.

## Interpreter

Run the internal APRIL script with APRIL's shared environment:

```bash
APRIL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/APRIL"
PYTHON="$APRIL_ROOT/.venv/bin/python"
SCRIPT="$APRIL_ROOT/scripts/pdf_quote_search.py"
REQUIREMENTS="$APRIL_ROOT/scripts/pdf-quote-search-requirements.txt"
```

If the environment is missing:

```bash
cd "$APRIL_ROOT"
uv venv .venv
uv pip install --python .venv/bin/python -r "$REQUIREMENTS"
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

## Implementation design

The implementation is distilled from [sabercomo/MEFinder](https://github.com/sabercomo/MEFinder) and narrowed to APRIL's evidence-verification workflow.

| Adopted idea | APRIL behaviour |
|---|---|
| Local-first search | No embeddings, vector database, or LLM |
| Cascading modes | `auto`: exact → compact → punctuation → fuzzy |
| Text normalisation | NFKC, quote/punctuation unification, case-folding, and line-break hyphen repair |
| Page units | One searchable unit per physical PDF page |
| Cross-page hits | Search adjacent-page boundary windows |
| Page honesty | Keep physical PDF page, PDF page label, and printed citation page distinct |

APRIL deliberately omits Word/DOCX corpus indexing, OCR/vision pipelines, citation-format builders, a graphical interface, automatic page calibration, and bibliographic enrichment. Route those needs to the appropriate APRIL or document workflow instead of expanding this script.

## Normalisation and fuzzy matching

The script:

1. applies Unicode NFKC normalisation;
2. unifies smart quotes and common CJK punctuation;
3. collapses whitespace, applies case-folding, and repairs Latin line-break hyphenation;
4. derives compact text without whitespace and plain text without whitespace, punctuation, or symbols;
5. ranks fuzzy candidates using character-bigram overlap;
6. applies a sliding-window `difflib.SequenceMatcher` comparison to the strongest candidates;
7. retains fuzzy ratios of at least 0.58 and caps fuzzy scores at 0.9.

Search output distinguishes:

- `pdf_page_*_1based`: the physical reader page number shown by Preview or Acrobat;
- `pdf_page_*_label`: a PDF page label when present, including roman numerals;
- printed citation page: unavailable unless separately calibrated and verified.

## Index placement

Store a reusable SQLite index beside the project data or PDF corpus, for example:

```text
<data-directory>/pdf-quote-index.sqlite3
/path/to/pdfs/.pdf-quote-index.sqlite3
```

Rebuild the index after PDFs are added or replaced.
