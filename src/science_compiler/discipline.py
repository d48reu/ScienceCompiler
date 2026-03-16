from __future__ import annotations

from collections import defaultdict

from science_compiler.curation import classify_claim_tier, score_claim
from science_compiler.models import Claim
from science_compiler.normalize import normalize_claims


MAX_HEADLINE_PER_SOURCE = 3
MAX_MECHANISTIC_PER_SOURCE = 1


def enforce_claim_discipline(claims: list[Claim]) -> list[Claim]:
    normalized = normalize_claims(claims)
    by_source: dict[str, list[Claim]] = defaultdict(list)
    for claim in normalized:
        by_source[claim.source_id].append(claim)

    kept: list[Claim] = []
    for source_id in sorted(by_source):
        source_claims = by_source[source_id]
        ranked = sorted(source_claims, key=lambda c: (-score_claim(c).score, c.claim_id))

        headline_like = []
        mechanistic = []
        leftovers = []
        for claim in ranked:
            tier = classify_claim_tier(claim)
            if tier in {'headline', 'supporting'}:
                headline_like.append(claim)
            elif tier == 'mechanistic':
                mechanistic.append(claim)
            else:
                leftovers.append(claim)

        selected = headline_like[:MAX_HEADLINE_PER_SOURCE]
        selected.extend(mechanistic[:MAX_MECHANISTIC_PER_SOURCE])

        # only use leftovers if we somehow selected nothing
        if not selected and leftovers:
            selected.append(leftovers[0])

        kept.extend(sorted(selected, key=lambda c: c.claim_id))

    return kept
