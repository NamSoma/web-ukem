import sys; sys.stdout.reconfigure(encoding='utf-8')
import os

files = ['รางวัลและความสำเร็จ.html', 'en/รางวัลและความสำเร็จ.html']
for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '[data-theme="dark"] .award-card' not in content:
            new_content = content.replace('</style>', '    [data-theme="dark"] .award-card {\n        border: 1px solid rgba(255, 255, 255, 0.15);\n    }\n</style>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Successfully updated {file_path}')
        else:
            print(f'Already updated {file_path}')
    except Exception as e:
        print(f'Error: {e}')
