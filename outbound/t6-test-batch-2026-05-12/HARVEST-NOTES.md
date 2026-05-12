# T6 Harvest — 2026-05-12

## Headline finding

**The T6 signal (open GTM Engineer role at vertical SaaS Series A-B) is empirically weaker than the playbook redraw implied for Thresh's actual ICP.**

GTM Engineer is a horizontal SaaS / AI startup title. After 50 records pulled (50 TheirStack credits), 4 candidates pass the Information Asymmetry Test (sells into a regulated/inspected vertical with public data on buyer pain). Hit rate ~8%, not the ~25% the redraw assumed.

## Numbers

| Window | Total US postings | Sampled | Vertical-SaaS fits | Hit rate |
|--------|------------------|---------|--------------------|----------|
| Posted last 30 days | 217 | 25 | 1 (Logicbroker) | 4% |
| Posted 60-90d ago | 68 | 25 | 3 (Harper, Software Toolbox, ici) | 12% |
| **Combined** | **285** | **50** | **4** | **8%** |

Two records initially flagged tentative-fit but dropped after closer review:
- **Delve** (delve.co) — sells horizontal compliance (SOC 2, HIPAA, ISO, GDPR) to any company. No vertical, no asymmetry.
- **Altruist** (altruist.com) — TheirStack returned hc=11 and industry="Telecommunications," which conflicts with Altruist's real profile (wealth-management SaaS, Series D+, ~600 employees). Likely a subsidiary mis-tag in the data. Skipped.

## The 4 candidates

| Tier | Company | Domain | HC | Industry | Why it fits |
|------|---------|--------|----|---------- |-------------|
| STRONG | Harper | harperinsure.com | 64 | Insurance (commercial E&S brokerage) | Vertical insurance SaaS, YC W25, regulated industry, AI-native tech stack |
| GOOD | Logicbroker | logicbroker.com | 65 | Multi-vendor commerce / EDI | Sells to retail/wholesale trading partners; public data on shipments/returns possibly usable |
| GOOD | Software Toolbox | softwaretoolbox.com | 28 | Industrial AI / connectivity | Sells to manufacturing; public data on safety/inspection plausible |
| GOOD | ici | icibot.com | 21 | Hospitality (guest experience for hotels) | Vertical hospitality SaaS; public data on hotel inspections/reviews possible |

## Strategic implication

Three paths forward, ranked:

### Path A — Expand T6 ICP to include horizontal SaaS (against thresh.md but with evidence)
Most GTM Engineer roles are at horizontal SaaS. If Thresh's offer can land at horizontal SaaS too, the TAM is significantly bigger. **Tradeoff:** Information Asymmetry Test fails for horizontal — no public regulatory data about their buyers. Thresh becomes "better cold email" not "intelligence." Likely a bad path.

### Path B — Change the signal for the same Thresh ICP
Drop the T6 "open GTME role" signal. Use staffing-event signals that DO show up in regulated vertical SaaS: open VP Sales / Head of Sales (Query 1, ~647 companies/month in your data), open first SDR (Query 2, ~755 companies/month), open RevOps (Query 3, ~258 companies/month). These are S-A from the playbook redraw's Stage 2.5 stub. **Tradeoff:** longer per-account research (the staffing event doesn't directly diagnose the GTM-tooling pain), but much larger qualified pool.

### Path C — Ship to the 4 candidates we have + accept smaller batch
Use this batch of 4 as the test send this week. Learn from replies. If reply rate is strong, expand the harvest by using narrower title filters ("GTM Engineer" only, drop "Growth Engineer" which catches horizontal growth/PLG roles). If reply rate is weak, pivot to Path B for the next batch.

**Recommended:** Path C this week + Path B next harvest pass. Don't keep burning TheirStack credits chasing T6 yield from horizontal AI startups.

## What this means for the playbook redraw

The redraw's Step 6 ship/park decision concluded T6 + T2-merged ship. After this empirical pull, **T6 should be reframed as "smaller TAM than expected; valid where it triggers but secondary to S-A signal for Thresh's primary ICP."** The S-A candidate situation in Stage 2.5 is probably the right primary segment for Phase-1 Thresh outbound — not T6.

Next-session todo update: promote S-A from Stage-2.5 stub to a full Stage-3 segment card. T6 demoted to secondary but keep — Harper-shaped fits are still valuable when they exist.

## Files written

- `outbound/t6-test-batch-2026-05-12/raw-pull.json` — 25 records, posted last 30 days
- `outbound/t6-test-batch-2026-05-12/raw-pull-older.json` — 25 records, posted 60-90 days ago
- `outbound/t6-test-batch-2026-05-12/accounts.csv` — 4 cleaned candidates (Harper, Logicbroker, Software Toolbox, ici)
- `outbound/t6-test-batch-2026-05-12/HARVEST-NOTES.md` — this file

## Credits burned

50 of ~150 remaining. ~100 left for future queries.
