# Session Handoff — 2026-05-18 / prospect-account batch refactor

> **TEMPORARY FILE.** Delete after the next session kicks off and runs the dry-run + smoke test successfully.

## Where we left off

`/prospect-account` skill has been refactored to support **batch mode** for CSV inputs. The implementation is done but **not yet executed**. The next session's first move is a `--dry-run` validation of the chain (free), then a `--rows 0:1` smoke test on cohort-2 row 1 (TruckLogics) with a $1 session limit.

## What was built this session

### Files modified (live on disk, no version control)
- `~/.agents/skills/prospect-account/SKILL.md` — dual-mode (single-account interactive vs batch CSV). Pipeline-overview table shows what runs in each mode. Added `--limit N` flag, `prospect_context` forward-compat hook, auto `cold-email-craft` scan in Step 5. Replaced direct `crustdata_companydb_search` / `apollo_enrich_company` with `deepline_native_enrich_company`. Replaced the apollo obfuscation dance with `company_to_contact_by_role_waterfall`. Replaced manual email patterns with `name_and_domain_to_email_waterfall`.
- `~/.agents/skills/prospect-account/diagnostic-chain.md` — Step 1 points at `deepline_native_enrich_company`. Step 4 ICP check references the shared 4-gate.
- `~/.agents/skills/prospect-account/signal-collectors.md` — full rewrite. Collector 1 = `deepline_native_enrich_company`. Collector 4 = Exa→Firecrawl chain. Dropped conflicting credit numbers. Added Deepline-CLI hygiene rule, signal-recency rule, signal-weighting rule.
- `~/.agents/skills/prospect-account/feedback-loop.md` — NEW. Edit classifier (tone/format/research/signal) + routing decision tree. Extends `email-paste-back` pattern.

### Files created (in `~/.claude` git repo, untracked)
- `~/.claude/skills/_shared/icp-4-gate.md` — Thresh 4-gate ICP rubric (NEW × EXISTENTIAL × IDENTIFIABLE × VPP-tier-≥-Risk-Mitigation). Shared sub-doc.
- `~/.claude/plans/i-have-questions-bout-federated-panda.md` — approved plan, reference for what was scoped.

## Critical context for the new session

### Validations done
- All 14 file paths referenced by skill / sub-docs resolve on disk
- Cohort-2 CSV exists with `domain` + `company_name` columns + 50 rows
- Deepline CLI flags confirmed via `deepline --help` and `deepline enrich --help`:
  - `--dry-run` — compiles + validates without execution ($0)
  - `--rows START:END` — slices rows (e.g. `0:1` = first row, `0:10` = first 10)
  - `--with-force ALIASES` — recompute selected aliases on rerun
  - `--in-place` — write to input CSV instead of new output
  - `deepline session limit --dollars N` — hard $ ceiling per session
  - `deepline billing balance` — check current credits
  - `deepline tools get <tool_id> --json` — inspect any tool's input/output schema

