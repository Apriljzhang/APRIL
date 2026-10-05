---
name: april-09-formatting
description: >-
  APRIL stage 09: manuscript formatting — dynamic target-journal length, TNR 12pt double,
  APA, two-line captions; DOCX/PDF export guidance.
---

# april-09-formatting

## Scope control (mandatory)

Read `../references/core/operating-contract.md` before acting. Format only the named document or elements; do not perform substantive rewriting or generate missing manuscript sections unless requested.

Read `../references/core/manuscript-contract.md` for the target journal, article type, language, word limit, and locked table/figure decisions.

## Length and formatting rules
- Determine article and abstract word limits from the target journal's current author instructions and the specified article type. Check whether the count includes the abstract, references, tables, or appendices.
- Do not impose a fixed APRIL word-count default. If no journal or limit is identified, ask for the target or establish a provisional scope with the user before treating any length as a requirement.
- Keep article length responsive to the journal's current requirements, article type, evidence, and user instructions. Do not cut necessary methods, results, or limitations merely to hit an unsupported generic target; explain the trade-off and ask how to proceed if the manuscript cannot fit.
- Abstract structure and length follow the journal's current requirements (see `../april-07-abstract/SKILL.md`).
- Typeface: Times New Roman **12 pt**, **double** spacing (or journal equivalent).
- Citations/refs: **APA** (latest edition the user names; default APA 7).
- Tables/figures: **two-line captions** (title line + note/legend line as needed).
- Margins/headers: follow journal template when provided; otherwise standard 1-inch.

## Checklist
1. Heading levels consistent; no orphan headings.
2. Number tables/figures in order of appearance; every one cited in text.
3. Caption style: Line 1 = Table/Figure N. Title. Line 2 = Note. …
4. In-text citations match reference list 1:1.
5. Check the correct journal word limits and count exclusions; report the measured count and any overage or ambiguity.
6. Export: DOCX for submission; PDF for sharing. Prefer user’s existing Office/Quarto pipeline.

## Paragraph rhythm and visual flow

- When the user requests paragraph-flow or prose-layout review, inspect length distribution by section and flag conspicuous runs of similarly sized paragraphs, including narrow bands such as 85–115 words. Paragraph length is not an APA compliance rule and no universal target should be imposed.
- Treat coherence and rhetorical function as the governing criteria. Recommend or apply splitting, merging, or reordering only when authorised and when it strengthens claim–support logic, evidence integration, or transitions; never pad prose or fragment a complete argument merely to manufacture variation.
- Check that quotations, tables, headings, and page breaks do not create isolated fragments, visually dense blocks, or misleading separation between a claim and its supporting evidence.

## Tools
If the user uses Office CLI patterns, keep formatting instructions journal-agnostic; do not invent vendor-specific macros unless they ask.

## Network figures
For network-analysis outputs:

- Define nodes, edges, signs, widths, colours, thresholds, and uncertainty/stability indicators in the caption or note.
- Use identical node placement, edge scaling, signs, and legends across comparison panels. Do not auto-scale each group network independently.
- Distinguish positive and negative edges with more than colour alone and use an accessible palette.
- Accompany network plots with edge, bridge, or NCT tables and accuracy/stability results; do not let the graph serve as the sole statistical evidence.

## JARS pre-submission gate
Before export, read `../references/reporting/reporting-router.md` and run the complete applicable pack. For Mixed, run all three design files; consider REC for every manuscript and apply its relevant items. Mark each item met, not met, not applicable, or unclear; record the manuscript location. Prefer official APA checklist PDFs when a journal requires formal JARS attestation.

## Genre calibration
Formatting rules are genre-dependent, but APRIL should enforce journal-article assumptions unless the user is working in another genre. Check `../references/genres/academic-genres.md` only when needed.

Journal-article default: prioritise the target journal's author guidelines over APRIL house defaults. Only switch to institution, sponsor, or publisher rules when the task is explicitly non-article.


---
**APRIL — Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
