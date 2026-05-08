# Thresh Outbound Pipeline — Trucking SaaS (Phase 0)

**Last updated:** 2026-05-07
**Scope:** Trucking SaaS only. Single-vertical Phase 0 test. Hazmat / waste-hauler verticals parked until trucking validates.

---

## What this doc is

The operating playbook for a single-vertical outbound campaign. Messaging architecture is sourced from the play corpora (Blueprint + GTM Alpha) — not human-pre-written or AI-generated per send. The corpus query establishes which public databases, signal categories, and pain phrases dominate trucking SaaS messaging via cross-corpus frequency.

**Cross-account state lives elsewhere:**
- Per-prospect status / sent emails: `MEMORY.md` + `outbound/sent-log.md` (gitignored)
- Per-account drafts + deliverables: `gtm-alpha/runs/<account>/outbound/`

This doc is for the *system*, not the *log*.

---

## The flow

```
                          ┌──────────────────────────┐
   1. Corpus query        │ Both Supabase corpora    │
      (run monthly)  ──→  │ blueprint_plays          │
                          │ gtm_alpha_plays/signals  │
                          └────────────┬─────────────┘
                                       │
                                       ↓
                          ┌──────────────────────────┐
                          │ Messaging registry       │
                          │ (§4 below)               │
                          └────────────┬─────────────┘
                                       │
   2. Audience sourcing                │
      (Clay / Ocean.io / Discolike     │
       — handled outside this doc)     │
                                       ↓
                          ┌──────────────────────────┐
   3. Per-prospect AI ──→ │ Clay/Claygent:           │
                          │  • classify (in-vertical)│
                          │  • hydrate enrichment    │
                          └────────────┬─────────────┘
                                       │
                                       ↓
                          ┌──────────────────────────┐
   4. SmartLead send ───→ │ Skeleton + registry      │
                          │ + per-prospect slots     │
                          └──────────────────────────┘
```

The corpus refresh script: `outbound/queries/trucking-saas-corpus.py`. Run it whenever the corpora update. Output lives at `outbound/queries/trucking-saas-corpus-output.json`.

---

## Email skeleton

```
Subject: signal-based outbound for {{vertical_descriptor}} SaaS

Hey {{first_name}},

A lot of {{customer_segment}} show {{pain_phrase}} publicly before they shop for new software:
• {{signal_1}}
• {{signal_2}}
• {{signal_3}}

Carriers triggering these at once (plus {{adjacent_signals}}) are in a buying window. Standard outbound stacks miss them — they look identical to dormant carriers in Apollo.

I dig public-data signals across {{db_count}} {{db_type}} databases for {{vertical_descriptor}} SaaS. Want me to pull what's currently hitting {{company_domain}}'s TAM? Takes ~24 hours.

Lucas
```

**Why this structure (mapped to playbooks):**
- **Bullets 1-3 = "lead with their situation, not your product"** (Rule 1, Signals & Messaging Playbook). Describes the recipient's customers' world before product appears.
- **Implication line ("look identical to dormant carriers in Apollo")** = PLA amplifier #1 (attach to existing investment — they already believe in their outbound stack; the gap rides that belief). Per the PLA doc: *"Find what they're already spending money/time on; make your outcome extend it."*
- **Capability claim ("I dig public-data signals")** = verb-led, not product-led. Replaces SaaS-coded language ("pipeline," "TAM," "plays") with action language. Per Rule 4 (inferred personalization): doesn't reveal methodology / doesn't sound automated.
- **Single low-friction CTA** with concrete time (~24 hrs) = Message Mechanics Checklist requirement.
- **No deliverable shape promise.** The actual GTM Alpha output (3-5 plays, named prospects, sourced links, draft openers — see `/Users/lucas/Documents/projects/gtm-alpha/runs/hauler-hero/outbound/3-plays.md`) is what the recipient gets after they say yes; the cold email doesn't sell the deliverable spec, it sells the *intel preview*.

### Slot taxonomy

| Slot | Filled by | Notes |
|---|---|---|
| `vertical_descriptor` | **Registry constant** | `trucking` for this vertical |
| `pain_phrase` | **Registry constant** | `compliance strain` (corpus-derived, see §4) |
| `signal_1` / `signal_2` / `signal_3` | **Registry constant** | The 3 bullets are pre-written from the top corpus signal cluster — same on every send in this vertical (segmentation > personalization) |
| `adjacent_signals` | **Registry constant** | `job postings, M&A press, recent insurance changes` — adjacent corpus sources outside the FMCSA cluster |
| `db_count` / `db_type` | **Registry constant** | `4-5` / `federal` |
| `first_name` | Per-prospect enrichment | Clay |
| `customer_segment` | Per-prospect enrichment (light) | E.g., "long-haul small fleets," "regional carriers" — derived from prospect's homepage, one of ~3 fixed values |
| `company_domain` | Per-prospect enrichment | Clay |

