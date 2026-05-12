"""Run LeadMagic email validation across all merged contacts.
Appends `lm_status`, `lm_confidence` (if provided), `lm_raw` columns.
Drops `invalid`. Keeps `catch_all` for now — flag with marker for Lucas review if confidence low.
"""
import csv, json, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "contacts" / "contacts-merged.csv"
OUT = ROOT / "contacts" / "contacts-validated.csv"
LOG = ROOT / "contacts" / "leadmagic-raw.jsonl"


def run_leadmagic(email, first_name=None, last_name=None):
    payload = {"email": email}
    if first_name: payload["first_name"] = first_name
    if last_name: payload["last_name"] = last_name
    result = subprocess.run(
        ["deepline", "tools", "execute", "leadmagic_email_validation",
         "--payload", json.dumps(payload)],
        capture_output=True, text=True, timeout=60,
    )
    return result.stdout, result.stderr, result.returncode


def parse_leadmagic_output(stdout):
    """Extract structured data from Deepline CLI stdout."""
    idx = stdout.find("Result:")
    if idx < 0:
        return None
    json_str = stdout[idx + len("Result:"):].strip()
    try:
        return json.loads(json_str)
    except Exception:
        return None


def main():
    with IN.open() as f:
        rows = list(csv.DictReader(f))

    enriched = []
    with LOG.open("w") as logf:
        for i, row in enumerate(rows, 1):
            email = row["email"]
            print(f"[{i}/{len(rows)}] {email}", flush=True)
            stdout, stderr, rc = run_leadmagic(email, row.get("first_name"), row.get("last_name"))
            parsed = parse_leadmagic_output(stdout)
            data = (parsed or {}).get("data") or {}
            row["lm_status"] = data.get("email_status") or data.get("status") or ""
            row["lm_message"] = data.get("message") or data.get("reason") or ""
            row["lm_is_domain_catch_all"] = str(data.get("is_domain_catch_all", "")).lower()
            row["lm_is_valid"] = str(data.get("is_valid", "")).lower()
            row["lm_mx_provider"] = data.get("mx_provider") or ""
            enriched.append(row)
            logf.write(json.dumps({"email": email, "stdout": stdout[:5000], "stderr": stderr[:1000]}) + "\n")
            time.sleep(0.3)  # gentle pace

    cols = list(enriched[0].keys())
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in enriched:
            w.writerow(r)

    # Report
    from collections import Counter
    print()
    print(f"Wrote {len(enriched)} validated rows to {OUT.relative_to(ROOT)}")
    print(f"LM status: {dict(Counter(r['lm_status'] for r in enriched))}")
    print(f"LM is_valid: {dict(Counter(r['lm_is_valid'] for r in enriched))}")
    print(f"LM is_domain_catch_all: {dict(Counter(r['lm_is_domain_catch_all'] for r in enriched))}")


if __name__ == "__main__":
    main()
