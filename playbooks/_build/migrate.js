#!/usr/bin/env node
/**
 * One-shot migration: extracts head meta + main body from each existing
 * playbooks/{slug}/index.html and writes playbooks/_content/{slug}.html
 * with frontmatter + body, ready for the build script.
 *
 * Run once. After this, _content/{slug}.html is the source of truth.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CONTENT = path.join(ROOT, '_content');

if (!fs.existsSync(CONTENT)) fs.mkdirSync(CONTENT, { recursive: true });

const slugs = fs.readdirSync(ROOT).filter(name => {
    const full = path.join(ROOT, name);
    return fs.statSync(full).isDirectory()
        && !name.startsWith('_')
        && fs.existsSync(path.join(full, 'index.html'));
});

console.log(`Found ${slugs.length} playbook directories to migrate: ${slugs.join(', ')}`);

const listingHtml = fs.existsSync(path.join(ROOT, 'index.html'))
    ? fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8')
    : '';

function extractMeta(html, slug) {
    const meta = {};

    const grab = (re) => {
        const m = html.match(re);
        return m ? m[1].trim() : '';
    };

    meta.TITLE = grab(/<title>([\s\S]*?)<\/title>/);
    meta.DESCRIPTION = grab(/<meta\s+name=["']description["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.OG_TITLE = grab(/<meta\s+property=["']og:title["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.OG_DESCRIPTION = grab(/<meta\s+property=["']og:description["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.TWITTER_TITLE = grab(/<meta\s+name=["']twitter:title["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.TWITTER_DESCRIPTION = grab(/<meta\s+name=["']twitter:description["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.ARTICLE_PUBLISHED = grab(/<meta\s+property=["']article:published_time["']\s+content=["']([\s\S]*?)["']\s*\/?>/);
    meta.ARTICLE_MODIFIED = grab(/<meta\s+property=["']article:modified_time["']\s+content=["']([\s\S]*?)["']\s*\/?>/);

    const jsonLdMatch = html.match(/<script\s+type=["']application\/ld\+json["']>\s*([\s\S]*?)\s*<\/script>/);
    if (jsonLdMatch) {
        try {
            const ld = JSON.parse(jsonLdMatch[1]);
            meta.ARTICLE_HEADLINE = ld.headline || '';
            meta.ARTICLE_DESCRIPTION = ld.description || '';
        } catch (e) {
            console.warn(`  ! Could not parse JSON-LD for ${slug}: ${e.message}`);
        }
    }

    return meta;
}

function extractBody(html) {
    const mainOpen = html.indexOf('<main id="main-content"');
    if (mainOpen < 0) throw new Error('Could not find <main id="main-content">');
    const afterOpen = html.indexOf('>', mainOpen) + 1;

    const mainClose = html.lastIndexOf('</main>');
    if (mainClose < 0) throw new Error('Could not find </main>');

    return html.slice(afterOpen, mainClose).trim();
}

function extractListingData(slug) {
    if (!listingHtml) return {};
    // Find the card for this slug
    const re = new RegExp(
        `<a href=["']/playbooks/${slug}/?["'][^>]*>([\\s\\S]*?)</a>`,
        'i'
    );
    const m = listingHtml.match(re);
    if (!m) return {};

    const cardHtml = m[1];
    const tag = cardHtml.match(/<p class="font-mono text-xs tracking-wider text-brand-faint uppercase mb-2">([\s\S]*?)<\/p>/);
    const title = cardHtml.match(/<h3[^>]*>([\s\S]*?)<\/h3>/);
    const desc = cardHtml.match(/<p class="text-brand-muted text-base leading-relaxed mb-4">\s*([\s\S]*?)\s*<\/p>/);
    const footnote = cardHtml.match(/<p class="font-mono text-xs text-brand-faint">\s*([\s\S]*?)\s*<\/p>/);

    return {
        LISTING_STATUS: 'live',
        LISTING_TAG: tag ? tag[1].trim() : '',
        LISTING_TITLE: title ? title[1].trim() : '',
        LISTING_DESCRIPTION: desc ? desc[1].trim() : '',
        LISTING_FOOTNOTE: footnote ? footnote[1].trim() : ''
    };
}

// Listing order — explicit per current site order, hardcoded once
const LISTING_ORDER = {
    'withassured-com': 1,
    'lightlabs-com': 2,
    'samsara-com': 3,
    'stratus-build': 4,
    'ambrook-com': 5,
    'hibob-com': 6,
};

function frontmatterFor(meta) {
    const lines = [];
    const order = [
        'TITLE', 'DESCRIPTION',
        'OG_TITLE', 'OG_DESCRIPTION',
        'TWITTER_TITLE', 'TWITTER_DESCRIPTION',
        'ARTICLE_HEADLINE', 'ARTICLE_DESCRIPTION',
        'ARTICLE_PUBLISHED', 'ARTICLE_MODIFIED',
        'LISTING_STATUS', 'LISTING_ORDER',
        'LISTING_TAG', 'LISTING_TITLE', 'LISTING_DESCRIPTION', 'LISTING_FOOTNOTE',
    ];
    for (const key of order) {
        if (meta[key] !== undefined && meta[key] !== '') {
            lines.push(`${key}: ${meta[key]}`);
        }
    }
    return lines.join('\n');
}

for (const slug of slugs) {
    try {
        const html = fs.readFileSync(path.join(ROOT, slug, 'index.html'), 'utf8');
        const meta = extractMeta(html, slug);
        const body = extractBody(html);
        const listing = extractListingData(slug);
        const order = LISTING_ORDER[slug] || 99;

        const fullMeta = Object.assign({}, meta, listing, { LISTING_ORDER: order });
        const frontmatter = frontmatterFor(fullMeta);
        const out = `---\n${frontmatter}\n---\n${body}\n`;

        fs.writeFileSync(path.join(CONTENT, `${slug}.html`), out);
        console.log(`  ✓ _content/${slug}.html (${body.length} body chars)`);
    } catch (e) {
        console.error(`  ✗ ${slug}: ${e.message}`);
    }
}

console.log('Migration complete. Now run: node playbooks/_build/build.js');
