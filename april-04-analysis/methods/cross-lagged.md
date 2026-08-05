# APRIL - Cross-lagged panel models (CLPM and RI-CLPM)

## When
Repeated measures address temporal ordering or reciprocal within-person dynamics. Lagged paths alone do not establish causality.

## Workflow
1. Define waves, process timescale, lag spacing, within-person question, and covariates.
2. Establish longitudinal measurement comparability before interpreting latent change or lagged paths.
3. Recognize that conventional CLPM mixes stable between-person differences with within-person fluctuations. Prefer RI-CLPM for person-centered dynamics; it generally requires at least three waves.
4. Specify autoregressive, cross-lagged, contemporaneous residual, and random-intercept components. Test equality/stationarity constraints rather than assuming them.
5. Compare defensible alternatives and inspect fit, residuals, uncertainty, and sensitivity to lag specification.
6. Report unstandardized and clearly defined standardized effects with intervals and a matching diagram.

## Do not
- Interpret a between-person CLPM coefficient as a within-person process.
- Call a variable causal because its lagged path is significant.
- Choose wave spacing only for convenience.

## Core references
Use `../references/method-citations.md`: Hamaker et al. (2015).
