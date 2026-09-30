import os

files = [
    r'f:\Back up อีก HDD\งาน\ลองทำ\index.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\เกี่ยวกับ UKEM.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\About UKEM.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\index.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html'
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if 'viewport' not in content:
            new_content = content.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
            
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as out:
                    out.write(new_content)
