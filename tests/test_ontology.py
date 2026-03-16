from science_compiler.normalize import normalize_claims
from science_compiler.models import Claim, Context


def test_normalize_claim_canonicalizes_intervention_outcome_and_mechanism_tags() -> None:
    claims = normalize_claims([
        Claim(
            claim_id="C1",
            source_id="P1",
            intervention="Sodium Butyrate Supplementation",
            outcome="Neuroinflammatory Response",
            effect="decrease",
            summary="x",
            mechanism_tags=["TLR4/MyD88/NF-kB pathway suppression", "microbiome-gut-brain axis repair"],
            context=Context(species="mouse"),
        )
    ])
    claim = claims[0]
    assert claim.intervention == "sodium butyrate"
    assert claim.outcome == "neuroinflammation"
    assert "tlr4/myd88/nf-κb pathway inhibition" in claim.mechanism_tags
    assert "microbiome-gut-brain axis" in claim.mechanism_tags


def test_normalize_claim_groups_semantically_similar_bbb_and_amyloid_labels() -> None:
    claims = normalize_claims([
        Claim("C1", "P1", "butyrate", "Aβ42 uptake and accumulation in endothelial cells", "decrease", "x", context=Context()),
        Claim("C2", "P2", "butyrate", "amyloid-beta uptake and accumulation in endothelial cells", "decrease", "x", context=Context()),
        Claim("C3", "P3", "butyrate", "blood-brain barrier integrity", "increase", "x", context=Context()),
        Claim("C4", "P4", "butyrate", "bbb integrity", "increase", "x", context=Context()),
    ])
    assert claims[0].outcome == claims[1].outcome == "amyloid-beta uptake and accumulation"
    assert claims[2].outcome == claims[3].outcome == "blood-brain barrier integrity"