**Rule:** The registry constants are written once per vertical and locked. Per-prospect AI only fills enrichment slots (`first_name`, `customer_segment`, `company_domain`). This is the discipline that defeats AI-SDR pattern detection — recipients in the same vertical see consistent messaging architecture, not dice-rolled prose.

---

## Trucking SaaS messaging registry

Generated 2026-05-07 from `trucking-saas-corpus.py` (166 Blueprint plays + 28 GTM Alpha plays + 43 GTM Alpha signals = **237 messaging rows**).

### Top public data sources (ranked by cross-corpus frequency)

| Rank | Data source | Total | Blueprint | GTM Alpha | Double-validated |
|---|---|---|---|---|---|
| 1 | FMCSA (general / DOT) | 88 | 65 | 23 | ✓ |
| 2 | FMCSA SAFER | 56 | 40 | 16 | ✓ |
| 3 | FMCSA SMS BASIC / CSA | 39 | 33 | 6 | ✓ |
| 4 | LinkedIn (firmographic) | 26 | 4 | 22 | ✓ |
| 5 | FMCSA Inspection DB | 24 | 24 | 0 | |
| 6 | EPA / ECHO / RCRA | 21 | 21 | 0 | |
| 7 | News / web scrape | 18 | 3 | 15 | ✓ |
| 8 | Job postings | 17 | 2 | 15 | ✓ |
| 9 | OSHA | 14 | 14 | 0 | |
| 10 | M&A press / PE filings | 11 | 3 | 8 | ✓ |

**FMCSA-anchored sources alone (1+2+3+5) = 207 of 237 rows = 87% of trucking SaaS messaging is keyed off FMCSA data.** That's the dominant signal architecture for this vertical.

**Vendors in GTM Alpha logistics corpus:** Double Nickel, Hauler Hero, Samsara, Tank Payments, Truckstop.

### Email constants for this vertical

| Slot | Locked value | Derivation |
|---|---|---|
| `vertical_descriptor` | `trucking` | — |
| `pain_phrase` | `compliance strain` | Most plays cluster around safety/compliance triggers |
| `signal_1` | `FMCSA SAFER rating drops to Conditional` | Top FMCSA source, both corpora |
| `signal_2` | `DOT SMS BASIC scores sliding into red zones` | 2nd-most-cited, both corpora |
| `signal_3` | `Roadside inspection failure clusters by region` | Inspection DB, Blueprint-dominant |
| `adjacent_signals` | `job postings, M&A press, recent insurance changes` | Adjacent corpus sources outside FMCSA — used in the implication line to broaden the deliverable scope |
| `db_count` | `4-5` | FMCSA SAFER + SMS BASIC + Inspection DB + Crash + L&I |
| `db_type` | `federal` | — |

### Customer segment values (for per-prospect hydration)

Buyer's customer segment, derived from the prospect's homepage by Claygent. One of:
- `long-haul small fleets` — owner-operator-adjacent, 5-50 trucks (Cell-A canonical)
- `regional carriers` — multi-state, 50-500 trucks
- `mixed-fleet operators` — long-haul + regional + intermodal

If Claygent can't determine confidently → reject the prospect (don't send).

### Persona priority

GTM Alpha plays don't tag persona consistently. Default order for contact-finding:
1. Founder / CEO (founder-led, 0-2 BDRs target)
2. Head of Sales / VP Sales / CRO
3. Head of Revenue / RevOps lead
4. Founding AE / first SDR (last-resort, signals readiness gap)

---

## Active prospects (carry-over)

Status from `MEMORY.md` + `sent-log.md` as of 2026-05-07.

| # | Company | Domain | Status |
|---|---|---|---|
| 1 | Double Nickel | getdoublenickel.com | Multi-touch — Francisco DM accepted (no email reply); Alex Croce + Deven cold emails sent 2026-05-05, awaiting |
| 2 | Tank Payments | tankpayments.com | Cold email sent 2026-05-03 (campaign 3275138, subj `factor signals`) — awaiting |
| 3 | CDL Funnel | cdlfunnel.com | Need founder verification + send |
| 4 | CDL DNA | cdldna.com | Need founder verification + send |
| 5 | Palace.so | palace.so | Ready — NYC, in-person possible |

