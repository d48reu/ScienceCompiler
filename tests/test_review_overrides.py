import json
from pathlib import Path

from science_compiler.models import Claim, Context
from science_compiler.review_overrides import apply_review_overrides, load_review_overrides


def test_apply_review_overrides_can_update_drop_and_add_claims() -> None:
    claims = [
        Claim('C1', 'P1', 'butyrate', 'il-6', 'decrease', 'old summary', context=Context(species='mouse')),
        Claim('C2', 'P1', 'butyrate', 'treg abundance', 'increase', 'keep me', context=Context(species='mouse')),
    ]
    overrides = {
        'updates': [
            {
                'source_id': 'P1',
                'claim_id': 'C1',
                'set': {
                    'outcome': 'neuroinflammation',
                    'summary': 'new summary',
                    'context': {'disease_state': 'aging-related neuroinflammation'}
                }
            }
        ],
        'drops': [
            {'source_id': 'P1', 'claim_id': 'C2'}
        ],
        'adds': [
            {
                'claim_id': 'C3',
                'source_id': 'P1',
                'intervention': 'butyrate',
                'outcome': 'memory deficits',
                'effect': 'decrease',
                'summary': 'added',
                'mechanism_tags': [],
                'confidence': 'medium',
                'evidence_type': 'unknown',
                'context': {'species': 'mouse'}
            }
        ]
    }

    out = apply_review_overrides(claims, overrides)
    assert len(out) == 2
    updated = next(c for c in out if c.claim_id == 'C1')
    added = next(c for c in out if c.claim_id == 'C3')
    assert updated.outcome == 'neuroinflammation'
    assert updated.context.disease_state == 'aging-related neuroinflammation'
    assert added.outcome == 'memory deficits'


def test_load_review_overrides_reads_json_file(tmp_path: Path) -> None:
    path = tmp_path / 'overrides.json'
    payload = {'updates': [], 'drops': [], 'adds': []}
    path.write_text(json.dumps(payload))
    loaded = load_review_overrides(path)
    assert loaded == payload
