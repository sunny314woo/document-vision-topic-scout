# Web Chat Context, Natural Migration, and Verified Handoff

## Context Risk

### LOW
Stable field/focus, stable venue band, understandable active paper/candidate set, no major state conflict, next work can be done from current files.

### MEDIUM
Paper/candidate set expanded materially; several gaps active; kill searches repeatedly change wording; major phase boundary near; distant chat memory is becoming important.

### HIGH
Active Q identity ambiguous; rejected/live candidates mix; closest prior changes repeatedly without clean state; venue/gap versions conflict; superseded reasoning dominates; next task depends mainly on memory.

## Natural Migration Points
- MP1 — Field + Venue Map complete
- MP2 — Anchor set selected and roles stable
- MP3 — Problem Map complete and formal Qs begin
- MP4 — Kill Search complete for leaders
- MP5 — Top-3 package complete or topic frozen

Natural point is an assessment, not a forced migration.

Decision:
- LOW + same task type: continue.
- MEDIUM: finish coherent unit, update state, consider continuation.
- HIGH: package + verify, then recommend continuation.
- Major task-type shift may justify migration at MEDIUM.

## Soft Turn / Length Control
Do not invent token counts.
Reassess after ~15–20 substantive research exchanges, several literature batches, sharp growth in active papers/candidates, or repeated candidate rewrites.
These trigger review, not automatic migration.

## Sequence and Titles
Continuation: 01, 02, 03...
Formal questions: Q01, Q02...
Title: `NN-[Qxx]CurrentScope-OCRScout`
Specialist/read-only does not consume continuation number.

## Handoff Gate
Before recommending a new Chat:
1. finish/safely stop current coherent unit;
2. update authoritative state;
3. record phase/Q/open items;
4. record previous/current/next sequence;
5. generate current/next title;
6. create START_HERE, manifest, prompt;
7. create ZIP;
8. inspect actual ZIP inventory;
9. verify required files/checksums;
10. check for accidental secrets/noise;
11. only then give downloads and new-chat instruction.

If verification fails: `HANDOFF BLOCKED`.

## Required Continuation State
START_HERE.md
HANDOFF_MANIFEST.md
HANDOFF_PROMPT.md
CHECKSUMS.sha256
PROJECT_STATE.md
FIELD_MAP.md
VENUE_MAP.md
PAPER_INDEX.md
RESEARCH_QUESTION_INDEX.md
CANDIDATE_GAPS.md
KILL_SEARCH_LEDGER.md
OPEN_QUESTIONS.md
SOURCE_MANIFEST.md
DECISION_LOG.md

## Receiving Acceptance
Verify handoff IDs, sequence continuity, expected title, actual inventory, state files, current phase/Q, and first task.

Success: `CONTINUATION ACCEPTED`
Failure: `HANDOFF BLOCKED`

## Specialist / Read-Only
Use for one bounded competitor search, venue-policy check, or narrow paper audit.
It does not become project owner and returns only a bounded report.
