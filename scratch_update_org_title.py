import re

def update_org_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_title_css = r'\.org-title\s*\{\s*background:[^}]*border-radius:\s*50px;[^}]*\}'
        
        new_title_css = """.org-title {
                    background: linear-gradient(135deg, #0070c0, #005a9e);
                    color: #fff;
                    width: 260px;
                    min-height: 60px;
                    padding: 12px 15px;
                    border-radius: 8px;
                    font-size: 20px;
                    font-weight: 600;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    position: relative;
                    z-index: 2;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }"""
                
        new_content = re.sub(old_title_css, new_title_css, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        pass

update_org_title('เกี่ยวกับ UKEM.html')
update_org_title('en/About UKEM.html')
