# Thresh Outbound Pipeline — Phase 0

**Last updated:** 2026-05-07
**Strategic playbook:** `~/Documents/projects/second-brain-cli/Reference/Thresh Phase 0 Playbook.md`

---

## What Phase 0 Is

30-60 day structured outbound test across **3 cells inside the Logistics & Supply Chain meta-vertical** to validate offer + list + messaging simultaneously. Goal: 300-700 emails over 4 weeks, measure positive replies by cell, decide which cell scales into Phase 1.

**Meta-vertical:** vertical SaaS whose end-customers are public-data-rich offline/regulated SMB businesses.

**Buyer filter:** Series Seed–B, $1-25M ARR, founder-led, 0-2 BDRs, no VP RevOps yet.

---

## The 3 Cells

### Cell A — Long-haul / mid-size carrier safety + migration (PRIMARY, 50% weight)

**Customer segment:** 5-50 truck long-haul carriers, owner-operator-adjacent, 1 dispatcher / 1 mechanic / no compliance manager.

**Public data anchor:** FMCSA SAFER + FMCSA Inspection Database + FMCSA SMS BASIC scores.

**Existing FMCSA artifact:** 100-Conditional-rated carriers CSV at `gtm-alpha/runs/double-nickel/pvp-data-drop-v1.csv` (already built — partial scraper exists, ready to redeploy).

**v1 cell template (signal-specific subject, pain-opener, single concrete number, interest-check CTA, value-add):**

> **Subject:** 47 long-haul carriers in TX dropped to FMCSA Conditional this month
>
> Hey [first_name] —
>
> Long-haul carriers running 5-50 trucks are getting hammered on roadside inspection scores. 47 in TX alone slid to Conditional in the last 30 days.
>
> The pattern: 1 dispatcher, 1 mechanic on call, no compliance manager — falling behind while the owner is trying to keep trucks rolling. Most aren't in any standard B2B database.
>
> I scrape FMCSA daily. Want the 47 + dispatch numbers? No catch.
>
> Lucas

#### Cell A active prospects (carry-over + Phase 0 list)

| # | Company | Sub-niche | Domain | Status / Last Touch |
|---|---|---|---|---|
| 1 | Double Nickel | CDL recruiting / compliance SaaS | getdoublenickel.com | DM sent 2026-03-01 (Francisco), connection accepted |
| 2 | Tank Payments | Payments for trucking carriers (YC S22) | tankpayments.com | Email sent 2026-05-03 (campaign 3275138, subj `factor signals`) |
| 3 | CDL Funnel | CDL recruiting | cdlfunnel.com | Need to verify founder + send |
| 4 | CDL DNA | CDL recruiting | cdldna.com | Need to verify founder + send |
| 5 | Palace.so | AI dispatch (YC S25, NYC) | palace.so | Ready — NYC, in-person possible |
| 6 | Fleetline.ai | AI load planning (YC S25, NYC) | fleetline.ai | Ready — NYC, has traction |
| 7 | Truckbase | TMS for small fleets (5-50 trucks, bootstrapped) | truckbase.com | Ready — Bryan Jones approachable via CCJ/Overdrive content |
| 8 | Spotter.ai | AI dispatch (founded 2019) | spotter.ai | Ready — more mature than Palace/Fleetline |
| 9 | Trucksafe | DOT training + compliance consulting | trucksafe.com | Ready — strongest non-recruiting fit; Brandon Wiseman would understand instantly |
| 10 | OpenEyes | Fleet insurtech (Series A $23M, Austin) | openeyes.com | Ready — pitch crash data, not OOS rates |
| 11 | Koffie Financial | Trucking insurance MGA (Series A $11M, Brooklyn) | koffie.com | Ready — DON'T pitch data as novel; pitch prospecting angle |

**Cell A sub-niche pitch nuances** (preserved from prior work — apply within the v1 template skeleton):

- **Recruiting (Double Nickel, CDL Funnel, CDL DNA):** lead with driver OOS rate + inspection count; frame as screening/qualification breakdown.
- **Dispatch / TMS (Palace, Fleetline, Truckbase, Spotter):** lead with inspection volume + OOS frequency; frame as "routes breaking" and "loads getting rescheduled" — these founders think in fleet utilization and revenue-per-mile.
- **Compliance consulting (Trucksafe):** most natural fit — their entire business is fixing what FMCSA exposes. Lead with Conditional rating + CSA score language.
- **Insurtech (OpenEyes):** lead with crash + fatal incident data, not OOS. Insurance buyers think in claims frequency and severity.
- **Insurance MGA (Koffie):** they already pull FMCSA for underwriting — DON'T pitch data as novel. Pitch prospecting intelligence: "carriers in acute distress = insurance shoppers when their current carrier non-renews."

