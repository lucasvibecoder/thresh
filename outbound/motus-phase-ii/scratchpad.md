# Scratchpad — Motus Phase II Outbound Activation

> **Execution working dir:** `/Users/lucas/Documents/projects/thresh/outbound/motus-phase-ii/`
> Before `/do execute`, cd into the campaign dir so all relative paths resolve.
>
> **Moved 2026-05-11:** originally under `gtm-alpha/runs/motus-phase-ii/` until end of session. Motus is Thresh's own outbound campaign, not a GTM Alpha client engagement — relocated to `thresh/outbound/` to match the naming convention (`gtm-alpha/runs/{client-domain}/` is reserved for client work).

## High-Level Goal

Go from "52 scrubbed factoring companies + final email draft" to "campaign loaded in SmartLead in draft state, 5 body variants assigned across 10 warmed inboxes, ready to launch Tue 5/12 or Wed 5/13 9am ET" — without re-litigating any decisions from `HANDOFF.md` or `outbound/cold-email-v1.md`.

The chain: AI Ark Pass 1 (Tier A credit/risk) → AI Ark Pass 2 (Tier B+C founder/CEO) → LeadMagic validation → variant generation → variant/inbox assignment → SmartLead dashboard config (Lucas in the loop) → hard stop at draft state.

**Excluded this cycle:** HubSpot push (not needed for first send; SmartLead handles lead + reply tracking on its own).

## Inbox inventory (9 sending inboxes, all warmed since ~2026-03-04)

| # | Inbox | Domain (DNS provider) |
|---|---|---|
| 1 | `lucas.l@threshworks.com` | Porkbun |
| 2 | `l@threshworks.com` | Porkbun |
| 3 | `lucas@threshworks.com` | Porkbun |
| 4 | `lucas.l@withthresh.com` | Porkbun |
| 5 | `l@withthresh.com` | Porkbun |
| 6 | `lucas@withthresh.com` | Porkbun |
| 7 | `lucas.l@threshhq.com` | Porkbun |
| 8 | `l@threshhq.com` | Porkbun |
| 9 | `lucas@threshhq.com` | Porkbun |

**Standing rule — cold outbound:** Send only from the 3 Porkbun lookalike domains (`threshworks.com`, `withthresh.com`, `threshhq.com`). Never from `runthresh.com` — that's the primary brand/website domain and must be insulated from cold-sending reputation risk. `lucas.linares@runthresh.com` (id 15888000) is excluded from this campaign and should be excluded from all future cold-outbound campaigns. It can remain in SmartLead for warmup and 1:1 reply purposes only.

**Amendment 2026-05-11:** Original scratchpad listed runthresh.com as inbox #10. Removed mid-execution after Lucas flagged the brand-domain risk. Campaign 3319888 has 9 inboxes attached.

## Deliverability rules (applied to this campaign)

- **Per-inbox cap on send day:** 20 emails max (well below the 25–30 industry-conservative ceiling).
- **Total daily capacity at the cap:** 9 × 20 = 180 sends. Actual list size: 14 contacts (LM-valid only). Massive headroom — 1.55 sends per inbox avg.
- **Brand domain excluded:** Cold outbound never fires from `runthresh.com`. See inbox-inventory section above.
- **Variant count:** 5 (matches Taylor Haren "5 email-1 variants" pattern). Same offer, same proof, different opener/angle/structure.
- **Variant ↔ inbox binding (amended 2026-05-11):** Consolidated to one campaign with 5 SmartLead native variants A-E + 9 attached inboxes. SmartLead distributes variants evenly across leads and rotates inboxes naturally. Sub-campaign architecture (originally planned, executed, then deleted) was over-engineered for 14-lead volume — anti-clustering rationale only pays rent at >5 sends/inbox/day.
- **Time-of-day:** SmartLead default 9am–5pm ET, 8 min gap between sends per inbox, weekdays only. Start: Tue 2026-05-12 9am ET.

## File Map

