from pathlib import Path

from science_compiler.models import Claim, Context
from science_compiler.refine import build_refinement_prompt, parse_refinement_output, refine_claims_with_text


RAW_TEXT = """We administered butyrate orally to mice in an LPS neuroinflammation model.
The treatment reduced IL-6 and TNF-alpha and improved cognition. The authors describe this as reduced neuroinflammation.
Treg expansion is proposed as a mechanism.
"""


def test_build_refinement_prompt_mentions_current_claims_and_headline_goal() -> None:
    claims = [
        Claim(
            claim_id="C1",
            source_id="Paper_A",
            intervention="oral butyrate",
            outcome="il-6",
            effect="decrease",
            summary="Butyrate decreased IL-6.",
            mechanism_tags=["treg expansion"],
            context=Context(species="mouse"),
        )
    ]
    prompt = build_refinement_prompt(RAW_TEXT, claims)
    assert "headline claim" in prompt.lower()
    assert "current extracted claims" in prompt.lower()
    assert "il-6" in prompt.lower()
    assert RAW_TEXT.strip() in prompt


def test_parse_refinement_output_handles_final_claims_object() -> None:
    output = """```json
    {
      "final_claims": [
        {
          "claim_id": "C1",
          "intervention": "oral butyrate",
          "outcome": "neuroinflammation",
          "effect": "decrease",
          "summary": "Oral butyrate reduced neuroinflammation.",
          "mechanism_tags": ["treg expansion"],
          "confidence": "medium",
          "evidence_type": "in_vivo",
          "context": {"species": "mouse"}
        }
      ],
      "dropped_claim_ids": ["C_biomarker"]
    }
    ```"""
    claims, dropped = parse_refinement_output(output, source_id="Paper_A")
    assert len(claims) == 1
    assert claims[0].outcome == "neuroinflammation"
    assert dropped == ["C_biomarker"]


def test_refine_claims_with_text_can_replace_biomarker_with_headline(tmp_path: Path) -> None:
    fake = tmp_path / "fake_refiner.py"
    fake.write_text(
        "import json, sys\n"
        "_ = sys.stdin.read()\n"
        "print(json.dumps({\n"
        "  'final_claims': [{\n"
        "    'claim_id': 'C1',\n"
        "    'intervention': 'oral butyrate',\n"
        "    'outcome': 'neuroinflammation',\n"
        "    'effect': 'decrease',\n"
        "    'summary': 'Oral butyrate reduced neuroinflammation.',\n"
        "    'mechanism_tags': ['treg expansion'],\n"
        "    'confidence': 'medium',\n"
        "    'evidence_type': 'in_vivo',\n"
        "    'context': {'species': 'mouse'}\n"
        "  }],\n"
        "  'dropped_claim_ids': ['C1_raw']\n"
        "}))\n"
    )

    raw_claims = [
        Claim(
            claim_id="C1_raw",
            source_id="Paper_A",
            intervention="oral butyrate",
            outcome="il-6",
            effect="decrease",
            summary="Oral butyrate decreased IL-6.",
            mechanism_tags=["treg expansion"],
            confidence="medium",
            evidence_type="in_vivo",
            context=Context(species="mouse"),
        )
    ]

    final_claims, dropped = refine_claims_with_text(
        RAW_TEXT,
        raw_claims,
        llm_command=["python3", str(fake)],
    )

    assert len(final_claims) == 1
    assert final_claims[0].outcome == "neuroinflammation"
    assert dropped == ["C1_raw"]