(GTM Alpha vendors Samsara + Hauler Hero are appearing in corpus as *playbook subjects* — they're prior Lucas/Jordan analysis targets, not necessarily current outbound prospects. Hauler Hero already in active engagement, Samsara framing-layer rewrite shipped 7c1dec8.)

---

## Phase 0 sequencing

### Day 0 (today)
- [x] Corpus registry locked (this doc, §4)
- [x] Email skeleton locked (§3)
- [ ] Build Clay TAM list — trucking SaaS, $1-25M ARR, Series Seed-B, founder-led, 0-2 BDRs
- [ ] Configure Claygent classification column: input `homepage` → output `customer_segment` ∈ {long-haul small fleets, regional carriers, mixed-fleet operators, REJECT}
- [ ] Configure Claygent enrichment columns: `first_name`, `company_domain`, `vertical_descriptor=trucking`
- [ ] Load SmartLead campaign — single skeleton, slots wired from Clay columns

### Day 1-2
- [ ] Verify enrichment quality on first 20 rows manually
- [ ] **Merge-tag check (hard pre-send gate):** spot-check the rendered email on 5 random rows in SmartLead before any auto-send. If a `{{first_name}}` / `{{customer_segment}}` / `{{company_domain}}` slot ever renders literally, the email is dead on arrival — pause campaign until Clay column is fixed.
- [ ] Verify deliverability — SmartLead inbox health on all 9 inboxes
- [ ] Push first 10 sends manually (not auto) to confirm rendered output

### Day 3-5
- [ ] Begin auto-send, 10%/day ramp (Taylor Haren Stage 3 rule)
- [ ] Single first-touch per prospect — no follow-ups in v1
- [ ] Tag positive replies in HubSpot for Day 30 measurement

### Day 6-30
- [ ] Continue sending at full capacity (8-min gap, weekdays only per current SmartLead config)
- [ ] When prospect replies "yes" to "want me to run it on {company}?" → trigger hand-raiser sequence (see §below)

### Day 30 — reply rate checkpoint
Measure: positive_reply_rate over the cohort.

### Day 60 — meetings booked checkpoint
Measure: meetings_booked from positive replies.

---

## Decision checkpoints

| Day | Signal | Decision |
|---|---|---|
| 30 | Reply rate <0.5% | Message problem — rewrite skeleton or registry. Don't blame the list. |
| 30 | Reply rate >1% | Continue. Audience + message both working. |
| 30 | 0.5-1% | Iterate one slot at a time (subject → opener → CTA), one variable per week. |
| 60 | Positive replies but zero meetings booked | Offer-on-call problem. Rethink what happens after "yes." |
| 60 | Meetings booking | Scale: increase send volume, or add second vertical from §below. |

---

## Hand-raiser sequence (after positive reply)

When prospect replies "yes, run it on {company.com}":

1. **Within 24 hrs** — run GTM Alpha for their domain (~1-2 hr compute). Reply with attached PDF of the playbook for *their* company. Body: *"Attached. 5 plays built specifically for {company} using the signals from my last note. Anything stand out, or any of these miss the mark?"*
2. **2-3 days later** — pitch Thresh: *"The playbook is a one-time snapshot. Thresh runs the underlying pipeline weekly, refreshes prospect lists, iterates messaging based on response data, and I work the campaign personally for the first 4 weeks. 60-90 days end-to-end — you inherit the system."*
3. **3-5 days later (silence)** — operator giveaway: *"Before I let this go — attached is the operator checklist + database registry + claim provenance map you'd need to run this yourself. Best of luck either way."*

Operator giveaway also seeds future top-of-funnel content marketing once 5+ prospects have received it.

---

## Future verticals (parked)

Two adjacent verticals identified but deferred until trucking validates:

- **Reverse-logistics / hazmat shippers** — EPA ECHO + RCRAInfo as anchor. Whitespace cell (Lucas has no plays here yet). Reconext-style platforms.
- **PE-acquired regional waste haulers** — M&A press + state mandates (CA SB 1383, organics RFPs). Lucas's most-developed cell content (Hauler Hero), but state-level scrapers are harder than federal APIs.

Add when: trucking SaaS hits >1% reply at Day 30 AND books 2+ paying clients.

---

## Refreshing the registry

```bash
python3 outbound/queries/trucking-saas-corpus.py
```

Reads `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` from `../blueprint-scraper/.env` (both projects share one Supabase instance). Rewrites `outbound/queries/trucking-saas-corpus-output.json` and prints top sources to stdout.

When to re-run:
- New plays added to either corpus (new Blueprint scrape, new GTM Alpha extraction)
- Day 30 / Day 60 checkpoint inputs
- Considering a vertical pivot (re-run with different industry filter)
