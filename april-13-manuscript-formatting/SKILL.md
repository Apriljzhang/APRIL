---
name: april-13-manuscript-formatting
description: >-
  APRIL stage 13 Manuscript Formatting: audit a research manuscript against April's
  standing house rules, or fix presentation and honest Word metadata when requested.
  Use for manuscript formatting checks or fixes; preserve content and scientific
  evidence. Reader-comprehension comments belong to APRIL Fresh Eyes.
---

# APRIL Manuscript Formatting

## Scope and mode

Read `../references/core/operating-contract.md`, then [the standing manuscript rules](../references/core/manuscript-house-style.md), the single source of truth. Use `../references/core/manuscript-contract.md` for known target requirements and locked decisions. Preserve British English and existing prose preferences without applying language edits.

Read [the concise APA presentation reference](references/apa-presentation.md) to distinguish official APA 7 baseline rules, JARS reporting requirements and April's house overrides. Use the chosen uniform 12-point Times New Roman and APA five-level hierarchy as needed, with the policy's left alignment; do not infer a 16/14/12-point ladder or a three-level cap.

- **Check only** is the default for an audit, check, or unspecified invocation: report located issues and make no document changes.
- **Fix** applies when the user asks to format, correct, or fix presentation. Make only authorised formatting/metadata corrections in a separate copy by default; follow an explicit in-place request. Do not ask again when permission to fix is already clear.
- This skill's creation or availability does not authorise processing any manuscript. Never run Fresh Eyes automatically. If both are requested, keep the outputs and purposes distinct.

Use stage 09 when the task is primarily interpreting journal submission specifications, word limits or caption requirements; use this stage for the standing-rule audit and controlled document fixes. Honour explicitly selected stages. Surface conflicts between house rules, journal requirements and blinded submissions; do not silently resolve a consequential conflict against the user's task instructions.

## Audit and controlled correction

1. Identify the requested file/elements, mode and target requirements. Inspect the actual document, including relevant styles, direct formatting, sections, headers/footers, fields, tables, figures and core/app metadata; a style name alone does not prove rendered compliance.
2. Check the applicable standing rules: black text; left-aligned heading hierarchy; Times New Roman figure text; italic qualitative-data quotations; front matter and section placement; real page breaks; automatic top-right page numbers as the only header content; monochrome minimalist APA tables and minimum necessary table/figure notes; and truthful identity, creation/modification and editing-time properties. Read the linked policy for exact requirements rather than recreating a competing checklist here.
3. Preserve wording, meaning, data, citation/reference text, quotations, genuine coauthors, field instructions, links, comments and tracked changes. Do not accept/reject revisions, flatten citation/PAGE/REF fields, invent missing metadata, or replace genuine creation history. Match field results and manuscript text before/after while allowing an automatically recalculated page-number display.
4. Formatting-only work does not authorise restructuring substantive text or moving interpretive claims between sections. Flag missing sections, misplaced content and JARS reporting gaps for the author; never invent content to satisfy them. For an authorised complete reporting/pre-submission check, follow `../references/reporting/reporting-router.md` and its applicable full packs; distinguish reporting gaps from presentation defects.
5. Change figure fonts only when an editable source supports a faithful export. Preserve plotted data, scales, labels and scientific encodings; do not silently redraw a scientific figure or substitute an approximation. Flag inaccessible figure sources or fonts.

## Journal-required ancillary matter

Within the requested formatting/submission scope, check the current official target-journal author guidelines, relevant article type and blinded-submission instructions when the journal is known. Record required ancillary items and their required locations: declarations, funding, conflicts of interest, data availability, ethics/consent and other applicable author information. These are permitted journal-required additions outside the six main scholarly sections, not a reason to restructure the research argument.

In check-only mode, flag missing or misplaced items. In authorised fix mode, add/place required items only from verified source facts and the user's instructions. Never assume no funding, no conflicts, consent or ethical approval, invent identifiers, or expose identifying information in a blinded file. Query missing facts or clearly flag what remains unresolved. Preserve existing truthful declarations. Journal-required placement governs these ancillary items; retain house style elsewhere and surface material conflicts.

For verified ethics approval and study timing, apply the policy's concise Methods-sentence and duration/design presentation preference. Do not insert a generic approval assertion, invent a study duration or use formatting to conceal a material unresolved contradiction.

If the journal is unknown, mark journal-specific compliance unverified and ask for the target only when it is needed to complete the requested outcome. For an authorised batch, check each paper's own target and supported declarations separately; do not carry another paper's funding, ethics or conflict statements across.

## Word document properties

Audit the actual DOCX `docProps/core.xml` and `docProps/app.xml`, not merely the filename or Finder dates. Include this audit in the formatting report and, in fix mode, verify the saved properties again:

- **Identity:** for identified manuscripts created in April's name, `dc:creator` is `April Jiawei Zhang`; set `cp:lastModifiedBy` truthfully for an edit performed on her behalf. These file properties do not authorise changing genuine coauthors/bylines. Preserve blinded-output anonymisation and report that exception rather than deanonymising the copy.
- **Dates:** a genuinely new file uses the actual timezone-aware instant creation begins, encoded validly in `dcterms:created`, and the actual save/update instant in `dcterms:modified`. Preserve the genuine original creation instant for revisions/continuations, even with a new filename. Flag inherited template epochs, missing/invalid dates or uncertain provenance; do not guess historical dates, backdate files or silently reset creation history.
- **Editing time:** initialise a genuinely new document's `TotalTime` to `0` minutes and preserve legitimate accumulated values on existing files. Never invent elapsed editing minutes or calculate them from file age. Subsequent automatic accumulation depends on Word/the editing application; generation alone cannot guarantee tracking.
- **Separate records:** filesystem birth/modification times are distinct from Word properties and editing time. Do not falsify them. Report unresolved property limits and the verified saved values/status within scope.

## Document workflow and verification

Use the available Word/document skill and its existing tools for DOCX operations; use the PDF skill when relevant. Preserve the source, comments, pending revisions and package parts. Prefer surgical edits over a conversion that loses unsupported features.

- Verify structure as well as appearance: page-break properties; `PAGE` field instructions, placement and font; table borders/shading; applied text colours/fonts; quote styling; and core/app properties. Inspect all relevant sections, including first/even-page header variants.
- Render the corrected copy and inspect every page for actual page starts, blank pages, heading alignment, page numbers, tables and figure labels. Do not claim a font was used merely because it was requested in code. Check that changed formatting did not alter substantive text, data, citations, fields, comments or revision markup.
- If tools, rendering, fonts, editable figures or metadata provenance prevent verification/correction, disclose the specific limit. Complete independent checks and do not label the whole document compliant.

## Deliverable

For check-only mode, give a concise issue list with section/paragraph or verified page location, observed defect, applicable rule and proposed correction. For fix mode, return the corrected copy with a short account of fixes, preservation/verification and unresolved items. Do not create a rewritten manuscript, extra section or Fresh Eyes review unless requested.

---
**APRIL — Academic Research Skills by April**
