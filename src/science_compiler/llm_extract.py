from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from science_compiler.discipline import enforce_claim_discipline
from science_compiler.llm_common import LLMExtractionError, extract_json_text, run_llm
from science_compiler.models import Claim
from science_compiler.normalize import normalize_claims
from science_compiler.refine import refine_claims_with_text

PROMPT_PATH = Path(__file__).resolve().parents[2] / 'prompts' / 'claim_extraction_prompt.txt'


def load_prompt_template(path: str | Path | None = None) -> str:
    prompt_path = Path(path) if path else PROMPT_PATH
    return prompt_path.read_text()


def build_prompt(paper_text: str, source_id: str, prompt_template: str | None = None) -> str:
    template = prompt_template if prompt_template is not None else load_prompt_template()
    return template.format(source_id=source_id, paper_text=paper_text.strip())


def parse_llm_claims_output(output_text: str, source_id: str) -> list[Claim]:
    json_text = extract_json_text(output_text)
    data = json.loads(json_text)
    if isinstance(data, dict):
        if 'claims' in data:
            data = data['claims']
        elif 'intervention' in data and 'outcome' in data:
            data = [data]
    if not isinstance(data, list):
        raise LLMExtractionError('Parsed JSON was not a list of claims.')

    claims: list[Claim] = []
    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise LLMExtractionError(f'Claim at index {idx} is not an object.')
        payload = dict(item)
        payload.setdefault('claim_id', f'C{idx}')
        payload['source_id'] = source_id
        payload.setdefault('mechanism_tags', [])
        payload.setdefault('confidence', 'medium')
        payload.setdefault('evidence_type', 'unknown')
        payload.setdefault('context', {})
        claims.append(Claim.from_dict(payload))
    return normalize_claims(claims)


def extract_claims_from_text(
    paper_text: str,
    source_id: str,
    llm_command: list[str] | None = None,
    prompt_template: str | None = None,
    timeout: int = 180,
    refine: bool = False,
    refine_llm_command: list[str] | None = None,
    refine_prompt_template: str | None = None,
) -> list[Claim]:
    prompt = build_prompt(paper_text, source_id=source_id, prompt_template=prompt_template)
    output = run_llm(prompt, llm_command=llm_command, timeout=timeout)
    claims = parse_llm_claims_output(output, source_id=source_id)
    if refine:
        claims, _ = refine_claims_with_text(
            paper_text,
            claims,
            llm_command=refine_llm_command or llm_command,
            prompt_template=refine_prompt_template,
            timeout=timeout,
        )
    return enforce_claim_discipline(claims)


def extract_claims_from_raw_paths(
    paths: Iterable[str | Path],
    llm_command: list[str] | None = None,
    prompt_template: str | None = None,
    timeout: int = 180,
    refine: bool = False,
    refine_llm_command: list[str] | None = None,
    refine_prompt_template: str | None = None,
) -> list[Claim]:
    claims: list[Claim] = []
    for path in sorted(Path(p) for p in paths):
        source_id = path.stem
        paper_text = path.read_text()
        claims.extend(
            extract_claims_from_text(
                paper_text,
                source_id=source_id,
                llm_command=llm_command,
                prompt_template=prompt_template,
                timeout=timeout,
                refine=refine,
                refine_llm_command=refine_llm_command,
                refine_prompt_template=refine_prompt_template,
            )
        )
    return claims
