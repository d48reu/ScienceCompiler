from __future__ import annotations

from science_compiler.models import Claim, Contradiction, ExperimentProposal


MODERATOR_PRIORITY = [
    "barrier_status",
    "microbiome_status",
    "dose_level",
    "administration_route",
    "species",
    "model_system",
    "disease_state",
    "tissue",
    "time_horizon",
]


def _claim_lookup(claims: list[Claim]) -> dict[str, Claim]:
    return {claim.claim_id: claim for claim in claims}


def _rank_moderators(moderators: list[str]) -> list[str]:
    rank = {name: i for i, name in enumerate(MODERATOR_PRIORITY)}
    return sorted(moderators, key=lambda x: (rank.get(x, 999), x))


def propose_experiments(contradictions: list[Contradiction], claims: list[Claim]) -> list[ExperimentProposal]:
    lookup = _claim_lookup(claims)
    proposals: list[ExperimentProposal] = []

    for contradiction in contradictions:
        claim_a = lookup[contradiction.claim_a_id]
        claim_b = lookup[contradiction.claim_b_id]

        moderators = _rank_moderators(contradiction.differing_context_axes or ["dose_level"])[:3]
        if contradiction.kind == "direct":
            title = f"Replicate matched-context effect of {claim_a.intervention} on {claim_a.outcome}"
            rationale = (
                f"Claims {claim_a.claim_id} and {claim_b.claim_id} disagree without obvious context differences. "
                "The highest-value next step is a tightly matched replication with preregistered assumptions."
            )
            design = [
                f"Hold species/model/tissue constant while testing {claim_a.intervention} vs control.",
                f"Primary outcome: {claim_a.outcome}.",
                "Use the same dose and administration route where possible, or explicitly bracket them.",
            ]
        else:
            mod_phrase = ", ".join(moderators)
            title = f"Test whether {mod_phrase} moderates the effect of {claim_a.intervention} on {claim_a.outcome}"
            rationale = (
                f"Claims {claim_a.claim_id} and {claim_b.claim_id} may only disagree because context axes differ: {mod_phrase}. "
                "A factorial design can separate true sign flips from hidden moderators."
            )
            design = [
                f"Run a factorial intervention varying {mod_phrase} alongside {claim_a.intervention} vs control.",
                f"Measure {claim_a.outcome} and any mechanistic mediators tied to {claim_a.mechanism_tags or ['unspecified mechanism']}.",
                "Include enough power to detect interaction effects, not just main effects.",
            ]

        predictions = [
            f"If claim {claim_a.claim_id} is right, {claim_a.intervention} should {claim_a.effect} {claim_a.outcome} in context A.",
            f"If claim {claim_b.claim_id} is right, {claim_b.intervention} should {claim_b.effect} {claim_b.outcome} in context B.",
        ]
        if contradiction.kind == "context_conditioned":
            predictions.append(
                "If the moderator hypothesis is right, the effect sign should depend on the manipulated context axis rather than stay globally fixed."
            )

        proposals.append(
            ExperimentProposal(
                title=title,
                contradiction_claim_ids=[claim_a.claim_id, claim_b.claim_id],
                rationale=rationale,
                candidate_moderators=moderators,
                design=design,
                predictions=predictions,
            )
        )

    return proposals
