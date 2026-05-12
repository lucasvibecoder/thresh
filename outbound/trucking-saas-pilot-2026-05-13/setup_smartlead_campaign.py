import csv
import html
import json
import os
import time
import warnings
from pathlib import Path

import requests

warnings.filterwarnings("ignore")

API_KEY = os.environ["SMARTLEAD_API_KEY"]
BASE = "https://server.smartlead.ai/api/v1"
CAMPAIGN_NAME = "Thresh - Trucking SaaS Mini-PVP - 2026-05-13"
ROOT = Path("/Users/lucas/Documents/projects/thresh/outbound/trucking-saas-pilot-2026-05-13")
CSV_PATH = ROOT / "smartlead-import.csv"
STATE_PATH = ROOT / "smartlead-state.json"

EXCLUDE_EMAILS = {"lucas.linares@runthresh.com"}
ALL_ALLOWED_SENDERS = [
    "lucas.l@threshworks.com",
    "l@threshworks.com",
    "lucas@threshworks.com",
    "lucas.l@withthresh.com",
    "l@withthresh.com",
    "lucas@withthresh.com",
    "lucas.l@threshhq.com",
    "l@threshhq.com",
    "lucas@threshhq.com",
]
LEAD_SENDER_ORDER = [
    "lucas.l@threshworks.com",
    "l@withthresh.com",
    "lucas.l@threshhq.com",
    "l@threshworks.com",
    "lucas@withthresh.com",
]


def request_json(method, endpoint, **kwargs):
    params = kwargs.pop("params", {}) or {}
    params["api_key"] = API_KEY
    response = requests.request(
        method,
        f"{BASE}{endpoint}",
        params=params,
        timeout=45,
        **kwargs,
    )
    try:
        data = response.json()
    except Exception:
        data = {"raw": response.text[:1000]}

    if response.status_code >= 400:
        raise RuntimeError(
            f"{method} {endpoint} failed {response.status_code}: "
            f"{json.dumps(data)[:1200]}"
        )
    return data


def payload_data(value):
    if isinstance(value, dict) and "data" in value:
        return value["data"]
    return value


def load_import_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def email_body_html():
    lines = [
        "{{opener_line}}",
        "",
        "I pulled 3 carriers in that pattern:",
        "",
        "- {{carrier_1}}",
        "- {{carrier_2}}",
        "- {{carrier_3}}",
        "",
        "{{architecture_line}}",
        "",
        "{{cta}}",
    ]
    return "<p>" + "<br>".join(html.escape(line) for line in lines) + "</p>"


def get_existing_sequence_id(campaign_id):
    data = request_json("GET", f"/campaigns/{campaign_id}/sequences")
    sequences = payload_data(data)
    if isinstance(sequences, dict):
        for key in ("sequences", "results", "data"):
            if isinstance(sequences.get(key), list):
                sequences = sequences[key]
                break
    if not isinstance(sequences, list):
        return None

    for sequence in sequences:
        if sequence.get("seq_number") == 1:
            return sequence.get("id")
    return None


def list_campaigns():
    data = request_json("GET", "/campaigns")
    campaigns = payload_data(data)
    return campaigns if isinstance(campaigns, list) else []


def find_campaign_by_name():
    for campaign in list_campaigns():
        if campaign.get("name") == CAMPAIGN_NAME:
            return campaign
    return None


def get_or_create_campaign():
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text())
            if state.get("campaign_id"):
                return {"id": state["campaign_id"], "name": CAMPAIGN_NAME}
        except Exception:
            pass

    existing = find_campaign_by_name()
    if existing:
        campaign_id = existing.get("id")
        STATE_PATH.write_text(json.dumps({"campaign_id": campaign_id}, indent=2))
        return existing

    campaign = request_json("POST", "/campaigns/create", json={"name": CAMPAIGN_NAME})
    campaign_id = campaign.get("id") or campaign.get("data", {}).get("id")
    if not campaign_id:
        raise RuntimeError(f"No campaign id returned: {campaign}")
    STATE_PATH.write_text(json.dumps({"campaign_id": campaign_id}, indent=2))
    return {"id": campaign_id, "name": CAMPAIGN_NAME}


def account_lookup():
    accounts = payload_data(request_json("GET", "/email-accounts"))
    lookup = {}
    for account in accounts:
        email = (account.get("from_email") or account.get("email") or "").lower()
        if email:
            lookup[email] = account
    return lookup


def lead_payloads(rows):
    leads = []
    assignments = []
    for index, row in enumerate(rows):
        sender_email = LEAD_SENDER_ORDER[index % len(LEAD_SENDER_ORDER)]
        lead = {
            "email": row["email"].lower(),
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "company_name": row["company_name"],
            "website": row["domain"],
            "company_url": row["domain"],
            "custom_fields": {
                "subject": row["subject"],
                "opener_line": row["opener_line"],
                "carrier_1": row["carrier_1"],
                "carrier_2": row["carrier_2"],
                "carrier_3": row["carrier_3"],
                "architecture_line": row["architecture_line"],
                "cta": row["cta"],
                "bucket": row["bucket"],
                "contact_title": row["contact_title"],
                "sales_team_structure": row["sales_team_structure"],
                "assigned_sender": sender_email,
                "pilot_date": "2026-05-13",
            },
        }
        leads.append(lead)
        assignments.append(
            {
                "email": lead["email"],
                "company_name": row["company_name"],
                "sender_email": sender_email,
            }
        )
    return leads, assignments


def extract_lead_ids(response):
    if isinstance(response, dict):
        if isinstance(response.get("lead_ids"), list):
            return response["lead_ids"]
        data = response.get("data")
        if isinstance(data, dict) and isinstance(data.get("lead_ids"), list):
            return data["lead_ids"]
    return []


