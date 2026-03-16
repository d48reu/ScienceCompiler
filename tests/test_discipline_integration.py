from pathlib import Path

from science_compiler.llm_extract import extract_claims_from_text


RAW_TEXT = 'dummy'


def test_extract_claims_from_text_applies_discipline_after_refinement(tmp_path: Path) -> None:
    extractor = tmp_path / 'extractor.py'
    extractor.write_text(
        "import json, sys\n"
        "_ = sys.stdin.read()\n"
        "print(json.dumps([\n"
        " {'claim_id':'C1','intervention':'sodium butyrate','outcome':'neuroinflammation','effect':'decrease','summary':'a','mechanism_tags':[],'confidence':'high','evidence_type':'in_vivo','context':{'species':'mouse'}},\n"
        " {'claim_id':'C2','intervention':'sodium butyrate','outcome':'motor performance','effect':'increase','summary':'b','mechanism_tags':[],'confidence':'medium','evidence_type':'in_vivo','context':{'species':'mouse'}},\n"
        " {'claim_id':'C3','intervention':'sodium butyrate','outcome':'memory deficits','effect':'decrease','summary':'c','mechanism_tags':[],'confidence':'medium','evidence_type':'in_vivo','context':{'species':'mouse'}},\n"
        " {'claim_id':'C4','intervention':'sodium butyrate','outcome':'il-6','effect':'decrease','summary':'d','mechanism_tags':[],'confidence':'medium','evidence_type':'in_vivo','context':{'species':'mouse'}},\n"
        " {'claim_id':'C5','intervention':'sodium butyrate','outcome':'treg abundance','effect':'increase','summary':'e','mechanism_tags':[],'confidence':'high','evidence_type':'in_vivo','context':{'species':'mouse'}}\n"
        "]))\n"
    )
    claims = extract_claims_from_text(RAW_TEXT, source_id='P1', llm_command=['python3', str(extractor)], refine=False)
    kept = {c.claim_id for c in claims}
    assert len(claims) <= 4
    assert 'C4' not in kept
