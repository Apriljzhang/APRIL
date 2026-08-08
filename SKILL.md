---
name: april
description: >-
  APRIL — Academic Paper Research & Inquiry Lab. Helps plan, write, and revise
  academic journal papers through staged skills: ideation, literature,
  methodology, analysis, discussion, framing and abstract, language, formatting,
  review, and revision. Use for a complete article workflow, for choosing the
  correct APRIL stage, or when work must comply with APA JARS reporting standards.
  Follow the user's requested stage and deliverables without silently expanding
  into unrequested manuscript sections or a complete paper.
---

# APRIL

**APRIL** (Academic Paper Research & Inquiry Lab) is a skill suite that helps you write academic journal papers step by step—from research questions to a submission-ready manuscript and reviewer responses.

APRIL is **for journal articles**. Adjacent genres such as thesis/dissertation chapters, research proposals, literature reviews, or book chapters are only handled as minor transfer cases when relevant. See `references/academic-genres.md`.

## Scope control (mandatory)

Read `references/scope-control.md` before routing or producing work. Treat uploaded materials as context, not permission to generate every possible output. Run the complete pipeline only when the user explicitly requests a whole manuscript or end-to-end workflow.

## Stages

| # | Skill | Helps you… |
|---|---|---|
| 01 | `april-01-ideation` | Shape topic, purpose, and RQs |
| 02 | `april-02-literature` | Search and synthesise literature |
| 03 | `april-03-methodology` | Design the study |
| 04 | `april-04-analysis` | Analyse data and write findings |
| 05 | `april-05-discussion` | Interpret results against the literature |
| 06 | `april-06-framing` | Write Introduction, Conclusion, and Abstract |
| 08 | `april-08-language` | Polish British English academic style |
| 09 | `april-09-formatting` | Format length, APA, captions |
| 10 | `april-10-review` | Review like an editor/referee |
| 11 | `april-11-revision` | Revise and write the response letter |

## How to use

1. Identify the user's requested operation, object, deliverables, and stopping point; then read the corresponding stage `SKILL.md` in full.
2. Load **one stage** at a time. Do not run every stage unless the user requests an end-to-end audit.
3. For analysis, open `april-04-analysis/references/method-index.md`, identify the primary approach and analytical family, then load the primary method card. Add support cards or separately specified substantive cards only when the RQs and integration plan justify them.
4. Preserve a compact manuscript contract across stages: target journal, article type, RQs/aims, design, sample/data, main claims, word limits, and unresolved risks. Do not silently change these decisions.
5. Treat each stage's `references/*sources.md` file as provenance. Read it when checking the basis of guidance, not for routine execution.

## Reporting standards

For empirical articles, read `references/jars/SKILL.md` before applying reporting standards. Then load the complete applicable APRIL checklist:

- quantitative: `references/jars/jars-quant.md`
- qualitative: `references/jars/jars-qual.md`
- mixed methods: all three of `references/jars/jars-mixed.md`, `references/jars/jars-qual.md`, and `references/jars/jars-quant.md`
- every manuscript: consider `references/jars/jars-rec.md`; apply each item when race, ethnicity, or culture is reported, analysed, interpreted, or relevant to generality

JARS governs reporting transparency, not study quality by itself. Never infer that a study is rigorous merely because all reporting items are present.

## Genre scope

Default assumption: you are writing a **journal article** for submission, review, or revision.

If the user is actually writing a proposal, thesis/dissertation chapter, literature review, or book chapter, use `references/academic-genres.md` only to make the smallest necessary calibration without changing APRIL's article core.

## Defaults

The target journal's current author instructions override APRIL defaults. Otherwise use British English; paper about 6–8k words; abstract 200–300 words; APA 7; Times New Roman 12pt double-spaced; APA-style table and figure titles and notes.

## Tools

- **Integrated local PDF quote search:** read `april-02-literature/references/pdf-quote-search.md`; it runs the internal code under `tools/pdf-quote-finder/` for page-accurate evidence verification.

## Core resource map

- **Reporting completeness:** `references/jars/SKILL.md`, then the applicable full checklist files beside it
- **Output scope and stopping rules:** `references/scope-control.md`
- **Local quotation search and page pinning:** `april-02-literature/references/pdf-quote-search.md`
- **Academic phrase functions:** `april-08-language/references/manchester-phrasebank.md`
- **Sentence cohesion:** `april-08-language/references/sentence-bridging.md`
- **Natural academic language and anti-formulaic editing:** `april-08-language/SKILL.md`
- **Reflexive thematic analysis:** `april-04-analysis/methods/qualitative-rta.md`, with its detailed reference guide
- **Nearby academic genres:** `references/academic-genres.md`, only when the task is not a journal article

Do not assume a resource has been applied merely because it exists in APRIL. Read the routed file before using its guidance.

## Separate skills

- `ai-for-grant-writing` — use instead when the task is primarily a grant or funding package
- `claude-prism` — Prism workflows


---
**APRIL — Academic Research Skills by April**
