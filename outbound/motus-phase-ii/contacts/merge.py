"""Flatten AI Ark Pass 1 + Pass 2 raw CSVs to contacts-merged.csv.

Tier from data/factoring-list-scrubbed.csv (joined by email domain).
Title regex per tier — drop off-target rows.
Dedupe by email.
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_LIST = ROOT / "data" / "factoring-list-scrubbed.csv"
PASS1 = ROOT / "contacts" / "pass1-tier-a-raw.csv"
PASS2 = ROOT / "contacts" / "pass2-tier-bc-raw.csv"
OUT = ROOT / "contacts" / "contacts-merged.csv"

# Tier lookup: domain -> tier
tier_by_domain = {}
company_by_domain = {}
with SRC_LIST.open() as f:
    r = csv.DictReader(f)
    for row in r:
        d = row["Domain"].strip().lower()
        tier_by_domain[d] = row["TIER"].strip()
        company_by_domain[d] = row["Name"].strip()

# Title regex per tier
RE_TIER_A = re.compile(
    r"\b(credit|risk|underwrit|portfolio|collections|"
    r"chief financial|cfo|chief operating|coo|chief executive|ceo|president|controller|"
    r"vp.*(?:finance|operations|specialty)|"
    r"director.*(?:finance|operations))\b",
    re.I,
)
RE_TIER_BC = re.compile(r"\b(founder|co.?founder|ceo|chief executive|president|owner|managing partner|managing director)\b", re.I)

# Anti-patterns (always reject)
RE_REJECT = re.compile(r"\b(sales|marketing|business development|bdr|sdr|account executive|partnership|customer success|recruit|hr |human resources)\b", re.I)


def parse_json(s):
    if not s or not s.strip():
        return None
    try:
        return json.loads(s)
    except Exception:
        return None


def extract_email(email_json):
    """Returns (address, status, sub_status, domain_type) or None."""
    if not email_json:
        return None
    output = email_json.get("output") or []
    if not output:
        return None
    e = output[0]
    addr = e.get("address")
    if not addr:
        return None
    return (
        addr.strip().lower(),
        e.get("status"),
        e.get("subStatus"),
        e.get("domainType"),
    )


def flatten_row(raw_row, pass_label):
    p = parse_json(raw_row.get("profile"))
    if not p:
        return None
    fn = (p.get("first_name") or "").strip()
    ln = (p.get("last_name") or "").strip()
    title = (p.get("title") or "").strip()
    if not fn or not title:
        return None

    email_data = extract_email(parse_json(raw_row.get("email")))
    if not email_data:
        return None
    email, email_status, email_sub_status, domain_type = email_data
    if email_status == "INVALID":
        return None
    email_domain = email.split("@")[-1] if "@" in email else ""

    company_json = parse_json(raw_row.get("company")) or {}
    company_name = company_json.get("summary", {}).get("name") or company_json.get("name") or ""

    dept = parse_json(raw_row.get("department")) or {}
    seniority = dept.get("seniority") or ""

    link = parse_json(raw_row.get("link")) or {}
    linkedin = link.get("linkedin") or ""

    # Tier lookup by email domain first, then by raw_row source pass
    tier = tier_by_domain.get(email_domain.lower(), "")
    src_company = company_by_domain.get(email_domain.lower(), "")
    if not tier:
        # No domain match — try matching by company name substring
        cn_lower = company_name.lower()
        for d, src_name in company_by_domain.items():
            if src_name.lower() in cn_lower or cn_lower.split()[0:1] == src_name.lower().split()[0:1]:
                tier = tier_by_domain[d]
                src_company = src_name
                email_domain = d  # remap for downstream
                break

    return {
        "first_name": fn,
        "last_name": ln,
        "email": email,
        "title": title,
        "seniority": seniority,
        "company_name": src_company or company_name,
        "domain": email_domain,
        "linkedin_url": linkedin,
        "tier": tier,
        "email_status": email_status,
        "email_sub_status": email_sub_status,
        "domain_type": domain_type,
        "source_pass": pass_label,
    }


def title_ok(title, tier):
    if RE_REJECT.search(title):
        return False
    if tier == "A":
        return bool(RE_TIER_A.search(title))
    elif tier in ("B", "C"):
        return bool(RE_TIER_BC.search(title))
    return False


def load_pass(path, label):
    out = []
    with path.open() as f:
        r = csv.DictReader(f)
        for raw in r:
            row = flatten_row(raw, label)
            if not row:
                continue
            if not row["tier"]:
                continue
            if not title_ok(row["title"], row["tier"]):
                continue
            out.append(row)
    return out


def main():
    rows = []
    rows.extend(load_pass(PASS1, "pass1_tier_a"))
    rows.extend(load_pass(PASS2, "pass2_tier_bc"))

    # Dedupe by email
    seen = set()
    deduped = []
    for r in rows:
        if r["email"] in seen:
            continue
        seen.add(r["email"])
        deduped.append(r)

    # Sort: tier then domain then email for determinism
    deduped.sort(key=lambda r: (r["tier"], r["domain"], r["email"]))

    cols = [
        "first_name", "last_name", "email", "title", "seniority",
        "company_name", "domain", "linkedin_url", "tier",
        "email_status", "email_sub_status", "domain_type", "source_pass",
    ]
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in deduped:
            w.writerow(r)

    # Tier breakdown report
    from collections import Counter
    tier_counts = Counter(r["tier"] for r in deduped)
    dt_counts = Counter(r["domain_type"] for r in deduped)
    print(f"Wrote {len(deduped)} contacts to {OUT.relative_to(ROOT)}")
    print(f"Tier breakdown: {dict(tier_counts)}")
    print(f"Email domain_type breakdown: {dict(dt_counts)}")
    domains_with_contacts = sorted(set(r["domain"] for r in deduped))
    print(f"Distinct domains with contacts: {len(domains_with_contacts)} / 52")
    print(f"Domains MISSING contacts:")
    missing = sorted(set(tier_by_domain.keys()) - set(domains_with_contacts))
    for d in missing:
        print(f"  [{tier_by_domain[d]}] {d}  ({company_by_domain[d]})")


if __name__ == "__main__":
    main()
