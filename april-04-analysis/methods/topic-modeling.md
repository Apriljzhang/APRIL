# APRIL - Topic modeling

## When
A sufficiently large text corpus is analyzed for lexical themes, with inferential target and document unit stated explicitly.

## Workflow
1. Define documents, language, sampling, metadata, deduplication, exclusions, and whether the goal is discovery, description, prediction, or covariate association.
2. Choose LDA for a generative bag-of-words mixture, STM for prevalence/content covariates, or embeddings when semantic representation and short/multilingual text justify them.
3. Treat preprocessing as modeling: record tokenization, case, stopwords, lemmatization, n-grams, thresholds, and retained vocabulary; test consequential alternatives.
4. Select K/specification using held-out performance, coherence, exclusivity/diversity, stability, and interpretability together. No single metric identifies true K.
5. Interpret from top words and representative documents with uncertainty and negative cases. Labels are analyst interpretations; topics are not attitudes or causal effects.
6. Validate across seeds, nearby K, preprocessing, and preferably external evidence. Report STM covariate uncertainty without causal language unless design supports it.

## Reporting
Report corpus construction, model/software, preprocessing, K evidence, stability, labels/exemplars, covariate analyses, uncertainty, and limits.

## Core references
Use `../references/method-citations.md`: Blei et al. (2003) for LDA and Roberts et al. (2014) for STM.