| Path | Action | Notes |
|---|---|---|
| `contacts/pass1-tier-a-credit-risk.json` | create | Raw `ai_ark_export_results` dump (Pass 1) |
| `contacts/pass2-tier-bc-founder-ceo.json` | create | Raw `ai_ark_export_results` dump (Pass 2) |
| `contacts/contacts-merged.csv` | create | Flattened across both passes, columns: `first_name,last_name,email,title,seniority,company_name,domain,linkedin_url,tier` |
| `contacts/contacts-validated.csv` | create | LeadMagic output — adds `email_status,email_confidence`; drop `invalid` + low-confidence `catch_all` rows |
| `contacts/contacts-final.csv` | create | Send-ready list; the file SmartLead consumes; adds `variant_id` + `assigned_inbox` columns |
| `outbound/variants/v1.md` … `v5.md` | create | 5 body variants, each with its own failure-mode scan |
| `outbound/variants/assignment-matrix.md` | create | Variant ↔ inbox map + per-cell expected send count |
| `contacts/smartlead-campaign-config.md` | create | Dashboard checklist + final pre-launch state snapshot (campaign ID, lead count, schedule) |
| `data/factoring-list-scrubbed.csv` | read-only | Source of truth for 52 companies + tiers |
| `outbound/cold-email-v1.md` | read-only | v1 master — subject + body — DO NOT MODIFY |
| `bench/curated-bench.md` | read-only | Reply ammo only; not used in this cycle |

## Low-Level Execution Steps

### Step 0 — Sanity check

```bash
cd /Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/
mkdir -p contacts outbound/variants
ls data/factoring-list-scrubbed.csv outbound/cold-email-v1.md
```

If either file missing, STOP.

### Step 1 — Confirm Tier B+C domain list

```bash
awk -F',' 'NR>1 && ($1=="B" || $1=="C") {print $2}' data/factoring-list-scrubbed.csv > contacts/tier-bc-domains.txt
wc -l contacts/tier-bc-domains.txt   # must be 41
```

If not 41, STOP.

### Step 2 — AI Ark Pass 1 (Tier A credit/risk, 11 cos)

**Amendment 2026-05-11:** Every `contact.title` filter shape (FUZZY/EXACT, array of strings, objects with text/keyword/include) returned 422 — AI Ark's published JSON schema is hollow at `any`/`all` and the API does opaque downstream validation. Dropping `contact.title` from the API call. Title filtering moved to Step 7 (Python regex on returned `title` field). Cost: ~$1/run in discarded rows. Worth it for determinism.

```bash
deepline tools execute ai_ark_export_people --payload '{
  "page": 0,
  "size": 50,
  "webhook": "https://runthresh.com/webhooks/ai-ark-noop",
  "account": {
    "domain": {"any": {"include": ["factorloads.com", "compassfs.net", "tbsfactoring.com", "summar.com", "rivierafinance.com", "bobtail.com", "singlepointgroup.com", "commercialfund.com", "corpbill.com", "bigthinkcapital.com", "farwestcapital.com"]}}
  },
  "contact": {
    "seniority": {"any": {"include": ["c_suite", "vp", "director"]}}
  }
}'
```

Capture returned `trackId`. We poll regardless — webhook delivery is unused.

**Amendment 2026-05-11:** webhook URL must NOT be a public request bin (webhook.site) — AI Ark pushes full PII payload to whatever URL is supplied, and a public bin leaks the contact list. Use a non-routable path on a Lucas-owned domain — `https://runthresh.com/webhooks/ai-ark-noop` — provider gets 404 trying to push, polling pulls results, PII stays in our stack.

### Step 3 — Poll Pass 1

```bash
deepline tools execute ai_ark_export_statistics --payload '{"trackId": "<PASS1_TRACK_ID>"}'
```

Loop with ~30s gaps until `state: "DONE"`. If `FAILED`, STOP.

### Step 4 — Fetch Pass 1 results

```bash
deepline tools execute ai_ark_export_results --payload '{"trackId": "<PASS1_TRACK_ID>", "page": 0, "size": 50}' > contacts/pass1-tier-a-credit-risk.json
```

