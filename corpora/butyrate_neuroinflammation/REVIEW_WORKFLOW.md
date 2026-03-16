# Butyrate / Neuroinflammation review workflow

Why this exists
The compiler is useful, but it still makes extraction, canonicalization, and grouping mistakes. This workflow is the human brake pedal.

Outputs generated for review
- claims_review.csv
- contradictions_review.csv
- evidence_balance_review.csv

How to generate review files
From project root:

  .venv/bin/python -m science_compiler.review_queue_cli \
    --report corpora/butyrate_neuroinflammation/reports/compiler_report.json \
    --output-dir corpora/butyrate_neuroinflammation/review_queue

What to review first
1. claims_review.csv
   - Is the claim actually supported by the source summary?
   - Is the outcome too narrow (biomarker) or too broad?
   - Is the intervention canonicalized correctly?
   - Is the effect sign correct?

2. contradictions_review.csv
   - Is this a real contradiction or just bad extraction?
   - Are the context axes meaningful?
   - Did ontology merging create or remove a contradiction incorrectly?

3. evidence_balance_review.csv
   - Are grouped intervention/outcome buckets semantically coherent?
   - Is the leading effect believable?
   - Do any rows need outcome or intervention splitting?

Suggested status labels
- accept
- fix_extraction
- fix_ontology
- split_bucket
- drop_claim
- investigate

Blunt rule
If a contradiction disappears when you read the underlying study summary carefully, that is not a scientific contradiction. That is a pipeline error. Mark it and fix the pipeline, not the story.