### NOT validated
- The `deepline enrich` chain in the dry-run command below has **never been executed** — every `extract_js`, `jsonSchema`, and `deeplineagent` prompt is structured per docs but untested
- The `gate_check` short-circuit step (skip Steps 2-5 when ICP fails) is NOT in the dry-run command — production batch should add it
- Local careers-page scraping is NOT in the dry-run — uses `crustdata_job_listings` only (skill's spec acknowledges both options)
- Exa→Firecrawl fanout is NOT in the dry-run — uses Exa with `contents.text.maxCharacters: 3000` inline

## Next session: pick up here

### Step 0 — Read these first
- `~/.agents/skills/prospect-account/SKILL.md` (especially "Batch Mode" section)
- `~/.claude/skills/_shared/icp-4-gate.md`
- `~/.agents/skills/prospect-account/feedback-loop.md`
- `~/.claude/plans/i-have-questions-bout-federated-panda.md` (approved scope)

### Step 1 — Run the dry-run (FREE)

Paste this command verbatim. Validates the entire chain without spending a cent:

```bash
INPUT=/Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13/cohort-2/accounts-qualified-50.csv
OUTPUT=/Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13/cohort-2/accounts-qualified-50.research.csv

deepline enrich --input "$INPUT" --output "$OUTPUT" --rows 0:1 --dry-run \
  --with '{"alias":"company","tool":"deepline_native_enrich_company","payload":{"domain":"{{domain}}"}}' \
  --with '{"alias":"company_flat","tool":"run_javascript","payload":{"code":"const c=row.company?.result?.output?.company||{};return {name:c.name,headcount:c.estimated_num_employees,industry:c.industry,funding:c.total_funding,stage:c.latest_funding_stage,hq:c.city,linkedin:c.linkedin_url,description:c.description,tech_stack:c.technology_names};"}}' \
  --with '{"alias":"icp_gate","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Apply Thresh 4-gate ICP test to {{company_name}} ({{domain}}). Firmographic context: {{company_flat}}.\n\nAll 4 gates must pass:\n1. NEW: pain emerged recently enough buyer has no workarounds (regulatory shift <18mo, funding-driven behavior change, forced migration off prior tool)\n2. EXISTENTIAL: mission-critical, not budget annoyance (breaks revenue/compliance/trust, has executive owner with quota or P&L)\n3. IDENTIFIABLE: detectable from outside via Layer-A public data (FMCSA, EPA, FDA, public hiring/funding/leadership)\n4. VPP tier: Thresh reads as Risk Mitigation, Growth, or Customer Satisfaction (NOT Efficiency tier — no save-time framing)\n\nReturn JSON. failing_gates is empty array if all pass. reason is 1-line per failing gate joined with | (or empty if all pass).","jsonSchema":{"type":"object","properties":{"pass":{"type":"boolean"},"failing_gates":{"type":"array","items":{"type":"string","enum":["NEW","EXISTENTIAL","IDENTIFIABLE","VPP"]}},"reason":{"type":"string"}},"required":["pass","failing_gates","reason"],"additionalProperties":false}}}' \
  --with '{"alias":"jobs","tool":"crustdata_job_listings","payload":{"companyDomains":["{{domain}}"]}}' \
  --with '{"alias":"website","tool":"exa_search","payload":{"query":"{{company_name}} site:{{domain}}","numResults":6,"contents":{"text":{"maxCharacters":3000}},"type":"auto"}}' \
  --with '{"alias":"signals","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Analyze signals for {{company_name}} ({{domain}}). Firmographics: {{company_flat}}. Jobs: {{jobs}}. Website: {{website}}.\n\nExtract: hiring_pattern (GTM roles + what stage that implies), tech_signals (tools/platforms mentioned), pain_language (problems they describe), org_structure_gaps (senior role with no team, first-hires), priorities (KPIs/outcomes optimized for), website_positioning (category + diff claims), customer_segments, integrations, compliance_certs, signal_recency_assessment (any signals >15d old?).","jsonSchema":{"type":"object","properties":{"hiring_pattern":{"type":"string"},"tech_signals":{"type":"string"},"pain_language":{"type":"string"},"org_structure_gaps":{"type":"string"},"priorities":{"type":"string"},"website_positioning":{"type":"string"},"customer_segments":{"type":"string"},"integrations":{"type":"string"},"compliance_certs":{"type":"string"},"signal_recency_assessment":{"type":"string"}},"required":["hiring_pattern","tech_signals","pain_language","org_structure_gaps","priorities","website_positioning","customer_segments","integrations","compliance_certs","signal_recency_assessment"],"additionalProperties":false}}}' \
  --with '{"alias":"data_cocktail","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Build a 2-4 sentence DATA COCKTAIL narrative for {{company_name}}. Combine 2-5 signals from DIFFERENT sources into a coherent story. Format: \"They are [X] while [Y], which means [Z].\" Must be falsifiable + specific. Signals: {{signals}}.","jsonSchema":{"type":"object","properties":{"narrative":{"type":"string"},"signals_used":{"type":"array","items":{"type":"string"}}},"required":["narrative","signals_used"],"additionalProperties":false}}}' \
  --with '{"alias":"tension","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Run TENSION reading on {{company_name}}. Context: {{data_cocktail}}, {{signals}}.\n\n1. SHOULD: what infrastructure/process/capability should they have given these signals?\n2. IS: what do they actually have based on evidence?\n3. GAP: specific difference\n4. MAGNITUDE: dollars, time, competitive risk\n5. FIT: can Thresh close it (signal-based outbound on public regulatory/operational data)?\n6. PATTERN: which tension pattern fits — ambition without capacity / money without bandwidth / new vision trapped in old systems / filling a leaky bucket / scaling chaos / none\n\nApply the sentence test: \"You are [doing X] but [Y is missing] — and that is going to cost you [specific $Z].\" If you cannot complete the sentence honestly, set tension_strength to \"forced\".","jsonSchema":{"type":"object","properties":{"should":{"type":"string"},"is_":{"type":"string"},"gap":{"type":"string"},"magnitude":{"type":"string"},"fit":{"type":"string"},"pattern":{"type":"string"},"sentence_test":{"type":"string"},"tension_strength":{"type":"string","enum":["strong","moderate","forced"]}},"required":["should","is_","gap","magnitude","fit","pattern","sentence_test","tension_strength"],"additionalProperties":false}}}' \
  --with '{"alias":"draft_email","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Write a signal-based cold email for {{company_name}} ({{domain}}). Format: (1) cite the signal directly — quote/reference where it came from, (2) name the implication — what it means for them, (3) one-line \"what I do\" — Thresh helps companies selling into regulated/inspected verticals build outbound from public compliance/enforcement data, (4) low-friction single CTA.\n\nHard constraints: ~100 words MAX. 5th grade reading level. ZERO links. ZERO attachments. NO em dashes (use hyphens or periods). NO buzzwords (leverage/synergy/scalable/robust/optimize/holistic). NO \"checking in\" / \"circling back\" / \"hope this finds you\". Subject 3-5 words, lowercase. Sender voice: Lucas — direct, plain language, short paragraphs. Sign off \"Cheers, Lucas\".\n\nContext: {{tension}}, {{data_cocktail}}.\n\nIf tension_strength is \"forced\" in context, write a DRAFT NOTE instead of an email: explain why the tension is forced and suggest a different angle or DQ.","jsonSchema":{"type":"object","properties":{"subject":{"type":"string"},"body":{"type":"string"},"word_count":{"type":"integer"},"is_draft_note":{"type":"boolean"}},"required":["subject","body","word_count","is_draft_note"],"additionalProperties":false}}}' \
  --with '{"alias":"craft_flags","tool":"deeplineagent","payload":{"model":"openai/gpt-5.4-mini","prompt":"Run cold-email-craft 8-failure-mode scan on this draft. Email: {{draft_email}}.\n\nFlag any that fire:\n- ai_sdr_opener: \"saw your LinkedIn post\" / \"loved your line about\" / quoting recent public content\n- forced_analogy: \"same structure as\" / \"applied to\"\n- constructed_urgency: manufactured deadlines / asserted timelines\n- entity_without_context: naming companies/people recipient cannot decode\n- telescoping: \"sample on one company\" when work is systematic\n- machinery_before_curiosity: Layer 1/Layer 2/architecture exposition before opt-in\n- jargon: \"signal layer\" / \"demand-gen layer\" / abstractions failing 10-year-old test\n- dual_cta: artifact + meeting ask in same email\n- cold_attachment: any attachment in first touch\n\nReturn array of flag names that fired (empty if clean).","jsonSchema":{"type":"object","properties":{"flags":{"type":"array","items":{"type":"string"}},"clean":{"type":"boolean"}},"required":["flags","clean"],"additionalProperties":false}}}'
```

**What to expect from dry-run:** either "Compile OK" / similar success message, or a specific error pointing at which `--with` block failed validation. Fix iteratively before spending credits.

### Step 2 — Set $ guardrail + run real on 1 row (~$0.40)

If Step 1 dry-run passes:
```bash
deepline session limit --dollars 1
# Then remove --dry-run from the command above and re-run
```

Inspect the output CSV. Check: TruckLogics' ICP gate result (probably PASS — it's a fit lookalike), signals_summary populated, draft_email reads like a Lucas email, craft_flags either empty or surfaces real issues.

