from science_compiler.discipline import enforce_claim_discipline
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_enforce_claim_discipline_limits_per_source_and_keeps_best_headlines() -> None:
    claims = normalize_claims([
        Claim('C1', 'P1', 'sodium butyrate', 'neuroinflammation', 'decrease', 'headline 1', confidence='high', evidence_type='in_vivo', context=Context(species='mouse')),
        Claim('C2', 'P1', 'sodium butyrate', 'motor performance', 'increase', 'headline 2', confidence='medium', evidence_type='in_vivo', context=Context(species='mouse')),
        Claim('C3', 'P1', 'sodium butyrate', 'memory deficits', 'decrease', 'headline 3', confidence='medium', evidence_type='in_vivo', context=Context(species='mouse')),
        Claim('C4', 'P1', 'sodium butyrate', 'il-6', 'decrease', 'biomarker', confidence='medium', evidence_type='in_vivo', context=Context(species='mouse')),
        Claim('C5', 'P1', 'sodium butyrate', 'treg abundance', 'increase', 'mechanistic', confidence='high', evidence_type='in_vivo', context=Context(species='mouse')),
        Claim('C6', 'P1', 'sodium butyrate', 'microglial activation', 'decrease', 'mechanistic 2', confidence='medium', evidence_type='in_vivo', context=Context(species='mouse')),
    ])

    disciplined = enforce_claim_discipline(claims)
    kept_ids = {c.claim_id for c in disciplined}
    assert len(disciplined) <= 4
    assert {'C1', 'C2', 'C3'}.issubset(kept_ids)
    assert 'C4' not in kept_ids
    assert 'C5' in kept_ids or 'C6' in kept_ids


def test_enforce_claim_discipline_keeps_all_when_already_small() -> None:
    claims = normalize_claims([
        Claim('C1', 'P1', 'butyrate', 'neuroinflammation', 'decrease', 'x', context=Context(species='mouse')),
        Claim('C2', 'P1', 'butyrate', 'treg abundance', 'increase', 'x', context=Context(species='mouse')),
    ])
    disciplined = enforce_claim_discipline(claims)
    assert [c.claim_id for c in disciplined] == ['C1', 'C2']
