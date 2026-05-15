# Thresh Painting Playbook — Lucas Internalize Doc

**Generated:** 2026-05-12 (third-pass companion to `playbook-redraw-2026-05-12.md` — added PQS/PVP tier split)
**Audience:** Lucas only. This is the internalize-first version. Generic methodology lives in `playbook-redraw-2026-05-12.md`; this doc is Thresh-specific application.
**Status:** T6 in flight (4-account PQS-tier smoke test pending reply data — measure vs ~7-10% bar, not 20%). T2-merged shipped but unmeasured. PVP upgrades for both not yet built. S-A, S-B, S-C, S-D stubbed. Stages 4-5 detail still TODO.

---

## What this is (one paragraph)

Thresh's own outbound playbook. **Painting** — because Thresh sits squarely on the painting side of the Stage 0 fork: vertical B2B SaaS ICP, ~2K-10K total TAM, existential clustered pain (burned hires, blown domains, board-pressure pipeline gaps), $20-50K ACV. Cannonball's own thresholds put Thresh in painting territory by every column. [Cannonball · *The Mass Market Arbitrage Playbook* · 2025-11-05] [Blueprint · *The Concentric Circle Test* · Layer 2]

The reference visuals floating around the AI-outbound discourse (4 inputs → ICP → Full TAM → Signals → Enrichment) describe Eric Nowoslawski's *printing* methodology — horizontal SaaS, 100K+ contact list-build, offer-arbitrage testing at 2-3% reply rate. **That's not this playbook.** If you ever feel pulled to draw a "Full TAM" node, you're being pulled toward the wrong methodology.

---

