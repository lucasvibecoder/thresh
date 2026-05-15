# Thresh (runthresh.com) - Project Rules

## 1. What This Is
- Operating repo for Thresh, Lucas's agency/business/consultancy for signal-based outbound and GTM engineering.
- Contains the public website at runthresh.com, public playbooks, outbound experiments to get clients for Thresh, and signal-based GTM research.
- Public playbooks are largely pulled from `/gtm-alpha/runs` artifacts, then adapted into the `playbooks/` publishing surface.
- Stack for the website: HTML + Tailwind CSS v4 (built via `@tailwindcss/cli`) + vanilla JS.
- Live at runthresh.com, deployed via Vercel from `main` branch.
- **Build commands:**
  - `npm run build` - runs `build:css` (Tailwind) then `build:playbooks` (regenerates all playbook indexes from `_content/`)
  - `npm run build:css` - Tailwind only
  - `npm run build:playbooks` - playbook indexes + listing only (no Tailwind step). Add a slug to build one: `node playbooks/_build/build.js truckstop-com`
  - `npm run dev` - Tailwind watch mode
- **CSS architecture:**
  - `src/input.css` - Tailwind import, `@theme` config (colors, fonts, radius), and all custom CSS
  - `output.css` - generated file, committed for local preview. Vercel rebuilds on deploy.
  - No CDN - CSS is pre-built at build time.

## 2. Repo Surfaces
- **Website surface:** `index.html`, `src/input.css`, `output.css`, `404.html`, `privacy.html`, `robots.txt`, `sitemap.xml`.
- **Playbook surface:** `playbooks/_content/`, `playbooks/_partials/`, `playbooks/_build/`, generated `playbooks/{slug}/index.html`, and hand-written artifact pages.
- **Outbound/research surface:** `outbound/`, `research/`, and `thresh.md`.
- **Business/strategy memory:** `thresh.md` is the operating doc for Thresh's offer, ICP, pricing, strategic state, and active validation notes. Do not treat it as a tool instruction file.

## 3. Design System (Sovereign Engineering reskin)
- **Fonts**: Inter Tight (display + body), JetBrains Mono (code/email cards/labels)
- **Aesthetic**: Terminal/hacker - square corners (all border-radius forced to 0), scanline overlay on desktop, monospace labels with `//` prefixes, green accent on near-black
- **Color tokens** (defined in `src/input.css` `@theme` block):
  - `brand-bg`: `#080808` (page background)
  - `brand-surface`: `#141414` (cards)
  - `brand-surface-alt`: `#1A1A1A` (card variants)
  - `brand-border`: `rgba(255,255,255, 0.10)` (card/section borders)
  - `brand-border-hover`: `#00FF41` (hover border)
  - `brand-accent`: `#00FF41` (green - CTAs, highlights, accent text)
  - `brand-accent-hover`: `#33FF66` (hover state)
  - `brand-accent-light`: `rgba(0, 255, 65, 0.10)` (subtle accent bg)
  - `brand-secondary`: `#D4622B` (orange - secondary CTAs)
  - `brand-secondary-hover`: `#E87040` (secondary hover)
  - `brand-secondary-light`: `rgba(212, 98, 43, 0.10)` (subtle secondary bg)
  - `brand-text`: `#E8EAF0` (primary text)
  - `brand-muted`: `#9CA1AA` (secondary text)
  - `brand-faint`: `#717985` (tertiary/disabled text)
- **Card pattern**: `bg-brand-surface panel p-8 card-lift` (panel = inset bevel shadow, no rounded corners)
- **CTA buttons**: `.btn-primary` = solid green bg, black text. `.btn-secondary` = orange border with hover fill.
- **Section labels**: `.section-label` - JetBrains Mono with auto `// ` prefix via CSS `::before`
- Keep the dark, terminal-aesthetic, high-contrast look. No color additions outside the existing palette.

## 4. Core Behavior
- Tone: Direct, concise. Match the site's existing copy voice - punchy, confident, no fluff.
- When editing copy, preserve the headline rhythm (short lines, line breaks for emphasis).
- When adding sections, follow the existing pattern: `reveal` class on containers, `stagger` on grids, `.divider` between sections.

