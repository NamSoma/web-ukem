import os
import re

filepath = r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html'

table_regex = re.compile(r'<table class="sh-table">.*?<tbody>(.*?)</tbody>.*?</table>', re.DOTALL)
row_regex = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
cell_regex = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
    
match = table_regex.search(html)
if match:
    inner_html = match.group(1)
    rows = row_regex.findall(inner_html)
    
    new_html = '<div class="sh-container">\n'
    col1_title = 'Summary'
    
    for row in rows:
        cells = cell_regex.findall(row)
        if len(cells) == 3:
            num = re.sub(r'<[^>]+>', '', cells[0]).strip()
            issue = re.sub(r'<[^>]+>', '', cells[1]).strip()
            summary = cells[2].strip()
            title = f'{num}. {issue}'
            new_html += f'''    <stakeholder-card title="{title}" col1-title="{col1_title}">
        <div slot="col1">
            <p style="margin:0;">{summary}</p>
        </div>
    </stakeholder-card>\n'''
            
    new_html += '</div>\n'
    new_full_html = html[:match.start()] + new_html + html[match.end():]
    
    if 'StakeholderCard.js' not in new_full_html:
        head_end = new_full_html.find('</head>')
        if head_end != -1:
            script_tag = '    <script src="../../components/StakeholderCard.js" defer></script>\n'
            new_full_html = new_full_html[:head_end] + script_tag + new_full_html[head_end:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
    print('Processed EN file')
else:
    print('Table not found')
