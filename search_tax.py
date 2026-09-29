import os
import re
import fitz

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['ภาษีเงินได้นิติบุคคล', 'ภาษีเงินได้ที่จ่าย', 'การจ่ายภาษี', 'ภาษีเงินได้']

found = []

# Check PDF
pdf_path = os.path.join(root_dir, 'ukem-or-2025-th.pdf')
try:
    doc = fitz.open(pdf_path)
    pdf_text = ''.join([page.get_text() for page in doc])
    for keyword in keywords:
        if re.search(keyword, pdf_text, re.IGNORECASE):
            snippet_matches = re.finditer(f'(.{{0,50}}{keyword}.{{0,50}})', pdf_text, re.IGNORECASE | re.DOTALL)
            count = 0
            for snippet_match in snippet_matches:
                if count > 5: break # only first 5 matches per keyword
                snippet = snippet_match.group(1).replace('\n', ' ').strip()
                found.append(f"PDF File: ukem-or-2025-th.pdf | Keyword: {keyword}\nSnippet: {snippet}\n")
                count += 1
except Exception as e:
    found.append(f"PDF Error: {e}\n")

with open('search_tax.txt', 'w', encoding='utf-8') as out:
    if found:
        out.write("Found mentions:\n")
        for item in found:
            out.write(item + "\n")
    else:
        out.write("No mentions found.\n")
