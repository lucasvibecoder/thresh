# Registry Pattern

## What this is

A **registry** is a markdown file that accumulates claims (hypotheses, prospects, queries, sends, observations) and drives decisions about them. It is not a journal. The job is **decision-readiness**, not capture.

Files in this project that should follow this pattern: `playbooks/feedback-log.md`, `outbound/sent-log.md`, `outbound/prospecting-queries.md`, `outbound/qualified-from-gtm-alpha.md`, `outbound/pipeline.md`, and any future log / tracker / experiment-record file.

The pattern exists because append-only logs without consolidation rules become unscannable, untrustworthy, and eventually unused. A registry that follows these rules stays useful at 4 entries and at 400.

## The six operating principles

**1. The unit is the claim, not the entry.**
An entry adds evidence to a claim (existing or new); claims are the rows of the active surface. Multiple entries can support one claim. One entry can support multiple claims. Don't duplicate synthesis across entries — claims are where synthesis lives.

**2. Source-independence is the promotion currency — and source quality is the multiplier.**
N entries from the same source = 1 evidence. N entries from N independent sources = N evidence. Cross-source confirmation triggers promotion; single-source repetition doesn't. One person saying something five times is one data point with high conviction; two people saying it once each is two independent data points.

But independence alone isn't enough — **source quality calibrates evidence weight**. Two ops-background reviewers may both miss the same sales-register signal in the same way; two pessimistic-friend reviewers may both over-flag the same things. When you know a source has known calibration bias (operational frame applied to a marketing question, friend trying to be a critical mirror, etc.), single-source evidence from that source should max out at `mounting-evidence` rather than driving promotion. Cross-validation from a *different-quality* source (different discipline, different relationship to the work) still carries promotion weight; same-bias sources stacking up does not.

**3. Promotion AND retirement are equally important.**
Confirmed claims **leave** the file — they graduate to a memory file, a conventions doc, a website copy change, or a CLAUDE.md rule. Disconfirmed claims **archive** with a one-line postmortem. The file should shrink as things resolve. A monotonically growing file is a failure mode, not a feature.

**4. Stale beats deleted.**
A claim with no fresh evidence in 60 days moves to a "stale, decide" section. This forces a quarterly call: revive, retire, or merge. Don't silently let claims rot — make decisions about them.

**5. Explicit triggers, not vibes.**
Each registry declares at the top: when to open it, how to add to it, when to consolidate, when to promote, where graduates go. A registry without explicit operating notes is dead infrastructure — it won't get opened at the right moments.

**6. Fidelity once, synthesis forever.**
Verbatim source content is preserved once at entry time; after that, the synthesis (the claim) is the load-bearing artifact. Don't re-preserve verbatim across multiple analytical layers — it bloats the file and creates competing sources of truth.

## Schema (recommended structure)

A registry file should have these sections, in this order:

```
# [Registry Name]

## Operating notes
- When to open this file
- How to add an entry vs. how to add evidence to an existing claim
- Promotion criteria (e.g., 2+ independent sources)
- Retirement criteria (e.g., disconfirmed by test, or stale 60+ days)
- Where claims graduate to (routing destinations)
- Pointer to docs/registry-pattern.md

## Claim ledger (active)
| ID | Claim | Sources | Status | Next action | Kill criteria |
|----|-------|---------|--------|-------------|---------------|
| C1 | [one-line claim] | [Le, Sage] | cross-validated | [what to do] | [what would disprove this] |

## Action queue
- **Ripe to test:** [claims with ≥2 independent sources, no test run yet]
- **Ripe to promote:** [claims confirmed, awaiting graduation to destination]
- **Stale:** [claims with no fresh evidence 60+ days — decide: revive / retire / merge]

## Source entries (archive)
[Verbatim feedback / observation / data, dated, lightly synthesized, tagged with claim IDs]

## Graveyard
[Promoted claims (with destination + date) and disconfirmed claims (with one-line postmortem)]
```

The claim ledger is the **active surface** — the part that should be scannable in under 60 seconds. Everything else supports it.

## Lifecycle states

A claim moves through these states:

