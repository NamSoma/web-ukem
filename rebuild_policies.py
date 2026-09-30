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
    return ""

def rebuild_page(is_en=False):
    lang_prefix = "en/" if is_en else ""
    path_prefix = "../" if is_en else ""
    
    # Paths to risk and control
    control_path = os.path.join(base_dir, lang_prefix, 'การกำกับดูแลและเศรษฐกิจ', 'การควบคุมภายใน.html')
    risk_path = os.path.join(base_dir, lang_prefix, 'การกำกับดูแลและเศรษฐกิจ', 'การบริหารจัดการความเสี่ยง.html')
    
    # Read risk and control
    with open(control_path, 'r', encoding='utf-8') as f:
        control_html = f.read()
    with open(risk_path, 'r', encoding='utf-8') as f:
        risk_html = f.read()
        
    control_content = extract_container(control_html)
    risk_content = extract_container(risk_html)
    
    # Styles for control and risk
    style_control = re.search(r'<style>(.*?)</style>', control_html, re.DOTALL)
    if style_control: control_content = f"<style>{style_control.group(1)}</style>\n" + control_content
    style_risk = re.search(r'<style>(.*?)</style>', risk_html, re.DOTALL)
    if style_risk: risk_content = f"<style>{style_risk.group(1)}</style>\n" + risk_content

    # Strings
    title_text = "Company Policies and Download Center" if is_en else "นโยบายบริษัทและเอกสารดาวน์โหลด"
    desc_text = "A collection of corporate policies, reports, and essential documents for transparency and accountability." if is_en else "รวบรวมนโยบายการดำเนินธุรกิจ รายงาน และเอกสารสำคัญต่างๆ ของบริษัท เพื่อความโปร่งใสและตรวจสอบได้"
    
    menu_org = "Corporate Governance" if is_en else "นโยบายการกำกับดูแลกิจการ"
    menu_risk = "Risk Management Policy" if is_en else "นโยบายบริหารจัดการความเสี่ยง"
    menu_control = "Internal Control" if is_en else "การควบคุมภายใน"
    menu_sus = "Sustainability Policy (ESG)" if is_en else "นโยบายด้านความยั่งยืน (ESG)"
    menu_hr = "Human Resources Policy" if is_en else "นโยบายด้านพนักงาน"
    menu_partner = "Partner & Business Policy" if is_en else "นโยบายคู่ค้าและธุรกิจ"
    
    label_download = "Download Documents" if is_en else "เอกสารดาวน์โหลด"
    label_pdf = "PDF File" if is_en else "ไฟล์ PDF"
    label_update = "Last Updated: 2024 | PDF File" if is_en else "อัปเดตล่าสุด: ปี 2567 | ไฟล์ PDF"
    btn_download = "Download" if is_en else "ดาวน์โหลด"

    html = f"""<!DOCTYPE html>
<html lang="{'en' if is_en else 'th'}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_text} - UKEM</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{path_prefix}css/global.css">
    
    <script src="{path_prefix}components/Navbar.js" defer></script>
    <script src="{path_prefix}components/Footer.js" defer></script>
    <script src="https://unpkg.com/feather-icons"></script>

    <style>
        .page-header {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            padding: 80px 0 60px;
            text-align: center;
            color: white;
            margin-top: 70px;
        }}
        .doc-layout {{
            display: flex;
            gap: 40px;
            margin-top: -30px;
            position: relative;
            z-index: 10;
        }}
        .doc-sidebar {{
            width: 280px;
            flex-shrink: 0;
            background: var(--surface);
            border-radius: 12px;
            box-shadow: var(--shadow-md);
            position: sticky;
            top: 100px;
            align-self: flex-start;
            padding: 20px;
        }}
        .sidebar-title {{
            font-size: 16px;
            color: var(--text-muted);
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding-left: 15px;
        }}
        .sidebar-menu {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .sidebar-btn {{
            display: block;
            width: 100%;
            text-align: left;
            padding: 12px 15px;
            background: none;
            border: none;
            border-left: 3px solid transparent;
            color: var(--text-main);
            font-size: 16px;
            font-family: 'Kanit', sans-serif;
            cursor: pointer;
            transition: all 0.3s;
            border-radius: 0 8px 8px 0;
        }}
        .sidebar-btn:hover {{
            background: rgba(43, 147, 219, 0.05);
            color: var(--primary);
        }}
        .sidebar-btn.active {{
            background: rgba(43, 147, 219, 0.1);
            color: var(--primary);
            border-left-color: var(--primary);
            font-weight: 500;
        }}
        .doc-content {{
            flex-grow: 1;
            background: var(--surface);
            border-radius: 12px;
            box-shadow: var(--shadow-md);
            padding: 40px;
            min-height: 500px;
        }}
        .category-section {{
            display: none;
            animation: fadeIn 0.4s ease;
        }}
        .category-section.active {{
            display: block;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .section-title {{
            color: var(--primary);
            border-bottom: 2px solid var(--border);
            padding-bottom: 15px;
            margin-bottom: 30px;
            font-size: 24px;
        }}
        .doc-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            border: 1px solid var(--border);
            border-radius: 8px;
            margin-bottom: 15px;
            transition: all 0.3s;
        }}
        .doc-item:hover {{
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-color: #cbd5e1;
            transform: translateX(5px);
        }}
        .doc-info {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .doc-icon {{
            color: var(--secondary);
            background: rgba(43, 147, 219, 0.1);
            padding: 12px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .doc-text h4 {{
            margin: 0 0 5px 0;
            font-size: 18px;
            color: var(--text-main);
        }}
        .doc-text p {{
            margin: 0;
            font-size: 14px;
            color: var(--text-muted);
        }}
        .doc-download-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--primary);
            color: white;
            padding: 8px 20px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.3s;
        }}
        .doc-download-btn:hover {{
            background: #122d50;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(25, 63, 110, 0.2);
        }}
        @media (max-width: 900px) {{
            .doc-layout {{ flex-direction: column; }}
            .doc-sidebar {{ width: 100%; position: static; }}
            .doc-item {{ flex-direction: column; align-items: flex-start; gap: 15px; }}
            .doc-download-btn {{ width: 100%; justify-content: center; }}
        }}
    </style>
</head>
<body>

    <main-nav depth="{'1' if is_en else '0'}" path="นโยบายและเอกสารดาวน์โหลด.html" lang="{'en' if is_en else 'th'}"></main-nav>

    <header class="page-header">
        <div class="container">
            <h1 style="margin-bottom: 15px; font-size: 36px; color: white;">{title_text}</h1>
            <p style="font-size: 18px; color: #e2e8f0; max-width: 700px; margin: 0 auto;">
                {desc_text}
            </p>
        </div>
    </header>

    <main class="container">
        <div class="doc-layout">
            
            <aside class="doc-sidebar">
                <div style="padding: 25px 0 0 0;">
                    <div class="sidebar-group">
                        <ul class="sidebar-menu">
                            <li><button class="sidebar-btn active" data-target="gov_policy">{menu_org}</button></li>
                            <li><button class="sidebar-btn" data-target="gov_risk">{menu_risk}</button></li>
                            <li><button class="sidebar-btn" data-target="gov_control">{menu_control}</button></li>
                            <li><button class="sidebar-btn" data-target="sustainability">{menu_sus}</button></li>
                            <li><button class="sidebar-btn" data-target="hr">{menu_hr}</button></li>
                            <li><button class="sidebar-btn" data-target="partner">{menu_partner}</button></li>
                        </ul>
                    </div>
                </div>
            </aside>

            <div class="doc-content">
                
                <div id="gov_policy" class="category-section active">
                    <h2 class="section-title">{menu_org}</h2>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Good Corporate Governance Policy' if is_en else 'นโยบายการกำกับดูแลกิจการที่ดี'}</h4>
                                <p>{label_update}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/1.-นโยบายกำกับดูแลกิจการที่ดี.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Anti-Corruption Policy' if is_en else 'นโยบายต่อต้านการทุจริตคอร์รัปชัน'}</h4>
                                <p>{label_update}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                </div>

                <div id="gov_risk" class="category-section">
                    <h2 class="section-title">{menu_risk}</h2>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Risk Management Policy' if is_en else 'นโยบายการบริหารจัดการความเสี่ยง'}</h4>
                                <p>{label_update}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/นโยบายบริหารความเสี่ยง.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                </div>

                <div id="gov_control" class="category-section">
                    <h2 class="section-title">{menu_control}</h2>
                    <div class="policy-content-wrapper">{control_content}</div>
                </div>

                <div id="sustainability" class="category-section">
                    <h2 class="section-title">{menu_sus}</h2>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Corporate Sustainability Policy' if is_en else 'นโยบายความยั่งยืนระดับองค์กร'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/นโยบายความยั่งยืนด้านผลิตภัณฑ์ ลูกค้า และ.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Environmental and Energy Policy' if is_en else 'นโยบายการจัดการสิ่งแวดล้อม การป้องกันมลพิษ และการใช้ทรัพยากรอย่างมีประสิทธิภาพ'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}assets/เอกสารสิ่งแวดล้อม/นโยบายการจัดการสิ่งแวดล้อม การป้องกันมลพิษ และการใช้ทรัพยากรอย่างมีประสิทธิภาพ.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Climate Change and Carbon Reduction Policy' if is_en else 'นโยบายการเปลี่ยนแปลงสภาพภูมิอากาศและการลดการปล่อยคาร์บอน'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}assets/เอกสารสิ่งแวดล้อม/นโยบายการเปลี่ยนแปลงสภาพภูมิอากาศและการลดการปล่อยคาร์บอน.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                </div>

                <div id="hr" class="category-section">
                    <h2 class="section-title">{menu_hr}</h2>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Human Rights Policy' if is_en else 'นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฏิบัติ'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="{path_prefix}assets/เอกสารสังคม/นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฎิบัติ.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                </div>

                <div id="partner" class="category-section">
                    <h2 class="section-title">{menu_partner}</h2>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Sustainable Procurement Policy' if is_en else 'นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>{'Personal Data Protection Policy (PDPA)' if is_en else 'นโยบายคุ้มครองข้อมูลส่วนบุคคล (PDPA)'}</h4>
                                <p>{label_pdf}</p>
                            </div>
                        </div>
                        <a href="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/PDPA.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> {btn_download}</a>
                    </div>
                </div>

            </div>
        </div>
    </main>

    <footer-nav depth="{'1' if is_en else '0'}"></footer-nav>

    <script>
        feather.replace();

        document.addEventListener('DOMContentLoaded', function() {{
            const btns = document.querySelectorAll('.sidebar-btn');
            const sections = document.querySelectorAll('.category-section');

            btns.forEach(btn => {{
                btn.addEventListener('click', function(e) {{
                    e.preventDefault();
                    
                    btns.forEach(b => b.classList.remove('active'));
                    sections.forEach(s => s.classList.remove('active'));
                    
                    this.classList.add('active');
                    const targetId = this.getAttribute('data-target');
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {{
                        targetElement.classList.add('active');
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""
    file_path = os.path.join(base_dir, lang_prefix, 'นโยบายและเอกสารดาวน์โหลด.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

rebuild_page(False)
