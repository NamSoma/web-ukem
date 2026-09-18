import os
import re
import json

directory = r"f:\Back up อีก HDD\งาน\ลองทำ"
json_path = os.path.join(directory, 'scratch_pdf_results.json')

with open(json_path, 'r', encoding='utf-8') as f:
    pdf_results = json.load(f)

# Deduplicate PDFs based on URL, keeping TH/EN logic in mind
# Let's manually categorize them since there are ~25 unique ones.

categories = {
    'reports': {
        'th_label': 'รายงานและการดำเนินการด้าน ESG',
        'en_label': 'ESG Reports & Performance',
        'keywords': ['ESG', 'One Report', 'แบบแสดงรายการข้อมูลประจำปี']
    },
    'gov': {
        'th_label': 'นโยบายและการกำกับดูแลกิจการ',
        'en_label': 'Corporate Governance & Policies',
        'keywords': ['กำกับดูแล', 'จรรยาบรรณ', 'คอร์รัปชัน', 'ตรวจสอบ', 'PDPA', 'Take Down', 'ความเสี่ยง', 'Governance', 'Code of Conduct', 'Anti-Corruption', 'Audit', 'Risk', 'Complaint']
    },
    'env': {
        'th_label': 'สิ่งแวดล้อม',
        'en_label': 'Environment',
        'keywords': ['สิ่งแวดล้อม', 'ภูมิอากาศ', 'คาร์บอน', 'ชีวภาพ', 'Climate', 'Carbon', 'Biodiversity']
    },
    'soc': {
        'th_label': 'สังคมและสิทธิมนุษยชน',
        'en_label': 'Social & Human Rights',
        'keywords': ['แรงงาน', 'สิทธิมนุษยชน', 'จัดซื้อ', 'ผู้หญิง', 'Labor', 'Human Rights', 'Procurement', 'Migrant', 'Women']
    }
}

def get_category(title):
    for cat_id, cat_info in categories.items():
        for kw in cat_info['keywords']:
            if kw.lower() in title.lower():
                return cat_id
    return 'reports' # default

th_docs = {}
en_docs = {}

for item in pdf_results:
    if item['file'] == 'ศูนย์รวมการดาวน์โหลด.html' or item['file'] == 'en/ศูนย์รวมการดาวน์โหลด.html' or item['file'] == 'index.html' or item['file'] == 'en/index.html':
        continue
    
    cat = get_category(item['title'])
    # adjust url if relative
    url = item['url']
    if url.startswith('../'):
        url = url[3:]
    if url.startswith('../../'):
        url = url[6:]
        
    if item['file'].startswith('en/'):
        if url not in [x['url'] for x in en_docs.get(cat, [])]:
            en_docs.setdefault(cat, []).append({'title': item['title'], 'url': url})
    else:
        if url not in [x['url'] for x in th_docs.get(cat, [])]:
            th_docs.setdefault(cat, []).append({'title': item['title'], 'url': url})

# add one reports and missing stuff from index
th_docs['reports'].insert(0, {'title': 'แบบแสดงรายการข้อมูลประจำปี (One Report) 2568', 'url': 'ukem-or-2025-th.pdf'})
th_docs['reports'].insert(0, {'title': 'รายงานผลการดำเนินงานด้าน ESG ประจำปี 2568', 'url': 'assets/เอกสารภาพรวมความยั่งยืน/ESG_Report_2025.pdf'})

en_docs['reports'].insert(0, {'title': 'Annual Registration Statement (One Report) 2025', 'url': 'ukem-or-2025-th.pdf'})
en_docs['reports'].insert(0, {'title': 'ESG Performance Report 2025', 'url': 'assets/เอกสารภาพรวมความยั่งยืน/ESG_Report_2025.pdf'})


def generate_html(docs, is_en=False):
    html = '<div class="download-list">\n'
    for cat_id, cat_info in categories.items():
        cat_docs = docs.get(cat_id, [])
        if not cat_docs: continue
        
        label = cat_info['en_label'] if is_en else cat_info['th_label']
        html += f'    <div>\n        <h2 class="section-label" style="margin-top: 20px;">{label}</h2>\n    </div>\n'
        
        for doc in cat_docs:
            # deduplicate
            # prefix with ../ if it's the EN center and the url is local (not http)
            url = doc['url']
            if is_en and not url.startswith('http'):
                url = '../' + url
            
            html += f'    <div style="margin-bottom: 15px;">\n'
            html += f'        <doc-card \n'
            html += f'            url="{url}" \n'
            html += f'            title="{doc["title"]}" \n'
            html += f'            meta="PDF">\n'
            html += f'        </doc-card>\n'
            html += f'    </div>\n'
    html += '</div>'
    return html

# 1. Update Download Centers
def update_center(filepath, docs, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_list_html = generate_html(docs, is_en)
    
    # regex replace the download-list div
    content = re.sub(r'<div class="download-list">.*?</div>\s*(?=</main>|</div>\s*</main>)', new_list_html + '\n', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_center(os.path.join(directory, 'ศูนย์รวมการดาวน์โหลด.html'), th_docs, is_en=False)
update_center(os.path.join(directory, 'en', 'ศูนย์รวมการดาวน์โหลด.html'), en_docs, is_en=True)


# 2. Cleanup all other files
for root, _, files in os.walk(directory):
    if "scratch" in root or ".gemini" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith('.html') and file not in ['ศูนย์รวมการดาวน์โหลด.html', 'index.html']:
            filepath = os.path.join(root, file)
            content = None
            encoding_used = 'utf-8'
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, 'r', encoding='utf-16') as f:
                        content = f.read()
                        encoding_used = 'utf-16'
                except Exception:
                    pass
            
            if content:
                # Remove <doc-section>...</doc-section> entirely
                new_content = re.sub(r'<doc-section[^>]*>.*?</doc-section>', '', content, flags=re.DOTALL)
                
                # In some files, there might be stray <doc-card> without <doc-section>
                # Let's remove them too just in case
                new_content = re.sub(r'<doc-card[^>]*>.*?</doc-card>', '', new_content, flags=re.DOTALL)
                
                # In Corporate Governance page, there's a title "ดาวน์โหลดเอกสาร"
                new_content = re.sub(r'<h3[^>]*>ดาวน์โหลดเอกสาร</h3>', '', new_content, flags=re.IGNORECASE)
                new_content = re.sub(r'<h3[^>]*>Document Download</h3>', '', new_content, flags=re.IGNORECASE)
                
                if new_content != content:
                    with open(filepath, 'w', encoding=encoding_used) as f:
                        f.write(new_content)
                    print(f"Cleaned up {filepath}")

print("Script completed")
