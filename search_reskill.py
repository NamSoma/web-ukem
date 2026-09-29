import os
import re

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
keywords = ['reskill', 'upskill', 'แผนพัฒนาทักษะ', 'พัฒนาทักษะ', 'reskilling', 'upskilling']

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
                    snippet_match = re.search(f'(.{{0,50}}{keyword}.{{0,50}})', content, re.IGNORECASE | re.DOTALL)
                    if snippet_match:
                        snippet = snippet_match.group(1).replace('\n', ' ').strip()
                        found.append(f"File: {os.path.relpath(filepath, root_dir)}\nKeyword: {keyword}\nSnippet: {snippet}\n")
                        break # Just one hit per file is enough for a quick check

with open('reskill_results.txt', 'w', encoding='utf-8') as out:
    if found:
        out.write("Found mentions:\n")
        for item in found:
            out.write(item + "\n")
    else:
        out.write("No mentions found.\n")
