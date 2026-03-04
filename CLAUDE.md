# Thresh (runthresh.com) — System Rules

## 1. What This Is
- Landing page for Thresh — signal-based outbound for niche B2B companies.
- Single-page site: `index.html` with a Tailwind CSS build step.
- Stack: HTML + Tailwind CSS v4 (built via `@tailwindcss/cli`) + vanilla JS.
- Live at runthresh.com, deployed via Vercel from `main` branch.
- **Build commands:**
  - `npm run build` — generates `output.css` (run after any Tailwind class changes in `index.html`)
  - `npm run dev` — watch mode, rebuilds on file changes
- **CSS architecture:**
  - `src/input.css` — Tailwind import, `@theme` config (colors, fonts, radius), and all custom CSS
  - `output.css` — generated file, committed for local preview. Vercel rebuilds on deploy.
  - No CDN — CSS is pre-built at build time.

## 2. Design System (Sovereign Engineering reskin)
- **Fonts**: Inter Tight (display + body), JetBrains Mono (code/email cards/labels)
- **Aesthetic**: Terminal/hacker — square corners (all border-radius forced to 0), scanline overlay on desktop, monospace labels with `//` prefixes, green accent on near-black
- **Color tokens** (defined in `src/input.css` `@theme` block):
  - `brand-bg`: `#080808` (page background)
  - `brand-surface`: `#141414` (cards)
  - `brand-surface-alt`: `#1A1A1A` (card variants)
  - `brand-border`: `rgba(255,255,255, 0.10)` (card/section borders)
  - `brand-border-hover`: `#00FF41` (hover border)
  - `brand-accent`: `#00FF41` (green — CTAs, highlights, accent text)
  - `brand-accent-hover`: `#33FF66` (hover state)
  - `brand-accent-light`: `rgba(0, 255, 65, 0.10)` (subtle accent bg)
  - `brand-secondary`: `#D4622B` (orange — secondary CTAs)
  - `brand-secondary-hover`: `#E87040` (secondary hover)
  - `brand-secondary-light`: `rgba(212, 98, 43, 0.10)` (subtle secondary bg)
  - `brand-text`: `#E8EAF0` (primary text)
  - `brand-muted`: `#9CA1AA` (secondary text)
  - `brand-faint`: `#4D5562` (tertiary/disabled text)
- **Card pattern**: `bg-brand-surface panel p-8 card-lift` (panel = inset bevel shadow, no rounded corners)
- **CTA buttons**: `.btn-primary` = solid green bg, black text. `.btn-secondary` = orange border with hover fill.
- **Section labels**: `.section-label` — JetBrains Mono with auto `// ` prefix via CSS `::before`
- Keep the dark, terminal-aesthetic, high-contrast look. No color additions outside the existing palette.

## 3. Core Behavior
- Tone: Direct, concise. Match the site's existing copy voice — punchy, confident, no fluff.
- When editing copy, preserve the headline rhythm (short lines, line breaks for emphasis).
- When adding sections, follow the existing pattern: `reveal` class on containers, `stagger` on grids, `.divider` between sections.

## 4. Research Folder
- `research/` contains competitive analysis, buyer intelligence, positioning docs, and design specs.
- These are reference material — read them for context but don't modify unless asked.

## 5. Editing Rules
- HTML changes go in `index.html`. CSS/theme changes go in `src/input.css`.
- After changing Tailwind classes in HTML or custom CSS in `src/input.css`, run `npm run build` to regenerate `output.css`.
- Test changes by opening `index.html` directly in browser (no server needed).
- Keep the page fast — no additional JS libraries or frameworks without asking.

## 6. SEO
- Meta description, Open Graph, and Twitter card tags are in `<head>`.
- `robots.txt` and `sitemap.xml` exist at project root.
- Update `sitemap.xml` lastmod date when making content changes.