def fetch_campaign_leads(campaign_id):
    data = request_json(
        "GET",
        f"/campaigns/{campaign_id}/leads",
        params={"offset": 0, "limit": 100},
    )
    leads = payload_data(data)
    if isinstance(leads, dict):
        for key in ("leads", "results", "data"):
            if isinstance(leads.get(key), list):
                return leads[key]
    return leads if isinstance(leads, list) else []


def main():
    print("Inspecting import CSV")
    rows = load_import_rows()
    print(f"lead_count={len(rows)}")

    print("Fetching sender accounts")
    accounts = account_lookup()
    missing = [email for email in ALL_ALLOWED_SENDERS if email not in accounts]
    if missing:
        raise RuntimeError(f"Missing expected sender accounts: {missing}")

    allowed_senders = [
        email
        for email in ALL_ALLOWED_SENDERS
        if email in accounts and email not in EXCLUDE_EMAILS
    ]
    print("allowed_senders=" + ",".join(allowed_senders))

    campaign = get_or_create_campaign()
    campaign_id = campaign.get("id")
    print(f"campaign_id={campaign_id}")

    print("Linking all 9 non-main sender accounts")
    request_json(
        "POST",
        f"/campaigns/{campaign_id}/email-accounts",
        json={"email_account_ids": [accounts[email]["id"] for email in allowed_senders]},
    )

    print("Saving one-step sequence")
    existing_sequence_id = get_existing_sequence_id(campaign_id)
    request_json(
        "POST",
        f"/campaigns/{campaign_id}/sequences",
        json={
            "sequences": [
                {
                    "id": existing_sequence_id,
                    "seq_number": 1,
                    "subject": "{{subject}}",
                    "email_body": email_body_html(),
                    "seq_delay_details": {"delay_in_days": 0},
                }
            ]
        },
    )

    print("Saving Wednesday schedule")
    schedule = {
        "timezone": "America/New_York",
        "days_of_the_week": [3],
        "start_hour": "09:00",
        "end_hour": "15:00",
        "min_time_btw_emails": 75,
        "max_new_leads_per_day": 5,
    }
    request_json("POST", f"/campaigns/{campaign_id}/schedule", json=schedule)

    print("Saving campaign settings")
    request_json(
        "POST",
        f"/campaigns/{campaign_id}/settings",
        json={
            "name": CAMPAIGN_NAME,
            "track_settings": ["DONT_TRACK_EMAIL_OPEN", "DONT_TRACK_LINK_CLICK"],
            "stop_lead_settings": "REPLY_TO_AN_EMAIL",
            "send_as_plain_text": True,
            "force_plain_text": True,
            "follow_up_percentage": 0,
            "enable_ai_esp_matching": False,
            "auto_pause_domain_leads_on_reply": True,
            "domain_level_rate_limit": True,
        },
    )

    print("Pushing leads")
    leads, assignments = lead_payloads(rows)
    lead_response = request_json(
        "POST",
        f"/campaigns/{campaign_id}/leads",
        json={
            "lead_list": leads,
            "settings": {
                "ignore_duplicate_leads_in_other_campaign": False,
                "return_lead_ids": True,
            },
        },
    )
    lead_ids = extract_lead_ids(lead_response)

    if len(lead_ids) != len(assignments):
        print("Lead IDs not returned cleanly; fetching campaign leads")
        campaign_leads = fetch_campaign_leads(campaign_id)
        by_email = {}
        for lead in campaign_leads:
            nested_lead = lead.get("lead") if isinstance(lead.get("lead"), dict) else {}
            email = (
                lead.get("email")
                or lead.get("lead_email")
                or nested_lead.get("email")
                or ""
            ).lower()
            lead_id = (
                nested_lead.get("id")
                or lead.get("email_lead_id")
                or lead.get("id")
                or lead.get("lead_id")
                or lead.get("campaign_lead_map_id")
            )
            if email and lead_id:
                by_email[email] = lead_id
        lead_ids = [by_email.get(item["email"]) for item in assignments]

    if any(lead_id is None for lead_id in lead_ids) or len(lead_ids) != len(assignments):
        raise RuntimeError(f"Could not resolve all lead IDs: {lead_ids}")

    print("Assigning lead-specific sender accounts")
    for lead_id, assignment in zip(lead_ids, assignments):
        sender = accounts[assignment["sender_email"]]
        assignment["lead_id"] = lead_id
        assignment["sender_id"] = sender["id"]
        request_json(
            "POST",
            "/campaigns/update-lead-email-account",
            json={
                "email_account_id": sender["id"],
                "email_campaign_id": campaign_id,
                "email_lead_id": lead_id,
                "override_lead_email_account": True,
            },
        )
        print(
            f"assigned {assignment['company_name']} -> "
            f"{assignment['sender_email']} (lead {lead_id})"
        )
        time.sleep(0.2)

    summary = {
        "campaign_id": campaign_id,
        "campaign_name": CAMPAIGN_NAME,
        "status": "configured_not_started",
        "allowed_senders": [
            {"id": accounts[email]["id"], "email": email} for email in allowed_senders
        ],
        "lead_assignments": assignments,
        "schedule": schedule,
        "settings": {
            "open_tracking": False,
            "click_tracking": False,
            "stop_on_reply": True,
            "plain_text": True,
            "followups_loaded": 0,
            "main_domain_excluded": True,
        },
    }
    print("SUMMARY_JSON_START")
    print(json.dumps(summary, indent=2))
    print("SUMMARY_JSON_END")


if __name__ == "__main__":
    main()
