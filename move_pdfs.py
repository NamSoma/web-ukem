import os
import shutil
from pathlib import Path

workspace = Path(r"f:\Back up อีก HDD\งาน\ลองทำ")
new_dir = workspace / "การกำกับดูแลและเศรษฐกิจ" / "เอกสารPDF"

def get_relative_path(html_path, target_path):
    html_dir = html_path.parent
    try:
        rel_path = os.path.relpath(target_path, html_dir)
        return rel_path.replace('\\', '/')
    except ValueError:
        return None

count = 0
for root, dirs, files in os.walk(workspace):
    dirs[:] = [d for d in dirs if d not in ['.agent', 'scratch', 'node_modules', 'ลองทำ']]
    for file in files:
        if file.endswith('.html'):
            html_path = Path(root) / file
            try:
                with open(html_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
                
            orig = content
            
            import re
            pattern = re.compile(r'href="([^"]*assets/เอกสารกำกับดูแล/([^"]+))"')
            
            def repl(match):
                filename = match.group(2)
                target_file = new_dir / filename
                new_href = get_relative_path(html_path, target_file)
                return f'href="{new_href}"'
            
            new_content = pattern.sub(repl, content)
            
            if new_content != orig:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
