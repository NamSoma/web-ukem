import os
file = r'f:\Back up อีก HDD\งาน\ลองทำ\components\StakeholderCard.js'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_html = '''            <div class="sh-row">
                <div class="sh-title-col">
                    <h4 class="sh-title">${title}</h4>
                </div>
                <div class="sh-content-col">'''

new_html = '''            <div class="sh-row">
                <div class="sh-title-col" ${this.hasAttribute('title-width') ? `style="flex: 0 0 ${this.getAttribute('title-width')}%;"` : ''}>
                    <h4 class="sh-title">${title}</h4>
                </div>
                <div class="sh-content-col" ${this.hasAttribute('title-width') ? `style="flex: 0 0 ${100 - parseInt(this.getAttribute('title-width'))}%;"` : ''}>'''

if old_html in content:
    content = content.replace(old_html, new_html)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated StakeholderCard.js')
else:
    print('old html not found')
