from science_compiler.contradictions import detect_contradictions
from science_compiler.experiments import propose_experiments
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_experiment_proposal_mentions_moderator() -> None:
    claims = normalize_claims([
        Claim("A", "p1", "butyrate", "neuroinflammation", "decrease", "x", ["treg expansion"], context=Context(species="mouse", barrier_status="intact")),
        Claim("B", "p2", "butyrate", "neuroinflammation", "increase", "x", ["barrier conditionality"], context=Context(species="mouse", barrier_status="impaired")),
    ])
    contradictions = detect_contradictions(claims)
    proposals = propose_experiments(contradictions, claims)
    assert len(proposals) == 1
    assert "barrier_status" in proposals[0].candidate_moderators
    assert "factorial" in proposals[0].design[0].lower()
