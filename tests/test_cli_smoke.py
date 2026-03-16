import json
from pathlib import Path

from science_compiler.compiler import compile_claims, load_claims, render_markdown


EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "microbiome_neuroinflammation_claims.json"


def test_compiler_smoke() -> None:
    claims = load_claims(EXAMPLE)
    report = compile_claims(claims)
    assert report["summary"]["claim_count"] == 8
    assert report["summary"]["contradiction_count"] >= 2
    assert report["summary"]["experiment_proposal_count"] >= 2

    markdown = render_markdown(report)
    assert "## Contradictions" in markdown
    assert "## Experiment Proposals" in markdown
    json.dumps(report)
