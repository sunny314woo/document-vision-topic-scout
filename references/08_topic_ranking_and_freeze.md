# Topic Ranking and Freeze

## Mandatory Gate Before Ranking

Before ranking a candidate, verify:
- evidence coverage is adequate;
- gap is not already likely closed;
- Closest Prior is identified;
- load-bearing Closest Prior / Kill Search sources have `FULL_TEXT`;
- public data path is credible;
- compute/equipment are acceptable;
- venue fit is credible;
- reproducibility/validation path exists.

If decisive literature is not available in full text, mark:
- source state: `BLOCKED_BY_SOURCE`;
- gap/novelty: `UNRESOLVED` or `UNCERTAIN`;
- verdict: `HOLD`.

Do not upgrade a source-blocked candidate to `RECOMMEND`.

## Candidate Card
Include:
- Research Question
- Why it matters
- Current state
- Closest prior work
- Closest-prior access level / source state
- Already solved
- Appears unresolved
- Gap status
- Novelty confidence
- Search envelope
- Source blockers
- Public datasets
- Baselines
- Metrics
- Expected compute/equipment
- Research/engineering complexity
- Target venue fit
- +1 potential
- Fatal risk
- What would kill the topic
- Next reading
- First decisive test
- Verdict

Any field not verified from the available source must remain explicitly unknown; never translate "not visible" into "absent."

Return at most three candidates.
Use RECOMMEND / HOLD / REJECT.
Only explicit user approval can set `TOPIC_STATUS: FROZEN`.
