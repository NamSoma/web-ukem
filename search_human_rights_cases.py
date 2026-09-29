import os
import re
import fitz

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['คดีสิทธิมนุษยชน', 'ข้อร้องเรียนด้านสิทธิมนุษยชน', 'คดีความด้านสิทธิมนุษยชน', 'ข้อพิพาท', 'ข้อร้องเรียน']

found = []

# Check PDF First (since litigations are usually there)
pdf_path = os.path.join(root_dir, 'ukem-or-2025-th.pdf')
try:
    doc = fitz.open(pdf_path)
    pdf_text = ''.join([page.get_text() for page in doc])
    for keyword in keywords:
        if re.search(keyword, pdf_text, re.IGNORECASE):
            # Only care about these if they are near 'สิทธิมนุษยชน' or 'ละเมิด'
            if keyword in ['ข้อพิพาท', 'ข้อร้องเรียน']:
                if not re.search(r'(ข้อพิพาท|ข้อร้องเรียน).{0,100}สิทธิมนุษยชน|สิทธิมนุษยชน.{0,100}(ข้อพิพาท|ข้อร้องเรียน)', pdf_text, re.IGNORECASE | re.DOTALL):
                    continue
            
            snippet_matches = re.finditer(f'(.{{0,50}}{keyword}.{{0,50}})', pdf_text, re.IGNORECASE | re.DOTALL)
            for snippet_match in snippet_matches:
                snippet = snippet_match.group(1).replace('\n', ' ').strip()
                found.append(f"PDF File: ukem-or-2025-th.pdf | Keyword: {keyword}\nSnippet: {snippet}\n")
except Exception as e:
    found.append(f"PDF Error: {e}\n")

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
                    if keyword in ['ข้อพิพาท', 'ข้อร้องเรียน']:
                        if not re.search(r'(ข้อพิพาท|ข้อร้องเรียน).{0,100}สิทธิมนุษยชน|สิทธิมนุษยชน.{0,100}(ข้อพิพาท|ข้อร้องเรียน)', content, re.IGNORECASE | re.DOTALL):
                            continue
                            
                    snippet_match = re.search(f'(.{{0,50}}{keyword}.{{0,50}})', content, re.IGNORECASE | re.DOTALL)
                    if snippet_match:
                        snippet = snippet_match.group(1).replace('\n', ' ').strip()
                        found.append(f"Web File: {os.path.relpath(filepath, root_dir)} | Keyword: {keyword}\nSnippet: {snippet}\n")

with open('search_human_rights_cases.txt', 'w', encoding='utf-8') as out:
    if found:
        out.write("Found mentions:\n")
        for item in found:
            out.write(item + "\n")
    else:
        out.write("No mentions found.\n")
