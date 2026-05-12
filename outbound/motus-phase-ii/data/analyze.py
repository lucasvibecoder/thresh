"""
Compute MCS-150 stale-rate stat from FMCSA Census file.

Reports % stale (MCS150_DATE >24 months from 2026-05-11) across three carrier universes:
  1. All STATUS_CODE=A (active USDOT) carriers
  2. Active USDOT + at least one active operating-authority docket (for-hire / interstate)
  3. Active USDOT + active authority + CARRIER_OPERATION = for-hire only

Band check: 8-25% -> email ships as-is; outside band -> surface to Lucas for reframe.

Also builds candidate bench (POWER_UNITS 5-200, named, stale, active authority).
"""
import csv
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

CENSUS_PATH = Path("/Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/data/census.csv")
BENCH_PATH = Path("/Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/bench/candidates.csv")
SUMMARY_PATH = Path("/Users/lucas/Documents/projects/gtm-alpha/runs/motus-phase-ii/data/stat-summary.md")
TODAY = date(2026, 5, 11)
CUTOFF = date(2024, 5, 11)  # 24 months prior

csv.field_size_limit(sys.maxsize)


def parse_date(s: str):
    if not s:
        return None
    s = s.strip()
    for fmt in ("%Y%m%d %H%M", "%Y%m%d", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def has_active_authority(row) -> bool:
    for k in ("DOCKET1_STATUS_CODE", "DOCKET2_STATUS_CODE", "DOCKET3_STATUS_CODE"):
        if (row.get(k) or "").strip().upper() == "A":
            return True
    return False


def is_for_hire(row) -> bool:
    op = (row.get("CARRIER_OPERATION") or "").strip().upper()
    # Common FMCSA codes for for-hire carriers
    return op in {"A", "1", "FOR-HIRE", "FORHIRE"}


def fmt_pct(n, d):
    return (n / d * 100) if d else 0.0


def main() -> None:
    universe_all = {"total": 0, "stale": 0}
    universe_auth = {"total": 0, "stale": 0}
    universe_forhire = {"total": 0, "stale": 0}

    candidates = []
    by_state_auth = defaultdict(lambda: {"total": 0, "stale": 0})
    op_code_counts = defaultdict(int)

    with CENSUS_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            status = (row.get("STATUS_CODE") or "").strip().upper()
            if status != "A":
                continue

            mcs150 = parse_date(row.get("MCS150_DATE") or "")
            if mcs150 is None:
                continue

            is_stale = mcs150 < CUTOFF
            has_auth = has_active_authority(row)
            forhire = is_for_hire(row)
            op_code_counts[(row.get("CARRIER_OPERATION") or "").strip().upper()] += 1

            universe_all["total"] += 1
            if is_stale:
                universe_all["stale"] += 1

            if has_auth:
                universe_auth["total"] += 1
                state = (row.get("PHY_STATE") or row.get("CARRIER_MAILING_STATE") or "??").strip().upper()
                by_state_auth[state]["total"] += 1
                if is_stale:
                    universe_auth["stale"] += 1
                    by_state_auth[state]["stale"] += 1

            if has_auth and forhire:
                universe_forhire["total"] += 1
                if is_stale:
                    universe_forhire["stale"] += 1

            # Bench: active-authority + stale + named + 5-200 power units
            if has_auth and is_stale:
                try:
                    pu = int(row.get("POWER_UNITS") or 0)
                except ValueError:
                    pu = 0
                if 5 <= pu <= 200 and (row.get("LEGAL_NAME") or "").strip():
                    candidates.append({
                        "DOT_NUMBER": row.get("DOT_NUMBER"),
                        "LEGAL_NAME": row.get("LEGAL_NAME"),
                        "DBA_NAME": row.get("DBA_NAME"),
                        "PHY_STATE": (row.get("PHY_STATE") or "").strip().upper(),
                        "PHY_CITY": row.get("PHY_CITY"),
                        "POWER_UNITS": pu,
                        "MCS150_DATE": mcs150.isoformat(),
                        "MCS150_AGE_YEARS": round((TODAY - mcs150).days / 365.25, 1),
                        "CARRIER_OPERATION": row.get("CARRIER_OPERATION"),
                        "OFFICER_1": row.get("COMPANY_OFFICER_1"),
                    })

            if i % 200_000 == 0 and i > 0:
                print(f"  ...processed {i:,} rows", file=sys.stderr)

    p_all = fmt_pct(universe_all["stale"], universe_all["total"])
    p_auth = fmt_pct(universe_auth["stale"], universe_auth["total"])
    p_forhire = fmt_pct(universe_forhire["stale"], universe_forhire["total"])

    summary_lines = []

    def emit(line=""):
        print(line)
        summary_lines.append(line)

    emit("=" * 70)
    emit("MCS-150 STALENESS ANALYSIS — Motus Phase II Campaign")
    emit("=" * 70)
    emit(f"Census file:           {CENSUS_PATH.name}")
    emit(f"Today:                 {TODAY.isoformat()}")
    emit(f"Cutoff (24 mo prior):  {CUTOFF.isoformat()}")
    emit("")
    emit("UNIVERSE 1 — All active USDOT carriers (STATUS_CODE=A)")
    emit(f"  Total:   {universe_all['total']:>10,}")
    emit(f"  Stale:   {universe_all['stale']:>10,}")
    emit(f"  Percent: {p_all:>10.2f}%")
    emit("")
    emit("UNIVERSE 2 — Active USDOT + active operating authority")
    emit(f"  Total:   {universe_auth['total']:>10,}")
    emit(f"  Stale:   {universe_auth['stale']:>10,}")
    emit(f"  Percent: {p_auth:>10.2f}%")
    emit("")
    emit("UNIVERSE 3 — Active USDOT + active authority + for-hire only")
    emit(f"  Total:   {universe_forhire['total']:>10,}")
    emit(f"  Stale:   {universe_forhire['stale']:>10,}")
    emit(f"  Percent: {p_forhire:>10.2f}%")
    emit("")
    emit("BAND CHECK (8-25%): which universes land in band?")
    for label, p in (("All active", p_all), ("Active+auth", p_auth), ("For-hire", p_forhire)):
        verdict = "IN BAND" if 8 <= p <= 25 else ("BELOW 8%" if p < 8 else "ABOVE 25%")
        emit(f"  {label:<14} {p:>6.2f}% — {verdict}")
    emit("")
    emit("TOP CARRIER_OPERATION codes (for context):")
    for code, count in sorted(op_code_counts.items(), key=lambda kv: -kv[1])[:8]:
        emit(f"  '{code}': {count:,}")
    emit("")
    emit("TOP 15 STATES BY STALE COUNT (active-authority subset):")
    top = sorted(by_state_auth.items(), key=lambda kv: -kv[1]["stale"])[:15]
    for state, d in top:
        rate = (d["stale"] / d["total"] * 100) if d["total"] else 0
        emit(f"  {state}: {d['stale']:>6,} stale of {d['total']:>6,} active ({rate:.1f}%)")
    emit("")
    emit(f"Bench candidate rows (active-authority, stale, named, 5-200 PU): {len(candidates):,}")

    BENCH_PATH.parent.mkdir(parents=True, exist_ok=True)
    with BENCH_PATH.open("w", encoding="utf-8", newline="") as f:
        if candidates:
            w = csv.DictWriter(f, fieldnames=list(candidates[0].keys()))
            w.writeheader()
            w.writerows(candidates[:5000])
    emit(f"Wrote candidate bench to: {BENCH_PATH}")

    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text("```\n" + "\n".join(summary_lines) + "\n```\n", encoding="utf-8")


if __name__ == "__main__":
    main()
