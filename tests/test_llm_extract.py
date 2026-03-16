from pathlib import Path

from science_compiler.llm_extract import build_prompt, parse_llm_claims_output, extract_claims_from_text


RAW_TEXT = """Paper notes
Butyrate was administered orally to mice in an LPS neuroinflammation model.
The paper reports reduced IL-6 and TNF-alpha and improved cognition.
Authors propose Treg expansion and HDAC inhibition as mechanisms.
Barrier status was intact.
"""


def test_build_prompt_mentions_schema_and_source() -> None:
    prompt = build_prompt(RAW_TEXT, source_id="Paper_A_2021")
    assert "Paper_A_2021" in prompt
    assert "JSON array" in prompt
    assert "claim_id" in prompt
    assert RAW_TEXT in prompt


def test_parse_llm_claims_output_handles_fenced_json() -> None:
    output = """Here you go.
```json
[
  {
    "claim_id": "C1",
    "intervention": "butyrate administration",
    "outcome": "neuroinflammation",
    "effect": "decrease",
    "summary": "Butyrate reduced inflammatory cytokines.",
    "mechanism_tags": ["treg expansion", "hdac inhibition"],
    "confidence": "medium",
    "evidence_type": "in_vivo",
    "context": {"species": "mouse", "barrier_status": "intact"}
  }
]
```
"""
    claims = parse_llm_claims_output(output, source_id="Paper_A_2021")
    assert len(claims) == 1
    assert claims[0].source_id == "Paper_A_2021"
    assert claims[0].effect == "decrease"
    assert claims[0].context.barrier_status == "intact"


def test_extract_claims_from_text_with_fake_command(tmp_path: Path) -> None:
    fake = tmp_path / "fake_llm.py"
    fake.write_text(
        "import json, sys\n"
        "_ = sys.stdin.read()\n"
        "print(json.dumps({\n"
        "  'claim_id': 'C1',\n"
        "  'intervention': 'butyrate administration',\n"
        "  'outcome': 'neuroinflammation',\n"
        "  'effect': 'decrease',\n"
        "  'summary': 'Butyrate reduced inflammatory cytokines.',\n"
        "  'mechanism_tags': ['treg expansion'],\n"
        "  'confidence': 'medium',\n"
        "  'evidence_type': 'in_vivo',\n"
        "  'context': {'species': 'mouse', 'barrier_status': 'intact'}\n"
        "}))\n"
    )
    claims = extract_claims_from_text(
        RAW_TEXT,
        source_id="Paper_A_2021",
        llm_command=["python3", str(fake)],
    )
    assert len(claims) == 1
    assert claims[0].outcome == "neuroinflammation"
    assert claims[0].mechanism_tags == ["treg expansion"]
