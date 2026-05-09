# thresh.md — Business Operating Document

**Last updated:** 2026-05-08

> **Status (2026-05-08):** Operating doc, evolving. Offer reframed around **Founding Cohort** — 3 vertical SaaS companies at founding rate ($20K flat / 90-day engagement). Carry-the-bag spans Weeks 4–7 of the 90-day engagement (Weeks 1–3 = setup + inbox warmup, Weeks 8–12 = transition + handoff). Service Guarantee + Anti-Guarantee combined. Payment terms: 50% upfront, 50% after first qualified reply. After cohort closes, rate moves to $30K and Service Guarantee comes off. Phase 0 outbound test active in trucking SaaS. Site (`runthresh.com`) updated 2026-05-08 to surface engagement shape, pricing, and guarantee. Reply-rate validation from Phase 0 will inform post-cohort pricing.

---

## What Thresh Is

Forward-Deployed GTM Engineering applied to outbound. A temporary builder who embeds inside a B2B company, deploys a custom signal-based outbound system, instruments it, documents it, and leaves it working in the team's hands. Similar (not exact) archetype as Palantir's FDEs, Vista's VCG, Alpine's CIT — applied to outbound rather than enterprise software or services rollups.

The work (still a WIP): find public-data pain signals, build target lists, write messages so valuable that the recipient would pay to receive (PVPs), launch the first campaigns, leave a working system the client owns.

Default engagement shape: 90-day deployment standard. 60-day variant available at separate pricing. Optional extension if both parties want to keep going.

---

## Current Direction (2026-05-07)

Active Phase 0 validation in **trucking SaaS** (single vertical inside the Logistics & Supply Chain meta-vertical). Messaging architecture sourced from a cross-corpus query of Blueprint (5,000+ plays) + GTM Alpha (122+ plays) — FMCSA-anchored signals dominate at ~87% of corpus messaging. Day 30 positive reply rate determines whether to scale send volume or rewrite the skeleton. Hazmat / reverse-logistics + waste-hauler verticals parked until trucking validates.

Strategic playbook + sequencing: `~/Documents/projects/second-brain-cli/Reference/Thresh Phase 0 Playbook.md`. Operational state: `outbound/pipeline.md`. Corpus refresh: `outbound/queries/trucking-saas-corpus.py`.

---

## Open Questions (for /cross-pollinate)

> **What this is.** Active questions and assumptions Thresh's plan rests on. The `/cross-pollinate` skill reads this section every time a new note is captured into second-brain and surfaces any capture that answers, contradicts, or adds evidence to one of these. Keep ≤10 entries. Drop questions when answered. Update weekly or on direction shifts.
>
> **Format per entry:** `Question | Currently assumed: X | Closes when: Y`

- **Q1 — Mode-switch trigger from signal-based to full-TAM coverage.** Phase 0 is signal-first (find the 3% with the right tension). Haren's 5-stage model says full-TAM coverage of the unaware 97% wins at 5M+/mo. Don't know what the actual switch trigger is. *Currently assumed:* signal-first until ~1M/mo, then revisit. *Closes when:* practitioner answer or Phase 0 reply-rate decay data shows diminishing returns on the 3%.
- **Q2 — Day 30 reply-rate threshold.** Phase 0 says Day 30 positive reply rate determines scale-vs-rewrite. *Currently assumed:* threshold not explicitly numbered. *Closes when:* a defensible benchmark for "Phase 0 is working" — likely tied to TAM size + offer difficulty per Nowoslawski's "1-in-2,000 can be a winner" framing.
- **Q3 — Which parked vertical to revive first if trucking validates.** Hazmat / reverse-logistics / waste-hauler all parked. *Currently assumed:* hazmat first (closest signal architecture to trucking). *Closes when:* trucking Day 60 result + comparison signal-asymmetry test across the three.
- **Q4 — Founding Cohort close rate.** Need to fill 3 spots at $20K founding rate. *Currently assumed:* 1-in-5 qualified conversations close. *Closes when:* actual outbound + warm-intro outcomes from first 10 conversations.
- **Q5 — Whether the Anti-Guarantee converts or scares off.** Combined Service Guarantee + Anti-Guarantee is unusual. *Currently assumed:* the combination filters for serious buyers without killing the top of funnel. *Closes when:* 5 disqualifications + 5 progressions through guarantee discussion in live conversations.
- **Q6 — Carry-the-bag offer reframe — does the prospect read it as "you're doing the work" or "you're a vendor"?** *Currently assumed:* framing as embedded operator (Vista VCG / Alpine CIT / Palantir FDE) lands as differentiated. *Closes when:* live reply data on the carry-the-bag-anchored sequence vs. control.
- **Q7 — Post-cohort pricing trajectory.** $20K founding → $30K standard. *Currently assumed:* $30K is defensible after Phase 0 validation + Service Guarantee removal. *Closes when:* cohort completion + first $30K conversation either converts or fails on price.

