# APRIL - Causal design and identification

## When

Use this single causal method card when the research question asks what an intervention, exposure, policy, threshold, assignment rule, or event causes. It covers the design modules most often needed in Stage 04: randomized and observational assignment, matching/weighting, regression discontinuity (RDD), panel and fixed-effects designs, difference-in-differences (DiD), instrumental variables (IV), and synthetic control.

This is one substantive causal card with design-specific modules, not a reason to run every module. Select the module that matches the assignment process and estimand. A regression, fixed effect, matching algorithm, or significant coefficient does not by itself identify a causal effect.

## Causal reasoning before estimation

### 1. Define the intervention and estimand

Write an estimand before choosing an estimator. Record:

- unit, treatment or exposure, treatment versions/dose, outcome, time zero, follow-up horizon, target population, and comparison or counterfactual;
- whether the target is an average treatment effect (ATE), average treatment effect on the treated (ATT), group-time ATT, conditional effect, local effect (such as an IV or RDD LATE), intent-to-treat effect, or an association/prediction target;
- the effect scale (raw units, standardized units, risk/probability, rate, odds, log scale, or other contrast), treatment timing, and aggregation rule;
- planned, secondary, and exploratory status, including any subgroup or moderator target.

Use potential-outcome notation when it clarifies the question: the causal effect compares the same unit's outcome under the observed intervention with the outcome under the relevant counterfactual. The latter is not observed directly, so the design must make the comparison credible.

### 2. Draw the causal structure and assignment timeline

Create a compact DAG or equivalent treatment-timing diagram before fitting the model. Mark pre-treatment confounders, mediators, colliders, post-treatment variables, selection/attrition, clusters, and possible spillovers. Use a theory- and institutional-justified adjustment set; do not adjust for a collider or mediator merely because it predicts the outcome. A DAG is a design aid, not proof that the graph is correct.

Record which assumptions are design/identification assumptions and which are model or measurement assumptions. Label diagnostics as informative rather than conclusive: balance, pre-trends, density tests, placebo cutoffs, and first-stage strength can expose problems but cannot prove all causal assumptions.

### 3. State the common causal contract

1. **Consistency/SUTVA:** the observed outcome corresponds to the assigned treatment version, and the no-interference/no-spillover condition is plausible for the target. If treatment versions or interference matter, redefine the estimand or model them explicitly.
2. **Assignment/identification:** state the exchangeability, randomization, continuity, parallel-trends, exclusion, or other assumption that links the observed comparison to the counterfactual.
3. **Overlap/positivity:** each target unit has a credible chance of receiving each relevant treatment level or comparison; report common support and sparse cells.
4. **Timing and composition:** treatment is not anticipated, outcomes are measured after treatment as specified, and changes in sample composition, attrition, or exposure do not silently change the target.
5. **Inference:** match standard errors or resampling to the assignment and dependence structure (clusters, repeated units, few treated groups, spatial/temporal dependence, or randomization).

Do not call an estimate causal when these conditions are only asserted. If the design cannot support the requested causal estimand, report an association or descriptive contrast and identify what additional information would be needed.

## Design routing modules

### Randomized assignment and randomization inference

- Verify the assignment rule, unit of randomization, treatment compliance, attrition, interference, and whether the analysis is intent-to-treat, treatment-on-the-treated, or another target.
- Use baseline balance as a diagnostic, not a gatekeeper for randomization. Report the assignment mechanism, exclusions, missing outcomes, protocol deviations, and the uncertainty procedure.
- For small or clustered experiments, consider randomization-based or cluster-aware inference. Do not recover a population effect beyond the randomized target without a transportability argument.

### Matching, subclassification, and weighting

- Use only when selection on the measured pre-treatment covariates is substantively defensible and overlap is adequate. Matching changes the comparison set; it does not remove unmeasured confounding.
- Define the target population and estimand before fitting a propensity or distance model. Show covariate balance, common support, weights/effective sample size, discarded observations, and sensitivity to defensible specifications.
- Do not select covariates or the method by outcome significance. Never include post-treatment variables or colliders in the adjustment set.

### Regression discontinuity (sharp or fuzzy)

- Define the running variable, cutoff, treatment rule, bandwidth, and local estimand. A sharp RDD has deterministic assignment at the threshold; a fuzzy RDD is an IV design whose effect is local to compliers at the cutoff.
- Defend continuity of untreated potential outcomes at the cutoff, absence of precise manipulation or sorting, no anticipatory treatment, and no other discontinuous change at the threshold. Check density/manipulation, covariate continuity, mass points, bandwidth sensitivity, and placebo cutoffs where meaningful.
- Prefer a transparent local specification with justified bandwidth and bias/variance trade-off. Avoid high-order polynomials chosen to fit the preferred result. Report the local sample, effective observations on each side, treatment jump/first stage for a fuzzy design, and the restricted population to which the effect applies.

### Panel and fixed-effects designs

