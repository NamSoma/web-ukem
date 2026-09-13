const fs = require('fs');

const data = JSON.parse(fs.readFileSync('thai_results.json', 'utf8'));

// Regex to remove matches that are just attributes or comments
const removeRegexes = [
    /href="[^"]*"/g,
    /src="[^"]*"/g,
    /path="[^"]*"/g,
    /url\([^)]*\)/g,
    /<!--[\s\S]*?-->/g,
    /image-url="[^"]*"/g,
    /<title>.*?<\/title>/g // we know titles are an issue, let's look for OTHER visible text first
];

let visibleThai = [];
let thaiTitles = [];

for (const item of data) {
    let line = item.Line;
    
    // Check titles specifically
    if (line.includes('<title>') && /[\u0E00-\u0E7F]/.test(line)) {
        thaiTitles.push(item);
    }
    
    // Remove attributes and comments
    for (const regex of removeRegexes) {
        line = line.replace(regex, '');
    }
    
    // After removing safe attributes, if there's still Thai, it might be visible text
    if (/[\u0E00-\u0E7F]/.test(line)) {
        // Also check if it's just a class name or something weird, though we don't have Thai classes usually
        visibleThai.push({
            Path: item.Path,
            LineNumber: item.LineNumber,
            Original: item.Line,
            Remaining: line.trim()
        });
    }
}

console.log("=== THAI TITLES ===");
console.log(JSON.stringify(thaiTitles, null, 2));

console.log("\n=== OTHER VISIBLE THAI ===");
console.log(JSON.stringify(visibleThai, null, 2));
