from pathlib import Path

from science_compiler.compiler import compile_claims
from science_compiler.extractor import extract_claims_from_paths


NOTE_A = """---
source_id: Paper_A_2021
---

## Claim: C1
- intervention: butyrate administration
- outcome: neuroinflammation
- effect: decrease
- summary: Butyrate reduced neuroinflammation.
- mechanism_tags: treg expansion
- species: mouse
- barrier_status: intact
- microbiome_status: conventional
"""

NOTE_B = """---
source_id: Paper_B_2022
---

## Claim: C2
- intervention: butyrate administration
- outcome: neuroinflammation
- effect: increase
- summary: Butyrate increased neuroinflammation in dysbiotic mice.
- mechanism_tags: barrier conditionality
- species: mouse
- barrier_status: impaired
- microbiome_status: dysbiotic
"""


def test_notes_flow_into_report(tmp_path: Path) -> None:
    a = tmp_path / "a.md"
    b = tmp_path / "b.md"
    a.write_text(NOTE_A)
    b.write_text(NOTE_B)

    claims = extract_claims_from_paths([a, b])
    report = compile_claims(claims)

    assert report["summary"]["claim_count"] == 2
    assert report["summary"]["contradiction_count"] == 1
    assert report["summary"]["experiment_proposal_count"] == 1
