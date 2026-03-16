#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

.venv/bin/python -m science_compiler.raw_extract_cli \
  --input-dir corpora/butyrate_neuroinflammation/raw_papers \
  --output corpora/butyrate_neuroinflammation/reports/claims_refined.json

.venv/bin/python -m science_compiler.review_apply_cli \
  --claims corpora/butyrate_neuroinflammation/reports/claims_refined.json \
  --overrides corpora/butyrate_neuroinflammation/review_overrides.json \
  --output corpora/butyrate_neuroinflammation/reports/claims_reviewed.json

.venv/bin/python -m science_compiler.cli \
  --input corpora/butyrate_neuroinflammation/reports/claims_reviewed.json \
  --output corpora/butyrate_neuroinflammation/reports/compiler_report_reviewed.json \
  --markdown corpora/butyrate_neuroinflammation/reports/compiler_report_reviewed.md

.venv/bin/python -m science_compiler.review_queue_cli \
  --report corpora/butyrate_neuroinflammation/reports/compiler_report_reviewed.json \
  --output-dir corpora/butyrate_neuroinflammation/review_queue_reviewed

printf 'Done. See reviewed outputs under corpora/butyrate_neuroinflammation/reports/ and review_queue_reviewed/\n'
