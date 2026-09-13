const fs = require('fs');
const path = require('path');

function findThai(dir) {
    let results = [];
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            results = results.concat(findThai(fullPath));
        } else if (fullPath.endsWith('.html')) {
            const content = fs.readFileSync(fullPath, 'utf8');
            const lines = content.split('\n');
            let thaiRegex = /[\u0E00-\u0E7F]/;
            for (let i = 0; i < lines.length; i++) {
                if (thaiRegex.test(lines[i])) {
                    results.push({ file: fullPath, lineNum: i + 1, line: lines[i].trim() });
                }
            }
        }
    }
    return results;
}

const res = findThai('en');
console.log(JSON.stringify(res, null, 2));
