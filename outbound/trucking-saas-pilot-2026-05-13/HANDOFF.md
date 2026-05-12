# Trucking SaaS Pilot Handoff

Last updated: 2026-05-12

## Current State

Smartlead campaign is configured and ready to send Wednesday, May 13, 2026.

- Campaign: `Thresh - Trucking SaaS Mini-PVP - 2026-05-13`
- Campaign ID: `3326039`
- Status at setup: `DRAFTED`
- Leads loaded: 5
- Sequence steps: 1 first-touch email, no follow-ups
- Schedule: Wednesday only, 9:00am-3:00pm ET, 75 minutes between sends
- New leads/day: 5
- Main mailbox excluded: `lucas.linares@runthresh.com`
- Open/click tracking disabled
- Stop on reply enabled
- Plain text enabled

## Journey Recap

### Where We Started

We started with a broad vertical SaaS TAM problem:

- Vertical SaaS does not map cleanly to LinkedIn/Apollo industry filters.
- Clay company search was too broad and noisy.
- Lookalike search could source likely-fit companies, but only after seed quality was improved.
- The original idea was: build a full world of possible accounts, run a fit gate, segment by team structure, find contacts, generate outbound.

The first architecture was:

1. Source companies from lookalikes.
2. Run a Fit Gate.
3. Classify team state.
4. Route to message angles.
5. Send.

That was directionally right, but it was missing a stronger answer to: what makes the first email valuable enough to earn attention?

### What We Learned From Jordan

Jordan pushed on three core points:

1. **Fit vs. timing is right, but TAM sourcing is separate.**
   - Lookalike-seeded TAM is the right v1.
   - Do not try to run lookalikes, vertical-by-vertical sourcing, and open signal streams all at once.

2. **The first hook must be SaaS-side pain, not carrier pain.**
   - FMCSA data is not the SaaS founder's core problem.
   - Their core problem is pipeline, reply quality, account selection, broken outbound, or a VP Sales mandate.
   - Carrier data is proof that Thresh can find better accounts.

3. **The CTA needed to become a mini-PVP.**
   - "Want me to pull 10 prospects?" is too weak.
   - The better move: show 3 named carrier examples now, then ask if they want the full trucking playbook.
   - The data has to already be in the email.

Jordan also clarified the scale model:

- The 3 carrier examples do not need to be unique per prospect.
- They need to be unique per **bucket**.
- Scale comes from building a carrier-signal bucket library, not manually researching every prospect.

### Where We Landed

We landed on a 5-send trucking SaaS pilot with:

- 5 verified contacts.
- 5 mapped product buckets.
- 3 named carrier examples per prospect.
- A one-step Smartlead campaign.
- No follow-ups yet.
- Tracking focused on whether the PVP works.

The pilot sends to:

| Company | Contact | Bucket |
|---|---|---|
| FleetOperate | Sharan Savadattimath | Motus / MCS-150 compliance |
| Simply Fleet | Mrigaen Kapadia | Maintenance / vehicle OOS |
| Ezlogz | Sergey Karman | DVIR / driver compliance |
| Tourmo | Ricardo Silva | Safety risk / FMCSA red flags |
| Trucking Hub | Milos Pavlovic | New authority / dispatch motion |

The most important learning signal is not reply rate at N=5. It is whether someone quotes a carrier name back or asks for the full playbook.

## Key Operating Principles Going Forward

1. Do not scale the 5-send campaign itself.
   - It is the proof test.
   - Keep it clean.

2. Scale the system behind it.
   - Build more seed companies.
   - Qualify with the Fit Gate.
   - Map every kept account to a bucket.
   - Use bucket-level carrier examples.

3. Use one message skeleton per segment.
   - Do not generate random AI copy per lead.
   - The variable part is the bucket proof block and SaaS-side opener.

4. Track learning at the bucket level.
   - Positive replies by bucket.
   - Carrier-name quote-backs by bucket.
   - Full playbook requests by bucket.
   - Meetings by bucket and persona.

## Next Phase Plan

### Phase 1: Observe the 5-Send Pilot

Time window: May 13-20, 2026

Goal:

Learn whether mini-PVP proof blocks create enough curiosity to justify scaling.

Track:

- Did all 5 send?
- Any bounce?
- Any positive reply?
- Did they quote a carrier name?
- Did they ask for the full trucking playbook?
- Did a meeting get booked?

