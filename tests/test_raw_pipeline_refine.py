from pathlib import Path

from science_compiler.llm_extract import extract_claims_from_text


RAW_TEXT = """We administered butyrate orally to mice in an LPS neuroinflammation model.
The treatment reduced IL-6 and TNF-alpha and improved cognition. The authors describe this as reduced neuroinflammation.
"""


def test_extract_claims_from_text_can_run_second_pass_refinement(tmp_path: Path) -> None:
    extractor = tmp_path / "extractor.py"
    refiner = tmp_path / "refiner.py"

    extractor.write_text(
        "import json, sys\n"
        "_ = sys.stdin.read()\n"
        "print(json.dumps([{\n"
        "  'claim_id': 'C1_raw',\n"
        "  'intervention': 'oral butyrate',\n"
        "  'outcome': 'il-6',\n"
        "  'effect': 'decrease',\n"
        "  'summary': 'Oral butyrate decreased IL-6.',\n"
        "  'mechanism_tags': ['treg expansion'],\n"
        "  'confidence': 'medium',\n"
        "  'evidence_type': 'in_vivo',\n"
        "  'context': {'species': 'mouse'}\n"
        "}]))\n"
    )

    refiner.write_text(
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

    claims = extract_claims_from_text(
        RAW_TEXT,
        source_id="Paper_A",
        llm_command=["python3", str(extractor)],
        refine=True,
        refine_llm_command=["python3", str(refiner)],
    )

    assert len(claims) == 1
    assert claims[0].outcome == "neuroinflammation"
