const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

walkDir('en', function(filePath) {
    if (filePath.endsWith('.html')) {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Depth 1 (root en/ files) or Depth 2 (en/folder/ files)
        const depth = filePath.split(path.sep).length === 2 ? 1 : 2;
        const prefix = depth === 1 ? '../' : '../../';

        // Fix CSS
        content = content.replace(/href="(\.\.\/)*css\//g, 'href="' + prefix + 'css/');
        
        // Fix components
        content = content.replace(/src="(\.\.\/)*components\//g, 'src="' + prefix + 'components/');
        
        // Fix assets
        content = content.replace(/src="(\.\.\/)*assets\//g, 'src="' + prefix + 'assets/');
        content = content.replace(/url\('(\.\.\/)*assets\//g, 'url(\'' + prefix + 'assets/');
        
        // Fix main-nav
        content = content.replace(/<main-nav(\s+depth="\d+")?\s+path=/g, '<main-nav depth="' + depth + '" path=');
        
        // Fix main-footer
        content = content.replace(/<main-footer(.*?)lang="en">/g, '<main-footer depth="' + depth + '" lang="en">');
        
        fs.writeFileSync(filePath, content, 'utf8');
    }
});
console.log('Done!');
