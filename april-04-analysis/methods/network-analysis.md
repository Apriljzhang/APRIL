# APRIL - Network analysis

## When
Relations among defined nodes are the research object. Distinguish social, citation, semantic, temporal, and psychological networks because their edges mean different things.

## Workflow
1. Define nodes, edge direction/weight/sign, time window, missing ties, sampling boundary, and the meaning of an absent edge.
2. Match estimation and regularization to network type and assumptions; report tuning, thresholding, and sensitivity.
3. Visualize with documented layout/scaling rules; visual position alone is not importance.
4. For psychological networks, bootstrap edge accuracy and use case-dropping procedures for centrality stability. Do not rank centrality when stability is inadequate.
5. For social/citation networks, address dependence, boundaries, and null/reference models before interpreting metrics.
6. Validate across plausible specifications. Cross-sectional conditional associations are not causal relations.

## Reporting
Provide network definition, preprocessing, estimator, tuning, uncertainty/stability, sensitivity, and reproducible edge/node data or code where ethical.

## Core references
Use `../references/method-citations.md`: Epskamp et al. (2018) for psychological-network accuracy; use a domain-specific source for other network families.
