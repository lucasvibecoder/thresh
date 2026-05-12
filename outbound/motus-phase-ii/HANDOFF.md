# Motus Phase II — Handoff (paste this into next session)

Started 2026-05-11. Session pivoted from compliance/ELD SaaS ICP → trucking factoring companies. Stat + bench + list all built. Ready for AI Ark contact finding + SmartLead setup + send Tue 5/12 or Wed 5/13.

---

## Where things stand

**The trigger:** FMCSA Motus (new registration system) launches May 18; legacy retires May 14. Carriers with stale MCS-150s, officer mismatches, or authority discrepancies will fail business verification and show up in public FMCSA records as flagged. Pre-launch send window = Tue 5/12 or Wed 5/13 (avoid 5/14 cutover; 5/15+ swallowed by launch noise).

**The pivot:** Compliance/ELD SaaS (original ICP 1) was the wrong target — those companies are FMCSA-native, would read the pitch as "selling sand at the beach." Pivoted to trucking factoring companies. Factoring credit/risk leaders are non-FMCSA-native and read carrier-failure signals as direct default-risk indicators against their book of advances.

**The stat:** 20.07% of US carriers with active FMCSA operating authority have MCS-150s past the 24-month update window. Computed via Socrata SoQL aggregate queries on FMCSA Census file (no full 1.4GB download needed). In the 8–25% defensibility band. Methodology + verification queries in `data/stat-summary.md`.

**The list:** 52 US trucking factoring companies, tier-labeled, scrubbed from 200-row Discolike export. Tier A (51–200 emp, n=11), Tier B (11–50 emp + sim ≥92, n=21), Tier C (1–10 emp + sim ≥92, n=20). Scrubbed list at `data/factoring-list-scrubbed.csv`. Dropped rows (audit trail) at `data/factoring-list-dropped.csv`.

**The email (final, ~85 words):**
```
Subject: motus may 18

{{first_name}} - Motus launches May 18. Carriers with stale MCS-150s,
officer mismatches, or authority discrepancies will start failing FMCSA
business verification and showing up in public records as flagged.

Roughly 20% of US carriers with active FMCSA operating authority have
MCS-150s past the 24-month update window — the most common of these gaps.

I pull public signals and flag the matches. For factoring, that reads
as early warning on default risk before it hits your book.

Want me to show you what it looks like?

Lucas
```
Full draft + failure-mode scan + intentional-decisions log at `outbound/cold-email-v1.md`.

