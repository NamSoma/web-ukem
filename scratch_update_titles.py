import os
file = r'f:\Back up อีก HDD\งาน\ลองทำ\components\StakeholderCard.js'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace col title logic
old_logic = '''        const col1Title = this.getAttribute('col1-title') || (lang === 'en' ? 'Engagement Channels' : 'ช่องทางการมีส่วนร่วม');
        const col2Title = this.getAttribute('col2-title') || (lang === 'en' ? 'Stakeholder Issues' : 'ประเด็นผู้มีส่วนได้เสีย');
        const col3Title = this.getAttribute('col3-title') || (lang === 'en' ? 'Related Sustainability Issues' : 'ประเด็นการพัฒนาที่ยั่งยืนที่เกี่ยวข้อง');'''

new_logic = '''        const col1Title = this.hasAttribute('col1-title') ? this.getAttribute('col1-title') : (lang === 'en' ? 'Engagement Channels' : 'ช่องทางการมีส่วนร่วม');
        const col2Title = this.hasAttribute('col2-title') ? this.getAttribute('col2-title') : (lang === 'en' ? 'Stakeholder Issues' : 'ประเด็นผู้มีส่วนได้เสีย');
        const col3Title = this.hasAttribute('col3-title') ? this.getAttribute('col3-title') : (lang === 'en' ? 'Related Sustainability Issues' : 'ประเด็นการพัฒนาที่ยั่งยืนที่เกี่ยวข้อง');'''

# Replace HTML generation
old_html_gen = '''        if (col1Content) {
            colsHtml += `
                <div class="sh-col">
                    <h5 class="sh-col-title">${col1Title}</h5>
                    <div class="sh-col-content">${col1Content}</div>
                </div>
            `;
        }
        if (col2Content) {
            colsHtml += `
                <div class="sh-col">
                    <h5 class="sh-col-title">${col2Title}</h5>
                    <div class="sh-col-content">${col2Content}</div>
                </div>
            `;
        }
        if (col3Content) {
            colsHtml += `
                <div class="sh-col">
                    <h5 class="sh-col-title">${col3Title}</h5>
                    <div class="sh-col-content">${col3Content}</div>
                </div>
            `;
        }'''

new_html_gen = '''        if (col1Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col1Title ? `<h5 class="sh-col-title">${col1Title}</h5>` : ''}
                    <div class="sh-col-content">${col1Content}</div>
                </div>
            `;
        }
        if (col2Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col2Title ? `<h5 class="sh-col-title">${col2Title}</h5>` : ''}
                    <div class="sh-col-content">${col2Content}</div>
                </div>
            `;
        }
        if (col3Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col3Title ? `<h5 class="sh-col-title">${col3Title}</h5>` : ''}
                    <div class="sh-col-content">${col3Content}</div>
                </div>
            `;
        }'''

if old_logic in content and old_html_gen in content:
    content = content.replace(old_logic, new_logic).replace(old_html_gen, new_html_gen)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated StakeholderCard.js to allow empty titles')
else:
    print('Pattern not found')
