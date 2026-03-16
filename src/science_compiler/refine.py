from __future__ import annotations

import json
from pathlib import Path

from science_compiler.llm_common import LLMExtractionError, extract_json_text, run_llm
from science_compiler.models import Claim
from science_compiler.normalize import normalize_claims

PROMPT_PATH = Path(__file__).resolve().parents[2] / 'prompts' / 'claim_refinement_prompt.txt'


def load_refinement_prompt_template(path: str | Path | None = None) -> str:
    prompt_path = Path(path) if path else PROMPT_PATH
    return prompt_path.read_text()


def build_refinement_prompt(
    paper_text: str,
    claims: list[Claim],
    source_id: str | None = None,
    prompt_template: str | None = None,
) -> str:
    source = source_id or (claims[0].source_id if claims else 'unknown_source')
    template = prompt_template if prompt_template is not None else load_refinement_prompt_template()
    claims_json = json.dumps([claim.to_dict() for claim in claims], indent=2)
    return template.format(source_id=source, claims_json=claims_json, paper_text=paper_text.strip())


def parse_refinement_output(output_text: str, source_id: str) -> tuple[list[Claim], list[str]]:
    json_text = extract_json_text(output_text)
    data = json.loads(json_text)
    if not isinstance(data, dict):
        raise LLMExtractionError('Refinement output must be a JSON object.')

    final_claims_data = data.get('final_claims', [])
    dropped_claim_ids = data.get('dropped_claim_ids', [])
    if not isinstance(final_claims_data, list):
        raise LLMExtractionError('final_claims must be a list.')
    if not isinstance(dropped_claim_ids, list):
        raise LLMExtractionError('dropped_claim_ids must be a list.')

    claims: list[Claim] = []
    for idx, item in enumerate(final_claims_data, start=1):
        if not isinstance(item, dict):
            raise LLMExtractionError(f'final_claims[{idx}] is not an object.')
        payload = dict(item)
        payload.setdefault('claim_id', f'C{idx}')
        payload['source_id'] = source_id
        payload.setdefault('mechanism_tags', [])
        payload.setdefault('confidence', 'medium')
        payload.setdefault('evidence_type', 'unknown')
        payload.setdefault('context', {})
        claims.append(Claim.from_dict(payload))

    return normalize_claims(claims), [str(x) for x in dropped_claim_ids]


def refine_claims_with_text(
    paper_text: str,
    claims: list[Claim],
    llm_command: list[str] | None = None,
    prompt_template: str | None = None,
    timeout: int = 180,
) -> tuple[list[Claim], list[str]]:
    if not claims:
        return [], []
    source_id = claims[0].source_id
    prompt = build_refinement_prompt(paper_text, claims, source_id=source_id, prompt_template=prompt_template)
    output = run_llm(prompt, llm_command=llm_command, timeout=timeout)
    return parse_refinement_output(output, source_id=source_id)
