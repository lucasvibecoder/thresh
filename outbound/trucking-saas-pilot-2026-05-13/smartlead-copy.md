# Smartlead Copy - Trucking SaaS Pilot

## Campaign Structure

Use one Smartlead campaign with 5 leads and custom fields from the import CSV.

For the first send, either use the exact per-lead copy below or use this single template:

Subject:

```text
{{subject}}
```

Body:

```text
{{opener_line}}

I pulled 3 carriers in that pattern:

- {{carrier_1}}
- {{carrier_2}}
- {{carrier_3}}

{{architecture_line}}

{{cta}}
```

Do not add a long signature. Let the sending inbox signature handle that if needed.

## Follow-up Rule

For the N=5 pilot, load only the first touch if you want the cleanest read.

If you want a real sequence, use one follow-up 4 business days later:

```text
{{first_name}}, should I send the full version of this for {{company_name}}, or is the carrier-signal angle not worth a look right now?
```

No more than one follow-up until we see how the PVP lands.

## Lead 1 - FleetOperate

Subject:

```text
Motus cutover Thursday
```

Body:

```text
Sharan,

FMCSA's Motus cutover starts Thursday. Legacy registration tools retire at 8pm ET, and carriers are being pushed to clean company info before the move.

The exposed accounts have stale MCS-150s and messy registration records. I pulled 3 active carriers in that pattern:

- C&C Transportation, DOT 179506 - 80 trucks, MCS-150 last updated 2004
- AFAB Trucking, DOT 1201424 - 114 trucks, last updated 2007
- Snyder Transportation, DOT 2168717 - 77 trucks, last updated 2011

Same FMCSA pull can refresh weekly against FleetOperate's TAM while the Motus transition is live.

Want me to run the full trucking playbook for FleetOperate?
```

## Lead 2 - Simply Fleet

Subject:

```text
3 fleets with maintenance signals
```

Body:

```text
Mrigaen,

Simply Fleet sits where maintenance pain is visible before demand is. Vehicle inspection failures show which fleets are feeling the issue before they shop.

I pulled 3 examples:

- Himco Waste-Away, DOT 271536 - 90.9% vehicle OOS across 11 inspections
- Black Hawk Waste Disposal, DOT 965457 - 81.8% vehicle OOS across 22 inspections
- Tennessee Auto Salvage, DOT 2533982 - 80.0% vehicle OOS across 25 inspections

Same FMCSA pull can refresh weekly against Simply Fleet's TAM.

Want me to run the full trucking playbook for Simply Fleet?
```

## Lead 3 - Ezlogz

Subject:

```text
Ezlogz DVIR signals
```

Body:

```text
Sergey,

Ezlogz is in a market where driver compliance pain leaks before intent does. Vehicle OOS clusters often point to broken DVIR and inspection workflows before a carrier shops.

I pulled 3 examples:

- Waste Path Services, DOT 1674904 - 50.0% driver OOS, 75.0% vehicle OOS
- Britt Demolition, DOT 424956 - 37.5% driver OOS, 77.3% vehicle OOS
- Carolina Waste & Recycling, DOT 2184616 - 50.0% driver OOS, 4 crashes

Same FMCSA pull can refresh weekly against Ezlogz's TAM.

Want me to run the full trucking playbook for Ezlogz?
```

## Lead 4 - Tourmo

Subject:

```text
3 risky fleets on FMCSA
```

Body:

```text
Ricardo,

For Tourmo, the revenue question probably is not "which fleets exist?" It is which fleets are sitting in red right now and should hear from you before they ask for another safety layer.

I pulled 3 examples:

- BR Williams, DOT 105824 - Vehicle Maintenance measure 3.93, with 6 crashes on SMS
- Good's Disposal, DOT 2074205 - 19 crashes and 33.3% vehicle OOS
- Active Waste Solutions, DOT 2497945 - 10 crashes and 52.2% vehicle OOS

Same FMCSA/SMS pull can refresh weekly against Tourmo's TAM.

Want me to run the full trucking playbook for Tourmo?
```

## Lead 5 - Trucking Hub

Subject:

```text
3 carriers got authority this week
```

Body:

```text
Milos,

Trucking Hub is in a market where demand often shows up as motion before intent. Newly active carriers are setting up dispatch workflows before they have a polished buying process.

I pulled 3 examples from FMCSA this week:

- FOE Transportation, DOT 4580579 - 40 power units, active-authority record added May 9
- Infinity Trucking, DOT 4580572 - 37 power units, active-authority record added May 9
- DP World Trucking, DOT 4579290 - 15 power units, active-authority record added May 7

Same pull can refresh weekly against Trucking Hub's TAM.

Want me to run the full trucking playbook for Trucking Hub?
```

## QA Before Send

Check these before scheduling:

- Every rendered email has a real first name.
- Every email has exactly 3 carrier bullets.
- No `{{merge_tag}}` appears in preview.
- No skipped companies are in the campaign.
- The follow-up is either off or scheduled 4 business days later.
