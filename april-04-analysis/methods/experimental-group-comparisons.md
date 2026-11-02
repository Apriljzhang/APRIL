# APRIL — Experimental and group comparisons

## When
Use for randomized or nonrandomized comparisons, factorial designs, repeated measures, ANCOVA/ANOVA-style questions, and intervention effects.

## Steps
1. Define the intervention, comparison, assignment mechanism, unit of assignment, unit of analysis, outcomes, time points, and causal estimand.
2. Preserve the actual design in analysis: randomisation, within- versus between-participant factors, factorial structure, counterbalancing, blocking, and the distinction between assignment and analysis units.
3. For randomized studies, preserve intention-to-treat as the primary analysis unless the protocol states otherwise; label per-protocol or as-treated analyses separately.
4. Account for clustering, blocking, stratification, repeated measures, baseline outcomes, and unequal allocation in the model and standard errors.
5. Report participant flow, exclusions, attrition, protocol deviations, fidelity, adherence, and adverse events when relevant.
6. Control multiplicity across outcomes, groups, time points, and post hoc contrasts. Distinguish planned contrasts from exploratory comparisons.
7. Report group summaries, effect estimates, confidence intervals, test statistics, degrees of freedom, and exact p values. Do not rely on omnibus p values alone.
8. For nonrandom assignment, describe the identification strategy and balance or adjustment diagnostics; use the causal-design card when DiD, IV, matching, or weighting is central.
9. Check sensitivity to missingness, influential cases, covariance assumptions, and alternative reasonable specifications.

## Do not
- Analyse repeated or clustered observations as independent.
- Equate statistical significance with practical or educational importance.
- Infer a group difference because one within-group test is significant and another is not; test the between-group contrast directly.

## nparLD: nonparametric factorial repeated measures

Use this within-family option for ordered continuous, ordinal or binary outcomes (including ties), crossed categorical between-/within-subject factors and independent subjects with dependent repeated observations. It avoids normality/sphericity assumptions, but still needs an appropriate design, estimable contrasts and adequate independent subjects; no universal minimum sample size guarantees validity. It does not establish causality or make parametric ordinal models inappropriate.

Read the [current CRAN documentation](https://cran.r-project.org/package=nparLD), [vignette](https://cran.r-project.org/web/packages/nparLD/vignettes/nparLD.html) and [manual](https://cran.r-project.org/web/packages/nparLD/nparLD.pdf) before implementation. The interface below was checked against version **2.3.3 (14 October 2026)**; record the actual installed version and recheck later changes. Use Noguchi et al. (2012) in the [citation registry](../references/method-citations.md) for the original methodology, not as documentation of the redesigned API.

- **Design and data:** map `y ~ time`, `y ~ group * time`, `y ~ time1 * time2`, `y ~ group * time1 * time2` or `y ~ group1 * group2 * time` to the actual factors and subject identifier. RHS variables become factors: adding numeric age/baseline does not provide continuous covariate adjustment. Keep planned subject-by-condition rows with `NA` outcomes and valid factor values; investigate unintended duplicate rows. Genuine dependent replicates require `replicate` and an explicit choice of subject- versus observation-weighting through `cell.weights`. Documented missing-outcome validity assumes MCAR, not arbitrary MAR/MNAR; assess missingness and sensitivity.
- **Estimand:** explicitly choose `hypothesis = "H0F"` for marginal-distribution contrasts or `hypothesis = "H0p"` for contrasts of unweighted relative marginal effects. With `effect = "unweighted"`, pseudo-ranks target `p_j = P(Z < X_j) + 0.5 P(Z = X_j)`, where the reference Z mixes factorial cells equally. Values above .5 indicate relatively larger outcomes, not necessarily better ones. This is not a mean/median difference, individual improvement probability or generally direct treatment-versus-control superiority. Ordinary-rank weighted effects depend on sample allocation.
- **Inference:** prespecify the primary statistic. An approximate-F ATS is generally preferable for modest samples; the asymptotic chi-square WTS can calibrate poorly. Neither is exact; do not select whichever is significant. The historical modified ATS's finite denominator applies to pure between-subject effects, not automatically time or interactions. Two-wave group-by-time comparisons are eligible, but do not imply nonlinear trajectories or covariate-adjusted raw-change effects.
- **Follow-up:** define the comparison family and multiplicity adjustment; inspect `nparLD::MCTP(fit_contrasts)` and `nparLD::contrastMatrix(fit_contrasts)` for a model fitted with the chosen `contrast`. For example, `contrast = list("group:time")` uses that term's hypothesis structure; do not automatically label it all simple effects. Marginal time contrasts are not group-specific changes. Report simultaneous intervals where supported; historical subset-refit posthocs change the relative-effect reference.
- **Permutation:** keep `perm.test = FALSE` for the factorial scaffold. The current option requires complete paired observations on one two-level within-subject factor; it is not a group-by-time permutation test.

Documentation-checked scaffold, **not executed**; use only after validating `dat`, with `group` a factor and `time` a factor whose explicit levels are `c("baseline", "followup")`:

```r
stopifnot(utils::packageVersion("nparLD") >= "2.3.3")
fit <- nparLD::nparLD(
  outcome ~ group * time, data = dat, subject = "id",
  effect = "unweighted", hypothesis = "H0p",
  Factor.Information = TRUE, covariance = TRUE, perm.test = FALSE
)
nparLD::ATS(fit)
nparLD::WTS(fit)
stats::effects(fit)
summary(fit)
```

Report design/cell and subject counts, factor ordering, missingness/replicate handling, hypothesis and reference distribution, package version, chosen statistic/df/p values, relative effects/intervals and adjusted contrast family. Do not report fitted results before verified execution.

**Legacy examples:** the [2012 paper and resources](https://www.jstatsoft.org/article/view/v050i12) remain useful, but `ld.f1`/`ld.f2`/`f1.ld.f1`/`f1.ld.f2`/`f2.ld.f1` and `description = FALSE` are legacy API. Do not run the [historical script](https://www.jstatsoft.org/article/download/v050i12/2536) unchanged: two dental mixed-model comparisons reuse `m810` instead of `m812`/`m814`, and the respiration plot uses `center` without defining it there. Check against the paper/current documentation; do not copy these errors.

## JARS
Use JARS–Quant Table 1 plus Table 2 and Module A or B; add Module C for clinical trials and Table 4 for longitudinal follow-up.

## Core references
Use `../references/method-citations.md`: Shadish et al. (2002) for causal-design logic and the local Field/Hole or Harris text for implementation and reporting.
