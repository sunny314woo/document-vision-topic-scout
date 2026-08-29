---
name: document-vision-topic-scout
description: >
  Web-Chat-first research-topic discovery skill for beginners entering Document Vision / OCR.
  Builds a field and venue map, selects anchor papers, identifies candidate problems,
  runs anti-fake-gap and closest-prior-work kill searches, evaluates low-resource feasibility,
  ranks at most three research questions, supports human topic freeze, and maintains verified
  multi-conversation handoff with sequence-aware mobile chat titles.
---

# Document Vision Topic Scout v0.1.0

## Purpose

Guide a researcher with little or no prior research experience in Document Vision / OCR from
"我不知道该研究什么" to a defensible, evidence-bounded, feasible research question.

The first real validation target is:

- Field: Document Vision / OCR
- Focus seed: OCR robustness
- Target venue: IJDAR or a comparable CCF-C venue
- Default venue expansion: target tier + 1
- Conditional expansion: target tier + 2 only for frontier calibration or novelty kill-check
- Equipment: none
- Compute: CPU / consumer GPU preferred
- Data: public datasets preferred
- Publication-cost preference: avoid mandatory APC / conference-registration cost where possible

This skill is not a paper-writing skill and does not guarantee novelty, acceptance, or publication.

## Core Principles

1. **Beginner-first.** Do not assume the user already knows the field, papers, benchmarks, metrics, or research question.
2. **Field before gap.** Build a field and venue map before claiming a research gap.
3. **Evidence before enthusiasm.** A plausible idea is not a verified gap.
4. **Gap is a hypothesis until re-searched.** Old "future work" statements are not current novelty evidence.
5. **Closest prior work is mandatory.** A serious candidate cannot pass without identifying the nearest competitor(s).
6. **Absence of search results is not proof of novelty.**
7. **Feasibility is a hard gate.** A novel topic can still be rejected when data, compute, equipment, cost, or validation are unrealistic.
8. **At most three finalists.** Eliminate weak ideas; do not generate long inspirational lists.
9. **Conversation is disposable; project state is authoritative.**
10. **Web Chat is the primary runtime.** Persist state, monitor context risk, and prepare verified handoff bundles before recommending a new conversation.
11. **Natural stage boundaries trigger migration assessment.** They do not automatically force a new Chat.
12. **Sequence continuity is linear.** Continuation conversations increment the two-digit sequence exactly once; specialist/read-only conversations do not consume it.
13. **The Skill suggests a title; it never claims to rename the Chat UI.**
14. **Human topic freeze is mandatory.** The Skill may recommend a question but cannot mark it `FROZEN` until the user explicitly approves it.
15. **Transfer evidence and provenance, not authority.** A research handoff transfers a defended opportunity, not a guarantee of novelty or publishability.

## Evidence Vocabulary

Use:
- `SOURCE` — explicitly supported by an inspected primary/authoritative source.
- `SYNTHESIS` — derived from comparing multiple inspected sources.
- `HYPOTHESIS` — candidate interpretation, gap, or research route requiring further testing.
- `UNRESOLVED` — insufficient evidence, inaccessible source, or unresolved ambiguity.

Gap status:
- `OPEN`
- `PARTIALLY_ADDRESSED`
- `LIKELY_CLOSED`
- `UNCERTAIN`

Topic verdict:
- `RECOMMEND`
- `HOLD`
- `REJECT`

Never write absolute novelty claims merely because a search returned no direct hit.

## Stable Identities

Maintain:
- Project short name, default `OCRScout`
- Conversation sequence: `01`, `02`, ...
- Formal candidate-question sequence: `Q01`, `Q02`, ...
- Stable `paper_id` for every paper used materially

Paper roles:
- `ANCHOR`
- `TARGET_VENUE`
- `UPPER_TIER`
- `FRONTIER_CALIBRATION`
- `CLOSEST_PRIOR`
- `KILL_SEARCH`
- `BACKGROUND`

## Venue Band Rule

Default:
`Target Tier -> Target Tier + 1`

Conditional:
`Target Tier + 2`

The +2 layer is for frontier calibration, source tracing, and novelty kill-check.
Do not let top-tier compute-heavy work automatically enter the personal candidate pool.