#### Cell A Phase 0 expansion list (to build)

Build TAM filter in Clay: B2B SaaS + Series Seed–B + $1-25M ARR + sells into trucking/fleet operators + at least one of (hiring GTME/RevOps in last 90 days, JD mentions Clay/Apollo/SmartLead, no BDRs but 3+ AEs). Run Claygent classification column to validate Cell A fit. Target: 100-200 net-new prospects beyond the 11 above.

---

### Cell B — Reverse-logistics / hazmat shippers (WHITESPACE, 30% weight)

**Customer segment:** hazmat generators, reverse-logistics shippers, electronics/aerospace recyclers.

**Public data anchor:** EPA ECHO + RCRAInfo (waste generators, treatment/storage/disposal facility data, enforcement records).

**Strategic note:** No existing GTM Alpha output here — this is a gap-fill cell. Jordan validates it works (Reconext ×3 plays at 9.8/9.5/9.4). Lucas is running it cold.

**v1 cell template (sketched — refine before sending):**

> **Subject:** 23 RCRA generators in PA hit Significant Non-Compliance this quarter
>
> Hey [first_name] —
>
> Mid-size hazmat generators are sliding into RCRA Significant Non-Compliance status faster than I've ever seen — 23 in PA alone hit SNC in the last 90 days.
>
> Most of these are facilities running waste manifests through legacy paper-or-PDF processes, no real-time visibility into shipping discrepancies, no one watching enforcement filings.
>
> I scrape EPA ECHO weekly. Want me to send the 23 + their TSDF relationships? No catch.
>
> Lucas

#### Cell B Phase 0 prospect list (to build)

Build TAM filter: B2B SaaS + Series Seed–B + $1-25M ARR + sells into reverse-logistics / hazmat / waste / electronics-recycling. Target: 50-100 prospects. Anchor reference vendor: Reconext-style platforms.

---

### Cell C — PE-acquired regional waste & specialty haulers (LUCAS-DISTINCTIVE, 20% weight)

**Customer segment:** PE-rolled regional waste/specialty haulers under 18-month integration timelines.

**Public data anchor:** M&A press releases, state mandates (CA SB 1383, organics RFPs), CalRecycle data.

**Strategic note:** Lucas's most-developed cell — Hauler Hero already produced 10 plays on this exact pattern. Jordan barely covers. v2 hydration is harder (state-level data, no clean federal API) — defer scraper build until Cell C signal proves out.

**Existing artifact:** Waste hauler data drop CSV ready, draft email written for Hauler Hero.

**v1 cell template (sketched):**

> **Subject:** Your acquirer has 18 months to absorb you — here's the 90-day playbook
>
> Hey [first_name] —
>
> Regional waste & specialty haulers acquired by PE in the last 12 months are facing the same compressed timeline: 18 months to integrate ops + tech + brand before the next valuation event.
>
> The pattern I'm seeing: M&A press hits, then 90 days of nothing, then frantic RFPs for routing/dispatch/customer-mgmt platforms — usually with a Q4 deadline tied to the rollup's reporting cycle.
>
> I track waste hauler M&A + state mandate triggers (SB 1383, organics RFPs). Want the list of acquired haulers within 90 days of their integration deadline? No catch.
>
> Lucas

#### Cell C active prospects

| # | Company | Sub-niche | Domain | Status |
|---|---|---|---|---|
| 1 | Hauler Hero | Waste management SaaS for regional haulers (Series A $16M) | hauler-hero.com | 10 plays drafted, email ready, just send |

#### Cell C Phase 0 expansion list

Build TAM filter: B2B SaaS + Series Seed–B + $1-25M ARR + sells into waste/specialty/regional haulers + at least one M&A or state mandate signal. Target: 30-60 prospects. Lower volume than A/B because the cell is narrower.

---

## Phase 0 Sequencing

