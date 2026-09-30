import os, re, urllib.parse

workspace = r'f:\Back up อีก HDD\งาน\ลองทำ'
missing_files = set()
all_html_files = []

for root, dirs, files in os.walk(workspace):
    # skip .git or node_modules or old backup folders if needed
    if 'ลองทำ\ลองทำ' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            all_html_files.append(os.path.join(root, file))

link_pattern = re.compile(r'(?:href|url)=[\"\']([^\"\']+\.pdf)[\"\']', re.IGNORECASE)

for html_file in all_html_files:
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = link_pattern.findall(content)
    for match in matches:
        if match.startswith('http'):
            continue
            
        html_dir = os.path.dirname(html_file)
        decoded_path = urllib.parse.unquote(match)
        decoded_path = decoded_path.replace('/', os.sep)
        
        target_path = os.path.normpath(os.path.join(html_dir, decoded_path))
        
        if not os.path.exists(target_path):
            missing_files.add(target_path)

if missing_files:
    print('Missing files:')
    with open('missing_pdfs.txt', 'w', encoding='utf-8') as f:
        for missing in sorted(missing_files):
            
            f.write(missing + '\n')
else:
    print('No missing PDF files found!')
