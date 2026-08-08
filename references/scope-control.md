# APRIL scope control

Apply this contract before every APRIL task, including when a stage skill is invoked directly.

## Core rule

Treat the user's explicit request as the output boundary. Manuscripts, data, references, variable descriptions, reviewer files, and prior-stage outputs provide context; their availability does not authorise work on every possible section or deliverable.

Before acting, identify internally:

- the requested operation: advise, analyse, draft, edit, format, review, or revise;
- the requested object: question, section, dataset, table, figure, file, or whole manuscript;
- the requested deliverables and any stated length or format;
- the active APRIL stage and the point at which the request is complete.

When scope is ambiguous, use the narrowest interpretation that still answers the request. Ask a concise question only when different interpretations would materially change the work and a safe narrow result would not be useful.

## Execution boundaries

- Produce the minimum complete deliverable requested. Optional outputs listed in a stage skill are a menu, not an automatic bundle.
- Do not draft, rewrite, analyse, format, or review neighbouring manuscript sections unless the user requests them.
- Do not run downstream APRIL stages merely because they are available. A handoff recommendation does not authorise execution of the next stage.
- Perform only prerequisites necessary for the requested deliverable. Keep incidental diagnostics or intermediate work subordinate to that deliverable.
- Do not create extra files, tables, figures, appendices, code, literature searches, or robustness analyses unless requested or analytically necessary. If analytically necessary, explain their role rather than expanding into unrelated outputs.
- Honour explicit limits such as “only,” “just,” “briefly,” named sections, named files, requested formats, or requested analytical models.
- After satisfying the requested deliverable and essential integrity caveats, stop. Offer a next step briefly instead of carrying it out.

Draft a complete manuscript or run the full APRIL pipeline only when the user explicitly requests a whole paper, complete manuscript, end-to-end workflow, or all relevant stages.

## Stage boundaries

| Stage | Default authorised output when invoked | Do not add without an explicit request |
|---|---|---|
| 01 Ideation | Requested scoping, RQs, hypotheses, or feasibility work | Literature review, Method, Results, or full proposal/manuscript |
| 02 Literature | Requested search, evidence matrix, synthesis, or literature section | Method, analysis, Discussion, or full manuscript |
| 03 Methodology | Requested design decision, critique, plan, diagram, or Method prose | Data analysis, fabricated results, or full manuscript |
| 04 Analysis | Requested analysis, diagnostics, tables/figures, Results/Findings, or bounded interpretation | Introduction, literature review, full Method, full Discussion, Conclusion, Abstract, or full manuscript |
| 05 Discussion | Requested interpretation or Discussion component based on locked findings | New analyses, other manuscript sections, or full manuscript |
| 06 Framing | Only the specifically named Introduction, Conclusion, Abstract, or subsection | The other framing sections or full manuscript |
| 08 Language | Revision of the supplied or named text/section | New arguments, evidence, sections, or manuscript-wide rewriting |
| 09 Formatting | Formatting of the named document or requested elements | Substantive rewriting or new manuscript content |
| 10 Review | Review findings in the requested scope | Silent rewriting or implementation of fixes |
| 11 Revision | Requested comment responses, edits, change log, or response letter | Unrelated manuscript overhaul or new analyses |

## Scope-preserving output

If missing information prevents completion, return only what remains useful within scope: a targeted question, a bounded plan, a code skeleton, marked placeholders, or a short blocker report. Do not compensate for missing evidence by generating additional manuscript sections.
