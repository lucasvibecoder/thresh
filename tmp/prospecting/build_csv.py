import csv

# Cold emails drafted in Lucas's voice. Format: cite signal -> implication -> what I do -> CTA.
# ~100 words, no em dashes, no fluff openers, lowercase subjects 3-5 words.

rows = [
    {
        "company": "Keebler Health",
        "domain": "keebler.health",
        "vertical": "Healthcare / Medicare risk adjustment",
        "signal": "Series A $22M (2026-04-15)",
        "public_data_angle": "CMS HCC coding files, MA Star Ratings, state MA enrollment shifts",
        "first_name": "Isaac",
        "last_name": "Park",
        "title": "CEO, Co-Founder",
        "email": "isaac@keebler.health",
        "linkedin": "https://www.linkedin.com/in/isaacpark",
        "send_priority": 1,
        "subject": "cms hcc data",
        "body": """Hey Isaac,

Saw the $22M Series A. Congrats.

Risk adjustment is the cleanest signal-data pitch I've seen this year. Your buyers (MA plans, at-risk providers) show up in CMS HCC files, Star Ratings, and state MA enrollment shifts. All public.

Most teams pitching them lead with "AI-first." Yours could lead with their actual coding gaps, by plan, by quarter.

I build signal-based prospect lists for companies selling into regulated verticals.

Worth a quick look?

Cheers,
Lucas""",
    },
    {
        "company": "Sunbound",
        "domain": "sunboundhomes.com",
        "vertical": "Senior care fintech",
        "signal": "Series A (2026-04-14)",
        "public_data_angle": "CMS Care Compare, Five-Star deficiencies, state survey citations, Provider of Services file",
        "first_name": "Manny",
        "last_name": "Cominsky",
        "title": "CEO",
        "email": "manny@sunboundhomes.com",
        "linkedin": "https://www.linkedin.com/in/mcominsky",
        "send_priority": 1,
        "subject": "cms five-star signals",
        "body": """Hey Manny,

Saw the Series A.

Senior care is one of the few verticals where your buyer's operational pain is graded publicly every quarter. CMS Five-Star deficiencies, state survey citations, days-cash-on-hand for non-profits. All public, all predictive of who needs you next.

Most outbound to SNFs is generic. Yours could be "we noticed your last survey flagged X."

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what this looks like for senior care?

Cheers,
Lucas""",
    },
    {
        "company": "Coral",
        "domain": "trycoral.ai",
        "vertical": "Healthcare provider automation",
        "signal": "Seed $12.5M (2026-04-20)",
        "public_data_angle": "CMS Compare, HCAHPS, prior-auth denial rates by payor",
        "first_name": "Ajay",
        "last_name": "Shrihari",
        "title": "Founder",
        "email": "ajay@trycoral.ai",
        "linkedin": "https://www.linkedin.com/in/ajay-shrihari",
        "send_priority": 2,
        "subject": "provider denial data",
        "body": """Hey Ajay,

Congrats on the $12.5M.

You're going after the right buyer. Provider orgs are measured publicly on HCAHPS, CMS Compare, prior-auth denial rates by payor. Same pain points your platform fixes.

Most teams pitching health systems use the same enterprise sales motion. Yours could rank prospects by their actual measured denial rate.

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what one of these looks like?

Cheers,
Lucas""",
    },
    {
        "company": "Ethermed",
        "domain": "ethermed.ai",
        "vertical": "Healthcare prior authorization",
        "signal": "Series A $8.5M (2026-04-16)",
        "public_data_angle": "CMS denial rate data, appeals win rates, payor policy changes, state DOI filings",
        "first_name": "Daniel",
        "last_name": "Friedman",
        "title": "CEO, Co-Founder",
        "email": "dan@ethermed.ai",
        "linkedin": "https://www.linkedin.com/in/dfriedm",
        "send_priority": 2,
        "subject": "prior auth signals",
        "body": """Hey Dan,

Saw the Series A.

Prior auth is a vertical where the buyer's pain is literally a CMS dataset. Denial rates by plan, by service category, by state. Public. So are appeals win rates.

Plenty of room to rank prospects by actual measured pain instead of generic firmographics.

I build signal-based prospect lists for companies selling into regulated verticals.

Worth showing you what this looks like for payor outreach?

Cheers,
Lucas""",
    },
    {
        "company": "Joyful Health",
        "domain": "joyfulhealth.io",
        "vertical": "Healthcare revenue cycle / RCM",
        "signal": "Series A $22M (2026-04-16)",
        "public_data_angle": "CMS physician billing PUF, denial patterns by specialty, Medicare claims",
        "first_name": "Eliana",
        "last_name": "Berger",
        "title": "CEO, Co-Founder",
        "email": "eliana@joyfulhealth.io",
        "linkedin": "https://www.linkedin.com/in/elianaberger",
        "send_priority": 1,
        "subject": "medicare claims signals",
        "body": """Hey Eliana,

Saw the $22M.

Your pitch is "we recover 5-10x our fees." That's quantified pain. Medicare claims data is public. So are denial rates by specialty. So is which practices are leaving money on the table.

Most outbound to practices is "AI-powered RCM" generic. Yours could be "we ran your claims, here's the leak."

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what one looks like for healthcare practices?

Cheers,
Lucas""",
    },
    {
        "company": "HeyDonto",
        "domain": "heydonto.com",
        "vertical": "Healthcare / dental data intelligence",
        "signal": "Seed $20M at $200M val (2026-04-07)",
        "public_data_angle": "State dental boards, CMS Medicaid dental utilization, FDA recalls, payor network changes",
        "first_name": "Rivers",
        "last_name": "Morrell",
        "title": "Founder, CEO",
        "email": "rivers@heydonto.com",
        "linkedin": "",
        "send_priority": 1,
        "subject": "dental interop signals",
        "body": """Hey Rivers,

$20M at $200M val. Congrats.

Dental and health interop is one of the verticals where buyers leave a public trail: state dental boards, CMS Medicaid dental utilization, FDA recalls, payor network changes. All sourceable.

Most outbound to dental orgs is generic. Yours could lead with the specific data leak each org cares about.

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what one looks like for dental?

Cheers,
Lucas""",
    },
    {
        "company": "Vibrant Practice",
        "domain": "vibrantpractice.com",
        "vertical": "Functional / longevity medicine SaaS",
        "signal": "Seed $9.3M (2026-04-13)",
        "public_data_angle": "State medical boards, CMS Open Payments, NPI registry changes, clinician hire patterns",
        "first_name": "Sunita",
        "last_name": "Mohanty",
        "title": "CEO, Co-Founder",
        "email": "sunita@vibrantpractice.com",
        "linkedin": "https://www.linkedin.com/in/sunita-mohanty-0843b0",
        "send_priority": 3,
        "subject": "clinic growth signals",
        "body": """Hey Sunita,

Saw the $9.3M seed.

Functional and longevity clinics are fragmented, but their growth shows up in public data: state med board licenses, CMS Open Payments, NPI registry changes, new clinician hires.

Plenty of signal to find practices about to outgrow whatever they're using now.

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what this looks like for functional medicine?

Cheers,
Lucas""",
    },
    {
        "company": "Primepoint",
        "domain": "primepoint.ai",
        "vertical": "Construction intelligence / GC SaaS",
        "signal": "Seed $10M (2026-04-13)",
        "public_data_angle": "OSHA violations, building permits, ENR rankings, jobsite incident reports",
        "first_name": "Lubomir",
        "last_name": "Bourdev",
        "title": "CEO, Co-Founder",
        "email": "lubomir@primepoint.ai",
        "linkedin": "https://www.linkedin.com/in/lubomir-bourdev-51a8652",
        "send_priority": 1,
        "subject": "gc safety data",
        "body": """Hey Lubomir,

Saw the $10M seed.

Construction is one of the cleanest verticals for signal-based outbound. OSHA violations, building permits, ENR rankings, jobsite incident reports. All public. You can rank GCs by who's actually losing money on rework right now.

Most outbound to construction is "schedule a demo." Yours could be "we saw your last 3 OSHA citations were drawing-related."

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what this looks like for GCs?

Cheers,
Lucas""",
    },
    {
        "company": "Boom",
        "domain": "boom.build",
        "vertical": "Surety / contractor underwriting fintech",
        "signal": "Seed (2026-04-14)",
        "public_data_angle": "State contractor licensing boards, OSHA citations, mechanic's liens, federal contract awards",
        "first_name": "Alex",
        "last_name": "Bandes",
        "title": "CEO, Co-Founder",
        "email": "alex@boom.build",
        "linkedin": "https://www.linkedin.com/in/alexbandes",
        "send_priority": 2,
        "subject": "contractor risk signals",
        "body": """Hey Alex,

Saw the seed.

Your buyer (sureties, lenders) underwrites contractors with publicly available data they're not using. State licensing boards, OSHA citations, mechanic's liens, federal contract awards. Plenty of signal to surface contractors before they default.

Most surety-tech outbound is generic "modern underwriting." Yours could be "we found 50 contractors in your book with new OSHA hits."

I build signal-based prospect lists for companies selling into regulated verticals.

Want to see what this looks like for sureties?

Cheers,
Lucas""",
    },
    {
        "company": "Critical Loop",
        "domain": "criticalloop.com",
        "vertical": "Energy / microgrid for data centers + critical infra",
        "signal": "Series A $26M (2026-04-13)",
        "public_data_angle": "FERC interconnection queues, EIA generator data, NERC reliability filings, utility tariff changes",
        "first_name": "Balachandar",
        "last_name": "Ramamurthy",
        "title": "CEO",
        "email": "bala@criticalloop.com",
        "linkedin": "https://www.linkedin.com/in/balachandarramamurthy",
        "send_priority": 2,
        "subject": "ferc queue signals",
        "body": """Hey Bala,

Saw the $26M Series A.

Your buyers (data centers, manufacturers, critical infra) leave a public trail in FERC interconnection queues, EIA generator data, NERC reliability filings, and utility tariff changes.

Plenty of signal to find who's about to need power before their utility tells them.

Most outbound in this space pitches "microgrid solutions." Yours could be "we saw your queue position slipped two quarters."

I build signal-based prospect lists for companies selling into regulated verticals.

Worth a quick look?

Cheers,
Lucas""",
    },
]

# Write CSV
out = "/Users/lucas/Documents/projects/thresh/tmp/prospecting/thresh_outbound_2026-04-27.csv"
fieldnames = ["send_priority","company","domain","vertical","signal","first_name","last_name","title","email","linkedin","subject","body","public_data_angle"]
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r in sorted(rows, key=lambda x: x["send_priority"]):
        w.writerow({k: r[k] for k in fieldnames})
print(f"wrote {len(rows)} rows -> {out}")
# word counts
for r in rows:
    wc = len(r["body"].split())
    print(f"  [{r['send_priority']}] {r['company']:18} | {r['first_name']} {r['last_name']:12} | {r['email']:35} | {wc}w")
