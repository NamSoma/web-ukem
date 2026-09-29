import fitz
import re
import os

pdf_path = r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf'
keywords = ['ภาษีเงินได้', 'ภาษีเงินได้นิติบุคคล']

found_pages = []

try:
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        for keyword in keywords:
            if re.search(keyword, text, re.IGNORECASE):
                found_pages.append(page_num + 1) # 1-indexed
                break # Move to next page if found
except Exception as e:
    print(f"Error: {e}")

with open('search_tax_pages.txt', 'w', encoding='utf-8') as f:
    f.write(f"Found on pages: {', '.join(map(str, found_pages))}\n")
