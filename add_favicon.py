import os
import re

root_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"

added_count = 0

for root, dirs, files in os.walk(root_dir):
    # skip .git or other system folders if any
    if '.git' in root or 'node_modules' in root or '.gemini' in root:
        continue

    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            # Calculate depth relative to root_dir
            rel_path = os.path.relpath(filepath, root_dir)
            parts = rel_path.split(os.sep)
            depth = len(parts) - 1
            
            prefix = '../' * depth
            icon_path = f"{prefix}components/union-logo.png"
            favicon_tag = f'    <link rel="icon" type="image/png" href="{icon_path}">'
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                encoding_used = 'utf-8'
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='utf-16') as f:
                    content = f.read()
                encoding_used = 'utf-16'
            
            # Check if it already has an icon
            if '<link rel="icon"' not in content:
                # Insert just before </head>
                # Using regex to find </head>
                match = re.search(r'</head>', content, re.IGNORECASE)
                if match:
                    # We want to replace </head> with \n<link...>\n</head>
                    new_content = content[:match.start()] + f"\n{favicon_tag}\n" + content[match.start():]
                    with open(filepath, 'w', encoding=encoding_used) as f:
                        f.write(new_content)
                    pass
                    added_count += 1
                else:
                    pass

print(f"Total files updated: {added_count}")
