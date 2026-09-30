const fs = require('fs');

function moveMessageSection(filename) {
    let content = fs.readFileSync(filename, 'utf8');

    const msgStart = content.indexOf('<!-- Message Section -->');
    if (msgStart === -1) {
        console.log('Message section not found in ' + filename);
        return;
    }

    const msgEnd = content.indexOf('    <!-- Leadership Section -->', msgStart);
    if (msgEnd === -1) {
        console.log('End of Message section not found in ' + filename);
        return;
    }

    const msgHtml = content.substring(msgStart, msgEnd);

    // Remove message section
    content = content.substring(0, msgStart) + content.substring(msgEnd);

    const orgStart = content.indexOf('    <!-- Organization Structure Section -->');
    if (orgStart === -1) {
        console.log('Organization section not found in ' + filename);
        return;
    }

    // Insert message section
    const newContent = content.substring(0, orgStart) + msgHtml + '\n' + content.substring(orgStart);

    fs.writeFileSync(filename, newContent, 'utf8');
    console.log('Successfully updated ' + filename);
}

moveMessageSection('เกี่ยวกับ UKEM.html');
moveMessageSection('en/About UKEM.html');