## The spine

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 1500" style="width:100%;max-width:1100px;height:auto;display:block;margin:0 auto;background:#0E0D1E">
  <defs>
    <style>
      .bg { fill: #0E0D1E; }
      .node { fill: #4A47C6; }
      .node-card { fill: #5854D1; }
      .text-title { fill: #FFFFFF; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 28px; font-weight: 700; text-anchor: middle; }
      .text-subtitle { fill: #B0AFBA; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; font-weight: 400; text-anchor: middle; }
      .text-node { fill: #FFFFFF; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 17px; font-weight: 600; text-anchor: middle; }
      .text-node-sm { fill: #E8E7F0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 13px; font-weight: 500; text-anchor: middle; }
      .text-layer { fill: #9E9CA8; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; font-weight: 400; text-anchor: end; }
      .connector { stroke: #5C5B6A; stroke-width: 1.5; fill: none; }
      .loop { stroke: #6F6D80; stroke-width: 1.5; stroke-dasharray: 5,4; fill: none; }
      .text-loop { fill: #9E9CA8; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 12px; font-weight: 400; font-style: italic; text-anchor: middle; }
    </style>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#5C5B6A" />
    </marker>
    <marker id="arrow-loop" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#6F6D80" />
    </marker>
  </defs>
  <rect class="bg" x="0" y="0" width="1400" height="1500" />
  <text class="text-title" x="700" y="75">The Thresh painting playbook</text>
  <text class="text-subtitle" x="700" y="105">Painting spine · vertical SaaS · existential pain · 20%+ reply bar</text>
  <text class="text-layer" x="140" y="204">Layer 0</text>
  <text class="text-layer" x="140" y="222">Route</text>
  <text class="text-layer" x="140" y="414">Layer 1</text>
  <text class="text-layer" x="140" y="432">Inputs</text>
  <text class="text-layer" x="140" y="679">Layer 2</text>
  <text class="text-layer" x="140" y="697">Synthesis</text>
  <text class="text-layer" x="140" y="919">Layer 3</text>
  <text class="text-layer" x="140" y="937">Cards</text>
  <text class="text-layer" x="140" y="1094">Layer 4</text>
  <text class="text-layer" x="140" y="1112">Execute</text>
  <text class="text-layer" x="140" y="1279">Layer 5</text>
  <text class="text-layer" x="140" y="1297">Measure &amp; loop</text>
  <rect class="node" x="460" y="170" width="480" height="80" rx="10" />
  <text class="text-node" x="700" y="215">Painting vs Printing fork</text>
  <path class="connector" d="M 700 250 L 700 295" />
  <path class="connector" d="M 340 295 L 1060 295" />
  <path class="connector" d="M 340 295 L 340 320" marker-end="url(#arrow)"/>
  <path class="connector" d="M 700 295 L 700 320" marker-end="url(#arrow)"/>
  <path class="connector" d="M 1060 295 L 1060 320" marker-end="url(#arrow)"/>
  <rect class="node" x="200" y="320" width="280" height="70" rx="10" />
  <text class="text-node" x="340" y="361">Reddit (HIGH)</text>
  <rect class="node" x="560" y="320" width="280" height="70" rx="10" />
  <text class="text-node" x="700" y="361">LinkedIn (MED)</text>
  <rect class="node" x="920" y="320" width="280" height="70" rx="10" />
  <text class="text-node" x="1060" y="361">G2 (LOW)</text>
  <path class="connector" d="M 340 390 L 340 425" />
  <path class="connector" d="M 700 390 L 700 425" />
  <path class="connector" d="M 1060 390 L 1060 425" />
  <path class="connector" d="M 340 425 L 1060 425" />
  <path class="connector" d="M 700 425 L 700 460" marker-end="url(#arrow)" />
  <rect class="node" x="460" y="460" width="480" height="70" rx="10" />
  <text class="text-node" x="700" y="501">3P pain corpus</text>
  <path class="connector" d="M 700 530 L 700 600" marker-end="url(#arrow)" />
  <rect class="node" x="460" y="600" width="480" height="70" rx="10" />
  <text class="text-node" x="700" y="641">Cluster by painShape</text>
  <path class="connector" d="M 700 670 L 700 720" marker-end="url(#arrow)" />
  <rect class="node" x="380" y="720" width="640" height="80" rx="10" />
  <text class="text-node" x="700" y="753">5-gate ship/park</text>
  <text class="text-node-sm" x="700" y="778">NEW × EXIST × IDENT × VPP × SIZE ≥ 100</text>
  <path class="connector" d="M 700 800 L 700 845" />
  <path class="connector" d="M 340 845 L 1060 845" />
  <path class="connector" d="M 340 845 L 340 880" marker-end="url(#arrow)" />
  <path class="connector" d="M 700 845 L 700 880" marker-end="url(#arrow)" />
  <path class="connector" d="M 1060 845 L 1060 880" marker-end="url(#arrow)" />
  <rect class="node-card" x="200" y="880" width="280" height="90" rx="10" />
  <text class="text-node" x="340" y="918">T6</text>
  <text class="text-node-sm" x="340" y="943">GTME hire didn't land</text>
  <rect class="node-card" x="560" y="880" width="280" height="90" rx="10" />
  <text class="text-node" x="700" y="918">T2-merged</text>
  <text class="text-node-sm" x="700" y="943">AI-SDR failure</text>
  <rect class="node-card" x="920" y="880" width="280" height="90" rx="10" />
  <text class="text-node" x="1060" y="918">Stubs</text>
  <text class="text-node-sm" x="1060" y="943">S-A · S-B · S-C · S-D</text>
  <path class="connector" d="M 340 970 L 340 1005" />
  <path class="connector" d="M 700 970 L 700 1005" />
  <path class="connector" d="M 1060 970 L 1060 1005" />
  <path class="connector" d="M 340 1005 L 1060 1005" />
  <path class="connector" d="M 340 1005 L 340 1040" marker-end="url(#arrow)" />
  <rect class="node" x="200" y="1040" width="280" height="90" rx="10" />
  <text class="text-node" x="340" y="1078">Per-segment</text>
  <text class="text-node" x="340" y="1102">list build</text>
  <path class="connector" d="M 480 1085 L 560 1085" marker-end="url(#arrow)" />
  <rect class="node" x="560" y="1040" width="280" height="90" rx="10" />
  <text class="text-node" x="700" y="1078">Verify +</text>
  <text class="text-node" x="700" y="1102">find contacts</text>
  <path class="connector" d="M 840 1085 L 920 1085" marker-end="url(#arrow)" />
  <rect class="node" x="920" y="1040" width="280" height="90" rx="10" />
  <text class="text-node" x="1060" y="1078">Send PQS first,</text>
  <text class="text-node" x="1060" y="1102">upgrade to PVP</text>
  <path class="connector" d="M 1060 1130 L 1060 1180 L 700 1180 L 700 1245" marker-end="url(#arrow)" />
  <rect class="node" x="460" y="1245" width="480" height="90" rx="10" />
  <text class="text-node" x="700" y="1283">Measure vs tier bar</text>
  <text class="text-node-sm" x="700" y="1308">PQS ~7-10% positive · PVP 20%+ positive</text>
  <path class="loop" d="M 940 1290 L 1320 1290 L 1320 495 L 940 495" marker-end="url(#arrow-loop)" />
  <text class="text-loop" x="1320" y="892" transform="rotate(-90 1320 892)">reply data → next harvest</text>
</svg>

**T6 callouts** (where the current Thresh run sits at each stage):
- **Stage 1:** 247 quotes harvested 2026-05-12 from Reddit/LinkedIn/G2
- **Stage 2:** clustered into T1-T6 painShapes; T6 + T2-merged passed gates 1-4; T6 below SIZE floor (4 accounts at current aperture)
- **Stage 3:** T6 card shipped with Founder + VP-Sales angle PVPs
- **Stage 4:** TheirStack pull (50 records) → 4 accounts verified → Prospeo email lookup (6/6 verified) → 4 final drafts at 2 accounts (Harper, Software Toolbox)
- **Stage 5:** sends pending; bar = 20%+ positive reply rate

---

## Why painting (one paragraph)

Run the four-column diagnostic against Thresh:

| Diagnostic axis | Painting requires | Thresh actual | Pass? |
|---|---|---|---|
| Total TAM | <5,000 | ~2K-10K vertical B2B SaaS | ✓ |
| Per-segment size | 100-2,000 | T6's aperture currently returns 4 (needs widening) | ✗ at aperture |
| ACV | any if pain is existential | $20-50K with existential pain | ✓ |
| Pain shape | existential, specific | T6 = burned hire $$ · T2 = domain rep · S-C = $200K wrong-hire | ✓ |
| Vertical/horizontal | niche vertical | vertical B2B SaaS | ✓ |
| Reply-rate bar | PQS ~7-10% · PVP 20%+ | matches Cannonball's two-tier methodology | ✓ |
| Method | pain-based PQS first → PVP upgrade | T6 + T2 anchors are PQS-tier today; PVP upgrades not yet built | ✓ (PQS) / TBD (PVP) |

Six of seven cleanly painting. The only fail is T6's *current aperture* being too tight — which is a knob to turn, not a verdict on the methodology. [Cannonball · *Mass Market Arbitrage* · When to Use This Methodology] [Blueprint · *Concentric Circle Test* · Layer 2]

---

## T6 — full walkthrough

This is the segment Thresh is currently running. Trace it stage-by-stage to internalize the playbook against an actual run.

### Stage 1 — Inputs (done 2026-05-12)
Harvested 247 quotes total across Reddit/LinkedIn/G2 keyed on AI-outbound and GTM-engineering tooling pain. Tagged by source-trust hierarchy (Reddit HIGH, LinkedIn MED, G2 LOW) and painShape family. Output: 3P corpus, 6 themes pre-cluster. Stored in `research/3p-pain-harvest.md`.

**Note:** 1P inputs (call recordings, closed-won analysis, customer interviews) are aspirational. They unlock once Thresh has 3-5 closed clients producing transcripts and notes. Until then, 3P is the only input — which is fine for painting at this stage of the company.

### Stage 2 — Synthesis (done 2026-05-12, revised twice)
Clustered into T1-T6 painShapes with strict-separation rule (never merge ai-sdr-collapse with data-quality with tool-underuse). Applied 4-gate then 5-gate ship/park (see generic doc Stage 2 Step 3).

- **T6 passed** gates 1-4 (NEW × EXISTENTIAL × IDENTIFIABLE × VPP-tier-≥-Risk-Mit)
- **T2-merged passed** all gates including a soft pass on SIZE (universe unmeasured but likely 500-2,000)
- **T1 absorbed** into T2-merged as a sub-failure-mode
- **T3, T4, T5 parked** (VPP-tier reads at Efficiency = unshippable)
- **T6 below SIZE floor** at current aperture (4 accounts) — flagged for aperture-widening

### Stage 3 — Card (see generic doc for full card content)
Card shipped with two cold-email anchor variants: Founder/CEO angle + VP-Sales/Head-of-Sales angle. Both lead with the Existential Data Point ("[Company]'s GTM Engineer role just hit [N] days open"). Both end with the playbook-CTA ("Want the playbook we shipped for [their vertical]?").

### Stage 4 — Execute (done 2026-05-12, partial)
- **Account discovery:** TheirStack query keyed on "GTM Engineer" / "Revenue Engineer" / "Growth Engineer" role open 60+ days → 50 raw records pulled
- **Per-account verification:** filtered to vertical-SaaS fits → 4 accounts after dropping Logicbroker (4-day vintage fails T6 thesis) and ici (Turkish, fails US ICP)
- **Contact discovery:** Prospeo email verification on 6 contacts → 6/6 verified
- **Final batch:** 4 drafts at 2 accounts (Harper × Dakotah Rice + Sebastian Correa; Software Toolbox × Michael Mcmahon + Win Worrall)
- **Software Toolbox nuance:** their JD is lifecycle marketing / HubSpot / demand-gen, not engineering-shape — drafts use marketing-tilted variant

### Stage 5 — Measure (pending)
Sends queued in `outbound/t6-test-batch-2026-05-12/SEND-READY.md`. **Measure against the tier-based bar — the current 4 anchors are PQS-tier, not PVP-tier**, so the right bar to measure against is **~7-10% positive reply (PQS), not 20%+ (PVP).** The SEND-READY doc currently says "<2% reply rate → T6 weakens" — that's the printing bar and is stale relative to this playbook. Update separately.

**The PQS / PVP distinction in plain words** (see generic playbook's "Tier-based messaging" section for full detail):
- **PQS** = a mirror of the prospect's situation. Your current anchors ("Your GTME role just hit [N] days open... most teams get stuck because [reason]") sit here. Easy to write. Reply target ~7-10% positive (1.5-2% meeting book per Cannonball's economics).
- **PVP** = independently valuable intelligence the prospect couldn't easily get themselves. Requires building a research artifact (named-competitor list, per-vertical benchmark, person directory, opportunity-cost math). Slow to write. Reply target 20%+ positive (4%+ meeting book).
- Stopping at PQS leaves 2-3x pricing power on the table. PVP is the upgrade you build AFTER PQS confirms the segment direction.

**What the 4-account batch actually is:** a PQS smoke test (does the mirror message land at all?), NOT segment validation (does this size-100+ universe convert?) and NOT PVP testing (does the upgraded intelligence-bearing anchor lift reply rate to 20%?).

**Decision tree on reply outcomes:**
- **PQS landing 7%+ across 4** → message direction validated. Two parallel next steps: (a) widen aperture (drop "vertical SaaS" → "all B2B SaaS"; drop "60+d" → "30+d") to reach 100-2,000 segment size; (b) build ONE of the PVP upgrade paths from the T6 card (named-competitor list is the easiest first build). Then run the PVP at the widened segment and measure against the 20% bar.
- **PQS landing <7% across 4** → mirror isn't tight enough. Re-craft the EDP-pull and angle. Do NOT widen aperture yet — wider distribution of a non-landing PQS just wastes credits. Do NOT skip ahead to building a PVP — if the PQS won't mirror, the PVP won't anchor either.
- **0 positive replies, multiple negative replies** → the diagnostic IS landing but the offer is wrong. Re-examine the VPP-tier read for this segment. Possible that "Effectiveness" tier is the wrong frame and Thresh actually reads at "Customer Satisfaction" for this buyer.
- **PQS landing 10%+ at proper aperture (100-2,000)** → build the PVP upgrade. Don't stop at PQS. 10% positive reply × no PVP upgrade leaves you in the 1.5-2% meeting-book band when the PVP could lift you to 4%+.
- **PVP landing 20%+ at proper aperture** → lock the segment. Run continuous send within its universe. Move energy to the next segment (T2-merged, then S-A).

---

## What "scale" looks like (the question Lucas asked)

> "I know we just executed some sort of play for the GTM-engineering role, but what does that look like at scale? Some other people blast a full TAM in 45 days — they put in filters and demographics and just spam the entire list, with signals turned on for tier-1 companies. That's basically how most companies are doing it today, and this is definitely different."

**Right — this IS definitely different. Scale here doesn't mean "more accounts in one list."** That's the Eric Nowoslawski / GEX printing model. It needs 100,000 contacts pre-cleanup, offer-arbitrage testing infrastructure, and a 2-3% reply rate target. Thresh's market doesn't have 100K contacts to feed that machine, and the existential pain Thresh's segments target doesn't surface through offer-arbitrage — it surfaces through pain-based PVPs.

**Scale for Thresh = N painted segments running in parallel, each sized into Jordan's 100-2,000 band.**

At steady state:
- T6 (GTME-role-didn't-pan-out) at widened aperture: ~500-1,500 accounts
- T2-merged (AI-SDR-isn't-delivering): ~500-2,000 accounts
- S-A (new VP Sales/CMO at vertical SaaS): ~500-2,000 accounts
- S-B (just raised Series A + "scale GTM" language): ~100-400 accounts
- S-C (founder-led → team-led transition): ~200-800 accounts
- S-D (AI-SDR deliverability burn, if separable): ~200-800 accounts

That's a steady-state pipeline of roughly **2,000-7,500 active painted accounts** across 6 parallel segments, each running its own PVP, each measuring against its own 20%+ reply bar, each getting locked/widened/killed independently. New segments get added when 3P harvest surfaces a new painShape that passes the 5-gate; old segments get retired when reply rate decays below 20% across two consecutive reply-validation cycles.

**Volume math, per segment, per month** (at PVP tier — the steady-state goal):
- 100-300 new sends from the segment's universe (limited by inbox warm-up + 9-inbox SmartLead rotation × 4 domains)
- Day-7 follow-up auto-queued for non-responders
- 20%+ positive reply × 20% reply→meeting conversion = **~4-12 booked meetings per segment per month**
- Across 6 segments at PVP-tier steady state: ~24-72 booked meetings per month

**At PQS tier (before PVP upgrade is built)** — useful for setting realistic Phase-0 expectations:
- 7-10% positive reply × 20% reply→meeting conversion = ~1.5-2% meeting book = **~1.5-6 booked meetings per segment per month**
- The PQS-to-PVP upgrade is the difference between "1-2 meetings/segment/month" and "4-12 meetings/segment/month." That's why building the PVP upgrade after PQS validates is non-optional.

That's painting. Not printing.

**Important nuance** — this scale model assumes Thresh has time + the inbox infrastructure to run 6 segments in parallel. In Phase 0 (Founding Cohort, 3 spots), Lucas is solo. Run 2 segments in parallel max until first cohort delivers and the operating model has proven out. T6 + S-A is the recommended pair (different painShapes, different buyer roles, won't cannibalize each other's send-domain budget).

---

## Current implementation — tool mapping

What each stage actually runs on today. Update on vendor swaps.

| Stage | What happens | Tools used today |
|---|---|---|
| Stage 1 — Harvest | 3P pull from Reddit / LinkedIn / G2; tag by painShape + source-trust | Apify (Reddit + LinkedIn scrapers) + Claude (clustering, tagging) |
| Stage 2 — Cluster | Strict-separation clustering, 5-gate scoring | Claude + manual review in `research/playbook-redraw-2026-05-12.md` |
| Stage 3 — Cards | Per-segment card authoring | Manual (Lucas) — cards live in `research/playbook-redraw-2026-05-12.md` |
| Stage 4 — List build | Signal-keyed account discovery per segment | TheirStack (job-post signals, BuiltWith logos) + Clay (enrichment) |
| Stage 4 — Verify | Per-account JD verification + ICP fit | Manual (Lucas) — careers-page visual verify + LinkedIn cross-check |
| Stage 4 — Contacts | Decision-maker identification + email verification | Prospeo (email verification + finding) |
| Stage 4 — Send | Cold-send via inbox rotation | SmartLead (9 inboxes × 4 domains) |
| Stage 5 — Measure | Reply tracking + reply-rate analysis | Manual (Lucas) — log in `outbound/sent-log.md`; reply outcomes in `outbound/pipeline.md` |
| Stage 5 — Loop | Reply data feeds next harvest's painShape priorities | Manual (Lucas) — quarterly review at minimum |

**Tools deliberately NOT in this stack:**
- AI-SDR tools (11x, Artisan, AiSDR, Regie.ai) — those are the *subject* of T2-merged, not the implementation. Using one would mean Thresh dogfooding the exact pain its T2 segment targets, which would land badly.
- Apollo / ZoomInfo for contact data — T3 and T4 (parked) explicitly diagnose those as untrustworthy for the painting bar. Prospeo + per-account verification is the right shape.
- Clay's sequencing features — Clay is good for enrichment, but the send path runs through SmartLead with handcrafted PVPs, not Clay-templated automation.

---

## What's TODO

In order of priority for next session:

1. **Wait for T6 4-account smoke-test reply data.** Apply the decision tree above. Treat the current anchors as PQS-tier (not PVP) — measure against ~7-10% positive reply bar, not 20%. Don't widen the aperture before reply data is in — wider distribution of a non-landing PQS wastes credits.
2. **If T6 PQS lands (≥7% positive reply):** widen aperture to 100-2,000 AND build ONE PVP upgrade from the card's PVP upgrade path. Named-competitor list is the easiest first build. Run the PVP at the widened segment and measure against the 20% bar.
3. **If T6 PQS lands <7%:** re-craft the EDP-pull and angle. Try the re-diagnosis hook as first-touch. Do NOT widen aperture or build a PVP yet.
4. **Harvest pass 2 — situations not tools.** Reddit/LinkedIn pulls keyed on "new VP Sales" / "just raised Series A" / "founder doing demos" / "AI-SDR burned my domain." Output: enough 3P corroboration to promote S-A through S-D from stubs to Stage-3 cards (or kill them). When promoting, write PQS anchors first; PVP upgrade paths come after.
5. **Build Stage 4 + Stage 5 detail in the generic playbook.** Per-segment list-build query, enrichment plan, sequencing shape, channel selection, MBR measurement spec.
6. **Validate T2-merged segment size.** Run a TheirStack pull keyed on AI-SDR vendor logos + 60-90d vintage + open SDR/AE role. Confirm hypothesis that universe lands in 500-2,000.
7. **Update `outbound/t6-test-batch-2026-05-12/SEND-READY.md`** to replace the printing-bar reply-rate threshold ("<2% → T6 weakens") with the tier-based bars (PQS ~7-10%, PVP 20%+). Separate pass.
8. **Split Thresh-buyer signals from Downstream Catalog signals** in the generic playbook — two distinct signal layers, currently blurred.

---

## Locked principles (carry forward across sessions)

- **Stage gates over asymmetry score alone.** All 5 gates: NEW × EXISTENTIAL × IDENTIFIABLE × VPP-tier-≥-Risk-Mit × SIZE-≥-100.
- **Source-trust hierarchy is non-optional.** Reddit HIGH · LinkedIn MED · G2 LOW. G2 never overrides Reddit.
- **Strict painShape separation during clustering.** Never merge across families.
- **Per-account verification REQUIRED before any send.** LinkedIn job postings persist after roles are filled or abandoned.
- **VPP tier ≥ Risk Mitigation** is the hardest gate. Efficiency-tier reads kill pricing power.
- **Tier-based reply bars (every shipped card carries both):**
  - **PQS anchor:** ~7-10% positive reply (1.5-2% meeting book). Mirror messages. Day-1 send.
  - **PVP anchor:** 20%+ positive reply (4%+ meeting book). Novel intelligence. Built after PQS validates segment direction.
  - <PQS bar = mirror isn't tight enough, re-craft. Don't skip ahead to PVP.
  - PQS bar hit but no PVP built = leaving 2-3x pricing power on the table.
- **Aperture is a knob, not a verdict.** If a segment is below the 100-floor, widen filters before declaring the segment dead. Aperture-widening happens BEFORE PVP-building, not after.
- **PQS vs PVP test** [Cannonball · *Battle of the Brands*]: if a competitor's prospect could write the same email about themselves with no research, it's a PQS, not a PVP. Be honest about which tier you're actually shipping.
