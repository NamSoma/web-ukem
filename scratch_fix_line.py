import os

target = '<div class="desktop-only" style="width: 30px; height: 2px; background: #ccc;"></div>'
replacement = '<div class="desktop-only" style="width: 30px; height: 2px; background: #ccc; margin-right: -30px; z-index: -1;"></div>'

files = ['เกี่ยวกับ UKEM.html', 'en/About UKEM.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace(target, replacement)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
