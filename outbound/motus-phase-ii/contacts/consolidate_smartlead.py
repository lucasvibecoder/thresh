"""Consolidate 5 sub-campaigns into 1 SmartLead campaign with 5 variants.

Steps:
1. Delete the existing 5 sub-campaigns
2. Create one parent campaign
3. Attach all 10 inboxes
4. Save sequence with 5 variants in one step
5. Set schedule (Mon-Fri 9-17 ET, 8min gap, 20/day, start Tue 2026-05-12 9am ET)
6. Set tracking settings
7. Push all 14 leads
"""
import csv, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_CAMPAIGN_IDS = {
    "v1": 3319867,
    "v2": 3319878,
    "v3": 3319879,
    "v4": 3319880,
    "v5": 3319881,
}

ALL_INBOX_IDS = [
    16019860,  # lucas.l@threshworks.com
    16019830,  # l@threshworks.com
    16019801,  # lucas@threshworks.com
    16019787,  # lucas.l@withthresh.com
    16019779,  # l@withthresh.com
    16019763,  # lucas@withthresh.com
    16019725,  # lucas.l@threshhq.com
    16019517,  # l@threshhq.com
    16019409,  # lucas@threshhq.com
    15888000,  # lucas.linares@runthresh.com
]

VARIANT_FILES = {
    "v1": ROOT / "outbound" / "cold-email-v1.md",
    "v2": ROOT / "outbound" / "variants" / "v2.md",
    "v3": ROOT / "outbound" / "variants" / "v3.md",
    "v4": ROOT / "outbound" / "variants" / "v4.md",
    "v5": ROOT / "outbound" / "variants" / "v5.md",
}

VARIANT_LABELS = {"v1": "A", "v2": "B", "v3": "C", "v4": "D", "v5": "E"}

SCHEDULE_PAYLOAD = {
    "timezone": "America/New_York",
    "days_of_the_week": [1, 2, 3, 4, 5],
    "start_hour": "09:00",
    "end_hour": "17:00",
    "min_time_btw_emails": 8,
    "max_new_leads_per_day": 20,
    "schedule_start_time": "2026-05-12T09:00:00-04:00",  # Tue 5/12 9am ET
}

SETTINGS_PAYLOAD = {
    "track_settings": ["DONT_TRACK_LINK_CLICK"],
    "stop_lead_settings": "REPLY_TO_AN_EMAIL",
    "follow_up_percentage": 0,
    "send_as_plain_text": False,
}


