---
name: april-10-review
description: >-
  APRIL stage 10: multi-persona review plus SSCI/journal editor bar — coherence,
  methods, contribution, ethics, language, and desk-reject risks.
---

# april-10-review

## Goal
Stress-test the manuscript before submission/revision.

## Multi-persona pass (run in order)
1. **Methodologist** — design, assumptions, analysis–claim fit, missing diagnostics.
2. **Literature scholar** — coverage, outdated hubs, straw-man gaps, citation integrity.
3. **Contribution hawk** — what is new vs incremental; overclaim vs underclaim.
4. **Clarity editor** — structure, topic sentences, undefined jargon, figure/table clarity.
5. **Ethics/integrity** — consent, anonymity, dual use, AI disclosure, data availability claims.
6. **SSCI / journal editor bar** — fit to outlet, desk-reject risks, reviewer flashpoints. Use `references/ssci-editor-bar.md`.

## Output format
For each persona: 3–7 concrete issues ranked P0/P1/P2 with suggested fix location (section).
End with a **priority fix list** (max 10) for `april-11-revision`, using `references/revision-roadmap.md`.

Persona prompts: `references/persona-cards.md`.

## Rules
Do not rewrite the whole paper here. Flag; leave drafting to revision.
Do not invent missing data or citations.

## Genre-fit review
Review against journal-article expectations first. Only use `../references/academic-genres.md` when the draft is clearly for another genre.

Primary flag here: article prose that is too chapter-like, too diffuse, too expository, or too weak on contribution. Use non-article checks only when the draft is explicitly not a journal article.

## JARS compliance (reviewer lens)
Score the manuscript against `../references/jars/` for the declared design. Do not stop at generic compliance; check the relevant module level as well.

Flag, where applicable:
- missing effect sizes/CIs, missing participant-flow details, unmarked exploratory analyses, absent diagnostics, or missing module-specific reporting in Quant
- absent reflexivity, weak data-source description, thin analytic-process reporting, or unsupported integrity claims in Qual
- missing mixed-design naming, missing strand-specific goals, or absent integration products in Mixed
- REC terminology, sampling, measurement, subgroup, or interpretation gaps from `jars-rec.md`

Feed JARS gaps into the revision roadmap with the exact section where the repair belongs.


---
**APRIL — Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
