Butyrate / Neuroinflammation Mini-Corpus

What this corpus is
- A first real domain corpus for the Science Compiler.
- It is intentionally small and tractable.
- It uses abstract-level / PubMed-page summary text, not full papers.

Why this scope
- Enough real literature to test extraction, refinement, contradiction detection, and experiment proposal generation.
- Small enough to inspect failures manually.

Current question
- Under what conditions does butyrate reduce, fail to reduce, or appear to worsen neuroinflammation-related pathology?

Current corpus contents
- 17 study summaries
- mostly mouse in vivo work, with a few mixed/intermediate models
- includes aging, alcohol, Parkinsonian, cardiac arrest, Alzheimer/gut-brain, BBB-related, obesity, ulcerative colitis, lead neurotoxicity, diabetic stroke, traumatic brain injury, and LPS-depression contexts

Caveat
- These files are not canonical abstracts copied directly from publishers.
- They are structured text assembled from PubMed/PMC-accessible summaries for rapid prototyping.
- Good enough for pipeline testing, not good enough for publication-grade evidence synthesis.

Suggested workflow
1. raw_papers/*.txt -> raw_extract_cli
2. extracted claims -> compiler
3. inspect contradictions and ranked claims
4. manually review bad extractions
5. iterate prompts/schema
