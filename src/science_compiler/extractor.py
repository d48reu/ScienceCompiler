from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
CLAIM_HEADER_RE = re.compile(r"^##\s*Claim\s*:?\s*(.+?)\s*$", re.IGNORECASE)
BULLET_RE = re.compile(r"^-\s*([A-Za-z0-9_\.]+)\s*:\s*(.+?)\s*$")
CONTEXT_FIELDS = set(Context.__dataclass_fields__.keys())


def _parse_key_values(lines: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        out[key.strip()] = value.strip()
    return out


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = _parse_key_values(match.group(1).splitlines())
    body = text[match.end():]
    return meta, body


def _split_claim_blocks(body: str) -> list[tuple[str, list[str]]]:
    blocks: list[tuple[str, list[str]]] = []
    current_id: str | None = None
    current_lines: list[str] = []

    for raw_line in body.splitlines():
        header = CLAIM_HEADER_RE.match(raw_line.strip())
        if header:
            if current_id is not None:
                blocks.append((current_id, current_lines))
            current_id = header.group(1).strip()
            current_lines = []
        elif current_id is not None:
            current_lines.append(raw_line)

    if current_id is not None:
        blocks.append((current_id, current_lines))
    return blocks


def _parse_claim_block(claim_id: str, lines: list[str], source_id: str) -> Claim:
    raw: dict[str, str] = {}
    for line in lines:
        match = BULLET_RE.match(line.strip())
        if match:
            raw[match.group(1).strip()] = match.group(2).strip()

    mechanism_tags = [tag.strip() for tag in re.split(r"[;,]", raw.get('mechanism_tags', '')) if tag.strip()]

    context_payload = {k: v for k, v in raw.items() if k in CONTEXT_FIELDS}
    for key, value in list(raw.items()):
        if key.startswith('context.'):
            context_payload[key.split('.', 1)[1]] = value

    return Claim(
        claim_id=claim_id,
        source_id=raw.get('source_id', source_id),
        intervention=raw.get('intervention', ''),
        outcome=raw.get('outcome', ''),
        effect=raw.get('effect', ''),
        summary=raw.get('summary', ''),
        mechanism_tags=mechanism_tags,
        confidence=raw.get('confidence', 'medium'),
        evidence_type=raw.get('evidence_type', 'unknown'),
        context=Context.from_dict(context_payload),
    )


def parse_markdown_note(text: str, fallback_source_id: str = 'unknown_source') -> list[Claim]:
    meta, body = _parse_frontmatter(text)
    source_id = meta.get('source_id', fallback_source_id)
    blocks = _split_claim_blocks(body)
    claims = [_parse_claim_block(claim_id, lines, source_id) for claim_id, lines in blocks]
    return normalize_claims(claims)


def extract_claims_from_paths(paths: Iterable[str | Path]) -> list[Claim]:
    claims: list[Claim] = []
    for path in sorted(Path(p) for p in paths):
        text = path.read_text()
        fallback = path.stem
        claims.extend(parse_markdown_note(text, fallback_source_id=fallback))
    return claims


def extract_claims_from_directory(directory: str | Path, glob: str = '*.md') -> list[Claim]:
    path = Path(directory)
    return extract_claims_from_paths(sorted(path.glob(glob)))


def write_claims_json(claims: list[Claim], output_path: str | Path) -> None:
    Path(output_path).write_text(json.dumps([claim.to_dict() for claim in claims], indent=2))
