import fitz
import re

doc = fitz.open(r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf')
keywords = ['reskill', 'upskill', 'แผนพัฒนาทักษะ', 'ฝึกอบรม', 'พัฒนาบุคลากร', 'ชั่วโมงการฝึกอบรม', 'พัฒนาทักษะ']

results = []
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    for kw in keywords:
        if re.search(kw, text, re.IGNORECASE):
            # Extract surrounding context
            matches = re.finditer(f'(.{{0,100}}{kw}.{{0,100}})', text, re.IGNORECASE | re.DOTALL)
            for m in matches:
                snippet = m.group(1).replace('\n', ' ')
                results.append(f"Page {page_num + 1} ({kw}): {snippet}")

with open(r'f:\Back up อีก HDD\งาน\ลองทำ\search_pdf_skills.txt', 'w', encoding='utf-8') as f:
    for r in set(results): # Use set to deduplicate a bit
        f.write(r + '\n')
