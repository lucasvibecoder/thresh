# Cold Email v1 — Motus Phase II / Factoring ICP

**Send window:** Tue 2026-05-12 or Wed 2026-05-13 (avoid May 14 cutover day)
**Audience:** Chief Credit Officer / VP Credit / Head of Underwriting / Director of Portfolio Risk at US trucking factoring shops, $20M–$200M. Founder/CEO at sub-$100M shops where they still own credit. **No sales titles.**
**Sender:** Lucas (single inbox or SmartLead rotation across 9 warmed inboxes)
**Word count:** ~85

---

## Subject

```
motus may 18
```

## Body

```
{{first_name}} - Motus launches May 18. Carriers with stale MCS-150s,
officer mismatches, or authority discrepancies will start failing FMCSA
business verification and showing up in public records as flagged.

Roughly 20% of US carriers with active FMCSA operating authority have
MCS-150s past the 24-month update window — the most common of these gaps.

I pull public signals and flag the matches. For factoring, that reads
as early warning on default risk before it hits your book.

Want me to show you what it looks like?

Lucas
```

## Methodology citation (use only if asked)

> FMCSA Company Census File pulled 2026-05-11. Filtered to carriers with STATUS_CODE='A' and at least one active operating-authority docket — 680,056 carriers. 136,498 of those have MCS-150 dates older than 24 months. 20.07% stale.

## Reply ammo

If recipient replies "like what?" → see `../bench/curated-bench.md` for 8 named carriers ready to drop in-thread.

## Failure-mode scan (per cold-email-craft skill)

- **Target/register:** factoring credit/risk vocabulary used throughout ("active FMCSA operating authority", "default risk", "your book"). ✓
- **AI-SDR pattern:** no LinkedIn quote, no fake observation. ✓
- **Forced analogies:** none. ✓
- **Telescoping:** system-level claim with %, not one-company specifics. ✓
- **Machinery before curiosity:** one line of "what I do," no Layer 1/2 explanation. ✓
- **Jargon:** all terms (MCS-150, operating authority, FMCSA verification) are recipient's daily vocabulary, not consultant jargon. ✓
- **Dual CTA:** single CTA ("Want me to show you?"). ✓
- **Premature attachments:** none. ✓
- **Signal recency:** Motus launches in 7 days. Fresh. ✓
- **Offer bar (Clay 30-sec filter test):** filter is "FMCSA Census + MCS-150 stale + active authority + cross-ref to recipient's region." Not Clay-able in 30 seconds — requires Socrata query + curation. Passes. ✓

## Decisions intentionally NOT taken

- **No named carrier in body** — at 50–100 send volume, same DOT# across emails = scale tell. False-positive risk against recipient's own book is asymmetric downside. Named examples held in `../bench/curated-bench.md` for reply layer only.
- **No combined-signal claim** — original "stale MCS-150s + officer mismatches + authority discrepancies" combined % would require state SoS scraping (half-day work, brittle). Cited the single-field stat (stale MCS-150s) and framed it as "the most common of these gaps."
- **No "at scale" phrasing** — replaced with "flag the matches" (recipient register, not vendor register).
