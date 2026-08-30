# Literature Mapping Protocol

## Goal
Understand what the field is doing before trying to find a gap, while preserving the boundary between what was actually read and what is merely plausible.

## Default Window
Recent 2–3 years for the active map, plus older anchors when needed.

## Evidence Access First

Before extracting substantive paper content, record one access level:
- `FULL_TEXT`
- `ABSTRACT_ONLY`
- `METADATA_ONLY`
- `SECONDARY_SOURCE`

Do not fill fields beyond what the current access level explicitly supports.

### Metadata only
May support identity-level facts only.

### Abstract only
May support only claims explicitly stated in the abstract: stated problem, high-level method description, and abstract-level reported result.
Do not infer dataset names, detailed metrics, baselines, ablations, implementation details, failure cases, limitations, or future work unless explicitly present in the abstract.

### Secondary source
Use for discovery and navigation. Do not silently convert a citing paper/review/search snippet into a primary-paper fact.

### Full text
May support detailed extraction, but only for content actually found in the inspected text.

## Extract per material paper

When the source level supports it, extract:
- exact identity/version;
- venue/year and role;
- research problem;
- method;
- datasets;
- metrics;
- baselines;
- claim-bearing experiments;
- limitations/failure cases;
- closest named predecessors;
- future-work claims as hypotheses only.

For every field that is not supported by the available source, write `NOT_VERIFIED_FROM_AVAILABLE_SOURCE` or `UNRESOLVED`.
Never replace "not visible in current material" with "the paper did not do it."

## Claim-Bearing Experiment
Identify the experiment(s) without which the paper's main empirical claim materially weakens.
This field requires `FULL_TEXT` unless the abstract itself explicitly supplies enough information, and abstract-level evidence must still be labeled as such.

## Load-Bearing Full-Text Gate

Full text is mandatory before a paper carries a decisive judgment as:
- deep-read Anchor Paper;
- Closest Prior Work;
- strongest Kill Search competitor;
- decisive gap-open/gap-closed evidence;
- decisive novelty evidence;
- evidence that changes topic verdict.

If full text is missing:
1. do not infer;
2. create a `SOURCE REQUEST`;
3. mark the dependent task `BLOCKED_BY_SOURCE`;
4. tell the user exactly which PDF/manuscript is needed and which questions must be verified.

Update `PAPER_INDEX.md`, paper notes, `SOURCE_MANIFEST.md`, `FIELD_MAP.md`, and `OPEN_QUESTIONS.md`.
