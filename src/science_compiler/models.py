from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class Context:
    species: str | None = None
    model_system: str | None = None
    tissue: str | None = None
    disease_state: str | None = None
    microbiome_status: str | None = None
    barrier_status: str | None = None
    administration_route: str | None = None
    dose_level: str | None = None
    time_horizon: str | None = None
    notes: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "Context":
        return cls(**(data or {}))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Claim:
    claim_id: str
    source_id: str
    intervention: str
    outcome: str
    effect: str
    summary: str
    mechanism_tags: list[str] = field(default_factory=list)
    confidence: str = "medium"
    evidence_type: str = "unknown"
    context: Context = field(default_factory=Context)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Claim":
        payload = dict(data)
        payload["context"] = Context.from_dict(payload.get("context"))
        payload.setdefault("mechanism_tags", [])
        payload.setdefault("confidence", "medium")
        payload.setdefault("evidence_type", "unknown")
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        out = asdict(self)
        out["context"] = self.context.to_dict()
        return out


@dataclass(slots=True)
class Contradiction:
    claim_a_id: str
    claim_b_id: str
    kind: str
    intervention: str
    outcome: str
    claim_a_effect: str
    claim_b_effect: str
    differing_context_axes: list[str]
    shared_context_axes: list[str]
    hypothesis: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class MechanismFamily:
    name: str
    claim_ids: list[str]
    intervention_outcomes: list[str]
    evidence_count: int
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ExperimentProposal:
    title: str
    contradiction_claim_ids: list[str]
    rationale: str
    candidate_moderators: list[str]
    design: list[str]
    predictions: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
