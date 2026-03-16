from __future__ import annotations

from dataclasses import dataclass

from science_compiler.models import Claim
from science_compiler.normalize import context_axes, normalize_claims


CONFIDENCE_ORDER = {"low": 0, "medium": 1, "high": 2}
EVIDENCE_BONUS = {
    "clinical": 3,
    "in_vivo": 2,
    "organoid": 1,
    "in_vitro": 1,
    "review": 0,
    "unknown": 0,
}
HEADLINE_OUTCOME_TERMS = {
    "neuroinflammation",
    "cognition",
    "survival",
    "lifespan",
    "healthspan",
    "tumor growth",
    "disease severity",
    "blood-brain barrier integrity",
    "barrier integrity",
    "mortality",
}
BIOMARKER_TERMS = {
    "il-6",
    "tnf-alpha",
    "tnfα",
    "cytokines",
    "nf-kb",
    "nf-κb",
    "gene expression",
    "protein expression",
}
MECHANISTIC_TERMS = {
    "treg abundance",
    "treg expansion",
    "microglial activation",
    "hdac activity",
    "microglial priming",
}


@dataclass(slots=True)
class RankedClaim:
    claim: Claim
    score: int
    tier: str


def _claim_key(claim: Claim) -> tuple:
    ctx = tuple(sorted(context_axes(claim.context).items()))
    return (claim.source_id, claim.intervention, claim.outcome, claim.effect, ctx)


def _pick_summary(a: str, b: str) -> str:
    return a if len(a) >= len(b) else b


def _pick_confidence(a: str, b: str) -> str:
    return a if CONFIDENCE_ORDER.get(a, -1) >= CONFIDENCE_ORDER.get(b, -1) else b


def consolidate_claims(claims: list[Claim]) -> list[Claim]:
    merged: dict[tuple, Claim] = {}
    for claim in normalize_claims(claims):
        key = _claim_key(claim)
        if key not in merged:
            merged[key] = claim
            continue

        existing = merged[key]
        merged[key] = Claim(
            claim_id=existing.claim_id,
            source_id=existing.source_id,
            intervention=existing.intervention,
            outcome=existing.outcome,
            effect=existing.effect,
            summary=_pick_summary(existing.summary, claim.summary),
            mechanism_tags=sorted(set(existing.mechanism_tags) | set(claim.mechanism_tags)),
            confidence=_pick_confidence(existing.confidence, claim.confidence),
            evidence_type=existing.evidence_type if existing.evidence_type != 'unknown' else claim.evidence_type,
            context=existing.context,
        )
    return sorted(merged.values(), key=lambda c: (c.source_id, c.claim_id, c.outcome))


def classify_claim_tier(claim: Claim) -> str:
    outcome = claim.outcome.lower()
    if outcome in HEADLINE_OUTCOME_TERMS:
        return 'headline'
    if outcome in BIOMARKER_TERMS:
        return 'biomarker'
    if outcome in MECHANISTIC_TERMS:
        return 'mechanistic'
    if any(term in outcome for term in ('inflammation', 'cognition', 'survival', 'integrity', 'severity')):
        return 'headline'
    if any(term in outcome for term in ('il-', 'tnf', 'cytok', 'expression')):
        return 'biomarker'
    if any(term in outcome for term in ('treg', 'microglial', 'hdac')):
        return 'mechanistic'
    return 'supporting'


def score_claim(claim: Claim) -> RankedClaim:
    tier = classify_claim_tier(claim)
    tier_score = {
        'headline': 30,
        'mechanistic': 20,
        'supporting': 15,
        'biomarker': 10,
    }[tier]
    confidence_score = CONFIDENCE_ORDER.get(claim.confidence, 1) + 1
    evidence_score = EVIDENCE_BONUS.get(claim.evidence_type, 0)
    context_score = min(len(context_axes(claim.context)), 4)
    score = tier_score + confidence_score + evidence_score + context_score
    return RankedClaim(claim=claim, score=score, tier=tier)


def rank_claims(claims: list[Claim]) -> list[RankedClaim]:
    curated = consolidate_claims(claims)
    ranked = [score_claim(claim) for claim in curated]
    return sorted(ranked, key=lambda item: (-item.score, item.claim.source_id, item.claim.claim_id))
