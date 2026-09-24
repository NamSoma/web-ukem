import os

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
about_th = os.path.join(base_dir, "เกี่ยวกับ UKEM.html")
about_en = os.path.join(base_dir, "en", "About UKEM.html")

def remove_heading(file_path, title):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        target = f"""            <div class="text-center" style="margin-bottom: 50px;">
                <h2 class="section-title">{title}</h2>
                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 20px;"></div>
            </div>"""
        
        content = content.replace(target, "")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

remove_heading(about_th, "โครงสร้างการกำกับดูแลกิจการ")
remove_heading(about_en, "Corporate Governance Structure")

print("Headings removed")
