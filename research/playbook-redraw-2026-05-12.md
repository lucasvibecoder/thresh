# 2026 AI-Native Outbound Playbook — Jordan-Shaped Redraw

**Generated:** 2026-05-12
**Status:** Working draft. Stage 2 + Stage 3 drafted, then revised after two consults against the Jordan/Cannonball corpus. **Currently shipped: 2 segments (T6, T2-merged). Parked: T3, T4 (with reasoning). Stage 2.5 stub holds 4 candidate situations (S-A, S-B, S-C, S-D) that need next-session harvest corroboration.** Stages 4 + 5 still TODO.
**Audience:** Lucas first (internalize), Thresh prospects second. Generic Jordan-shape — no Thresh / FMCSA specifics inside the visual.
**Locked decisions:** see `HANDOFF-2026-05-12.md`. Reddit HIGH · LinkedIn MED · G2 LOW. Strict painShape separation.
**Consult-driven changes (2026-05-12):** added 4-gate ship-or-park check to Stage 2 Step 3 (NEW × EXISTENTIAL × IDENTIFIABLE × VPP-tier-≥-Risk-Mitigation); demoted T3 + T4 to PARKED with reasoning; added EDP + VPP-tier fields to T6 + T2-merged; added Cannonball GTME-rename leader-corroboration to T6; added Stage 2.5 for missing event-shaped situations.

---

## Spine

```
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 0 — Painting vs Printing fork  (route the reader)     │
   └──────────────────────────────────────────────────────────────┘
                              │  (printing path)
                              ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 1 — Inputs        (harvest pain language by source)   │
   └──────────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 2 — Synthesis     (cluster → score → ship-or-park)    │
   └──────────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 3 — Pain Segments (3-5 shipped cards)                 │
   └──────────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 4 — Per-Segment Build         (TODO this session)     │
   └──────────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  STAGE 5 — Send + measure MBR        (TODO this session)     │
   └──────────────────────────────────────────────────────────────┘
```

---

## STAGE 0 — Painting vs Printing Fork

> Before you build anything, choose the lane. Not every business should run signal-based programmatic outbound. The fork is not a preference — it is dictated by TAM × ACV × pain-repeatability.

```
                    ┌─────────────────────────────────────┐
                    │  DIAGNOSTIC — answer all 3          │
                    └─────────────────┬───────────────────┘
                                      │
                                      ▼
              ┌──────────────────────────────────────────────┐
              │  1. TAM size?                                │
              │  2. ACV?                                     │
              │  3. Is the buyer's pain                      │
              │     repeatable across accounts —             │
              │     or unique per account?                   │
              └──────────────────┬───────────────────────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              ▼                                     ▼
  ┌────────────────────────────┐       ┌────────────────────────────┐
  │         PAINTING           │       │         PRINTING           │
  │                            │       │                            │
  │  TAM:    < ~500 accounts   │       │  TAM:    > ~5,000 accounts │
  │  ACV:    very high         │       │  ACV:    mid               │
  │  Pain:   unique per acct   │       │  Pain:   patterned         │
  │                            │       │                            │
  │  → 1:1 account research    │       │  → public-data signals     │
  │  → handcrafted PVPs        │       │  → programmatic detection │
  │  → tiny target list        │       │  → segment-scale messaging │
  │  → high $ per touch        │       │  → low $ per touch         │
  │                            │       │                            │
  │  NOT THIS PLAYBOOK         │       │  ← THIS PLAYBOOK           │
  └────────────────────────────┘       └─────────────┬──────────────┘
                                                     │
                                                     ▼
                                              continue to Stage 1
```

**Painting-side failure mode (for the reader who self-routes here by mistake):** if you try to "print" a market that is actually painting-shaped (< 500 accounts, very high ACV, pain unique per account), the signal-based programmatic motion will exhaust your TAM in 60–90 days and you'll have spent the budget on infrastructure instead of account research.

**Printing-side failure mode (what the rest of this playbook protects against):** if you try to "paint" a market that is actually printing-shaped (> 5,000 accounts, mid ACV, patterned pain), you'll handcraft 200 emails when the same insight could have addressed 20,000. You will run out of runway before you reach pattern-detection.

The rest of this playbook is the printing-side spine.

---

## STAGE 1 — Inputs