Paginate if `totalCount > 50`. Expect 25–30 contacts.

### Step 5 — AI Ark Pass 2 (Tier B+C founder/CEO, 41 cos)

```bash
DOMAINS_JSON=$(jq -R . contacts/tier-bc-domains.txt | jq -s -c .)
deepline tools execute ai_ark_export_people --payload "{
  \"page\": 0,
  \"size\": 200,
  \"webhook\": \"https://runthresh.com/webhooks/ai-ark-noop\",
  \"account\": {\"domain\": {\"any\": {\"include\": $DOMAINS_JSON}}},
  \"contact\": {
    \"seniority\": {\"any\": {\"include\": [\"c_suite\"]}}
  }
}"
```

(Amendment: same title-filter removal as Step 2; seniority narrowed to `c_suite` for Tier B+C since we want founders/CEOs only, not VPs/directors. Title regex applied in Step 7.)

### Step 6 — Poll + fetch Pass 2

```bash
deepline tools execute ai_ark_export_statistics --payload '{"trackId": "<PASS2_TRACK_ID>"}'
# loop until DONE
deepline tools execute ai_ark_export_results --payload '{"trackId": "<PASS2_TRACK_ID>", "page": 0, "size": 50}' > contacts/pass2-tier-bc-founder-ceo.json
```

Expect 25–35 contacts.

### Step 7 — Merge + flatten to CSV

Inline Python (`contacts/merge.py`) that:
- Reads both raw CSVs (AI Ark returns JSON-embedded CSV, not pure JSON)
- Parses JSON-in-cell columns: `profile`, `email`, `company`, `department`, `link`
- Joins each contact to its company tier via email-domain → row in `data/factoring-list-scrubbed.csv`
- Title regex filter per tier (amended 2026-05-11):
  - **Tier A:** `credit|risk|underwrit|portfolio|collections|chief financial|cfo|chief operating|coo|chief executive|ceo|president|vp.*finance|vp.*operations|controller` — broader than original because mid-market factors don't carry dedicated "credit/risk" titles; credit decisions sit with CFO/COO/President at this scale, same buyer register for the email message
  - **Tier B+C:** `founder|co.?founder|ceo|chief executive|president|owner|managing partner|managing director` (unchanged)
- Anti-pattern reject: `sales|marketing|business development|bdr|sdr|recruit|hr` (these are NOT credit decision-makers, regardless of seniority)
- Emits `contacts/contacts-merged.csv` with columns: `first_name,last_name,email,title,seniority,company_name,domain,linkedin_url,tier,email_status,email_sub_status,domain_type,source_pass`
- Drops rows with missing email, missing first_name, or `email_status==INVALID`
- Preserves AI Ark's email validation columns for Step 8 decision (LeadMagic may be redundant — AI Ark already classifies SMTP/CATCH_ALL/INVALID)
- Dedupes by email (keep first)

### Step 8 — LeadMagic email validation

```bash
python3 contacts/validate.py
```

LeadMagic returns one row per call (no batch endpoint). 32 calls, ~$0.29 total. Appends `lm_status` + `lm_message` + `lm_mx_provider` columns → `contacts/contacts-validated.csv`.

**Result 2026-05-11:** LM ran across 32 contacts → 14 valid, 12 unknown (probe inconclusive on catch-all domains), 6 invalid. **Decision (Lucas, strict policy):** keep LM-valid only. Final send list = 14 contacts. This trades volume for inbox-health certainty — under the original ≥30 AC but consciously chosen given that 4 of 10 warmed inboxes are first-production this cycle. The acceptance criterion is amended to ≥14 send-ready rows.

Output → `contacts/contacts-validated.csv` includes only LM-valid rows.

### Step 9 — Generate 5 body variants

Source: `outbound/cold-email-v1.md` is v1 (the master). Generate v2–v5 in `outbound/variants/v2.md` … `v5.md`.

