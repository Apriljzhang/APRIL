# CSDID and staggered-DiD design decisions

Read this reference when a proposed design uses difference-in-differences with multiple periods, staggered treatment adoption, Callaway–Sant'Anna group-time effects, R `did::att_gt`, or Stata `csdid`. Use it to decide whether the design and estimand are defensible. Do not execute estimation in Stage 03; hand the locked design to `../../april-04-analysis/methods/causal-did-iv.md`.

## Provenance and evidence boundary

This design guide was prompted by the historical `did-event-study` skill in Pedro H. C. Sant'Anna's MIT-licensed `pedrohcgs/claude-code-my-workflow` repository at tag `v2.1.0`. The upstream project removed that skill in `v2.5.0` because its methodological prescriptions lacked current owner sign-off. Treat that historical skill as workflow inspiration, not authority. Resolve technical choices against the current official `did`/`csdid` documentation and the primary literature, especially Callaway and Sant'Anna (2021).

## Applicability gate

Use a Callaway–Sant'Anna-style staggered DiD route only when all of the following are plausible:

- units are observed across multiple periods as panel data or defensible repeated cross-sections;
- treatment timing varies across cohorts, or multiple pre/post periods make group-time effects useful;
- treatment is binary and absorbing for the target analysis: after first treatment, a unit does not return to untreated status;
- a credible never-treated or not-yet-treated comparison is available for the relevant group-time contrasts;
- no anticipation, parallel trends for the chosen comparison and conditioning set, and limited interference/spillovers are substantively defensible;
- treatment timing, outcome measurement, sample composition, and the unit-period structure can be defined without post-treatment recoding.

Do not force this route onto reversible or repeatedly switching treatments, a setting without a credible comparison group, or a purely associational question. A simple two-group/two-period design may need only a transparent 2x2 DiD or doubly robust 2x2 estimator. Continuous or time-varying dose requires a separate, currently supported design route rather than relabelling dose as binary treatment.

## Design contract

Lock these decisions before choosing software or writing code.

1. **Unit and timing:** unit of analysis; calendar-time variable; first-treatment cohort; observation window; treatment onset; anticipation window; whether treatment is genuinely absorbing.
2. **Target estimand:** define the group-time effect `ATT(g,t)` and the intended aggregation. Distinguish an overall group-weighted ATT, event-time dynamics, calendar-time effects, and cohort-specific effects. Do not present an unaggregated matrix or a default TWFE coefficient as if it were the unique target.
3. **Comparison group:** choose `nevertreated` or `notyettreated` from the institutional counterfactual, not package convenience. The current R `did::att_gt` default is `nevertreated`; `notyettreated` adds units that will be treated later while they remain untreated. State how the chosen group changes the parallel-trends claim, support, and target population.
4. **Parallel trends:** state whether trends are assumed unconditionally or conditional on pre-treatment/baseline covariates. Do not condition on mediators, post-treatment variables, or treatment-affected covariates. Explain why the selected comparison units would have followed the treated cohort's untreated path.
5. **Data form:** require long data with one row per unit-period, a stable unit identifier, a first-treatment cohort variable, and explicit coding for never-treated units. Check duplicate unit-period rows, missing periods, panel balance, attrition, and whether balancing changes the population or estimand. For repeated cross-sections, specify how population composition remains comparable.
6. **Threats:** assess anticipation, spillovers/interference, coincident policies or shocks, endogenous timing, selective attrition, outcome-definition changes, sparse cohorts, limited overlap, and few treated clusters.
7. **Inference:** choose clustering or resampling from the treatment-assignment and dependence structure. Record the number of treated groups/clusters and flag settings where conventional cluster-robust inference is unreliable.

## Estimator and comparison map

- **Staggered adoption with heterogeneous effects:** prefer interpretable group-time effects or another estimator designed for staggered timing; use TWFE only as a clearly labelled benchmark when its weighting and comparison structure are understood.
- **Single adoption date with a credible untreated group:** a conventional DiD or 2xT design may be sufficient; group-time machinery is optional rather than automatically superior.
- **Two groups and two periods:** consider a transparent 2x2 DiD; use a doubly robust 2x2 route when justified covariates are part of the identification strategy.
- **Quasi-random rollout timing:** consider design-based staggered estimators in addition to the general group-time route, stating the stronger timing assumption.
- **Reversible, repeated, or continuous treatment:** stop and choose a method whose identification results match that treatment process.
- **No credible counterfactual group:** redesign the identification strategy; changing estimators cannot repair the missing comparison.

## Diagnostics and sensitivity plan

Plan diagnostics as evidence about assumptions, not proof:

- cohort-by-time treatment and sample-size table;
- pre-treatment outcome paths and group-time pre-treatment pseudo-effects;
- event-time estimates with simultaneous uncertainty where supported;
- alternative defensible comparison groups, windows, and aggregation rules;
- placebo periods or outcomes and negative controls when design-justified;
- overlap and weight diagnostics when using covariate adjustment;
- sensitivity to plausible violations of parallel trends and to functional-form choices such as levels versus logs.

A non-significant pre-trend test does not establish parallel trends. A visible pre-trend, contaminated comparison group, severe lack of overlap, or coincident shock is an identification problem, not a standard-error problem.

## Stage 03 output and Stage 04 handoff

Return a compact CSDID design brief containing:

- the causal question and claim boundary;
- unit, outcome, treatment, cohort/timing variables, panel or repeated-cross-section status;
- `ATT(g,t)` definition and planned aggregation(s);
- comparison-group choice with rationale;
- identification assumptions and threat-to-diagnostic table;
- clustering/inference rationale and sparse-cohort concerns;
- a cohort-time diagram showing valid comparison cells and the target post-treatment cells;
- the locked handoff to `causal-did-iv.md`, including any requested R/Stata implementation route without executing it.
