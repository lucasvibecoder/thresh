# What's the Thresh Version of the TAM to Target Playbook?

**Date:** 2026-05-06
**Purpose:** Answer the strategic question raised by reading TAM to Target's positioning side-by-side with Thresh's. Map the public-data substrates worth mining, identify the "Starbridge of X" SaaS aggregators behind each, and test two strategic shapes — TTT-clone (one vertical) vs. partner-of-many-vertical-SaaS.
**Status:** Decision made — see banner below.

> **Decision (2026-05-07):** Phase 0 = single-vertical trucking SaaS test. Messaging architecture sourced from cross-corpus Blueprint + GTM Alpha query (FMCSA-anchored signals dominate at ~87%). Day-30 positive reply rate determines whether to scale send volume or rewrite the skeleton; hazmat / reverse-logistics + waste-hauler verticals parked until trucking validates. The TTT-clone vs. partner-of-many decision is *deferred*, not closed — Phase 0 is run as a TTT-clone shape in trucking; partner-of-many remains an option for Phase 1+. Operating doc: `thresh.md`. Operational state: `outbound/pipeline.md`.

---

## TL;DR

> ⚠️ **2026-05-06 update**: data correction in Section 3.6 supersedes the substrate ranking in bullet #4 below. The Section 3.5 "construction + ag + food/FDA top-3" claim is correct for the 9 vendors it evaluated, but **does not hold across all 26 vendors**. Top vendors when sorted by full corpus: Stuut.ai (Financial, 4.04), HiBob (HR, 3.89), Samsara (Logistics, 3.86). Financial Services and HR & Recruiting were undersold in this doc. Also: the partnership-first frame underlying bullets 2-3 was set aside in the same conversation — see Section 3.6 "Implications" for substrate-first reframe.

1. **TTT's moat is a three-leg stool**: vertical operator credibility (Bobby Offterdinger = ex-K-12 teacher) + a category-defining data SaaS partner (Starbridge, $42M Series A) + an in-house execution layer running campaigns on top.
2. **Across 14 substrates evaluated, only 3 verticals have a partnership-ready Starbridge-equivalent + high-quality public-data signals**: building permits (Shovels.ai), FDA enforcement (Redica Systems), and ag/USDA (FarmRaise). Insurance, workers' comp, OSHA, and CRE energy are whitespace — no SaaS aggregator to partner with.
3. **The top 3 partnership candidates** — Shovels.ai (Seed, $5M), Redica Systems (Series B, $30M), FarmRaise (YC W21 Seed) — share a shape: small enough to want growth velocity, no in-house outbound army, no existing TTT-style execution partner. **Defense (Usul) ruled out** — relationship gravity + military-background preference Lucas doesn't have; partnership shape inherits the same problem.
4. **gtm-alpha signal grades validate the choice.** Construction procurement (3.83), ag (3.72), and food/FDA (3.69) are the top-3 substrates by composite signal score across runs. Healthcare (3.41) underperformed — Trilliant Health drops off the top list. See Section 3.5. ⚠️ *See 3.6 for full-corpus correction.*
5. **Two strategic shapes pass scrutiny**: (A) TTT-clone — pick one vertical, claim it, build deep. (B) Partner-of-many — non-exclusive partnerships across 3-5 vertical data SaaS, leveraging Lucas's *Clay Labs operator* credibility (horizontal) instead of vertical operator credibility (which he doesn't have). Runway favors partner-of-many; TTT-clone has higher long-term ceiling if the vertical sticks.

---

## 1. The TTT Playbook, Decomposed

A structural rubric of what makes TAM to Target work. Every alternative we evaluate gets scored against these legs.

| Leg | What TTT has | Why it matters |
|---|---|---|
| **Vertical scope** | Single finite market (K-12) → adjacent expansion (higher ed, state/local gov) | Finite TAM = fewer wasted touches; adjacency = growth without restart |
| **Operator credibility** | Bobby Offterdinger, "Recovering 5th Grade Teacher" → CEO. Knows the K-12 buyer's mental model from inside the building | Buyer trusts before he opens his mouth. Cannot be faked or rented. |
| **Data layer** | Starbridge — $42M Series A, public-sector intelligence platform (RFPs, board meetings, contracts, budgets). Publicly credited, not owned | Provides the unfair list. Without it, agency is generic SDR shop. |
| **Execution layer** | In-house SDR team (Halle Rice, Trevor Deans, Nick Haddad, Glenn M.). Coaching-led management. | Where revenue gets booked. Also where margin lives. |
| **Content engine** | Vertical-specific thought leadership (FAQ posts, "5 steps to pipeline in finite markets", LinkedIn frameworks) | Compounds inbound + builds operator credibility publicly |
| **Buyer-network effect** | K-12 admins talk to each other; vendors share what works | Referral velocity inside finite markets is the multiplier |
| **Pricing model** | $8-9k/mo per SDR seat, bundled tools + management; 2-3 wk onboarding | Anchored as labor replacement, not consulting hour |
| **Moat ranking** | Operator credibility > data layer > execution coaching > content | Vertical credibility is the leg hardest to copy |

**Key insight:** the data layer (Starbridge) is the most visible leg, but **operator credibility** is the moat. A competitor could license Starbridge tomorrow; they couldn't manufacture Bobby's K-12 teacher background. This matters for how we evaluate alternatives.

