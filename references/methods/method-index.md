# APRIL method taxonomy and index

Use two routing levels: **primary approach** describes the evidence logic; **analytical family** groups methods that answer related kinds of questions. These labels organise workflow and do not erase legitimate cross-paradigm features.

## Contents
1. Selection sequence
2. Quantitative
3. Qualitative
4. Mixed, integrative, and cross-paradigm
5. Configurational and computational
6. Support and reproducibility
7. Boundary and cross-route rules

## Selection sequence
1. Classify the RQ and intended claim under a primary approach.
2. Select the analytical family from the data structure, estimand, and design.
3. Open the primary card under `../../april-04-analysis/methods/`. Read `../../april-04-analysis/references/analysis-contract.md` before execution.
4. Add support cards or modules only when needed. For genuinely distinct methods, specify and validate each analysis separately and state the integration point.

## Quantitative

### Variable-centred, comparative, and multilevel models

| Goal | Card |
|---|---|
| Linear, logistic, ordinal, count, or rate regression | `regression-glm.md` |
| Experimental, quasi-experimental, factorial, repeated, or group comparisons | `experimental-group-comparisons.md` |
| Mediation, moderation, interaction, or conditional process | `mediation-moderation.md` |
| Nested, repeated, crossed, multilevel, or panel regression | `multilevel-regression.md` |

### Latent-variable and person-centred models

| Goal | Card |
|---|---|
| CFA, latent measurement, or structural equation model | `sem-cfa.md` |
| Classes from categorical/ordinal indicator patterns | `latent-class-lca.md` |
| Profiles from continuous indicator patterns | `latent-profile-lpa.md` |

### Longitudinal, sequential, forecasting, and causal models

| Goal | Card |
|---|---|
| CLPM or RI-CLPM for reciprocal longitudinal relations | `cross-lagged.md` |
| Time series, interventions in series, or forecasting | `time-series.md` |
| Ordered behavioural-event transitions or contingencies | `lag-sequential.md` |
| Causal design and identification (DiD, IV, RDD, matching, panel, synthetic control) | `causal-did-iv.md` |

### Inferential framework

| Goal | Card |
|---|---|
| Bayesian estimation, prior/posterior workflow, or predictive checking | `bayesian.md` |

Bayesian analysis is a cross-cutting inferential framework. Pair it with a substantive model family when the likelihood or design requires another card.

## Qualitative

### Interpretive coding and thematic analysis

| Goal | Card |
|---|---|
| Braun and Clarke reflexive thematic analysis | `qualitative-rta.md` |
| General qualitative coding, categorising, matrices, or pattern analysis | `qualitative-coding-analysis.md` |

### Ethnographic inquiry

| Goal | Card |
|---|---|
| Online/virtual ethnography of practices, communities, or platforms | `online-virtual-ethnography.md` |

Do not force grounded theory, IPA, conversation analysis, narrative inquiry, or critical discourse analysis into the generic coding card; redesign and add the proper method route first.

## Mixed, integrative, and cross-paradigm

| Analytical family | Goal | Card |
|---|---|---|
| Mixed-methods integration | Integrate quantitative and qualitative strands and produce meta-inferences | `mixed-methods-integration.md` |
| Q methodology | Identify and interpret shared viewpoints using Q sorts and by-person factor analysis | `q-methodology.md` |
| Corpus-assisted discourse | Integrate corpus patterns, concordance evidence, and contextual discourse interpretation | `corpus-assisted-discourse-analysis.md` |
| Evidence synthesis | Quantitative meta-analysis, qualitative synthesis, scoping/systematic review, or mixed synthesis | `evidence-synthesis.md` |

Name the strand or synthesis subtype explicitly. Coexistence of numerical and textual outputs is not integration by itself.

## Configurational and computational

| Analytical family | Goal | Card |
|---|---|---|
| Set-theoretic/configurational | Necessity, sufficiency, equifinality, and asymmetric configurations | `fsqca.md` |
| Network/computational | Network estimation, bridge analysis, or two-network comparison/NCT | `network-analysis.md` |
| Computational text analysis | LDA, STM, BERTopic/embedding-based topic models, and related validation | `topic-modeling.md` |

These methods often use quantitative estimation, but their research objects and inferential logic differ from standard variable-centred regression. Topic and network outputs still require substantive interpretation; fsQCA configurations are not net effects.

## Support and reproducibility

| Role | Card |
|---|---|
| Power, sensitivity, precision, or sample-size planning | `power-analysis.md` |
| Reproducible implementation in Stata, R, or Python | `tooling-stata-r-python.md` |

Support cards do not define the substantive method.

## Boundary and cross-route rules
- Keep observed-variable mediation/moderation distinct from latent-variable SEM; use both cards when the analysis genuinely combines them.
- Keep LCA and LPA separate according to indicator type; do not use generic clustering as an unacknowledged substitute.
- Use network analysis only when relations among nodes are the research object; use regression/SEM when directional effects or latent constructs are primary.
- Use topic modelling for computational lexical structure, corpus-assisted discourse for iterative quantitative-contextual discourse analysis, and qualitative coding for interpretive coding without a topic model.
- Treat fsQCA and regression/SEM as distinct configurational and net-effect analyses. If both are justified, execute them separately and integrate conclusions explicitly.
- Route each evidence-synthesis subtype to its own standards and estimands; do not blend meta-analysis, qualitative synthesis, and scoping review procedures.

If the needed method has no card, for example survival/event-history analysis, identify the missing route rather than forcing the problem into the nearest family.
