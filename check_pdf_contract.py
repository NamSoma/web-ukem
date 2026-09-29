import fitz, re

doc=fitz.open(r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf')
text=''.join([page.get_text() for page in doc])

with open('search_contract_pdf.txt', 'w', encoding='utf-8') as f:
    f.write('Found สัญญาจ้าง\n' if re.search('สัญญาจ้าง', text) else 'Not found สัญญาจ้าง\n')
    f.write('Found ชั่วคราว\n' if re.search('ชั่วคราว', text) else 'Not found ชั่วคราว\n')
