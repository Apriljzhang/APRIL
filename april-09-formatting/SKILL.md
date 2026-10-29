---
name: april-09-formatting
description: >-
  APRIL stage 09 Manuscript Formatting: prepare, audit or fix manuscripts with
  April's house rules, author-information consistency and honest Word properties,
  then adapt a separate copy to current journal requirements when in scope.
  Preserve content and scientific evidence; first-reader comments use Fresh Eyes.
---

# APRIL Manuscript Formatting

## Scope and mode

Read `../references/core/operating-contract.md`, then [the standing manuscript rules](../references/core/manuscript-house-style.md), the single source of truth. Use `../references/core/manuscript-contract.md` for known target requirements and locked decisions. Preserve British English and existing prose preferences without applying language edits.

Read [the concise APA presentation reference](references/apa-presentation.md) to distinguish official APA 7 baseline rules, JARS reporting requirements and April's house overrides. Use the chosen uniform 12-point Times New Roman and APA five-level hierarchy as needed, with the policy's left alignment; do not infer a 16/14/12-point ladder or a three-level cap.

- **Check only** is the default for an audit, check, or unspecified invocation: report located issues and make no document changes.
- **Fix** applies when the user asks to format, correct, or fix presentation. Make only authorised formatting/metadata corrections in a separate copy by default; follow an explicit in-place request. Do not ask again when permission to fix is already clear.
- This skill's creation or availability does not authorise processing any manuscript. Never run Fresh Eyes automatically. If both are requested, keep the outputs and purposes distinct.

This is APRIL's single Formatting sub-skill: it combines the existing journal/APA/length/export guidance with today's standing-rule audit, controlled fixes, author-information consistency and Word-property checks. Do not route to a second Formatting skill.

## House preparation and journal adaptation

For manuscript preparation, apply the standing house rules first. Then, when a target journal/submission version is in scope, check the current official journal instructions and adapt a separate journal-ready copy, retaining the house-prepared copy. In audit mode report the differences without changing files; in fix mode produce the requested copy/copies. A narrow house-only or element-level task remains narrow.

Journal-specific required presentation governs the journal-adapted version, including requirements that alter house numbering, page breaks, alignment or ancillary placement. These adaptations do not permanently change the global house policy. Report the adaptations; do not repeatedly seek permission for journal formatting already authorised by this workflow. Resolve factual gaps separately rather than inventing declarations.

## Audit and controlled correction

1. Identify the requested file/elements, mode and target requirements. Inspect the actual document, including relevant styles, direct formatting, sections, headers/footers, fields, tables, figures and core/app metadata; a style name alone does not prove rendered compliance.
2. Check the applicable standing rules: black text; left paragraph alignment throughout, including title/authors/front matter and all table text, with only the top-right page number excepted; the semantic, hierarchically numbered heading structure; Times New Roman figure text; italic qualitative-data quotations; front matter and section placement; real page breaks; automatic top-right page numbers as the only header content; monochrome minimalist APA tables and minimum necessary table/figure notes; and truthful identity, creation/modification and editing-time properties. Preserve meaningful indents and numeric precision; flag a scientific-figure alignment conflict instead of destructively repositioning labels. Read the linked policy for exact requirements rather than recreating a competing checklist here.
3. Preserve wording, meaning, data, citation/reference text, quotations, genuine coauthors, field instructions, links, comments and tracked changes. Do not accept/reject revisions, flatten citation/PAGE/REF fields, invent missing metadata, or replace genuine creation history. Match field results and manuscript text before/after while allowing an automatically recalculated page-number display.
4. Formatting-only work does not authorise restructuring substantive text or moving interpretive claims between sections. Flag missing sections, misplaced content and JARS reporting gaps for the author; never invent content to satisfy them. For an authorised complete reporting/pre-submission check, follow `../references/reporting/reporting-router.md` and its applicable full packs; distinguish reporting gaps from presentation defects.
5. Change figure fonts only when an editable source supports a faithful export. Preserve plotted data, scales, labels and scientific encodings; do not silently redraw a scientific figure or substitute an approximation. Flag inaccessible figure sources or fonts.

