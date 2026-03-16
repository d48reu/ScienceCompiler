from pathlib import Path

from science_compiler.extractor import parse_markdown_note, extract_claims_from_paths


NOTE_TEXT = """---
source_id: Paper_A_2021
title: Butyrate in LPS mice
---

## Claim: C1
- intervention: butyrate administration
- outcome: neuroinflammation
- effect: decrease
- summary: Oral butyrate reduced inflammatory cytokines in an LPS mouse model.
- mechanism_tags: treg expansion; hdac inhibition
- confidence: medium
- evidence_type: in_vivo
- species: mouse
- model_system: lps model
- tissue: brain
- disease_state: acute neuroinflammation
- microbiome_status: conventional
- barrier_status: intact
- administration_route: oral
- dose_level: medium
- time_horizon: acute

## Claim: C2
- intervention: butyrate administration
- outcome: treg abundance
- effect: increase
- summary: Butyrate increased Treg abundance.
- mechanism_tags: treg expansion
- confidence: high
- evidence_type: in_vivo
- species: mouse
- tissue: colon
"""


def test_parse_markdown_note_into_claims() -> None:
    claims = parse_markdown_note(NOTE_TEXT)
    assert len(claims) == 2
    assert claims[0].source_id == "Paper_A_2021"
    assert claims[0].claim_id == "C1"
    assert claims[0].context.barrier_status == "intact"
    assert claims[1].outcome == "treg abundance"


def test_extract_claims_from_paths(tmp_path: Path) -> None:
    note = tmp_path / "paper_a.md"
    note.write_text(NOTE_TEXT)
    claims = extract_claims_from_paths([note])
    assert len(claims) == 2
    assert {claim.claim_id for claim in claims} == {"C1", "C2"}