```yaml
DAY_0_today_2026-05-07:
  decisions:
    - "Lock cell scope: A + B + C, weighted 50/30/20"
    - "Pricing tiers documented in thresh.md"
  outputs:
    - "Clay TAM filter spec built per cell"
    - "Claygent classification column configured"

DAY_1_to_2:
  outputs:
    - "Hand-write 3 cell email templates (refine the sketches above)"
    - "Build Cell A net-new list (~100-200 prospects)"
    - "Build Cell B prospect list (~50-100 prospects, this is the gap-fill)"
    - "Build Cell C prospect list (~30-60 prospects)"
    - "Run Claygent classification, filter rejects"
    - "Pull decision-makers (founder Tier 1, head-of-revenue fallback)"
    - "Load into SmartLead, 3 campaigns segmented by cell"

DAY_3_to_5:
  outputs:
    - "Begin sending v1 — 10%/day ramp until full capacity"
    - "Single first-touch per prospect, no follow-ups in v1"
    - "Track positive replies sortable by cell"
    - "Send Hauler Hero email (Cell C, already drafted)"
    - "Follow up Tank Payments thread if no response by day 5"
    - "Follow up Double Nickel DM if no response by day 5"

DAY_6_to_14:
  parallel_work:
    - "Continue sending at full capacity"
    - "Build FMCSA SAFER API wrapper (~4-8 hrs)"
    - "Build EPA ECHO API wrapper (~4-8 hrs)"
    - "Build Claude subagent: (cell, segment, geography) → one signal hook number"

DAY_15_to_30:
  outputs:
    - "Ship v2 emails — Cells A + B with hydrated per-prospect data hooks"
    - "Cell C stays at v1 (state-data scrapers deferred)"
    - "Track v1 vs v2 reply rate lift per cell"

DAY_30_CHECKPOINT:
  measure: "positive_reply_rate by cell"
  decisions:
    - "If <0.5% across all cells: rewrite messages (don't blame list yet)"
    - "If >1% in one cell, <0.3% in others: double down on winner"
    - "If positive replies but no meetings: continue, meetings lag replies"

DAY_60_CHECKPOINT:
  measure: "meetings_booked from positive replies"
  decisions:
    - "If meetings booking: offer is real, scale top cell into Phase 1"
    - "If positive replies but zero meetings: offer problem on the call, fundamental rethink"
    - "If a cell shows zero signal at day 60: kill it, redeploy capacity"
```

---

## Decision Framework

- **Scale a cell** when: >1% positive reply rate sustained over 30 days + >10% positive-reply-to-meeting conversion.
- **Pivot a cell** when: <0.5% at day 30 (try v2 hooks first); <0.5% at day 60 with multiple variants tested = cell is dead.
- **Deprioritize Cell C** if v1 generic hooks underperform A+B by 50%+ AND A or B is hitting >1%. Defer to Phase 1 rather than building state-mandate scrapers.
- **Add a 4th cell** only after one cell has booked 2+ paying clients (Phase 0 → Phase 1 transition).

---

## Adjacent / Parked

These don't fit the 3-cell Phase 0 structure but stay live as side-door inbounds or future expansion.

| # | Company | Sub-niche | Domain | Status / Notes |
|---|---|---|---|---|
| - | Usul | Defense tech — AI gov contracting (YC S24, $3.3M) | usul.com | Intro call booked Mar 6; defense tech as potential signature vertical for Thresh post-Phase 0 if Logistics underperforms |
| - | Coverforce | Insurance distribution API (P&C / PEO / carriers) | coverforce.com | Tier 1 from gtm-alpha runs; insurance/NAIC angle ready; adjacent meta-vertical (regulated, but customers may be on LinkedIn — re-test 4-quadrant fit) |
| - | Stratus | BIM-to-fabrication for MEP/sheet metal contractors | stratus.build | Tier 1; construction-adjacent; potential Phase 1 cell if "construction SaaS" cluster opens |
| - | Usekojo | Construction materials procurement | usekojo.com | Tier 1; same as above |
| - | Chartahealth | AI pre-billing for healthcare practices | chartahealth.com | Adam Morris call booked 2026-03-06; healthcare meta-vertical, separate Phase 1+ cluster |
| - | Lightlabs | ISO 17025 food/supplement testing lab | lightlabs.com | Active thread; FDA warning letters anchor; food safety meta-vertical |

---

## Sent Log

See `outbound/sent-log.md` for individual send timestamps and reply tracking.
