# Document Vision Topic Scout

A Web-Chat-first research-topic discovery Skill for beginners entering Document Vision / OCR.

## v0.1.0 focus

- beginner orientation before gap mining;
- target venue + one tier by default;
- conditional +2 only for frontier calibration / novelty kill-search;
- anchor-paper selection;
- anti-fake-gap and closest-prior-work checks;
- low-resource personal feasibility gates;
- at most Top 3 candidate questions;
- explicit human topic freeze;
- ChatGPT Web continuation numbering, mobile title suggestions, natural migration points, verified ZIP handoff, and receiving-side acceptance.

## Primary flow

`zero background -> field map -> venue map -> anchors -> problem map -> gap hypotheses -> kill search -> feasibility -> top 3 -> human freeze -> research handoff`

## Natural migration checkpoints

- MP1: Field + Venue Map complete
- MP2: Anchor set stabilized
- MP3: Problem map complete / candidate questions begin
- MP4: Kill Search complete
- MP5: Top-3 package or topic freeze complete

A checkpoint triggers migration assessment, not mandatory migration.

## Chat title

`NN-[Qxx]CurrentScope-OCRScout`

The Skill suggests the title; the UI rename remains manual.

## Design sources

Selectively adapted from:
- `sunny314woo/pde-read-paper`: evidence boundaries, stable paper identity, bounded verification, controlled reference excursions, state-first handoff;
- `sunny314woo/pde-research-paper`: Web Chat continuation sequence, mobile title protocol, verified handoff, linear ownership, receiving-side acceptance;
- `avocadotech2018/research-topic-scout`: anti-fake-gap, closest-prior-work, feasibility;
- `ginaecho/topic-scout`: living corpus / research-opportunity tracking.

v0.1.0 intentionally excludes dashboards, databases, large multi-agent orchestration, and full-paper writing.
