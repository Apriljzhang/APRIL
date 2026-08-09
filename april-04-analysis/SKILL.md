---
name: april-04-analysis
description: >-
  APRIL stage 04: empirical data analysis and findings. Use when Codex receives
  data, variable descriptions, research questions, or hypotheses and must select
  a justified quantitative, qualitative, mixed, computational, longitudinal, or
  causal method; execute baseline models, heterogeneity analyses, and robustness
  checks; produce reproducible academic tables and figures; interpret findings;
  execute R code through a supervised live RStudio session when requested; or
  draft evidence-bounded Results/Findings and Discussion-ready prose. Produce
  only the analysis outputs or sections the user requests; never expand an
  analysis request into a complete manuscript.
---

# april-04-analysis

## Scope control (mandatory)

Read `../references/core/operating-contract.md` before acting. Data and a manuscript provide analytic context, not authorisation to draft the whole paper. Limit output to the requested analysis, diagnostics, tables/figures, Results/Findings, or bounded interpretation.

Preserve the study and deliverable decisions through `../references/core/manuscript-contract.md`. Apply `../references/evidence/evidence-integrity.md` to data, model output, tables, figures, quotations, and prose.

## Goal
Select, execute, diagnose, and report the requested defensible substantive analysis without inventing evidence or unrelated manuscript content.

## Routing
1. Inventory the uploaded files, variable descriptions, design, RQs/hypotheses, requested deliverables, excluded sections, and stopping point. Do not fit a model until the unit of analysis and outcome are identifiable.
2. Read `../references/methods/method-index.md`; record the primary approach, analytical family, and card. Then read `references/analysis-contract.md`.
3. For an end-to-end empirical request involving uploaded tabular data, read `references/empirical-analysis-workflow.md`.
4. Open the primary substantive file under `methods/`; record why its approach and family match the RQ, outcome/data form, design, dependence, and estimand. For a causal RQ, record the intervention, counterfactual, assignment timeline, DAG/design diagram, and identification assumptions before choosing a design module. The causal card contains alternative modules; do not run them all by default. Add a second substantive card only for a distinct RQ or genuinely multi-method design, and execute it as a separately specified analysis before integration.
5. Read `references/method-citations.md`; route each methodological claim to a source listed for that card and verify page-specific claims in the local PDF/Markdown.
6. Use `methods/tooling-stata-r-python.md` and `methods/power-analysis.md` only as support cards when needed. For an explicitly requested live RStudio session, also read `references/rstudio-execution.md` before connecting or executing code.
7. For reflexive TA, follow the detailed guide under `references/rta/`; it remains part of Stage 04.
8. When the user specifically requests research-story development, narrative depth, or a story-led empirical figure, read `../references/rhetoric/empirical-storytelling.md`. Treat it as optional presentation guidance, and stop before an untested mechanism or full Discussion.
9. Lock the verified Results/Findings before interpretation. For a full Discussion, pass the locked findings to `april-05-discussion`; style later with `april-07-language`.

## Rules
- Use one primary analytical family at a time. Allow supporting procedures and within-family modules when they answer aligned RQs and estimands. For genuinely distinct methods, specify, execute, and validate each separately, then integrate findings explicitly.
- `methods/tooling-stata-r-python.md` and `methods/power-analysis.md` are support cards and may accompany one substantive card.
- Treat the integrated RStudio bridge as supervised execution infrastructure, never as a method card or reason to select R. Use it only for the requested analysis, keep it authenticated and localhost-only, preserve its audit trail, and stop it when the bounded task ends.
- Keep related but distinct methods separate: SEM versus mediation/moderation and LCA versus LPA. Cross-route shared references rather than merging their estimands or data assumptions.
- Select models from the research design, estimand, outcome scale/distribution, dependence, and measurement properties—not from file type, automated stepwise selection, or whichever result is significant. Do not infer a within-cluster, between-cluster, marginal, or causal estimand from nesting or data shape alone.
- Treat a causal design as credible only when its assignment story, counterfactual, assumptions, and diagnostics are documented. Fixed effects, matching, IV, RDD, DiD, or a significant result do not create causal identification automatically; if the design does not identify the requested effect, report the defensible association/descriptive target and state the gap.
- Treat baseline, heterogeneity, and robustness analyses as one coherent specification family. Tie every additional model to a hypothesis or a named validity threat.
- Label analyses as confirmatory, secondary, or exploratory. Do not present discovered subgroups, cut points, transformations, or outcomes as prespecified.
- Do not invent results, citations, diagnostics, or model settings.
- Do not draft numerical Results or claim support for a hypothesis before verified model output exists. If execution is impossible, provide an analysis plan and code skeleton with placeholders clearly marked.
- Do not draft the Introduction, literature review, full Method, full Discussion, Conclusion, Abstract, or complete manuscript unless the user explicitly requests those outputs. A brief interpretation requested with the analysis is not permission to generate a full Discussion.
- Treat tables, figures, robustness checks, and prose templates as conditional deliverables. Produce those requested or analytically necessary for the stated RQ; do not emit every available output by default.
- Match numbers in prose to tables exactly.
- When drafting Results prose, prefer a bounded description of the verified empirical pattern over coefficient-by-coefficient table narration. This is a presentation preference, not an extra analytical requirement. Never invent a nonlinearity, threshold, subgroup story, mechanism, or surprise that the analysis did not establish.
- Separate analytic validity from reporting completeness: JARS can reveal omissions but cannot validate a model or identification strategy.

## JARS (Results / Findings)
Read `../references/reporting/reporting-router.md`, then use the complete applicable checklist:

- **Quant:** effect sizes/intervals and primary versus secondary/exploratory reporting, plus relevant modules for experiments, longitudinal work, N-of-1, replication, SEM, Bayesian analysis, and meta-analysis.
- **Qual:** themes/categories with evidentiary excerpts, analytic transparency, and methodological integrity.
- **Mixed:** explicit integration products such as joint displays, merged summaries, connected inferences, transformed data, or meta-inferences.
- **REC:** apply `../references/reporting/jars-rec.md` whenever race, ethnicity, or culture enters sampling, coding, modeling, interpretation, subgroup reporting, or discussion.

---
**APRIL - Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