def run_tool(tool, payload):
    result = subprocess.run(
        ["deepline", "tools", "execute", tool, "--payload", json.dumps(payload)],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{tool} failed (rc={result.returncode}):\n{result.stdout}\n{result.stderr}")
    txt = result.stdout
    idx = txt.find("Result:")
    if idx < 0:
        raise RuntimeError(f"{tool}: no Result block:\n{txt[:2000]}")
    return json.loads(txt[idx + len("Result:"):])


def extract_subject_body(md_path):
    text = md_path.read_text()
    sub_match = re.search(r"## Subject\s*\n+```\s*\n(.+?)\n```", text, re.S)
    body_match = re.search(r"## Body\s*\n+```\s*\n(.+?)\n```", text, re.S)
    return sub_match.group(1).strip(), body_match.group(1).strip()


def body_to_html(body):
    paragraphs = re.split(r"\n\s*\n", body.strip())
    out = []
    for p in paragraphs:
        flat = re.sub(r"\s*\n\s*", " ", p.strip())
        out.append(f"<p>{flat}</p>")
    return "\n".join(out)


def load_all_leads():
    """Load all 14 leads from contacts-final.csv (no variant filter — SmartLead distributes)."""
    leads = []
    with (ROOT / "contacts" / "contacts-final.csv").open() as f:
        for r in csv.DictReader(f):
            leads.append({
                "email": r["email"],
                "first_name": r["first_name"],
                "last_name": r["last_name"],
                "company_name": r["company_name"],
                "linkedin_profile": r.get("linkedin_url", ""),
                "custom_fields": {
                    "title": r["title"],
                    "tier": r["tier"],
                    "domain": r["domain"],
                },
            })
    return leads


def main():
    # 1. Delete old sub-campaigns
    print("=" * 60)
    print("STEP 1: Delete 5 old sub-campaigns")
    print("=" * 60)
    for v, cid in OLD_CAMPAIGN_IDS.items():
        try:
            run_tool("smartlead_delete_campaign", {"campaign_id": cid})
            print(f"  deleted {v} (id={cid})")
        except Exception as e:
            print(f"  FAILED to delete {v} (id={cid}): {e}")

    # 2. Create parent campaign
    print()
    print("=" * 60)
    print("STEP 2: Create consolidated campaign")
    print("=" * 60)
    r = run_tool("smartlead_create_campaign", {"name": "Motus Phase II — Factoring"})
    campaign_id = r.get("data", {}).get("id") or r.get("id")
    if not campaign_id:
        print(f"RAW: {json.dumps(r, indent=2)[:1000]}")
        raise RuntimeError("Could not extract campaign_id")
    print(f"  campaign_id = {campaign_id}")

    # 3. Attach all 10 inboxes
    print()
    print("=" * 60)
    print("STEP 3: Attach all 10 inboxes")
    print("=" * 60)
    run_tool("smartlead_add_campaign_email_account", {
        "campaign_id": campaign_id,
        "email_account_ids": ALL_INBOX_IDS,
    })
    print(f"  attached {len(ALL_INBOX_IDS)} inboxes")

    # 4. Save sequence with 5 variants
    print()
    print("=" * 60)
    print("STEP 4: Save sequence with 5 variants")
    print("=" * 60)
    seq_variants = []
    for v in ["v1", "v2", "v3", "v4", "v5"]:
        subject, body = extract_subject_body(VARIANT_FILES[v])
        seq_variants.append({
            "subject": subject,
            "email_body": body_to_html(body),
            "variant_label": VARIANT_LABELS[v],
        })
        print(f"  variant {VARIANT_LABELS[v]} ({v}): subject='{subject}'")
    run_tool("smartlead_save_campaign_sequences", {
        "campaign_id": campaign_id,
        "sequences": [{
            "seq_number": 1,
            "seq_delay_details": {"delay_in_days": 0},
            "seq_variants": seq_variants,
        }],
    })
    print(f"  saved 1 sequence step with {len(seq_variants)} variants")

    # 5. Schedule with start date
    print()
    print("=" * 60)
    print("STEP 5: Set schedule (start Tue 2026-05-12 9am ET)")
    print("=" * 60)
    run_tool("smartlead_update_campaign_schedule", {"campaign_id": campaign_id, **SCHEDULE_PAYLOAD})
    print(f"  Mon-Fri 9-17 ET, 8min gap, 20/day, start=2026-05-12T09:00 ET")

    # 6. Settings
    print()
    print("=" * 60)
    print("STEP 6: Set tracking + stop-on-reply")
    print("=" * 60)
    run_tool("smartlead_update_campaign_settings", {"campaign_id": campaign_id, **SETTINGS_PAYLOAD})
    print(f"  open ON, click OFF, stop-on-reply ON, no follow-up")

    # 7. Push leads
    print()
    print("=" * 60)
    print("STEP 7: Push all 14 leads")
    print("=" * 60)
    leads = load_all_leads()
    push_r = run_tool("smartlead_push_to_campaign", {
        "campaign_id": campaign_id,
        "lead_list": leads,
    })
    print(f"  pushed: {json.dumps(push_r.get('data', push_r))[:200]}")

    print()
    print("=" * 60)
    print("DONE — consolidated campaign in DRAFT state")
    print("=" * 60)
    print(f"  Campaign ID: {campaign_id}")
    print(f"  Inboxes: 10")
    print(f"  Variants: 5 (A=v1, B=v2, C=v3, D=v4, E=v5)")
    print(f"  Leads: {len(leads)}")
    print(f"  Schedule: Mon-Fri 9-17 ET, start Tue 2026-05-12 9am ET")
    print(f"  Status: DRAFTED — click Review and Launch in UI when ready")


if __name__ == "__main__":
    main()
