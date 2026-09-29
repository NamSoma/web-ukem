import os
import re

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['Human Rights Due Diligence', 'Due Diligence', 'การตรวจสอบสิทธิมนุษยชนอย่างรอบด้าน', 'การประเมินความเสี่ยงด้านสิทธิมนุษยชน', 'HRDD']

found = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(('.html', '.txt', '.json', '.md')):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue

            for keyword in keywords:
                if re.search(keyword, content, re.IGNORECASE):
                    # extract a snippet
                    snippet_match = re.search(f'(.{{0,80}}{keyword}.{{0,80}})', content, re.IGNORECASE | re.DOTALL)
                    if snippet_match:
                        snippet = snippet_match.group(1).replace('\n', ' ').strip()
                        found.append(f"File: {os.path.relpath(filepath, root_dir)}\nKeyword: {keyword}\nSnippet: {snippet}\n")

with open('search_hrdd.txt', 'w', encoding='utf-8') as out:
    if found:
        out.write("Found mentions:\n")
        for item in found:
            out.write(item + "\n")
    else:
        out.write("No mentions found.\n")
