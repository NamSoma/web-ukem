const fs = require('fs');
const path = require('path');

function getFiles(dir, files = []) {
    const fileList = fs.readdirSync(dir);
    for (const file of fileList) {
        const name = dir + '/' + file;
        if (fs.statSync(name).isDirectory()) {
            getFiles(name, files);
        } else {
            if (name.endsWith('.html') && !name.endsWith('index.html')) {
                files.push(name);
            }
        }
    }
    return files;
}

const rootDir = '.';
const htmlFiles = getFiles(rootDir);

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;

    // Check if already inner-hero
    if (content.includes('<header class="inner-hero"')) {
        const newContent = content.replace(/style="background-image: url\([^)]+\);"/g, 'style="background-color: #2c3e50;"');
        if (newContent !== content) {
            content = newContent;
            modified = true;
        }
    }

    // Fix corrupted Thai characters if any (from previous script)
    if (content.includes('à¸«à¸™à¹‰à¸²à¸«à¸¥à¸±à¸')) {
        content = content.replace(/à¸«à¸™à¹‰à¸²à¸«à¸¥à¸±à¸[\s\S]*?(?=<\/a>)/g, 'หน้าหลัก\n                ');
        modified = true;
    }

    // Process old hero-banner
    const heroRegex = /<(?:header|div)\s+class="hero-banner">[\s\S]*?<\/(?:header|div)>/g;
    
    // We need to carefully replace. If it's a div, we might need to remove an extra </div> if it was nested.
    // Wait, let's just match the exact structure.
    
    const divHeroRegex = /<div class="hero-banner">\s*<div class="container">[\s\S]*?<\/div>\s*<\/div>/g;
    const headerHeroRegex = /<header class="hero-banner">[\s\S]*?<\/header>/g;

    const fileDir = path.dirname(file);
    const fileName = path.basename(file, '.html');
    const isRoot = fileDir === rootDir;
    const prefix = isRoot ? '' : '../';
    const category = isRoot ? '' : path.basename(fileDir);
    
    let breadcrumb = `
            <div class="inner-breadcrumb">
                <a href="${prefix}index.html">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    หน้าหลัก
                </a>`;
    if (!isRoot) {
        breadcrumb += `\n                <span>&gt;</span>\n                <a href="#">${category}</a>`;
    }
    breadcrumb += `\n                <span>&gt;</span>\n                <span>${fileName}</span>\n            </div>`;

    const newHeader = `    <header class="inner-hero" style="background-color: #2c3e50;">
        <div class="inner-hero-content">
            <h1>${fileName}</h1>${breadcrumb}
        </div>
        <a href="#content-start" class="scroll-down-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </a>
    </header>`;

    if (divHeroRegex.test(content)) {
        content = content.replace(divHeroRegex, newHeader);
        modified = true;
    }
    if (headerHeroRegex.test(content)) {
        content = content.replace(headerHeroRegex, newHeader);
        modified = true;
    }
    
    // Also, the previous script might have left an extra </div> after the inner-hero for files that were previously <div class="hero-banner">
    // Let's clean that up.
    // If we see </header>\s*</div>\s*<div class="container">\s*<div class="content-section"
    content = content.replace(/<\/header>\s*<\/div>\s*(<div class="container">|<main class="content-section")/g, '</header>\n\n    $1');

    if (content.includes('<main class="content-section">')) {
        content = content.replace('<main class="content-section">', '<main class="content-section" id="content-start">');
        modified = true;
    }
    if (content.includes('<div class="content-section">')) {
        content = content.replace('<div class="content-section">', '<div class="content-section" id="content-start">');
        modified = true;
    }

    if (modified) {
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Updated ${file}`);
    }
});
