import os
import re

workspace = r'f:\Back up อีก HDD\งาน\ลองทำ'

url1 = re.compile(r'https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68\.pdf', re.IGNORECASE)
url1_encoded = re.compile(r'https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%97%E0%B8%B5%E0%B9%88-02-%E0%B8%99%E0%B9%82%E0%B8%A2%E0%B8%9A%E0%B8%B2%E0%B8%A2%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%95%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A3%E0%B8%B1%E0%B8%9B%E0%B8%8A%E0%B8%B1%E0%B8%99-26-2-68\.pdf', re.IGNORECASE)

url2 = re.compile(r'https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+1.-นโยบายกำกับดูแลกิจการที่ดี\.pdf', re.IGNORECASE)
url2_encoded = re.compile(r'https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+1.-%E0%B8%99%E0%B9%82%E0%B8%A2%E0%B8%9A%E0%B8%B2%E0%B8%A2%E0%B8%81%E0%B8%B3%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%94%E0%B8%B9%E0%B9%81%E0%B8%A5%E0%B8%81%E0%B8%B4%E0%B8%88%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%94%E0%B8%B5\.pdf', re.IGNORECASE)

count = 0

for root, dirs, files in os.walk(workspace):
    if any(x in root for x in ['.agent', 'scratch', 'node_modules', 'ลองทำ\\ลองทำ']):
        continue
        
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
                
            orig = content
            
            rel_dir = os.path.relpath(root, workspace)
            depth = 0 if rel_dir == '.' else len(rel_dir.split(os.sep))
            prefix = '../' * depth
            
            path1 = prefix + 'assets/เอกสารกำกับดูแล/ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68.pdf'
            path2 = prefix + 'assets/เอกสารกำกับดูแล/1.-นโยบายกำกับดูแลกิจการที่ดี.pdf'
            
            content = url1.sub(path1, content)
            content = url1_encoded.sub(path1, content)
            
            content = url2.sub(path2, content)
            content = url2_encoded.sub(path2, content)
            
            if content != orig:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Done replacing in {count} files.")
