"""
Scrub the Discolike export, apply tier labels, and write the AI-Ark-ready CSV.

Input:  /Users/lucas/Downloads/discolike_export_discover_202605112117.csv
Output: /Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/data/factoring-list-scrubbed.csv

Exclusions:
  - Broker/matchmaker domains (not actual factors)
  - Pure payments/fuel-card companies (different buyer, different pitch)
  - Oil & gas vertical mismatch
  - Duplicates of already-included companies
  - Description-based pattern matches: "connects clients with", "network of factoring firms",
    "matches it with the best financing", "marketplace of over 300"

Tier labels:
  - A: 51-200 employees (dedicated credit team, VP Credit / Head of Underwriting target)
  - B: 11-50 employees + similarity >= 92 (founder/CEO target, still owns credit)
  - C: 1-10 employees + similarity >= 92 (founder only, smaller pool)
  - DROP: 1-10 with sim < 92, or excluded by domain/pattern
"""
import csv
from pathlib import Path

SRC = Path("/Users/lucas/Downloads/discolike_export_discover_202605112117.csv")
DST = Path("/Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/data/factoring-list-scrubbed.csv")
DROPPED = Path("/Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/data/factoring-list-dropped.csv")

EXCLUDE_DOMAINS = {
    # Broker / matchmaker (not actual factors)
    "factorfinders.com",
    "factoringcompanies.com",
    "factor.bot",
    # Pure payments / fuel-card (different buyer)
    "roadsync.com",
    "relaypayments.com",
    "atob.com",
    # Vertical mismatch
    "sbfactoring.net",  # oil & gas focus
    # Duplicate of fleetonefactoring.com (both are WEX)
    "efsllc.com",
}

EXCLUDE_DESC_PATTERNS = [
    "connects clients with",
    "network of factoring firms",
    "matches it with the best financing",
    "marketplace of over",
    "vetted factoring firms",
    "factoring broker that connects",
    "compares factoring",
    "300 factoring firms",
]


def tier_of(row) -> str:
    emp = row.get("Employees", "").strip()
    try:
        sim = int(row.get("Similarity", "0") or 0)
    except ValueError:
        sim = 0
    if emp == "51-200":
        return "A"
    if emp == "11-50" and sim >= 92:
        return "B"
    if emp == "1-10" and sim >= 92:
        return "C"
    return "DROP_LOW_SIM"


def main() -> None:
    with SRC.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    kept = []
    dropped = []

    for row in rows:
        domain = (row.get("Domain") or "").strip().lower()
        desc = (row.get("Description") or "").lower()

        if domain in EXCLUDE_DOMAINS:
            row["DROP_REASON"] = f"domain-excluded ({domain})"
            dropped.append(row)
            continue

        matched_pattern = next((p for p in EXCLUDE_DESC_PATTERNS if p in desc), None)
        if matched_pattern:
            row["DROP_REASON"] = f"broker-pattern: {matched_pattern!r}"
            dropped.append(row)
            continue

        t = tier_of(row)
        if t == "DROP_LOW_SIM":
            row["DROP_REASON"] = f"low similarity ({row.get('Similarity')}) in {row.get('Employees')} band"
            dropped.append(row)
            continue

        row["TIER"] = t
        kept.append(row)

    # Sort kept by tier then similarity desc
    kept.sort(key=lambda r: (r["TIER"], -int(r.get("Similarity") or 0)))

    # Write outputs
    out_fields = ["TIER"] + [k for k in kept[0].keys() if k not in ("TIER", "DROP_REASON")]
    DST.parent.mkdir(parents=True, exist_ok=True)
    with DST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    drop_fields = ["DROP_REASON"] + [k for k in dropped[0].keys() if k != "DROP_REASON"]
    with DROPPED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=drop_fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(dropped)

    # Summary
    by_tier = {}
    for r in kept:
        by_tier[r["TIER"]] = by_tier.get(r["TIER"], 0) + 1

    print(f"Source rows:    {len(rows)}")
    print(f"Kept:           {len(kept)}")
    print(f"Dropped:        {len(dropped)}")
    print()
    print("Kept by tier:")
    for t in sorted(by_tier):
        label = {"A": "51-200 emp (VP Credit / Head of Underwriting)",
                 "B": "11-50 emp + sim>=92 (Founder / CEO)",
                 "C": "1-10 emp + sim>=92 (Founder only)"}.get(t, t)
        print(f"  Tier {t}: {by_tier[t]:>3}  - {label}")
    print()
    print(f"Output:  {DST}")
    print(f"Dropped: {DROPPED}")

    # Drop reason summary
    drop_reasons = {}
    for r in dropped:
        reason = r["DROP_REASON"].split("(")[0].strip()
        drop_reasons[reason] = drop_reasons.get(reason, 0) + 1
    print()
    print("Drop reason summary:")
    for k, v in sorted(drop_reasons.items(), key=lambda x: -x[1]):
        print(f"  {v:>3}  {k}")


if __name__ == "__main__":
    main()
