# Playbook Feedback Log

A registry of claims about playbooks (advisor / buyer / customer / peer feedback synthesized into testable hypotheses). Follows the [registry pattern](../docs/registry-pattern.md).

## Operating notes

**When to open this file:**
- Before building a new playbook (scan claim ledger for relevant rules)
- Before revising an existing playbook (scan for playbook-specific entries)
- After receiving new feedback (decide: extends an existing claim, or new claim?)
- Quarterly cadence (review stale claims, decide on action queue)

**How to add:**
- New feedback → add a source entry in the archive section, dated, verbatim where useful
- Tag the entry with claim IDs it informs (existing or new)
- Update the claim ledger: increment evidence-source count, update status
- If status flips to `cross-validated`, add to action queue
- If a claim graduates, move it to the graveyard with destination + date

**Promotion criteria:** ≥2 independent *and different-quality* sources confirming the same claim → ripe to promote. Source quality calibrates weight (see `docs/registry-pattern.md` Principle 2).

**Source calibrations active:**
- **Le** (interim Head of Marketing / advisor at Assured) — ops-background, pessimistic-friend disposition. Le-only claims max out at `mounting-evidence`. Cross-validation by a different-discipline source still counts.

**Retirement criteria:** disconfirmed by test, or stale 60+ days without fresh evidence.

**Promotion routing (where claims graduate to):**
- Playbook-template / artifact rules → `playbooks/_CONVENTIONS.md`
- Cold-email principles → memory files (`~/.claude/projects/.../memory/feedback_outbound_*.md`)
- Positioning / offer claims → `thresh.md` and/or website copy
- Project-level operating rules → `CLAUDE.md`

---

## Claim ledger (active)

