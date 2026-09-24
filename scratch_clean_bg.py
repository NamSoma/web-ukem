import os
import re
import glob

def update_all_html_files():
    html_files = glob.glob('**/*.html', recursive=True)
    count = 0
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(
                r'(<section[^>]+style="[^"]*?background-color:\s*)var\(--bg-light\)([^"]*?")',
                r'\1transparent\2',
                content
            )
            new_content = re.sub(
                r'(<section[^>]+style="[^"]*?background-color:\s*)var\(--white\)([^"]*?")',
                r'\1transparent\2',
                new_content
            )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
        except Exception as e:
            pass
            
    print(count)

if __name__ == "__main__":
    update_all_html_files()
