from science_compiler.contradictions import detect_contradictions
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def make_claim(claim_id: str, effect: str, barrier_status: str = "intact") -> Claim:
    return Claim(
        claim_id=claim_id,
        source_id="paper",
        intervention="butyrate administration",
        outcome="neuroinflammation",
        effect=effect,
        summary="summary",
        context=Context(
            species="mouse",
            model_system="lps model",
            tissue="brain",
            barrier_status=barrier_status,
            microbiome_status="conventional",
        ),
    )


def test_detects_direct_contradiction_when_context_matches() -> None:
    claims = normalize_claims([make_claim("A", "decrease"), make_claim("B", "increase")])
    contradictions = detect_contradictions(claims)
    assert len(contradictions) == 1
    assert contradictions[0].kind == "direct"
    assert contradictions[0].differing_context_axes == []


def test_detects_context_conditioned_contradiction_when_context_differs() -> None:
    claims = normalize_claims([
        make_claim("A", "decrease", barrier_status="intact"),
        make_claim("B", "increase", barrier_status="impaired"),
    ])
    contradictions = detect_contradictions(claims)
    assert len(contradictions) == 1
    assert contradictions[0].kind == "context_conditioned"
    assert "barrier_status" in contradictions[0].differing_context_axes