---

## Downstream Market Catalog

A living library of regulatory events, compliance deadlines, and public-data moments in the *buyer's* market that create outbound urgency for Thresh clients. This is separate from the Observable Signals list (which qualifies whether a SaaS company is ready to *buy* Thresh) — entries here qualify whether a SaaS company has a hot *opportunity* in their customer base that Thresh can package.

Each entry is reusable across every Thresh client selling into that vertical. The catalog is the productized layer of Thresh: the asset that compounds across engagements.

### Format

Every entry follows the same structure:

- **Vertical:** Which client market this applies to
- **Event / Signal:** The regulatory event or public-data moment
- **Date / Window:** When it triggers and when the signal decays
- **Why it matters:** What buying urgency this creates for Thresh's clients' prospects
- **Public data sources:** Where the data lives (APIs, bulk files, scraped portals)
- **Asymmetry test:** Whether the prospects know this data is being tracked
- **Reusable for clients selling to:** The downstream buyer types

---

### Entry 001 — FMCSA Motus Phase II Launch

- **Vertical:** Trucking SaaS / Logistics & Supply Chain
- **Event / Signal:** FMCSA Motus Phase II launch — replacement for the Unified Registration System (URS) and FMCSA Portal. Mandatory identity verification (IDEMIA / CLEAR) and mandatory business verification for every registrant on first access.
- **Date / Window:** URS retires May 14, 2026 at 8:00 PM ET. Motus Phase II launches week of May 18, 2026. Active signal window: May–August 2026. Decays Q3 2026 as discrepancies are resolved.
- **Peak / use-by:** Hottest 6 weeks are **May 14 – June 30, 2026**. Carriers failing business verification surface in the first 2-3 weeks post-launch. Outbound mentioning Motus is most credible while the deadline is still in the news cycle. By July, "we got flagged" buyers will have already started shopping fixes — late entry risks looking like the third vendor in the inbox.
- **Why it matters:** ~800,000 carriers, brokers, and freight forwarders must verify identity and business data against independent sources. Carriers with stale MCS-150s, multiple operating authorities, recent ownership changes, or officer mismatches will fail business verification — creating a second-wave buying need ("we got flagged, who can help us fix it"). FMCSA explicitly asked carriers to clean records before launch, which is rare and signals expected discrepancy volume. Forced action + deadline + verification gate + hidden data exposure = textbook signal moment.
- **Public data sources:**
  - QCMobile API (REST, free, requires WebKey via Login.gov) — registration, authority, insurance, inspection, crash data per DOT
  - MCMIS Data Dissemination — bulk files: 3 years inspections, 5 years crashes, full registration, compliance reviews, safety audits
  - SAFER Company Snapshot — per-DOT JSON lookup, no key required for basic use
  - SaferBus API — same data shape for passenger carriers