---

## 2. Substrate Inventory

What public-data substrates Thresh has touched (or could plausibly mine) across runs and the data-source registry.

| Substrate | Vertical | Run-evidence | Tier |
|---|---|---|---|
| FMCSA / SAFER + drug/alcohol clearinghouse | Trucking | DoubleNickel, Tank Payments, Truckstop runs | 3 |
| EPA + ECHO permits | Waste, environmental | Hauler Hero | 3 |
| OSHA citations | Workplace safety, construction, waste | Stratus, USEKojo | 3 |
| NPI registry, CMS, OIG exclusions | Healthcare | Charta Health, PointClickCare | 3 |
| FDA warning letters / FSMA / FTC enforcement | Food, supplements, pharma | LightLabs (live thread) | 3 |
| NAIC / state DOI complaints / NMLS | Insurance, fintech | CoverForce | 3 |
| Contractor licenses, bonding | Construction, MEP | Stratus, USEKojo | 3 |
| SAM.gov, FedBizOpps, DoD awards | Defense, federal contracting | Usul (intro call 3/6) | 3 |
| Building permits (DOB, state) | Construction, solar, home services | Mentioned, not run | 3 |
| ENERGY STAR + LL97 (NYC) | Commercial real estate, energy | 277 Park Ave hero example | 3 |
| USDA / EQIP / REAP | Agriculture | Ambrook (showcase) | 3 |
| Workers' comp / NCCI / EMR ratings | Cross-vertical (construction, manufacturing) | Helpside (Tier 2 flag) | 3 |
| Job postings (vertical-filtered) | Cross-vertical | Used as supporting signal across most runs | 1 |
| SEC EDGAR full-text + 8-K filings | Mid-market industrials, financial services | Stuut.ai | 3 *(promoted from 2 — see 3.6)* |

**Substrates Lucas hasn't yet worked but could:** SBIR awards, Federal Register comment proceedings, state pharmacy board actions, USPTO patent issuance velocity, FCC broadband filings, FAA Part 135 operator rosters, DOE LIHEAP/weatherization data, state cannabis license registries.

---

## 3. Starbridge-of-X Landscape (Scored)

For each substrate, we asked: is there a SaaS aggregator that has packaged this data, sells it to teams selling INTO the vertical, and has a partnership-shaped surface area (not yet locked up by enterprise sales orgs or PE rollups)?

**Score (1-5)**: 5 = high partnership viability (well-funded, no in-house outbound, no existing TTT-style partner, founders look operator-friendly). 1 = low (public co, locked partnerships, or wrong shape entirely).

| Substrate | Top Aggregator | Stage | Founders | Score | Notes |
|---|---|---|---|---|---|
| Building permits | **Shovels.ai** | Seed $5M (Jun 2025, Base10) | Ryan Buckley, Luka Kacil (YC alums) | **5** | Engineering-led, no SDR team, exact Starbridge clone for construction |
| FDA enforcement | **Redica Systems** | Series B $30M ($43.5M total, Dec 2021 Savant Growth) | Michael de la Torre | **5** | FDA warning letters + 483s + FOIA; sells to QA/regulatory in pharma + food |
| Federal contracting | **HigherGov** | Bootstrapped | Justin Siken (solo) | **5** | SAM.gov + contracts + grants + agency budgets; growing, no execution arm |
| Defense / DoD | **Usul** | Seed $3.3M (YC S24, Scout Ventures) | Jarren Reid, Joonghyun Lee, Oliver Gomez | **5** | "PitchBook for Government" — DoD market sizing, decision-maker mapping. **Lucas already had an intro call 3/6.** |
| Federal contracting (SMB) | FedScout | $1.13M total (Federal Foundry) | Geoff Orazem | 4 | Capital-constrained, small but operator-led |
| FMCSA / trucking | CarrierOK | Bootstrapped, undisclosed | Not surfaced | 4 | Right ICP — sells FMCSA risk into broker/insurer/factoring buyers |
| FMCSA / trucking | CarrierSource | Seed $800K | Not surfaced | 4 | Underfunded; equity/rev-share play possible |
| Healthcare commercial | Trilliant Health | Series A $12.7M (Jul 2021) | Hal Andrews | 4 | Scaling 40→100; no visible execution partner |
| SNF / Five-Star | StarPRO | Bootstrapped (2-10 ppl) | Colleen (founder) | 4 | Right buyer-direction, but small ARR ceiling near-term |
| Agriculture / USDA | FarmRaise | Seed (YC W21) | Jayce Hafner, Sami Tellatin | 4 | Closest functional ag match; aggregates EQIP/REAP data; Syngenta partnership exists |
| Federal contracting | Govly | Series A $9.5M (2023, Insight Partners) | Mike Weiland, Nick Weiland, Jon Wright | 3 | Channel-partner network model partially substitutes for outbound |
| FMCSA / trucking | Highway | Strategic growth equity (FTV Capital, Aug 2025) | Jordan Graft (ex-TriumphPay) | 3 | Well-funded with commercial muscle; partnership wedge narrower |
| Healthcare workforce | Revelio Labs | Series A $15M ($19.5M total, 2022) | Ben Zweig, Yedidya Gorsetman | 3 | Buyer base is alt-data/finance, not "vendors selling INTO hiring cos" |
| FMCSA / trucking | RigDig BI / FleetSeek | Owned by Fusable (PE) | Corporate carve-out | 1 | Mature PE-backed division |
| Healthcare | Definitive Healthcare | Public (NASDAQ: DH) | Jason Krantz | 1 | Public co; partnership irrelevant |
| Healthcare | Komodo Health | Series E $200M | Arif Nathoo, Web Sun | 2 | Late-stage, enterprise pharma sales already built |
| Healthcare | H1 | $381M total | Ariel Katz, Ian Sax | 2 | Acquired Veda + Ribbon; full GTM org |
| Food / FDA | TraceGains | Acquired by Veralto $350M (2024) | Gary Nowacki | 1 | Off the table |
| Food / FDA | Trustwell | PE-owned (Riverside → TPG) | n/a | 2 | PE rollup with installed GTM |
| Insurance | Verikai | Acquired by AFG (Dec 2021) | — | 1 | Off-market |
| Insurance | Cape Analytics | Acquired by Moody's (Jan 2025) | — | 1 | Off-market |
| Permits (legacy) | BuildZoom | $19.6M total (no recent round) | David Petersen, Jiyan Wei | 2 | Mature, dual consumer/B2B focus |
| Energy / LL97 | Runwise | Series B $55M (Jun 2025, Menlo) | Jeff Carleton, Lee Hoffman, Michael Cook | 2 | Sells the solution to building owners, not the data layer |
| Workers' comp | Foresight (Safesite) | Series B $39M ($59M total, 2022 OMERS) | David Fontain, Peter Grant, Leigh Appel | 2 | Insurance MGA, not data-SaaS partner |

