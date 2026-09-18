import os

files = [
    r'f:\Back up อีก HDD\งาน\ลองทำ\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content.replace('<stakeholder-card title=', '<stakeholder-card title-width="35" title=')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
