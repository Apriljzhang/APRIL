# APRIL - Causal designs (DiD and IV)

## When
The question names a causal estimand and the design supplies a defensible identification strategy. Adjustment alone is not identification.

## Shared contract
1. Define treatment, outcome, population, timing, horizon, and estimand before estimation.
2. State assumptions and distinguish testable diagnostics from inherently untestable identification claims.
3. Disclose exclusions, missingness, treatment timing, and outcome construction.
4. Report estimates with uncertainty, diagnostics, robustness checks, and assumption-linked limitations.

## Difference-in-differences
- With staggered adoption, estimate interpretable group-time effects rather than defaulting to one two-way fixed-effects coefficient.
- State comparison group, no anticipation, parallel trends, adjustment, overlap, and aggregation weights.
- Use event-time estimates appropriately. Pre-treatment coefficients may reveal problems but cannot prove parallel trends.

## Instrumental variables
- Defend relevance, independence, exclusion, and monotonicity.
- Report first stage and weak-instrument diagnostics; describe compliers and interpret LATE unless stronger assumptions support another estimand.
- A strong first stage does not validate exclusion or independence.

## Core references
Use `../references/method-citations.md`: Callaway and Sant'Anna (2021) for DiD and Imbens and Angrist (1994) for LATE.
