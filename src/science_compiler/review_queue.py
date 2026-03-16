from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_review_queue(report_path: str | Path, output_dir: str | Path) -> None:
    report = json.loads(Path(report_path).read_text())
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    claim_rows = []
    for item in report.get('ranked_claims', []):
        claim = item['claim']
        claim_rows.append({
            'claim_id': claim['claim_id'],
            'source_id': claim['source_id'],
            'intervention': claim['intervention'],
            'outcome': claim['outcome'],
            'effect': claim['effect'],
            'tier': item['tier'],
            'score': item['score'],
            'evidence_weight': item['evidence_weight'],
            'summary': claim['summary'],
            'review_status': '',
            'review_issue_type': '',
            'review_notes': '',
        })
    _write_csv(
        output / 'claims_review.csv',
        claim_rows,
        ['claim_id', 'source_id', 'intervention', 'outcome', 'effect', 'tier', 'score', 'evidence_weight', 'summary', 'review_status', 'review_issue_type', 'review_notes'],
    )

    contradiction_rows = []
    for item in report.get('contradictions', []):
        contradiction_rows.append({
            'claim_a_id': item['claim_a_id'],
            'claim_b_id': item['claim_b_id'],
            'intervention': item['intervention'],
            'outcome': item['outcome'],
            'kind': item['kind'],
            'differing_context_axes': '; '.join(item['differing_context_axes']),
            'hypothesis': item['hypothesis'],
            'review_status': '',
            'review_notes': '',
        })
    _write_csv(
        output / 'contradictions_review.csv',
        contradiction_rows,
        ['claim_a_id', 'claim_b_id', 'intervention', 'outcome', 'kind', 'differing_context_axes', 'hypothesis', 'review_status', 'review_notes'],
    )

    balance_rows = []
    for item in report.get('evidence_balance', []):
        balance_rows.append({
            'intervention': item['intervention'],
            'outcome': item['outcome'],
            'leading_effect': item['leading_effect'],
            'net_support': item['net_support'],
            'claim_count': item['claim_count'],
            'weighted_support_by_effect': json.dumps(item['weighted_support_by_effect'], sort_keys=True),
            'review_status': '',
            'review_notes': '',
        })
    _write_csv(
        output / 'evidence_balance_review.csv',
        balance_rows,
        ['intervention', 'outcome', 'leading_effect', 'net_support', 'claim_count', 'weighted_support_by_effect', 'review_status', 'review_notes'],
    )

    family_rows = []
    for item in report.get('family_evidence_balance', []):
        family_rows.append({
            'intervention_family': item['intervention_family'],
            'disease_family': item['disease_family'],
            'outcome': item['outcome'],
            'leading_effect': item['leading_effect'],
            'net_support': item['net_support'],
            'claim_count': item['claim_count'],
            'weighted_support_by_effect': json.dumps(item['weighted_support_by_effect'], sort_keys=True),
            'review_status': '',
            'review_notes': '',
        })
    _write_csv(
        output / 'family_evidence_balance_review.csv',
        family_rows,
        ['intervention_family', 'disease_family', 'outcome', 'leading_effect', 'net_support', 'claim_count', 'weighted_support_by_effect', 'review_status', 'review_notes'],
    )