## Workflow

### Phase 0 — Beginner Orientation
Read `references/01_beginner_orientation.md`.
Output a Field Primer and initialize `FIELD_MAP.md`.

### Phase 1 — Field and Venue Mapping
Read `references/02_scope_and_taxonomy.md` and `references/03_venue_band_policy.md`.
Output `FIELD_MAP.md` and `VENUE_MAP.md`.

### Phase 2 — Anchor Paper Selection
Read `references/04_literature_mapping_protocol.md` and `references/05_anchor_paper_selection.md`.
Select a minimal learning set, normally 8–12 papers with explicit roles.

### Phase 3 — Targeted Reading and Problem Map
For each material paper extract research problem, method family, datasets, metrics, baselines, claim-bearing experiments, limitations/failure cases, closest predecessors, and unresolved points.

### Phase 4 — Candidate Gap Formation
Convert repeated limitations, contradictions, failure modes, benchmark weaknesses, or unresolved comparisons into `HYPOTHESIS`-level candidate gaps.

### Phase 5 — Kill Search
Read `references/06_gap_and_kill_search_protocol.md`.
Search target tier and +1; trigger +2 only under the venue policy; identify closest prior work and strongest invalidating competitor.

### Phase 6 — Personal Feasibility
Read `references/07_feasibility_gate.md` and load `profiles/low_resource_independent.yaml`.

### Phase 7 — Topic Decision
Read `references/08_topic_ranking_and_freeze.md`.
Return at most three candidate cards.

### Phase 8 — Human Topic Freeze
Only explicit user approval can set `TOPIC_STATUS: FROZEN`.

### Phase 9 — Research Handoff
Read `references/09_research_handoff_contract.md`.
Transfer the frozen question and evidence package to a later research skill.

## Natural Migration Points

At each natural checkpoint, perform a context-risk assessment:

1. **MP1** — Field + Venue Map completed.
2. **MP2** — Anchor Paper set selected and roles stabilized.
3. **MP3** — Problem Map completed and formal candidate questions begin.
4. **MP4** — Kill Search completed for the leading candidates.
5. **MP5** — Top-3 decision package completed or one topic is frozen.

A natural migration point is an assessment point, not an automatic switch.
Continue in the same Chat when state is stable and risk is LOW.
Prefer a verified continuation when risk is MEDIUM/HIGH or the next phase changes task type materially.

## Context Length / Turn Control

Do not invent token counts.
Use a soft cadence check after a substantial batch of work, such as ~15–20 substantive research exchanges, several literature batches, or a sharp increase in active papers/candidates; and a semantic migration gate based on contamination, superseded states, phase change, and dependence on distant chat memory.
Message count is never the sole trigger.

## Web Chat Naming

Use:
`NN-[Qxx]CurrentScope-OCRScout`

Examples:
- `01-领域地图-OCRScout`
- `02-Anchor筛选-OCRScout`
- `03-Q03退化鲁棒-OCRScout`
- `04-Q03查重新颖性-OCRScout`
- `05-Q03选题冻结-OCRScout`

`Qxx` appears only after a formal candidate exists.
The Skill suggests the title; the user renames the Chat manually if desired.

## Authoritative Runtime State

Maintain `PROJECT_STATE.md`, `FIELD_MAP.md`, `VENUE_MAP.md`, `PAPER_INDEX.md`, `RESEARCH_QUESTION_INDEX.md`, `CANDIDATE_GAPS.md`, `KILL_SEARCH_LEDGER.md`, `OPEN_QUESTIONS.md`, `SOURCE_MANIFEST.md`, and `DECISION_LOG.md`.
Conversation history is lower authority than these files.

## Web Chat Handoff

Read `references/10_web_chat_context_handoff.md`.
Never recommend a new conversation until a real handoff bundle exists and has passed inventory verification.
When code execution is available, use `scripts/package_chat_handoff.py`.
Receiving conversation must verify sequence and actual inventory before reporting `CONTINUATION ACCEPTED`.
If critical state is missing: `HANDOFF BLOCKED`.

## Researcher-Facing Style

Speak as a research mentor, not a workflow operator.
Lead with what the field/literature suggests, why it matters, what remains uncertain, and the next smallest useful action.
