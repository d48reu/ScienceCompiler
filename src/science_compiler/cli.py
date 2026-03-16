from __future__ import annotations

import argparse

from science_compiler.compiler import compile_claims, load_claims, write_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile structured scientific claims into contradictions and experiment proposals")
    parser.add_argument("--input", required=True, help="Path to input claims JSON")
    parser.add_argument("--output", required=True, help="Path to output report JSON")
    parser.add_argument("--markdown", help="Optional path to output report Markdown")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    claims = load_claims(args.input)
    report = compile_claims(claims)
    write_report(report, args.output, args.markdown)
    print(f"Compiled {report['summary']['claim_count']} claims")
    print(f"Contradictions: {report['summary']['contradiction_count']}")
    print(f"Mechanism families: {report['summary']['mechanism_family_count']}")
    print(f"Experiment proposals: {report['summary']['experiment_proposal_count']}")
    print(f"Wrote {args.output}")
    if args.markdown:
        print(f"Wrote {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
