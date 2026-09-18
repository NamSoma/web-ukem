import os

filepath = r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    
new_content = content.replace('col1-title="Summary"', 'col1-title=""')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
