from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from science_compiler.bucketing import summarize_family_evidence_balance
from science_compiler.contradictions import detect_contradictions
from science_compiler.curation import consolidate_claims, rank_claims
from science_compiler.evidence import compute_evidence_weight, summarize_evidence_balance
from science_compiler.experiments import propose_experiments
from science_compiler.mechanisms import build_mechanism_families
from science_compiler.models import Claim
from science_compiler.normalize import normalize_claims


def load_claims(path: str | Path) -> list[Claim]:
    raw = json.loads(Path(path).read_text())
    return normalize_claims([Claim.from_dict(item) for item in raw])


def ensure_unique_claim_ids(claims: list[Claim]) -> list[Claim]:
    counts: dict[str, int] = {}
    for claim in claims:
        counts[claim.claim_id] = counts.get(claim.claim_id, 0) + 1

    out: list[Claim] = []
    for claim in claims:
        if counts[claim.claim_id] == 1:
            out.append(claim)
        else:
            out.append(
                Claim(
                    claim_id=f"{claim.source_id}::{claim.claim_id}",
                    source_id=claim.source_id,
                    intervention=claim.intervention,
                    outcome=claim.outcome,
                    effect=claim.effect,
                    summary=claim.summary,
                    mechanism_tags=list(claim.mechanism_tags),
                    confidence=claim.confidence,
                    evidence_type=claim.evidence_type,
                    context=claim.context,
                )
            )
    return out


def compile_claims(claims: list[Claim]) -> dict[str, Any]:
    normalized = normalize_claims(claims)
    curated = ensure_unique_claim_ids(consolidate_claims(normalized))
    ranked = rank_claims(curated)
    contradictions = detect_contradictions(curated)
    mechanisms = build_mechanism_families(curated)
    experiments = propose_experiments(contradictions, curated)
    evidence_balance = summarize_evidence_balance(curated)
    family_evidence_balance = summarize_family_evidence_balance(curated)

    return {
        "summary": {
            "raw_claim_count": len(normalized),
            "claim_count": len(curated),
            "contradiction_count": len(contradictions),
            "mechanism_family_count": len(mechanisms),
            "experiment_proposal_count": len(experiments),
        },
        "claims": [
            {**claim.to_dict(), "evidence_weight": compute_evidence_weight(claim)} for claim in curated
        ],
        "ranked_claims": [
            {
                "score": item.score,
                "tier": item.tier,
                "evidence_weight": compute_evidence_weight(item.claim),
                "claim": item.claim.to_dict(),
            }
            for item in ranked
        ],
        "evidence_balance": [item.to_dict() for item in evidence_balance],
        "family_evidence_balance": [item.to_dict() for item in family_evidence_balance],
        "contradictions": [item.to_dict() for item in contradictions],
        "mechanism_families": [item.to_dict() for item in mechanisms],
        "experiment_proposals": [item.to_dict() for item in experiments],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines: list[str] = []
    summary = report["summary"]
    lines.append("# Science Compiler Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Raw claims: {summary['raw_claim_count']}")
    lines.append(f"- Curated claims: {summary['claim_count']}")
    lines.append(f"- Contradictions: {summary['contradiction_count']}")
    lines.append(f"- Mechanism families: {summary['mechanism_family_count']}")
    lines.append(f"- Experiment proposals: {summary['experiment_proposal_count']}")
    lines.append("")

    lines.append("## Claims")
    lines.append("")
    for claim in report["claims"]:
        ctx = {k: v for k, v in claim['context'].items() if v not in (None, '')}
        lines.append(f"- {claim['claim_id']} | {claim['intervention']} -> {claim['outcome']} | effect={claim['effect']} | source={claim['source_id']} | evidence_weight={claim['evidence_weight']:.2f}")
        lines.append(f"  - summary: {claim['summary']}")
        if claim["mechanism_tags"]:
            lines.append(f"  - mechanism tags: {', '.join(claim['mechanism_tags'])}")
        if ctx:
            rendered_ctx = ", ".join(f"{k}={v}" for k, v in ctx.items())
            lines.append(f"  - context: {rendered_ctx}")
    lines.append("")

    lines.append("## Ranked Claims")
    lines.append("")
    for item in report["ranked_claims"]:
        claim = item["claim"]
        lines.append(
            f"- score={item['score']} | evidence_weight={item['evidence_weight']:.2f} | tier={item['tier']} | {claim['claim_id']} | {claim['intervention']} -> {claim['outcome']}"
        )
    lines.append("")

    lines.append("## Evidence Balance")
    lines.append("")
    for row in report["evidence_balance"]:
        support = ', '.join(f"{k}={v:.2f}" for k, v in row['weighted_support_by_effect'].items())
        lines.append(
            f"- {row['intervention']} -> {row['outcome']} | leading_effect={row['leading_effect']} | net_support={row['net_support']:.2f} | claims={row['claim_count']}"
        )
        lines.append(f"  - weighted support: {support}")
    lines.append("")

    lines.append("## Family-Split Evidence Balance")
    lines.append("")
    for row in report["family_evidence_balance"]:
        support = ', '.join(f"{k}={v:.2f}" for k, v in row['weighted_support_by_effect'].items())
        lines.append(
            f"- intervention_family={row['intervention_family']} | disease_family={row['disease_family']} | outcome={row['outcome']} | leading_effect={row['leading_effect']} | net_support={row['net_support']:.2f} | claims={row['claim_count']}"
        )
        lines.append(f"  - weighted support: {support}")
    lines.append("")

    lines.append("## Contradictions")
    lines.append("")
    if not report["contradictions"]:
        lines.append("- None")
    for item in report["contradictions"]:
        lines.append(
            f"- {item['claim_a_id']} vs {item['claim_b_id']} | {item['intervention']} -> {item['outcome']} | kind={item['kind']}"
        )
        lines.append(f"  - differing context axes: {', '.join(item['differing_context_axes']) or 'none'}")
        lines.append(f"  - hypothesis: {item['hypothesis']}")
    lines.append("")

    lines.append("## Mechanism Families")
    lines.append("")
    for item in report["mechanism_families"]:
        lines.append(f"- {item['name']} | evidence_count={item['evidence_count']}")
        lines.append(f"  - claims: {', '.join(item['claim_ids'])}")
        lines.append(f"  - intervention/outcomes: {', '.join(item['intervention_outcomes'])}")
    lines.append("")

    lines.append("## Experiment Proposals")
    lines.append("")
    for item in report["experiment_proposals"]:
        lines.append(f"- {item['title']}")
        lines.append(f"  - contradiction claims: {', '.join(item['contradiction_claim_ids'])}")
        lines.append(f"  - rationale: {item['rationale']}")
        lines.append(f"  - candidate moderators: {', '.join(item['candidate_moderators'])}")
        lines.append("  - design:")
        for step in item['design']:
            lines.append(f"    - {step}")
        lines.append("  - predictions:")
        for pred in item['predictions']:
            lines.append(f"    - {pred}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_report(report: dict[str, Any], output_path: str | Path, markdown_path: str | Path | None = None) -> None:
    Path(output_path).write_text(json.dumps(report, indent=2))
    if markdown_path is not None:
        Path(markdown_path).write_text(render_markdown(report))
