from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from science_compiler.models import Claim, Context


def load_review_overrides(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text())
    data.setdefault('updates', [])
    data.setdefault('drops', [])
    data.setdefault('adds', [])
    return data


def _claim_key(claim: Claim) -> tuple[str, str]:
    return claim.source_id, claim.claim_id


def _drop_keys(overrides: dict[str, Any]) -> set[tuple[str, str]]:
    return {(item['source_id'], item['claim_id']) for item in overrides.get('drops', [])}


def _update_map(overrides: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    return {
        (item['source_id'], item['claim_id']): item.get('set', {})
        for item in overrides.get('updates', [])
    }


def _apply_update(claim: Claim, patch: dict[str, Any]) -> Claim:
    payload = claim.to_dict()
    for key, value in patch.items():
        if key == 'context' and isinstance(value, dict):
            context_payload = dict(payload.get('context', {}))
            context_payload.update(value)
            payload['context'] = context_payload
        else:
            payload[key] = value
    return Claim.from_dict(payload)


def apply_review_overrides(claims: list[Claim], overrides: dict[str, Any]) -> list[Claim]:
    drop_keys = _drop_keys(overrides)
    updates = _update_map(overrides)
    out: list[Claim] = []

    for claim in claims:
        key = _claim_key(claim)
        if key in drop_keys:
            continue
        if key in updates:
            out.append(_apply_update(claim, updates[key]))
        else:
            out.append(claim)

    for item in overrides.get('adds', []):
        out.append(Claim.from_dict(item))

    return out
