import sys; sys.stdout.reconfigure(encoding='utf-8')
import re

files = ['ภาพรวมความยั่งยืน/ห่วงโซ่คุณค่าของธุรกิจ.html', 'en/ภาพรวมความยั่งยืน/ห่วงโซ่คุณค่าของธุรกิจ.html']

pattern = re.compile(
    r'<div class="vc-card">\s*<div class="vc-card-header">\s*<h4>(.*?)</h4>\s*</div>\s*<div class="vc-card-body">\s*<ul>(.*?)</ul>\s*</div>\s*</div>',
    re.DOTALL
)

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add script tag before </body> if not present
        if 'ValueChainCard.js' not in content:
            content = content.replace('</body>', '    <script src="../components/ValueChainCard.js"></script>\n</body>')

        # Replace cards
        def repl(match):
            title = match.group(1).strip()
            body = match.group(2).strip()
            return f'<value-chain-card title="{title}">\n{body}\n</value-chain-card>'
            
        new_content = pattern.sub(repl, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Successfully updated {file_path}')
        else:
            print(f'No changes made to {file_path}')
            
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
