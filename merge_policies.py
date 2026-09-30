import re
import os

base_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'

def merge_content(lang_dir, is_en=False):
    if is_en:
        download_html_path = os.path.join(base_dir, 'en', 'นโยบายและเอกสารดาวน์โหลด.html')
        control_html_path = os.path.join(base_dir, 'en', 'การกำกับดูแลและเศรษฐกิจ', 'การควบคุมภายใน.html')
        risk_html_path = os.path.join(base_dir, 'en', 'การกำกับดูแลและเศรษฐกิจ', 'การบริหารจัดการความเสี่ยง.html')
    else:
        download_html_path = os.path.join(base_dir, 'นโยบายและเอกสารดาวน์โหลด.html')
        control_html_path = os.path.join(base_dir, 'การกำกับดูแลและเศรษฐกิจ', 'การควบคุมภายใน.html')
        risk_html_path = os.path.join(base_dir, 'การกำกับดูแลและเศรษฐกิจ', 'การบริหารจัดการความเสี่ยง.html')

    with open(download_html_path, 'r', encoding='utf-8') as f:
        download_html = f.read()

    with open(control_html_path, 'r', encoding='utf-8') as f:
        control_html = f.read()

    with open(risk_html_path, 'r', encoding='utf-8') as f:
        risk_html = f.read()

    # Find the main container content using a more robust search
    def extract_container(html):
        match = re.search(r'<div class="container[^>]*>(.*?)</div>\s*</main>', html, re.DOTALL)
        if match: return match.group(1).strip()
        # Fallback if there is a section before main ends
        match = re.search(r'<div class="container[^>]*>(.*?)</div>\s*<section', html, re.DOTALL)
        if match: return match.group(1).strip()
        # Manual fallback
        start_tag = '<section-header'
        end_tag = '    </main>'
        start_idx = html.find(start_tag)
        end_idx = html.rfind('</div>', 0, html.find(end_tag))
        if start_idx != -1 and end_idx != -1:
            return html[start_idx:end_idx].strip()
        return None

    control_content = extract_container(control_html)
    if not control_content:
        print("Could not find control content")
        return
    
    style_match = re.search(r'<style>(.*?)</style>', control_html, re.DOTALL)
    if style_match:
        control_content = f"<style>{style_match.group(1)}</style>\n{control_content}"

    risk_content = extract_container(risk_html)
    if not risk_content:
        print("Could not find risk content")
        return
    
    style_match = re.search(r'<style>(.*?)</style>', risk_html, re.DOTALL)
    if style_match:
        risk_content = f"<style>{style_match.group(1)}</style>\n{risk_content}"

    # Now we insert control_content into download_html inside <div id="gov_control" ...> 
    download_html = re.sub(
        r'(<div id="gov_control" class="category-section[^>]*>\s*<h2 class="section-title"[^>]*>.*?</h2>)',
        r'\1\n<div class="policy-content-wrapper">' + control_content.replace('\\', '\\\\') + r'</div>\n<h3 style="margin-top:40px; color:var(--primary);">' + ('เอกสารดาวน์โหลด' if not is_en else 'Download Documents') + '</h3>\n',
        download_html,
        flags=re.DOTALL
    )

    # Insert risk_content into download_html inside <div id="gov_risk" ...>
    download_html = re.sub(
        r'(<div id="gov_risk" class="category-section[^>]*>\s*<h2 class="section-title"[^>]*>.*?</h2>)',
        r'\1\n<div class="policy-content-wrapper">' + risk_content.replace('\\', '\\\\') + r'</div>\n<h3 style="margin-top:40px; color:var(--primary);">' + ('เอกสารดาวน์โหลด' if not is_en else 'Download Documents') + '</h3>\n',
        download_html,
        flags=re.DOTALL
    )

    with open(download_html_path, 'w', encoding='utf-8') as f:
        f.write(download_html)
        
    print(f"Successfully merged for {'EN' if is_en else 'TH'}")

merge_content(base_dir, False)
merge_content(base_dir, True)