- State whether the target is within-unit change, between-unit difference, or a population-average effect. Unit fixed effects remove time-invariant additive differences; they do not remove time-varying confounding, reverse causality, anticipation, or spillovers.
- Specify time effects, treatment timing, lags/leads, missing panels, composition, and clustering. Do not describe a fixed-effects coefficient as causal without an assignment or comparison argument.
- Check serial correlation, few-cluster inference, treatment variation after fixed effects, and whether the transformation changes the target population.

### Difference-in-differences

- For two-period designs, define the treated and comparison groups, pre/post windows, treatment timing, and the counterfactual parallel-trends claim. For staggered adoption, prefer interpretable group-time effects or another estimator that handles heterogeneous effects rather than treating a default two-way fixed-effects coefficient as the target.
- State no anticipation, no differential spillovers, credible comparison units, stable measurement/composition, treatment reversals or repeated treatments, and any conditional adjustment used to make trends comparable.
- Use event-time estimates, pre-period plots, negative-control/placebo periods, alternative windows, and design-justified comparison groups as diagnostics. Pre-treatment coefficients or a non-significant pre-trend test do not prove parallel trends; post-treatment event-study coefficients must be interpreted with the estimator's weighting and dynamic-effect assumptions.
- Report group-time effects, aggregation weights, cluster level/count, and uncertainty appropriate to the number of treated units and time periods. Treat a failed pre-trend or contaminated comparison as an identification problem, not something a different standard error can repair.

### Instrumental variables

- Define the instrument, treatment, outcome, population, first-stage variation, and the target complier population. Defend relevance, independence/exogeneity, exclusion (no outcome path other than through treatment), and monotonicity when interpreting a LATE.
- Report the first stage, reduced form, second-stage/2SLS result, weak-instrument-robust diagnostics when warranted, instrument construction, and any sample loss. A strong first stage does not establish independence or exclusion; overidentification tests do not prove them.
- Interpret the estimate as a local average effect for compliers unless stronger assumptions support a broader effect. Explain who the compliers plausibly are and whether the sign/monotonicity story is credible. For a fuzzy RDD, apply the same IV logic locally at the cutoff.

### Synthetic control and comparative case designs

- Define the treated case, intervention date, donor pool, outcome path, and local comparative-case estimand. Donors must not be exposed to the intervention or a closely related shock during the relevant period.
- Show pre-treatment fit and justify predictor/outcome windows. Examine placebo or permutation distributions, in-time/placebo interventions, leave-one-donor-out sensitivity, donor-weight concentration, and other shocks that coincide with treatment.
- Keep the claim local to the case and design. Good pre-treatment fit is necessary but does not prove that the post-treatment counterfactual is correct.

## Baseline, heterogeneity, and robustness

Treat the baseline as the primary specification tied to the causal estimand, not the simplest or most favorable regression. Freeze treatment coding, sample, covariates, timing, comparison group, fixed effects, weights, bandwidth/donor pool, and variance estimator before reading focal results when feasible.

For heterogeneity:

- define a subgroup or moderator estimand and its mechanism or design rationale in advance;
- estimate pooled interactions or design-compatible group-time/local effects, and compare contrasts directly rather than comparing separate p values;
- report subgroup N, overlap, treatment variation, and multiplicity; label data-discovered splits as exploratory;
- check whether the design identifies the subgroup effect (for example, local RDD/IV effects need not generalize across subgroups).

Build a threat-to-check matrix before robustness models. Choose checks that target plausible threats: alternative defensible treatment/outcome definitions, comparison groups, time windows, bandwidths, donor pools, covariate sets, functional forms, clustering, missingness/attrition, placebo or negative-control outcomes, pre-treatment periods, randomization/permutation inference, and sensitivity to hidden bias. Judge robustness by the estimand, magnitude, interval, and substantive conclusion—not by whether every p value crosses a threshold. No robustness check repairs an unidentified design.

## Minimum reporting package

Report, in a reproducible order:

1. the causal question, intervention, unit, target population, time horizon, counterfactual, estimand, and effect scale;
2. the assignment/institutional setting, treatment timing, sample construction, exclusions, missingness, attrition, and exposure versions;
3. a DAG or assignment/timing figure and a short assumption-to-diagnostic table;
4. the exact estimator and formula/specification, comparison group/donor pool/instrument/running variable as applicable, fixed effects/weights, clustering, and uncertainty procedure;
5. the baseline estimate with interval and sample, design-specific diagnostics, prespecified heterogeneity, and threat-linked robustness;
6. the strongest supported claim, local/population boundary, unresolved assumptions, and whether the result is causal, associative, descriptive, or predictive.

Generate figures that make the identification visible where relevant: treatment timing and event-study plots for DiD, first-stage/reduced-form or compliance plots for IV, cutoff and bandwidth plots for RDD, balance/overlap plots for matching, and pre-treatment fit/placebo plots for synthetic control. Keep tables and prose linked to saved analysis objects.

## Core references

Use `../references/method-citations.md` for source-to-claim routing. Cunningham (2021) supplies the design-first causal framework and a cross-design teaching synthesis; use the estimator-specific primary sources listed there for claims about DiD, IV, or other estimators. Do not copy source prose, and verify page-specific claims against the cited source.
