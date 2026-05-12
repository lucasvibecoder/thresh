"""Assign 14 LM-valid contacts to (variant, inbox) cells.
Round-robin across variants v1-v5; within each variant, alternate between Inbox A and Inbox B.
Writes contacts-final.csv with variant_id + assigned_inbox columns.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "contacts" / "contacts-validated.csv"
OUT = ROOT / "contacts" / "contacts-final.csv"

INBOXES = {
    "v1": ("lucas.l@threshworks.com", "lucas.l@withthresh.com"),
    "v2": ("l@threshworks.com",       "l@withthresh.com"),
    "v3": ("lucas@threshworks.com",   "lucas@withthresh.com"),
    "v4": ("lucas.l@threshhq.com",    "lucas.linares@runthresh.com"),
    "v5": ("l@threshhq.com",          "lucas@threshhq.com"),
}
VARIANTS = list(INBOXES.keys())

with IN.open() as f:
    rows = list(csv.DictReader(f))

# Deterministic sort
rows.sort(key=lambda r: (r["tier"], r["domain"], r["email"]))

# Round-robin variants
assigned = []
inbox_counters = {v: 0 for v in VARIANTS}
for i, r in enumerate(rows):
    v = VARIANTS[i % len(VARIANTS)]
    inbox_idx = inbox_counters[v] % 2
    inbox = INBOXES[v][inbox_idx]
    r["variant_id"] = v
    r["assigned_inbox"] = inbox
    inbox_counters[v] += 1
    assigned.append(r)

# Sort final by variant + inbox + email for clean CSV
assigned.sort(key=lambda r: (r["variant_id"], r["assigned_inbox"], r["email"]))

cols = list(assigned[0].keys())
with OUT.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in assigned:
        w.writerow(r)

# Report
from collections import Counter
print(f"Wrote {len(assigned)} rows to {OUT.relative_to(ROOT)}")
print()
print("Per-variant distribution:")
for v in VARIANTS:
    n = sum(1 for r in assigned if r["variant_id"] == v)
    print(f"  {v}: {n}")
print()
print("Per-inbox distribution:")
inbox_counts = Counter(r["assigned_inbox"] for r in assigned)
for inbox, n in sorted(inbox_counts.items()):
    print(f"  {inbox:35s} {n}")
print()
print("Max sends per inbox:", max(inbox_counts.values()))
assert max(inbox_counts.values()) <= 20, "Sanity check failed: inbox exceeds 20-send cap"
print("Sanity check passed: no inbox exceeds 20-send cap")