### Step 3 — If row 1 looks good, scale to 10 (~$4)

Change `--rows 0:1` → `--rows 0:10`. Review the 10 outputs. Edit any drafts that miss. Then invoke `feedback-loop.md` to route the edits → voice profile / email-writer / framework / memory.

### Step 4 — Run the remaining 40 (~$16)

After feedback-loop rules have been applied, run `--rows 10:50` for the rest of cohort-2.

## Commit / save guidance

### Nothing to commit in the `thresh` repo from this session

The session only edited skill files outside the repo. No thresh code changed.

### Files at risk if you don't save them somewhere

- **`~/.agents/skills/prospect-account/SKILL.md` + `diagnostic-chain.md` + `signal-collectors.md` + `feedback-loop.md`** — these live on local disk only, no version control. If you ever want a backup, manually copy the directory before any future edit session. Filesystem snapshot or backup-to-iCloud would do.

### Things you *could* commit to `~/.claude` repo

These are untracked there right now. Whether to commit depends on whether you version your Claude config:
- `~/.claude/plans/i-have-questions-bout-federated-panda.md` — this session's plan
- `~/.claude/skills/_shared/icp-4-gate.md` — new shared sub-doc (referenced by both /prospect-account today and a future /prospect-triage)

### This handoff file

`~/Documents/projects/thresh/research/HANDOFF-2026-05-18-prospect-account-refactor.md` is **temporary** — delete after the dry-run + smoke test runs successfully and you've internalized the next-step ladder.
