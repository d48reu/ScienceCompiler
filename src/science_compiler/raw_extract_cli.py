from __future__ import annotations

import argparse
import json
import shlex
from pathlib import Path

from science_compiler.llm_extract import extract_claims_from_raw_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Use an LLM to extract structured claims from raw paper text files')
    parser.add_argument('--input-dir', required=True, help='Directory containing raw paper text files')
    parser.add_argument('--glob', default='*.txt', help='Glob for raw text files (default: *.txt)')
    parser.add_argument('--output', required=True, help='Output JSON file for extracted claims')
    parser.add_argument('--llm-command', help='Override extraction LLM command')
    parser.add_argument('--refine-llm-command', help='Optional override command for second-pass refinement')
    parser.add_argument('--no-refine', action='store_true', help='Disable second-pass claim refinement')
    parser.add_argument('--timeout', type=int, default=180, help='Timeout per file in seconds')
    return parser


def main() -> int:
    args = build_parser().parse_args()
    llm_command = shlex.split(args.llm_command) if args.llm_command else None
    refine_llm_command = shlex.split(args.refine_llm_command) if args.refine_llm_command else None
    paths = sorted(Path(args.input_dir).glob(args.glob))
    claims = extract_claims_from_raw_paths(
        paths,
        llm_command=llm_command,
        timeout=args.timeout,
        refine=not args.no_refine,
        refine_llm_command=refine_llm_command,
    )
    Path(args.output).write_text(json.dumps([claim.to_dict() for claim in claims], indent=2))
    print(f'Processed {len(paths)} file(s)')
    print(f'Extracted {len(claims)} claims')
    print(f'Refinement enabled: {not args.no_refine}')
    print(f'Wrote {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
