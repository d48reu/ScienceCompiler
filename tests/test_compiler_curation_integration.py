from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_compiler_reports_curated_and_ranked_claims() -> None:
    claims = [
        Claim(
            claim_id="C1",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="il-6",
            effect="decrease",
            summary="Butyrate lowered IL-6.",
            mechanism_tags=[],
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
        Claim(
            claim_id="C2",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="neuroinflammation",
            effect="decrease",
            summary="Butyrate reduced neuroinflammation.",
            mechanism_tags=[],
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
        Claim(
            claim_id="C3",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="neuroinflammation",
            effect="decrease",
            summary="Butyrate reduced inflammatory burden in the brain.",
            mechanism_tags=["treg expansion"],
            confidence="high",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
    ]

    report = compile_claims(claims)

    assert report["summary"]["raw_claim_count"] == 3
    assert report["summary"]["claim_count"] == 2
    assert report["ranked_claims"][0]["tier"] == "headline"
    assert report["ranked_claims"][0]["claim"]["outcome"] == "neuroinflammation"
