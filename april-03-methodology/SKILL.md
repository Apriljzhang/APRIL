---
name: april-03-methodology
description: >-
  APRIL stage 03: methodology expert — quantitative and qualitative design choice,
  critique, validity threats, and diagrams (PRISMA, path/CLPM, multilevel, LPA,
  CSDID/staggered-DiD, and network-analysis decision maps).
  Hands execution to april-04-analysis.
---

# april-03-methodology

## Scope control (mandatory)

Read `../references/core/operating-contract.md` before acting. Produce only the requested design, critique, plan, diagram, or Method text; a pointer to Stage 04 is a handoff, not permission to execute it.

Preserve the problem, purpose, RQs, constructs, population, and other settled choices through `../references/core/manuscript-contract.md`. Surface any design requirement that conflicts with them.

## Goal
Decide **whether** the design fits the RQs. Critique weaknesses. Produce diagrams. Do **not** run full analyses here → `april-04-analysis`.

## Workflow
1. Restate RQs and claim type (describe / compare / explain / evaluate / predict).
2. Map to a design family (experiment, survey, panel, case, ethnography, mixed, secondary, observational coding, text corpus, etc.), then use `../references/methods/method-index.md` to name the primary approach and analytical family.
3. Choose among close alternatives when relevant:
   - LPA vs LCA vs clustering
   - CLPM vs RI-CLPM
   - STM/topic model vs qualitative coding
   - DiD vs IV vs other identification
   - conventional DiD/TWFE vs Callaway–Sant'Anna group-time effects for staggered adoption: read `references/csdid-design.md` and lock the estimand, comparison group, timing, and identifying assumptions before implementation
   - fsQCA (configurational sufficiency/necessity) vs net-effects regression/SEM
   - cross-sectional network analysis vs regression/SEM/latent-variable models: use a network only when conditional relations among nodes are the research object
   - one-network estimation vs bridge analysis vs two-network comparison/NCT: require defensible communities for bridge metrics and two commensurable networks for NCT
4. Specify sampling, measures, procedures, analysis plan, ethics. Explain why each consequential choice can answer the RQ or address a named validity threat; do not report only how the procedure will be performed.
5. List validity threats and mitigations.
6. Provide diagram specs (mermaid/ASCII acceptable): PRISMA flow, path model, multilevel nesting, profile decision tree, staggered-DiD cohort-time/valid-comparison map, QCA solution/configuration map, or network-analysis module decision map.
7. Name the primary `april-04-analysis/methods/*.md` card to execute next. For a justified multi-method design, name each additional substantive card, the distinct RQ/estimand it serves, execution order, and integration point.

Optional narrative enhancement: when the user asks for an explanatory story, read `../references/rhetoric/empirical-storytelling.md` and distinguish the phenomenon, directly examined mechanism, and tested condition or boundary. Do not add analyses merely to complete that narrative pattern.

## Thematic analysis design

When the RQ calls for patterned meaning in qualitative material, name the form of thematic analysis before planning its procedures: reflexive, codebook, or coding-reliability TA. Align the choice with the epistemology, researcher role, intended analytic product, and quality criteria. Route reflexive TA to `april-04-analysis/methods/qualitative-rta.md`; route a structured codebook or coding-reliability design to `april-04-analysis/methods/qualitative-coding-analysis.md` when no more specific method applies. Do not describe a fixed codebook, consensus coding, or inter-rater agreement as reflexive TA.

For an AI-assisted codebook design, plan a traceable path from protected transcripts to meaning-based segments, initial codes, a documented and revisable codebook, contextual pattern comparison, candidate themes, exceptions, and source-linked claims and quotations. Specify a corpus and metadata audit; case, speaker, and segment identifiers; familiarisation and analytic memos; pilot coding of varied material; code definitions and inclusion/exclusion boundaries; human review of code changes; and how contradictory, partial, or boundary cases will be examined. Compare across cases only when cases are defined, and do not infer theme importance from code counts alone. Decide whether consent and data governance permit AI processing, and how original wording and identifying information will be protected.

When interpretive themes are the intended output, distinguish a topic or category from a theme by stating the pattern of meaning, its central organising concept, and how it answers the RQ. If the design instead calls for topic summaries, label them accurately. For reflexive TA, plan recursive familiarisation, coding, theme development, review, and reflexive memoing without imposing the codebook pipeline or its reliability criteria. In every approach, the researcher judges theme quality and owns the interpretation; software may help organise, retrieve, and compare material but cannot supply an evidentiary warrant on its own.

## Systematic reviews
If SLR/scoping: follow `../references/reporting/prisma.md` before analysis/synthesis writing.

## Outputs
Design rationale; threats table; diagram; pointer to the primary analysis card; and, when justified, a sequenced multi-method and integration plan.

## JARS (Method)
Before locking the design write-up, read `../references/reporting/reporting-router.md`, then run the Method section of `../references/reporting/jars-quant.md`, `../references/reporting/jars-qual.md`, and/or all three design files for Mixed. Consider `../references/reporting/jars-rec.md` for every manuscript and apply its relevant items.

- **Quant:** name the relevant JARS–Quant module when the design is specialised, not only the general Table 1 checklist:
  - experimental manipulation (`Table 2`)
  - random assignment (`Table 2A`)
  - nonrandom assignment (`Table 2B`)
  - clinical trial (`Table 2C`)
  - no experimental manipulation / observational (`Table 3`)
  - longitudinal (`Table 4`)
  - N-of-1 (`Table 5`)
  - replication (`Table 6`)
  - SEM (`Table 7`)
  - Bayesian (`Table 8`)
  - quantitative meta-analysis (`Table 9`)
- **Qual:** plan researcher description, reflexivity, data-source selection, analytic transparency, and methodological integrity.
- **Mixed:** name the mixed design explicitly and state the qualitative, quantitative, and integration goals separately.
- **All designs:** carry relevant REC terminology, sampling, and measurement issues forward from `../references/reporting/jars-rec.md`.


---
**APRIL — Academic Research Skills by April** (Academic Paper Research & Inquiry Lab)
