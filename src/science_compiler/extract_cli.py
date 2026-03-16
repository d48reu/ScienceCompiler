from __future__ import annotations

import argparse
from pathlib import Path

from science_compiler.extractor import extract_claims_from_directory, write_claims_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Extract structured claims from markdown paper notes')
    parser.add_argument('--input-dir', required=True, help='Directory containing markdown note files')
    parser.add_argument('--glob', default='*.md', help='Glob for note files (default: *.md)')
    parser.add_argument('--output', required=True, help='Output JSON file for extracted claims')
    return parser


def main() -> int:
    args = build_parser().parse_args()
    claims = extract_claims_from_directory(Path(args.input_dir), args.glob)
    write_claims_json(claims, args.output)
    print(f'Extracted {len(claims)} claims')
    print(f'Wrote {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
