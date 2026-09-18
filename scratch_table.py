import os
import re

files = [
    r'f:\Back up อีก HDD\งาน\ลองทำ\ภาพรวมความยั่งยืน\ห่วงโซ่คุณค่าของธุรกิจ.html',
    r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\ห่วงโซ่คุณค่าของธุรกิจ.html'
]

def extract_table_data(html):
    # Find the table contents
    table_match = re.search(r'<table class="vc-table">(.*?)</table>', html, re.DOTALL)
    if not table_match:
        print("vc-table not found")
        return None
    table_content = table_match.group(1)
    
    # Extract headers (skip the title-row which has colspan="6")
    headers_raw = re.findall(r'<th[^>]*>(.*?)</th>', table_content, re.DOTALL)
    
    # Filter out the title row (the one with Value Chain)
    headers = [h for h in headers_raw if 'Value Chain' not in h and 'ห่วงโซ่คุณค่า' not in h]
    
    # Extract the tds
    tds = re.findall(r'<td[^>]*>(.*?)</td>', table_content, re.DOTALL)
    
    return headers, tds

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    data = extract_table_data(html)
    if not data:
        print(f"Skipping {filepath}")
        continue
    
    headers, tds = data
    
    if len(headers) != len(tds):
        print(f"Mismatch in {filepath}: {len(headers)} headers, {len(tds)} tds")
        continue
    
    new_html = '<div class="value-chain-container">\n'
    for i in range(len(headers)):
        header = headers[i].strip()
        # Clean up <br> to space
        header_text = re.sub(r'<br\s*/?>', ' ', header, flags=re.IGNORECASE)
        td_content = tds[i].strip()
        
        # In td_content, ensure ul has a class if needed, but it's fine without.
        
        new_html += f'''
    <div class="vc-card">
        <div class="vc-card-header">
            <h4>{header_text}</h4>
        </div>
        <div class="vc-card-body">
            {td_content}
        </div>
    </div>
'''
        # Add arrow if not the last card
        if i < len(headers) - 1:
            new_html += '    <div class="vc-arrow"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>\n'
    
    new_html += '</div>'
    
    new_full_html = re.sub(r'<table class="vc-table">.*?</table>', new_html, html, flags=re.DOTALL)
    new_full_html = new_full_html.replace('style="margin-top: 60px; overflow-x: auto; padding-bottom: 20px;"', 'style="margin-top: 40px; margin-bottom: 40px;"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
    print(f"Updated {filepath}")
