#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

.venv/bin/python -m science_compiler.raw_extract_cli \
  --input-dir corpora/senolytics_aging/raw_papers \
  --output corpora/senolytics_aging/reports/claims_refined.json

.venv/bin/python -m science_compiler.cli \
  --input corpora/senolytics_aging/reports/claims_refined.json \
  --output corpora/senolytics_aging/reports/compiler_report.json \
  --markdown corpora/senolytics_aging/reports/compiler_report.md

.venv/bin/python -m science_compiler.review_queue_cli \
  --report corpora/senolytics_aging/reports/compiler_report.json \
  --output-dir corpora/senolytics_aging/review_queue

printf 'Done. See corpora/senolytics_aging/reports/ and review_queue/\n'
