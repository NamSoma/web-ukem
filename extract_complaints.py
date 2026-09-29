import re
content = open(r'สังคม\สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html', 'r', encoding='utf-8').read()
matches = re.finditer(r'.{0,80}ร้องเรียน.{0,80}', content)
with open('temp_complaints.txt', 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(m.group(0).replace('\n', ' ').strip() + '\n')