- **Asymmetry test:** Pass. Carriers do not know their MCS-150 staleness, ownership-officer mismatches, or authority-record discrepancies will surface during Motus business verification. Plaintiff-side litigation framing (Saxton & Stump) adds a second layer of asymmetry — carriers don't realize their FMCSA record is discovery material.
- **Reusable for clients selling to:** Motor carriers, freight forwarders, property brokers, fleet operators, BOC-3 process agents, transportation insurers, DOT compliance services, ELD providers, TMS platforms, driver qualification file (DQF) systems, transportation legal/consulting firms.

---

## The Offer

A 90-day deployment where Lucas embeds with a vertical SaaS company, builds a custom signal-based outbound system, **and personally runs sends, replies, meeting-booking, and cold calls during Weeks 4–7 before handing it off to the client's team during Weeks 8–12.** Weeks 1–3 are setup, infrastructure, inbox warmup, messaging finalization, and playbook lock with the client team. The wedge against PMM-led competitors (Slingshot, Blueprint) is the in-engagement work itself: Lucas sits the seat instead of shipping a system and walking. The client inherits a working production line *plus* the operating credibility of an ex-SDR/founding AE who actually ran the campaign before the handoff. Service Guarantee covers the carry-the-bag period (Lucas keeps working free until baseline reply rate hit, conditional on client meeting their obligations).

