from __future__ import annotations

from typing import Iterable

from science_compiler.models import Claim, Context
from science_compiler.ontology import canonicalize_intervention, canonicalize_mechanism_tag, canonicalize_outcome


EFFECT_ALIASES = {
    "increase": "increase",
    "increases": "increase",
    "increased": "increase",
    "up": "increase",
    "positive": "increase",
    "pro-inflammatory": "increase",
    "pro inflammatory": "increase",
    "protective": "decrease",
    "anti-inflammatory": "decrease",
    "anti inflammatory": "decrease",
    "decrease": "decrease",
    "decreases": "decrease",
    "decreased": "decrease",
    "down": "decrease",
    "negative": "decrease",
    "worsens": "increase",
    "worsened": "increase",
    "no_effect": "null",
    "none": "null",
    "null": "null",
    "mixed": "mixed",
    "conditional": "conditional",
}


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = " ".join(value.strip().lower().split())
    return cleaned or None


def normalize_effect(value: str) -> str:
    key = normalize_text(value)
    if key is None:
        return "unknown"
    return EFFECT_ALIASES.get(key, key)


def normalize_context(context: Context) -> Context:
    return Context(
        species=normalize_text(context.species),
        model_system=normalize_text(context.model_system),
        tissue=normalize_text(context.tissue),
        disease_state=normalize_text(context.disease_state),
        microbiome_status=normalize_text(context.microbiome_status),
        barrier_status=normalize_text(context.barrier_status),
        administration_route=normalize_text(context.administration_route),
        dose_level=normalize_text(context.dose_level),
        time_horizon=normalize_text(context.time_horizon),
        notes=context.notes,
    )


def normalize_claim(claim: Claim) -> Claim:
    normalized_intervention = normalize_text(claim.intervention) or ""
    normalized_outcome = normalize_text(claim.outcome) or ""
    mechanism_tags = []
    for tag in claim.mechanism_tags:
        normalized_tag = normalize_text(tag)
        if not normalized_tag:
            continue
        mechanism_tags.append(canonicalize_mechanism_tag(normalized_tag) or normalized_tag)

    return Claim(
        claim_id=claim.claim_id,
        source_id=claim.source_id,
        intervention=canonicalize_intervention(normalized_intervention) or normalized_intervention,
        outcome=canonicalize_outcome(normalized_outcome) or normalized_outcome,
        effect=normalize_effect(claim.effect),
        summary=claim.summary.strip(),
        mechanism_tags=sorted(set(mechanism_tags)),
        confidence=normalize_text(claim.confidence) or "medium",
        evidence_type=normalize_text(claim.evidence_type) or "unknown",
        context=normalize_context(claim.context),
    )


def normalize_claims(claims: Iterable[Claim]) -> list[Claim]:
    return [normalize_claim(claim) for claim in claims]


def comparison_key(claim: Claim) -> tuple[str, str]:
    return claim.intervention, claim.outcome


def context_axes(context: Context) -> dict[str, str]:
    return {k: v for k, v in context.to_dict().items() if v not in (None, "") and k != "notes"}


def compare_contexts(a: Context, b: Context) -> tuple[list[str], list[str]]:
    a_axes = context_axes(a)
    b_axes = context_axes(b)
    keys = sorted(set(a_axes) | set(b_axes))
    shared: list[str] = []
    differing: list[str] = []
    for key in keys:
        if a_axes.get(key) == b_axes.get(key) and key in a_axes and key in b_axes:
            shared.append(key)
        else:
            differing.append(key)
    return shared, differing


def effects_are_opposed(a: str, b: str) -> bool:
    return {a, b} == {"increase", "decrease"}
