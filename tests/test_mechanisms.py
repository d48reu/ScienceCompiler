from science_compiler.mechanisms import build_mechanism_families
from science_compiler.models import Claim, Context
from science_compiler.normalize import normalize_claims


def test_groups_claims_into_mechanism_families() -> None:
    claims = normalize_claims([
        Claim("A", "p1", "butyrate", "neuroinflammation", "decrease", "x", ["treg expansion"], context=Context()),
        Claim("B", "p2", "butyrate", "treg abundance", "increase", "x", ["treg expansion"], context=Context()),
        Claim("C", "p3", "butyrate", "neuroinflammation", "increase", "x", ["barrier conditionality"], context=Context()),
    ])
    families = build_mechanism_families(claims)
    names = [family.name for family in families]
    assert "treg expansion" in names
    assert "barrier conditionality" in names
    treg = next(f for f in families if f.name == "treg expansion")
    assert treg.evidence_count == 2
