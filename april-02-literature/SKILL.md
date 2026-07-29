---
name: april-02-literature
description: >-
  APRIL stage 02: literature review — search, triage, synthesis, citation integrity,
  Zotero library search (PapersGPT/pz), and local PDF quote pinning (pdf-quote-finder).
---

# april-02-literature

## Goal
Build a credible, synthesised evidence base. Prefer the user’s local library and PDFs when available.

## Workflow

1. **Scope the search** — databases/years/inclusion–exclusion; record a search log.
2. **Collect** — public sources and/or local Zotero (see Zotero section).
3. **Triage** — living matrix: claim → source → quality/role (support, conflict, method).
4. **Synthesise by debate/theme**, not paper-by-paper dumping.
5. **Pin quotes** from local PDFs when page-accurate citation is needed (see PDF quotes).
6. **Integrity gate** — no invented DOIs/pages; flag unverified items.
7. Hand matrix to methodology or drafting stages.

## Zotero (APRIL workflow)

When the user has a local Zotero library and PapersGPT CLI (`pz` / `pgz`) is available:

```bash
# one-time
pz init
# or custom storage
pz init "/path/to/Zotero/storage"

pz search "your query"
pz stop   # when finished
```

Install if missing: `npm install -g papersgpt-for-zotero` (see https://github.com/papersgpt/papersgpt-for-zotero).

Use Zotero search for discovery inside the user’s collection only — not as a substitute for verifying citations.

## Local PDF quote pinning (APRIL tool)

```bash
PYTHON="$HOME/.cursor/skills/april/tools/pdf-quote-finder/.venv/bin/python"
SCRIPT="$HOME/.cursor/skills/april/tools/pdf-quote-finder/scripts/pdf_quote_finder.py"

"$PYTHON" "$SCRIPT" search "exact or noisy quote" --path "/path/to/pdfs"
```

If the venv is missing, create it from `tools/pdf-quote-finder/requirements.txt` with `uv`.

Match modes: auto (default), exact, compact, punctuation, fuzzy. No embeddings/LLM.

## Outputs
Search log; inclusion table; synthesis matrix; quote pins (file + page); citation risk list.

## Prompt aids
See `references/prompt-bank.md`.

## JARS (literature)
- Meet Introduction “relevant scholarship” expectations in `../references/jars/` (Quant/Qual as applicable).
- Apply `../references/jars/jars-rec.md` citation praxis: diversify sources, avoid unread “classics,” credit specialty and local-language work when relevant.


---
**APRIL — Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
