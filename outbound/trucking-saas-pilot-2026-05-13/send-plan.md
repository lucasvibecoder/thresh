# Trucking SaaS Pilot Send Plan - 2026-05-13

## Goal

Send the first 5 mini-PVP emails on Wednesday, May 13, 2026.

This is not a volume test. It is a proof-quality test:

- Can we make a trucking SaaS buyer care about public carrier signals?
- Do they quote one of the carrier examples back?
- Do they ask for the full trucking playbook?

At N=5, reply rate is mostly noise. A single reply that references a carrier name is the signal.

## Send-ready contacts

| Company | Domain | Contact | Title | Email | Structure | Bucket |
|---|---|---|---|---|---|---|
| FleetOperate | fleetoperate.com | Sharan Savadattimath | Co-Founder | sharan@fleetoperate.com | Founder, no sales team | compliance_authority_staleness |
| Simply Fleet | simplyfleet.app | Mrigaen Kapadia | Co-Founder | mrigaen@simplyfleet.app | Founder + first seller | maintenance_inspection |
| Ezlogz | ezlogz.com | Sergey Karman | CEO | cj@ezlogz.com | Founder, no sales team | driver_compliance_oos |
| Tourmo | tourmo.ai | Ricardo Silva | CRO | ricardos@tourmo.ai | VP Sales with thin/no SDR support | safety_risk_trend |
| Trucking Hub | truckinghub.com | Milos Pavlovic | Founder and CEO | milos@truckinghub.com | Founder, no sales team | tms_dispatch_motion |

## Skip for this pilot

| Company | Why skipped |
|---|---|
| FleetSpy | Email found was not a company-domain email. |
| Datatruck | No verified work email after waterfall. Second contact search found no profile. |
| YES! TMS | No verified work email after waterfall. |
| Trucker Tools | No verified work email after waterfall. |
| Truckpedia | Contact rejected: wrong seniority. |
| RouteMate | Contact rejected: wrong seniority. |

## Bucket logic

| Bucket | Use when prospect sells | Finding types | Notes |
|---|---|---|---|
| compliance_authority_staleness | Compliance, carrier ops, credentialing, fleet operations | stale MCS-150, authority/compliance gaps | Best for FleetOperate. Structural signal with Motus cutover urgency. |
| driver_compliance_oos | ELD, HOS, DVIR, driver workflow, compliance | driver OOS, vehicle OOS, inspection failures | Best for Ezlogz. Phrase as driver compliance/OOS unless HOS is explicitly sourced. |
| maintenance_inspection | Maintenance, inspections, work orders, fleet upkeep | vehicle OOS, recurring maintenance failures | Best for Simply Fleet. Strongest current examples are vehicle OOS rates. |
| safety_risk_trend | Fleet intelligence, safety analytics, risk, insurance | crash count, unsafe driving, vehicle maintenance, worsening BASIC measures | Best for Tourmo. Use risk getting worse, not generic compliance. |
| tms_dispatch_motion | TMS, dispatch, carrier operations | new active authority, newly added FMCSA record, fleet growth | Best for Trucking Hub. This is a motion/buying-trigger wedge, not a pain wedge. |

## Wednesday send schedule

| Time ET | Action |
|---|---|
| 8:30am | Open Smartlead campaign preview. Check every merge field on all 5 leads. |
| 8:45am | Spot-check the 15 carrier examples against source links if anything feels off. For FleetOperate, use "Motus cutover starts Thursday," not "will fail Motus." |
| 9:15am | Send FleetOperate and Simply Fleet. |
| 10:45am | Send Ezlogz. |
| 12:30pm | Send Tourmo. |
| 2:15pm | Send Trucking Hub. |
| End of day | Log replies, opens if useful, and any carrier-name quote-backs. |

## Smartlead tracking fields

Add these fields or labels so the learning loop is clean:

- `pilot_date`: `2026-05-13`
- `bucket`
- `sales_team_structure`
- `reply_status`: blank / positive / neutral / negative / ooo
- `playbook_requested`: yes / no
- `meeting_booked`: yes / no
- `carrier_quoted_back`: yes / no
- `carrier_quoted_name`
- `notes`

## Decision rule

After 7 days:

- If 1+ person quotes a carrier or asks how the pull works: scale to N=20 with the same skeleton.
- If replies are curious but no carrier is mentioned: tighten the PVP block before scaling.
- If no replies: do not rewrite copy first. Re-check SaaS-side triggers and whether these 5 were close enough to the pain.
