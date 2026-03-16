# Butyrate / Neuroinflammation corpus summary

Corpus status
- 17 abstract-level study-summary files
- 17 refined claims extracted
- 5 context-conditioned contradictions
- 31 mechanism families
- 5 experiment proposals
- review queue CSVs generated for claims, contradictions, and evidence balances

What changed after corpus expansion
The original mini-corpus was too small and gave a brittle picture. After expansion, the corpus now covers more disease contexts:
- aging
- Alzheimer's / amyloid
- Parkinson's disease
- alcohol-related neuroinflammation
- obesity / hypothalamic inflammation
- ulcerative colitis gut-brain signaling
- lead neurotoxicity
- diabetic stroke
- traumatic brain injury
- LPS-induced depression-like behavior

Most important weighted result
For the main grouped bucket:
- intervention: sodium butyrate
- outcome: neuroinflammation
- weighted support for increase: 5.80
- weighted support for decrease: 22.80
- net support: +17.00
- claim count: 6

Blunt interpretation
Once the corpus is expanded and canonicalized, the current evidence in this small abstract-level set leans clearly toward sodium butyrate decreasing neuroinflammation in many contexts. However, one Parkinson/MPTP paper still points the other way and generates genuine contradiction structure.

Main contradiction cluster
All current contradictions center on the same negative Parkinson/MPTP study versus multiple positive contexts:
- Parkinson/MPTP negative study: sodium butyrate increases neuroinflammation
- Positive studies: sodium butyrate decreases neuroinflammation in 5XFAD Alzheimer's, binge-ethanol, chronic alcohol, lead neurotoxicity, and cardiac arrest contexts

Compiler interpretation
The system does not treat this as a simple replication dispute. It treats it as context-conditioned sign flipping, with likely moderators including:
- disease/model system
- microbiome status
- administration route
- dose level
- tissue / brain region context

Best current experiment ideas
1. Test whether dose level, administration route, and model system moderate sodium butyrate's effect on neuroinflammation.
2. Test whether microbiome status, dose level, and administration route moderate sodium butyrate's effect on neuroinflammation.

What still limits trust
- The corpus still uses abstract-level or summary-level text, not full papers.
- Extraction is much better than before but still not perfect.
- Evidence weighting is heuristic, not formal meta-analysis.
- Some outcomes remain neighboring rather than fully unified (for example microglial activation vs neuroinflammation).

Human review workflow
Generate / inspect:
- corpora/butyrate_neuroinflammation/review_queue/claims_review.csv
- corpora/butyrate_neuroinflammation/review_queue/contradictions_review.csv
- corpora/butyrate_neuroinflammation/review_queue/evidence_balance_review.csv

These are the files to use for manual QA before trusting any scientific story too much.
