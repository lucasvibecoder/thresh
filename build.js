const fs = require('fs');
const path = require('path');

const gtmId = process.env.GTM_ID || 'GTM-XXXXXXX';
const distDir = path.join(__dirname, 'public');

// Create public directory if it doesn't exist
if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir);
}

// Copy assets folder if it exists
const assetsSrc = path.join(__dirname, 'assets');
const assetsDest = path.join(distDir, 'assets');
if (fs.existsSync(assetsSrc)) {
    // fs.cpSync requires Node 16.7+
    fs.cpSync(assetsSrc, assetsDest, { recursive: true });
    console.log('[build] Copied assets/ to public/assets/');
}

function processFile(file) {
    const srcPath = path.join(__dirname, file);
    const destPath = path.join(distDir, file);

    if (fs.existsSync(srcPath)) {
        let content = fs.readFileSync(srcPath, 'utf8');
        content = content.replace(/%%GTM_ID%%/g, gtmId);
        fs.writeFileSync(destPath, content);
        console.log(`[build] Processed ${file} -> public/${file}`);
    }
}

processFile('index.html');
processFile('gtm-market.html');
