import fitz, re

doc=fitz.open(r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf')
text=''.join([page.get_text() for page in doc])

with open('check_labor_pdf.txt', 'w', encoding='utf-8') as f:
    f.write('Found แรงงานสัมพันธ์\n' if re.search('แรงงานสัมพันธ์', text) else 'Not found แรงงานสัมพันธ์\n')
