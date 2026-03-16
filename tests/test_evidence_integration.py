from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_compiler_emits_evidence_balance_section() -> None:
    claims = [
        Claim(
            claim_id="C1",
            source_id="P1",
            intervention="sodium butyrate",
            outcome="neuroinflammation",
            effect="decrease",
            summary="positive",
            confidence="high",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
        Claim(
            claim_id="C1",
            source_id="P2",
            intervention="sodium butyrate",
            outcome="neuroinflammation",
            effect="increase",
            summary="negative",
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
    ]

    report = compile_claims(claims)
    assert "evidence_balance" in report
    assert len(report["evidence_balance"]) == 1
    row = report["evidence_balance"][0]
    assert row["intervention"] == "sodium butyrate"
    assert row["outcome"] == "neuroinflammation"
    assert row["leading_effect"] in {"decrease", "increase", "mixed"}
    assert "weighted_support_by_effect" in row
