# Post-Launch Check — Motus Phase II

**Run this Tuesday 2026-05-12 around noon ET** (after the campaign has had ~3 hours of send time to accumulate signal).

Campaign ID: **3319888**

## Commands to paste

```bash
# Current campaign metrics (sent / opens / replies / bounces)
deepline tools execute smartlead_get_campaign_stats --payload '{"campaign_id": 3319888}'

# Lead-level statistics
deepline tools execute smartlead_get_lead_statistics --payload '{"campaign_id": 3319888}'

# Email-wise inbox health (catches if any inbox is bouncing or getting flagged)
deepline tools execute smartlead_get_analytics_email_wise_health --payload '{"campaign_id": 3319888}'

# Master Inbox — pull recent replies
deepline tools execute smartlead_get_inbox_messages --payload '{"campaign_id": 3319888}'
```

## What to look for

| Metric | Healthy | Warning | Action |
|---|---|---|---|
| Bounce rate | <2% | 2-5% | Investigate which inbox; check SPF/DKIM/DMARC |
| Opens by 12pm ET | >40% | 20-40% | Wait until end of day before drawing conclusions |
| Replies | 1+ by EOD | 0 by EOD | Single-send open rate matters more than reply at this volume |
| Spam complaints | 0 | 1+ | Pause sending immediately, audit inbox health |
| Per-inbox sent count | 1-2 | 0 | Confirm all 9 inboxes are firing (some may be queued for tomorrow) |

## Update memory after the check

Append to MEMORY.md or [blanchq-run-2026-05-10.md style entry] something like:

> Motus Phase II launched 2026-05-12 09:00 ET. By 12pm ET: X sent / Y opens (Z%) / W replies. Per-variant: A=__, B=__, C=__, D=__. Inbox health: all 9 green / X flagged. First reply at HH:MM from [name, company]. Top-performing variant (early signal): __.

## If something's off

- High bounce → one of the 9 inboxes may have DKIM/SPF drift; spot-check the email-wise-health output
- Low opens → subject lines aren't landing; not actionable mid-flight, but note for next campaign
- Spam complaint → pause the campaign via `smartlead_update_campaign_status` with `"status": "PAUSED"`, then triage
