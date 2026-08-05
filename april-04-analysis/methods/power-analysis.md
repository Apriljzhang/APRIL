# APRIL - Power, sensitivity, and precision planning

## Role
Support card only. Use with the substantive analysis card when planning or explaining sample size; do not treat power analysis as the study's analytic method.

## Steps
1. Select the intended statistical test and primary estimand before choosing a power procedure.
2. State whether the analysis is a priori, sensitivity, criterion, compromise, or post hoc, and why that mode answers the planning question.
3. Record alpha, target power, effect-size metric and value, allocation ratio, sidedness, predictors/groups, dependence assumptions, and any design effect.
4. Derive effect-size assumptions from the closest credible prior evidence, a smallest effect of interest, or a justified range. Do not default silently to generic small/medium/large labels.
5. Report the software and version, procedure/test family, all inputs, required sample size, and the achieved power after integer rounding.
6. For an attained sample, prefer sensitivity analysis and confidence-interval precision over retrospective observed-power claims.
7. Run scenario checks across plausible effect sizes, attrition, clustering, imbalance, and multiplicity when these could change feasibility.

## Do not
- Choose the test after seeing which option produces the smallest required sample.
- Use observed power as evidence that a nonsignificant result is trustworthy.
- Ignore attrition, clustering, repeated measures, unequal allocation, or model complexity present in the actual design.

## Core references
Use `../references/method-citations.md`: Faul et al. (2009) for G*Power procedures, not as the sole justification for an assumed effect size.
