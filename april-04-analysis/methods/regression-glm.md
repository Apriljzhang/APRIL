# APRIL — Regression and generalized linear models

## When
Use for continuous, binary, ordinal, count, or rate outcomes when the RQ concerns adjusted association, prediction, or group differences. Use the multilevel card when dependence requires random effects or another hierarchical model.

## Steps
1. Define the outcome, focal predictors, covariates, estimand, unit of analysis, and whether the goal is explanation, prediction, or description.
2. Match model family and link to the outcome: linear, logistic, ordinal, Poisson, negative binomial, or another justified GLM.
3. Justify covariates from theory or a causal model; do not select them only by univariable significance or automated stepwise procedures.
4. Predefine coding, reference categories, transformations, nonlinear terms, and interactions. Centre variables only for a clear interpretive or numerical reason.
5. Diagnose functional form, influential observations, collinearity, residual structure, heteroskedasticity, overdispersion, separation, and dependence as applicable.
6. Address missing data and exclusions transparently; compare complete-case and principled missing-data approaches when consequential.
7. Report coefficients on interpretable scales with confidence intervals and model fit. Add predicted values, marginal effects, or contrasts when raw coefficients are hard to interpret.
8. Report the test statistic, degrees of freedom when applicable, exact p value, effect magnitude, and uncertainty; distinguish statistical significance from substantive importance.
9. Separate confirmatory and exploratory models and limit researcher degrees of freedom.

## Do not
- Call adjusted association causal without a defensible identification strategy.
- Interpret a nonsignificant coefficient as proof of no effect.
- Compare coefficient size across differently scaled variables or nonlinear models without an appropriate transformation or estimand.
- Treat a large sample's small p value as evidence that an effect is educationally important, or a small sample's nonsignificance as evidence of no meaningful effect.

## Core references
Use `../references/method-citations.md`: Fox (2016) for general regression/GLM specification and diagnostics, plus a model-family source for specialized estimators.