Decision rule:

- 1 carrier-name quote-back or full playbook request: build next 20 immediately.
- Curious replies without carrier mention: tighten PVP block before expanding.
- No replies after 5 business days: inspect SaaS-side opener/trigger before rewriting the whole system.

### Phase 2: Build the Next 50

Goal:

Create the next send-ready pool without adding to the first campaign.

Pipeline:

1. Run more Discolike clusters.
2. Require company LinkedIn URL.
3. Run Fit JSON.
4. Keep only:
   - fit status = `keep`
   - fit score 4 or 5
   - campaign lane not `adjacent_research`
5. Run team-state enrichment only after fit passes.
6. Find one senior contact.
7. Validate contact.
8. Find work email.
9. Map each company to a carrier-signal bucket.
10. Export Smartlead-ready rows.

Target output:

- 50 qualified trucking/logistics SaaS accounts.
- 30-40 verified contacts.
- 20-30 send-ready after email waterfall.

### Phase 3: Expand Carrier Bucket Library

Goal:

Move from 10 examples per bucket to 30-50 examples per bucket.

Priority buckets:

1. Motus / MCS-150 / business verification
2. Vehicle OOS / maintenance inspection failures
3. Driver OOS / DVIR / driver compliance
4. Safety risk / crashes / BASIC scores
5. New authority / dispatch motion

Schema to keep:

- bucket
- wedge type: pain or motion
- freshness type: fresh or structural
- finding type
- carrier name
- DOT number
- fleet size or driver count
- finding
- source
- selected for
- sent to
- sent date
- reply quoted carrier

### Phase 4: Launch Cohort 2

Only after pilot sanity checks.

Starting send size:

- 15-20 sends if no deliverability issues.
- 30-50 sends if pilot gets a strong qualitative reply.

Sender rules:

- Do not use `lucas.linares@runthresh.com`.
- Round-robin across non-main inboxes.
- No more than 2 leads/day per mailbox at current ramp.
- Keep the same sender on follow-ups.
- Do not use multiple senders to the same company.

## Tomorrow To-Do List

### Morning

1. Confirm campaign is active/running and still scheduled for Wednesday only.
2. Confirm no emails sent before 9:00am ET.
3. Around 9:15am ET, confirm first email sent.
4. Check sender used on first lead.
5. Do not edit the campaign unless rendering breaks.

### Midday

6. Check sends after 11:30am ET.
7. Watch for bounce/failed-send issues.
8. If a reply comes in, do not pitch a meeting immediately.
9. If positive, reply:

```text
Yep. I’ll run the full version for {{company}} and send it over.

I’ll keep it tight: the carrier signal, why it maps to your product, and the first outbound angle I’d test.
```

### Afternoon

10. Confirm all 5 sent by 2:30-3:15pm ET.
11. Fill a simple reply tracker:
    - company
    - replied yes/no
    - positive/neutral/negative
    - quoted carrier yes/no
    - playbook requested yes/no
    - meeting booked yes/no
12. If nobody replies yet, leave it alone. Do not add follow-ups the same day.

### Parallel Build Work

13. Start a new table for Cohort 2.
14. Pull more Discolike lookalikes across logistics/trucking SaaS clusters.
15. Run the same Fit JSON and LinkedIn URL gate.
16. Build a 50-account shortlist.
17. Expand carrier buckets to 30 examples each.

## Files In This Folder

- `send-plan.md`: pilot send rules and schedule
- `carrier-buckets.csv`: current 50 carrier examples
- `smartlead-copy.md`: sequence copy and fallback follow-up
- `smartlead-import.csv`: 5 lead import rows
- `smartlead-setup-summary.md`: Smartlead campaign setup record
- `setup_smartlead_campaign.py`: reproducible campaign setup script; requires `SMARTLEAD_API_KEY` env var
- `verify_smartlead_campaign.py`: campaign verification script; requires `SMARTLEAD_API_KEY` env var
- `smartlead-state.json`: campaign ID only

No API key is stored in this folder.

## Suggested Prompt For The Next Chat

```text
We are continuing the Thresh trucking SaaS outbound pilot.

Read:
- /Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13/HANDOFF.md
- /Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13/smartlead-setup-summary.md
- /Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13/carrier-buckets.csv

Current goal: monitor the 5-send Smartlead pilot, then build Cohort 2 with 50 qualified accounts and expand the carrier bucket library.
```

