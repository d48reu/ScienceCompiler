from science_compiler.bucketing import intervention_family, disease_family, summarize_family_evidence_balance
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_intervention_family_groups_direct_vs_microbiome_vs_mixed_scfa() -> None:
    direct = Claim('C1', 'P1', 'sodium butyrate', 'neuroinflammation', 'decrease', 'x', context=Context(disease_state='alzheimer\'s'))
    probiotic = Claim('C2', 'P2', 'clostridium butyricum', 'microglial activation', 'decrease', 'x', context=Context(disease_state='alzheimer\'s'))
    mixed = Claim('C3', 'P3', 'scfa supplementation', 'ventriculomegaly', 'decrease', 'x', context=Context(disease_state='traumatic brain injury'))

    assert intervention_family(direct) == 'direct butyrate'
    assert intervention_family(probiotic) == 'microbiome-mediated butyrate'
    assert intervention_family(mixed) == 'mixed scfa intervention'


def test_disease_family_splits_parkinson_from_alzheimer_and_injury() -> None:
    parkinson = Claim('C1', 'P1', 'sodium butyrate', 'neuroinflammation', 'increase', 'x', context=Context(disease_state="parkinson's disease"))
    alz = Claim('C2', 'P2', 'sodium butyrate', 'neuroinflammation', 'decrease', 'x', context=Context(disease_state="alzheimer's disease"))
    injury = Claim('C3', 'P3', 'sodium butyrate', 'neuroinflammation', 'decrease', 'x', context=Context(disease_state='cardiac arrest'))

    assert disease_family(parkinson) == 'parkinsonian'
    assert disease_family(alz) == 'alzheimer_related'
    assert disease_family(injury) == 'acute_injury'


def test_summarize_family_evidence_balance_separates_context_families() -> None:
    claims = normalize_claims([
        Claim('C1', 'P1', 'sodium butyrate', 'neuroinflammation', 'increase', 'x', confidence='high', evidence_type='in_vivo', context=Context(disease_state="parkinson's disease")),
        Claim('C1', 'P2', 'sodium butyrate', 'neuroinflammation', 'decrease', 'x', confidence='medium', evidence_type='in_vivo', context=Context(disease_state="alzheimer's disease")),
        Claim('C1', 'P3', 'sodium butyrate', 'neuroinflammation', 'decrease', 'x', confidence='medium', evidence_type='in_vivo', context=Context(disease_state='cardiac arrest')),
    ])
    rows = summarize_family_evidence_balance(claims)
    keys = {(r.intervention_family, r.disease_family, r.outcome) for r in rows}
    assert ('direct butyrate', 'parkinsonian', 'neuroinflammation') in keys
    assert ('direct butyrate', 'alzheimer_related', 'neuroinflammation') in keys
    assert ('direct butyrate', 'acute_injury', 'neuroinflammation') in keys
