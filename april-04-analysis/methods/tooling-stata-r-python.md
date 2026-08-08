# APRIL - Tooling and reproducibility (Stata, R, and Python)

## Role
Support card only. Use it with the relevant substantive card or sequenced multi-method analyses; software does not define methodology.

## Workflow
1. Prefer the established stack unless an estimator, diagnostic, or reproducibility need justifies a change.
2. Keep raw data immutable; separate raw, derived, code, results, figures, documentation, and temporary files.
3. Script every transformation in executable order; record seeds, versions, dependencies, and environment information.
4. Use relative project paths, stable names, assertions, and validation checks. Never store credentials or identifiable data in repositories.
5. Generate tables/figures from analysis objects for `april-08-formatting`; do not transcribe results manually.
6. Save machine-readable model summaries beside publication outputs so coefficients, intervals, sample sizes, and notes can be cross-checked programmatically.
7. Keep preprocessing, model fitting, diagnostics, robustness checks, tables, and figures in executable order. Fail loudly when required variables, labels, expected row counts, or output files are missing.
8. Maintain a README, data dictionary, analysis log, and session information sufficient for a collaborator to reproduce the work.

## Method-specific note
For fsQCA, keep calibration anchors, truth-table thresholds, directional expectations, and minimization settings in code and prose.

## Core references
Use `../references/method-citations.md`: Wilson et al. (2017).
