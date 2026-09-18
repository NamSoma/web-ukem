import os
import re

files_to_process = [
    r'f:\Back up อีก HDD\งาน\ลองทำ\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html'
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
    
    lang = 'en' if 'en\\' in filepath else 'th'
    col1_title = 'Summary' if lang == 'en' else 'สาระสำคัญโดยสรุป'
    
    for row in rows:
        cells = cell_regex.findall(row)
        if len(cells) == 3:
            num = re.sub(r'<[^>]+>', '', cells[0]).strip()
            issue = re.sub(r'<[^>]+>', '', cells[1]).strip()
            summary = cells[2].strip()
            
            title = f"{num}. {issue}"
            
            # The summary is not a ul list currently, it's just plain text.
            # Our component expects text or ul. To look good, we can wrap it in a <p> or leave it.
            # I will wrap it in a div with some styling or just leave it.
            # Actually, the component styling works fine with plain text.
            
            new_html += f'''    <stakeholder-card title="{title}" col1-title="{col1_title}">
        <div slot="col1">
            <p style="margin:0;">{summary}</p>
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
            # adjust path for en
            if 'en\\' in filepath:
                script_tag = '    <script src="../../components/StakeholderCard.js" defer></script>\n'
            new_full_html = new_full_html[:head_end] + script_tag + new_full_html[head_end:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
        
    print(f"Processed successfully: {filepath}")
