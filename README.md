# APRIL — Academic Paper Research & Inquiry Lab

**APRIL** (**A**cademic **P**aper **R**esearch & **I**nquiry **L**ab) is a staged skill suite for writing journal-style academic manuscripts in Cursor (and compatible agent environments).

Instead of generating a full paper in one shot, APRIL routes work through specialised stage skills—from ideation and literature through analysis, discussion, framing, language, formatting, review, and revision.

## What it is for

- Academic journal articles and manuscript drafting
- Research question and study design support
- Method-specific data analysis and findings writing
- British English academic style polishing
- APA formatting checks
- Self-critique, peer-review simulation, and reviewer response letters

## Default manuscript contract

Unless you override these defaults:

| Setting | Default |
|---|---|
| Article length | 6000–8000 words |
| Abstract | 200–300 words |
| Font / spacing | Times New Roman 12pt, double-spaced |
| References | APA |
| Table/figure captions | APA two-line style |
| Language | British English (`april-08-language`) |

## Stages

| Stage | Skill | Use when you need… |
|---|---|---|
| 01 | [`april-01-ideation`](april-01-ideation/SKILL.md) | Topic, RQs, hypotheses, scope |
| 02 | [`april-02-literature`](april-02-literature/SKILL.md) | Literature search, synthesis, citations, local PDF quotes |
| 03 | [`april-03-methodology`](april-03-methodology/SKILL.md) | Study design, method critique, diagrams |
| 04 | [`april-04-analysis`](april-04-analysis/SKILL.md) | Data analysis / findings (RTA, LPA, time series, CLPM, …) |
| 05 | [`april-05-discussion`](april-05-discussion/SKILL.md) | Discussion linked to literature |
| 06 | [`april-06-framing`](april-06-framing/SKILL.md) | Introduction and conclusion |
| 07 | [`april-07-abstract`](april-07-abstract/SKILL.md) | Journal abstract |
| 08 | [`april-08-language`](april-08-language/SKILL.md) | Style, British English, humanizer |
| 09 | [`april-09-formatting`](april-09-formatting/SKILL.md) | Word count, APA, captions, layout |
| 10 | [`april-10-review`](april-10-review/SKILL.md) | Author self-critique or peer-review simulation |
| 11 | [`april-11-revision`](april-11-revision/SKILL.md) | Point-by-point response to reviewers |

## Typical pipeline

```text
Ideation → Literature → Methodology → Analysis → Discussion
  → Framing → Abstract → Language → Formatting → Review → Revision
```

Do **not** load every stage at once. Pick the smallest matching child skill and read its `SKILL.md` first. For analysis, load **one** method card under [`april-04-analysis/methods/`](april-04-analysis/methods/).

## Install (Cursor)

1. Clone this repository into your Cursor skills directory:

```bash
git clone git@github.com:Apriljzhang/APRIL.git ~/.cursor/skills/april
```

2. Restart Cursor or reload the window so skills are discovered.
3. Ask the agent for the stage you need (e.g. “use APRIL ideation” or “run APRIL review on this draft”).

The router entry point is [`SKILL.md`](SKILL.md).

## Operating principles

1. Keep the human researcher in control of questions, methods, interpretation, and final prose.
2. Verify citations and claims before treating output as publication-ready.
3. Prefer staged checkpoints over one-shot full papers.
4. For analysis, load one method card at a time.
5. Language house rules take precedence over the humanizer when they conflict.

## Repository layout

```text
april/
├── SKILL.md                 # Router / overview
├── april-01-ideation/
├── april-02-literature/
├── april-03-methodology/
├── april-04-analysis/
│   └── methods/             # Method cards (RTA, LPA, SEM, …)
├── april-05-discussion/
├── april-06-framing/
├── april-07-abstract/
├── april-08-language/
├── april-09-formatting/
├── april-10-review/
└── april-11-revision/
```

## Author

April — Academic Paper Research & Inquiry Lab.
