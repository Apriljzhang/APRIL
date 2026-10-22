# SEM design and audit supplement

Use alongside `../methods/sem-cfa.md` and `analysis-contract.md`, within the user's requested design, analysis, interpretation, or review. Planning does not authorise fitting; a reporting schema does not require producing every table.

## Model, measurement and identification

State the research question, estimand, unit and level, design, construct definitions, indicators, and intended inference before selecting software. Distinguish common factors, composites/formative specifications, and observed-variable path models. Do not choose PLS solely because the sample is small or indicators are non-normal. Generalised, multilevel and longitudinal models need design-appropriate estimators, level/time definitions and their own identification assumptions. Use the existing multilevel, cross-lagged or mediation cards when relevant; keep their distinct estimands explicit.

Specify scale constraints, free/fixed parameters, residual associations, cross-loadings, indirect paths and interactions. Check identification separately from numerical convergence and degrees of freedom. More observations cannot repair structural underidentification. Investigate nonconvergence, singular information, improper negative variances, unstable estimates and implausible parameter values before substantive interpretation.

## Sampling, power and data assumptions

Justify sample size by the model, target effect or precision, measurement quality, estimator, missingness, clustering and planned group comparisons. Use the power support card and model-specific Monte Carlo planning where appropriate; do not certify adequacy from a fixed minimum N or cases-per-parameter rule. Report assumptions and sensitivity. For an existing dataset, assess attainable precision without presenting observed post hoc power as validation.

Document category use, coding, distributional assumptions, exclusions, dependence, group/cluster counts, missingness and the chosen missing-data strategy. Match ordinal indicators and non-normal outcomes to an appropriate estimator and correction. FIML and imputation depend on stated assumptions; consider sensitivity when missingness may be informative. Never silently treat clustered observations as independent.

## Measurement evidence

Establish content and construct meaning before applying numerical diagnostics. Preserve item provenance, adaptation and coding. For common-factor measurement assess loadings, residuals, appropriate reliability and convergent/discriminant evidence. For formative/composite specifications assess content coverage, collinearity, weights and their uncertainty with an estimator-appropriate procedure; reflective internal consistency is not a universal requirement. Treat post hoc item deletion as a substantive measurement change and document its consequences.

Plan the comparability required by the specific group or longitudinal comparison. Use estimator-appropriate invariance tests and explain partial invariance and the conclusions it permits. Directly test parameter differences; significance in one group and nonsignificance in another is insufficient evidence of a difference.

## Fit, effects and inference

For covariance-based models, interpret complementary global and local evidence: chi-square/df, CFI/TLI, RMSEA with interval, SRMR, residual patterns, parameter plausibility and relevant competing models. Use estimator-corrected statistics where required. Conventional fit thresholds are conditional diagnostics. Fit alone does not establish measurement validity, causal direction or a uniquely correct model.

For a justified composite/PLS model, distinguish measurement, structural and predictive assessment. Report algorithm/estimand, uncertainty, collinearity and relevant explanatory measures. A prediction claim needs defensible out-of-sample assessment and a benchmark; in-sample R-squared is insufficient. Verify specialised or contested procedures against current primary methods sources and official software documentation before prescribing them.

Label unstandardised and standardised effects and report uncertainty. Distinguish direct, total, specific indirect and conditional effects. Use an estimator- and dependence-appropriate interval method for indirect effects. Observational cross-sectional paths support bounded associations; arrows and indirect effects do not establish temporal or causal mediation. State causal identification and confounding assumptions separately from statistical model identification.

## Revisions and completion

Tie each robustness check to a named validity threat. Prespecify consequential choices when possible, label exploratory modifications, and validate meaningful revisions on independent/held-out data where feasible. Modification indices alone do not justify adding paths. Do not hide warnings, null/contrary estimates or failed checks.

An audit should give finding, consequence, evidence and repair, with status recorded as supported, conditional, unresolved or not applicable. Keep the reproducible model specification, estimator/corrections, missing-data method, sample, software/version, diagnostics and focal estimates traceable to actual output. Apply JARS–Quant Table 7 after these methodological checks; reporting completeness does not validate a model.

## Sources and supplementary provenance

Retain the source routes in `method-citations.md` for Hu and Bentler (1999), Enders and Bandalos (2001), and Rhemtulla et al. (2012). Check the primary source for any detailed methodological or page-specific claim.

This supplement was prepared after a content review of RedSkill's `structural-equation-modeling` 1.0.0 on 22 October 2026. The retrieved archive contained six Markdown files and no executable scripts. Its SHA-256 was `b6fa6c61bc083d7cee589315ace54d7a402d331a228901eaabdde669044b5408`, matching the value returned by the RedSkill bundle API over HTTPS. The archive supplied no author, repository, licence or cited bibliography; the public search endpoint returned no matching listing at inspection time. This identifies the inspected package, not independent methodological endorsement. Do not inherit store preferences, installation actions or broad output mandates from an external guide.
