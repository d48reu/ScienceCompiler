# Draft scientific memo: butyrate and neuroinflammation

Status
- Internal draft
- Based on abstract-level / summary-level corpus, not full-paper adjudication
- Uses the gold 14-claim reviewed corpus

## Core question
Under what conditions does direct butyrate reduce neuroinflammation, and under what conditions might it worsen it?

## Provisional answer
In the current gold corpus, direct sodium butyrate most often appears anti-neuroinflammatory across several disease families, including alcohol-related neuroinflammation, Alzheimer-related models, acute-injury contexts, gut-inflammation spillover contexts, and toxic-exposure contexts. However, one parkinsonian MPTP model shows the opposite direction: sodium butyrate worsens neuroinflammation and broader disease pathology. The most defensible current interpretation is therefore context-dependent effect heterogeneity rather than a universal anti-inflammatory rule.

## Why this memo exists
The Science Compiler corpus was built to move beyond vague literature summaries and identify where the scientific story is coherent versus where it breaks. After extraction, refinement, ontology normalization, evidence weighting, family-split grouping, and manual gold-set curation, the butyrate corpus now supports a sharper scientific claim than “butyrate is good for the brain.”

## Corpus basis
Gold corpus size:
- 14 claims
- 6 contradiction pairs
- 20 mechanism families
- 6 generated experiment proposals

Key file:
- `compiler_report_gold.md`

## Main gold-set evidence balance
Global bucket:
- intervention: sodium butyrate
- outcome: neuroinflammation
- leading effect: decrease
- net support: +23.40
- claim count: 7

Family-split buckets:
- direct butyrate | parkinsonian | neuroinflammation -> increase, net support -5.70
- direct butyrate | alcohol_related | neuroinflammation -> decrease, net support +10.10
- direct butyrate | alzheimer_related | neuroinflammation -> decrease, net support +4.70
- direct butyrate | acute_injury | neuroinflammation -> decrease, net support +4.20
- direct butyrate | gut_inflammation | neuroinflammation -> decrease, net support +5.50
- direct butyrate | toxic_exposure | neuroinflammation -> decrease, net support +4.60

## Best current scientific read
The strongest positive multi-paper cluster is not generic neuroinflammation in the abstract. It is anti-neuroinflammatory benefit in alcohol-related models and several non-parkinsonian injury/toxicity/neurodegeneration contexts.

The strongest negative signal is not generic either. It is concentrated in a parkinsonian MPTP context.

That means the scientifically interesting question is no longer “does butyrate reduce neuroinflammation?” The better question is:

Why does direct sodium butyrate appear anti-neuroinflammatory across several contexts but pro-neuroinflammatory in at least one parkinsonian MPTP model?

## Studies most responsible for the current story
Negative anchor:
- PMID 32556930
  - MPTP Parkinson model
  - sodium butyrate worsened neuroinflammation and broader pathology

Positive anchors:
- PMID 33785315
  - 5XFAD Alzheimer model
  - sodium butyrate reduced neuroinflammation and improved synaptic plasticity
- PMID 36555338
  - binge-ethanol model
  - sodium butyrate prevented pro-inflammatory cytokine increases and normalized microglial changes
- PMID 36709599
  - chronic alcohol model
  - sodium butyrate reduced neuroinflammation and improved barrier-related gut-brain features
- PMID 37665564
  - DSS ulcerative-colitis model with brain spillover
  - sodium butyrate reduced prefrontal-cortex neuroinflammation
- PMID 38340407
  - lead neurotoxicity model
  - sodium butyrate alleviated neuroinflammation and improved cognition
- PMID 39962509
  - cardiac arrest model
  - sodium butyrate reduced microglia-associated neuroinflammation

## Mechanistic themes that recur in the positive side
Several mechanistic motifs recur across the positive buckets:
- microglial suppression / reduced microglial activation
- cytokine reduction
- gut-brain axis or microbiome involvement
- barrier repair / reduced endotoxemia in some contexts
- TLR4/MyD88/NF-kB pathway suppression in some contexts
- HDAC-linked anti-inflammatory framing in some contexts

The negative parkinsonian study instead emphasizes:
- increased microglial activation
- increased astrocyte activation
- worsened inflammatory markers
- worsened broader disease phenotype

## Most plausible interpretation right now
The sign of the butyrate effect is likely moderated by disease program, model context, and possibly treatment details rather than being intrinsically fixed.

The current contradiction set most plausibly points to one or more of the following moderators:
- disease/model family (Parkinsonian toxin model versus Alzheimer/alcohol/injury contexts)
- route or dosing differences
- baseline immune or microbiome state
- gut-barrier state
- timing relative to insult progression

## What this memo does NOT claim
This memo does not prove that sodium butyrate is broadly therapeutic.
This memo does not prove that sodium butyrate is harmful in Parkinson’s disease generally.
This memo does not substitute for a full-paper systematic review or meta-analysis.
This memo does not treat abstract-level extraction as final truth.

## Most important limitations
- Corpus is abstract-level / summary-level, not full-text adjudicated.
- Evidence weighting is heuristic, not formal meta-analysis.
- Some buckets still rely on single-paper support.
- Intervention purity varies; some supporting claims are microbiome-mediated or mixed-SCFA rather than direct sodium butyrate.
- A negative bucket driven by one strong study is scientifically interesting, but not yet definitive.

## Best next-step scientific work
1. Full-paper review of the core contradiction cluster:
   - PMID 32556930
   - PMID 33785315
   - PMID 36555338
   - PMID 36709599
   - PMID 37665564
   - PMID 38340407
   - PMID 39962509

2. Build a structured contrast table across:
   - disease family
   - route
   - dose
   - timing
   - brain region
   - microbiome state
   - barrier status
   - inflammatory readouts

3. Ask whether the parkinsonian negative signal survives after full-paper adjudication.

4. If it does, treat “butyrate sign flip in parkinsonian contexts” as the primary scientific hypothesis rather than a nuisance outlier.

## Draft thesis sentence
Direct sodium butyrate appears predominantly anti-neuroinflammatory across several non-parkinsonian preclinical contexts in the current gold corpus, but a parkinsonian MPTP model shows the opposite direction, suggesting that butyrate’s neuroimmune effects are disease-context dependent rather than uniformly protective.

## Recommendation
This project is now strong enough to justify a real narrative memo, an internal research note, or a tighter domain-specific preprint outline centered on context-dependent butyrate effects. It is not yet strong enough for a high-confidence public scientific claim without deeper full-paper review.
