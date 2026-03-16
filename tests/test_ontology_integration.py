from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_compiler_evidence_balance_uses_canonicalized_labels() -> None:
    claims = [
        Claim(
            claim_id="C1",
            source_id="P1",
            intervention="sodium butyrate supplementation",
            outcome="neuroinflammatory response",
            effect="decrease",
            summary="x",
            mechanism_tags=[],
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
        Claim(
            claim_id="C1",
            source_id="P2",
            intervention="sodium butyrate",
            outcome="neuroinflammation",
            effect="increase",
            summary="x",
            mechanism_tags=[],
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
    ]
    report = compile_claims(claims)
    rows = report["evidence_balance"]
    assert len(rows) == 1
    assert rows[0]["intervention"] == "sodium butyrate"
    assert rows[0]["outcome"] == "neuroinflammation"
