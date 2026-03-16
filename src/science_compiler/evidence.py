from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, asdict

from science_compiler.models import Claim
from science_compiler.normalize import context_axes


EVIDENCE_BASE = {
    'clinical': 5.0,
    'in_vivo': 4.0,
    'organoid': 3.0,
    'in_vitro': 2.0,
    'review': 1.5,
    'unknown': 1.0,
}

CONFIDENCE_MULTIPLIER = {
    'high': 1.25,
    'medium': 1.0,
    'low': 0.75,
}

EFFECT_DIRECTIONS = ('increase', 'decrease', 'null', 'mixed', 'conditional')


@dataclass(slots=True)
class EvidenceBalance:
    intervention: str
    outcome: str
    weighted_support_by_effect: dict[str, float]
    leading_effect: str
    net_support: float
    claim_count: int

    def to_dict(self) -> dict:
        return asdict(self)


def compute_evidence_weight(claim: Claim) -> float:
    base = EVIDENCE_BASE.get(claim.evidence_type, EVIDENCE_BASE['unknown'])
    confidence = CONFIDENCE_MULTIPLIER.get(claim.confidence, 1.0)
    context_bonus = min(len(context_axes(claim.context)) * 0.1, 0.5)
    mechanism_bonus = min(len(claim.mechanism_tags) * 0.1, 0.3)
    return round(base * confidence + context_bonus + mechanism_bonus, 4)


def summarize_evidence_balance(claims: list[Claim]) -> list[EvidenceBalance]:
    grouped: dict[tuple[str, str], list[Claim]] = defaultdict(list)
    for claim in claims:
        grouped[(claim.intervention, claim.outcome)].append(claim)

    rows: list[EvidenceBalance] = []
    for (intervention, outcome), items in sorted(grouped.items()):
        effect_weights = {k: 0.0 for k in EFFECT_DIRECTIONS}
        for claim in items:
            effect = 'null' if claim.effect == 'null' else claim.effect
            effect_weights.setdefault(effect, 0.0)
            effect_weights[effect] += compute_evidence_weight(claim)

        leading_effect = max(effect_weights.items(), key=lambda kv: kv[1])[0]
        increase = effect_weights.get('increase', 0.0)
        decrease = effect_weights.get('decrease', 0.0)
        net_support = round(decrease - increase, 4)
        if abs(net_support) < 0.25 and increase > 0 and decrease > 0:
            leading_effect = 'mixed'

        rows.append(
            EvidenceBalance(
                intervention=intervention,
                outcome=outcome,
                weighted_support_by_effect={k: round(v, 4) for k, v in effect_weights.items() if v > 0},
                leading_effect=leading_effect,
                net_support=net_support,
                claim_count=len(items),
            )
        )
    return rows
