# APRIL — Topic modeling

## When
Large text corpora; topical structure; optional covariate effects on prevalence (STM).

## Steps
1. Choose STM (covariates), LDA (large, no covariates), or BERTopic (short/multilingual embeddings).
2. Document preprocessing (not neutral): lowercasing, stopwords, rare-term thresholds.
3. Select K with coherence/exclusivity (and STM diagnostics).
4. Interpret with exemplars; topics ≠ attitudes.
5. Robustness: seeds, preprocessing variants.
6. Report model choice, K, covariates, and limitations in Findings/Methods.

## Stack
R `stm`; Python gensim / BERTopic as appropriate.
