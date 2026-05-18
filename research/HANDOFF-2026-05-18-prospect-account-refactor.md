# Session Handoff — 2026-05-18 / batch-mode plan revision

> **TEMPORARY FILE.** Delete after `/prospect-batch` is built and validated.

## TL;DR

The 2026-05-18 batch refactor was tested on 1 row of cohort-2 (TruckLogics) and **rolled back**. The Deepline `deeplineagent`-based batch produced materially worse email drafts than single-account `/prospect-account` because it bypasses the `email-writer` skill chain (voice profile + reference files + cold-email-craft) and uses a smaller model. `/prospect-account` is now restored to its original 2026-03-06 state. New direction: build batch as a separate skill (`/prospect-batch`) using subagent fan-out — Claude Code spawns N subagents in parallel, each runs `/prospect-account` on one row. Quality matches single-account by definition.

## What ran today

1. **Refactored `/prospect-account`** into dual-mode (single-account + batch via `deepline enrich --with` chain calling `deeplineagent` per step). Modernized provider calls to Deepline waterfalls.

2. **Dry-run validated** — all 10 `--with` blocks compiled clean.

3. **Smoke test on 1 row** (TruckLogics, cohort-2 row 1):
   - Chain executed end-to-end, $0.18/row cost
   - ICP 4-gate correctly DQ'd TruckLogics on NEW + VPP gates (matches existing memory)
   - **But the email draft was bad** — parroted product copy ("You say TruckLogics can connect..."), generic "what I do" line, wrote a full email despite ICP fail, no actual signal cited
   - Cold-email-craft scan over-flagged false positives on `dual_cta` and `machinery_before_curiosity`

4. **Root cause:** `deeplineagent` is a single AI call with a prompt string. It cannot:
   - Invoke the `email-writer` skill (skills are not callable from inside `deepline enrich`)
   - Load voice profile, reference files, or memory dynamically
   - Run Claude Opus
   
   So the batch was a *thin substitute* for the skill chain, not the actual skill chain.

5. **Reverted all changes to `/prospect-account`** to preserve the known-good single-account quality. Files now match their 2026-03-06 state exactly.

## Current file state (verified)

**Restored to pre-session original:**
- `~/.agents/skills/prospect-account/SKILL.md`
- `~/.agents/skills/prospect-account/diagnostic-chain.md`
- `~/.agents/skills/prospect-account/signal-collectors.md`

**Deleted:**
- `~/.agents/skills/prospect-account/feedback-loop.md` (was new, no longer needed)

**Kept (useful regardless of batch architecture):**
- `~/.claude/skills/_shared/icp-4-gate.md` — codifies the 4-gate ICP rubric from `feedback_thresh_segment_gates.md`. Future `/prospect-batch` skill can reference this. So can any future ICP-related work.

**Snapshot of the refactored state** (in case any of it is salvageable later):
- `~/.claude/skill-backups/prospect-account-2026-05-18/`

## New direction: `/prospect-batch` via subagent fan-out

Instead of `deepline enrich` with `deeplineagent` calls (the broken approach), the batch skill spawns Claude Code subagents in parallel. Each subagent runs `/prospect-account` on one row of the CSV with the full skill chain loaded. Output gets collected back into a result CSV.

**Architecture:**

```
CSV (50 rows)
   ↓
/prospect-batch orchestrator reads CSV
   ↓
Spawns N subagents in parallel via Agent tool
   ├─ Subagent 1: /prospect-account row 1 → full skill quality
   ├─ Subagent 2: /prospect-account row 2 → full skill quality
   └─ ...
   ↓
Orchestrator collects per-row output → result CSV
```

**Why this works:**

- Each subagent IS Claude Code with full filesystem access. Loads voice profile, references, cold-email-craft, memory files — all dynamically.
- Each subagent runs Claude Opus quality.
- Deepline still gets used inside each subagent for what it's actually good at: data fetching (`deepline_native_enrich_company`, `crustdata_job_listings`, `exa_search`, etc.)
- Quality matches single-account by definition — it literally IS single-account, running N times in parallel.

**Cost per row:**
- ~$0.10 in Deepline credits (data fetching only)
- Claude Code tokens from existing subscription (no incremental API cost)
- Total: cheaper than the failed Deepline batch ($0.18/row) AND cheaper than the original handoff estimate ($0.40/row)

## Next session: pick up here

