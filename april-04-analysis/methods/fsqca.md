# APRIL — fsQCA (fuzzy-set Qualitative Comparative Analysis)

## When
Configurational, set-theoretic questions: which **combinations of conditions** are necessary and/or sufficient for an outcome; equifinality; asymmetric causality. Typical medium-N case designs (often ~10–50+, not a hard rule). Prefer fsQCA when conditions/outcomes are graded (calibrated into fuzzy membership), not only crisp 0/1.

## Not this card
- Pure regression / SEM net-effects framing → use those cards instead (or mixed-methods design under april-03).
- Crisp-set QCA (csQCA) or multi-value QCA (mvQCA): same workflow spirit; note crisp/mv calibration explicitly if used.
- Large-N “QCA-labelled regression” without calibration, necessity, and truth-table logic — reject as misuse.

## Steps
1. **Cases and outcome** — define the case, outcome set, and theoretically motivated conditions. Justify inclusion/exclusion; avoid dumping every available variable.
2. **Calibration** — map raw scores to fuzzy membership (0–1) with explicit anchors (full non-membership, crossover, full membership). Document thresholds and theory/empirics behind them. Report calibration tables.
3. **Necessity** — test single conditions (and theoretically justified compounds) for necessity; report consistency and coverage (and relevance/triviality checks when used). Do not skip necessity before sufficiency storytelling.
4. **Truth table** — construct configurations; set frequency and consistency cut-offs with justification; handle contradictory rows transparently.
5. **Logical minimisation** — derive complex / intermediate / parsimonious solutions as appropriate; state directional expectations for intermediate solutions; do not present only the most convenient solution.
6. **Interpretation** — read configurations as recipes (AND/OR/NOT), not as net coefficients. Name paths; link back to cases (typical/deviant); discuss equifinality and asymmetry (presence vs absence of outcome).
7. **Robustness** — sensitivity to calibration anchors, consistency/frequency thresholds, and (where relevant) case drops; report what holds.
8. **Findings prose** — consistency/coverage for necessity and for solution terms; configuration notation explained for readers unfamiliar with QCA; limitations (calibration discretion, limited diversity, generalisation).

## Reporting checklist
- [ ] Calibration rules and anchors stated
- [ ] Necessity results before/alongside sufficiency
- [ ] Truth-table parameters justified
- [ ] Solution type(s) named; raw/unique coverage and consistency for terms
- [ ] Case narrative for key configurations
- [ ] Robustness / limited diversity discussed honestly

## Stack
R (`QCA`, `SetMethods`), fs/QCA software, or Python QCA tooling the user already uses. Prefer reproducible scripts that regenerate truth tables and solution objects.

## Hand-off
Style with `april-08-language`; tables/figures via `april-09-formatting`. If the paper also runs regression as a complement, treat that as a **separate** april-04 pass with the regression/multilevel card—do not collapse both into one card.
