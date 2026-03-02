const fs = require('fs');
const path = require('path');

// Fallback to empty string if GTM_ID is not provided
const gtmId = process.env.GTM_ID || 'GTM-XXXXXXX';

function injectGTM(file) {
    const filePath = path.join(__dirname, file);
    if (fs.existsSync(filePath)) {
        let content = fs.readFileSync(filePath, 'utf8');
        // Replace the placeholder with the actual GTM ID
        content = content.replace(/%%GTM_ID%%/g, gtmId);
        fs.writeFileSync(filePath, content);
        console.log(`[build] Injected GTM_ID into ${file}`);
    }
}

injectGTM('index.html');
injectGTM('gtm-market.html');
