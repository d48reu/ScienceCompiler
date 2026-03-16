from science_compiler.evidence import compute_evidence_weight, summarize_evidence_balance
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_compute_evidence_weight_prefers_stronger_evidence_and_confidence() -> None:
    weak = Claim(
        claim_id="C1",
        source_id="A",
        intervention="butyrate",
        outcome="neuroinflammation",
        effect="decrease",
        summary="weak",
        confidence="low",
        evidence_type="in_vitro",
        context=Context(species="cell culture"),
    )
    strong = Claim(
        claim_id="C2",
        source_id="B",
        intervention="butyrate",
        outcome="neuroinflammation",
        effect="decrease",
        summary="strong",
        confidence="high",
        evidence_type="clinical",
        context=Context(species="human", disease_state="alzheimer's disease", tissue="brain"),
    )
    assert compute_evidence_weight(strong) > compute_evidence_weight(weak)


def test_summarize_evidence_balance_tracks_net_direction() -> None:
    claims = normalize_claims([
        Claim("C1", "P1", "sodium butyrate", "neuroinflammation", "decrease", "x", confidence="high", evidence_type="in_vivo", context=Context(species="mouse")),
        Claim("C2", "P2", "sodium butyrate", "neuroinflammation", "decrease", "x", confidence="medium", evidence_type="in_vivo", context=Context(species="mouse")),
        Claim("C3", "P3", "sodium butyrate", "neuroinflammation", "increase", "x", confidence="medium", evidence_type="in_vivo", context=Context(species="mouse")),
    ])

    balances = summarize_evidence_balance(claims)
    assert len(balances) == 1
    balance = balances[0]
    assert balance.intervention == "sodium butyrate"
    assert balance.outcome == "neuroinflammation"
    assert balance.leading_effect == "decrease"
    assert balance.net_support > 0
