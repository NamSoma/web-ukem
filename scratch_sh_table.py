import os
import re

files_to_process = [
    r'f:\Back up อีก HDD\งาน\ลองทำ\ภาพรวมความยั่งยืน\ห่วงโซ่คุณค่าของธุรกิจ.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\ห่วงโซ่คุณค่าของธุรกิจ.html'
]

table_regex = re.compile(r'<table class="sh-table">.*?<tbody>(.*?)</tbody>.*?</table>', re.DOTALL)
row_regex = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
cell_regex = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

for filepath in files_to_process:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    match = table_regex.search(html)
    if not match:
        print(f"Table not found in {filepath}")
        continue
        
    inner_html = match.group(1)
    rows = row_regex.findall(inner_html)
    
    new_html = '<div class="sh-container">\n'
    
    for row in rows:
        cells = cell_regex.findall(row)
        if len(cells) == 4:
            title = re.sub(r'<[^>]+>', '', cells[0]).strip()
            
            col1 = cells[1].strip()
            col2 = cells[2].strip()
            col3 = cells[3].strip()
            
            new_html += f'''    <stakeholder-card title="{title}">
        <div slot="col1">
            {col1}
        </div>
        <div slot="col2">
            {col2}
        </div>
        <div slot="col3">
            {col3}
        </div>
    </stakeholder-card>\n'''
            
    new_html += '</div>\n'
    
    # Replace the whole table
    new_full_html = html[:match.start()] + new_html + html[match.end():]
    
    # Add script tag if missing
    if 'StakeholderCard.js' not in new_full_html:
        head_end = new_full_html.find('</head>')
        if head_end != -1:
            script_tag = '    <script src="../components/StakeholderCard.js" defer></script>\n'
            new_full_html = new_full_html[:head_end] + script_tag + new_full_html[head_end:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
        
    print(f"Processed successfully.")
