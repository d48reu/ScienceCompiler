from science_compiler.curation import consolidate_claims, rank_claims
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_consolidate_claims_merges_exact_duplicate_extractions_within_source() -> None:
    claims = normalize_claims([
        Claim(
            claim_id="C1",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="neuroinflammation",
            effect="decrease",
            summary="Butyrate reduced neuroinflammation.",
            mechanism_tags=["treg expansion"],
            confidence="medium",
            context=Context(species="mouse", barrier_status="intact"),
        ),
        Claim(
            claim_id="C2",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="neuroinflammation",
            effect="decrease",
            summary="Oral butyrate reduced inflammatory burden in the brain.",
            mechanism_tags=["hdac inhibition"],
            confidence="high",
            context=Context(species="mouse", barrier_status="intact"),
        ),
    ])

    curated = consolidate_claims(claims)

    assert len(curated) == 1
    assert curated[0].confidence == "high"
    assert curated[0].mechanism_tags == ["hdac inhibition", "treg expansion"]
    assert "reduced inflammatory burden" in curated[0].summary.lower()


def test_rank_claims_prefers_high_level_outcomes_over_biomarkers() -> None:
    claims = normalize_claims([
        Claim(
            claim_id="C1",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="il-6",
            effect="decrease",
            summary="Butyrate lowered IL-6.",
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
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
        Claim(
            claim_id="C3",
            source_id="Paper_A",
            intervention="butyrate administration",
            outcome="treg abundance",
            effect="increase",
            summary="Butyrate increased Treg abundance.",
            confidence="high",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        ),
    ])

    ranked = rank_claims(claims)

    assert ranked[0].claim.outcome == "neuroinflammation"
    assert ranked[0].tier == "headline"
    assert ranked[-1].claim.outcome == "il-6"
    assert ranked[-1].tier == "biomarker"
