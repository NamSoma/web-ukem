import os
import re

base_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'

def extract_container(html):
    match = re.search(r'<div class="container[^>]*>(.*?)</div>\s*</main>', html, re.DOTALL)
    if match: return match.group(1).strip()
    match = re.search(r'<div class="container[^>]*>(.*?)</div>\s*<section', html, re.DOTALL)
    if match: return match.group(1).strip()
    start_tag = '<section-header'
    end_tag = '    </main>'
    start_idx = html.find(start_tag)
    end_idx = html.rfind('</div>', 0, html.find(end_tag))
    if start_idx != -1 and end_idx != -1:
        return html[start_idx:end_idx].strip()
    return ''

risk_path = os.path.join(base_dir, 'การกำกับดูแลและเศรษฐกิจ', 'การบริหารจัดการความเสี่ยง.html')
with open(risk_path, 'r', encoding='utf-8') as f:
    risk_html = f.read()

risk_content = extract_container(risk_html)
style_risk = re.search(r'<style>(.*?)</style>', risk_html, re.DOTALL)
if style_risk:
    risk_content = f'<style>{style_risk.group(1)}</style>\n' + risk_content

file_path = os.path.join(base_dir, 'นโยบายและเอกสารดาวน์โหลด.html')
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''                <div id="gov_risk" class="category-section">
                    <h2 class="section-title">นโยบายบริหารจัดการความเสี่ยง</h2>
                    <div class="doc-item">'''

replacement = f'''                <div id="gov_risk" class="category-section">
                    <h2 class="section-title">นโยบายบริหารจัดการความเสี่ยง</h2>
                    <div class="policy-content-wrapper">{risk_content}</div>
                    <h3 style="margin-top:40px; color:var(--primary);">เอกสารดาวน์โหลด</h3>
                    <div class="doc-item">'''

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Restored risk content')
else:
    print('Target not found')
