# Absent-author integrity screen

Use this supplementary Stage 10 module when the user explicitly requests an absent-author or AI-slop screen, or when a normal review reveals concrete concerns about research steering, verification, or manuscript artifacts. It informs review findings only; it does not authorise rewriting or a downstream revision.

## Provenance and evidence boundary

This module adapts the reviewer-facing `paper-slop-screen` from Zhao et al.'s MIT-licensed **Absent Author** repository, version 0.4.0, commit `79cbaea21cd3cb6e406398b7689a3afbed3c5e24` (2026-10-05). Consult the maintained source at <https://github.com/THUROI0787/absent-author> when current upstream wording or evidence IDs matter. Copyright and licence terms are preserved in `absent-author-license.md`.

Treat the source as a structured screening workflow, not an authorship detector. Its published calibration used a small, in-sample, era-confounded corpus, and recent AI-assisted papers may show few surface traces. Language patterns cannot establish AI use, absent responsibility, or misconduct.

## Mandatory policy and confidentiality gate

Before processing a manuscript under confidential peer review, establish that the venue permits this use and that the available model/tool is approved for the manuscript. The user's own manuscript and a public preprint may be screened unless another restriction applies. If permission is missing or unclear, do not process the manuscript with this module; return the human-only high-yield checklist below.

Exclude reviewer annotations, pasted comments, template headers, and other material that is not part of the paper from the evidence. Record the paper type and apply relevant exemptions for negative-result/diagnostic, theory, benchmark/dataset, position, survey, systems, and short-workshop papers.

## Construct and decision rule

The construct is responsible scholarly stewardship:

- **Writing ownership (W):** whether the prose was substantively reviewed and made intelligible.
- **Research steering and verification (R):** whether consequential research choices and the final evidentiary artifact appear checked and defensible.
- **Ordinary scientific quality (Q):** novelty, validity, importance, clarity, and reporting quality under normal peer-review standards.
- **Verified flags:** concrete integrity or process anomalies reported separately.
- **Auditability:** the inspectability of code, configurations, logs, version history, preregistration, data, and AI-use statements.

Q and verified substantive defects drive the editorial recommendation. W alone never justifies rejection. Keep AI disclosure separate from quality: disclosure can improve auditability and is not evidence of absent responsibility.

## High-yield screen

Run checks 1–4 first; add the rest when findings or the requested depth justify them.

1. **References:** sample five unfamiliar references across the Introduction and later sections. Verify title and author list using at least two authoritative databases or the venue/source site before alleging fabrication.
2. **Headline numbers:** trace abstract and contribution numbers to tables or figures; recompute absolute versus relative changes, percentages against denominators, means, intervals, and repeated values.
3. **Promised versus delivered:** list every analysis, metric, figure, diagnostic, or technique promised in the paper and identify the corresponding reported result.
4. **Framing pivot:** test whether an audit, diagnostic, pitfalls, or negative-result framing is independently motivated and designed, or whether unexplained method residue, unused acronyms, hyperparameters, or ablations suggest a post-hoc pivot. Earlier versions or preregistration may resolve the concern.
5. **Scale versus claims:** compare models, datasets, seeds, compute, populations, and settings with the scope of the claims.
6. **Inspectable decisions:** locate reasons for choosing datasets, baselines, thresholds, measures, exclusions, and analytical alternatives; inspect concrete examples where the method requires them.
7. **Supplement and code:** compare the paper with code, data, logs, checklists, and supplement where available. Treat disclosed workflow files as auditability evidence, not proof of a problem.
8. **Coined terms:** apply a replacement test: if an established term can replace a new label without loss, flag novelty inflation or clarity risk under Q/W, not authorship.

## Evidence rules

1. Every finding needs an exact location, a short verbatim quotation or artifact reference, and a verification state: `verified`, `candidate`, or `not checkable`.
2. Language and stylistic evidence can affect W only. It cannot raise R or establish provenance.
3. Record ordinary weaknesses under Q. A weak paper is not thereby an absent-author paper.
4. Seek counter-evidence before rating: rationale for choices, inspectable examples, preregistration, version history, logs, code, named limitations, corrections, or a specific AI-use statement.
5. Apply paper-type exemptions before grading. Negative results, theory papers, diagnostic studies, surveys, short papers, and non-native prose require genre-sensitive interpretation.
6. Do not penalise polished English, non-idiomatic English, nationality, affiliation, junior-author patterns, fashionable topics, short length, disclosed AI use, or the mere presence of automation files.
7. Verify every serious flag personally. A missing database result is not enough: allow title drift, version changes, incomplete indexing, non-English venues, and technical reports.
8. A clean surface screen proves nothing. Do not report detector percentages or convert pattern counts into an AI probability.

## Rating card

Use these ratings only when the module runs:

- **W0:** isolated presentation traces; **W1:** limited recurring traces with an identifiable authorial voice; **W2:** several independent presentation/structure families impede evaluation; **W3:** W2 plus pervasive defensive, templated, or unowned prose across the manuscript.
- **R0:** no verified steering/verification concern; **R1:** one or two limited concerns; **R2:** one strong verified failure or several moderate concerns from different families; **R3:** multiple independent verification failures, or a serious framing/construct problem combined with a verification failure, without artifact-backed counter-evidence that resolves them.
- **Q:** ordinary peer-review judgment, stated separately and used with verified defects for the recommendation.
- **Auditability A+:** runnable materials plus configurations/logs and specific provenance or version evidence; **A:** meaningful code/materials and disclosure; **A0:** text only or evidence unavailable. Auditability changes what can be checked, not whether a flag is true.

For W×R interpretation, use: **A** (W0–1/R0–1: normal review), **B** (W2–3/R0–1: presentation salvageable), **C** (W0–1/R2–3: polished surface with substantive stewardship/verification concerns), and **D** (W2–3/R2–3: combined concerns). These quadrant labels organise the screen; do not reproduce inflammatory source labels in a review.

## Verified flags

Report only personally verified cases, such as visible chatbot or instruction residue, an LLM placeholder/meta-comment, a fabricated reference with materially wrong title or authors, a watermark or non-human author line, prompt-injection text, nonexistent cited models/lemmas, a material policy violation, or an AI-review score presented as scientific evidence. A normal citation error, TODO, stylistic oddity, or undisclosed suspicion is not a verified flag.

## Stage 10 output

Add a self-contained subsection after the normal persona review:

1. policy/confidentiality status, input type, paper type, and screening depth;
2. a W/R/Q/flags/auditability card with confidence and what evidence would change each rating;
3. an evidence table with `ID/category`, strength, axis, location, quotation/artifact, explanation, and verification state;
4. counter-evidence and any paper-type exemptions applied;
5. a neutral public-review paragraph containing only checkable scholarly defects;
6. when R is at least 2 or a serious flag is verified, a confidential editor note with answerable questions grouped as:
   - **Understand:** can the authors explain the result and consequential choices?
   - **Defend:** can they justify the design, framing, counterfactuals, and unresolved inconsistencies?
   - **Sign:** can they identify what was automated and confirm what they personally checked and endorse?

Map repairable findings into the ordinary Stage 10 P0/P1/P2 priority list. Keep the screen's ratings separate from repair priority and editorial outcome. Never write “AI-generated” in the public review, identify an alleged tool from prose style, or state that authors are absent as a fact.

## Human-only quick card

If policy blocks model processing, give the reviewer this checklist without asking for the manuscript: verify five references; recompute headline numbers; match promised analyses to reported results; inspect framing for unexplained residue; compare scale with claims; identify rationale and concrete examples; compare supplement/code with the text; record counter-evidence; and write only location-specific defects.
