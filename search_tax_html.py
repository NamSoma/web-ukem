import os
import re

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['ภาษีเงินได้นิติบุคคล', 'ภาษีเงินได้ที่จ่าย', 'ค่าใช้จ่ายภาษีเงินได้', 'ภาษี']

found = False
with open('search_tax_web.txt', 'w', encoding='utf-8') as out:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for k in keywords:
                            if re.search(k, content):
                                snippet = re.search(f'(.{{0,30}}{k}.{{0,30}})', content).group(1).replace('\n', '')
                                out.write(f"Found {k} in {filename}: {snippet}\n")
                                found = True
                except Exception as e:
                    pass
    if not found:
        out.write("No tax mentions in HTML\n")
