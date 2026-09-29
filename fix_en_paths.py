import os
import re

root_dir = 'en'
for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    if os.path.isdir(subdir_path):
        for file in os.listdir(subdir_path):
            if file.endswith('.html'):
                filepath = os.path.join(subdir_path, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for ../assets/ instead of ../../assets/
                if '../assets/' in content and '../../assets/' not in content:
                    new_content = content.replace('../assets/', '../../assets/')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                elif '../assets/' in content:
                    new_content = content.replace('../../assets/', 'THISTEMPORARY')
                    new_content = new_content.replace('../assets/', '../../assets/')
                    new_content = new_content.replace('THISTEMPORARY', '../../assets/')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
