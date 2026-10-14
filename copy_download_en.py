import os
from pathlib import Path
import re

workspace = Path(r"f:\Back up อีก HDD\งาน\ลองทำ")
src = workspace / "นโยบายและเอกสารดาวน์โหลด.html"
dst = workspace / "en" / "นโยบายและเอกสารดาวน์โหลด.html"

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# Update path in main-nav
content = content.replace('lang="th"', 'lang="en"')
content = content.replace('depth="0"', 'depth="1"')

# Translate headers
content = content.replace('นโยบายบริษัทและเอกสารดาวน์โหลด', 'Company Policies and Download Center')
content = content.replace('รวบรวมนโยบายการดำเนินธุรกิจ รายงาน และเอกสารสำคัญต่างๆ ของบริษัท เพื่อความโปร่งใสและตรวจสอบได้', 'A collection of corporate policies, reports, and essential documents for transparency and accountability.')

# Translate Sidebar
content = content.replace('การกำกับดูแลกิจการ', 'Corporate Governance')
content = content.replace('นโยบายการกำกับดูแลกิจการ', 'Corporate Governance Policy')
content = content.replace('การบริหารจัดการความเสี่ยง', 'Risk Management')
content = content.replace('การควบคุมภายใน', 'Internal Control')
content = content.replace('นโยบายด้านความยั่งยืน (ESG)', 'Sustainability Policy (ESG)')
content = content.replace('นโยบายด้านพนักงาน', 'Human Resources Policy')
content = content.replace('นโยบายคู่ค้าและธุรกิจ', 'Partner & Business Policy')
content = content.replace('รายงานประจำปี (One Report)', 'Annual Report (One Report)')

# Translate document titles
content = content.replace('นโยบายการกำกับดูแลกิจการที่ดี', 'Good Corporate Governance Policy')
content = content.replace('นโยบายต่อต้านการทุจริตคอร์รัปชัน', 'Anti-Corruption Policy')
content = content.replace('นโยบายการแจ้งเบาะแส (Whistleblowing Policy)', 'Whistleblowing Policy')
content = content.replace('นโยบายการบริหารจัดการความเสี่ยง', 'Risk Management Policy')
content = content.replace('นโยบายความยั่งยืนระดับองค์กร', 'Corporate Sustainability Policy')
content = content.replace('นโยบายด้านสิ่งแวดล้อมและพลังงาน', 'Environmental and Energy Policy')
content = content.replace('นโยบายสิทธิมนุษยชน', 'Human Rights Policy')
content = content.replace('นโยบายความปลอดภัย อาชีวอนามัย และสภาพแวดล้อมในการทำงาน', 'Occupational Health and Safety Policy')
content = content.replace('นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน', 'Sustainable Procurement Policy')
content = content.replace('นโยบายสำหรับคู่ค้าและกระบวนการขาย', 'Policy for Partners and Sales Process')
content = content.replace('นโยบายความปลอดภัยและความรับผิดชอบต่อผลิตภัณฑ์', 'Product Safety and Responsibility Policy')
content = content.replace('รายงานประจำปี (56-1 One Report) 2568', 'Annual Registration Statement (56-1 One Report) 2025')
content = content.replace('รายงานความยั่งยืน (Sustainability Report) 2568', 'Sustainability Report (ESG) 2025')

# Metadata and buttons
content = content.replace('อัปเดตล่าสุด: ปี 2567 | ไฟล์ PDF', 'Last Updated: 2024 | PDF File')
content = content.replace('ไฟล์ PDF', 'PDF File')
content = content.replace('ขนาดไฟล์: 7.9 MB | ไฟล์ PDF', 'File Size: 7.9 MB | PDF File')
content = content.replace('ดาวน์โหลดฉบับภาษาไทย', 'Download English Version')
content = content.replace('ดาวน์โหลด', 'Download')

# Update the PDF links to the English versions where applicable!
content = content.replace('ukem-or-2025-th.pdf', '../assets/เอกสารดาวน์โหลด/ukem-or-2025-en.pdf')
content = content.replace('assets/เอกสารภาพรวมความยั่งยืน/ESG_Report_2025.pdf', '../assets/เอกสารดาวน์โหลด/ESG_Report_2025_en.pdf')
content = content.replace('assets/เอกสารดาวน์โหลด/นโยบายการขายและการตลาด.pdf', '../assets/เอกสารดาวน์โหลด/SALES AND MARKETING POLICY.pdf')
content = content.replace('assets/เอกสารสังคม/นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฎิบัติ.pdf', '../assets/เอกสารสังคม/Labor, Human Rights and Non-Discrimination Policy.pdf')
content = content.replace('นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฏิบัติ', 'Labor, Human Rights and Non-Discrimination Policy')
content = content.replace('https://www.unionpetrochemical.com/wp-content/uploads/2026/06/นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน.pdf', '../assets/เอกสารดาวน์โหลด/นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน.pdf')
content = content.replace('assets/เอกสารกำกับดูแล/ประกาศนโยบายการควบคุมการปฏิบัติงาน.pdf', '../assets/เอกสารกำกับดูแล/Policy on Operations Control and Security En.pdf')
content = content.replace('ประกาศนโยบายการควบคุมการปฏิบัติงาน', 'Policy on Operations Control and Security')
content = content.replace('Operational Control Policy', 'Policy on Operations Control and Security')
content = content.replace('https://www.unionpetrochemical.com/wp-content/uploads/2026/06/Sustainable-Procurement-Policy.pdf', '../assets/เอกสารดาวน์โหลด/SUSTAINABLE PROCUREMENT POLICY.pdf')
content = content.replace('assets/เอกสารกำกับดูแล/แนวปฏิบัติแผนรองรับและแนวทางป้องกัน.pdf', '../assets/เอกสารกำกับดูแล/Emergency Preparedness and Preventive Measures for Information Technology Disasters.pdf')
content = content.replace('แนวปฏิบัติแผนรองรับและแนวทางป้องกันกรณีระบบไอที', 'Emergency Preparedness and Preventive Measures for Information Technology Disasters')
content = content.replace('IT Incident Response and Prevention Plan', 'Emergency Preparedness and Preventive Measures for Information Technology Disasters')
content = content.replace('assets/เอกสารดาวน์โหลด/นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน.pdf', '../assets/เอกสารดาวน์โหลด/SUSTAINABLE PROCUREMENT POLICY.pdf')

# Update relative paths to PDFs for deep links (since this is in en/ folder, we need ../)
def repl_href(m):
    href = m.group(1)
    if href.startswith('http') or href.startswith('#') or href.startswith('../'):
        return f'href="{href}"'
    return f'href="../{href}"'

content = re.sub(r'href="([^"]+\.pdf)"', repl_href, content)

# Save
with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created en/นโยบายและเอกสารดาวน์โหลด.html")
