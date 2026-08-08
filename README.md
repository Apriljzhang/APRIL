# APRIL — Academic Paper Research & Inquiry Lab

APRIL is a staged Codex skill suite for planning, analysing, writing, reviewing, and revising academic journal articles. Designed for education, applied linguistics, TESOL, psychology, and related social sciences, it connects methodological reasoning, evidence integrity, reporting standards, and academic language without collapsing them into a single generic writing workflow.

## Core behaviour

APRIL follows the user's requested operation, object, deliverables, and stopping point.

- A narrow request remains narrow: “three RQs only” produces three RQs, and editing one paragraph does not trigger a manuscript-wide rewrite.
- A broad request authorises the integral working artefacts needed to complete it: an end-to-end analysis may require diagnostics, tables, figures, code, and an audit trail even when each item is not named separately.
- Optional outputs are not automatic bundles.
- A new manuscript section, analytical question, method, audience, or downstream stage requires explicit instruction.

Uploaded manuscripts, datasets, variable descriptions, and references provide context; their availability does not authorise APRIL to generate a complete paper unless requested.

## Stages

| Stage | Skill | Primary role |
|---|---|---|
| 01 | [`april-01-ideation`](april-01-ideation/SKILL.md) | Actively question and shape the problem, purpose, contribution, RQs, hypotheses, feasibility, and boundaries |
| 02 | [`april-02-literature`](april-02-literature/SKILL.md) | Search, verify, and synthesise literature, including Zotero and local PDF evidence |
| 03 | [`april-03-methodology`](april-03-methodology/SKILL.md) | Select and critique the research design and prepare the analysis handoff |
| 04 | [`april-04-analysis`](april-04-analysis/SKILL.md) | Select and execute empirical analyses, diagnostics, tables, figures, and requested Results/Findings |
| 05 | [`april-05-discussion`](april-05-discussion/SKILL.md) | Interpret locked findings against verified literature without introducing new results |
| 06 | [`april-06-framing`](april-06-framing/SKILL.md) | Draft the specifically requested Introduction, Conclusion, or Abstract |
| 07 | [`april-07-language`](april-07-language/SKILL.md) | Edit academic prose while preserving evidence, terminology, citations, quotations, and analytic meaning |
| 08 | [`april-08-formatting`](april-08-formatting/SKILL.md) | Apply journal, APA, table, figure, caption, and submission formatting |
| 09 | [`april-09-review`](april-09-review/SKILL.md) | Review the requested scope through methodological, literature, contribution, clarity, ethics, and journal-editor lenses |
| 10 | [`april-10-revision`](april-10-revision/SKILL.md) | Revise selected comments or sections and prepare response-to-reviewer materials |

## APRIL Commons

Shared resources live under [`references/`](references/) and are loaded only when relevant. They are not separate skills.

| Family | Purpose |
|---|---|
| [`core`](references/core/) | Instruction precedence, proportional scope, cross-stage manuscript decisions, and stopping rules |
| [`evidence`](references/evidence/) | Citation, quotation, data, and claim integrity; integrated local PDF quotation search |
| [`framing`](references/framing/) | Shared problem, purpose, contribution, and RQ distinctions |
| [`genres`](references/genres/) | Minimal calibration for nearby academic genres while retaining the journal-article core |
| [`methods`](references/methods/) | Primary approach, analytical-family taxonomy, and method-card routing |
| [`reporting`](references/reporting/) | APA JARS Quant, Qual, Mixed, and REC; PRISMA routing; reporting-standard precedence |
| [`rhetoric`](references/rhetoric/) | Manchester-inspired rhetorical moves, Discussion moves, qualification, cohesion, and APRIL house style |

JARS governs what should be reported. Method cards govern whether a design or analysis is defensible. Rhetorical resources govern how an evidence-supported scholarly move is expressed. Reporting completeness is not a substitute for methodological quality.

## Analysis methods

Stage 04 currently contains 24 method cards organised through the shared [method index](references/methods/method-index.md):

- quantitative variable-centred, comparative, multilevel, latent-variable, longitudinal, causal, Bayesian, network, and time-series approaches;
- qualitative coding, reflexive thematic analysis, and online/virtual ethnography;
- mixed-methods integration, Q methodology, corpus-assisted discourse analysis, and evidence synthesis;
- configurational and computational approaches, including fsQCA and topic modelling;
- supporting cards for power/precision and reproducible implementation in Stata, R, or Python.

APRIL selects methods from the research question, estimand or qualitative objective, design, outcome/data form, dependence, measurement, and claim boundary—not from whichever model produces a preferred result.

For R-based analyses, Stage 04 can work through a supervised live RStudio session using its [integrated authenticated localhost workflow](april-04-analysis/references/rstudio-execution.md). This is an execution option within the tooling support card, not a separate skill or analytical method.

## Defaults

The user's instruction and the target journal's current requirements override APRIL defaults.

| Setting | Default when unspecified |
|---|---|
| Article length | 6,000–8,000 words |
| Abstract | 200–300 words |
| Language | British English |
| Citations and references | APA 7 |
| Typeface and spacing | Times New Roman 12 pt, double-spaced |
| Tables and figures | APA-compatible titles, captions, notes, and accessible visual design |

## Installation

Clone APRIL into the Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Apriljzhang/APRIL.git ~/.codex/skills/APRIL
```

Verify the installation:

```bash
cd ~/.codex/skills/APRIL
git status
git log -1 --oneline
```

Restart or reload Codex after installation so the skill list is refreshed.

## Updating

Pull the latest release from the repository:

```bash
cd ~/.codex/skills/APRIL
git pull --ff-only origin main
git log -1 --oneline
```

## Integrated local PDF quotation search

APRIL Literature includes the shared script [`scripts/pdf_quote_search.py`](scripts/pdf_quote_search.py). It supports exact and noise-tolerant matching and reports the source file and physical PDF page. Read [`references/evidence/pdf-quote-search.md`](references/evidence/pdf-quote-search.md) before using it. The implementation is part of APRIL's evidence layer and does not require a separate quotation-finder skill or tools package.

---

**APRIL — Academic Research Skills by April**
