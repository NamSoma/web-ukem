import os
import re

directory = r"f:\Back up อีก HDD\งาน\ลองทำ"

for root, _, files in os.walk(directory):
    if "scratch" in root or ".gemini" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith('.html') and file not in ['ศูนย์รวมการดาวน์โหลด.html', 'en\\ศูนย์รวมการดาวน์โหลด.html', 'index.html']:
            filepath = os.path.join(root, file)
            content = None
            encoding_used = 'utf-8'
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, 'r', encoding='utf-16') as f:
                        content = f.read()
                        encoding_used = 'utf-16'
                except Exception:
                    pass
            
            if content:
                # Remove <doc-section>...</doc-section> entirely
                new_content = re.sub(r'<doc-section[^>]*>.*?</doc-section>', '', content, flags=re.DOTALL)
                
                # In some files, there might be stray <doc-card> without <doc-section>
                new_content = re.sub(r'<doc-card[^>]*>.*?</doc-card>', '', new_content, flags=re.DOTALL)
                
                # In Corporate Governance page, there's a title "ดาวน์โหลดเอกสาร"
                new_content = re.sub(r'<h3[^>]*>ดาวน์โหลดเอกสาร</h3>', '', new_content, flags=re.IGNORECASE)
                new_content = re.sub(r'<h3[^>]*>Document Download</h3>', '', new_content, flags=re.IGNORECASE)
                
                if new_content != content:
                    try:
                        with open(filepath, 'w', encoding=encoding_used) as f:
                            f.write(new_content)
                        print("Cleaned up: " + file)
                    except Exception as e:
                        print("Write Error: " + str(e))
