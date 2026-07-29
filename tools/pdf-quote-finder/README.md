# pdf-quote-finder

Cursor Agent Skill that locates exact sentences, fragments, or slightly noisy quotes in **local PDF files** — inspired by [MEFinder](https://github.com/sabercomo/MEFinder).

No embeddings, vector DB, or LLM. Cascading local match modes: exact → compact → punctuation → fuzzy.

## Install into Cursor

```bash
git clone https://github.com/Apriljzhang/pdf-quote-finder.git ~/.cursor/skills/pdf-quote-finder
cd ~/.cursor/skills/pdf-quote-finder
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

Or symlink from a checkout elsewhere into `~/.cursor/skills/pdf-quote-finder`.

## Usage

```bash
PYTHON="$HOME/.cursor/skills/pdf-quote-finder/.venv/bin/python"
SCRIPT="$HOME/.cursor/skills/pdf-quote-finder/scripts/pdf_quote_finder.py"

# One-off search over a PDF or directory
"$PYTHON" "$SCRIPT" search "your quote" --path "/path/to/pdfs"

# Index once, search many times
"$PYTHON" "$SCRIPT" index --path "/path/to/pdfs" --index "/tmp/pdf-quote-index.sqlite3"
"$PYTHON" "$SCRIPT" search "your quote" --index "/tmp/pdf-quote-index.sqlite3"
```

Match modes: `auto` (default), `exact`, `compact`, `punctuation`, `fuzzy`.

## Notes

- Prefers PyMuPDF; falls back to `pypdf`.
- Scanned / image-only PDFs with no text layer will not match (no remote OCR).
- PDF physical page ≠ printed citation page unless you calibrate separately.

See `SKILL.md` for agent instructions and `reference.md` for design details.
