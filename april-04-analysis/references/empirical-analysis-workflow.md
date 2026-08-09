# End-to-end empirical analysis workflow

Use this workflow when the user supplies tabular data, variable descriptions, and RQs or hypotheses and expects model selection, estimation, baseline and secondary analyses, academic tables/figures, interpretation, and paper-ready prose. Use it with `analysis-contract.md`, one substantive method card, and the tooling card.

## Contents

1. Establish an analysis-ready brief
2. Audit the data before modeling
3. Select the substantive model
4. Define and fit the baseline specification
5. Conduct heterogeneity analysis
6. Design robustness checks from threats
7. Generate academic tables and figures
8. Interpret in a fixed evidence hierarchy
9. Draft Results and Discussion-ready prose
10. Deliver and verify the analysis package

## 1. Establish an analysis-ready brief

Extract or request the following before fitting:

- research question and directional or nondirectional hypotheses;
- unit of analysis, sampling frame, design, timing, assignment or exposure process, and target population;
- outcome, focal predictor/exposure, moderators, mediators, covariates, fixed effects, clusters, strata, and weights;
- variable definitions, coding, reference categories, scale construction, valid ranges, and special missing codes;
- planned versus secondary or exploratory status;
- inferential target: association, group contrast, prediction, within-unit change, or causal effect;
- preferred software, target journal/style, and required deliverables.

Inspect first and ask only for omissions that can change the estimand or model. If variable semantics, time order, assignment, outcome, or unit of analysis remain ambiguous, stop at a provisional plan. Never infer construct meaning from column names alone.

## 2. Audit the data before modeling

Keep raw files immutable and create scripted derived data. Record the file name and fingerprint, import engine/settings, sheet or table, row and column counts, labels, encodings, and software/package versions.

Check and report:

- storage type versus substantive measurement level;
- valid ranges, category frequencies, zero counts, rare levels, impossible values, and special missing codes;
- missingness by variable and analysis group, plus the complete-case count for each planned model;
- duplicate rows and duplicate identifiers;
- merge cardinality and unmatched records when files are joined;
- nesting, repeated observations, panel balance, dates, exposure/outcome ordering, attrition, and survey design variables;
- scale scoring, reverse-coded items, reliability evidence, and construct validity when composites are used;
- leakage, post-treatment controls, perfect prediction, sparse cells, and variables with no usable variation.

Produce a short data-audit table with `issue`, `evidence`, `decision`, `affected analyses`, and `remaining limitation`. Do not silently repair ambiguous values.

## 3. Select the substantive model

Create a model-selection record before estimation:

| Field | Required content |
|---|---|
| Target | RQ/hypothesis, estimand, population, and unit |
| Outcome | Scale, distribution, timing, and censoring/truncation if relevant |
| Design | Experimental/observational, cross-sectional/longitudinal, sampling/assignment |
| Dependence | Independent, clustered, repeated, panel, spatial, or temporal |
| Specification | Family, link, functional form, covariates, interactions, FE/RE, weights |
| Uncertainty | Model-based, robust, clustered, bootstrap, randomization-based, or posterior |
| Assumptions | Design and model assumptions that identify or interpret the target |
| Decision | Selected card/model, rejected alternatives, and reason |
| Claim boundary | Association, prediction, description, or causal claim actually supported |

For a causal target, add an identification record before selecting the estimator: intervention and counterfactual, target estimand/population, assignment timeline, DAG or design diagram, required assumptions, design-specific diagnostics, and the claim boundary if an assumption fails. Route to the relevant module inside `causal-did-iv.md`; the modules are alternatives within one causal family, not a checklist to run all at once.

Use this routing logic, then read the named card:

| Data/RQ characteristic | Default route | Selection checks |
|---|---|---|
| Continuous outcome; independent observations | `regression-glm.md` | Functional form, residual structure, influential cases, heteroskedasticity |
| Binary, ordinal, count, or rate outcome | `regression-glm.md` | Link, exposure/offset, overdispersion, zero process, separation, proportional odds |
| Randomized groups or repeated experimental contrasts | `experimental-group-comparisons.md` | Assignment, baseline adjustment, repeated structure, multiplicity |
| Nested, repeated, or panel observations | `multilevel-regression.md` | Level-specific estimand, within-between separation, FE versus RE, cluster count |
| Mediation, moderation, or conditional effect | `mediation-moderation.md` | Temporal ordering, interaction scale, indirect-effect assumptions, uncertainty |
| Causal intervention, assignment rule, threshold, policy timing, or comparative case | `causal-did-iv.md` | Potential outcomes/DAG, assignment process, design module (randomization, matching, RDD, panel, DiD, IV, synthetic control), estimand, diagnostics |
| Longitudinal reciprocal constructs | `cross-lagged.md` | Within-person versus between-person target, waves, stationarity constraints |
| Serially ordered aggregate outcome | `time-series.md` | Trend/seasonality, autocorrelation, horizon, leakage, rolling evaluation |
| Latent constructs or measurement model | `sem-cfa.md` | Indicator type, identification, estimator, missingness, measurement invariance |
| Latent subgroups | `latent-class-lca.md` or `latent-profile-lpa.md` | Indicator type, enumeration, local independence, uncertainty; keep LCA/LPA separate |
| Set-theoretic sufficiency/necessity | `fsqca.md` | Calibration theory, truth-table thresholds, limited diversity |
| Conditional relations among variables as the research object | `network-analysis.md` | Node type/boundary, network estimand, accuracy/stability; add bridge or NCT only when the RQ requires it |

Do not select a model from bivariate significance, stepwise routines, fit indices alone, or the estimator that yields the preferred conclusion. If the needed method has no Stage 04 card, identify the gap and do not force a substitute.

When clustered or longitudinal data permit multiple targets, distinguish within-unit, between-unit, cluster-specific, and population-average estimands. Do not select one merely because the data are nested. If the RQ does not resolve the target, present the defensible alternatives and pause for that decision before declaring a primary model.

## 4. Define and fit the baseline specification

Treat “baseline” as the primary specification tied to the hypothesis and estimand, not automatically the simplest or most favorable model.

1. Freeze the analysis sample, coding, transformations, reference categories, covariates, fixed/random effects, weights, and variance estimator before reading focal results when feasible.
2. Justify covariates from design, theory, or a causal model. Flag post-treatment controls and colliders; do not use automated significance-based selection.
3. If sequential models clarify adjustment, use a declared ladder such as unadjusted/design-only, primary prespecified, and extended secondary. Keep a common sample for coefficient comparisons or explicitly explain sample changes.
4. Align uncertainty with assignment and dependence. Report cluster counts and small-cluster limitations where relevant.
5. Run the selected card's diagnostics and preserve warnings, failed fits, and corrective decisions.
6. Report the estimand on an interpretable scale using contrasts, standardized effects, predicted values, probabilities, marginal effects, or incidence-rate ratios when raw coefficients are not substantively clear.

Never equate a baseline association with a causal effect unless the design and identification strategy warrant it.

Do not choose complete-case analysis, likelihood-based handling, weighting, or multiple imputation from the missing percentage alone. Justify the primary approach from the missingness process, available auxiliary variables, model compatibility, and sensitivity to departures from its assumptions.

## 5. Conduct heterogeneity analysis

Run heterogeneity analysis only when theory, design, equity relevance, or a clearly labeled exploratory aim supports it.

- Prefer a pooled interaction model and report the interaction contrast or marginal effect. Do not infer subgroup differences because one subgroup is significant and another is not.
- Preserve continuous moderators when possible; do not create data-driven median splits or hunt for cut points.
- Predefine subgroup boundaries and reference categories. Report subgroup sample sizes, events/cells, overlap, and precision.
- Distinguish effect heterogeneity from differences in outcome levels and from scale artifacts in nonlinear models.
- Use predicted outcomes or marginal effects for interpretable nonlinear-model comparisons.
- Address multiplicity across many subgroups or outcomes and label exploratory analyses.
- Apply the JARS-REC guidance when race, ethnicity, or culture enters the analysis; avoid biological or essentialist interpretations unsupported by the design.

If sparse data, poor overlap, or unstable estimates make subgroup inference unreliable, report the limitation rather than suppressing the failed analysis.

## 6. Design robustness checks from threats

Build a threat-to-check matrix before running robustness models:

| Validity threat | Targeted check | What would change confidence | Limitation of the check |
|---|---|---|---|

Choose only checks that probe plausible consequential decisions, such as:

