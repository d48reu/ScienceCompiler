import csv
from pathlib import Path

from science_compiler.review_queue import build_review_queue


def test_build_review_queue_writes_csvs(tmp_path: Path) -> None:
    report = {
        'ranked_claims': [
            {
                'score': 10,
                'tier': 'headline',
                'evidence_weight': 4.2,
                'claim': {
                    'claim_id': 'P1::C1',
                    'source_id': 'P1',
                    'intervention': 'sodium butyrate',
                    'outcome': 'neuroinflammation',
                    'effect': 'decrease',
                    'summary': 'x',
                },
            }
        ],
        'contradictions': [
            {
                'claim_a_id': 'P1::C1',
                'claim_b_id': 'P2::C1',
                'intervention': 'sodium butyrate',
                'outcome': 'neuroinflammation',
                'kind': 'context_conditioned',
                'differing_context_axes': ['model_system'],
                'hypothesis': 'x',
            }
        ],
        'evidence_balance': [
            {
                'intervention': 'sodium butyrate',
                'outcome': 'neuroinflammation',
                'leading_effect': 'decrease',
                'net_support': 3.4,
                'claim_count': 2,
                'weighted_support_by_effect': {'decrease': 8.0, 'increase': 4.6},
            }
        ],
        'family_evidence_balance': [
            {
                'intervention_family': 'direct butyrate',
                'disease_family': 'parkinsonian',
                'outcome': 'neuroinflammation',
                'leading_effect': 'increase',
                'net_support': -4.6,
                'claim_count': 1,
                'weighted_support_by_effect': {'increase': 4.6},
            }
        ],
    }
    report_path = tmp_path / 'report.json'
    report_path.write_text(__import__('json').dumps(report))
    out_dir = tmp_path / 'review'

    build_review_queue(report_path, out_dir)

    assert (out_dir / 'claims_review.csv').exists()
    assert (out_dir / 'contradictions_review.csv').exists()
    assert (out_dir / 'evidence_balance_review.csv').exists()

    rows = list(csv.DictReader((out_dir / 'claims_review.csv').open()))
    assert rows[0]['claim_id'] == 'P1::C1'
