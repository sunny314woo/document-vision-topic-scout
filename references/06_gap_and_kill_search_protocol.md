# Gap and Kill Search Protocol

## Governing Rule
A research gap is a hypothesis until freshly checked.

No missing source may be completed from model memory, domain convention, title wording, an abstract omission, or a secondary description.

## Candidate Gap Sources
- repeated limitations;
- contradictions;
- failure cases;
- benchmark blind spots;
- untested generalization;
- reliability/calibration weaknesses;
- data/method mismatch;
- cost/latency bottlenecks;
- real-vs-synthetic degradation mismatch.

A limitation/failure case is paper-derived evidence only if the inspected source level actually supports it.

## Anti-Fake-Gap Procedure
For every serious candidate:
1. state the gap precisely;
2. list synonyms/adjacent terminology;
3. search target +1;
4. trigger +2 only when policy permits;
5. inspect relevant conferences/preprints when necessary;
6. identify closest prior work;
7. identify strongest invalidating competitor;
8. record each decisive source's access level and source state;
9. obtain `FULL_TEXT` for Closest Prior and any competitor that may decisively open/close the gap;
10. record search date, envelope, and limitations;
11. classify OPEN / PARTIALLY_ADDRESSED / LIKELY_CLOSED / UNCERTAIN.

## Full-Text Blocking Rule

If Closest Prior or a decisive Kill Search competitor is only `ABSTRACT_ONLY`, `METADATA_ONLY`, or `SECONDARY_SOURCE`:
- do not infer its datasets, baselines, experiments, limitations, or scope;
- do not use an abstract omission as evidence that the paper lacks a feature;
- issue a structured `SOURCE REQUEST`;
- set the affected novelty/gap judgment to `UNRESOLVED` or `UNCERTAIN`;
- set the dependent candidate to `HOLD / BLOCKED_BY_SOURCE` when otherwise viable.

A candidate cannot enter Top 3 as `RECOMMEND` while decisive full-text evidence remains blocked.

## Source Request Content

Record:
- paper ID and exact identity;
- locator (DOI/arXiv/publisher/author page when available);
- current access level;
- why full text is load-bearing;
- exact questions to verify;
- acceptable source forms;
- source state: `SOURCE_REQUESTED`, `BLOCKED_BY_SOURCE`, or `SOURCE_UNAVAILABLE`.

If the full text never becomes available, preserve that uncertainty instead of silently resolving it.
