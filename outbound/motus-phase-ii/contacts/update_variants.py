"""Update campaign 3319888 sequence: 4 variants (A-D) instead of 5.
- B body: 'next month' -> 'after cutover'
- D body: 'those fail' -> 'those can fail'
- E: dropped entirely
"""
import json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAMPAIGN_ID = 3319888

VARIANT_FILES = {
    "A": ROOT / "outbound" / "cold-email-v1.md",
    "B": ROOT / "outbound" / "variants" / "v2.md",
    "C": ROOT / "outbound" / "variants" / "v3.md",
    "D": ROOT / "outbound" / "variants" / "v4.md",
}


def run_tool(tool, payload):
    r = subprocess.run(
        ["deepline", "tools", "execute", tool, "--payload", json.dumps(payload)],
        capture_output=True, text=True, timeout=120,
    )
    if r.returncode != 0:
        raise RuntimeError(f"{tool} failed:\n{r.stdout}\n{r.stderr}")
    idx = r.stdout.find("Result:")
    return json.loads(r.stdout[idx + len("Result:"):])


def extract_subject_body(md):
    text = md.read_text()
    s = re.search(r"## Subject\s*\n+```\s*\n(.+?)\n```", text, re.S).group(1).strip()
    b = re.search(r"## Body\s*\n+```\s*\n(.+?)\n```", text, re.S).group(1).strip()
    return s, b


def body_to_html(body):
    parts = re.split(r"\n\s*\n", body.strip())
    out = []
    for p in parts:
        flat = re.sub(r"\s*\n\s*", " ", p.strip())
        out.append(f"<p>{flat}</p>")
    return "\n".join(out)


seq_variants = []
for label, path in VARIANT_FILES.items():
    s, b = extract_subject_body(path)
    seq_variants.append({
        "subject": s,
        "email_body": body_to_html(b),
        "variant_label": label,
    })
    print(f"variant {label}: {s}")

print(f"\nPushing 4 variants to campaign {CAMPAIGN_ID} (E removed, B + D edited)...")
run_tool("smartlead_save_campaign_sequences", {
    "campaign_id": CAMPAIGN_ID,
    "sequences": [{
        "seq_number": 1,
        "seq_delay_details": {"delay_in_days": 0},
        "seq_variants": seq_variants,
    }],
})
print("Done.")

# Verify
print("\nVerifying...")
result = run_tool("smartlead_fetch_campaign_sequences", {"campaign_id": CAMPAIGN_ID})
sequences = result if isinstance(result, list) else result.get("data", [])
for seq in (sequences if isinstance(sequences, list) else [sequences]):
    if isinstance(seq, dict):
        vs = seq.get("seq_variants", [])
        print(f"  step {seq.get('seq_number','?')}: {len(vs)} variants")
        for v in vs:
            print(f"    {v.get('variant_label','?')}: {v.get('subject','?')}")
