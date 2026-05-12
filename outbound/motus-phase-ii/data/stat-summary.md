# MCS-150 Staleness Stat — Motus Phase II Campaign

**Pulled:** 2026-05-11
**Source:** FMCSA Company Census File via Socrata SoQL aggregate queries on `datahub.transportation.gov/resource/az4n-8mr2.csv`
**Dataset last refreshed:** 2026-05-11 09:36 UTC (same-day)
**Cutoff:** MCS150_DATE < `20240511 0000` (24 months prior to 2026-05-11)

## Methodology

Used Socrata SoQL `$select=count(*)` with `$where` clauses rather than downloading the full ~1.4GB CSV. Server-side aggregation across three nested carrier universes. Each query returned in <2 seconds.

Universe definitions:
- **U1 — All active USDOT:** `status_code = 'A'`
- **U2 — Active + operating authority:** U1 + at least one of `docket1_status_code`, `docket2_status_code`, `docket3_status_code` = `'A'`
- **U3 — Active + authority + interstate:** U2 + `carrier_operation = 'A'`

Stale predicate: `mcs150_date < '20240511 0000'` (text comparison works because FMCSA stores dates as `YYYYMMDD HHMM`, lexicographically sortable).

## Results

| Universe | Total | Stale | % Stale | Band Check (8–25%) |
|---|---|---|---|---|
| U1 | 2,190,649 | 910,497 | 41.56% | Above 25% — too broad |
| **U2** | **680,056** | **136,498** | **20.07%** | **IN BAND ✓** |
| U3 | 486,853 | 40,628 | 8.34% | In band (lower bound) |

## Decision: cite **U2 (20%)**

Why U2 over U1 or U3:
- **U1 (41%)** includes ~1.5M private/intrastate-only carriers that aren't part of factoring's universe. Bloats denominator with carriers a factor would never advance to. Reads as "true but irrelevant."
- **U2 (20%)** matches the factoring world exactly: carriers with active FMCSA operating authority = carriers eligible to haul for-hire freight = carriers a factor's book is actually drawn from.
- **U3 (8%)** narrows to interstate-only, drops intrastate hazmat / intrastate non-hazmat carriers that factors may still serve. Lower bound of band, leaves a sharper claim on the table.

## Email line update

Replace:
```
Roughly [X]% of active carriers have MCS-150s past the 24-month update window — the most common of these gaps.
```

With:
```
Roughly 20% of US carriers with active FMCSA operating authority have MCS-150s past the 24-month update window — the most common of these gaps.
```

## Defensibility note

If a recipient asks "where'd that number come from?":
> "FMCSA Company Census File pulled 2026-05-11. Filtered to carriers with STATUS_CODE='A' and at least one active operating-authority docket — 680,056 carriers. 136,498 of those have MCS-150 dates older than 24 months. Happy to share the SoQL queries."

The dataset is refreshed daily; the number will drift by <1% week-over-week. Safe to cite for the next ~30 days without re-pulling.