**Constraints — apply to every variant:**
- Same offer (public-signal monitoring for factoring credit/risk leads)
- Same proof point (20% stat, FMCSA Census methodology) — **but each variant renders the stat in a different surface form** to defeat spam-filter clustering on verbatim strings. See "Stat rendering" below.
- Same word count band (75–100)
- Same single CTA shape ("low-friction question — want me to show you?")
- All 8 failure modes from `~/.claude/skills/cold-email-craft/SKILL.md` re-scanned per variant
- Subject line varies per variant (still lowercase, 3–6 words, no punctuation)

**Stat rendering — every variant uses a DIFFERENT surface form of the same fact:**
- **v1:** `Roughly 20% of US carriers with active FMCSA operating authority...` (existing master phrasing)
- **v2:** `About 1 in 5 active-authority carriers...`
- **v3:** `Roughly a fifth of carriers with active FMCSA operating authority...`
- **v4:** `Over 130,000 active-authority carriers...` (raw count from methodology — 136,498)
- **v5:** `Twenty percent of carriers operating under active FMCSA authority...`

Underlying number (20.07% / 136,498 of 680,056) and methodology citation stay identical across all variants. Only the surface string changes. If the failure-mode scan flags the rendered form as awkward in any variant, swap for another non-overlapping rendering — never collapse two variants onto the same surface form.

**Variant axes — pick a different lever per variant:**
- **v1** (existing): lead with launch date → symptom → stat → what I do → CTA
- **v2**: lead with the stat → trigger → what I do → CTA
- **v3**: lead with the question form ("how does your team flag stale-MCS-150 carriers today?") → trigger → what I do
- **v4**: 60-word stripped version → trigger + stat + what I do + CTA, no second clause anywhere
- **v5**: lead with the "default risk reads as" reframing → trigger → stat → CTA

For each variant: copy the v1 file structure (Subject / Body / Methodology citation / Reply ammo pointer / Failure-mode scan / Decisions log) so every variant carries its own audit trail.

If any variant fails the failure-mode scan, STOP and surface — do not ship a broken variant just to hit 5.

### Step 10 — Variant × inbox assignment matrix

Write `outbound/variants/assignment-matrix.md` with this layout (10 inboxes, 5 variants, 2 inboxes per variant — one Porkbun-trio domain rotated, plus runthresh.com distributed across variants):

| Variant | Inbox A | Inbox B |
|---|---|---|
| v1 | `lucas.l@threshworks.com` | `lucas.l@withthresh.com` |
| v2 | `l@threshworks.com` | `l@withthresh.com` |
| v3 | `lucas@threshworks.com` | `lucas@withthresh.com` |
| v4 | `lucas.l@threshhq.com` | `lucas.linares@runthresh.com` |
| v5 | `l@threshhq.com` | `lucas@threshhq.com` |

Then assign contacts to (variant, inbox) cells:
- Shuffle the deduped contacts-validated list deterministically (sort by `domain` then `email` for reproducibility, then round-robin allocate)
- Each cell gets `floor(N/10)` contacts; remainder distributed v1 → v5 in order
- Append `variant_id` (v1–v5) and `assigned_inbox` (full email address) columns → `contacts/contacts-final.csv`

Sanity check before saving: no inbox gets >20 contacts. If it does, STOP — list size estimate was wrong; revisit variant assignment math.

### Step 11 — SmartLead dashboard checklist (human-in-the-loop)

Generate `contacts/smartlead-campaign-config.md` as a step-by-step checklist for Lucas to execute in the SmartLead UI. The checklist must enumerate:

1. **Create campaign** named `Motus Phase II — Factoring` (or similar; Lucas picks final name).
2. **Lead upload**: upload `contacts/contacts-final.csv` segmented by variant — SmartLead handles per-sequence lead lists, so create 5 sub-campaigns OR use a single campaign with conditional logic per `variant_id`. Default: 5 sub-campaigns (simpler, no SmartLead-side conditional). Each sub-campaign uploads its own slice of the CSV filtered by `variant_id`.
3. **Per-sub-campaign sequence**: 1 email only — pull subject + body verbatim from the corresponding `outbound/variants/v{N}.md`.
4. **Inbox assignment per sub-campaign**: assign the 2 inboxes per the matrix above. Disable inbox rotation across sub-campaigns (each sub-campaign uses only its 2 assigned inboxes).
5. **Schedule per sub-campaign**: Mon-Fri only, 9am–5pm ET, 8 min gap, daily cap **20** per inbox.
6. **Launch date**: Tue 2026-05-12 or Wed 2026-05-13, 9am ET start.
7. **Verify merge tags resolve** on test row preview for each sub-campaign — no literal `{{first_name}}` in preview.
8. **Confirm no follow-up step** configured anywhere — one email only this cycle.
9. **Snapshot pre-launch state** into the same `smartlead-campaign-config.md` file: campaign IDs, sub-campaign IDs, total lead count per sub-campaign, schedule visualization, screenshot path (Lucas exports from SmartLead UI).

Hard stop at draft. Do not push the "Launch" button.

### Step 12 — Pre-launch verification (executed by Lucas before clicking Launch)

```
- [ ] contacts/contacts-final.csv row count = sum of 5 sub-campaign lead counts
- [ ] All 10 inboxes show "active" in SmartLead account list
- [ ] Each sub-campaign uses ONLY its 2 assigned inboxes (cross-check against matrix)
- [ ] Test-row preview for each variant: merge tags resolve, body matches the source v{N}.md exactly
- [ ] Subject lines are lowercase, no period, 3–6 words, one per variant
- [ ] Schedule shows Tue 5/12 or Wed 5/13 launch with daily cap 20 per inbox
- [ ] No auto-follow-up step in any sub-campaign
```

If all checked, Lucas launches. After launch, MEMORY.md gets an update with launch timestamp + per-variant lead count + initial inbox health snapshot.

## Acceptance Criteria

- [ ] `contacts/contacts-final.csv` exists with ≥30 verified-email rows; every row has `variant_id` + `assigned_inbox`
- [ ] Tier A rows hold credit/risk titles only; Tier B+C rows hold founder/CEO titles only (no cross-contamination)
- [ ] `outbound/variants/v2.md` through `v5.md` exist; each has its own failure-mode scan and intentional-decisions log
- [ ] `outbound/variants/assignment-matrix.md` exists and matches the 10-inbox / 5-variant layout above
- [ ] `contacts/smartlead-campaign-config.md` exists with the 9-item dashboard checklist completed up to (but not including) launch
- [ ] No SmartLead sub-campaign exceeds 20 sends per inbox per day
- [ ] All 5 sub-campaigns exist in SmartLead in **draft** state — no live sends
- [ ] HubSpot is NOT touched this cycle (explicit out-of-scope confirmation)

## Out of Scope

- **HubSpot push** — explicitly excluded. Reply tracking lives in SmartLead this cycle. Backfill to HubSpot is a later cycle if reply rate warrants.
- **Do not edit `outbound/cold-email-v1.md`.** v1 is the master; variants live in `outbound/variants/`.
- **Do not edit `bench/curated-bench.md`.** Reply ammo only.
- **Do not draft Email 2 (post-5/18 follow-up).** Separate cycle after Motus launches.
- **Do not chase Tier 1 factors** (RTS, Apex, OTR, Triumph, eCapital).
- **Do not add sales-title personas** to either AI Ark pass.
- **Do not click "Launch" in SmartLead.** Hard stop at draft. Lucas launches manually.
- **Do not commit / push** the new `contacts/` files unless Lucas asks. `contacts/` may want a `.gitignore` entry.
- **Do not re-litigate the pivot** from compliance/ELD ICP to factoring.
- **Do not waterfall** missing contacts (no Apollo/Crustdata fallback). If AI Ark returns 0 for a company, mark `no_contact` and move on.
- **Do not ship a variant that fails the failure-mode scan.** Better 4 clean variants than 5 with one weak link.
- **Do not generate variants that change the offer** (public-signal monitoring) or the proof (20% stat) — only the surface form rotates.
- **Do not modify any file in `data/` or `bench/` or `outbound/cold-email-v1.md`.** Read-only this cycle.
