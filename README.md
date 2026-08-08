# APRIL — Academic Paper Research & Inquiry Lab

APRIL is a staged Codex skill suite for planning, analysing, writing, reviewing, and revising academic journal articles. It supports education, applied linguistics, TESOL, psychology, and related social-science research while keeping methods, evidence, reporting standards, and language work distinct.

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
| 08 | [`april-08-language`](april-08-language/SKILL.md) | Edit academic prose while preserving evidence, terminology, citations, quotations, and analytic meaning |
| 09 | [`april-09-formatting`](april-09-formatting/SKILL.md) | Apply journal, APA, table, figure, caption, and submission formatting |
| 10 | [`april-10-review`](april-10-review/SKILL.md) | Review the requested scope through methodological, literature, contribution, clarity, ethics, and journal-editor lenses |
| 11 | [`april-11-revision`](april-11-revision/SKILL.md) | Revise selected comments or sections and prepare response-to-reviewer materials |

Stage 07 is intentionally folded into Stage 06 because Abstract drafting depends on stable framing, methods, and findings.

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

## Install on a Mac

Open **Terminal** on the Mac where Codex will use APRIL.

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:Apriljzhang/APRIL.git ~/.codex/skills/APRIL
```

Verify the installation:

```bash
cd ~/.codex/skills/APRIL
git status
git log -1 --oneline
```

Restart or reload Codex after installation so the skill list is refreshed.

## Update APRIL on another Mac

Run these commands in Terminal on that Mac:

```bash
cd ~/.codex/skills/APRIL
git pull --ff-only origin main
git log -1 --oneline
```

If GitHub SSH has not been configured on that computer, test it with:

```bash
ssh -T git@github.com
```

GitHub normally responds that authentication succeeded but shell access is unavailable. That message confirms the SSH key works.

## Two-Mac workflow

Before switching computers, commit and push completed APRIL changes from the computer where they were made. On the other computer, pull before editing:

```bash
cd ~/.codex/skills/APRIL
git pull --ff-only origin main
```

Do not edit the same uncommitted APRIL files independently on both computers. GitHub is the synchronisation source for the skill; manuscript files and research materials can remain in their separate document-storage workflow.

## Integrated local PDF quotation search

APRIL Literature includes a local quotation locator under `tools/pdf-quote-finder/`. It supports exact and noise-tolerant matching and reports the source file and physical PDF page. Read [`references/evidence/pdf-quote-search.md`](references/evidence/pdf-quote-search.md) before using it. This capability is internal to APRIL and does not require a separate quotation-finder skill.

---

**APRIL — Academic Research Skills by April**
