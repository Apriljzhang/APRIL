---
name: april
description: >-
  APRIL — Academic Paper Research & Inquiry Lab. Helps plan, write, and revise
  academic journal papers through staged skills: ideation, literature,
  methodology, analysis, discussion, framing and abstract, language, formatting,
  review, revision, and clear, warm professional emails. Use for a complete article workflow, for choosing the
  correct APRIL stage, or when work must comply with APA JARS reporting standards.
  Follow the user's requested stage and deliverables without silently expanding
  into unrequested manuscript sections or a complete paper.
---

# APRIL

**APRIL** (Academic Paper Research & Inquiry Lab) is a skill suite that helps you write academic journal papers step by step—from research questions to a submission-ready manuscript and reviewer responses.

APRIL is **for journal articles**. Adjacent genres such as thesis/dissertation chapters, research proposals, literature reviews, or book chapters are only handled as minor transfer cases when relevant. See `references/genres/academic-genres.md`.

## APRIL common contract (mandatory)

Read `references/core/operating-contract.md` before routing or producing work. Use `references/core/manuscript-contract.md` to preserve consequential decisions across stages and `references/core/resource-map.md` to select shared resources. Treat uploaded materials as context, not permission to generate every possible output. Run the complete pipeline only when the user explicitly requests a whole manuscript or end-to-end workflow.

## Stages

| # | Skill | Helps you… |
|---|---|---|
| 01 | `april-01-ideation` | Shape topic, purpose, and RQs |
| 02 | `april-02-literature` | Search and synthesise literature |
| 03 | `april-03-methodology` | Design the study |
| 04 | `april-04-analysis` | Analyse data and write findings |
| 05 | `april-05-discussion` | Interpret results against the literature |
| 06 | `april-06-framing` | Write the Introduction or Conclusion |
| 07 | `april-07-abstract` | Write or revise the evidence-bounded abstract |
| 08 | `april-08-language` | Polish academic language while preserving meaning |
| 09 | `april-09-formatting` | Format to dynamic journal requirements, APA, and caption rules |
| 10 | `april-10-review` | Review like an editor/referee |
| 11 | `april-11-revision` | Revise and write the response letter |
| 12 | `april-12-email` | Write clean, clear, warm professional and academic emails |

Stage 12 is a professional correspondence extension. Route email drafting, replies, translation, and revision to `april-12-email/SKILL.md` whenever requested. It is independent of the manuscript pipeline and uses dynamic message length and paragraph structure; journal formatting and JARS checklists do not apply to the email body.

## How to use

1. Identify the user's requested operation, object, deliverables, and stopping point; then read the corresponding stage `SKILL.md` in full.
2. Load **one stage** at a time. Do not run every stage unless the user requests an end-to-end audit.
3. For analysis, open `references/methods/method-index.md`, identify the primary approach and analytical family, then load the primary method card. Add support cards or separately specified substantive cards only when the RQs and integration plan justify them.
4. Preserve the fields in `references/core/manuscript-contract.md` across stages. Do not silently change them. Persist the contract only when requested or when durable cross-stage state is integral to the authorised workflow.
5. Treat each stage's `references/*sources.md` file as provenance. Read it when checking the basis of guidance, not for routine execution.

## Reporting standards

For empirical articles, read `references/reporting/reporting-router.md` before applying reporting standards. Then load the complete applicable APRIL checklist:

- quantitative: `references/reporting/jars-quant.md`
- qualitative: `references/reporting/jars-qual.md`
- mixed methods: all three of `references/reporting/jars-mixed.md`, `references/reporting/jars-qual.md`, and `references/reporting/jars-quant.md`
- every manuscript: consider `references/reporting/jars-rec.md`; apply each item when race, ethnicity, or culture is reported, analysed, interpreted, or relevant to generality

JARS governs reporting transparency, not study quality by itself. Never infer that a study is rigorous merely because all reporting items are present.

## Genre scope

Default assumption: you are writing a **journal article** for submission, review, or revision.

If the user is actually writing a proposal, thesis/dissertation chapter, literature review, or book chapter, use `references/genres/academic-genres.md` only to make the smallest necessary calibration without changing APRIL's article core.

## Defaults

The target journal's current author instructions and the user's requirements determine article and abstract length; APRIL has no fixed word-count default. If the target or limit is unknown, verify it or ask before treating a count as final. Other defaults are British English, APA 7, Times New Roman 12pt double-spaced, and APA-style table and figure titles and notes.

## Scripts

- **Integrated local PDF quote search:** read `references/evidence/pdf-quote-search.md`; it runs `scripts/pdf_quote_search.py` for page-accurate evidence verification.

## Core resource map

- **Reporting completeness:** `references/reporting/reporting-router.md`, then the applicable full checklist files beside it
- **Output scope and stopping rules:** `references/core/operating-contract.md`
- **Cross-stage decisions:** `references/core/manuscript-contract.md`
- **Shared-resource routing:** `references/core/resource-map.md`
- **Evidence and citation integrity:** `references/evidence/evidence-integrity.md`
- **Local quotation search and page pinning:** `references/evidence/pdf-quote-search.md`
- **Academic phrase functions:** `references/rhetoric/manchester-phrasebank.md`
- **Optional empirical research storytelling:** `references/rhetoric/empirical-storytelling.md`
- **Sentence cohesion:** `references/rhetoric/sentence-bridging.md`
- **Natural academic language and anti-formulaic editing:** `april-08-language/SKILL.md`
- **Abstract writing:** `april-07-abstract/SKILL.md`
- **Reflexive thematic analysis:** `april-04-analysis/methods/qualitative-rta.md`, with its detailed reference guide
- **Nearby academic genres:** `references/genres/academic-genres.md`, only when the task is not a journal article

Do not assume a resource has been applied merely because it exists in APRIL. Read the routed file before using its guidance.

When APRIL skills or user-specific requirements are changed in a local Codex installation, remind the user to sync the changes to this GitHub repository. Keep Codex and GitHub copies aligned when the user authorises both updates.

## Separate skills

- `ai-for-grant-writing` — use instead when the task is primarily a grant or funding package
- `claude-prism` — Prism workflows


---
**APRIL — Academic Research Skills by April**
