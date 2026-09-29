import os
import re
import fitz

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['การป้องกันการเลือกปฏิบัติต่อชุมชน', 'การเลือกปฏิบัติต่อชุมชน', 'ไม่เลือกปฏิบัติต่อชุมชน', 'เลือกปฏิบัติ']

found = []

# Check HTML files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue

            for keyword in keywords:
                if re.search(keyword, content, re.IGNORECASE):
                    snippet_match = re.search(f'(.{{0,50}}{keyword}.{{0,50}})', content, re.IGNORECASE | re.DOTALL)
                    if snippet_match:
                        snippet = snippet_match.group(1).replace('\n', ' ').strip()
                        found.append(f"Web File: {os.path.relpath(filepath, root_dir)} | Keyword: {keyword}\nSnippet: {snippet}\n")

# Check PDF
pdf_path = os.path.join(root_dir, 'ukem-or-2025-th.pdf')
try:
    doc = fitz.open(pdf_path)
    pdf_text = ''.join([page.get_text() for page in doc])
    for keyword in keywords:
        if re.search(keyword, pdf_text, re.IGNORECASE):
            # for 'เลือกปฏิบัติ' we only care if it's near 'ชุมชน'
            if keyword == 'เลือกปฏิบัติ':
                if not re.search(r'เลือกปฏิบัติ.{0,100}ชุมชน|ชุมชน.{0,100}เลือกปฏิบัติ', pdf_text, re.IGNORECASE | re.DOTALL):
                    continue
            
            snippet_match = re.search(f'(.{{0,50}}{keyword}.{{0,50}})', pdf_text, re.IGNORECASE | re.DOTALL)
            if snippet_match:
                snippet = snippet_match.group(1).replace('\n', ' ').strip()
                found.append(f"PDF File: ukem-or-2025-th.pdf | Keyword: {keyword}\nSnippet: {snippet}\n")
except Exception as e:
    found.append(f"PDF Error: {e}\n")

with open('search_discrimination.txt', 'w', encoding='utf-8') as out:
    if found:
        out.write("Found mentions:\n")
        for item in found:
            out.write(item + "\n")
    else:
        out.write("No mentions found.\n")