- alternative defensible operationalizations of the outcome or focal predictor;
- functional-form changes, nonlinear terms, links, distributional families, or variance estimators;
- missing-data approaches and attrition assumptions;
- influential-observation, leverage, overlap, or trimming sensitivity;
- alternative clustering, fixed effects, lag structures, or time windows justified by design;
- placebo, falsification, pretrend, negative-control, or sensitivity analyses when their assumptions fit the causal design;
- bootstrap, permutation, posterior predictive, or out-of-sample checks when appropriate to the selected method.

Judge robustness by the estimand's direction, magnitude, interval, and substantive conclusion—not by whether every p value remains below a threshold. A robustness check cannot repair an unidentified design, invalid measurement, or poor data quality.

## 7. Generate academic tables and figures

Generate every displayed number from saved analysis objects. Adapt to the target journal; absent a specified style, use compact APA-compatible conventions.

Recommended output set:

- Table 1: analytic sample, variable definitions, descriptive statistics, and missingness;
- Table 2: primary/baseline model sequence;
- Table 3: prespecified or clearly labeled exploratory heterogeneity effects;
- Table 4: robustness or sensitivity summary organized by validity threat;
- Figure 1: coefficient/effect plot with uncertainty intervals;
- Figure 2: marginal effects or predicted outcomes for key interactions/nonlinear findings;
- Supplement: model diagnostics and additional sensitivity results.

For each table, identify the outcome, coefficient/effect scale, reference categories, covariates, fixed/random effects, weights, variance estimator, clustering level/count, interval level, model-specific fit, and per-model sample size. Define exact p-value or significance-symbol rules if used; do not report stars without effect sizes and intervals.

For each figure, show uncertainty, use an honest axis and accessible palette, label scales and units, and write a self-contained caption. Use coefficient plots instead of dense regression tables when comparison is the message, and marginal-effect or predicted-probability plots instead of interpreting nonlinear interaction coefficients in isolation.

## 8. Interpret in a fixed evidence hierarchy

For each key finding, state:

1. the model, comparison, population, and estimand;
2. direction, magnitude, units or scale, and uncertainty;
3. whether and how the result addresses the hypothesis;
4. substantive meaning, not only statistical significance;
5. relevant diagnostic and robustness evidence;
6. the strongest claim the design permits and what it does not establish.

Do not treat nonsignificance as proof of no effect, a wide interval as equivalence, a proxy as the construct itself, or an exploratory pattern as confirmation. Do not explain mechanisms unless measured or clearly presented as a hypothesis.

## 9. Draft Results and Discussion-ready prose

Write Results in the order of the hypotheses, not the order in which models were tried. Use this paragraph logic: analysis and estimand → estimate and uncertainty → diagnostic/robustness evidence → hypothesis status → table/figure callout. Match every number to the final table or figure and avoid citations unless they justify a method.

When a research-story presentation is requested, also read `../../references/rhetoric/empirical-storytelling.md`. For each RQ, describe the direction, magnitude, shape, variation, or patterned meaning before stating its interpretation boundary. Report nonlinearities, thresholds, subgroup differences, mechanisms, and unexpected results only when the corresponding analysis or evidence establishes them. Do not convert a table into sentence-by-sentence coefficient narration.

Create a locked findings ledger before prose with `finding_id`, hypothesis, model/output object, estimate, interval, p value or posterior summary, N, sample, interpretation, and claim boundary. Draft only from this ledger.

For Discussion-ready synthesis, separate:

- **supported interpretation:** what the estimates imply at their observed scale;
- **theoretical interpretation:** how the pattern bears on the stated theory or mechanism, with uncertainty;
- **boundary conditions:** population, design, measurement, model, and subgroup limits;
- **robustness qualification:** which alternatives were tested and which remain unresolved;
- **implication:** a proportionate research or practice implication, avoiding causal language when unsupported.

Use `april-05-discussion` for the full Discussion, especially comparisons with prior literature, contributions, implications, and future research. Do not invent literature or citations when the user has not supplied a verified evidence base.

## 10. Deliver and verify the analysis package

Return or save, as requested:

1. analysis brief and model-selection record;
2. reproducible data-preparation and analysis code;
3. data and decision audit tables;
4. publication-ready tables and figures plus machine-readable source values;
5. diagnostics and threat-linked robustness outputs;
6. locked findings ledger;
7. Results draft and Discussion-ready synthesis;
8. limitations, unresolved decisions, and JARS status.

Before delivery, rerun the workflow from a clean session when feasible; confirm expected files are nonempty; reconcile sample sizes across data, models, tables, and prose; and programmatically compare reported estimates, intervals, labels, and notes with the final model objects.