### Step 0 — Read these first
- `~/.agents/skills/prospect-account/SKILL.md` (the known-good single-account flow)
- `~/.claude/skills/_shared/icp-4-gate.md` (4-gate rubric — used by both single-account ICP check and the new batch)
- `~/.claude/plans/i-have-questions-bout-federated-panda.md` (original plan — contains useful framing on feedback loop, signal recency, etc. that should make its way into `/prospect-batch`)
- `feedback_thresh_segment_gates.md` (source for 4-gate)
- `feedback_outbound_*.md` files (the failure-mode memory that informs cold-email-craft)

### Step 1 — Draft a new plan for `/prospect-batch`

The plan should cover:

1. **Orchestrator skill design**
   - Trigger phrases: `/prospect-batch <csv>`, "batch prospect this list", "run prospect-account on these accounts"
   - CSV requirements: must have `domain` column (or `company_domain`)
   - Optional `--limit N` flag (note: `deepline enrich --rows 0:N` is inclusive-stop — `0:9` = 10 rows)
   - Parallel concurrency: probably 5-10 subagents at a time to avoid rate limits

2. **Subagent invocation pattern**
   - Use Agent tool with subagent_type=`general-purpose` (or `claude` if available)
   - Each subagent receives: domain + company_name + any pass-through columns
   - Subagent prompt: "Run /prospect-account on `<domain>` for the research phase (Steps 1-5). Skip Steps 6-9 (no contacts/CRM/Gmail). Output the data cocktail, tension reading, draft email, and any flags as structured JSON."
   - Subagent works in its own context window — full skill access

3. **Output collection**
   - Orchestrator polls subagent results
   - Writes each result back to the corresponding CSV row
   - Columns added: `data_cocktail`, `tension`, `draft_email`, `craft_flags`, `signals_summary`

4. **ICP gating (use `_shared/icp-4-gate.md`)**
   - Subagent checks the 4-gate after Step 1 LIST
   - If fail → returns DQ stub instead of full output
   - Orchestrator writes DQ reason to output CSV

5. **Quality gates per row**
   - cold-email-craft scan runs inside each subagent (since cold-email-craft is a skill, subagent can invoke it naturally)
   - Output includes craft_flags column

6. **Feedback loop**
   - Lives inside `/prospect-batch` SKILL.md, not modifying `/prospect-account`
   - When user edits batch output, classify (tone/format/research/signal), route to:
     - voice-profiles/lucas.md
     - email-writer/SKILL.md or references
     - cold-email-craft/SKILL.md
     - feedback_outbound_*.md memory
   - Same routing logic as the rolled-back feedback-loop.md — but scoped to batch output only

7. **`--limit N` for first-N iteration**
   - Match the Clay-style validation habit: run 10, review, iterate, run remaining

### Step 2 — Build the skill, test on cohort-2 row 1 (TruckLogics)

Same smoke test pattern: 1 row first, then 10, then 50. With subagent fan-out, the 1-row test is essentially "does the orchestrator successfully spawn a subagent and collect its output." Quality is guaranteed because the subagent IS `/prospect-account`.

## Key memory from the smoke test

- **TruckLogics fails the 4-gate on NEW + VPP.** Matches existing campaign memory (low-cost probe sent 2026-05-18). The 4-gate rubric is well-calibrated.
- **`deepline enrich --rows 0:N` is inclusive-stop.** `0:1` = 2 rows, `0:9` = 10 rows. Documented per real CLI behavior, not Python slicing.
- **`--dry-run` exists and is free.** Always pilot with `--dry-run --rows 0:1` before real execution.
- **`deepline session limit --dollars N` exists.** Use as a hard ceiling on real runs.
- **`--config <jsonc>` reuses saved enrich configs.** The dry-run saved one at `/Users/lucas/Documents/projects/thresh/deepline/enrichments/accounts-qualified-50-20260518-185353.jsonc` — could be cleaned up or reused as a reference for the data-fetching-only steps of `/prospect-batch`.

## Commit/save guidance for the new session

After `/prospect-batch` skill is drafted + tested:
- Skill files live at `~/.agents/skills/prospect-batch/` (or wherever new skills go locally) — no version control there
- Take a backup snapshot once the skill works: `cp -r ~/.agents/skills/prospect-batch ~/.claude/skill-backups/prospect-batch-<date>`
- Any new shared sub-docs go in `~/.claude/skills/_shared/` (git-tracked)
- Commit handoff updates + any new shared docs to `~/Documents/projects/thresh/` if useful