| ID | Claim | Sources (independent) | Status | Next action | Kill criteria |
|----|-------|-----------------------|--------|-------------|---------------|
| C4 | Real Thresh ICP profile = Series A-C company with TAM scored, BDR bandwidth gone (events/conferences), email infra dissatisfaction. Maps to "carry-the-bag" offer near 1:1. | Le (1) | mounting-evidence | Pick 5-10 fitting accounts; pitch carry-the-bag offer using Le's articulation; track conversion to discovery call. | Pitched at 5+ profiles; <1 discovery call → ICP profile is wrong or offer pitch is wrong. |
| C5 | Playbook deep-pages (`/playbooks/[name]/`) may not surface the offer-clarity already established on the runthresh.com homepage. Reviewers landing directly on a playbook can miss the Tier 01 / sample framing. | Le (1, downweighted per source calibration — may reflect her skipping homepage context). Sage's "is this for sale" reading was implicit, not explicit. | mounting-evidence | Optional: add a small "this is a sample — see runthresh.com for the full offer" back-link or footer on each playbook deep-page. Low-cost, low-risk experiment. | Back-link added; offer-clarity confusion persists in new reviewer feedback → issue is on the homepage itself, not the navigation. |
| C6 | PE buying behavior = relationship-driven (introductions from existing investors / co-presence at events), not cold-email-driven. Has implications for Phase 0 Cell C (PE-acquired waste haulers). | Le (1) | untested | On Cell C work, allocate one outreach effort to investor-side or event-side motion in parallel with cold-to-ops. Compare yield over 60-day window. | Investor/event motion yields equal-or-worse than cold-to-ops → not worth the channel-build cost. |
| C7 | Seed-stage may be better-fit ICP than later-stage (smaller team, less in-house signal work, more receptive to outsourced execution). | Le (1, hint via "have you tried selling to seed companies?") | untested | Score outreach response across stages over next 30-60 days. If Seed-stage outperforms meaningfully, tighten ICP. | Stage-level reply rates are flat or inverted (later-stage performs better) → Le's hint is discovery curiosity, not signal. |
| C8 | Person-level (Layer 2) personalization is the next-tier ask from sophisticated AE/buyer-side reviewers. Currently every playbook does Layer 1 (company-level) only. | Sage (1) | untested | Build one Layer-2-personalized variant of an existing play. Compare reply / quality rate to Layer-1 baseline. | Layer 2 yields marginal lift over Layer 1 → not worth the data-acquisition cost; stays at Layer 1. |
| C9 | For data-sparse segments (ag, blue-collar trades, small-town pro services), contact data is the rate-limiter, not signal data. Every play assumes contact-info is solvable downstream — none addresses this gap. | Le (1) | untested | Pick a data-sparse segment. Identify 10-20 entities. Attempt outbound via non-Apollo / non-LinkedIn sources (FSA agent directories, association rolls, etc.). Compare contact-yield to digital-footprint-rich segment baseline. | Yield is poor across all alternative sources → segment-availability disqualifier is the right move (don't pursue these segments). |

## Action queue

**Ripe to test (≥2 different-quality independent sources OR explicit test plan):**
- (none currently — Le-only claims downgraded; cross-validated claims have all graduated)

**Ripe to promote (cross-validated, awaiting graduation):**
- (none currently — most recent graduations moved to graveyard)

**Stale (no fresh evidence 60+ days):**
- (none yet — log is <2 weeks old)

**Low-cost optional experiments (single-source, not promotion-ready):**
- C5 — add a small back-link on each playbook deep-page pointing to homepage offer-clarity. Low-risk navigation fix, even if Le's underlying claim is downweighted.

**Pending external action (graduated, but action lives outside the file):**
- C2 (graveyard) — already directionally aligned with current homepage. Reframe is "methodology table stakes; differentiation = executing it correctly with the public-data substrate," NOT "better than your BDR." Sense-check next homepage iteration against this framing. Do not auto-write.

---

## Source entries (archive)

### 2026-05-04 — Le on Ambrook playbook
**Source:** Le, interim Head of Marketing / advisor at Assured. Personal relationship.
**Playbook:** `playbooks/ambrook-com/`
**Tags:** C5, C9, **C2 (promoted)**

> "Ohh this is pretty interesting. I'll need to look up a few things to see how applicable / relevant this is. I think the data sources mentioned r interesting. Can you try this for assured health? The farming space is interesting cuz we do know the entities but we don't have their contact info to outbound. That's the main issue w outbounding to this segment."

**Notes:** First Le interaction. Methodology + data-source curation reaction was strong enough to convert into the Assured-playbook ask (chronological cause of all subsequent Le entries). Contact-data observation seeded C9.

---

### 2026-05-08 — Le on Assured playbook (initial chat)
**Source:** Le.
**Playbook:** `playbooks/withassured-com/`
**Tags:** **C1 (promoted)**

> "Yes but for some reasons I don't think the final product was good. I agree w the methodology. But maybe something is missing. For the assured playbook that's not how their buyers talk at least from my experience chatting with them. They respond most to simplest messaging — credentialing in 48 hrs. It gets them curious. And then they ask how do you do that. The most common objection is pricing 😂 after that."

**Notes:** Originally produced two hypotheses (A: outcome-led messaging when self-evident category-leading outcome exists; the convoluted-messaging observation that became part of C1). Outcome-led-messaging insight is real but Assured-specific and product-specific (depends on existence of a "30-45x compression" headline number); not promoted as a general rule, retired into source archive only.

---

### 2026-05-08 — Le on Assured playbook (extended)
**Source:** Le, follow-up to initial chat.
**Playbook:** `playbooks/withassured-com/`
**Tags:** **C1 (promoted)**, **C2 (promoted)**, C4, C5, C6, C7, footnote H

> "The triggers are pretty much what we are using rn! There were some new data sources I haven't heard of before.
>
> The messaging / the plays seem a bit convoluted to read imo. A bit confusing.
>
> The current challenge is how to scale / automate outbounding as much as possible to the relevant companies. I have a list of 2-3k accounts scored but the BDRs are kinda slow in going thru them / don't have as much bandwidth cuz they have to go to events / conferences. Thanks so much for generating these btw! Helpful. But again unsure if I would pay for this. The goal is they would tell u they don't have enough capacity and then you pitch to them you can do it for them? The play books are what I'm generally familiar with / already having the BDRs own.
>
> For PEs most effective way to get in front of them meaningfully is to go thru investors from my experience. And attending PE events in general. Email deliverability has been an issue. I really don't like smartlead and instantly and these standard warmup platforms they all suck.
>
> Have you tried selling your service to seed companies?"

**Notes:** Densest single feedback message in the log. Buyer-articulated ICP (C4), offer-clarity diagnosis (C5), PE channel intel (C6), Seed-stage hint (C7). Methodology validation ("triggers are pretty much what we are using") was the evidence that pushed C2 from `mounting-evidence` to `confirmed`.

---

### 2026-05-08 — Sage on HiBob playbook
**Source:** Sage, AE at HiBob. Personal friend of Lucas. Buyer-side AE / sales-operator perspective (different vantage from Le's marketing-leader perspective).
**Playbook:** `playbooks/hibob-com/`
**Tags:** **C1 (promoted)**, **C3 (promoted)**, C5 (implicit), C8

> "Just messed around with it for a bit. First impression is it's really sick. The triggers are spot on. It has an incredible sense of HiBob value prop and the ICP knowledge is seriously good. The personalization around the targeted company is awesome, and I like the straightforward nature of the tool as well.
>
> A couple things that could help:
>
> - Could you personalize the play to the individual as well as the company? I realize this requires a different level of data, and not sure how easily accessible this is. I know linkedIn has some, but would be insane to be able to tap into other data points (without it being creepy)
>
> - Tbh could dumb down the jargon of the play to the prospect so it sounds more human and is an easier read. I think these days folks are weary of things with too big words and will stop reading if it sound like AI. If possible to deliver that message in a simple way
>
> Hope this helps, but love where you're at. This is already better than my BDR lol"

**Notes:** Cross-validated C1 (jargon/AI-detector) — same week as Le, completely different vantage point (AE vs marketing leader, Series D vs Seed, HRIS vs health-tech). Unprompted "better than my BDR" benchmark = C3.

---

## Footnotes (single-data-point observations, not yet claims)

**H — Standard warmup platforms (SmartLead, Instantly) have buyer-side dissatisfaction at the GTM-leader level.** Source: Le 2026-05-08 ("I really don't like smartlead and instantly and these standard warmup platforms they all suck"). Lucas currently runs 9 inboxes on SmartLead. Not actionable as a claim (single source, no clear test). Re-evaluate at next deliverability re-audit (~2026-03-24 per memory) — if Lucas's own deliverability suffers, this footnote earns its way to a real claim with a real test.

---

## Graveyard

### C1 — Playbook copy reads as convoluted / AI-generated to sophisticated recipients
- **Status:** promoted 2026-05-08
- **Destination:** `playbooks/_CONVENTIONS.md` (Playbook copy register)
- **Sources:** Le (Ambrook + Assured) + Sage (HiBob), 2 independent
- **Why graduated:** Cross-validated by 2 independent sources (different industries, different roles, same week). Stable enough to be a rule.

### C2 — Methodology + signal/trigger work + data-source curation = at-or-above peer baseline; not the differentiation
- **Status:** promoted 2026-05-08 (confirmed)
- **Destination:** Already directionally reflected in current `index.html` and `thresh.md`. The right framing is **"methodology is table stakes; everyone wants to do this — almost no one executes it correctly because they lack the public-data substrate or the rigor."** NOT "better than your BDR" / substitution-against-internal-team framing — Lucas explicitly rejected adversarial positioning 2026-05-08. Sense-check next positioning iteration against this framing. Do not auto-write.
- **Sources:** Le ("triggers are pretty much what we are using rn") + Sage ("triggers are spot on"), 2 independent + different-quality (marketing-leader + AE)
- **Why graduated:** Confirmed by different-quality cross-validation. Differentiation lives in execution rigor + public-data substrate, not adversarial substitution.

### C3 — Sage's "better than my BDR" is real, unprompted, but not actioned
- **Status:** promoted 2026-05-08 (no further action)
- **Destination:** Lives here as supporting evidence for C2 (methodology = table stakes). Lucas explicitly rejected adversarial-substitution framing 2026-05-08 — does NOT want to position against the buyer's internal team. Sage's line is real signal, but the path it implies (testimonial / "better than your BDR" website copy) is the wrong path for Thresh's positioning.
- **Sources:** Sage (HiBob, AE), 1 strong unprompted source.
- **Why graduated:** Lucas decided 2026-05-08 NOT to action it. Stays in graveyard as evidence that the table-stakes-methodology read is real (someone benchmarked Thresh as already credible vs. their existing capability) without being used to fuel adversarial framing.

---

## Retired (untested, never promoted)

(none yet)
