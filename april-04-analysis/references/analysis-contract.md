# APRIL Common Analysis Contract

Read this before the selected method card. Every analysis pass must address these requirements, even when a short method card does not repeat them.

First apply `../../references/core/operating-contract.md`, `../../references/core/manuscript-contract.md`, and `../../references/evidence/evidence-integrity.md`. These requirements govern analytic integrity; they do not authorise every possible analysis artifact or manuscript section. Maintain necessary diagnostics and audit information internally, but deliver only the requested outputs plus essential qualifications.

## Before fitting

1. Verify that the data are readable and preserve the raw files unchanged. Record file identity, import settings, labels, and missing-value codes.
2. Restate the RQ, hypothesis, estimand, or qualitative objective and the claim the design can support.
3. Identify the unit of analysis, dependence or nesting, sample construction, exclusions, missingness, measurement level, time order, and relevant weights.
4. Map every analysis variable to its source field and definition. Resolve ambiguous coding, scale construction, reference categories, and impossible values before fitting.
5. Distinguish preregistered or planned analyses from secondary and exploratory analyses.
6. Justify sample size, precision, information adequacy, or stopping logic in a form appropriate to the method.
7. Name assumptions that make the analysis interpretable; do not reduce assumptions to a software checklist.

## During analysis

8. Preserve a reproducible script or audit trail, software/package versions, seeds for stochastic procedures, and all consequential analyst decisions.
9. Run method-appropriate diagnostics. Investigate failures rather than hiding warnings, nonconvergence, inadmissible solutions, sparse cells, or unstable estimates.
10. Report uncertainty and magnitude, not only thresholded significance. Use effect sizes, intervals, posterior summaries, classification uncertainty, or qualitative evidentiary support as appropriate.
11. Run sensitivity or robustness checks tied to plausible alternative decisions, not a random collection of extra models.
12. Protect against multiplicity, overfitting, researcher degrees of freedom, leakage, and post hoc storytelling where relevant.

## Reporting

13. Maintain a compact audit record: decision, rationale, diagnostic/evidence, result, and limitation. Include it in the deliverable only when requested or when it is necessary to make consequential analytic decisions transparent.
14. When tables or figures are requested or analytically necessary, generate them from model objects rather than manually transcribing values. State the analysis sample, scale, uncertainty interval, variance estimator, weights, and multiplicity treatment where applicable.
15. Make tables, figures, and prose numerically and conceptually consistent; verify every reported value against the final artifact.
16. State what the analysis does not establish, especially for causal, predictive, subgroup, and latent-class claims.
17. Apply the applicable JARS pack and design module after methodological checks; report each item as met, not met, not applicable, or unclear.

Stop and ask for missing data, design details, or an expert decision when those omissions could materially change the analysis. Never fill gaps by inventing values or silently selecting a convenient specification.
