from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_compiler_emits_family_split_evidence_balance() -> None:
    claims = [
        Claim('C1', 'P1', 'sodium butyrate', 'neuroinflammation', 'increase', 'x', confidence='high', evidence_type='in_vivo', context=Context(disease_state="parkinson's disease")),
        Claim('C1', 'P2', 'sodium butyrate supplementation', 'neuroinflammatory response', 'decrease', 'x', confidence='medium', evidence_type='in_vivo', context=Context(disease_state="alzheimer's disease")),
    ]
    report = compile_claims(claims)
    rows = report['family_evidence_balance']
    assert len(rows) == 2
    assert {row['disease_family'] for row in rows} == {'parkinsonian', 'alzheimer_related'}
    assert all(row['intervention_family'] == 'direct butyrate' for row in rows)