- `untested` — proposed by a single source, no validation
- `mounting-evidence` — multiple entries from same source(s), no cross-source confirmation yet
- `cross-validated` — 2+ independent sources confirm; ripe to test or promote
- `promoted` — graduated to destination; **leaves the active ledger** (archived in graveyard with destination noted)
- `disconfirmed` — tested and falsified; archived in graveyard with postmortem
- `stale` — no fresh evidence in 60+ days; awaiting revive / retire / merge decision

A healthy registry has claims flowing through these states, not piling up at `untested`.

## Promotion routing

When a claim graduates, it goes to one of these destinations based on what kind of rule it is:

| Claim type | Destination |
|------------|-------------|
| Cold-email principles (writing rules, register rules) | Memory file: `~/.claude/projects/.../memory/feedback_outbound_*.md` |
| Playbook-template rules (artifact copy, structure, slots) | `playbooks/_CONVENTIONS.md` |
| Positioning / offer claims | `thresh.md` and/or website copy in `index.html` |
| Project-level operating rules | `CLAUDE.md` |
| Cross-conversation user/project context | Memory file (`user_*.md` / `project_*.md`) |

When promoting, **leave a stub in the graveyard** noting:
- Claim ID and one-line summary
- Destination file
- Date promoted
- Sources of evidence

This preserves traceability without bloating the active surface.

## Worked example

**Hypothesis A+I from `playbooks/feedback-log.md`:** "Playbook copy reads as convoluted / AI-generated to sophisticated recipients."

- **Entry 1 (2026-05-08, Le):** "the messaging / the plays seem a bit convoluted to read imo. A bit confusing."
- **Entry 2 (2026-05-08, Sage):** "could dumb down the jargon... folks are weary of things with too big words and will stop reading if it sound like AI."

Both entries inform claim C1 ("playbook copy reads convoluted/AI-generated"). Two independent sources (Le = Seed health-tech / marketing leader; Sage = Series D HRIS / AE) on the same week. Status: `cross-validated`.

**Promotion path:** This is a playbook-template rule, not a cold-email rule (the artifact itself reads convoluted, not just individual emails). Destination: `playbooks/_CONVENTIONS.md`.

**Graveyard stub after promotion:**
```
- C1 (cross-validated 2026-05-08): "Playbook copy reads as convoluted / AI-generated."
  Promoted to playbooks/_CONVENTIONS.md, 2026-05-08.
  Sources: Le (Le on Assured + Le on Ambrook), Sage (Sage on HiBob).
```

**`playbooks/_CONVENTIONS.md` rule (after promotion):**
```
## Playbook copy register
- Avoid jargon density and AI-detector patterns at the artifact level.
  Cross-validated by Le (Seed health-tech) and Sage (Series D HRIS), 2026-05-08.
  Recipients pattern-match against AI-generated copy and bail on jargon density.
```

## Anti-patterns

Things to avoid in any registry:

- **Verbatim everywhere.** Preserve the source quote once at entry; after that, work from the claim.
- **Status fields that don't trigger anything.** If `cross-validated` doesn't trigger a promotion check, the status is decorative.
- **Permanent untested.** A claim that sits at `untested` for >60 days is stale — decide on it, don't ignore it.
- **Implicit retirement.** Claims that become irrelevant should be moved to the graveyard with a postmortem, not silently left in the active ledger forever.
- **Capture without consolidation.** Adding entries without checking whether they extend an existing claim creates duplicate hypotheses (the failure mode that produced 11 overlapping hypotheses A-K in the first feedback-log.md draft).
- **No retrieval trigger.** A registry that isn't pointed to from somewhere always-loaded (CLAUDE.md, a skill, a workflow) won't be opened at the right moments. Define the trigger.

## When to consolidate

Consolidate the registry when:
- A new entry could extend an existing claim instead of creating a new one
- Two claims look like the same idea seen from different angles (merge them)
- A claim hits cross-source confirmation (promote it)
- A claim has been stale for 60+ days (decide)
- The active ledger no longer fits on one screen (something needs to graduate or retire)

Consolidation is not a separate ritual — it happens at entry-add time and on the way out (before closing a session that touched the registry).
