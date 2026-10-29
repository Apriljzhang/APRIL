# April's standing research-manuscript rules

Apply these personal defaults to research manuscripts and manuscript-related figures, including tasks that do not explicitly invoke APRIL. Apply only the requested operation, sections and deliverables; a section-level request does not authorise creating a complete paper or editing other files. Professional emails and unrelated documents are outside this policy.

## Precedence and continuity

- Follow explicit task instructions and preserve verified evidence, locked decisions, genuine authorship and confidentiality. Surface conflicts with the target journal's current requirements or a blinded submission; follow explicit task-specific decisions rather than silently claiming both standards are satisfied.
- April's black text, left-aligned headings and italic qualitative-data quotation preferences override generic APA presentation defaults. These are house-style choices, not requirements attributed to APA.
- Retain existing APRIL British English, natural academic prose, claim-oriented paragraph development, varied paragraph rhythm and evidence-integrity guidance. Do not impose paragraph-length quotas or rewrite substantively during a formatting-only task.

## Presentation

- All manuscript text is black, including title/front matter, headings, captions, notes, table text, reference text, hyperlinks and figure labels. Set explicit black formatting where inherited themes would otherwise introduce colour.
- All manuscript headings, at every level, are left aligned. Use APA title case and the five-level hierarchy below, employing only as many levels as needed without skipping levels or imposing a three-level cap. Use distinct semantic Word heading styles/outline levels even where the all-left house preference makes Levels 1 and 2 look similar.
- Use Times New Roman 12 pt throughout the manuscript, including title, body, headings, table/figure numbers and titles, notes, table text and page numbers; double-space unless an applicable APA/journal exception or explicit task instruction changes spacing. Do not apply the tentative 16/14/12-point size ladder. Use APA title case for the manuscript title.
- Use Times New Roman 12 pt for all text inside figures, including axes, tick labels, legends, annotations and panel labels. Check the rendered/exported figure for font substitution. If an existing raster figure cannot be edited faithfully, report the limitation rather than claiming its font has been changed.
- Use APA-style minimalist three-line tables: a top horizontal rule, a rule below the column headings, and a bottom rule. Use no vertical borders or full grid, no coloured text or background shading, and black text/rules on white. Add horizontal rules only where necessary to clarify complex headings/totals or to follow explicit task/journal requirements; preserve accessible legibility. This is April's house style, not a claim that every APA table must contain exactly three rules.
- Format table/figure labels as a bold number above an italic title-case title, on separate lines. Keep numbering and in-text callouts consistent.
- Keep table/figure notes to the minimum needed for independent interpretation: omit repeated narrative and boilerplate, but retain necessary abbreviations, symbols, units, denominators, uncertainty/statistical indicators and attribution/licence details as applicable. Use notes only when needed; never strip essential information to meet an arbitrary word cap.
- Italicise direct quotations from interviews and other qualitative datasets, inline or block, while preserving exact wording, attribution, confidentiality, participant identifiers and the declared transcription/translation policy. Keep applicable APA quotation punctuation and source details; quotations of 40 or more words retain block formatting. Do not invent participant references or extend this italic rule automatically to quotations from published literature.

### Heading hierarchy

| Level | April's APA-based presentation |
|---|---|
| 1 | Left-aligned, bold, title case; text starts a new paragraph |
| 2 | Left-aligned, bold, title case; text starts a new paragraph |
| 3 | Left-aligned, bold italic, title case; text starts a new paragraph |
| 4 | Left-aligned paragraph with a 0.5-inch first-line indent; bold, title case, ending with a full stop; text continues on the same line |
| 5 | Left-aligned paragraph with a 0.5-inch first-line indent; bold italic, title case, ending with a full stop; text continues on the same line |

All levels remain 12 pt. Left alignment is compatible with the first-line indentation of run-in Levels 4 and 5. April's Level 1 left alignment overrides APA's centred default. Do not number headings, add blank lines for heading spacing or invent different sizes to distinguish levels; preserve a logical outline through semantic styles.

## Reporting and evidence

