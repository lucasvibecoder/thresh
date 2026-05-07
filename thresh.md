# thresh.md — Business Operating Document

**Last updated:** 2026-05-07

> **Status (2026-05-07):** Operating doc, evolving. Offer reframed around in-engagement carry-the-bag validation; pricing tiers documented. Phase 0 outbound test active across 3 cells inside Logistics meta-vertical. Pricing and exact engagement scope still pending validation from Phase 0 results.

---

## What Thresh Is

Forward-Deployed GTM Engineering applied to outbound. A temporary builder who embeds inside a B2B company, deploys a custom signal-based outbound system, instruments it, documents it, and leaves it working in the team's hands. Same archetype as Palantir's FDEs, Vista's VCG, Alpine's CIT — applied to outbound rather than enterprise software or services rollups.

The work: find public-data pain signals, build target lists, write messages so valuable that the receipient would pay to receive (PVPs), launch the first campaigns, leave a working system the client owns.

Default engagement shape: 60-90 day deployment, optional extension if both parties want to keep going.

---

## Current Direction (2026-05-07)

Active Phase 0 validation across **3 cells inside the Logistics & Supply Chain meta-vertical** — Cell A (long-haul/mid-size carrier safety, FMCSA-anchored), Cell B (reverse-logistics/hazmat shippers, EPA ECHO-anchored), Cell C (PE-acquired regional waste haulers, M&A + state mandate-anchored). 30-day positive reply rate by cell determines which to scale into Phase 1.

Strategic playbook + sequencing: `~/Documents/projects/second-brain-cli/Reference/Thresh Phase 0 Playbook.md`. Operational state: `outbound/pipeline.md`.

---

## The Offer

A 60-90 day deployment where Lucas embeds with a vertical SaaS company, builds a custom signal-based outbound system, **AND personally books the first N qualified meetings off it before handing the system to the client's team.** The wedge against PMM-led competitors (Slingshot, Blueprint) is the in-engagement validation — Lucas carries the bag for the first 4 weeks himself, so the client inherits a working production line plus the credibility of an ex-SDR, founding AE who booked meetings off it before the handoff.