> Output of this stage: a corpus of pain-language quotes, tagged by source-trust and painShape family. You cannot start Stage 2 until you have this corpus.

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│   1P INPUTS                          3P INPUTS                         │
│   (your data — gold standard)        (the world's data — proxy only)   │
│                                                                        │
│   • closed-won/lost notes            • Reddit       — HIGH trust        │
│   • call recordings                  • LinkedIn     — MED trust         │
│   • CRM win/loss text                • G2 / Capterra — LOW trust        │
│   • CS transcripts                                                     │
│   • churn-call recordings            (Source-trust hierarchy is        │
│                                       NOT optional. G2 never           │
│                                       overrides Reddit — G2 is         │
│                                       vendor-incentivized and          │
│                                       suppressible.)                   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘

                  STRICT painShape SEPARATION RULE
                  ────────────────────────────────
   Tag each quote with one of:
     • ai-sdr-collapse      — AI-SDR vendors (11x, Artisan, AiSDR, Regie)
     • data-quality         — data/list tools (Apollo, ZoomInfo)
     • tool-underuse        — data orchestration (Clay)
     • stack-fragmentation  — multi-tool orchestration failure
     • methodology-meta     — peer practitioner talk (vocabulary only)

   NEVER merge across families during clustering. The pain shapes are
   genuinely different and merging them produces unshippable segments.
```

**Hypothesis-protection rule (this is the new one — added after the Lucas-flag at the start of this redraw):**

> If you have no 1P data yet, every Pain Segment you ship must trace back to a 3P quote. Hypothesis-only persona pain language does not survive Stage 2. Your own operating doc's persona pain points are HYPOTHESIS until corroborated by 3P harvest.

**Volume target before you start Stage 2:** ~200+ quotes across the three 3P sources, with at least 5 quotes per painShape family. (Methodology-meta is optional — used for cold-email vocabulary, not pain.)

---

## STAGE 2 — Synthesis

> Input: corpus from Stage 1. Output: 4-7 themes ranked by asymmetry, of which 3-5 ship as Stage 3 segment cards. The rest park.

### Step 1 — Harvest box (this redraw's actual inputs)

```
┌──────────────────────────────────────────────────────────────────────┐
│  CORPUS — 247 quotes, harvested 2026-05-12                           │
├──────────────────────────────────────────────────────────────────────┤
│  painShape family    Reddit(HIGH)  G2(LOW)  LinkedIn(MED)   Total   │
│  ─────────────────   ──────────    ──────   ────────────    ─────   │
│  ai-sdr-collapse         93           20         0           113    │
│  data-quality            27           12         1            40    │
│  tool-underuse           27           12         3            42    │
│  stack-fragmentation      2            0         2             4    │
│  methodology-meta         0            0        48            48    │
└──────────────────────────────────────────────────────────────────────┘

  Quality flags:
  - stack-fragmentation N too small → cannot ship a segment yet
  - methodology-meta = vocabulary library, never a segment
```

### Step 2 — Cluster within painShape (the strict-separation rule binds here)

```
   ai-sdr-collapse ──┬── T1  AI-SDR has no conversation-state awareness
                     └── T2  AI-SDR output generic + burns time without
                             booking meetings

   data-quality   ──┬── T3  ZoomInfo is the overpriced default for teams
                    │       that don't need it
                    └── T4  Apollo data tanked post-LinkedIn enforcement;
                            buyers now verify everything separately

   tool-underuse  ──┬── T5  Clay credit-burn / "atrocious pricing" /
                    │       "under mind control" subscription
                    └── T6  "GTM Engineer" role didn't pan out — hired
                            for Clay magic, got an "enrichment donkey"

   stack-fragmentation ──── (N=4, too few to cluster — flag for next pass)

   methodology-meta    ──── (vocabulary library — Q-238 through Q-247,
                            not a segment)
```

### Step 3 — Score each theme on 4 gates (revised 2026-05-12 post-consult)

> Asymmetry score alone wasn't enough. After consulting Jordan/Cannonball corpus, every theme must pass **4 gates** before it can ship as a segment. Cannonball trifecta: NEW × EXISTENTIAL × IDENTIFIABLE. Plus the Value Prop Pyramid tier check: Thresh's solution must sit at Risk Mitigation or higher when reading this pain — Efficiency-tier reads kill pricing power. [Cannonball · *Brand Blitz: Finding Pain-Based Segments* · What the Hell is a Pain-Based Segment?] [Cannonball · *The Cannonball Value Prop Pyramid* · Introducing the Cannonball Value Prop Pyramid]

```
 ID  Theme                            NEW   EXISTENTIAL   IDENTIFIABLE   VPP≥Risk-Mit   SHIP?
 ──  ─────                            ───   ───────────   ────────────   ────────────   ─────
 T6  GTME role didn't pan out         ✓     ✓ headcount   ✓ HIGH         ✓ Risk-Mit     SHIP
                                            staked
 T2  AI-SDR generic + burns time      ✓     ✓ domain      ✓ MED          ✓ Risk-Mit     SHIP
   (merged with T1)                         rep damaged                    + Growth
 T3  ZoomInfo overpriced default      ✗     ✗ annoyance,  ✓ HIGH         ✗ Efficiency   PARK
                                      (years not exist.                    only
                                      old)
 T4  Apollo data tanked              ~     ~ they're     ✓ HIGH         ✗ Efficiency   PARK
                                      (6mo+ already                       only
                                      ago)  verifying
                                            sep.
 T1  AI-SDR no conversation-state     —     —             —              —             ABSORBED
                                                                                       into T2
 T5  Clay credit-burn                ~     ✗ budget      ✓ MED          ✗ Efficiency   PARK
                                            annoyance                     only
```

  Gate definitions:
  - **NEW** = pain emerged recently enough that the buyer hasn't built coping mechanisms
  - **EXISTENTIAL** = solving it is mission-critical, not nice-to-have
  - **IDENTIFIABLE** = pain is detectable via Layer-A public data (asymmetry score)
  - **VPP ≥ Risk-Mit** = Thresh's solution reads at Risk-Mitigation, Growth, or Customer-Satisfaction tier — not Efficiency. If buyer reads Thresh as "save money," card is unshippable.

  Verdict: 2 themes pass all 4 gates. T3/T4/T5 fail. T1 absorbed into T2.

### Step 4 — Pain ↔ Public-Data mapping

> Layer A = directly observable from public data (job posts, vendor logos, BuiltWith).
> Layer B = inference / triangulation (overspend math from headcount, bounce-rate from sent-domain analytics).
> A theme without a working Layer-A signal cannot anchor a printing-side segment — it has nowhere to start the list.

```
   Theme  →   Layer-A signal                       Layer-B inference
   ─────      ───────────────                       ─────────────────
   T6     →   Open GTME role 60+d (Greenhouse/      Paid Clay tenure +
              Lever/LinkedIn)                       team-size mismatch

   T3     →   ZoomInfo logo (BuiltWith / case       Per-seat overspend math
              study) + LinkedIn HC < 30 reps        from team size

   T4     →   Apollo customer + tenure 6mo+         Bounce-rate decay post-
                                                    LinkedIn enforcement

   T2     →   AI-SDR vendor logo + open SDR/AE      Rep-ramp pattern from
              role (proves AI didn't replace        LinkedIn activity
              human work)

   T1     →   AI-SDR vendor logo                    Cold-send audit of their
                                                    actual reply threads

   T5     →   Clay customer (BuiltWith) +           Credit-burn estimate from
              recent GTME hire                      team size + workflow shape
```

### Step 5 — Cross-cutting observation (this is META-EDP, NOT a 7th segment)

```
┌──────────────────────────────────────────────────────────────────────┐
│  DATA QUALITY IS THE UNIFYING ROOT CAUSE                             │
│                                                                      │
│  Q-165 (Reddit · r/SaaS · 2026-05-03 · u/Time-Mix3963):              │
│                                                                      │
│  "once you automate list building, you realize the bottleneck was    │
│   never there anyway. it's still data quality."                      │
│                                                                      │
│  Implication for messaging: every segment's cold email should        │
│  RE-DIAGNOSE the buyer's pain back to data quality, even when the    │
│  buyer's stated complaint is about a tool layer above it.            │
│                                                                      │
│  This is meta-EDP. It does NOT become a 7th segment card. It         │
│  becomes a copy rule that runs through all 4 shipped cards.          │
└──────────────────────────────────────────────────────────────────────┘
```

### Step 6 — Ship-or-park decision (revised 2026-05-12 post-consult)

```
   SHIP as Stage 3 cards (passed all 4 gates):
     T6 — GTME role didn't pan out        (Risk-Mitigation read; staffing-event)
     T2 — AI-SDR isn't delivering         (Risk-Mit + Growth read; merges T1)

   PARK with reasoning:
     T1 — AI-SDR no conversation-state    (absorbed into T2 as sub-failure-mode)
     T3 — ZoomInfo overpriced default     (FAILS: not NEW, not EXISTENTIAL,
                                          Thresh reads at Efficiency tier only)
     T4 — Apollo data tanked              (FAILS: marginal-NEW, marginal-
                                          EXISTENTIAL, Efficiency-tier read)
     T5 — Clay credit-burn                (FAILS: not EXISTENTIAL, Efficiency
                                          tier; overlaps T6 buyer)
     stack-fragmentation                  (N=4, harvest more before ship)

   WHY ONLY 2 (NOT 4): the previous ship list included T3 + T4. Re-applying
   Jordan's Concentric Circle Test + Cannonball's 3-gate trifecta + Value
   Prop Pyramid tier check, T3 and T4 don't survive. Buyer reads them at
   Efficiency tier ("save money on ZoomInfo / fix data") — which kills
   pricing power and leaves Thresh "selling 3 rings out" from the segment's
   actual core challenge. [Blueprint · *The Concentric Circle Test* · Layer 1]

   What this means for Phase 0: only T6 + T2 ship from this harvest pass.
   The harvest itself was tool-keyed (Apollo, ZoomInfo, 11x, Clay), which
   surfaced tool-failure themes but missed staffing/funding/transition
   situations. See Stage 2.5 below for the missing scenarios that need a
   second harvest pass.
```

---

## STAGE 3 — Pain Segment Cards (2 shipped + 2 parked-with-reasoning)

> Each card is structured the same way so the rest of the playbook (Stage 4 list-build, Stage 5 send) can ingest them programmatically.

> **Revised 2026-05-12 post-consult:** T3 + T4 moved to PARKED. They failed the Cannonball 3-gate trifecta (NEW × EXISTENTIAL × IDENTIFIABLE) + the Value Prop Pyramid tier check. Cards preserved below with reasoning. **Shipped:** T6, T2-merged.

### SEGMENT 1 — T6 · "GTM Engineer role didn't pan out"  · SHIPPED

```
┌─────────────────────────────────────────────────────────────────────┐
│  painShape:        tool-underuse                                    │
│  family:           Data orchestration (Clay)                        │
│  event-type:       staffing-event (failed internal hire)            │
│  asymmetry:        ★★★ HIGH                                          │
│  Cannonball 3-gate: NEW ✓ · EXISTENTIAL ✓ · IDENTIFIABLE ✓           │
│  VPP tier:         Risk Mitigation (headcount $ staked, can't bleed │
│                    more) + Effectiveness (Thresh delivers the       │
│                    capability the failed hire was meant to deliver) │
│  Existential Data  Days the GTME role has been open ×               │
│  Point (EDP):      team-size dependent on the role landing          │
│  N quotes:         5 (Reddit anchors Q-165, Q-170, Q-174)           │
│                                                                     │
│  Leader-level corroboration (NEW):                                  │
│    Cannonball renamed "GTM Engineer" → "Revenue Growth Engineer"    │
│    on 2026-01-31. *"The term was working. People understood it.     │
│    Why rock the boat? But Jordan's on stage building SaaS products  │
│    in sixty minutes, and I'm out here teaching people how to write  │
│    better cold emails? The market moved."* [Cannonball · *Why       │
│    We're Changing from GTM Engineers to Revenue Growth Engineers*]  │
│    Use this in the cold-email anchor — it's leader-level proof      │
│    that the role-as-defined doesn't work, stronger than Reddit      │
│    canceller voice alone.                                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Most-cited pain element (verbatim Reddit voice):                   │
│  "GTME role was 95% branding, 5% Clay operator. Companies hired     │
│   expecting magic, got expensive list-builders.                     │
│   I'll be happy to see the term die."                               │
│                                                                     │
│  Public-data signal (Layer A — start your list here):               │
│  → Open GTM Engineer / Revenue Engineer / Growth Engineer role,     │
│    posted 60+ days ago on LinkedIn / Lever / Greenhouse             │
│  → Bonus enrichment: paid Clay subscription (BuiltWith)             │
│  → Bonus enrichment: vertical SaaS classification                   │
│                                                                     │
│  Cold-email anchor (WORKING DRAFT — Lucas to review):               │
│  > Your GTM Engineer role has been open [N] days. The role fills    │
│  > <30% of the time within 90. The reason isn't talent supply —     │
│  > it's that the role was defined to do what Clay already does.     │
│  > Here's what your team actually needs instead.                    │
│                                                                     │
│  Re-diagnosis hook (the meta-EDP from Stage 2 Step 5):              │
│  Reframe their GTME-shaped need as a data-quality problem one       │
│  layer down. "You're hiring for Clay orchestration, but the         │
│  bottleneck is the data underneath it."                             │
└─────────────────────────────────────────────────────────────────────┘
```

### PARKED — T3 · "ZoomInfo is the overpriced default"

> **STATUS: PARKED.** Fails 2 of 4 ship-gates. Pain isn't NEW (buyer has had ZoomInfo for years and built coping mechanisms). Pain isn't EXISTENTIAL (it's a budget annoyance, not a survival threat). Asymmetry is real (IDENTIFIABLE passes) but Thresh's solution reads at the Efficiency tier ("save money") — which is the bottom of the Cannonball Value Prop Pyramid and produces no pricing power. Card preserved below for the record. Do not build Stage 4 or Stage 5 against this card.

```
┌─────────────────────────────────────────────────────────────────────┐
│  painShape:    data-quality                                         │
│  family:       Data / list tools (Apollo, ZoomInfo)                 │
│  asymmetry:    ★★★ HIGH                                              │
│  N quotes:     7 (Reddit anchors Q-141, Q-142, Q-148)               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Most-cited pain element (verbatim Reddit voice):                   │
│  "Honestly ZoomInfo is the default for a reason but it's overkill   │
│   if u just need standard enrichment ... save a ton by switching    │
│   to something like apollo or clearbit ... 90% of the same data     │
│   for way less cash."                                               │
│                                                                     │
│  Public-data signal (Layer A — start your list here):               │
│  → ZoomInfo customer logo (BuiltWith / public case study / their    │
│    own customer wall)                                               │
│  → LinkedIn headcount < 30 sales reps                               │
│  → Bonus enrichment: per-seat-overspend math (Layer B)              │
│                                                                     │
│  Cold-email anchor (WORKING DRAFT — Lucas to review):               │
│  > You're paying ZoomInfo enterprise rates for a sales org of [N].  │
│  > At this team size, the alternatives are [X], [Y], [Z] — and the  │
│  > data-quality gap is smaller than ZoomInfo's pricing implies.     │
│                                                                     │
│  Re-diagnosis hook:                                                 │
│  ZoomInfo is the symptom; the real pain is they bought enterprise   │
│  data infrastructure for a team that needed enrichment hygiene.     │
│  Reframe as "you don't need a bigger database, you need a better    │
│  cleaner one."                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### PARKED — T4 · "Apollo data tanked"

> **STATUS: PARKED.** Fails 2 of 4 ship-gates. NEW is marginal (the LinkedIn-enforcement event hit 6+ months ago — buyers have already started verifying separately, i.e., they've built a coping mechanism). EXISTENTIAL is marginal (the workaround exists, it's just annoying). IDENTIFIABLE passes. But Thresh's solution reads at the Efficiency tier ("we'll replace your data tool") — Value Prop Pyramid bottom. Card preserved below for the record. Do not build Stage 4 or Stage 5 against this card.

```
┌─────────────────────────────────────────────────────────────────────┐
│  painShape:    data-quality                                         │
│  family:       Data / list tools (Apollo, ZoomInfo)                 │
│  asymmetry:    ★★★ HIGH                                              │
│  N quotes:     1 strong anchor (Q-139) + corroboration across       │
│                multiple Apollo-customer threads                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Most-cited pain element (verbatim Reddit voice):                   │
│  "Apollo: quality tanked after the LinkedIn thing. Used it for      │
│   6 months and ended up verifying everything separately anyway,     │
│   which defeats the purpose."                                       │
│                                                                     │
│  Public-data signal (Layer A — start your list here):               │
│  → Apollo customer (BuiltWith / customer logo / disclosed in case   │
│    study)                                                           │
│  → Tenure 6+ months (post-LinkedIn-enforcement event)               │
│  → Bonus Layer-B: bounce-rate from sent-domain analytics            │
│                                                                     │
│  Cold-email anchor (WORKING DRAFT — Lucas to review):               │
│  > You've been on Apollo since [date]. The data-quality drop after  │
│  > LinkedIn's anti-scraping enforcement hit around the 6-month      │
│  > mark — your team is now verifying separately, which defeats      │
│  > the purpose. Here's the replacement structure.                   │
│                                                                     │
│  Re-diagnosis hook:                                                 │
│  Apollo's quality decay is downstream of LinkedIn's enforcement —   │
│  not Apollo's product team. Buyer typically blames the vendor;      │
│  reframe it as a structural data-supply problem they can't fix      │
│  by switching providers laterally.                                  │
│                                                                     │
│  Caveat: N=1 strong Reddit anchor. Verify the pattern in a second   │
│  harvest pass before committing serious send volume to this segment.│
└─────────────────────────────────────────────────────────────────────┘
```

### SEGMENT 2 — T2-merged · "AI-SDR isn't delivering" (absorbs T1)  · SHIPPED

```
┌─────────────────────────────────────────────────────────────────────┐
│  painShape:        ai-sdr-collapse                                  │
│  family:           AI-SDRs (11x, Artisan, AiSDR, Regie.ai)          │
│  event-type:       failure-event (tool purchase didn't deliver)     │
│  asymmetry:        ★★ MED                                            │
│  Cannonball 3-gate: NEW ✓ (60-90d vintage) · EXISTENTIAL ✓ (domain  │
│                    rep damaged, cost-per-meeting blown) ·           │
│                    IDENTIFIABLE ✓ (vendor logo + open SDR role)     │
│  VPP tier:         Risk Mitigation (sales-domain reputation /       │
│                    pipeline cliff) + Growth (replacement pipeline)  │
│  Existential Data  Cost-per-meeting trend since AI-SDR purchase ×   │
│  Point (EDP):      send-domain reputation score                     │
│  N quotes:         35 total (T2: 16 + T1: 19 absorbed)              │
│                    Reddit anchors: Q-045, Q-048, Q-049, Q-050, Q-051│
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Most-cited pain element (verbatim Reddit voice):                   │
│  "Some look great in demos, but when I start to use them they're    │
│   either clunky, too generic, or just create more work than they    │
│   save. I'm done trialling 'the AI-SDR.'"                           │
│                                                                     │
│  Documented sub-failure-modes (both ship in the same card):         │
│  (a) Generic output + buyer burns time babysitting / cleaning up    │
│      (T2 anchor — Q-045, Q-048, Q-051)                              │
│  (b) No conversation-state awareness — AI sends next-in-sequence    │
│      to prospects who already replied (T1 anchor — Q-049, Q-050)    │
│                                                                     │
│  Public-data signal (Layer A — start your list here):               │
│  → AI-SDR vendor logo (BuiltWith / customer-list scrape)            │
│  → Vendor adoption 60-90 days vintage                               │
│  → Open SDR/AE role (proves the AI didn't replace the human)        │
│  → Bonus Layer-B: cold-send audit of their actual threads to        │
│    surface conversation-state failures                              │
│                                                                     │
│  Cold-email anchor (WORKING DRAFT — Lucas to review):               │
│  > You bought [Vendor] ~75 days ago to scale outbound. You still    │
│  > have [N] SDR roles open. The math on "AI replaces the SDR"       │
│  > isn't playing out — and we audited 14 of your recent threads,    │
│  > the agent kept sending next-in-sequence after the prospect       │
│  > replied. Here's what the replacement playbook looks like.        │
│                                                                     │
│  Re-diagnosis hook:                                                 │
│  Buyer reads their pain as "the AI isn't good enough." Reframe      │
│  as "the AI doesn't have the data layer it needs to be specific."   │
│  This is the meta-EDP from Stage 2 Step 5 in action — pull them     │
│  back to data quality, not vendor selection.                        │
│                                                                     │
│  Why T1 was absorbed instead of shipped separately: same buyer,     │
│  same Layer-A signal (AI-SDR vendor logo), same core narrative      │
│  ("the AI didn't deliver what was sold"). Sub-failure-mode (b)      │
│  adds specificity to the cold-email anchor without justifying a     │
│  separate card.                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage 2.5 — Situations missing from this harvest pass (added 2026-05-12 post-consult)

> The first harvest pass keyed off tool names (Apollo, ZoomInfo, 11x, Clay). That produced tool-failure-shaped themes (the 6 in Stage 2). It missed *event-shaped* situations — the cut Jordan actually uses to segment. Cannonball segments construction by *Labor Capacity Trap* + *Start-Gate Stranglehold*, not by which software they own. [Cannonball · *The challenge for construction vertical SaaS* · The Two Other Segments]
>
> The 4 segments below are named candidates that need a second harvest pass (3P corroboration) before they can become full Stage-3 cards. They are HYPOTHESIS at this point — do not build Stage 4 / Stage 5 against them yet.

### S-A — "Just hired a VP Sales / CMO" (staffing-event trigger)
- **Situation:** new GTM leader, days 60-120 in seat, needs a visible methodology win before the honeymoon ends
- **Hypothesis EDP:** days-in-seat × current pipeline-coverage gap vs. plan
- **Hypothesis Layer-A signal:** LinkedIn job change in past 90d for VP Sales / CMO / Head of Sales at vertical SaaS Series A-B
- **VPP tier read:** Risk Mitigation (career-saving) + Growth (visible change)
- **Status:** named in thresh.md as Persona 3 trigger; needs Reddit/LinkedIn corroboration before promoting to Stage-3 card

### S-B — "Just raised Series A" (funding-event trigger)
- **Situation:** capital deployed in last 90d, board demands pipeline coverage in 90-180d
- **Hypothesis EDP:** time-since-funding × pipeline-coverage-vs-plan
- **Hypothesis Layer-A signal:** Series A announcement with "scale go-to-market" / "build out sales" language + 90d freshness window
- **VPP tier read:** Growth
- **Status:** in thresh.md ICP signal #4; needs 3P corroboration before promoting

### S-C — "Founder-led → team-led transition" (build-vs-buy crossroads)
- **Situation:** founder still doing demos, can't continue. At the crossroads — about to spend $200K on a GTME hire, $60K on an agency, or engage Thresh.
- **Hypothesis EDP:** founder-hours-on-demos × revenue-per-rep target gap
- **Hypothesis Layer-A signal:** founder LinkedIn activity shows active Calendly + recent Sales Engineer / GTME / SDR job post + LinkedIn HC < 20
- **VPP tier read:** Effectiveness (capability they don't have yet) + Risk Mitigation (don't burn a wrong hire)
- **Status:** in thresh.md ICP signal #5/#10; this is the **direct "Thresh vs in-house GTME hire vs agency" buyer**. Currently missing from the playbook entirely.

### S-D — "Burned by AI-SDR deliverability cliff" (failure-event sub-segment)
- **Situation:** AI-SDR vendor burned the sending domain. Cost-per-meeting blew from $35 to $150+. Sales-domain reputation damaged. (Distinct from T2's "AI is generic" — this is "the AI nuked our infrastructure.")
- **Hypothesis EDP:** cost-per-meeting trend × send-domain reputation score
- **Hypothesis Layer-A signal:** AI-SDR adoption + open SDR role + LinkedIn posts mentioning the burn (OR observable spam-folder behavior via cold-send test)
- **VPP tier read:** Risk Mitigation
- **Status:** partially covered by T2-merged; the deliverability-collapse specifically is its own existential anchor. Decide in next session whether to ship as a separate card or fold deeper into T2-merged.

### Note: separating Thresh-buyer signals from downstream-catalog signals
The current playbook also blurs two distinct signal layers. **Stage 3 = "what makes a company a Thresh buyer."** **Downstream Catalog (lives in thresh.md, FMCSA-Motus entry, etc.) = "what makes a vertical hot for a Thresh client's outbound."** These are different signal layers, used at different stages of the engagement. Next-session work: split explicitly.

---

## What's still TODO

**Deferred from this session (consult corrections beyond the structural fixes):**
- **Full taxonomy recut** from tool-category families to event-type families (staffing-event / funding-event / failure-event / external-event). Currently the painShape labels still organize Stage 2 — Jordan's cut is event-shaped. Next session.
- **Harvest pass 2 — situations not tools.** Targeted Reddit/LinkedIn pulls keyed on "new VP Sales" / "just raised" / "founder doing demos" / "AI-SDR burned our domain" — not on vendor names. Output: enough 3P corroboration to promote S-A, S-B, S-C, S-D from Stage-2.5 stubs to full Stage-3 cards (or kill them).
- **Split Stage 3 (Thresh-buyer signals) from Downstream Catalog (Thresh-client's-market signals)** as two distinct signal layers in the playbook. Currently blurred.

**Originally planned, still TODO:**
- **Stage 4 (Per-Segment Build)** — for each shipped card: list-build query, enrichment plan, sequencing shape, channel selection. Build generically AND with a T6 Thresh-worked example (T6 is the recommended Phase-0 first segment).
- **Stage 5 (Send + measure MBR)** — cadence, deliverability protection, MBR measurement spec.
- **Cold-email anchor review** — the working drafts on T6 + T2-merged need Lucas's pass before they're treated as real anchors. Rewrite to lead with the EDP, not the surface complaint.
- **Methodology-meta vocab extraction** — pull the 48 LinkedIn quotes into a phrase library for cold-email word-choice fuel (not a segment).

**Killed / dropped this session:**
- T3, T4 cards (failed Jordan's 3-gate trifecta + Value Prop Pyramid tier check). Cards preserved for the record.
- T5 (Clay credit-burn) — never shipped; fails EXISTENTIAL + Efficiency-tier read.
- Stack-fragmentation painShape — N=4 too low to ship without targeted harvest; deferred.

---

## Consult-driven changes log (2026-05-12)

The Stage 2 and Stage 3 drafts above went through two corpus consults against Jordan Crawford + Cannonball GTM. Surfaced findings and what changed:

### Applied this session (the 6 structural fixes)
1. Added the Cannonball 3-gate trifecta to Stage 2 Step 3 (NEW × EXISTENTIAL × IDENTIFIABLE). [Cannonball · *Brand Blitz* · What the Hell is a Pain-Based Segment?]
2. Added the Value Prop Pyramid tier check as the 4th gate (must read at Risk Mitigation or higher). [Cannonball · *The Cannonball Value Prop Pyramid*]
3. Re-ran T1-T6 through the 4-gate matrix; T3, T4, T5 fail; demoted T3 + T4 to PARKED with explicit reasoning. (T5 was already parked.)
4. Added Existential Data Point + VPP tier fields to T6 and T2-merged. [Cannonball · *A Quick and Dirty Guide* · Glossary]
5. Added Cannonball GTME-rename leader-corroboration line to T6. [Cannonball · *Why We're Changing from GTM Engineers to Revenue Growth Engineers*]
6. Added Stage 2.5 stub for S-A, S-B, S-C, S-D — event-shaped situations the tool-keyed harvest missed.

### Deferred (substantive but beyond a one-session fix)
- Recutting painShape families from tool-category to event-type
- Harvest pass 2 keyed on situations not tools
- Splitting Thresh-buyer signals from downstream-catalog signals
- Cold-email anchor rewrites to lead with EDP, not surface complaint
- Stage 0 adding a "Concentric Circle Test" 4th diagnostic axis (does Thresh sit dead-center of the segment's core challenge?)
- Adding GTM Maturity Stage 2 filter to Stage 1's input harvest. [Cannonball · *The 3 Stages of GTM*]

---

## Notes for next session

The 2 shipped segments (T6, T2-merged) plus the 4 stubbed candidate situations (S-A, S-B, S-C, S-D) are the working spine for Phase 0 trucking AND for the post-cohort general pitch. Recommended first segment to operationalize: **T6** — passes all 4 gates, has the cleanest detection signal (open GTME role 60+d), and now has leader-level corroboration from the Cannonball GTME-rename post. Phase 0 trucking can use T6 as the *qualification gate for who is a Thresh buyer*, separately from running FMCSA-anchored *downstream messaging* about the trucking client's own buyers' market. Don't conflate the two signal layers — that split is now an explicit next-session todo.
