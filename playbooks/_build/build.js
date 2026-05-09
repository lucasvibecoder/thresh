#!/usr/bin/env node
/**
 * Playbook builder — composes _partials/ + _content/{slug}.html → {slug}/index.html.
 * Also regenerates the "Live Now" cards in playbooks/index.html (between markers).
 *
 * Usage:
 *   node playbooks/_build/build.js              # build all
 *   node playbooks/_build/build.js stratus-build # build one
 *
 * Source-of-truth files:
 *   playbooks/_partials/shell-top.html
 *   playbooks/_partials/shell-bottom.html
 *   playbooks/_partials/listing-card.html
 *   playbooks/_content/{slug}.html              # frontmatter + body
 *
 * Output (do not edit by hand):
 *   playbooks/{slug}/index.html
 *   playbooks/index.html (cards block regenerated; rest stays manual)
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PARTIALS = path.join(ROOT, '_partials');
const CONTENT = path.join(ROOT, '_content');

const NUMBER_WORDS = [
    'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
    'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'
];

function loadPartial(name) {
    return fs.readFileSync(path.join(PARTIALS, name), 'utf8');
}

function parseFrontmatter(raw) {
    const match = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
    if (!match) {
        throw new Error('Missing frontmatter (--- block) at top of content file');
    }
    const meta = {};
    const lines = match[1].split('\n');
    let currentKey = null;
    let currentBuf = [];
    for (const line of lines) {
        const kv = line.match(/^([A-Z_]+):\s*(.*)$/);
        if (kv) {
            if (currentKey) meta[currentKey] = currentBuf.join('\n').trim();
            currentKey = kv[1];
            currentBuf = [kv[2]];
        } else if (currentKey) {
            currentBuf.push(line);
        }
    }
    if (currentKey) meta[currentKey] = currentBuf.join('\n').trim();
    return { meta, body: match[2] };
}

function substitute(template, vars) {
    return template.replace(/\{\{([A-Z_]+)\}\}/g, (full, key) => {
        if (vars[key] === undefined) {
            console.warn(`  ! Missing variable: ${key} (left as ${full})`);
            return full;
        }
        return vars[key];
    });
}

function defaultsFor(meta, slug) {
    const merged = Object.assign({}, meta);
    merged.SLUG = slug;
    merged.CSS_PATH = '../../output.css';
    merged.NAV_PLAYBOOKS_CLASS = 'text-brand-muted hover:text-brand-accent';
    if (!merged.OG_TITLE) merged.OG_TITLE = merged.TITLE;
    if (!merged.OG_DESCRIPTION) merged.OG_DESCRIPTION = merged.DESCRIPTION;
    if (!merged.TWITTER_TITLE) merged.TWITTER_TITLE = merged.OG_TITLE;
    if (!merged.TWITTER_DESCRIPTION) merged.TWITTER_DESCRIPTION = merged.OG_DESCRIPTION;
    if (!merged.ARTICLE_HEADLINE) merged.ARTICLE_HEADLINE = merged.OG_TITLE;
    if (!merged.ARTICLE_DESCRIPTION) merged.ARTICLE_DESCRIPTION = merged.OG_DESCRIPTION;
    return merged;
}

function buildPlaybook(slug) {
    const contentPath = path.join(CONTENT, `${slug}.html`);
    if (!fs.existsSync(contentPath)) {
        throw new Error(`No content file: ${contentPath}`);
    }
    const raw = fs.readFileSync(contentPath, 'utf8');
    const { meta, body } = parseFrontmatter(raw);
    const vars = defaultsFor(meta, slug);

    const top = substitute(loadPartial('shell-top.html'), vars);
    const bot = loadPartial('shell-bottom.html');

    const html = top + '\n' + body.trim() + '\n' + bot;

    const outDir = path.join(ROOT, slug);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(path.join(outDir, 'index.html'), html);
    console.log(`  ✓ ${slug}/index.html`);
    return vars;
}

function regenerateListing(allMeta) {
    const listingPath = path.join(ROOT, 'index.html');
    if (!fs.existsSync(listingPath)) {
        console.warn(`  ! Listing not found: ${listingPath} (skipping)`);
        return;
    }

    const cardTemplate = loadPartial('listing-card.html');
    const live = allMeta
        .filter(m => m.LISTING_STATUS === 'live')
        .sort((a, b) => Number(a.LISTING_ORDER) - Number(b.LISTING_ORDER));

    const cardsHtml = live
        .map(m => substitute(cardTemplate, m))
        .join('\n');

    let listing = fs.readFileSync(listingPath, 'utf8');

    // Replace cards block between markers
    const cardsMarker = /(<!-- LIVE_PLAYBOOKS_START -->)[\s\S]*?(<!-- LIVE_PLAYBOOKS_END -->)/;
    if (!cardsMarker.test(listing)) {
        console.warn(`  ! Listing has no <!-- LIVE_PLAYBOOKS_START --> markers (skipping cards regen)`);
    } else {
        listing = listing.replace(cardsMarker, `$1\n${cardsHtml}\n                    $2`);
    }

    // Replace count word in H2 between markers
    const countMarker = /(<!-- LIVE_COUNT_START -->)[\s\S]*?(<!-- LIVE_COUNT_END -->)/;
    const countWord = NUMBER_WORDS[live.length] || String(live.length);
    if (countMarker.test(listing)) {
        listing = listing.replace(countMarker, `$1${countWord}$2`);
    }

    fs.writeFileSync(listingPath, listing);
    console.log(`  ✓ index.html (regenerated ${live.length} live cards)`);
}

function main() {
    const target = process.argv[2];
    let slugs;
    if (target) {
        slugs = [target];
    } else {
        slugs = fs.readdirSync(CONTENT)
            .filter(f => f.endsWith('.html'))
            .map(f => f.replace(/\.html$/, ''))
            .sort();
    }

    console.log(`Building ${slugs.length} playbook${slugs.length === 1 ? '' : 's'}...`);
    const allMeta = [];
    for (const slug of slugs) {
        try {
            const meta = buildPlaybook(slug);
            allMeta.push(meta);
        } catch (e) {
            console.error(`  ✗ ${slug}: ${e.message}`);
            process.exit(1);
        }
    }

    if (!target) {
        regenerateListing(allMeta);
    } else {
        // For single-slug builds, still need full meta to regenerate the listing.
        const allSlugs = fs.readdirSync(CONTENT)
            .filter(f => f.endsWith('.html'))
            .map(f => f.replace(/\.html$/, ''));
        const fullMeta = allSlugs.map(slug => {
            const raw = fs.readFileSync(path.join(CONTENT, `${slug}.html`), 'utf8');
            const { meta } = parseFrontmatter(raw);
            return defaultsFor(meta, slug);
        });
        regenerateListing(fullMeta);
    }

    console.log('Done.');
}

main();
