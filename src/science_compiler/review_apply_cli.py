from __future__ import annotations

import argparse
import json
from pathlib import Path

from science_compiler.models import Claim
from science_compiler.review_overrides import apply_review_overrides, load_review_overrides


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Apply reviewed claim overrides to extracted claims JSON')
    parser.add_argument('--claims', required=True, help='Input claims JSON path')
    parser.add_argument('--overrides', required=True, help='Review overrides JSON path')
    parser.add_argument('--output', required=True, help='Output reviewed claims JSON path')
    return parser


def main() -> int:
    args = build_parser().parse_args()
    claims = [Claim.from_dict(item) for item in json.loads(Path(args.claims).read_text())]
    overrides = load_review_overrides(args.overrides)
    reviewed = apply_review_overrides(claims, overrides)
    Path(args.output).write_text(json.dumps([claim.to_dict() for claim in reviewed], indent=2))
    print(f'Loaded {len(claims)} claims')
    print(f'Wrote {len(reviewed)} reviewed claims to {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
