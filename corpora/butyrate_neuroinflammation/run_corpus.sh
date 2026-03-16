#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

.venv/bin/python -m science_compiler.raw_extract_cli \
  --input-dir corpora/butyrate_neuroinflammation/raw_papers \
  --output corpora/butyrate_neuroinflammation/reports/claims_refined.json

.venv/bin/python -m science_compiler.cli \
  --input corpora/butyrate_neuroinflammation/reports/claims_refined.json \
  --output corpora/butyrate_neuroinflammation/reports/compiler_report.json \
  --markdown corpora/butyrate_neuroinflammation/reports/compiler_report.md

.venv/bin/python -m science_compiler.review_queue_cli \
  --report corpora/butyrate_neuroinflammation/reports/compiler_report.json \
  --output-dir corpora/butyrate_neuroinflammation/review_queue

printf 'Done. See corpora/butyrate_neuroinflammation/reports/ and review_queue/\n'
