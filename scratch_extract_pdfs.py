import os
import re
import json

directory = r"f:\Back up อีก HDD\งาน\ลองทำ"
results = []

def extract_attributes(tag_string):
    attrs = {}
    matches = re.findall(r'(\w+)="([^"]*)"', tag_string)
    for k, v in matches:
        attrs[k] = v
    return attrs

for root, _, files in os.walk(directory):
    if "scratch" in root or ".gemini" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            content = None
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, 'r', encoding='utf-16') as f:
                        content = f.read()
                except Exception:
                    pass
            
            if content:
                # Find all doc-card and doc-download tags
                tags = re.findall(r'<doc-(?:card|download)[^>]*>', content)
                for tag in tags:
                    attrs = extract_attributes(tag)
                    
                    # Normalize title and url
                    title = attrs.get('title') or attrs.get('file-name')
                    url = attrs.get('url') or attrs.get('file-url')
                    
                    if title and url:
                        rel_path = os.path.relpath(filepath, directory)
                        # Use a clean dict
                        results.append({
                            'file': rel_path.replace('\\', '/'),
                            'title': title.strip(),
                            'url': url.strip()
                        })

# Ensure we print using utf-8 so powershell doesn't garble it
with open(os.path.join(directory, 'scratch_pdf_results.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Done")
