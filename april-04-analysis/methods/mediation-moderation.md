# APRIL — Mediation, moderation, and conditional process

## When
Use when the RQ concerns a proposed mechanism, an indirect effect, effect heterogeneity, or an interaction between predictors.

## Steps
1. Draw the causal or temporal ordering and define the total, direct, indirect, conditional, or interaction estimand before fitting models.
2. Check whether design, timing, theory, and data support mechanism language. Coefficient magnitude cannot repair weak causal identification, and statistical control cannot eliminate unknown confounding.
3. For mediation, state treatment-mediator, mediator-outcome, and confounding assumptions; address exposure-mediator interaction when relevant. Do not require a significant total X-Y association before testing an indirect effect.
4. Estimate indirect effects with bootstrap, Monte Carlo, or posterior intervals rather than relying on separate path significance. Report direct, indirect, and total effects in a clearly stated metric, preferably unstandardized when interpretable.
5. For moderation, specify the interaction scale and coding. Report the interaction term with uncertainty, then probe it using predicted values, simple slopes, contrasts, or Johnson–Neyman regions as appropriate.
6. Keep continuous moderators continuous unless categorization has a defensible substantive basis. Centre only to make zero interpretable or improve numerical stability, not as a ritual cure for multicollinearity.
7. Run sensitivity checks for alternative temporal order, omitted confounding, influential observations, and model form.
8. Present a path diagram or interaction plot that matches the fitted model and reported estimates.

## Do not
- Describe statistical mediation as a proven psychological or social mechanism.
- Infer subgroup effects from significance in one subgroup and nonsignificance in another; test the interaction directly.
- Use standardized effects involving a dichotomous X without explaining what the standardisation means and why it is useful.

## Core references
Use `../references/method-citations.md`: Hayes (2013) for regression-based conditional process analysis. Cross-route to `sem-cfa.md` when effects are estimated with latent variables.
