import fitz, re

doc=fitz.open(r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf')
text=''.join([page.get_text() for page in doc])

with open('check_hrdd_pdf.txt', 'w', encoding='utf-8') as f:
    if re.search('due diligence', text, re.IGNORECASE):
        f.write('Found Due Diligence in PDF\n')
    else:
        f.write('Not found Due Diligence in PDF\n')
