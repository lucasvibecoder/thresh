"""Push 5 Motus Phase II sub-campaigns into SmartLead in DRAFT state.

Per-variant: create campaign → attach 2 inboxes → save subject+body → set schedule → set tracking → push leads.

DOES NOT launch any campaign. Sub-campaigns stay in DRAFTED state for Lucas to launch from UI.
"""
import csv, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VARIANT_INBOXES = {
    "v1": (16019860, 16019787),  # lucas.l@threshworks, lucas.l@withthresh
    "v2": (16019830, 16019779),  # l@threshworks,        l@withthresh
    "v3": (16019801, 16019763),  # lucas@threshworks,    lucas@withthresh
    "v4": (16019725, 15888000),  # lucas.l@threshhq,     lucas.linares@runthresh
    "v5": (16019517, 16019409),  # l@threshhq,           lucas@threshhq
}

VARIANT_FILES = {
    "v1": ROOT / "outbound" / "cold-email-v1.md",
    "v2": ROOT / "outbound" / "variants" / "v2.md",
    "v3": ROOT / "outbound" / "variants" / "v3.md",
    "v4": ROOT / "outbound" / "variants" / "v4.md",
    "v5": ROOT / "outbound" / "variants" / "v5.md",
}

SCHEDULE_PAYLOAD = {
    "timezone": "America/New_York",
    "days_of_the_week": [1, 2, 3, 4, 5],  # Mon-Fri
    "start_hour": "09:00",
    "end_hour": "17:00",
    "min_time_btw_emails": 8,
    "max_new_leads_per_day": 20,
}

SETTINGS_PAYLOAD = {
    "track_settings": ["DONT_TRACK_LINK_CLICK"],  # open tracking ON, click tracking OFF
    "stop_lead_settings": "REPLY_TO_AN_EMAIL",  # stop on reply
    "follow_up_percentage": 0,
    "send_as_plain_text": False,
}


def run_tool(tool, payload):
    """Execute a Deepline tool; return parsed JSON result or raise."""
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
    # Subject = first fenced block under ## Subject
    sub_match = re.search(r"## Subject\s*\n+```\s*\n(.+?)\n```", text, re.S)
    body_match = re.search(r"## Body\s*\n+```\s*\n(.+?)\n```", text, re.S)
    if not sub_match or not body_match:
        raise ValueError(f"Could not extract subject/body from {md_path}")
    subject = sub_match.group(1).strip()
    body = body_match.group(1).strip()
    return subject, body


def body_to_html(body):
    """SmartLead expects HTML — convert newlines, preserve paragraph breaks."""
    paragraphs = re.split(r"\n\s*\n", body.strip())
    html_paragraphs = []
    for p in paragraphs:
        # Within a paragraph, join wrapped lines into a single line (clean up the markdown hard-wraps)
        flat = re.sub(r"\s*\n\s*", " ", p.strip())
        html_paragraphs.append(f"<p>{flat}</p>")
    return "\n".join(html_paragraphs)


def load_leads(variant):
    leads = []
    with (ROOT / "contacts" / f"leads-{variant}.csv").open() as f:
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
                    "variant_id": r["variant_id"],
                    "assigned_inbox": r["assigned_inbox"],
                },
            })
    return leads


def push_variant(variant):
    print(f"\n{'=' * 60}")
    print(f"VARIANT: {variant}")
    print(f"{'=' * 60}")

    subject, body = extract_subject_body(VARIANT_FILES[variant])
    body_html = body_to_html(body)
    leads = load_leads(variant)
    inbox_a, inbox_b = VARIANT_INBOXES[variant]

    print(f"  Subject: {subject}")
    print(f"  Body preview: {body[:80]}...")
    print(f"  Leads: {len(leads)}")
    print(f"  Inboxes: {inbox_a}, {inbox_b}")

    # 1. Create campaign
    print(f"\n  [1/6] Creating campaign...")
    r = run_tool("smartlead_create_campaign", {"name": f"Motus Phase II — {variant}"})
    campaign_id = r.get("data", {}).get("id") or r.get("id") or (r.get("data", [{}])[0] if isinstance(r.get("data"), list) else None)
    if not campaign_id:
        # Try other shapes
        campaign_id = r.get("campaign", {}).get("id") if isinstance(r.get("campaign"), dict) else None
    if not campaign_id:
        print(f"    RAW RESPONSE: {json.dumps(r, indent=2)[:1000]}")
        raise RuntimeError("Could not extract campaign_id")
    print(f"    campaign_id = {campaign_id}")

    # 2. Attach inboxes
    print(f"  [2/6] Attaching inboxes...")
    run_tool("smartlead_add_campaign_email_account", {
        "campaign_id": campaign_id,
        "email_account_ids": [inbox_a, inbox_b],
    })
    print(f"    attached {inbox_a}, {inbox_b}")

    # 3. Save sequence (subject + body)
    print(f"  [3/6] Saving sequence...")
    seq_payload = {
        "campaign_id": campaign_id,
        "sequences": [{
            "seq_number": 1,
            "seq_delay_details": {"delay_in_days": 0},
            "seq_variants": [{
                "subject": subject,
                "email_body": body_html,
                "variant_label": "A",
            }],
        }],
    }
    run_tool("smartlead_save_campaign_sequences", seq_payload)
    print(f"    sequence saved")

    # 4. Set schedule
    print(f"  [4/6] Setting schedule...")
    run_tool("smartlead_update_campaign_schedule", {"campaign_id": campaign_id, **SCHEDULE_PAYLOAD})
    print(f"    Mon-Fri 9-17 ET, 8min gap, 20/day cap")

    # 5. Set tracking + stop conditions
    print(f"  [5/6] Setting tracking + stop conditions...")
    run_tool("smartlead_update_campaign_settings", {"campaign_id": campaign_id, **SETTINGS_PAYLOAD})
    print(f"    open tracking ON, click tracking OFF, stop-on-reply ON")

    # 6. Push leads
    print(f"  [6/6] Pushing {len(leads)} leads...")
    push_result = run_tool("smartlead_push_to_campaign", {
        "campaign_id": campaign_id,
        "lead_list": leads,
    })
    print(f"    leads pushed (raw: {json.dumps(push_result.get('data', push_result))[:200]})")

    return {
        "variant": variant,
        "campaign_id": campaign_id,
        "leads_pushed": len(leads),
        "inboxes": [inbox_a, inbox_b],
        "subject": subject,
    }


def main():
    results = []
    variants_to_run = sys.argv[1:] if len(sys.argv) > 1 else ["v1", "v2", "v3", "v4", "v5"]
    for v in variants_to_run:
        try:
            results.append(push_variant(v))
        except Exception as e:
            print(f"\nFAILED on {v}: {e}")
            results.append({"variant": v, "error": str(e)})

    print(f"\n\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    for r in results:
        if "error" in r:
            print(f"  {r['variant']}: FAILED — {r['error'][:100]}")
        else:
            print(f"  {r['variant']}: campaign_id={r['campaign_id']}, leads={r['leads_pushed']}, inboxes={r['inboxes']}, subject='{r['subject']}'")

    print(f"\nAll campaigns left in DRAFTED state. Launch manually from SmartLead UI.")


if __name__ == "__main__":
    main()
