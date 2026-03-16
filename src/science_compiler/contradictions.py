from __future__ import annotations

from itertools import combinations

from science_compiler.models import Claim, Contradiction
from science_compiler.normalize import compare_contexts, comparison_key, effects_are_opposed


def contradiction_hypothesis(claim_a: Claim, claim_b: Claim, differing_axes: list[str]) -> str:
    if differing_axes:
        axes = ", ".join(differing_axes)
        return (
            f"The sign flip may be explained by hidden moderators on axes: {axes}. "
            f"Claim {claim_a.claim_id} and claim {claim_b.claim_id} may both be true under different contexts."
        )
    return (
        f"Claims {claim_a.claim_id} and {claim_b.claim_id} directly disagree under matched context. "
        "At least one claim, extraction, or assumption set is wrong or incomplete."
    )


def detect_contradictions(claims: list[Claim]) -> list[Contradiction]:
    out: list[Contradiction] = []
    for claim_a, claim_b in combinations(claims, 2):
        if comparison_key(claim_a) != comparison_key(claim_b):
            continue
        if not effects_are_opposed(claim_a.effect, claim_b.effect):
            continue

        shared, differing = compare_contexts(claim_a.context, claim_b.context)
        kind = "context_conditioned" if differing else "direct"
        out.append(
            Contradiction(
                claim_a_id=claim_a.claim_id,
                claim_b_id=claim_b.claim_id,
                kind=kind,
                intervention=claim_a.intervention,
                outcome=claim_a.outcome,
                claim_a_effect=claim_a.effect,
                claim_b_effect=claim_b.effect,
                differing_context_axes=differing,
                shared_context_axes=shared,
                hypothesis=contradiction_hypothesis(claim_a, claim_b, differing),
            )
        )
    return sorted(out, key=lambda x: (x.intervention, x.outcome, x.kind, x.claim_a_id, x.claim_b_id))
