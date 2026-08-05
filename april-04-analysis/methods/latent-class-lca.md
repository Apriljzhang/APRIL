# APRIL - Latent class analysis

## When
Categorical or ordinal indicators define a finite-mixture model of response-pattern classes. Use LPA for continuous indicators.

## Workflow
1. Justify indicators, coding, sample size, missingness, and local-independence assumptions.
2. Fit a planned 1-through-K sequence with many random starts; confirm replication of the best log likelihood and inspect boundaries.
3. Weigh BIC/aBIC, valid likelihood-ratio tests, class size, stability, item-response separation, and usefulness together. Entropy is not an enumeration criterion by itself.
4. Inspect bivariate residuals/local dependence and revise only with substantive justification.
5. Characterize classes from item-response probabilities before naming them; do not reify sample-dependent classes.
6. Preserve classification uncertainty for covariates and distal outcomes with an appropriate one-step or corrected three-step method.

## Reporting
Report starts, convergence, fit table, proportions, item-response probabilities, classification diagnostics, local-dependence checks, sensitivities, and selection rationale.

## Core references
Use `../references/method-citations.md`: Nylund et al. (2007).
