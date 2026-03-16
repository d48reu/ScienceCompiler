# Contributing

Science Compiler is still an experimental research workflow, so the most useful contributions right now are:
- better corpora
- cleaner ontologies
- tighter extraction / refinement behavior
- sharper review workflows
- better contradiction and tradeoff grouping

## Best way to contribute

Open an issue with one of these:
- domain proposal
- corpus improvement
- extraction/refinement bug
- ontology/canonicalization problem
- evidence-weighting concern
- report/review workflow suggestion

## Preferred contribution style

- keep changes small and legible
- add or update tests when behavior changes
- prefer explicit structure over magic
- do not silently change corpus claims without documenting why

## For corpus edits

If a scientific judgment changes the corpus meaningfully:
- prefer review overrides or documented corpus edits
- do not bury important changes inside unrelated commits

## For ontology changes

If you merge or split labels, include examples of:
- before
- after
- why the change is scientifically more faithful
