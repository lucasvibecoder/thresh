# Smartlead Setup Summary - 2026-05-12

## Campaign

- Campaign name: `Thresh - Trucking SaaS Mini-PVP - 2026-05-13`
- Campaign ID: `3326039`
- Status: `DRAFTED`
- Start status: not started
- Sequence count: 1
- Leads loaded: 5

## Schedule

- Timezone: `America/New_York`
- Send day: Wednesday
- Send window: `09:00` to `15:00`
- Minimum time between emails: 75 minutes
- Max new leads per day: 5

## Settings

- Open tracking: disabled
- Click tracking: disabled
- Stop on reply: enabled
- Plain text: enabled
- Follow-ups loaded: 0
- Main `runthresh.com` mailbox excluded

## Linked Senders

All 9 non-main inboxes are linked to the campaign:

- `lucas.l@threshworks.com`
- `l@threshworks.com`
- `lucas@threshworks.com`
- `lucas.l@withthresh.com`
- `l@withthresh.com`
- `lucas@withthresh.com`
- `lucas.l@threshhq.com`
- `l@threshhq.com`
- `lucas@threshhq.com`

Excluded:

- `lucas.linares@runthresh.com`

## Lead-Specific Sender Assignments

| Company | Lead Email | Assigned Sender |
|---|---|---|
| FleetOperate | `sharan@fleetoperate.com` | `lucas.l@threshworks.com` |
| Simply Fleet | `mrigaen@simplyfleet.app` | `l@withthresh.com` |
| Ezlogz | `cj@ezlogz.com` | `lucas.l@threshhq.com` |
| Tourmo | `ricardos@tourmo.ai` | `l@threshworks.com` |
| Trucking Hub | `milos@truckinghub.com` | `lucas@withthresh.com` |

## Final QA Result

Verified through Smartlead API:

- Campaign exists and is `DRAFTED`.
- Exactly 1 sequence exists.
- 9 sender accounts are linked.
- 5 leads are loaded.
- Each lead has the intended assigned sender in its custom fields.

Note: Smartlead shows lead-level status as `STARTED`, but the campaign status is still `DRAFTED`. The campaign has not been started.

