import os
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

target_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"

def clean_style(match):
    style_content = match.group(1)
    
    # Remove background
    style_content = re.sub(r'background:\s*[^;]+;?\s*', '', style_content)
    # Remove border
    style_content = re.sub(r'border:\s*[^;]+;?\s*', '', style_content)
    # Remove border-left/right/top/bottom
    style_content = re.sub(r'border-[a-z]+:\s*[^;]+;?\s*', '', style_content)
    # Remove padding
    style_content = re.sub(r'padding:\s*[^;]+;?\s*', '', style_content)
    # Remove box-shadow
    style_content = re.sub(r'box-shadow:\s*[^;]+;?\s*', '', style_content)
    
    style_content = style_content.strip()
    
    if not style_content:
        return ''
    else:
        return f'style="{style_content}"'

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    def clean_tag(m):
        tag = m.group(0)
        # Remove activity-card class
        tag = re.sub(r'\bclass=["\']([^"\']*)activity-card([^"\']*)["\']', 
                     lambda cl: f'class="{cl.group(1).strip()} {cl.group(2).strip()}"'.strip().replace('class=""', '').replace('class=" "', ''), tag)
        
        # Clean up empty class attrs
        tag = re.sub(r'\s*class=""\s*', ' ', tag)
        tag = re.sub(r'\s*class=" "\s*', ' ', tag)
        
        # Clean up style
        tag = re.sub(r'style=["\']([^"\']*)["\']', clean_style, tag)
        
        # Clean up empty style attrs
        tag = re.sub(r'\s*style=""\s*', ' ', tag)
        
        # Collapse multiple spaces
        tag = re.sub(r'\s+>', '>', tag)
        
        return tag

    # Find all <div ... activity-card ... >
    pattern = re.compile(r'<div[^>]*activity-card[^>]*>', re.IGNORECASE)
    content = pattern.sub(clean_tag, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_files = 0
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if process_html_file(filepath):
                print(f"Modified: {filepath}")
                modified_files += 1

print(f"Total files modified: {modified_files}")