**Whitespace verticals (no Starbridge-equivalent exists):**
- **OSHA / contractor safety** — dominated by prequal platforms (Avetta, Veriforce, ISNetworld) that sell TO contractors/owners, not to vendors selling INTO them. Wrong ontology.
- **NYC LL97 / ENERGY STAR** — every well-funded player (Runwise, Logical Buildings, BlocPower) is a solution provider, not a data layer.
- **Insurance / NAIC** — incumbents acquired (Verikai, Cape) or untouchable (S&P, Moody's). No fundable independent aggregator visible.
- **Workers' comp / NCCI** — NCCI controls EMR data licensing; downstream players (Origami Risk, Riskonnect) consume it but don't aggregate-and-resell to vendor outbound teams.

These four whitespace verticals are interesting in a *different* way: if Thresh wants to **build** the data layer (rather than partner), these are the substrates without an incumbent to dislodge. That's the original Thresh vision (per `research/09-why-thresh-is-different.md`, "Productize the signal layer — make the data accessible as a platform"). It's a 12-24 month build, not a 30-day partnership.

---

## 3.5 Signal Quality by Vertical (from gtm-alpha runs)

The Starbridge-of-X landscape tells us *whether a partnership is shaped right*. The signal-quality grades from prior gtm-alpha runs tell us *whether the public-data substrate yields workable plays at all*. Two different lenses; both matter.

Each gtm-alpha run scores 6-9 candidate signals on five dimensions (Volume, Detectability, Specificity, Timing Precision, Actionability) → composite 1-5. Below 2.5 = killed. The composite tells us how *workable* the public-data substrate is for that vertical's buyers, independent of any one company's fit.

**Average composite per vertical run** (higher = more workable substrate):

| Vertical | Run | Signals scored | Avg composite | Max signal | Signal that scored max |
|---|---|---|---|---|---|
| Construction procurement | usekojo.com | 7 | **3.83** | 4.35 | PE Acquisition of Trade Contractor |
| Ag / USDA | ambrook.com | 9 | **3.72** | 4.30 | Active USDA conservation contract holder |
| Food / FDA | lightlabs.com | 9 | **3.69** | 4.60 | Brand contamination incident |
| Trucking CDL | getdoublenickel.com | 8 | 3.64 | 4.35 | Driver Recruiter Job Posting |
| Defense | usul.com | 9 | 3.58 | 4.15 | Contract Recompete Approaching |
| Insurance | coverforce.com | 6 | 3.49 | 4.00 | Commercial Lines CSR Hiring Surge |
| MEP / Construction | stratus.build | 9 | 3.48 | 4.25 | Data-Center Experience Job Posting |
| Healthcare | chartahealth.com | 9 | 3.41 | 3.95 | Medical Coder / Biller Job Posting Surge |
| Trucking fintech | tankpayments.com | 9 | 3.32 | 4.00 | Broker on FMCSA Suspension List |

**What this changes vs. the partnership-only landscape:**

1. **Construction procurement + ag + food/FDA = the three top-quality substrates.** Maps cleanly to **Shovels.ai (construction), FarmRaise (ag), Redica Systems (FDA)** — three of our top partnership candidates. The two lenses converge.

2. **Healthcare underperformed (3.41 avg).** Charta's strongest signals are firmographic (PE acquisitions, coder hiring) — workable but not the third-order regulatory plays Thresh's moat depends on. **Trilliant Health drops off the top list** despite being a partnership-shaped target. The substrate quality didn't validate.

3. **Defense (3.58) is mid-pack** — the substrate is workable but not exceptional. Combined with the Usul fit issues Lucas surfaced (relationship-gravity + military-background preference), **defense is doubly de-prioritized** — even HigherGov / FedScout inherit the same industry-relational gravity.

4. **Insurance (3.49) was workable on paper** — Lucas's CoverForce signals scored mid-pack — but the SaaS landscape is dead-end (Verikai/Cape acquired). Vertical with workable signals + no partnership target = candidate for the *whitespace build* play if/when Thresh wants to own a data layer.

5. **MEP/Stratus (3.48) and trucking fintech (3.32)** scored at the bottom. These verticals are weaker substrates *or* the specific run targets had problematic signal sets. Either way, not first picks.

**Interpretation rule:** When partnership shape AND signal-quality both rank a vertical in the top tier, that's a strong combined signal. When they diverge (e.g., Trilliant Health is a fine partnership target but healthcare signals scored low), defer to the signal grades — the substrate quality is the bottleneck, not the partnership shape.

---

## 3.6 Data correction — full 26-vendor signal ranking (added 2026-05-06)

**Why this section exists:** Section 3.5 above used 9 of 26 vendors, selected for vertical-narrative coverage (one example per vertical the doc was evaluating), not by score. When the full 26-vendor corpus is sorted by avg `composite_score`, the ranking shifts in load-bearing ways. The Section 3.5 table is correct for the 9 vendors it includes, but it is *not* a representative ranking of the substrates.

### Top 10 vendors by avg composite score (5-pt scale, all 26 ranked)

| Rank | Vendor | Industry | Signals | Avg | Max |
|---|---|---|---|---|---|
| 1 | **Stuut.ai** | Financial Services | 7 | **4.04** | 4.60 |
| 2 | **HiBob** | HR & Recruiting | 11 | 3.89 | 4.55 |
| 3 | Samsara | Logistics & Supply Chain | 9 | 3.86 | 4.35 |
| 4 | Kojo | Construction & Trades | 7 | 3.83 | 4.35 |
| 5 | Taxwire | Financial Services | 8 | 3.82 | 4.20 |
| 6 | Helpside | HR & Recruiting | 9 | 3.81 | 4.40 |
| 7 | PointClickCare | Healthcare | 9 | 3.79 | 4.65 |
| 8 | Truckstop | Logistics & Supply Chain | 8 | 3.77 | 4.50 |
| 9 | Ambrook | Agriculture (tagged "Other") | 9 | 3.72 | 4.30 |
| 10 | Hauler Hero | Logistics & Supply Chain | 9 | 3.70 | 4.00 |

### Industry-level (avg of vendor avgs, all 12 industries ranked)

| Industry | Vendors | Avg | Top vendor |
|---|---|---|---|
| **Financial Services** | 3 | **3.77** | Stuut.ai (4.04) |
| Agriculture (tagged "Other") | 1 | 3.72 | Ambrook |
| Food & Hospitality (FDA) | 1 | 3.69 | Light Labs |
| Logistics & Supply Chain | 5 | 3.66 | Samsara (3.86) |
| Technology & SaaS | 2 | 3.65 | Reflex (3.67) |
| **HR & Recruiting** | 3 | **3.62** | HiBob (3.89) |
| Healthcare | 2 | 3.60 | PointClickCare (3.79) |
| Construction & Trades | 5 | 3.60 | Kojo (3.83) |
| Government | 1 | 3.58 | Usul |
| Energy & Utilities | 1 | 3.54 | Trane |
| Insurance | 1 | 3.49 | CoverForce |
| Marketing & AdTech | 1 | 3.37 | Ryze AI |

### What changes vs. Section 3.5

1. **Stuut.ai is the highest-scoring vendor in the entire corpus.** SEC EDGAR + 8-K filings substrate (tagged Tier 2 in Section 2) outperforms every other vendor and was excluded from the 3.5 analysis. Tier rating should be promoted to Tier 3.
2. **Financial Services is the strongest industry cluster.** 3 vendors averaging 3.77. The doc's Section 3 (Starbridge-of-X landscape) evaluates zero Financial Services / SEC-EDGAR aggregator candidates — entire substrate is missing from partnership analysis.
3. **HR & Recruiting is the surprise top-tier substrate.** HiBob is the #2 vendor overall; Helpside #6. The substrate scored 3.62 industry avg with 3 vendors — comparable to ag (1 vendor) and food/FDA (1 vendor) on quality, with broader evidence base.
4. **Construction & Trades drops to mid-pack at industry level.** Kojo at 3.83 is fine but Wold (3.66), Bobyard (3.53), Fieldwire (3.51), Stratus (3.48) drag the average to 3.60 — tied with Healthcare, below Logistics, HR, and Tech. The "construction is top-3" framing held for Kojo specifically; not for the substrate broadly.

### Why the original analysis missed this — three compounding biases

1. **Tier rating in Section 2 used run count, not signal quality.** Stuut got Tier 2 (1 run) while Light Labs (also 1 run) got Tier 3. The criterion was never explicit — likely vibes-based.
2. **Section 3.5 vendor selection was driven by vertical coverage**, not score. The strongest vendors (Stuut, HiBob, Helpside, Taxwire, Truckstop) were excluded from the headline table.
3. **Section 3 (partnership candidates) filtered out substrates without obvious aggregator-shape partners.** Financial-data and HR-data are dominated by big incumbents (LinkedIn, S&P, Moody's, ZoomInfo) — no fundable independent aggregator. Once the partnership-first frame is dropped (per the 2026-05-06 conversation), both substrates re-enter contention as direct-outbound or build-the-data-layer candidates.

### Implications for Section 5 (strategic shapes)

The "TTT-clone vs. partner-of-many" decision frame holds, but the candidate set widens:

- **Financial / SEC EDGAR (via Stuut artifact)** — top substrate, no Starbridge-equivalent partner. Either direct-outbound to financial-data customers, or whitespace build (Thresh becomes the data layer).
- **HR & Recruiting (via HiBob artifact)** — #2 vendor, most thoroughly developed run (10 plays, conviction-scored). Strong substrate, no obvious partnership shape. Direct-outbound.
- **Logistics (via Samsara artifact)** — five vendors, multi-substrate evidence base (FMCSA, fuel, factoring, telematics).
- **Ag (Ambrook), FDA (Light Labs), Construction (Kojo)** — still in the candidate set; not the only options.

The ranking shift doesn't invalidate the doc's strategic shapes. It corrects which verticals deserve consideration. Sections 4-6 below were written against the incomplete top-3 — re-evaluate accordingly.

### Data hygiene note

Ambrook is tagged `primary_industry = "Other"` in `gtm_alpha_vendors` instead of "Agriculture." This is an industry-tagger gap, not a strategic finding. Worth a one-row update next time the tagger runs.

---

## 4. Top 3 Partnership Candidates — Deep Dives

> ⚠️ **2026-05-06 retirement:** The partnership-first frame underlying this entire section has been set aside. After deeper review, the framework cracked on contact with the actual offer mechanics:
>
> - Each candidate (Shovels, Redica, FarmRaise) is too early-stage to operate a partnership program. Founder attention at Seed–Series-B is binary: revenue today or speculative partnerships for revenue someday. Partnerships lose that triage every time.
> - The "proof artifacts" (Ambrook for ag, LightLabs for FDA) are evidence Lucas can run signal-based outbound *on the substrate*. They are not evidence he can deliver value to those specific aggregators' customer bases. The Ambrook→FarmRaise logic does not connect — see 4.3 for the specific gap.
> - The partnership pitch requires the partner to vouch, vet, and operationally engage. That cost is meaningful even when the upside is large.
>
> **Substrate-first reframe (replaces this section's strategic recommendation):** Build outbound directly on the data substrate (USDA, FDA, SEC EDGAR, FMCSA, etc.). Each gtm-alpha run *is* the outbound artifact and the proof of capability. Sell to the end customer directly — the SaaS aggregator becomes a secondary referral source if/when revenue lands, not the gating distribution partner. See Section 3.6 "Implications" and the broader discussion in the 2026-05-06 conversation log.
>
> The deep dives below are preserved as audit trail. They document the partnership-shape evaluation as it stood when written. **Do not act on the partnership pitches in 4.1–4.3 — they are superseded.** The substrate observations (data sources, ICPs, founder profiles) remain useful as context.

### 4.1 Shovels.ai

**One-paragraph overview:** AI-powered building permit + contractor intelligence platform. 170M+ permits aggregated nationally. Sells to solar installers, home-improvement brands, PE firms doing residential construction roll-ups, and B2B SaaS targeting GCs/contractors. Engineering-heavy team; product-led growth motion.

**Funding:** $5M Seed (June 2025, Base10 Partners); $6.5M total raised. Recent + active.

**ICP they serve:** Solar, home services, contractor-tech SaaS, residential PE. Their customers need to find/qualify contractors in specific markets — exactly the buyer Thresh would arm with intelligence-led outbound.

**Their customers' GTM motion:** Most are early-stage SaaS / DTC / PE. They consume Shovels data via API or dashboard, then need to *do something* with it (book meetings, build target lists, run campaigns). The gap between data + execution is wide and unaddressed.

**Founders + signals of partnership openness:** Ryan Buckley + Luka Kacil are YC alums. Public-facing engineering team. Have a blog (showing operator-friendly disposition). Recent seed = need to show topline growth → partnerships with execution arms move that needle.

**Existing partnership / channel program:** None visible. No "trusted partners" page. No press releases naming agency partners.

**Partnership shape Thresh would propose:**
- Shovels licenses their permit-data API → Thresh + 1-2 design-partner customers run pilots showing "Shovels data → Thresh signal-based outbound → meetings booked"
- Thresh becomes the named execution partner Shovels recommends to customers stuck in the "I bought the data, now what?" gap
- Revenue split: per-engagement fee paid by end customer + referral fee from Shovels for sourced revenue
- Lucas's vertical-credibility ramp: he doesn't need to BE a contractor — he needs to be the operator who knows how to turn permits into meetings. His Clay Labs background + 4 yrs quota-carrying covers this.

**Risks:** (1) Shovels may want to build their own outbound layer in-house at Series A. (2) Founders may prefer customers self-serve (PLG default). (3) Could end up exclusively partnered with one agency they pick, locking out late entrants — speed matters.

**First-touch path:** Cold email to Ryan Buckley citing 1-2 specific permit-trigger plays Thresh would build for a Shovels customer (e.g., "permit pulled for $5M+ commercial reroofing → outreach to roofing materials suppliers in 30-mile radius"). Lead with the play, not the partnership ask. Call comes later.

---

### 4.2 Redica Systems

**One-paragraph overview:** FDA enforcement + inspection intelligence aggregator. Pulls warning letters, 483 observations, FDA inspection data, FOIA-sourced enforcement. Sells to quality, regulatory, and compliance teams in pharma and food/supplement companies. The FDA-data layer most directly equivalent to Starbridge's public-sector model.

**Funding:** Series B, $30M (Dec 2021, Savant Growth); $43.5M total raised. Mature enough to have budget; not so mature they've ossified.

**ICP they serve:** Pharma QA/regulatory teams, food/beverage compliance teams, supplement manufacturers. But also adjacent: the SaaS/services companies *selling INTO* these regulated buyers — testing labs (LightLabs), QMS software, audit prep services, regulatory consultancies.

**Their customers' GTM motion:** Two camps. Camp A = compliance teams using Redica defensively (their job is to avoid being on the warning letter list). Camp B = vendors selling to camps A — these are the Thresh-relevant ones. Camp B is the underserved customer in Redica's base.

**Founders + signals of partnership openness:** Michael de la Torre. Series B was 4+ years ago; if no Series C is imminent, they need to grow into existing capital → partnerships matter. No visible execution layer or "channel partners" program.

**Existing partnership / channel program:** None visible. Standard SaaS sales motion via inside sales. No agency named in case studies.

**Partnership shape Thresh would propose:**
- Thresh becomes the *outbound execution partner* for Camp B customers (vendors selling into FDA-regulated buyers)
- Use cases: "warning letter issued to [supplement brand] → outbound to QMS providers, testing labs, audit firms in their network"; "483 observation cluster in [pharma site] → outbound to regulatory consultancies"
- Lucas's credibility ramp: LightLabs run already done — has a working FDA-warning-letter PVP analysis (Naked Nutrition transparency). That's a real artifact, not a hypothetical.
- Pricing: per-engagement, $5-10k/mo retainer Thresh-side, paid by end customer, with Redica earning either referral fee or co-marketed pilot

**Risks:** (1) Redica may consider Camp B a niche they don't want to invest in. (2) Their core buyer (QA at Pfizer) is enterprise, not the Series A SaaS buyer Thresh serves — partnership requires Redica to allocate attention to a customer segment they may not prioritize. (3) Mid-Series-B founders are often heads-down on enterprise expansion, less open to channel experiments.

**First-touch path:** Cold email or LinkedIn DM to Michael de la Torre. Lead with the LightLabs analysis — show, don't tell. Frame it as "I've been running this play for one of your potential customers; want to compare notes on the underserved Camp B customer set?"

---

### 4.3 FarmRaise (farmraise.com)

> ⚠️ **2026-05-06 — partnership thesis retracted.** The Ambrook→FarmRaise logic does not connect. Specific failure mode:
>
> - **Ambrook is FarmRaise-adjacent, not their customer.** Both serve ag, different products. The Ambrook artifact proves Lucas can run signal-based outbound for *any* ag SaaS — including potentially competitive ones to FarmRaise. From FarmRaise's seat, that's not a credibility asset; it's a slight risk.
> - **FarmRaise's product sells to farmers (B2C-ish).** They aggregate conservation-program data for farmer-side decision-making. The "corporate customer base" referenced below is shallow — Syngenta and a handful of other large enterprises. Not a long tail Lucas can be referred into.
> - **Their corporate customers are large enterprise.** Not Lucas's buyer. The Syngenta-shape company has its own field rep army; the smaller corporate ag-input firms aren't large enough to fund $5–10k/mo outbound retainers reliably.
> - **Founder attention is allocated to survival.** YC Seed-stage. Hands-free is the bar — and a partnership program isn't hands-free. Ever.
>
> **The pitch in this section was speculative.** It extended the strategic frame too eagerly. Preserved below as audit trail. Substrate observations remain valid (USDA EQIP/REAP signal substrate is genuinely strong — see 3.6); the partnership-vehicle framing does not survive contact.

**One-paragraph overview:** USDA grant + EQIP/REAP/CSP application platform. Aggregates 1,000+ public conservation/farm funding programs, helps farmers + ranchers find and apply for grants, and exposes that funding-recipient data through partnerships. YC W21 alum. Existing Syngenta partnership (corporate ag input company) shows they're already willing to layer corporate distribution on top of their data product.

**Funding:** Seed (undisclosed, YC W21 graduate). Early enough that growth velocity matters; mature enough to have shipped a real product and a real partnership.

**Why FarmRaise replaces Usul in the top-3:** (1) ag/USDA scored 3.72 average composite signal grade — second-highest substrate quality across runs, with EQIP-holder signal at 4.30. (2) Lucas already has the **Ambrook showcase pipeline run** as a public credibility artifact — the work is done, the methodology is proven, and Ambrook is a high-profile reference point in ag GTM. (3) Ag has none of the relationship-gravity / military-credential gating defense has.

**ICP they serve:** Farmers/ranchers directly (B2C-ish), but also corporate ag partners (Syngenta partnership = ag input/seed companies wanting access to conservation-program-active farmers). Their corporate-side customers are exactly the buyer Thresh would arm — companies selling sustainability inputs, conservation tech, regenerative-ag SaaS, ag fintech, equipment financing — into operators visibly engaged with USDA programs.

**Their customers' GTM motion:** Corporate ag is heavily relationship-driven and dealer-channel-driven. SaaS players selling into farms (Ambrook, AgVend, Bushel-adjacents) struggle to find the right operators at the right moment. EQIP/CSP/REAP enrollment is a near-perfect "this farm just committed to a 5-yr conservation practice" trigger — high-intent, public, time-bounded.

**Founders + signals of partnership openness:** Jayce Hafner (CEO, ex-USDA + Episcopal Church climate policy lead), Sami Tellatin (COO, ex-NRCS field). Operator backgrounds — they've worked inside USDA, they know the buyer. They've already proven they'll partner (Syngenta) — partnership infrastructure exists.

**Existing partnership / channel program:** Syngenta corporate partnership confirmed. No visible execution-layer agency partner. The Syngenta deal is "data feed into Syngenta's own field reps" — different shape than what Thresh would propose.

**Partnership shape Thresh would propose:**
- Thresh becomes the *outbound execution arm* for FarmRaise's smaller corporate customers (the ones not big enough to have Syngenta-scale field rep teams)
- Use cases: "operator with 2+ concurrent EQIP/CSP contracts → outbound to regenerative-ag input cos, conservation tech SaaS, ag fintech"; "USDA Value-Added Producer Grant recipient → outbound to processing equipment vendors, packaging cos"
- Lucas's credibility ramp: lean on the **Ambrook showcase pipeline run** as proof. "Here's how I built signal-based outbound on USDA conservation data for an ag SaaS — same playbook, applied to your customers."
- Pricing: per-customer engagement fee paid by end customer + referral kickback to FarmRaise. Could also do co-marketed pilots with FarmRaise's smaller corporate customers as design partners.

**Risks:** (1) Syngenta partnership may have exclusivity clauses on corporate data distribution. (2) Ag-tech SaaS buyers (FarmRaise's corporate customers' customers) are slow to adopt outbound tooling — long sales cycles per pilot. (3) Lucas's ag credibility is shallow beyond the Ambrook run; he'd need to lean on FarmRaise's domain expertise for buyer-language calibration.

**First-touch path:** Cold email or LinkedIn DM to Jayce Hafner. Lead with the Ambrook showcase work — show, don't tell. Frame: "I ran a public-data-driven pipeline analysis on Ambrook last month using USDA EQIP signals. The natural next step is helping FarmRaise customers do the same thing at scale. Here's a 2-paragraph memo." Memo proposes a pilot with 1-2 of FarmRaise's smaller corporate customers.

---

## 5. Meta-Hypothesis Test: TTT-Clone vs. Partner-of-Many

Both shapes pass the "this could work" bar. Different tradeoffs across the legs of the stool.

| Axis | TTT-Clone (one vertical) | Partner-of-Many |
|---|---|---|
| **Vertical scope** | One vertical chosen, claimed, owned. E.g., construction (via Shovels). | 3-5 verticals served via 3-5 SaaS partnerships. Non-exclusive. |
| **Operator credibility ramp** | High lift. Lucas must become "the construction GTM person" (or whichever). 6-12 months of public work, content, customer logos before referrals compound. | Low lift. Lucas leverages Clay Labs alum + 4 yrs quota credibility (already real). Each partnership uses partner's vertical credibility; Lucas is the GTM operator. |
| **Moat structure** | Vertical specialization compounds. Defense via referrals + reputation. Operator credibility hardens over time. | Cross-vertical pattern recognition. Multiple partnerships = harder to replace, but each one less defensible alone. |
| **Sales cycle** | Fast inside vertical (referrals). Slow to first vertical-relevant customer. | Slow per partnership (6-week courtship). Fast per individual deal once a partnership lights up. |
| **Pricing model** | $8-9k/mo SDR seats (TTT pattern) or $3-5k/mo methodology (current Thresh). Recurring. | Per-engagement fees ($3-10k/mo) + revenue share/referral fees with each SaaS partner. Less recurring at start. |
| **Concentration risk** | One vertical + one SaaS. If Shovels gets acquired or pivots, business shocks. | One partner can disappear without killing the business. Channel concentration risk per partner, not per business. |
| **Lucas's natural fit** | Requires picking ONE and going deep — high opportunity cost on the other 4. Doesn't match Lucas's current work pattern (cross-vertical experimentation). | Closer to current shape. Each partnership is a discrete bet. Doesn't force a commitment Lucas isn't ready to make. |
| **Capital + runway** | 60-90 days to claim a vertical. Slower to first $$. Higher upside if it sticks. | 30 days to first partnership conversation. Faster to first $$. Lower upside per partnership. |
| **Comparable model** | TAM to Target, vertical SDR shops. The Bobby Offterdinger play. | Crawford (Blueprint) — but with data-SaaS partnerships layered on. The "operator-for-hire across many vertical SaaS" play. |
| **What it forces Lucas to give up** | The cross-vertical pattern matching that's currently his unique edge. The freedom to take an interesting one-off run. | The shot at a defensible category-of-one ("the construction GTM guy") that compounds for 5+ years. |

**Key tension:** Lucas's *individual* credibility (Clay Labs alum, 4 yrs quota, Crawford-style methodology) is **horizontal**. His *Thresh* positioning so far has been **horizontal** (regulated industries, broad). TTT-clone requires inverting that — picking a vertical and gaining vertical credibility he doesn't currently have. Partner-of-many lets him keep his existing credibility surface and add data-SaaS leverage on top.

**The honest read:** TTT's playbook works because Bobby Offterdinger spent years as a 5th grade teacher before TAM to Target. Lucas doesn't have that head start in any single vertical. He has it horizontally (Clay Labs, GTM engineer track). **The TTT-clone play asks Lucas to manufacture credibility he doesn't yet have. The partner-of-many play uses credibility he already has.**

That doesn't make TTT-clone wrong — it just makes it slower and more expensive *for Lucas specifically*. A different operator (e.g., a former waste-industry exec) would have the inverse calculus.

**Hybrid path worth considering:** Start with partner-of-many to get to revenue and partnerships fast (30-60 days). Once one partnership compounds heavier than the others (e.g., Shovels ends up driving 60% of revenue), let that pull Lucas into a vertical-clone play organically. The market chooses the vertical, not the strategy doc.

---

## 6. Decision Framework + Open Questions

### Decision criteria

| Question | If yes → | If no → |
|---|---|---|
| Does Lucas want to commit a vertical for 12+ months? | TTT-clone is on the table | Partner-of-many is the better shape |
| Is Lucas willing to slow revenue ramp to build vertical depth? | TTT-clone | Partner-of-many |
| Does Lucas have an operator-credibility starting point in any one vertical? | TTT-clone in that vertical | Partner-of-many across many |
| Is the goal a 5-year defensible business or a 12-month proof-of-life? | TTT-clone (5-year) / Partner-of-many (12-month) | — |
| Is runway pressure forcing 30-day revenue moves? | Partner-of-many | TTT-clone |

### Open questions for Lucas

1. **What does success look like in 12 months?** Three logos in waste management vs. three live partnerships across three verticals — these point to different shapes.
2. **Which of the three top candidates is Lucas most willing to commit to a 6-week courtship for?** Shovels (cold), Redica (cold but he has the LightLabs artifact), FarmRaise (cold but he has the Ambrook showcase artifact). FarmRaise has the cheapest cold-open because Ambrook is the most public/polished showcase asset.
3. **Does Lucas want to keep building Thresh's own data layer (per `research/09`'s vision step #3 — "productize the signal layer") in parallel, or accept that partnership = renting the data layer?** This is a fundamental fork.
4. **Is the original Thresh ICP (Stage 2 vertical SaaS, $3-5k/mo methodology engagements) abandoned, paused, or run in parallel with the partnership play?** The paid Thresh offer ($3-5k/mo) and a partnership play don't necessarily compete — but Lucas's attention does.
5. **Whitespace question:** the four whitespace verticals (OSHA, LL97, insurance, workers' comp) have NO incumbent SaaS aggregator. Is there a future where Thresh becomes the Starbridge for one of those — building the data layer rather than partnering on it? That's a bigger, slower bet, but with higher ownership.

### Concrete next-90-day moves (if going partner-of-many)

| Day | Move | Cost |
|---|---|---|
| Day 1-7 | Cold-email Jayce Hafner at FarmRaise. Lead with the Ambrook showcase run as proof artifact. | 3 hours |
| Day 7-14 | Cold-email Ryan Buckley at Shovels with 2-3 specific permit-trigger plays. | 4 hours |
| Day 14-21 | Cold-email Michael de la Torre at Redica. Lead with the LightLabs PVP artifact. | 4 hours |
| Day 21-45 | First partnership conversation lands → pilot scope agreed → 1 design-partner customer chosen | TBD |
| Day 45-90 | First pilot runs. Outcome data. Decide: double down on this partnership, or test the next bench candidate (HigherGov, CarrierOK, Trilliant Health). | Variable |

### Concrete next-90-day moves (if going TTT-clone)

| Day | Move | Cost |
|---|---|---|
| Day 1-30 | Pick the vertical (most likely construction via Shovels OR food/FDA via Redica — both have fresh signals + existing artifact). Commit publicly. | Sunk |
| Day 30-60 | Build vertical thought leadership: 5 LinkedIn posts, 1 long-form piece, 1 vertical-specific data atlas page on runthresh.com. | High |
| Day 60-90 | Land 2-3 logos in the chosen vertical. Use partnership with the chosen data SaaS as the unfair advantage in pitches. | High effort |

---

## 7. What This Artifact Doesn't Decide

- Whether to do TTT-clone or partner-of-many — Lucas's call.
- Which vertical to claim if going TTT-clone — would require deeper customer-conversation evidence than this scan provides.
- Whether the Thresh website needs to change before any of this — not in scope.
- Whether to hire / find a co-founder for the execution layer — partnership shapes can shift this question, addressed if pursued.

The next conversation is a yes/no on direction, not on tactics.
