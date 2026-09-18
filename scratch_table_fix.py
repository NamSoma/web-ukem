import os, re
filepath = r'f:\Back up อีก HDD\งาน\ลองทำ\en\ภาพรวมความยั่งยืน\ห่วงโซ่คุณค่าของธุรกิจ.html'

def extract_table_data(html):
    table_match = re.search(r'<table class="vc-table">(.*?)</table>', html, re.DOTALL)
    if not table_match: return None
    table_content = table_match.group(1)
    headers_raw = re.findall(r'<th[^>]*>(.*?)</th>', table_content, re.DOTALL)
    headers = [h for h in headers_raw if 'Value Chain' not in h]
    tds = re.findall(r'<td[^>]*>(.*?)</td>', table_content, re.DOTALL)
    return headers, tds

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

data = extract_table_data(html)
if data:
    headers, tds = data
    new_html = '<div class="value-chain-container">\n'
    for i in range(len(headers)):
        header_text = re.sub(r'<br\s*/?>', ' ', headers[i].strip(), flags=re.IGNORECASE)
        td_content = tds[i].strip()
        new_html += f'''    <div class="vc-card">
        <div class="vc-card-header">
            <h4>{header_text}</h4>
        </div>
        <div class="vc-card-body">
            {td_content}
        </div>
    </div>\n'''
        if i < len(headers) - 1:
            new_html += '    <div class="vc-arrow"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>\n'
    new_html += '</div>'
    new_full_html = re.sub(r'<table class="vc-table">.*?</table>', new_html, html, flags=re.DOTALL)
    new_full_html = new_full_html.replace('style="margin-top: 60px; overflow-x: auto; padding-bottom: 20px;"', 'style="margin-top: 40px; margin-bottom: 40px;"')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
    print('Converted English file.')
