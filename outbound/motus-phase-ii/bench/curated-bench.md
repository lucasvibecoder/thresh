# Named-Examples Bench — Motus Phase II Reply Ammo

**Use:** When a factoring recipient replies "interesting, like what?" — drop a named carrier in-thread as proof-of-work. Not body content. Not attached to outbound. Reply layer only.

**Sourced:** FMCSA Company Census File, 2026-05-11
**Filter:** STATUS_CODE='A' + active operating authority + MCS150_DATE < 2024-05-11 + 75–200 power units + US-based + for-hire trucking name pattern + officer named

**Quality bar applied:** Eight US states represented, no bus/transit/school/specialty operators, all carriers ≥ 8 years stale on MCS-150 (median: 12 years stale).

---

## 8 Curated Carriers (sorted by stale-age)

| # | Legal Name | DOT# | State / City | Power Units | MCS-150 Date | Years Stale | Officer |
|---|---|---|---|---|---|---|---|
| 1 | C&C TRANSPORTATION COMPANY INC | 179506 | PA / Philadelphia | 80 | 2004-05-28 | 22 | Dominick A Cipollini |
| 2 | AFAB TRUCKING INC | 1201424 | FL / North Fort Myers | 114 | 2007-03-27 | 19 | Troy Futch Jr. |
| 3 | C T HARRIS INC | 238183 | GA / Sandersville | 129 | 2009-02-11 | 17 | C T Harris Jr |
| 4 | SNYDER TRANSPORTATION LLC | 2168717 | NY / West Seneca | 77 | 2011-06-29 | 15 | Thomas Ayers |
| 5 | MEDIC TRANSPORTATION LLC | 2440489 | TN / Memphis | 112 | 2013-09-24 | 12 | H. Gordon Wynn, III |
| 6 | S & H DEDICATED INC (S & H LEASING OF MICHIGAN INC) | 2504104 | MI / Warren | 100 | 2014-05-08 | 12 | Thomas O Wellsman |
| 7 | F T SILFIES INC | 173850 | PA / Allentown | 110 | 2015-03-27 | 11 | Chris Silfies |
| 8 | LINDEN BULK TRANSPORTATION CO INC | 237425 | NJ / Linden | 190 | 2016-06-24 | 10 | Paul J Defalco |

## How to deploy in a reply

When recipient asks "like what?" — send something like:

> "Sure. Pulled a few examples from FMCSA today:
>
> - C&C Transportation, Philadelphia PA — 80 trucks, MCS-150 last updated 2004 (22 years stale)
> - AFAB Trucking, North Fort Myers FL — 114 trucks, last updated 2007 (19 years stale)
> - C T Harris, Sandersville GA — 129 trucks, last updated 2009 (17 years stale)
>
> All three have active FMCSA operating authority right now. Each one fails business verification the moment Motus does its first reconciliation pass. Want me to do this against a region you cover?"

The reply re-asserts the offer and pivots to a specific request (a region they cover) — less friction than asking for their book.

## Caveats

- These are stale-on-MCS-150 carriers. They're not necessarily defaulting *today* — staleness ≠ insolvency. The pitch is that Motus will surface them as risk signals, not that they're currently defaulting.
- A few of these carriers may have updated MCS-150s since the 2026-05-11 pull. Census refreshes daily; before sending any specific name, spot-check via SAFER (https://safer.fmcsa.dot.gov/CompanySnapshot.aspx).
- Officer names are public per FMCSA Census — fine to mention. Don't reveal in body of cold first-touch (entity-decoding rule applies).

## Source

Raw 100-row candidate pool: `raw-candidates.csv` (same directory). Query used:

```
GET https://datahub.transportation.gov/resource/az4n-8mr2.csv
  ?$select=dot_number,legal_name,dba_name,phy_state,phy_city,power_units,mcs150_date,carrier_operation,company_officer_1
  &$where=status_code='A'
    AND (docket1_status_code='A' OR docket2_status_code='A' OR docket3_status_code='A')
    AND mcs150_date < '20240511 0000'
    AND (power_units::number) >= 5
    AND (power_units::number) <= 200
    AND legal_name IS NOT NULL
  &$order=power_units::number DESC
  &$limit=100
```