**The bench (reply ammo, not body):** 8 curated carriers (DOT#, state, MCS-150 vintage 10–22 years stale) at `bench/curated-bench.md`. Use only when recipient replies "like what?" — never in body. Pre-pulled from FMCSA Census via the same Socrata endpoint.

---

## What's left to do (start here in new session)

### 1. AI Ark contact finding via Deepline (~25–35 credits, ~$15–25)

`ai_ark` is a Deepline-exposed provider. Use `ai_ark_export_people` (bulk async w/ verified emails) — Path A in `/Users/lucas/.claude/skills/deepline-gtm/provider-playbooks/ai_ark.md`.

**Pass 1 — Tier A credit/risk personas (n=11 cos, expect ~25–30 contacts):**
```json
{
  "account": {
    "domain": {"any": {"include": ["factorloads.com", "compassfs.net", "tbsfactoring.com", "summar.com", "rivierafinance.com", "bobtail.com", "singlepointgroup.com", "commercialfund.com", "corpbill.com", "bigthinkcapital.com", "farwestcapital.com"]}}
  },
  "contact": {
    "title": {"any": {"include": {"mode": "FUZZY", "content": ["Chief Credit Officer", "VP Credit", "Head of Underwriting", "Director of Underwriting", "Head of Risk", "Director of Portfolio Risk", "Head of Portfolio Risk"]}}},
    "seniority": {"any": {"include": ["c_suite", "vp", "director", "head"]}}
  }
}
```

**Pass 2 — Tier B+C founder/CEO (n=41 cos, expect ~25–35 contacts):**
Same shape, but with all 41 Tier B+C domains in `account.domain.any.include`, and contact title FUZZY: `["Founder", "Co-Founder", "CEO", "President", "Owner"]`, seniority: `["c_suite", "owner", "founder"]`.

Domains list available by reading `data/factoring-list-scrubbed.csv` and filtering on `TIER == "B" OR TIER == "C"`.

**Excluded personas (do NOT include in either pass):** Head of Sales, VP Sales, CRO. They chase origination volume and will misroute this risk-monitoring pitch.

**Output:** CSV with verified emails. Diff against scrubbed list → which cos returned 0 contacts → Deepline waterfall (Apollo → Crustdata → LeadMagic) to fill gaps.

### 2. Email verification pass
LeadMagic via Deepline (`leadmagic_email_validation`) on full contact list before SmartLead push. Drop anything that comes back as "invalid" or "catch_all" with low confidence.

### 3. HubSpot push (MCP)
- Companies: push all 52 (or kept subset after contact-finding) with TIER label as a custom property
- Contacts: push all verified contacts associated to their companies
- Clean CRM record before any replies arrive
- HubSpot MCP already connected (Hub ID 245333171 per project MEMORY.md)

### 4. SmartLead campaign setup
- 9-inbox rotation across runthresh.com / threshhq.com / withthresh.com / threshworks.com (per project MEMORY.md)
- Weekday only, 8-min gap, daily cap ~30 sends per inbox
- Merge tags: `{{first_name}}`, `{{company_name}}`
- Campaign in draft state with merge tags resolving on a test row before launch

### 5. Send window
- **Target: Tue 2026-05-12 9am ET** or **Wed 2026-05-13 9am ET**
- Avoid Thu 5/14 (legacy-system cutover day, credit teams heads-down)
- Avoid Fri 5/15+ (swallowed by launch noise)

### 6. Post-May 18 follow-up (Email 2, draft after launch)
Threaded reply with live flagged-carrier data once Motus launches and the real flagged list surfaces in FMCSA records. Reuse the bench infrastructure. Draft separately after 5/18.

---

## Reply layer (when responses come in)

**If "interesting, like what?"** → drop 2–3 carriers from `bench/curated-bench.md` in-thread with the framing from that file's "How to deploy in a reply" section.

**If "we could build this ourselves"** → push back with one question: "what's your refresh cadence on book-wide MCS-150 checks today?" Most non-Tier-1 factors only check at application time, not continuously. If they confirm continuous monitoring exists, walk — they're rare and you're not adding value.

**If "send the list"** → ask for region or fleet-size band they cover (don't ask for their book). Run the Socrata query against that band + return 20–30 named carriers in 24 hours.

**Methodology citation (use only if asked):** "FMCSA Company Census File pulled 2026-05-11. Filtered to carriers with STATUS_CODE='A' and at least one active operating-authority docket — 680,056 carriers. 136,498 of those have MCS-150 dates older than 24 months. 20.07% stale."

---

## Files in this campaign run

```
runs/motus-phase-ii/
├── HANDOFF.md (this file)
├── data/
│   ├── analyze.py (full-CSV approach — UNUSED, kept for reference if Census ever needs offline analysis)
│   ├── scrub-discolike.py (the scrubber, reusable for next campaign)
│   ├── stat-summary.md (methodology + 3-universe results + decision rationale)
│   ├── factoring-list-scrubbed.csv (52 rows, tier-labeled, AI-Ark-ready)
│   └── factoring-list-dropped.csv (148 rows w/ drop reasons — audit trail)
├── bench/
│   ├── curated-bench.md (8 named carriers, reply ammo only, deployment instructions)
│   └── raw-candidates.csv (100-row pool from Socrata query, for future bench refresh)
└── outbound/
    └── cold-email-v1.md (final email draft + failure-mode scan + intentional-decisions log)
```

---

## Decisions intentionally NOT taken (don't re-litigate)

- **No named carrier in email body.** Scale tell at 50–100 send volume + false-positive-against-recipient's-book risk + 60–90 min per regional variant. Reply layer only.
- **No combined-signal claim** in the 20% stat. Officer mismatches require brittle state SoS scraping (half-day work, 50 state systems). Cited single-field stat (stale MCS-150s) and framed as "the most common of these gaps."
- **No "at scale" phrasing** — vendor-y register break. Replaced with "flag the matches."
- **No Tier 1 factors** (RTS, Apex, OTR, Triumph, eCapital). They have internal risk analytics teams and would dismiss the offer as "we already do this." Size filter ($20M–$200M / 1–200 emp) removed them automatically — this is a feature, not a bug.
- **No sales-title personas.** Head of Sales / VP Sales / CRO at factoring shops chase origination volume; risk-monitoring pitch misroutes. Credit/risk only.

---

## Related project memory

- `~/.claude/projects/-Users-lucas-Documents-projects-thresh/memory/MEMORY.md` — see "Motus Phase II — Compliance/ELD SaaS" entry (note: now stale — pivoted to factoring this session)
- `~/.claude/plans/parallelize-the-stat-cozy-crescent.md` — original parallelized plan (Tue 5/12 or Wed 5/13 send target, defensible MCS-150 stat methodology, named-bench scoping)
- Failure-mode memory at `~/.claude/projects/-Users-lucas-Documents-projects-thresh/memory/feedback_outbound_*.md` — applies to all email drafts in this campaign
