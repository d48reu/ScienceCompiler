# Reviewed corpus workflow

Goal
Make human judgment reproducible instead of relying on one-off manual patches.

Core files
- raw extracted claims:
  corpora/butyrate_neuroinflammation/reports/claims_refined.json
- reviewed overrides:
  corpora/butyrate_neuroinflammation/review_overrides.json
- reviewed claims:
  corpora/butyrate_neuroinflammation/reports/claims_reviewed.json
- reviewed report:
  corpora/butyrate_neuroinflammation/reports/compiler_report_reviewed.md
- reviewed review queue:
  corpora/butyrate_neuroinflammation/review_queue_reviewed/

How it works
1. Extract/refine claims from raw paper summaries.
2. Apply review_overrides.json.
3. Compile the reviewed claims into the reviewed report.
4. Generate a fresh review queue for the reviewed report.

One-command run
From project root:
  ./corpora/butyrate_neuroinflammation/run_reviewed_corpus.sh

How to edit reviewed judgments
Open:
  corpora/butyrate_neuroinflammation/review_overrides.json

Supported override actions
- updates: patch an existing claim by source_id + claim_id
- drops: remove an extracted claim entirely
- adds: inject a hand-authored claim

Blunt rule
If a reviewed change matters scientifically, put it in review_overrides.json.
Do not quietly hand-edit claims_reviewed.json and call it a workflow.
