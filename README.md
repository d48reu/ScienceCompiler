# Science Compiler

Science Compiler is an AI-assisted research workflow for turning scientific literature into structured, computable objects instead of vague summaries.

Instead of stopping at "the literature is mixed," it tries to produce:
- structured claims
- contradiction maps
- weighted evidence balances
- mechanism groupings
- follow-up experiment ideas
- human review queues

In short:

`papers -> claims -> contradictions / tradeoffs -> better scientific questions`

## Why this exists

Most "AI for science" tools do one of two things:
1. summarize papers into prose
2. predict on datasets

Science Compiler targets a different bottleneck: making disagreements inside the literature legible and computable.

The goal is not to replace researchers.
The goal is to help them see:
- where evidence really agrees
- where it breaks
- which contexts flip the apparent effect
- what should be tested next

## Current project status

This repo is the public home for the project.

The current working prototype includes:
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

### 2. Senolytics / aging
In a second domain, the structure changed.

Instead of one main contradiction, the system surfaced a benefit-vs-harm tradeoff map:
- some senolytics improve lifespan, function, or resilience
- some agents or contexts show null effects, tissue-specific harm, or sex-specific downside

That matters because it shows the workflow is not locked to one scientific pattern.

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

## Current limitations

This is still an early-stage research tool.

Important caveats:
- current corpora often use abstract-level or summary-level text, not full-paper adjudication
- evidence weighting is heuristic, not formal meta-analysis
- extraction quality still depends on review and curation
- domain choice matters a lot

## Direction

The long-term vision is a system that helps compile scientific literature into rival, testable world-models instead of disconnected notes.

Not:
- another paper chatbot
- another citation wrapper
- another generic RAG demo

But:
- a tool for computing over scientific disagreement

## Contact / context

Built as an experimental project exploring AI as a scientific reasoning tool.

If you're interested in literature synthesis, contradiction mining, or AI-assisted hypothesis generation, feel free to reach out or open an issue once the repo is fully populated.