For the Discussion structure check, use [stage 05's RQ-ordered organisation](../april-05-discussion/SKILL.md). Flag substantive order/placement issues for the author; this check does not authorise rewriting the Discussion or generating missing implications.

## Journal-required ancillary matter

Within the requested formatting/submission scope, check the current official target-journal author guidelines, relevant article type and blinded-submission instructions when the journal is known. Record required ancillary items and their required locations: declarations, funding, conflicts of interest, data availability, ethics/consent and other applicable author information. These are permitted journal-required additions outside the six main scholarly sections, not a reason to restructure the research argument.

In check-only mode, flag missing or misplaced items. In authorised fix mode, add/place required items only from verified source facts and the user's instructions. Never assume no funding, no conflicts, consent or ethical approval, invent identifiers, or expose identifying information in a blinded file. Query missing facts or clearly flag what remains unresolved. Preserve existing truthful declarations. Journal-required placement governs these ancillary items; retain house style elsewhere and surface material conflicts.

For manuscript-production AI declarations, check the current official journal disclosure requirements within journal adaptation and preserve required factual disclosures. Use [Fresh Eyes' unintended-AI-mention check](../april-13-fresh-eyes/SKILL.md#what-deserves-a-comment) to classify accidental drafting/tool commentary and remove clear residue only in an authorised revision mode with a traceable record. Preserve ambiguous/intentional or required declarations pending a specific question; never conceal substantive AI methods or claim no AI use without evidence.

For verified ethics approval and study timing, apply the [shared ethics-presentation rule](../references/core/manuscript-house-style.md#structure-and-pagination): place the single verified approval sentence after recruitment/context in Methods' Participants and Context subsection, without a standalone Ethics heading in the house copy. Keep unresolved identifiers as yellow queries and preserve necessary consent/confidentiality facts; journal adaptations follow their required placement. Do not insert a generic approval assertion, invent a study duration or use formatting to conceal a material unresolved contradiction.

If the journal is unknown, mark journal-specific compliance unverified and ask for the target only when it is needed to complete the requested outcome. For an authorised batch, check each paper's own target and supported declarations separately; do not carry another paper's funding, ethics or conflict statements across.

Apply the [working-draft placeholder/query rule](../references/core/manuscript-house-style.md#working-draft-placeholders-and-author-questions): use actual yellow Word text highlighting with black font only on genuine unresolved placeholders/author-input queries, not ordinary brackets, citations or statistical notation. Preserve unknowns and surface concise located questions through an available user-input tool or chat; do not invent facts or a popup capability. Verify the highlight property and rendered draft appearance.

Check the [shared RQ-label rule](../references/core/manuscript-house-style.md#research-question-labels): listed questions use bold `RQ1:`, `RQ2:`, etc., with normal question text by default, preserving wording/order and consistent cross-references. Verify label-run bold formatting rather than making whole questions bold or treating RQs as section headings.

## Author-information consistency

Audit the visible author block separately from DOCX properties. For the user's identified manuscripts, compare the intended author's confirmed name, affiliation, preferred email, ORCID and verified institutional/office postal address across the supplied title page, author note, correspondence and submission fields within scope. Read the private profile at `$CODEX_HOME/manuscript-author-profile.md` (or `~/.codex/manuscript-author-profile.md` when unset); if unavailable, use user-provided/verified sources and flag missing fields. Never infer a personal office from a school's general contact footer or invent a room/postcode.

Normalise only the intended author's supported details. Preserve all coauthors, author order, contributions, existing corresponding-author choices and genuine study-specific affiliation requirements. A preferred email does not make that person the corresponding author. Do not insert the user into unrelated papers or alter names in published reference entries. Apply journal-required placement, and keep author details out of blinded copies. Keep private profiles/contact dossiers outside public skill repositories; public instructions contain the checking workflow, not personal address data.

Audit the [shared author-block layout](../references/core/manuscript-house-style.md#author-block-layout): comma-separated actual byline with superscript affiliation markers and the actual correspondence asterisk, mapped affiliation lines, then separate corresponding-author, `Email:`, `Address:` and `ORCID:` lines. Use the shortened labels and the correct owners' verified details; preserve the paper-specific author list/order/roles, unknown-field queries, journal adaptation and blinding.

## Word document properties

Audit the actual DOCX `docProps/core.xml` and `docProps/app.xml`, not merely the filename or Finder dates. Include this audit in the formatting report and, in fix mode, verify the saved properties again:

- **Identity:** for identified manuscripts created in April's name, `dc:creator` is `April Jiawei Zhang`; set `cp:lastModifiedBy` truthfully for an edit performed on her behalf. These file properties do not authorise changing genuine coauthors/bylines. Preserve blinded-output anonymisation and report that exception rather than deanonymising the copy.
- **Dates:** a genuinely new file uses the actual timezone-aware instant creation begins, encoded validly in `dcterms:created`, and the actual save/update instant in `dcterms:modified`. Preserve the genuine original creation instant for revisions/continuations, even with a new filename. Flag inherited template epochs, missing/invalid dates or uncertain provenance; do not guess historical dates, backdate files or silently reset creation history.
- **Editing time:** initialise a genuinely new document's `TotalTime` to `0` minutes and preserve legitimate accumulated values on existing files. Never invent elapsed editing minutes or calculate them from file age. Subsequent automatic accumulation depends on Word/the editing application; generation alone cannot guarantee tracking.
- **Separate records:** filesystem birth/modification times are distinct from Word properties and editing time. Do not falsify them. Report unresolved property limits and the verified saved values/status within scope.

## Document workflow and verification

Use the available Word/document skill and its existing tools for DOCX operations; use the PDF skill when relevant. Preserve the source, comments, pending revisions and package parts. Prefer surgical edits over a conversion that loses unsupported features.

- Verify structure as well as appearance: effective paragraph alignment across title/byline/author information, other front matter, body, tables, captions, notes, references and appendices; the page-number exception and preserved indents; multilevel heading numbering linked to styles starting at `1. Introduction`, unnumbered title/authors/Abstract/Keywords/Highlights, no skipped/doubled section numbers, numbering glyphs matching heading bold/bold-italic/font/size/colour through effective `word/numbering.xml` level/override run properties as well as text runs, and rendered/cross-reference agreement; section numbering must not silently change the independent `PAGE` sequence; page-break properties; `PAGE` field instructions, placement and font; table borders/shading; applied text colours/fonts; quote styling; and core/app properties. Inspect all relevant sections, including first/even-page header variants.
- Render the corrected copy and inspect every page for actual page starts, blank pages, heading alignment, page numbers, tables and figure labels. Do not claim a font was used merely because it was requested in code. Check that changed formatting did not alter substantive text, data, citations, fields, comments or revision markup.
- If tools, rendering, fonts, editable figures or metadata provenance prevent verification/correction, disclose the specific limit. Complete independent checks and do not label the whole document compliant.

## Journal length, reporting and specialised checks

- Determine article/abstract limits and count exclusions from the current official journal instructions and article type; report the measured count and any overage/ambiguity. APRIL has no fixed word-count default. An unknown target does not block house preparation; do not treat a provisional count as a journal requirement. Read `../april-07-abstract/SKILL.md` for an authorised abstract task.
- Do not cut necessary methods/results/limitations to hit an unsupported target. If the evidence cannot fit the actual limit, explain the trade-off and seek the needed content decision rather than silently changing substance.
- Check numbering and in-text callouts for tables/figures and citation/reference correspondence within scope. Use the shared caption policy and `references/apa-presentation.md`; notes are optional when unnecessary. Prefer the user's existing Office/Quarto pipeline; DOCX and PDF outputs follow the requested deliverable. Do not invent vendor-specific macros.
- When paragraph-flow review is requested, judge coherence and rhetorical function; flag conspicuous uniformity without imposing word bands, padding or fragmenting prose. Split/merge/reorder text only when substantive editing is authorised. Check visual separation of headings, quotations, tables and claims.
- For network figures, preserve node placement, edge scaling, signs and legends across comparisons; define relevant encodings and uncertainty/stability information. Do not independently rescale panels or silently recast scientific data. Flag missing supporting edge/bridge/comparison or stability reporting rather than run unrequested analyses. Use accessible encodings beyond colour alone.
- Before whole-manuscript pre-submission export, read `../references/reporting/reporting-router.md` and run the complete applicable JARS pack (all three design files for Mixed; relevant Quant modules and REC items). Record met/not met/not applicable/unclear with locations. Prefer official APA checklist PDFs for formal attestation. Missing reporting is an author flag, not permission to invent content.
- Retain APRIL's journal-article core. For an explicitly different genre, consult `../references/genres/academic-genres.md` only as needed.

Before saving a Word manuscript output, apply the [shared filename convention](../references/core/manuscript-house-style.md#manuscript-filenames-and-output-separation): `Manuscript-with authors-[2–3 topic keywords]-YYYYMMDD.docx`, with a literal version marker and the output-creation date in UTC+8. Delimiter hyphens have no adjacent spaces; spaces inside the marker/topic remain. Use an accurate blinded marker for anonymous copies, stage folders for formatted/commented/revised/journal-adapted versions and collision checks that preserve originals. Validate this separately from genuine DOCX metadata dates; do not bulk rename unrelated existing files.

## Deliverable

For check-only mode, give a concise issue list with section/paragraph or verified page location, observed defect, applicable rule and proposed correction. For fix mode, return the corrected copy with a short account of fixes, preservation/verification and unresolved items. Do not create a rewritten manuscript, extra section or Fresh Eyes review unless requested.

---
**APRIL — Academic Research Skills by April**
