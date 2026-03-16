#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

./corpora/butyrate_neuroinflammation/run_reviewed_corpus.sh

.venv/bin/python -m science_compiler.review_apply_cli \
  --claims corpora/butyrate_neuroinflammation/reports/claims_reviewed.json \
  --overrides corpora/butyrate_neuroinflammation/gold_overrides.json \
  --output corpora/butyrate_neuroinflammation/reports/claims_gold.json

.venv/bin/python -m science_compiler.cli \
  --input corpora/butyrate_neuroinflammation/reports/claims_gold.json \
  --output corpora/butyrate_neuroinflammation/reports/compiler_report_gold.json \
  --markdown corpora/butyrate_neuroinflammation/reports/compiler_report_gold.md

.venv/bin/python -m science_compiler.review_queue_cli \
  --report corpora/butyrate_neuroinflammation/reports/compiler_report_gold.json \
  --output-dir corpora/butyrate_neuroinflammation/review_queue_gold

printf 'Done. See gold outputs under corpora/butyrate_neuroinflammation/reports/ and review_queue_gold/\n'
