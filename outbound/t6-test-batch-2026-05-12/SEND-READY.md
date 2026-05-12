# T6 Test Batch — Send-Ready Checklist (2026-05-12)

> **What this is.** Everything Lucas needs to do between now and clicking send on the 4 drafts in `drafts/`.

## The batch

| # | Draft file | Account | Recipient | Angle | Role-open days |
|---|------------|---------|-----------|-------|----------------|
| 01 | `drafts/01-harper-dakotah.md` | Harper | Dakotah Rice (CEO) | Founder | 61 |
| 02 | `drafts/02-harper-sebastian.md` | Harper | Sebastian Correa (Head of Growth) | Sales/Growth | 61 |
| 03 | `drafts/03-softwaretoolbox-mcmahon.md` | Software Toolbox | Michael Mcmahon (CFO) | Exec (marketing-tilted) | 68 |
| 04 | `drafts/04-softwaretoolbox-win.md` | Software Toolbox | Win Worrall (Sales Director) | Sales (marketing-tilted) | 68 |

## Before you hit send

### 1. Visual-verify each role is still active

- **Harper:** open https://jobs.ashbyhq.com/harperinsure/0e713032-76ec-4c12-b244-f99ffbc198a9 — confirm the GTM Engineer role is still listed and accepting applications. (WebFetch couldn't render the Ashby SPA so this is a manual check.)
- **Software Toolbox:** open https://www.softwaretoolbox.com/careers — confirm the GTM Engineer role is still listed. (Was live as of 2026-05-12 per WebFetch.)
- If either role is gone → drop those drafts. The signal is broken.

### 2. Substitute the CTA playbook name

The drafts say "Want the playbook we shipped for commercial insurance?" / "...for industrial automation?" Neither matches your 8 live playbooks exactly.

| Draft target vertical | Closest live playbook | Suggested CTA substitution |
|------------------------|------------------------|----------------------------|
| commercial insurance (Harper drafts 01, 02) | `withassured.com` (verify it covers insurance — open `playbooks/withassured-com/`) | "Want the Assured playbook?" or keep "commercial insurance" if Assured is the right shape |
| industrial automation (Software Toolbox drafts 03, 04) | `samsara.com` (fleet telematics, industrial-adjacent) | "Want the Samsara playbook?" or "Want the playbook we shipped for fleet telematics?" — flag the adjacency |

**If no shipped playbook fits:** rewrite the CTA to soften the claim. Suggestions:
- "Want a sample play from our most relevant deliverable?"
- "Want the closest playbook we've shipped (fleet telematics)?"

### 3. Pick which inbox to send from

Per memory's `Email Infrastructure` setup — you have 9 inboxes across 4 domains. Recommended pattern:
- Send Harper from one inbox, Software Toolbox from a different inbox. Different domain ideally.
- Stagger 1-2 days between the two contacts at the same account (Dakotah vs. Sebastian) so they don't land in the same hour.

### 4. Cold-email-craft scan (final pass)

Each draft already passed the scan as templates. Re-scan after you make CTA substitutions — that's the only place new failure modes could enter.

### 5. Send + log

After send:
- Update `outbound/sent-log.md` with each send (date, recipient, inbox-used, subject)
- Update `outbound/pipeline.md` if you treat these as named-prospect entries
- Set a Day-7 follow-up reminder if no reply

## Reply ammo (if recipient pushes back)

These are reserve facts for in-thread responses, NOT for first-touch:

- **Cannonball GTME-rename (2026-01-31):** Jordan Crawford / Doug Bell renamed their term from "GTM Engineer" to "Revenue Growth Engineer" because the term was getting watered down. Source: cannonballgtm.substack.com — "Why We're Changing from GTM Engineers to Revenue Growth Engineers"
- **The Reddit canceller quote:** "Yeah the Sculptor thing killed our need for a dedicated gtm engineer... we spent months perfecting Clay waterfalls only to get 40% bounce rates because the underlying data sucked." (Reddit · r/SaaS · 2026-05-03)
- **The data-quality meta-EDP:** "Once you automate list building, you realize the bottleneck was never there anyway. It's still data quality." (Reddit, Q-165 in harvest)

## What's deliberately NOT in the drafts

- No constructed urgency ("worth 20 min before that hire's first day," etc.)
- No "Saw your LinkedIn post" opener
- No "we audited 14 of your threads" (that was a fabricated specificity in the prior draft, dropped)
- No attachments
- No meeting ask in first touch — single low-friction artifact CTA only

## If the batch underperforms

Track reply outcomes. If reply rate is <2% across all 4:
- The T6 hypothesis weakens further
- Pivot next batch to S-A signal (new VP Sales / CMO hired last 90 days at vertical SaaS) — see `research/playbook-redraw-2026-05-12.md` Stage 2.5
- Or pivot to direct-vertical signals (FMCSA Motus, etc.) that are already in flight

If reply rate is ≥10%: T6 works at small batches. Run a larger pass with stricter title filters ("GTM Engineer" only, drop "Growth Engineer" / "Revenue Engineer") to reduce horizontal-SaaS noise.
