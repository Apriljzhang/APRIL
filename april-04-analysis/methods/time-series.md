# APRIL - Time series and forecasting

## When
Chronological dependence, dynamics, intervention effects, or future prediction are substantive.

## Workflow
1. Define frequency, timestamp integrity, gaps, revisions, aggregation, interventions, seasonality, horizon, and target.
2. Plot the series and transformations. Treat stationarity tests as evidence, not automatic instructions to difference.
3. Prevent leakage with chronological, rolling-origin, or blocked validation; compare transparent naive/seasonal-naive benchmarks.
4. Match ARIMA, ETS, dynamic regression, VAR/VECM, state-space, or alternatives to the estimand; justify lags and deterministic terms.
5. Diagnose residual autocorrelation, distribution, heteroskedasticity, parameter stability, and influential periods. State VAR/VECM identification choices.
6. Evaluate point and interval forecasts with scale-appropriate metrics, coverage, and sensitivity across windows/specifications.

## Reporting
Report windows, horizon, benchmark, preprocessing, selection, diagnostics, accuracy, intervals, software/version, and code.

## Core references
Use `../references/method-citations.md`: Petropoulos et al. (2022).
