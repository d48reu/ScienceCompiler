from __future__ import annotations

from collections import defaultdict

from science_compiler.models import Claim, MechanismFamily


def build_mechanism_families(claims: list[Claim]) -> list[MechanismFamily]:
    grouped: dict[str, list[Claim]] = defaultdict(list)
    for claim in claims:
        tags = claim.mechanism_tags or ["unspecified mechanism"]
        for tag in tags:
            grouped[tag].append(claim)

    families: list[MechanismFamily] = []
    for tag, tag_claims in grouped.items():
        pairs = sorted({f"{claim.intervention} -> {claim.outcome}" for claim in tag_claims})
        notes = (
            f"Mechanism family '{tag}' has {len(tag_claims)} supporting claims spanning "
            f"{len(pairs)} intervention/outcome pair(s)."
        )
        families.append(
            MechanismFamily(
                name=tag,
                claim_ids=sorted({claim.claim_id for claim in tag_claims}),
                intervention_outcomes=pairs,
                evidence_count=len(tag_claims),
                notes=notes,
            )
        )
    return sorted(families, key=lambda x: (-x.evidence_count, x.name))
