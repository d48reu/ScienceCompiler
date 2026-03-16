import json
from pathlib import Path

from science_compiler.review_overrides import apply_review_overrides, load_review_overrides
from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_overrides_make_reviewed_report_reproducible(tmp_path: Path) -> None:
    claims = [
        Claim('C1', 'P1', 'sodium butyrate', 'il-6', 'decrease', 'raw', context=Context(species='mouse')),
    ]
    overrides_path = tmp_path / 'overrides.json'
    overrides_path.write_text(json.dumps({
        'updates': [
            {'source_id': 'P1', 'claim_id': 'C1', 'set': {'outcome': 'neuroinflammation', 'summary': 'reviewed'}}
        ],
        'drops': [],
        'adds': []
    }))
    reviewed_claims = apply_review_overrides(claims, load_review_overrides(overrides_path))
    report = compile_claims(reviewed_claims)
    assert report['claims'][0]['outcome'] == 'neuroinflammation'
    assert report['claims'][0]['summary'] == 'reviewed'
