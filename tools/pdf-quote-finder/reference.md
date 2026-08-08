# APRIL PDF quote locator — implementation reference

Design distilled from [sabercomo/MEFinder](https://github.com/sabercomo/MEFinder).

## What this internal tool adopts

| MEFinder idea | Skill behavior |
|---|---|
| Local-first search | No embeddings / vector DB / LLM |
| Cascading modes | `auto`: exact → compact → punctuation → fuzzy |
| Text normalization | NFKC, quote/punct unify, casefold, hyphen stitch |
| Page units | One searchable unit per PDF page |
| Cross-page hits | Adjacent pages: last 900 + first 900 chars |
| Page honesty | PDF physical page ≠ citation page unless calibrated |

## What this internal tool deliberately omits

- Word/DOCX corpus indexing
- MinerU / vision API OCR pipelines
- Citation format builders (GB/T, APA, …)
- Desktop/Web UI and page-calibration library
- Bibliographic metadata enrichment

Those belong in the full MEFinder app. This internal APRIL component is a focused local locator.

## Normalization details

1. Unicode NFKC
2. Smart quotes → ASCII; CJK punct → ASCII equivalents
3. Collapse whitespace; lowercase
4. Join `word-\\nword` style hyphenation for Latin text
5. `compact_text`: remove all whitespace
6. `plain_text`: remove whitespace + Unicode punctuation/symbols

## Fuzzy matching

1. Build char bigrams over `plain_text`
2. Rank units by bigram overlap; take top ~700
3. Sliding window + `difflib.SequenceMatcher`
4. Keep ratio ≥ 0.58; score capped at 0.9

## Page display language

Always distinguish:

- `pdf_page_*_1based` — reader page number (what Preview/Acrobat show as page N)
- `pdf_page_*_label` — PDF Page Label if present (roman numerals, etc.)
- citation / printed page — **not produced** unless a future calibration layer is added

Default string:

```text
PDF page 48; citation page not calibrated
```

## Suggested index location

Per project:

```text
<data-dir>/pdf-quote-index.sqlite3
```

Or under the corpus folder:

```text
/path/to/pdfs/.pdf-quote-index.sqlite3
```

Rebuild the index after adding/replacing PDFs.
