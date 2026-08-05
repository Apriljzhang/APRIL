# APRIL - Latent profile analysis

## When
Continuous indicators are modeled as arising from unobserved profiles. Keep LPA distinct from categorical-indicator LCA.

## Workflow
1. Justify indicators, scaling, distributional assumptions, outliers, sample size, and missingness.
2. Predefine plausible within-profile variance/covariance structures; do not search only across K.
3. Fit 1-through-K models with many random starts and verify the replicated optimum.
4. Weigh BIC/aBIC, available likelihood-ratio tests, profile size, stability, separation, and interpretability. Entropy alone must not select K.
5. Name profiles descriptively from patterns and uncertainty; avoid treating them as immutable person types.
6. Validate across starts, seeds, nearby covariance structures, preprocessing, and preferably a new sample.
7. Preserve classification uncertainty for predictors/distals with one-step or corrected three-step methods.

## Multilevel extension
Specify profiles at each level and whether the cluster count supports the model. Clustered standard errors alone are not multilevel LPA.

## Core references
Use `../references/method-citations.md`: Spurk et al. (2020), with Nylund et al. (2007) only for applicable mixture-enumeration evidence.
