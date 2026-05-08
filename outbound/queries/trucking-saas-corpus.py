"""Pull trucking/logistics SaaS messaging architecture from both Supabase corpora.

Sources:
  - blueprint_playbooks + blueprint_plays  (Jordan Crawford / Blueprint, 5k+ plays)
  - gtm_alpha_vendors + gtm_alpha_plays + gtm_alpha_signals  (Lucas's own corpus)

Both tables live in the same Supabase project (URL configured in
blueprint-scraper/.env or gtm-alpha-extractor/.env).

Output:
  - outbound/queries/trucking-saas-corpus-output.json
    Structured aggregation: data sources by frequency, double-validated overlap,
    signal categories with sample phrasings, target personas, raw plays.

Usage:
    python3 outbound/queries/trucking-saas-corpus.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import httpx
from urllib.parse import quote

REPO = Path(__file__).resolve().parents[2]
ENV_CANDIDATES = [
    REPO.parent / "blueprint-scraper" / ".env",
    REPO.parent / "gtm-alpha-extractor" / ".env",
]
OUT_PATH = Path(__file__).parent / "trucking-saas-corpus-output.json"

INDUSTRY_TERMS = ["logistic", "supply chain", "transport", "freight", "truck", "fleet"]
LOGISTICS_INDUSTRY_LITERAL = "Logistics & Supply Chain"


def load_env() -> dict[str, str]:
    for path in ENV_CANDIDATES:
        if not path.exists():
            continue
        env: dict[str, str] = {}
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
        if env.get("SUPABASE_URL") and env.get("SUPABASE_SERVICE_ROLE_KEY"):
            return env
    for k in ("SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY"):
        if os.environ.get(k):
            pass
    if os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SERVICE_ROLE_KEY"):
        return {
            "SUPABASE_URL": os.environ["SUPABASE_URL"],
            "SUPABASE_SERVICE_ROLE_KEY": os.environ["SUPABASE_SERVICE_ROLE_KEY"],
        }
    sys.exit("Could not find SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY in any .env")


def query_blueprint(url: str, headers: dict[str, str]) -> list[dict]:
    """Logistics playbooks → public-data plays only (internal_data_callout IS NULL)."""
    or_clauses = []
    for term in INDUSTRY_TERMS:
        for col in ("industry", "sub_industry", "playbook_category", "company_name"):
            or_clauses.append(f"{col}.ilike.*{term}*")
    select = (
        "select=slug,company_name,domain,industry,sub_industry,playbook_category,"
        "blueprint_plays(quality_score,quality_label,play_name,play_type,data_type,"
        "whats_the_play,why_it_works,data_sources,internal_data_callout,message_example)"
    )
    endpoint = f"{url}/rest/v1/blueprint_playbooks?{select}&or=({','.join(or_clauses)})"
    r = httpx.get(endpoint, headers=headers, timeout=30)
    r.raise_for_status()
    playbooks = r.json()
    rows: list[dict] = []
    for pb in playbooks:
        for p in pb.get("blueprint_plays") or []:
            if p.get("internal_data_callout"):
                continue
            rows.append({
                "source_corpus": "blueprint",
                "company_name": pb.get("company_name"),
                "domain": pb.get("domain"),
                "industry": pb.get("industry"),
                "sub_industry": pb.get("sub_industry"),
                "playbook_category": pb.get("playbook_category"),
                "quality_score": p.get("quality_score"),
                "play_name": p.get("play_name"),
                "play_type": p.get("play_type"),
                "data_type": p.get("data_type"),
                "whats_the_play": p.get("whats_the_play"),
                "why_it_works": p.get("why_it_works"),
                "data_sources": p.get("data_sources"),
                "message_example": p.get("message_example"),
            })
    return rows


def query_gtm_alpha(url: str, headers: dict[str, str]) -> tuple[list[dict], list[dict]]:
    """All logistics vendors → their plays + signals."""
    select_v = (
        "select=domain,vendor_name,primary_industry,executive_summary,edp_metric,"
        "gtm_alpha_plays(play_number,play_name,category,conviction,conviction_score,"
        "motion,data_type,target_persona_role,whats_the_play,why_it_works,"
        "signal_trigger,data_sources,email_subject,email_body),"
        "gtm_alpha_signals(signal_number,signal_name,composite_score,pain_points,"
        "target_industry,observable_indicator,causal_logic,data_source,claim_type,is_adjacent)"
    )
    endpoint = (
        f"{url}/rest/v1/gtm_alpha_vendors"
        f"?{select_v}&primary_industry=eq.{quote(LOGISTICS_INDUSTRY_LITERAL, safe='')}"
    )
    r = httpx.get(endpoint, headers=headers, timeout=30)
    r.raise_for_status()
    vendors = r.json()
    plays: list[dict] = []
    signals: list[dict] = []
    for v in vendors:
        for p in v.get("gtm_alpha_plays") or []:
            plays.append({
                "source_corpus": "gtm_alpha",
                "vendor_domain": v.get("domain"),
                "vendor_name": v.get("vendor_name"),
                "primary_industry": v.get("primary_industry"),
                "play_number": p.get("play_number"),
                "play_name": p.get("play_name"),
                "category": p.get("category"),
                "conviction": p.get("conviction"),
                "conviction_score": p.get("conviction_score"),
                "data_type": p.get("data_type"),
                "target_persona_role": p.get("target_persona_role"),
                "whats_the_play": p.get("whats_the_play"),
                "why_it_works": p.get("why_it_works"),
                "signal_trigger": p.get("signal_trigger"),
                "data_sources": p.get("data_sources"),
                "email_subject": p.get("email_subject"),
                "email_body": p.get("email_body"),
            })
        for s in v.get("gtm_alpha_signals") or []:
            if s.get("is_adjacent"):
                continue
            signals.append({
                "source_corpus": "gtm_alpha",
                "vendor_domain": v.get("domain"),
                "vendor_name": v.get("vendor_name"),
                "signal_number": s.get("signal_number"),
                "signal_name": s.get("signal_name"),
                "composite_score": s.get("composite_score"),
                "pain_points": s.get("pain_points"),
                "target_industry": s.get("target_industry"),
                "observable_indicator": s.get("observable_indicator"),
                "causal_logic": s.get("causal_logic"),
                "data_source": s.get("data_source"),
            })
    return plays, signals


# Canonical data-source labels — collapses common synonyms so frequency
# counts mean something. Anything not matched stays in `_other`.
DATA_SOURCE_PATTERNS = [
    ("FMCSA SAFER",            r"\bFMCSA\s*SAFER\b|\bSAFER\b"),
    ("FMCSA Inspection DB",    r"\bFMCSA\s*Inspection|\binspection\s*data|roadside\s*inspection"),
    ("FMCSA SMS BASIC / CSA",  r"\bSMS\b|\bBASIC\b|\bCSA\b"),
    ("FMCSA Crash DB",         r"\bcrash\s*data|FMCSA\s*Crash"),
    ("FMCSA L&I (licensing)",  r"\bL&I\b|FMCSA\s*L&I|operating\s*authorit"),
    ("FMCSA (general)",        r"\bFMCSA\b|\bDOT\b"),
    ("OSHA",                   r"\bOSHA\b"),
    ("EPA / ECHO / RCRA",      r"\bEPA\b|\bECHO\b|\bRCRA\b"),
    ("State licensing",        r"licensing\s*board|state\s*contractor|state\s*licens"),
    ("SEC / EDGAR",            r"\bSEC\b|\bEDGAR\b|10-K|8-K"),
    ("Job postings",           r"job\s*posting|hiring|LinkedIn\s*Jobs|Indeed"),
    ("LinkedIn (firmographic)", r"\bLinkedIn\b(?!\s*Jobs)"),
    ("Tech stack (BuiltWith/Wappalyzer)", r"BuiltWith|Wappalyzer|tech\s*stack"),
    ("Funding (Crunchbase/PitchBook)", r"Crunchbase|PitchBook|funding\s*round"),
    ("M&A press / PE filings", r"M&A|press\s*release|PE\s*acquisi"),
    ("State permits / filings", r"state\s*permit|state\s*filing|secretary\s*of\s*state"),
    ("Court / litigation",     r"court|litigation|PACER|docket"),
    ("News / web scrape",      r"news|web\s*scrape|press"),
]


def canonicalize_source(text: str | None) -> list[str]:
    if not text:
        return []
    matched: list[str] = []
    for label, pattern in DATA_SOURCE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            matched.append(label)
    return matched or ["_other"]


def aggregate_data_sources(rows: list[dict]) -> Counter:
    """Frequency count, scoped per row (a row contributes once per matched source)."""
    counts: Counter = Counter()
    for row in rows:
        text = " ".join(filter(None, [
            row.get("data_sources"),
            row.get("data_source"),
            row.get("signal_trigger"),
        ]))
        seen_in_row = set(canonicalize_source(text))
        for s in seen_in_row:
            counts[s] += 1
    return counts


def cluster_signals_by_source(rows: list[dict]) -> dict[str, list[dict]]:
    clusters: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        text = " ".join(filter(None, [
            row.get("data_sources"),
            row.get("data_source"),
            row.get("signal_trigger"),
        ]))
        sources = set(canonicalize_source(text))
        title = (
            row.get("signal_name")
            or row.get("play_name")
            or "(unnamed)"
        )
        snippet = (
            row.get("observable_indicator")
            or row.get("signal_trigger")
            or row.get("whats_the_play")
            or ""
        )[:280]
        for s in sources:
            clusters[s].append({
                "title": title,
                "snippet": snippet,
                "source_corpus": row.get("source_corpus"),
                "company": row.get("company_name") or row.get("vendor_name"),
            })
    return clusters


def aggregate_personas(plays: list[dict]) -> Counter:
    counts: Counter = Counter()
    for p in plays:
        role = p.get("target_persona_role")
        if role:
            counts[role.strip()] += 1
    return counts


def main() -> None:
    env = load_env()
    url = env["SUPABASE_URL"].rstrip("/")
    key = env["SUPABASE_SERVICE_ROLE_KEY"]
    headers = {"apikey": key, "Authorization": f"Bearer {key}"}

    print("Querying Blueprint corpus…")
    bp_plays = query_blueprint(url, headers)
    print(f"  {len(bp_plays)} public-data logistics plays")

    print("Querying GTM Alpha corpus…")
    ga_plays, ga_signals = query_gtm_alpha(url, headers)
    print(f"  {len(ga_plays)} plays, {len(ga_signals)} signals across logistics vendors")

    all_messaging_rows: list[dict] = bp_plays + ga_plays + ga_signals

    bp_sources = aggregate_data_sources(bp_plays)
    ga_sources = aggregate_data_sources(ga_plays + ga_signals)
    combined_sources = aggregate_data_sources(all_messaging_rows)

    data_sources_ranked = []
    for source, freq in combined_sources.most_common():
        if source == "_other":
            continue
        data_sources_ranked.append({
            "source": source,
            "frequency_total": freq,
            "frequency_blueprint": bp_sources.get(source, 0),
            "frequency_gtm_alpha": ga_sources.get(source, 0),
            "double_validated": bp_sources.get(source, 0) > 0 and ga_sources.get(source, 0) > 0,
        })

    clusters = cluster_signals_by_source(all_messaging_rows)
    signal_categories = []
    for s in data_sources_ranked[:10]:
        examples = clusters.get(s["source"], [])[:5]
        signal_categories.append({
            "data_source": s["source"],
            "frequency": s["frequency_total"],
            "double_validated": s["double_validated"],
            "examples": examples,
        })

    persona_counts = aggregate_personas(ga_plays)
    target_personas = [
        {"role": r, "frequency": c}
        for r, c in persona_counts.most_common()
    ]

    output = {
        "summary": {
            "blueprint_play_count": len(bp_plays),
            "gtm_alpha_play_count": len(ga_plays),
            "gtm_alpha_signal_count": len(ga_signals),
            "blueprint_companies": sorted({r["company_name"] for r in bp_plays if r.get("company_name")}),
            "gtm_alpha_vendors": sorted({r["vendor_name"] for r in ga_plays if r.get("vendor_name")}),
        },
        "data_sources_ranked": data_sources_ranked,
        "signal_categories": signal_categories,
        "target_personas": target_personas,
        "raw": {
            "blueprint_plays": bp_plays,
            "gtm_alpha_plays": ga_plays,
            "gtm_alpha_signals": ga_signals,
        },
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(output, indent=2, default=str))
    print(f"\nWrote {OUT_PATH}")
    print(f"  {len(data_sources_ranked)} canonical data sources after collapse")
    if data_sources_ranked:
        print("\nTop 10 data sources by frequency (✓ = double-validated):")
        for s in data_sources_ranked[:10]:
            mark = "✓" if s["double_validated"] else " "
            print(f"  {mark} {s['source']:<40} total={s['frequency_total']:<3} bp={s['frequency_blueprint']:<3} ga={s['frequency_gtm_alpha']}")
    if target_personas:
        print("\nTop target personas (GTM Alpha plays):")
        for p in target_personas[:8]:
            print(f"   {p['role']:<55} {p['frequency']}")


if __name__ == "__main__":
    main()
