# APRIL - Multilevel, mixed, and panel regression

## When
Observations are nested, repeated, crossed, or otherwise dependent and effects must be defined at explicit levels.

## Workflow
1. Define levels, cluster count/size, time metric, outcome distribution, and within- or between-cluster estimand.
2. Report ICC/variance partitioning when useful; low ICC does not automatically remove dependence concerns.
3. Separate within and between effects. Group-mean centering plus the cluster mean usually makes this explicit; grand-mean centering changes interpretation but does not isolate within effects.
4. Build fixed and random effects from design/theory; consider random slopes and report covariance/estimation issues.
5. Diagnose residuals, influential clusters, singular fits, missingness, and sensitivity to covariance or degrees-of-freedom choices.
6. For panels, distinguish unit fixed effects, random effects, time effects, and dynamics.

## Reporting
Report software/estimator, level-specific N, centering, fixed/random effects with intervals, variance components, ICC, comparisons, and diagnostics.

## Core references
Use `../references/method-citations.md`: Enders and Tofighi (2007).