## 5. Research Folder
- `research/` contains competitive analysis, buyer intelligence, positioning docs, and design specs.
- These are reference material - read them for context but don't modify unless asked.

## 6. Outbound Folder
- `outbound/` holds cross-account state (`sent-log.md`, `prospecting-queries.md`, `qualified-from-gtm-alpha.md`).
- Per-account drafts, deliverables, and sent emails live in `gtm-alpha/runs/<account>/outbound/`.

## 7. Editing Rules
- HTML changes go in `index.html`. CSS/theme changes go in `src/input.css`.
- After changing Tailwind classes in HTML or custom CSS in `src/input.css`, run `npm run build` to regenerate `output.css`.
- Test website changes by opening `index.html` directly in browser unless a server is specifically needed.
- Keep the page fast - no additional JS libraries or frameworks without asking.
- Before building or revising any playbook, scan `playbooks/feedback-log.md` (claim ledger) and `playbooks/_CONVENTIONS.md` for relevant rules.

## 8. Playbook Authoring (`/playbooks/{slug}/`)
- **Source of truth:** `playbooks/_content/{slug}.html` (frontmatter + body). Never edit `playbooks/{slug}/index.html` directly - it is auto-generated and overwritten on every build.
- **Shared boilerplate:** `playbooks/_partials/shell-top.html` (head + nav), `shell-bottom.html` (centralized CTA form + footer + scripts), `listing-card.html` (the listing-page card). Editing a partial updates all playbooks consistently - this is how we prevent drift. The "Want yours?" form CTA at the bottom of every playbook lives in `shell-bottom.html`; edit there and run `npm run build:playbooks` to propagate.
- **Build script:** `playbooks/_build/build.js` composes partials + content, regenerates per-playbook `index.html`, and regenerates the cards block in `playbooks/index.html` between `<!-- LIVE_PLAYBOOKS_START -->` and `<!-- LIVE_PLAYBOOKS_END -->`.
- **Adding a new playbook:**
  1. Create `playbooks/_content/{slug}.html` with frontmatter (`TITLE`, `DESCRIPTION`, `OG_*`, `TWITTER_*`, `ARTICLE_*`, `LISTING_STATUS=live`, `LISTING_ORDER`, `LISTING_TAG`, `LISTING_TITLE`, `LISTING_DESCRIPTION`, `LISTING_FOOTNOTE`) and the body (everything that goes inside `<main>`).
  2. Run `npm run build:playbooks` or `node playbooks/_build/build.js {slug}` to build only that one.
  3. Add the playbook URL to `sitemap.xml`.
  4. Any per-playbook artifact pages (PVPs, scorecards, benchmarks) live next to the index in `playbooks/{slug}/{artifact-name}.html` - those are hand-written; the build script does not manage artifact pages.
- **Listing page:** Mostly hand-editable; only the cards block between markers is auto-regenerated. The "In The Queue" section, hero, and CTA stay manual.
- **Drift uplift:** If a partial is updated (for example, a new meta tag), running `npm run build:playbooks` propagates the change across all playbooks immediately. No manual repair across files.

## 9. SEO
- Meta description, Open Graph, and Twitter card tags are in `<head>`.
- `robots.txt` and `sitemap.xml` exist at project root.
- Update `sitemap.xml` lastmod date when making content changes.

## 10. Registries
- Files that accumulate claims (feedback, sends, prospects, queries) follow the registry pattern in `docs/registry-pattern.md`. Read it before creating or restructuring a registry.
- Active registries:
  - `playbooks/feedback-log.md` - advisor / buyer feedback on shipped playbooks
  - `outbound/sent-log.md` - chronological cold-send log
  - `outbound/prospecting-queries.md` - reusable TheirStack queries
  - `outbound/qualified-from-gtm-alpha.md` - tiered prospect qualification
  - `outbound/pipeline.md` - single-vertical operating playbook
- Graduated rules from registries land in: `playbooks/_CONVENTIONS.md` (playbook-artifact rules), memory files (cold-email principles), `thresh.md` / website copy (positioning), or this project-rules doc (project-level operating rules).
