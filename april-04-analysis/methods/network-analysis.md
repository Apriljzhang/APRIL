# APRIL - Network analysis

## When
Use when relations among defined nodes are the research object. Distinguish social, citation, semantic, temporal, and psychological networks because their edges have different meanings. For cross-sectional psychological networks, treat edges as model-dependent conditional associations, not temporal or causal effects.

## Choose the module from the RQ
1. Use **network estimation** to describe one network's edges, uncertainty, node metrics, and optional predictability.
2. Add **bridge analysis** only when nodes belong to defensible communities or dimensions and the RQ concerns cross-community connectivity.
3. Add **network comparison** only when the RQ compares two commensurable networks or groups. Do not run bridge analysis or NCT merely because software makes them available.

Keep these as conditional modules within one substantive network-analysis card. Label unplanned modules exploratory.

## Design gate
1. Define nodes, edge direction/weight/sign, sampling boundary, time window, missing ties or values, and the meaning of an absent edge.
2. Match the model to node type and design: for example, a Gaussian graphical model for suitable continuous nodes, an Ising model for binary nodes, or a mixed graphical model for mixed node types. Justify ordinal handling rather than treating categories as continuous automatically.
3. Document item overlap, redundant nodes, restricted variance, floor/ceiling effects, transformations, missing-data handling, and whether the same variables are measured comparably across groups.
4. Predefine the estimator, tuning or regularisation, correlation/input matrix, thresholding, and sensitivity specifications. Do not choose the visually cleanest network.
5. Separate cross-sectional between-person networks from within-person temporal networks. Route a temporal estimand to the appropriate longitudinal/time-series method instead of giving a cross-sectional graph a dynamic interpretation.

## Module A - Network estimation
1. Estimate the network with the declared model and record software/package versions, seed, estimator, tuning, and all nondefault settings.
2. Export the weighted edge matrix and an edge table with node pair, sign, weight, and uncertainty or selection-frequency information where available.
3. Visualise the network with documented layout, edge-width, sign/colour, threshold, and node-order rules. Visual position alone is not evidence of importance.
4. Assess edge-weight accuracy with method-appropriate bootstrap intervals or resampling. Use case-dropping bootstrap procedures for the stability of centrality orders when applicable; do not rank unstable metrics.
5. Select centrality metrics from a substantive process model. In signed networks, distinguish strength, which sums absolute edge weights, from expected influence, which retains signs. Do not routinely interpret closeness or betweenness without a defensible flow and shortest-path account.
6. Report nodewise predictability only when it answers the RQ and the fitted model supports it. Use an outcome-appropriate metric, such as explained variance for continuous nodes or accuracy plus a marginal/baseline-adjusted measure for categorical nodes. Predictability is not centrality and does not identify a causal intervention target.
7. Run sensitivity analyses across plausible estimators, tuning choices, transformations, missing-data decisions, and redundant-node decisions. Interpret isolated edges and rank order cautiously when conclusions change.

## Module B - Bridge analysis
1. Define and justify community membership before computing bridge statistics. Report every node-to-community assignment. If communities are data-derived, describe the detection method, label the analysis exploratory, and assess assignment stability.
2. Use bridge strength for the absolute magnitude of cross-community connections. Use bridge expected influence when edge signs matter; state whether one-step or two-step expected influence is reported.
3. Avoid bridge closeness and bridge betweenness when negative edges are present or when shortest-path/flow assumptions are not substantively defensible.
4. Assess robustness to plausible community definitions, estimation choices, and sampling variation. Do not call the top-ranked bridge node a mechanism, treatment target, or cause without separate evidence.
5. Output a bridge-metric table, a bridge plot with uncertainty/stability information where available, and a cross-community edge table. Explain whether a high score reflects many small edges, a few strong edges, or signed cancellation.

## Module C - Network comparison
1. Verify identical node definitions, order, coding, measurement quality, and defensible group or occasion comparability before testing. Distinguish independent groups from paired/repeated samples.
2. Treat the Network Comparison Test as a two-network permutation procedure. For more than two groups, predefine justified pairwise comparisons with multiplicity control or use a method that supports the required omnibus question; do not describe multiple pairwise NCTs as one omnibus test.
3. Use the same estimator and settings across networks. Record the number of permutations and seed; use enough permutations for the desired p-value resolution and do not rely on demonstration-level runs.
4. Report the network-structure invariance statistic (maximum edge difference), global-strength values and their difference, and the corresponding permutation p values.
5. Test individual edges or node/bridge centralities only when prespecified or clearly exploratory. Name the tested set and multiplicity adjustment. Restrict centrality comparisons to interpretable, sufficiently stable metrics.
6. Do not infer network equality from a nonsignificant test. Discuss sample size, group imbalance, estimation accuracy, power, and confidence limits or sensitivity evidence.
7. Compare group plots with identical node placement, edge scaling, signs, and legends. Never infer a difference by visually comparing independently auto-scaled graphs.

## Reporting package
- **Table 1:** node definitions, scales, missingness, sample/group sizes, and community assignments when relevant.
- **Table 2:** edge-weight matrix or focal edge table with uncertainty/accuracy information.
- **Table 3:** centrality and predictability metrics with stability evidence; omit unsupported rankings.
- **Table 4:** bridge results and/or NCT statistics, multiplicity decisions, and sensitivity checks when those modules answer the RQ.
- **Figures:** one-network plot, bridge plot, and/or aligned comparison panels, each with a self-contained caption and accessible encodings.
- **Prose:** describe the estimand, estimator, uncertainty, magnitude, stability, and claim boundary. Say “more strongly connected in the estimated network” rather than “more important” unless importance is operationally defined.

## Do not
- Infer causality, temporal activation, symptom spread, or intervention effects from cross-sectional edges, centrality, bridge scores, or predictability.
- Treat a zero regularised edge as proof of no population relation.
- Compare groups from separate edge-presence decisions, centrality ranks, or visual inspection alone.
- Report every available centrality index without a substantive rationale and stability evidence.

## Core references
Use `../references/method-citations.md`: Epskamp and Fried (2018) for regularised partial-correlation estimation; Epskamp et al. (2018) for edge accuracy and centrality stability; Burger et al. (2023) for cross-sectional network reporting; Haslbeck and Waldorp (2018) for predictability; Bringmann et al. (2019) for centrality interpretation; Jones et al. (2021) for bridge centrality; and van Borkulo et al. (2023) for NCT. Use current package documentation only for implementation details.
