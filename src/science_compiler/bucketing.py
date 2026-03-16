from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass

from science_compiler.evidence import compute_evidence_weight
from science_compiler.models import Claim


@dataclass(slots=True)
class FamilyEvidenceBalance:
    intervention_family: str
    disease_family: str
    outcome: str
    weighted_support_by_effect: dict[str, float]
    leading_effect: str
    net_support: float
    claim_count: int

    def to_dict(self) -> dict:
        return asdict(self)


def intervention_family(claim: Claim) -> str:
    text = claim.intervention
    if 'clostridium butyricum' in text or 'microbial production' in text or 'high-fiber inulin diet' in text:
        return 'microbiome-mediated butyrate'
    if 'scfa supplementation' in text:
        return 'mixed scfa intervention'
    if 'butyrate' in text:
        return 'direct butyrate'
    return 'other'


def disease_family(claim: Claim) -> str:
    disease = (claim.context.disease_state or '')
    model = (claim.context.model_system or '')
    blob = f'{disease} {model}'.lower()

    if 'parkinson' in blob or 'mptp' in blob or 'rotenone' in blob:
        return 'parkinsonian'
    if 'alzheimer' in blob or '5xfad' in blob or 'app/ps1' in blob or 'samp8' in blob or 'amyloid' in blob:
        return 'alzheimer_related'
    if 'cardiac arrest' in blob or 'stroke' in blob or 'traumatic brain injury' in blob or 'controlled cortical impact' in blob:
        return 'acute_injury'
    if 'alcohol' in blob or 'ethanol' in blob:
        return 'alcohol_related'
    if 'lead' in blob:
        return 'toxic_exposure'
    if 'ulcerative colitis' in blob or 'dss' in blob or 'inflammatory bowel' in blob:
        return 'gut_inflammation'
    if 'depression' in blob or 'lps-induced depression' in blob:
        return 'behavioral_inflammation'
    if 'aging' in blob or 'aged' in blob:
        return 'aging'
    if 'overnutrition' in blob or 'high-fat' in blob or 'obesity' in blob:
        return 'metabolic_inflammation'
    return 'other'


def summarize_family_evidence_balance(claims: list[Claim]) -> list[FamilyEvidenceBalance]:
    grouped: dict[tuple[str, str, str], list[Claim]] = defaultdict(list)
    for claim in claims:
        grouped[(intervention_family(claim), disease_family(claim), claim.outcome)].append(claim)

    rows: list[FamilyEvidenceBalance] = []
    for (ifam, dfam, outcome), items in sorted(grouped.items()):
        effect_weights: dict[str, float] = defaultdict(float)
        for claim in items:
            effect_weights[claim.effect] += compute_evidence_weight(claim)
        inc = effect_weights.get('increase', 0.0)
        dec = effect_weights.get('decrease', 0.0)
        leading = max(effect_weights.items(), key=lambda kv: kv[1])[0]
        net = round(dec - inc, 4)
        if abs(net) < 0.25 and inc > 0 and dec > 0:
            leading = 'mixed'
        rows.append(
            FamilyEvidenceBalance(
                intervention_family=ifam,
                disease_family=dfam,
                outcome=outcome,
                weighted_support_by_effect={k: round(v, 4) for k, v in effect_weights.items()},
                leading_effect=leading,
                net_support=net,
                claim_count=len(items),
            )
        )
    return rows
