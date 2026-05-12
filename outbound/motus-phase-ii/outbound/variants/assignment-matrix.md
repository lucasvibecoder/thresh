# Variant × Inbox Assignment Matrix

**Total contacts:** 14 (LM-valid only, strict policy)
**Cycle:** Motus Phase II — Factoring
**Send window:** Tue 2026-05-12 or Wed 2026-05-13, 9am ET
**Per-inbox cap:** 20/day (this campaign uses 1-2 per inbox; massive headroom)

---

## Variant → Inbox map

| Variant | Inbox A | Inbox B |
|---|---|---|
| v1 | `lucas.l@threshworks.com` (Porkbun) | `lucas.l@withthresh.com` (Porkbun) |
| v2 | `l@threshworks.com` (Porkbun) | `l@withthresh.com` (Porkbun) |
| v3 | `lucas@threshworks.com` (Porkbun) | `lucas@withthresh.com` (Porkbun) |
| v4 | `lucas.l@threshhq.com` (Porkbun) | `lucas.linares@runthresh.com` (Vercel) |
| v5 | `l@threshhq.com` (Porkbun) | `lucas@threshhq.com` (Porkbun) |

The runthresh.com inbox is paired with the threshhq.com trio under v4 (only 10 inboxes for 5 variants × 2 cells = 10).

---

## Final per-cell counts

| Variant | Inbox A count | Inbox B count | Total |
|---|---|---|---|
| v1 | 2 | 1 | 3 |
| v2 | 2 | 1 | 3 |
| v3 | 2 | 1 | 3 |
| v4 | 2 | 1 | 3 |
| v5 | 1 | 1 | 2 |
| **Total** | **9** | **5** | **14** |

---

## Per-inbox total sends

| Inbox | Sends |
|---|---|
| `lucas.l@threshworks.com` | 2 |
| `lucas.l@withthresh.com` | 1 |
| `l@threshworks.com` | 2 |
| `l@withthresh.com` | 1 |
| `lucas@threshworks.com` | 2 |
| `lucas@withthresh.com` | 1 |
| `lucas.l@threshhq.com` | 2 |
| `lucas.linares@runthresh.com` | 1 |
| `l@threshhq.com` | 1 |
| `lucas@threshhq.com` | 1 |

All inboxes 1-2 sends — well under the 20/day cap and easily within the 8-min-gap warm-inbox cadence.

---

## Allocation rule

- Sort contacts deterministically by `(tier, domain, email)` ascending
- Round-robin across variants v1 → v5 → v1 → v2 ...
- Within each variant, alternate between Inbox A and Inbox B
- Result: even distribution across variants + inboxes; same assignment reproducible from `contacts/contacts-validated.csv`

Source script: `contacts/assign.py`
Output: `contacts/contacts-final.csv` (adds `variant_id` + `assigned_inbox` columns)