The 7-piece deliverable system (deliverable #5 is the headline outcome the other six support):

1. **Pain signal map** — 5+ validated signals showing "this prospect is bleeding right now"
2. **Data source registry** — 3-5 unique public data sources mapped to their vertical, with API/scrape playbooks
3. **Validated ICP** — live list of companies currently triggering the signals (proof the pipeline works)
4. **Messaging framework** — PVP-style messages keyed to each signal, tested by Lucas in production
5. **First campaign — N meetings personally booked by Lucas in the first 4 weeks** (the headline outcome — distinguishes Thresh from "we built a system, your team executes" competitors)
6. **Instrumented dashboard** — signal → enriched contact → message → response → meeting
7. **Runbook** — "follow this and you'll book meetings like the N I just put on your calendar"

### Pricing tiers (working hypothesis, pending Phase 0 validation)

| Tier | Cost | Delivery | Purpose |
|---|---|---|---|
| **Free Playbook buildout (the output of GTM-Alpha)** | $0 | GTM Alpha output: 5+ signals + 3 PVPs + 5 named prospects + sample messaging | Lead magnet — proves competence and exposes operational complexity |
| **Monthly retainer** | $3K–$5K/month | Ongoing list refreshes, messaging iteration, no carry-the-bag | Lower-friction conversion path for sample recipients not yet ready for full engagement |
| **Full Thresh engagement (flagship)** | $50K–$100K fixed-fee | All 7 deliverables including N meetings personally booked + full system handoff + runbook | The flagship offer; capacity-constrained to 1-2 simultaneous engagements |

Will update once first 1-3 deals close.

---

## Offer Evolution

Phase 2 (multi-signal, ongoing intelligence) and Phase 3 (continuous monitoring) deferred until Phase 1 is validated by 3-5 closed deployments.

---

## ICP Definition

### Firmographics

| Attribute | Criteria |
|-----------|----------|
| Company stage | Seed to Series B ($1M-$25M ARR) |
| Team size | 10-200 employees |
| Sales motion | Founder-led or small sales team (1-5 reps) |
| Category | Vertical SaaS, B2B services, or industrial technology |
| Buyer's industry | Must sell into regulated, licensed, or inspected industries where federal/state/local public data tracks their buyers' problems. Examples but not limited to: construction, fleet management, energy, commercial real estate, data centers, automotive, local services, fintech, healthcare facilities, manufacturing |
| Geography | US-based (federal databases are US-centric for now) |
| GTM maturity | Has a product, has some customers, doing outbound but results are mediocre. Maybe just got burned by another agency or AI-sdr who promise massive send volume but leads to shitty meetins or simply no results. Not pre-product. Not enterprise with a 20-person sales org. |

### Stage Model

Companies go through a predictable sequence from founder-led sales to outbound infrastructure. Thresh's sweet spot is **Stage 2**.

| Stage | ARR Range | Team Shape | What's Happening | Thresh Fit |
|-------|-----------|------------|-----------------|---------------|
| **0 — Founder-led** | $0-$250K | Founder is the sales team | Personal network, warm intros, occasional cold email from Gmail | Too early |
| **1 — First sales hire** | $250K-$1M | Founder + 1 SDR or AE | First outbound attempts, basic CRM, manual everything | Getting warm |
| **2 — Small team, no ops** | $1M-$5M | 2-8 reps, VP Sales just arrived, no ops person | Outbound exists but is manual and inconsistent. VP Sales is "doing it all" — strategy, hiring, prospecting, closing, AND building infrastructure. Reps spend ~33% of time actually selling. | **SWEET SPOT** |
| **3 — First ops hire** | $3M-$10M | Small/founding Sales team + first RevOps/Sales Ops person | CRM cleanup, reporting, pipeline management — but still no signal-based outbound or intelligence layer | Still good |
| **4 — GTM Engineer** | $10M+ | Proven GTM motion, 10+ tools | Decided to build in-house. Has named the problem. | Too late |

**Key data point:** Only 128 GTM Engineer job posts appeared in a 3-month window in 2025 — one for every 92 SDR positions. ~45% of those titled "GTM Engineer" are actually agencies/consultants. (Source: Kyle Poyar / Growth Unhinged)

### Observable Signals (how to find Stage 2 companies)

#### Tier 1 — Strongest leading indicators

1. **VP Sales / Head of Sales hired in last 6 months** — This person arrives, discovers there's no playbook, no ops support, no outbound infrastructure. They ARE the buyer. Detectable via LinkedIn job changes.
2. **First SDR/BDR posted or just hired** — Company committed to outbound but has zero systems to support it. The SDR is doing everything manually. Detectable via TheirStack, LinkedIn, job boards.
3. **Series A in last 90 days with "scale sales" or "go-to-market" in the press release** — Money + growth mandate + nothing built yet. Trigger-based outreach after funding yields 4x higher conversions. Detectable via Crunchbase, PredictLeads.

#### Tier 2 — Supporting signals

4. **"Outbound" buried in an AE job description** — No dedicated outbound function. AEs are expected to self-source leads.
5. **First RevOps/Sales Ops posting** — Manual processes just broke. They know something is wrong but are solving with headcount, not intelligence.
6. **Job posting mentions Clay/Apollo/Outreach as "nice to have"** — Exploring outbound tools, hasn't built systems yet.
7. **Recently adopted HubSpot or Salesforce** — Formalizing CRM = starting to think about process. (Detectable via BuiltWith, Wappalyzer.)


#### Tier 3 — Behavioral / harder to detect

8. **Founder still doing demos** — Visible on LinkedIn activity, Calendly links, conference speaking.
9. **Tried and abandoned an outbound agency or AI SDR tool** — Frustrated buyer, ready for a different approach. Sometimes visible in LinkedIn posts/comments. Spent 3–6 months and $30–80K on an AI SDR vendor (11x.ai, Artisan, AiSDR, Reggie, Air AI). Deliverability collapsed in week 4. Sales-domain reputation damaged. Cost-per-meeting blew from $35 to $150–300.
10. **Posting on LinkedIn/Reddit about outbound challenges** — Founders sharing struggles publicly.

### Qualifying Signals (how we know they're ready to buy)

| Signal | Why it matters |
|--------|---------------|
| Recently hired first SDR or AE | They're investing in outbound but don't have sophisticated targeting yet |
| Active Clay account | They've bought the tool but likely struggling to get value from it |
| Founder posting about outbound challenges on LinkedIn | Self-identified pain |
| Raised seed/Series A in last 12 months | Have budget, have growth pressure, likely founder-led sales |
| Selling into a compliance-heavy vertical | Their buyers have public data we can exploit |
| Currently using ZoomInfo/Apollo + generic sequences | Doing outbound the old way — high volume, low signal |

### The Information Asymmetry Test

Before taking any engagement, answer one question: **Does public data exist about their prospects' problems that their prospects don't know is being tracked?**

- If yes → green light. The signal creates genuine information asymmetry.
- If no → walk away. Without asymmetry, the messages are just better-written cold emails, not intelligence.

Examples that pass:
- Fleet carriers don't know their FMCSA driver OOS rate is visible and comparable
- Building owners don't know their ENERGY STAR score and LL97 penalty exposure are calculable from public data
- Data center operators don't know their cooling specs are publishable alongside GPU roadmaps
- Construction companies don't know their OSHA investigation history is cross-referenceable with their permit filings
- Auto dealerships don't know their warranty complaint patterns and FTC enforcement exposure are trackable from public filings
- Fintech companies don't know their prospects' state money transmitter license status and FinCEN registration gaps are public record

Examples that fail:
- SaaS companies selling to other SaaS companies — buyers are data-literate, no asymmetry
- Consumer brands selling DTC — no meaningful public compliance data on individual consumers
- Recruiting firms selling to tech companies — hiring data is already commoditized via LinkedIn

---

## Buyer Personas

### Persona 1: The Vertical SaaS Founder

**Title:** CEO / Co-Founder
**Company:** Seed to Series A vertical SaaS
**Team:** 5-30 people, likely no dedicated sales team yet
**Day-to-day:** Product, fundraising, and doing founder-led sales between everything else
**Quota pressure:** Needs to show pipeline and early revenue to raise next round

**Pain points (in their words):**
- "I know our ICP but I don't have time to build lists and personalize every email"
- "We bought Clay but I burned $500 in credits and still don't have a working workflow"
- "Our outbound sounds generic — we get 1-2% reply rates and most replies are 'not interested'"
- "I know there's public data about our buyers' problems but I don't know where to find it or how to use it"
- "I can't afford a $15K/month agency and I don't want to hire an SDR yet"

**What they actually need:** Someone to hand them a list of 100 companies experiencing the exact problem their product solves, with the evidence attached and the messages written. They send it. It books meetings.

**Trigger to buy:** They've tried generic outbound for 2-3 months and it's not working. They're about to either hire an SDR ($60K+ fully loaded) or pay an agency ($5-15K/month). The free 10-prospect sample lands at this exact moment and shows them a different way.

**Channel:** Email works if they're technical founders who live in their inbox. LinkedIn DM for founders active on the platform. Warm intro through Clay community, Primary Ventures network, or mutual connections is strongest.

### Persona 2: The Growth Lead at Mid-Market B2B

**Title:** Head of Growth / VP Sales / Revenue Operations
**Company:** Series A-B, $5-25M ARR
**Team:** 3-10 person sales team, possibly 1-2 SDRs already
**Day-to-day:** Pipeline targets, campaign management, reporting to CEO/CRO

**Pain points (in their words):**
- "Our SDRs are sending 200 emails a day and booking maybe 3 meetings a week"
- "We use the same intent data as every other company in our space — job postings, funding announcements, website visits. Nothing differentiates our outreach."
- "I need something that makes our outbound stand out because every inbox is flooded with AI-personalized garbage"
- "My CEO keeps asking why our reply rates are dropping and I don't have a good answer"

**What they actually need:** A signal source their competitors aren't using. Not more volume, not better copy — intelligence their reps can use that no competitor is sending. Thresh arms the existing team with data advantages, not replacement workflows.

**Trigger to buy:** Reply rates have dropped below 1%. CEO is questioning outbound spend. They've already tried switching email copy, subject lines, and sequencing cadences. The problem isn't the words — it's the targeting.

**Channel:** Email works. These buyers live in their inbox. LinkedIn content showing real examples (anonymized) gets their attention because they're actively looking for new approaches.

---

## Disqualifications

### Hard Disqualifications (immediate no)

| Signal | Why |
|--------|-----|
| Horizontal SaaS selling to tech buyers | No information asymmetry. Buyers are data-literate. Public compliance data doesn't exist for their market. |
| No public data about their buyers' problems | If the Information Asymmetry Test fails, the deliverable is just better-written cold email, not intelligence. Walk away. |
| "Experimental AI budget" | Client wants to "try AI outbound" without a clear ICP or sales motion. These engagements die after month 1. Revenue is not worth the time. |
| Pre-product / pre-revenue | They don't have something to sell yet. The signal-based list is useless without a product behind it. |
| Needs CRM management, inbox setup, SDR management, or sending infrastructure | That's not what Thresh does. Refer them to a Clay agency or ops consultant. |
| Burned sending domains / terrible deliverability and unwilling to fix it | If their emails go to spam, they'll blame the data. Qualifying question before engagement: "What's your current open rate and how many domains are you sending from?" If the answer is bad and they won't fix it, walk. |

### Soft Disqualifications (proceed with caution)

| Signal | Why | Mitigation |
|--------|-----|------------|
| Very small TAM (< 500 total companies in their market) | Signal-based approach may exhaust the market in 2-3 months. Short engagement lifespan. | Price as a one-time project, not a retainer. Or expand to adjacent verticals. |
| Blue collar buyers who don't check email | The messages are strong but the channel may not work for cold email specifically. | Frame deliverable as "messages" not "emails." Output works for call scripts, LinkedIn outreach, or direct mail. Discuss channel fit in the qualifying call. |
| Client wants guaranteed meeting counts | Thresh delivers intelligence and messages, not booked meetings. Too many variables between the list and the meeting (their rep quality, their sending infra, their follow-up speed). | Set expectations upfront: "I control the quality of the data and the messages. You control the execution. If the data is right and the messages are sharp, meetings follow — but I don't guarantee a number." |
| Large enterprise (500+ employees, complex procurement) | Long sales cycles, procurement review, legal review on data sourcing. Not worth it at $3-5K/month price point. | Only engage if there's a champion who can buy on a credit card or through a small consulting PO. Otherwise, pass until Thresh has case studies and higher pricing. |

### The 5-Minute Qualifying Checklist

Before any engagement, answer these five questions:

1. **Does public data exist about their buyers' problems?** (If no → hard stop)
2. **Do their buyers not already know this data is public?** (If buyers already track it → no asymmetry → hard stop)
3. **Is their sending infrastructure healthy?** (If burned domains and won't fix → hard stop)
4. **Do they have a sales motion that can act on the list?** (If no one is sending emails or making calls → too early)
5. **Can they pay either $3-5K/month for the retainer or $50-100K for the full Thresh engagement?** (If the budget isn't there → friendly no, revisit later)

If all five are yes, take the engagement. If any are no, either fix the blocker first or walk.

---

## System

- Deliverables built using gtm-alpha engine at `/projects/gtm-alpha`
- Run outputs: `gtm-alpha/runs/{domain}/`
- Data source registry: `gtm-alpha/contracts/data-source-registry.md`
- Outbound pipeline: `outbound/pipeline.md`
- Prospecting queries: `outbound/prospecting-queries.md`
