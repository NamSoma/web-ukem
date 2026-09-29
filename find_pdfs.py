import os
root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
pdfs = []
for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith('.pdf'):
            pdfs.append(os.path.join(dirpath, f))

with open('all_pdfs.txt', 'w', encoding='utf-8') as out:
    for p in pdfs:
        out.write(p + '\n')
