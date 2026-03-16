Preprint-Style Outline

Working title
Context-dependent neuroimmune effects of sodium butyrate across preclinical disease models: a structured literature-compilation analysis

1. Abstract
- Motivation: butyrate is often described as broadly anti-inflammatory, but the literature may be more context-dependent.
- Methods: structured claim extraction, refinement, ontology normalization, evidence weighting, family-split grouping, and contradiction analysis across a curated preclinical corpus.
- Results: most non-parkinsonian buckets show anti-neuroinflammatory directionality, while one parkinsonian MPTP bucket shows the opposite.
- Interpretation: butyrate’s neuroimmune effects appear heterogeneous across disease contexts.

2. Introduction
2.1 Background
- Butyrate as a microbial metabolite and HDAC-related signaling molecule
- Common claims about butyrate and neuroinflammation
- Problem: literature is broad, mechanistically diverse, and easy to oversimplify

2.2 Gap
- Existing discussions often collapse together distinct disease programs
- Need a structured synthesis that preserves contradiction rather than averaging it away

2.3 Aim
- Build a reproducible structured-literature workflow
- Test whether butyrate’s apparent neuroimmune effects are context-dependent

3. Methods
3.1 Corpus construction
- Domain: butyrate / neuroinflammation
- Source type: abstract-level or summary-level study text
- Inclusion logic: preclinical studies relevant to direct butyrate or closely related gut-brain butyrate mechanisms

3.2 Science Compiler workflow
- raw extraction
- second-pass refinement
- curation and claim ranking
- ontology/canonicalization
- evidence weighting
- contradiction detection
- family-split evidence balance
- reviewed gold-set overrides

3.3 Gold-set curation
- rationale for selecting higher-value claims
- override workflow and reproducibility

3.4 Limitations of method
- abstract-level evidence
- heuristic weighting
- no formal meta-analysis

4. Results
4.1 Corpus overview
- corpus size
- claim counts before/after review
- contradiction counts
- family buckets

4.2 Global result
- overall sodium butyrate -> neuroinflammation bucket leans protective
- but global aggregation masks important heterogeneity

4.3 Family-split result
- parkinsonian bucket: negative
- alcohol-related bucket: positive
- alzheimer-related bucket: positive
- acute injury bucket: positive
- gut-inflammation spillover bucket: positive
- toxic exposure bucket: positive

4.4 Core contradiction cluster
- negative anchor: PMID 32556930
- positive anchors: 33785315, 36555338, 36709599, 37665564, 38340407, 39962509
- contradiction interpreted as context-conditioned rather than direct failed replication

4.5 Mechanistic motifs
- microglial suppression in positive cluster
- cytokine reduction
- barrier repair / gut-brain axis involvement in several contexts
- Parkinson negative cluster emphasizing worsened glial activation and inflammatory markers

5. Discussion
5.1 Main interpretation
- butyrate is not uniformly neuroprotective
- disease program likely moderates effect sign

5.2 Why the Parkinson signal matters
- negative outlier is not nuisance noise
- may indicate disease-specific biology, timing, route, or immunologic context

5.3 Alternative explanations
- extraction or abstraction error
- hidden route/dose/timing differences
- insufficient corpus size
- model-system artifact

5.4 Practical implication
- caution against universalized butyrate narratives
- disease-family-specific framing is more defensible

6. Limitations
- abstract-level text
- no direct quantitative effect sizes
- no study-quality appraisal beyond heuristic weighting
- single-paper support for some buckets

7. Future work
- full-paper adjudication of core contradiction cluster
- route/dose/timing contrast table
- larger corpus expansion
- formal study-quality schema
- second domain replication for method generalization

8. Conclusion
- structured compilation suggests sodium butyrate’s neuroimmune effects are context-dependent
- most current positive signal lies outside the parkinsonian MPTP context
- the parkinsonian sign flip is the most important hypothesis-generating finding

Potential figures/tables
- Figure 1: pipeline diagram
- Figure 2: family-split evidence balance
- Figure 3: contradiction graph centered on the Parkinson outlier
- Table 1: gold-set core papers
- Table 2: disease/model-family contrast table
