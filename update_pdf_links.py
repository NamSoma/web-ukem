import os

replacements = {
    "https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-1-แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ-26-2-68.pdf": "assets/เอกสารกำกับดูแล/แนวทางปฎิบัติ.pdf",
    "https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-2-กฎบัตรคณะกรรมการตรวจสอบ-14-11-67.pdf": "assets/เอกสารกำกับดูแล/กฎบัตรและแนวทางปฎิบัติคณะกรรมการตรวจสอบ.pdf",
    "https://www.unionpetrochemical.com/wp-content/uploads/2022/06/2.-จรรยาบรรณธุรกิจ.pdf": "assets/เอกสารกำกับดูแล/จรรยาบรรณธุรกิจ.pdf"
}

root = r"f:\Back up อีก HDD\งาน\ลองทำ"

for dirpath, _, files in os.walk(root):
    if '.git' in dirpath or 'node_modules' in dirpath:
        continue
        
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(dirpath, f)
            rel_path = os.path.relpath(filepath, root)
            depth = len(rel_path.split(os.sep)) - 1
            prefix = "../" * depth
            
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                encoding_used = 'utf-8'
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='utf-16') as file:
                    content = file.read()
                encoding_used = 'utf-16'
                
            modified = False
            for old_url, new_base_url in replacements.items():
                if old_url in content:
                    new_url = prefix + new_base_url
                    content = content.replace(old_url, new_url)
                    modified = True
                    
            if modified:
                with open(filepath, 'w', encoding=encoding_used) as file:
                    file.write(content)
                pass
