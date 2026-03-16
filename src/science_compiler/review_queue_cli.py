from __future__ import annotations

import argparse
from pathlib import Path

from science_compiler.review_queue import build_review_queue


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Generate human review queue CSVs from a compiler report JSON')
    parser.add_argument('--report', required=True, help='Compiler report JSON path')
    parser.add_argument('--output-dir', required=True, help='Directory for review CSVs')
    return parser


def main() -> int:
    args = build_parser().parse_args()
    build_review_queue(Path(args.report), Path(args.output_dir))
    print(f'Wrote review queue to {args.output_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
