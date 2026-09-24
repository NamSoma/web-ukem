import re

def update_bg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace background-color: var(--white); with background-color: transparent;
    # in any <section ...> tag
    new_content = re.sub(
        r'(<section[^>]+style="[^"]*?background-color:\s*)var\(--white\)([^"]*?")',
        r'\1transparent\2',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

update_bg('เกี่ยวกับ UKEM.html')
update_bg('en/About UKEM.html')
