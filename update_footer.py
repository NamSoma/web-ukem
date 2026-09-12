import os, re
base_dir = r'f:\Back up อีก HDD\งาน\ลองทำ\en'
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(r'<main-footer[^>]*>', '<main-footer lang="en">', content)
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
print("done")
