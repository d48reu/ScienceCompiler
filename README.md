# Science Compiler

Science Compiler is a local-first AI research workflow for turning scientific literature into structured, computable objects instead of vague summaries.

Instead of stopping at:

> “the literature is mixed and context-dependent”

it tries to produce:
- structured claims
- contradiction maps
- weighted evidence balances
- mechanism groupings
- follow-up experiment ideas
- human review queues

In short:

`papers -> claims -> contradictions / tradeoffs -> better scientific questions`

## What is this trying to do?

Most “AI for science” tools do one of two things:
1. summarize papers into prose
2. predict on datasets

Science Compiler targets a different bottleneck: making disagreements inside the literature legible and computable.

The goal is not to replace researchers.
The goal is to help them see:
- where evidence actually agrees
- where it breaks
- which contexts flip the apparent effect
- what should be tested next

## Why this is interesting

The project treats scientific literature less like text to chat over and more like something that can be compiled into a structured intermediate representation.

That enables workflows like:
- finding contradiction clusters instead of averaging them away
- grouping mechanism families across papers
- weighting evidence by claim type and context
- splitting results by disease family or intervention family
- generating candidate moderator-focused experiments
- building human review loops on top of AI extraction

## Current capabilities

The current prototype includes:
- raw-text claim extraction
- second-pass claim refinement
- curation and ranking
- ontology / canonicalization
- evidence weighting
- contradiction detection
- family-split evidence views
- review override workflow
- review queue CSV generation

## What it has already found

### 1. Butyrate / neuroinflammation
The prototype found a real context-dependent sign flip.

Current best read:
- direct sodium butyrate looks mostly anti-neuroinflammatory across several non-parkinsonian contexts
- but a parkinsonian MPTP paper points the other way

That makes the useful scientific question:

Why does the sign flip in that disease context?

Relevant files:
- `corpora/butyrate_neuroinflammation/reports/compiler_report_gold.md`
- `corpora/butyrate_neuroinflammation/reports/EXECUTIVE_BRIEF.md`
- `corpora/butyrate_neuroinflammation/reports/DRAFT_SCIENTIFIC_MEMO.md`

### 2. Senolytics / aging
In a second domain, the structure changed.

Instead of one main contradiction, the system surfaced a benefit-vs-harm tradeoff map:
- some senolytics improve lifespan, function, or resilience
- some agents or contexts show null effects, tissue-specific harm, or sex-specific downside

That matters because it shows the workflow is not locked to one scientific pattern.

Relevant files:
- `corpora/senolytics_aging/reports/TRADEOFF_MEMO.md`
- `corpora/senolytics_aging/reports/EXECUTIVE_BRIEF.md`
- `corpora/senolytics_aging/reports/core_tradeoff_contrast.md`

## Design principles

- Local-first by default
- Human review is part of the workflow, not an afterthought
- Preserve contradiction instead of erasing it
- Prefer explicit structure over chatty prose
- Treat AI as a scientific instrument, not a mascot

## High-level pipeline

1. Ingest paper text or structured notes
2. Extract claims
3. Refine claims
4. Canonicalize interventions / outcomes / mechanisms
5. Weight evidence
6. Detect contradiction or tradeoff structure
7. Generate experiment ideas
8. Produce human review artifacts

## Repo layout

- `src/science_compiler/` — core package
- `prompts/` — extraction and refinement prompts
- `tests/` — test suite
- `examples/` — small example inputs
- `corpora/` — domain-specific corpora, reports, and review artifacts
- `hackathon/` — demo scripts, submission text, and presentation assets

## Quick start

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

### Run tests

```bash
pytest -q
```

### Example: compile markdown notes

```bash
python -m science_compiler.extract_cli \
  --input-dir examples/microbiome_notes \
  --output reports/microbiome_extracted_claims.json

python -m science_compiler.cli \
  --input reports/microbiome_extracted_claims.json \
  --output reports/microbiome_neuroinflammation_report.json \
  --markdown reports/microbiome_neuroinflammation_report.md
```

### Example: run a real corpus

```bash
./corpora/butyrate_neuroinflammation/run_corpus.sh
./corpora/butyrate_neuroinflammation/run_reviewed_corpus.sh
./corpora/butyrate_neuroinflammation/run_gold_corpus.sh
```

## Current limitations

This is still an early-stage research tool.

Important caveats:
- current corpora often use abstract-level or summary-level text, not full-paper adjudication
- evidence weighting is heuristic, not formal meta-analysis
- extraction quality still depends on review and curation
- domain choice matters a lot
- outcome and mechanism schemas still need deeper ontology work for many domains

## Roadmap

Near-term:
- stronger reviewed-corpus workflows
- tighter extraction discipline
- better intervention / outcome ontologies
- more contradiction-rich domains
- improved source-level claim preference logic

Long-term:
- compile literature into rival, testable world-models rather than disconnected notes
- move beyond summaries into explicit scientific reasoning support

Not:
- another paper chatbot
- another citation wrapper
- another generic RAG demo

But:
- a tool for computing over scientific disagreement

## Contributing

This project is still in a fast-moving experimental stage.
If you want to contribute, open an issue with:
- domain ideas
- ontology suggestions
- extraction / review workflow problems
- corpus-quality improvements

## Context

Built as an experimental project exploring AI as a scientific reasoning tool.

If you're interested in literature synthesis, contradiction mining, or AI-assisted hypothesis generation, feel free to open an issue or fork the repo.
