import os
import re
import json

def find_thai(directory):
    results = []
    thai_pattern = re.compile(r'[\u0E00-\u0E7F]')
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if thai_pattern.search(line):
                                results.append({
                                    'file': file_path,
                                    'lineNum': i + 1,
                                    'line': line.strip()
                                })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    
    return results

res = find_thai('en')
with open('thai_results.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
