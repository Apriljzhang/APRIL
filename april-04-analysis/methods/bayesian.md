# APRIL - Bayesian analysis

## When
Priors, posterior uncertainty, and predictive adequacy are the appropriate inferential frame.

## Workflow
1. Define the estimand, likelihood, link, hierarchy, and prior predictive implications before fitting.
2. Justify priors on the model scale; use prior predictive simulation to detect implausible implications.
3. Fit multiple chains and inspect rank/trace plots, rank-normalized split R-hat, bulk and tail ESS, divergences, treedepth, and sampler warnings. Do not declare convergence from R-hat alone.
4. Report posterior summaries and intervals on interpretable scales.
5. Target posterior predictive checks to substantively important data features; use mismatch for model criticism or expansion.
6. Test sensitivity to consequential priors and reasonable model alternatives.

## Reporting
State software/version, sampler, chains, iterations, warm-up, adaptation settings, seed, priors, diagnostics, posterior summaries, predictive checks, and sensitivity analyses.

## Core references
Use `../references/method-citations.md`: Gabry et al. (2019) for workflow and Vehtari et al. (2021) for R-hat and ESS.