The 7-piece deliverable system (deliverable #5 is the in-engagement validation the other six support):

1. **Pain signal map** — 5+ validated signals showing "this prospect is bleeding right now"
2. **Data source registry** — 3-5 unique public data sources mapped to their vertical, with API/scrape playbooks
3. **Validated ICP** — live list of companies currently triggering the signals (proof the pipeline works)
4. **Messaging framework** — PVP and PQS style messages keyed to each signal, tested by Lucas in production (definitions and examples in *Messaging vocabulary* below)
5. **First campaign — Lucas personally runs sends, replies, meeting-booking, and cold calls during Weeks 4–7** (in-engagement validation — distinguishes Thresh from "we built a system, your team executes" competitors)
6. **Instrumented dashboard** — signal → enriched contact → message → response → meeting
7. **Runbook** — the operating manual the client's team uses to keep the system running after the 4-week handoff

### Messaging vocabulary

**PVP** = *Permissionless Value Prop.* A message so valuable that the prospect would pay to receive it even if they never buy from you.

**PQS** = *Pain-Qualified Segment.* A message that mirrors a prospect's specific pain back to them, identified through programmatic data. You describe their situation, not your product.

#### PVP example — Big Tex Trailers (bigtextrailers.com)

- **Industry:** Manufacturing
- **Data type:** Public data
- **Play name:** Maxwell Demo Contact with Equipment Need
- **What's the play:** Pull specific demolition permits showing contractors actively seeking 16K+ equipment, then provide complete contact information (name, email, phone) so the prospect can reach out immediately.
- **Why it works:** Pure PVP — you're giving them a qualified lead they can call RIGHT NOW. The permit filing date, project timeline, and contractor notes showing they're still sourcing equipment means this is an active, in-market opportunity. Complete contact info removes all friction to action.
- **Data sources:** Municipal Demolition Permit Databases — permit details, project timelines, contractor information, equipment requirements
- **Message:**

  > **Subject:** Maxwell Demo just filed for 16K equipment
  >
  > Maxwell Demolition (Jim Maxwell, jim@maxwelldemo.com, 214-555-0847) filed a permit March 3rd for a Richardson commercial demo requiring 16K+ dump trailers. Project starts April 15th and they're still sourcing equipment according to the contractor notes. Want me to intro you to Jim?

#### PQS example — LoanPro (loanpro.io)

- **Industry:** Financial services
- **Play name:** Enforcement Order + Growth Dual Pressure
- **What's the play:** Target community banks under active FDIC or OCC consent orders who are simultaneously experiencing significant loan portfolio growth (25%+ YoY). These banks face dual pressure: they must remediate compliance violations on legacy systems WHILE scaling operations to support rapid growth.
- **Why it works:** The nightmare scenario for a Lending Operations Director. Consent orders require enhanced controls and monthly reporting, which typically means months of manual system audits and process documentation. Most banks pause growth during remediation. Banks that DON'T pause are drowning — trying to build compliance on inflexible legacy platforms while volume accelerates rarely works. LoanPro's compliance-ready platform (SOC 2, GDPR, PCI, NACHA certified) with built-in compliance guardrails solves both problems simultaneously.
- **Data sources:**
  - FDIC Enforcement Decisions and Orders — searchable database of consent orders with specific corrective actions and timelines
  - OCC Enforcement Actions Search — public enforcement actions since 1989
  - FDIC BankFind API — quarterly call report data including loan portfolio totals (field: `total_loans`)
- **Message:**

  > **Subject:** Consent order + 28% growth
  >
  > Your FDIC consent order from March 2024 requires enhanced loan servicing controls and monthly compliance reporting, yet your loan portfolio grew 28% since then — you're building compliance systems while scaling operations simultaneously. Most banks pause growth during remediation, but you're doing both. What's the timeline on the consent order milestones?

### Pricing tiers

| Tier | Cost | Delivery | Purpose |
|---|---|---|---|
| **Tier 1: GTM Alpha Playbook** | $0 | Pain Signal Map for vertical + 3 PVPs + 5 named prospects | Lead magnet. Hand-built per vertical, limited weekly capacity. |
| **Tier 2: Signal Intelligence Retainer** | $3K–$5K/month | Monthly target list refresh, data pipe maintenance, messaging iteration, scored leads delivered to client team weekly. No carry-the-bag execution. | For sales orgs that already have an SDR seat. Lower-friction conversion path for sample recipients not yet ready for full engagement. |
| **Tier 3: Founding Cohort — 90-Day Build (FLAGSHIP)** | **$20K founding / $30K post-cohort** | All 7 deliverables. See Founding Cohort details + Guarantee below. | Flagship. **3-spot Founding Cohort.** Founding rate while spots remain. After cohort closes, rate moves to $30K and Service Guarantee comes off. Capacity: 1–2 simultaneous engagements. |

### Founding Cohort details

**Cohort size:** 3 vertical SaaS companies. Founding rate while spots remain. After cohort closes, rate moves to $30K and Service Guarantee comes off.

**Engagement timeline (90 days):**
- **48-hour kickoff:** Expanded Signal Map + 20 hyper-targeted prospects delivered the moment the contract signs
- **Weeks 1–3:** Setup — infrastructure, inbox warmup, messaging finalization, playbook lock with client team
- **Weeks 4–7:** Carry-the-bag — Lucas personally runs sends, replies, meeting-booking, cold calls
- **Weeks 8–12:** Transition — full handoff with permanent runbook

**Payment terms:** 50% upfront, 50% after first qualified reply hits the client's inbox.

### Guarantee

**Conditional Personal Service Guarantee:** If the client doesn't hit a baseline positive reply rate by the end of the 4-week sprint (Weeks 4–7), Lucas personally continues to run, test, and iterate the campaigns free of charge until they do — provided the client responds within 24 hours, approves messaging on time, and attends all onboarding calls.

**Anti-Guarantee on the build:** Because Lucas exposes the exact government data sources, prompt architecture, and messaging frameworks, all sales are final on the build itself. The Service Guarantee covers ongoing execution.

Will update once first 1–3 deals close.

---

## Offer Evolution

Phase 2 (multi-signal, ongoing intelligence) and Phase 3 (continuous monitoring) deferred until Phase 1 is validated by 3-5 closed deployments.

---

## ICP Definition

### Firmographics

| Attribute | Criteria |
|-----------|----------|
| Company stage | Seed to Series B ($1M-$25M ARR) |
| Team size | 1-100 employees |
| Sales motion | Founder-led or small sales team (1-5 reps) |
| Category | Vertical SaaS, fintech, healthcare, or industrial technology |
| Buyer's industry | Must sell into regulated, licensed, or inspected industries where federal/state/local public data tracks their buyers' problems. Examples but not limited to: construction, fleet management, energy, commercial real estate, data centers, automotive, local services, fintech, healthcare facilities, manufacturing |
| Geography | US-based (federal databases are US-centric for now) |
| GTM maturity | Has a product, has some customers, doing outbound but results are mediocre. Maybe just got burned by another agency who promise cold email, but they did massive spray and pray and the quality of meetings were terrible. Or an AI-SDR where they had massive send volume and didn't even get meetings booked. Not pre-product. Not enterprise with a 20-person sales org. |

### Stage Model

Companies go through a predictable sequence from founder-led sales to outbound infrastructure.

| Stage | ARR Range | Team Shape | What's Happening | Thresh Fit |
|-------|-----------|------------|-----------------|---------------|
| **0 — Founder-led** | $0-$1M | Founder is the sales team | Personal network, warm intros, occasional cold email from Gmail | Early — possible fit if showing PMF signs and treating this as message-market-fit work, not repeatable revenue |
| **1 — First sales hire** | $250K-$2M | Founder + 1 SDR or AE | First outbound attempts, basic CRM, manual everything | Getting warm |
| **2 — Small team, no ops** | $1M-$5M | 2-8 reps, VP Sales just arrived, no ops person | Outbound exists but is manual and inconsistent. VP Sales is "doing it all" — strategy, hiring, prospecting, closing, AND building infrastructure. Reps spend ~33% of time actually selling. | **SWEET SPOT** |
| **3 — First Ops/GTME hire** | $3M-$10M | Small/founding Sales team + hiring for their first RevOps/Sales Ops/GTME person | CRM cleanup, reporting, pipeline management — but still no signal-based outbound or intelligence layer | Still good |
| **4 — Scaling, hiring multiple roles across teams** | $10M+ | Proven GTM motion, 10+ tools | Decided to build in-house. Has named the problem. | Likely too late |

**Key data point:** Only 128 GTM Engineer job posts appeared in a 3-month window in 2025 — one for every 92 SDR positions. ~45% of those titled "GTM Engineer" are actually agencies/consultants. (Source: Kyle Poyar / Growth Unhinged)

### Observable Signal Ideas

1. **VP Sales / Head of Sales hired in last 6 months** — This person arrives, discovers there's no playbook, no ops support, no outbound infrastructure. They ARE the buyer. Detectable via LinkedIn job changes. They often are very focused on just closing, and usually don't have the best eye for what good emails look like.
2. **First SDR/BDR posted or just hired** — Company committed to outbound but has zero systems to support it. The SDR — likely a fresh college grad — is doing everything manually.
3. **AI SDR vendor adoption + 60–90 day vintage** — AI SDR adoption signal appears → company is in or approaching the 90-day deliverability kill curve → CMO/VP Sales sees sales-domain reputation deteriorating + cost-per-meeting blowing out → actively shopping replacement methodology that won't trigger the same failure mode → receptive to new ideas.
4. **Series A in last 90 days with "scale sales" or "go-to-market" in the press release** — Money + growth mandate + nothing built yet. Trigger-based outreach after funding yields 4x higher conversions. Investor demand for CAC efficiency forces attention on outbound; the vertical-specific public-data layer is the unbuilt opportunity.
5. **GTM Engineer job posting open >60 days at vertical SaaS** — Tried to build internal capability → labor market said no (hard to fill role due to ambiguity of the job and how new it is; 45% are agencies/consultants, not real in-house roles per Kyle Poyar / Growth Unhinged) → ready for outsourced methodology engagement. Angle: did you fill it? Most teams struggle. I'll support and document everything to hand off to your in-house hire when it happens.
6. **"Outbound" buried in an AE job description** — No dedicated outbound function. AEs are expected to self-source leads.
7. **First RevOps/Sales Ops posting** — Manual processes just broke. They know something is wrong but are solving with headcount, not intelligence.
8. **Job posting mentions Clay/Apollo/Outreach as "nice to have"** — Exploring outbound tools, hasn't built systems yet.
9. **Recently adopted HubSpot or Salesforce** — Formalizing CRM = starting to think about process. (Detectable via BuiltWith, Wappalyzer.)
10. **Founder still doing demos** — Visible on LinkedIn activity, Calendly links, conference speaking.
11. **Tried and abandoned an outbound agency or AI SDR tool** — Frustrated buyer, ready for a different approach. Sometimes visible in LinkedIn posts/comments. Spent 3–6 months and $30–80K on an AI SDR vendor (11x.ai, Artisan, AiSDR, Reggie, Air AI). Deliverability collapsed in week 4. Sales-domain reputation damaged. Cost-per-meeting blew from $35 to $150–300.
12. **Posting on LinkedIn/Reddit about outbound challenges** — Founders sharing struggles publicly.
13. **Paying for Clay/Apollo/ZoomInfo but underutilizing it** — Bought the tool, burned credits without a working workflow, now sitting on a sunk cost they want to justify. Buying objection isn't "do we need outbound infra?" — it's "how do we get value from what we already pay for?" Lower friction to a yes because you're not asking them to add a line item; you're helping them maximize the one they already own.
14. **Generic, volume-driven outbound sequences from ZoomInfo + Apollo + the same intent data as everyone else** — High-volume, low-signal motion. Reply rates degrading. Ready to hear about a different approach because the current one is visibly failing in their own dashboards.

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

Examples more likely to fail:
- SaaS companies selling to other SaaS companies (horizontal SaaS) — buyers are data-literate, no asymmetry
- Consumer brands selling DTC — no meaningful public compliance data on individual consumers
- Recruiting firms selling to tech companies — hiring data is already commoditized via LinkedIn

---

## Buyer Personas

### Persona 1: Founder / CEO at Earlier-Stage Vertical SaaS

**Title:** CEO / Co-Founder
**Company:** Seed to Series A vertical SaaS
**Team:** 5-30 people, likely no dedicated sales team yet
**Day-to-day:** Product, fundraising, and doing founder-led sales between everything else. Founder-led GTM transitioning to scaled motion. Hiring a VP Sales soon (or just hired). Has not yet built outbound infrastructure beyond manual SDR work + Apollo/Clay. Ideally listens to Crawford / Pavilion / GTMnow.
**Quota pressure:** Needs to show pipeline and early revenue to raise next round

**What keeps them up at night:** "I want to get outbound right from the start of our scaled motion — not waste 12 months fighting it. Jordan's (anti-AI-SDR) methodology resonates with how I think about our buyer. I need to fundraise in 9 months, and that depends on outbound working."

**Pain points (in their words):**
- "I know our ICP but I don't have time to build lists and personalize every email. But I also don't really trust anyone else to do it because they don't know my ICP as well as me"
- "We bought Clay but I burned $500 in credits and still don't have a working workflow"
- "Our outbound sounds generic — we get terrible reply rates and most replies are 'not interested'"
- "I know there's public data about our buyers' problems but I don't know where to find it or how to use it"
- "I can't afford a $15K/month agency and I don't want to hire an SDR yet"

**What they actually need:** Someone to take all the unique insights the founder has in their brain and translate it to outbound campaigns that actually win. Done via interviews, call recordings, CRM analysis, and deeply researching the market. Someone to build a list of X companies experiencing the exact problem their product solves, with the evidence attached and the messages written. They send it on behalf of the founder in DFY or DWY. It books meetings. Document everything and hand it off to their next hires.

**Trigger to buy:** They've tried generic outbound for 2-3 months and it's not working. They're about to either hire an SDR/Founding Growth ($100K+ fully loaded), pay an agency ($5-15K/month), or buy an AI-SDR. That's if they haven't already been burned by any of those options.

### Persona 2: The Growth/Marketing/Sales Lead at Vertical SaaS

**Title:** CMO, VP Marketing, Head of Marketing, or Marketing Operations lead at vertical B2B SaaS
**Company:** Series A, $1-5M ARR
**Team:** 3-5 person GTM team, possibly 1-2 SDRs already
**Day-to-day:** Pipeline targets, campaign management, reporting to CEO. Owns demand gen + marketing-sourced pipeline. Often co-owns outbound strategy with VP Sales. Champion / co-buyer rather than sole authority. Has visibility into reply-rate / open-rate / pipeline-source attribution. Ideally has been consuming Crawford-circuit content — podcasts (Pavilion, Outbound Kitchen, GTMnow, Mutiny), Cannonball GTM newsletter, or Crawford's LinkedIn.

**What keeps them up at night:** "I'm tired of justifying outbound spend to the CEO with the same dashboard that says reply rates are dropping. I know there's a better way — I see Jordan's stuff every week — but I don't have someone on my team who can build what he describes. Hiring a GTM Engineer takes 6 months and they cost $200K."

**Pain points (in their words):**
- "Our SDRs are sending 200 emails a day and booking maybe 3 meetings a week, and most aren't even qualified"
- "We use the same intent data as every other company in our space — job postings, funding announcements, website visits. Nothing differentiates our outreach."
- "I need something that makes our outbound stand out because every inbox is flooded with AI-personalized garbage"
- "My CEO keeps asking why our reply rates are dropping and I don't have a good answer"

**What they actually need:** A signal source their competitors aren't using. Better copy — intelligence their reps can use that no competitor is sending. Not more volume.

**Trigger to buy:** Reply rates have dropped below 1%. CEO is questioning outbound spend. They've already tried switching email copy, subject lines, and sequencing cadences. The problem isn't just the words — it's the targeting.

**Channel:** Email works. These buyers live in their inbox. LinkedIn content showing real examples (anonymized) gets their attention because they're actively looking for new approaches.

### Persona 3: The VP Sales / VP Revenue at Vertical SaaS

**Title:** VP Sales, VP Revenue, or Head of Sales at vertical B2B SaaS
**Company:** Series A, $1-5M ARR
**Team:** 3-5 person GTM team, possibly 1-2 SDRs already
**Day-to-day:** Owns the revenue number. Manages SDR + AE team. Reports to CEO weekly on pipeline. Owns outbound budget. Authority to sign $60K/year vendor contracts with minimal procurement review. Inherited an outbound motion that's breaking at current scale OR was hired to fix it.

**What keeps them up at night:** Not hitting revenue numbers. Hiring the wrong people. Making the wrong budget decisions.

**Pain points (in their words):**
- "Our outbound used to work and I don't know exactly why it stopped. I tried hiring more SDRs — it made it worse."
- "I tried an AI SDR vendor — they killed our domain reputation."
- "The CEO keeps asking when we'll see lift, and I'm running out of plausible answers. If I can't show pipeline lift in the next 90 days, my job is at risk"

**What they actually need:** A solution that solves their outbound. Specificity (does this person understand my buyer's vertical?). Methodology depth (do they have a system, or just better-written emails?). Speed-to-value (will I see lift in 30/60/90 days?). Documented receipts (case studies with named customer + named metric). Risk asymmetry ($60K/year << failed AI SDR contract loss + lost pipeline + trust damage).

**Trigger to buy:** Either (a) a board or PE quarterly checkpoint is 30–60 days out and current outbound can't produce the pipeline coverage the deck needs, OR (b) they're in their first 60–120 days in the VP Sales seat, have diagnosed outbound as the broken layer, and need to ship a visible methodology change before the honeymoon ends. In both cases the existing tooling stack (Clay/Apollo/ZoomInfo, possibly a failed AI SDR contract) is already paid for — what's missing is the signal layer underneath it. Decision happens in days, not quarters, because the calendar is the forcing function.

Persona 2 and Persona 3 often appear at the same account; CMO is typically the champion, VP Sales is typically the budget-holder.

---

## Disqualifications

### Hard Disqualifications (immediate no)

| Signal | Why |
|--------|-----|
| Horizontal SaaS selling to tech buyers | No information asymmetry. Buyers are data-literate. Public compliance data doesn't exist for their market. |
| No public data about their buyers' problems | If the Information Asymmetry Test fails, the deliverable is just better-written cold email, not intelligence. Walk away. |
| "Experimental AI budget" | Client wants to "try AI outbound" without a clear ICP or sales motion. These engagements die after month 1. Revenue is not worth the time. |
| Pre-product / pre-revenue | They don't have something to sell yet. The signal-based list is useless without a product behind it. |
| Burned sending domains / terrible deliverability and unwilling to fix it | If their emails go to spam, they'll blame the data. Qualifying question before engagement: "What's your current open rate and how many domains are you sending from?" If the answer is bad and they won't fix it, walk. |

### Soft Disqualifications (proceed with caution)

| Signal | Why | Mitigation |
|--------|-----|------------|
| Very small TAM (< 500 total companies in their market) | Signal-based approach may exhaust the market in 2-3 months. Short engagement lifespan. | Price as a one-time project, not a retainer. Or expand to adjacent verticals. |
| Blue collar buyers who don't check email | The messages are strong but the channel may not work for cold email specifically. | Frame deliverable as "messages" not "emails." Output works for call scripts, LinkedIn outreach, or direct mail. Discuss channel fit in the qualifying call. |
| Client wants guaranteed meeting counts | Even though Lucas runs the campaign personally for 4 weeks (Weeks 4–7), too many variables sit outside his control (their market depth, list quality after audience filters, deliverability state, what happens on the call). The Service Guarantee covers continued execution if baseline reply rate isn't hit, but does not promise specific meeting counts. | Point them at the Service Guarantee: "I keep working free until your team is getting positive replies — that's the commitment. Specific meeting counts depend on your market and your team's continuation after handoff." If they still demand a meeting number, walk. |
| Large enterprise (500+ employees, complex procurement) | Long sales cycles, procurement review, and legal review on data sourcing eat the engagement margin. $20K founding (or $30K post-cohort) is still too low to absorb enterprise procurement timelines. | Only engage if there's a champion who can buy on a credit card or through a small consulting PO. Otherwise, pass until Thresh has case studies that justify enterprise-tier pricing. |

### The 5-Minute Qualifying Checklist

Before any engagement, answer these four questions:

1. **Does public data exist about their buyers' problems?** (If no → pause)
2. **Is their sending infrastructure healthy?** (If burned domains and won't fix → pause)
3. **Do they have a sales motion that can act on the list?** (If no one is sending emails or making calls → it's early; manage expectations and cost if you're gonna do it all)
4. **Can they pay either $3–5K/month for the Signal Intelligence Retainer or $20K founding (Founding Cohort) / $30K (post-cohort) for the full 90-day Thresh engagement?** (If the budget isn't there → friendly no, revisit later)

If all four are yes, take the engagement. If any are no, either fix the blocker first or walk.

---

## System

- Deliverables built using gtm-alpha engine at `/projects/gtm-alpha`
- Run outputs: `gtm-alpha/runs/{domain}/`
- Data source registry: `gtm-alpha/contracts/data-source-registry.md`
- Outbound pipeline: `outbound/pipeline.md`
- Prospecting queries: `outbound/prospecting-queries.md`