- Use APA 7 for citations, references and reporting unless the user specifies another edition or an explicit journal requirement applies.
- Select the appropriate complete APA Journal Article Reporting Standards (JARS) through APRIL's `../reporting/reporting-router.md`: Quant for quantitative work, Qual for qualitative work, and Mixed/MMARS plus both Quant and Qual for integrated mixed methods. Apply relevant design modules and consider relevant JARS-REC items. Use other design-specific standards when required.
- JARS checks reporting completeness; they do not prove study quality. For a limited task, check relevant items within scope. For a whole-manuscript reporting review or pre-submission export, check the complete applicable pack and record met, not met, not applicable or unclear, with manuscript locations or needed repairs.
- Never invent missing methods, sample details, ethics/consent, analyses, quotations or findings to fill a checklist. Flag missing evidence. Do not claim a JARS check merely because a checklist is linked.

Official baseline checklists: [JARS-Quant Table 1](https://apastyle.apa.org/jars/quant-table-1.pdf), [JARS-Qual Table 1](https://apastyle.apa.org/jars/qual-table-1.pdf), and [JARS-Mixed Table 1](https://apastyle.apa.org/jars/mixed-table-1.pdf). These baseline links do not replace applicable modules or full APRIL checklists.

## Structure and pagination

- A complete paper normally has Introduction, Literature Review, Methods, Findings or Results, Discussion, and Conclusion, in that order. Use Findings or Results as appropriate to the study. Preserve task-authorised or journal-required structural exceptions.
- Put contributions, implications, limitations and related interpretive subsections inside Discussion; do not create them as additional top-level sections by default.
- Group front matter together: title, verified author/byline and affiliation/contact/author-note details, abstract, keywords, and highlights only when requested or required. Do not invent missing details. Front matter may naturally span pages.
- Insert a real page break before Introduction. Keep the six main sections flowing normally unless a specific requirement calls for another break.
- After Conclusion, start References on a new page. Place appendices after References by default, following APA order, unless the user expressly requests another order.
- Each appendix starts on its own new page. Label a single appendix `Appendix`; label multiple appendices `Appendix A`, `Appendix B`, `Appendix C`, and so on, with informative titles when known.
- Use actual Word page breaks or paragraph page-break-before properties, never repeated blank paragraphs for pagination. Verify rendered page starts and avoid accidental blank pages.

- The sole permitted header content is an actual automatic `PAGE` field at the top right, in Times New Roman 12 pt and black. Include no running head, other header text, footer text, logos or decoration. Apply this consistently across document sections; do not invent unrequested numbering exceptions.

## Word identity, dates and editing time

- For identified Word manuscripts created in April's name, set the document-property creator/author (`dc:creator`) to `April Jiawei Zhang`, and `cp:lastModifiedBy` appropriately to `April Jiawei Zhang` when generating or editing on her behalf. This is file metadata; it does not authorise replacing actual coauthors, changing author order, inventing affiliations or deanonymising a blinded submission. For blinded copies, follow the submission's anonymisation requirements and flag this exception.
- For a genuinely new document, capture the actual timezone-aware instant when its creation begins, retain that instant throughout generation, and write it to `dcterms:created` in valid UTC/W3CDTF form. Set `dcterms:modified` to the actual save/update instant. Do not inherit stale template/epoch dates or substitute midnight, a guessed date, or a backdated value.
- When revising or exporting a continuation of an existing document, preserve its genuine original creation time and meaningful metadata. Update modified time for the actual revision. If creation metadata is missing or demonstrably invalid, report it and use a transparent repair; do not invent historical provenance or reset it merely because a new output filename is used.
- A genuinely new Word document starts `docProps/app.xml` `TotalTime` at `0` minutes. Existing files retain legitimate accumulated editing time. Never derive editing duration from wall-clock age or invent elapsed minutes. Automatic accumulation after creation depends on Microsoft Word/the editing application and cannot be guaranteed by file generation alone; disclose that limitation when relevant.
- Do not falsify filesystem creation/modification timestamps. Filesystem dates, OOXML document properties and Word's accumulated editing time are separate records.

## Delivery check

Within the authorised scope, verify actual formatting and page starts in rendered output, inspect DOCX core/app properties where a Word file is produced, and report unresolved font, evidence, reporting or metadata limitations. Follow the relevant document/PDF skill when those formats are created or edited. This policy does not itself authorise retroactive edits, publication or cross-device configuration changes.
