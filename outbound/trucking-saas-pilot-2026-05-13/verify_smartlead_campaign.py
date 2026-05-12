import os
import requests

API_KEY = os.environ["SMARTLEAD_API_KEY"]
BASE = "https://server.smartlead.ai/api/v1"
CAMPAIGN_ID = 3326039


def get(endpoint, **params):
    params["api_key"] = API_KEY
    response = requests.get(f"{BASE}{endpoint}", params=params, timeout=30)
    print(endpoint, response.status_code)
    response.raise_for_status()
    return response.json()


campaign = get(f"/campaigns/{CAMPAIGN_ID}")
print("campaign", {k: campaign.get(k) for k in ["id", "name", "status", "is_active"]})

sequences = get(f"/campaigns/{CAMPAIGN_ID}/sequences")
seq_data = sequences.get("data", sequences) if isinstance(sequences, dict) else sequences
if isinstance(seq_data, dict):
    seq_data = seq_data.get("data") or seq_data.get("sequences") or []
print("sequence_count", len(seq_data) if isinstance(seq_data, list) else type(seq_data))
if isinstance(seq_data, list):
    for sequence in seq_data:
        print("sequence", sequence.get("id"), sequence.get("seq_number"), sequence.get("subject"))

accounts = get(f"/campaigns/{CAMPAIGN_ID}/email-accounts")
account_data = accounts.get("data", accounts) if isinstance(accounts, dict) else accounts
print("sender_count", len(account_data) if isinstance(account_data, list) else type(account_data))
if isinstance(account_data, list):
    print("senders", [account.get("from_email") for account in account_data])

leads = get(f"/campaigns/{CAMPAIGN_ID}/leads", offset=0, limit=20)
print("total_leads", leads.get("total_leads"))
for item in leads.get("data", []):
    lead = item.get("lead", {})
    fields = lead.get("custom_fields", {})
    print(
        "lead",
        lead.get("company_name"),
        lead.get("email"),
        "assigned_sender=" + str(fields.get("assigned_sender")),
        "status=" + str(item.get("status")),
    )
