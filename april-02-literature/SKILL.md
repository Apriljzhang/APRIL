---
name: april-02-literature
description: >-
  APRIL stage 02: literature review — search, triage, synthesis, citation integrity,
  Zotero library search (PapersGPT/pz), and integrated local PDF quotation search
  with physical-page pinning.
---

# april-02-literature

## Scope control (mandatory)

Read `../references/core/operating-contract.md` before acting. Search, synthesise, or draft only within the requested literature scope; do not continue into other manuscript sections.

Preserve prior decisions through `../references/core/manuscript-contract.md` and apply `../references/evidence/evidence-integrity.md` to every search, synthesis, citation, and quotation task.

## Goal
Build a credible, synthesised evidence base. Prefer the user’s local library and PDFs when available.

## Workflow

1. **Scope the search** — databases/years/inclusion–exclusion; record a search log.
2. **Collect** — public sources and/or local Zotero (see Zotero section).
3. **Triage** — living matrix: claim → source → quality/role (support, conflict, method).
4. **Synthesise by debate/theme**, not paper-by-paper dumping. When developing the empirical research story, read `../references/rhetoric/empirical-storytelling.md` and organise the evidence as established account → tension or scope limit → complementary/competing account → unresolved discriminating question. Do not manufacture a debate the sources do not support.
5. **Pin quotes** from local PDFs when page-accurate citation is needed. Read `../references/evidence/pdf-quote-search.md` before running APRIL's integrated locator.
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

Read `../references/evidence/pdf-quote-search.md` for the full workflow, match modes, output fields, and page-number integrity rules. This capability is part of APRIL Literature; do not invoke or require a separate PDF quote-finder skill.

```bash
APRIL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/APRIL"
PYTHON="$APRIL_ROOT/.venv/bin/python"
SCRIPT="$APRIL_ROOT/scripts/pdf_quote_search.py"
REQUIREMENTS="$APRIL_ROOT/scripts/pdf-quote-search-requirements.txt"

"$PYTHON" "$SCRIPT" search "exact or noisy quote" --path "/path/to/pdfs"
```

If the environment is missing, create `$APRIL_ROOT/.venv` from `$REQUIREMENTS` with `uv` as specified in the shared evidence reference.

Match modes: auto (default), exact, compact, punctuation, fuzzy. No embeddings/LLM.

## Outputs
Search log; inclusion table; synthesis matrix; quote pins (file + page); citation risk list.

## Genre calibration
Keep the literature workflow article-oriented by default. Use `../references/genres/academic-genres.md` only for light genre adjustments when needed.

For journal articles, compress toward debate, gap, and contribution. Only expand the scaffolding when the user explicitly needs a non-article genre.

## Prompt aids
See `references/prompt-bank.md`.

## JARS (literature)
- Read `../references/reporting/reporting-router.md`, then use the Introduction and relevant-scholarship items in the applicable complete Quant, Qual, or Mixed checklist.
- Apply `../references/reporting/jars-rec.md` citation praxis: diversify sources, avoid unread “classics,” credit specialty and local-language work when relevant.


---
**APRIL — Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
