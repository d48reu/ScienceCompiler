from science_compiler.compiler import compile_claims
from science_compiler.models import Claim, Context


def test_compiler_disambiguates_duplicate_claim_ids_across_sources() -> None:
    claims = [
        Claim(
            claim_id="C1",
            source_id="Paper_Positive",
            intervention="sodium butyrate",
            outcome="neuroinflammation",
            effect="decrease",
            summary="Positive claim.",
            mechanism_tags=["gut-brain axis"],
            context=Context(species="mouse", disease_state="alcohol"),
        ),
        Claim(
            claim_id="C1",
            source_id="Paper_Negative",
            intervention="sodium butyrate",
            outcome="neuroinflammation",
            effect="increase",
            summary="Negative claim.",
            mechanism_tags=["microglial activation"],
            context=Context(species="mouse", disease_state="parkinson's disease"),
        ),
    ]

    report = compile_claims(claims)

    contradiction = report["contradictions"][0]
    assert contradiction["claim_a_id"] != contradiction["claim_b_id"]
    assert "Paper_Positive" in contradiction["claim_a_id"] or "Paper_Positive" in contradiction["claim_b_id"]
    assert "Paper_Negative" in contradiction["claim_a_id"] or "Paper_Negative" in contradiction["claim_b_id"]

    proposal = report["experiment_proposals"][0]
    assert len(set(proposal["contradiction_claim_ids"])) == 2
