# SmartLead Campaign Config — Motus Phase II / Factoring

**Status:** Draft until Lucas clicks Launch (Tue 2026-05-12 or Wed 2026-05-13)
**Total send-list size:** 14 contacts (LM-valid only)
**Structure:** 5 sub-campaigns, one per variant (v1–v5)
**Launch window:** 9am ET start, Mon-Fri schedule, 9am–5pm window, 8 min gap

---

## Pre-flight: source files

| File | Purpose |
|---|---|
| `contacts/contacts-final.csv` | The send list — already has `variant_id` + `assigned_inbox` columns |
| `outbound/cold-email-v1.md` | v1 subject + body (master) |
| `outbound/variants/v2.md` … `v5.md` | v2-v5 subject + body |
| `outbound/variants/assignment-matrix.md` | Variant ↔ inbox map (the canonical source) |

---

## Step-by-step dashboard checklist

### 1. Create the parent campaign

- [ ] In SmartLead, **Campaigns → Create new** → name it `Motus Phase II — Factoring (v1-v5)` (or your preferred final name)
- [ ] Mark it private to your account / team if relevant

### 2. Pre-segment the CSV (off-platform, before upload)

The 5 sub-campaigns each need their own filtered slice of `contacts-final.csv`. Pre-export 5 mini-CSVs:

```bash
cd /Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii
for v in v1 v2 v3 v4 v5; do
  python3 -c "
import csv
with open('contacts/contacts-final.csv') as f, open('contacts/leads-$v.csv','w',newline='') as out:
    rows = [r for r in csv.DictReader(f) if r['variant_id']=='$v']
    if rows:
        w = csv.DictWriter(out, fieldnames=rows[0].keys()); w.writeheader()
        for r in rows: w.writerow(r)
        print(f'$v: {len(rows)} contacts')
"
done
```

Expected:
- `leads-v1.csv`: 3 rows
- `leads-v2.csv`: 3 rows
- `leads-v3.csv`: 3 rows
- `leads-v4.csv`: 3 rows
- `leads-v5.csv`: 2 rows

### 3. Create 5 sub-campaigns (one per variant)

For each variant N in (1, 2, 3, 4, 5):

- [ ] **Create sub-campaign** named `Motus Phase II — vN`
- [ ] **Upload leads:** `contacts/leads-vN.csv`
  - SmartLead auto-detects columns. Confirm `first_name`, `email`, `company_name` map correctly. Merge tag is `{{first_name}}`.
- [ ] **Sequence:** 1 email only. **No follow-up step.**
  - Subject: paste from `outbound/variants/vN.md` (or `cold-email-v1.md` for v1)
  - Body: paste from same file (the fenced code block under `## Body`)
  - Confirm preview resolves `{{first_name}}` on a test row — no literal `{{first_name}}` anywhere in rendered output
- [ ] **Sending accounts:** assign the 2 inboxes per the assignment matrix:
  - v1 → `lucas.l@threshworks.com` + `lucas.l@withthresh.com`
  - v2 → `l@threshworks.com` + `l@withthresh.com`
  - v3 → `lucas@threshworks.com` + `lucas@withthresh.com`
  - v4 → `lucas.l@threshhq.com` + `lucas.linares@runthresh.com`
  - v5 → `l@threshhq.com` + `lucas@threshhq.com`
- [ ] **Inbox rotation:** enabled within the sub-campaign (across the 2 assigned inboxes)
- [ ] **Schedule:**
  - Days: Mon-Fri only
  - Window: 9:00 AM – 5:00 PM **ET**
  - Gap between emails per inbox: **8 min**
  - Daily cap per inbox: **20** (huge headroom — actual sends per inbox = 1-2)
- [ ] **Tracking:** open tracking ON, click tracking OFF (avoid trackable-link spam-filter penalty for a 1-email cold)
- [ ] **Stop conditions:** reply detection ON (auto-stop sequence on reply — irrelevant for 1-email but enable anyway)

### 4. Per-sub-campaign verification (executed before clicking Launch)

For each sub-campaign N:

- [ ] Lead count in SmartLead matches `leads-vN.csv` row count
- [ ] Test-row preview shows the right subject + body from `vN.md`
- [ ] Only the 2 assigned inboxes are linked (cross-check assignment-matrix.md)
- [ ] No follow-up step is configured
- [ ] Schedule shows Tue 5/12 OR Wed 5/13 as the launch date with 9am ET start
- [ ] Subject line is lowercase, no period, 3-6 words

### 5. Pre-launch snapshot (recorded 2026-05-11 ET, consolidated)

**Architecture change 2026-05-11:** Original 5-sub-campaign architecture (campaigns 3319867, 3319878, 3319879, 3319880, 3319881) was over-engineered for 14-lead volume — at 1.4 emails per inbox, anti-clustering rationale didn't pay rent. Deleted the 5 sub-campaigns and consolidated into one campaign with 5 SmartLead native variants (which is what SmartLead's variant feature was designed for).

```
Campaign:        Motus Phase II — Factoring
Campaign ID:     3319888
Status:          DRAFTED
Inboxes:         10 attached (all warmed threshworks/withthresh/threshhq + runthresh)
Variants:        5 under sequence step 1
  variant A (was v1):  subject "motus may 18"
  variant B (was v2):  subject "about 1 in 5 carriers"
  variant C (was v3):  subject "stale mcs 150 question"
  variant D (was v4):  subject "may 18 fmcsa cutover"
  variant E (was v5):  subject "default risk early warning"
Leads:           14 pushed (all LM-valid)
Schedule:        Mon-Fri 09:00-17:00 America/New_York, 8min gap, 20/day cap
Start time:      2026-05-12 09:00 ET (Tue)
Tracking:        open ON, click OFF, stop-on-reply ON
Follow-up:       none (0%)
```

SmartLead distributes variants A-E across the 14 leads automatically (~2-3 leads per variant) and rotates inboxes naturally across all 10 attached. Stats split per-variant in the dashboard.

To launch: open campaign 3319888 in SmartLead, click "Review and Launch."

### 6. Hard stop

- [ ] Launch button **NOT** pressed
- [ ] Sub-campaigns left in **Draft** state for Lucas's final review
- [ ] Lucas signs off → clicks Launch manually

### 7. Post-launch update (after Lucas clicks Launch)

Update `~/.claude/projects/-Users-lucas-Documents-projects-gtm-alpha/memory/MEMORY.md` (or wherever the run log lives) with:
- Launch timestamp
- Per-variant lead count + first-hour open/reply rate
- Initial inbox health snapshot (any soft bounces / spam complaints)

---

## Out-of-scope reminders (per scratchpad)

- ✗ HubSpot push — reply tracking lives in SmartLead this cycle
- ✗ Email 2 / follow-up step — separate cycle after Motus launches 2026-05-18
- ✗ Editing `cold-email-v1.md` — v1 is the master, frozen
- ✗ Editing `bench/curated-bench.md` — reply ammo only
- ✗ Clicking Launch — Lucas does this manually after the verification pass
