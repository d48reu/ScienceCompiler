from __future__ import annotations

import json
import os
import re
import subprocess
from urllib import request

DEFAULT_OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://127.0.0.1:11434').rstrip('/')
DEFAULT_OLLAMA_MODEL = os.getenv('SCIENCE_COMPILER_OLLAMA_MODEL', 'qwen3:30b')
FALLBACK_OLLAMA_MODELS = [
    DEFAULT_OLLAMA_MODEL,
    'jackrong-qwen35-opus:27b-q4km',
    'qwen3-coder:30b',
    'qwen3:8b',
]
JSON_BLOCK_RE = re.compile(r'```json\s*(.*?)\s*```', re.DOTALL | re.IGNORECASE)


class LLMExtractionError(RuntimeError):
    pass


def extract_json_text(output_text: str) -> str:
    output_text = output_text.strip()

    try:
        json.loads(output_text)
        return output_text
    except Exception:
        pass

    fenced = JSON_BLOCK_RE.search(output_text)
    if fenced:
        candidate = fenced.group(1).strip()
        json.loads(candidate)
        return candidate

    decoder = json.JSONDecoder()
    for opener in ('{', '['):
        start = output_text.find(opener)
        if start == -1:
            continue
        try:
            parsed, _ = decoder.raw_decode(output_text[start:])
            return json.dumps(parsed)
        except Exception:
            continue

    raise LLMExtractionError('Could not find JSON in model output.')


def _available_ollama_models(timeout: int = 30) -> set[str]:
    try:
        with request.urlopen(f'{DEFAULT_OLLAMA_HOST}/api/tags', timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        return {m['name'] for m in data.get('models', [])}
    except Exception:
        return set()


def _select_ollama_model() -> str:
    available = _available_ollama_models()
    if not available:
        return DEFAULT_OLLAMA_MODEL
    for model in FALLBACK_OLLAMA_MODELS:
        if model in available:
            return model
    return next(iter(available))


def run_ollama_api(prompt: str, timeout: int = 180) -> str:
    model = _select_ollama_model()
    payload = json.dumps({
        'model': model,
        'prompt': prompt,
        'format': 'json',
        'stream': False,
        'options': {
            'temperature': 0,
            'top_p': 0.9,
        },
    }).encode('utf-8')
    req = request.Request(
        f'{DEFAULT_OLLAMA_HOST}/api/generate',
        data=payload,
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as ex:
        raise LLMExtractionError(f'Ollama API call failed using model {model}: {ex}') from ex

    text = data.get('response') or data.get('thinking')
    if not text:
        raise LLMExtractionError(f'Ollama API response missing usable text field: {data}')
    return text


def run_llm(prompt: str, llm_command: list[str] | None = None, timeout: int = 180) -> str:
    if llm_command is None:
        return run_ollama_api(prompt, timeout=timeout)

    proc = subprocess.run(
        llm_command,
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    if proc.returncode != 0:
        raise LLMExtractionError(
            f'LLM command failed with exit code {proc.returncode}: {proc.stderr.strip() or proc.stdout.strip()}'
        )
    return proc.stdout
