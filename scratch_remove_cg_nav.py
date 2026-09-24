import os

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
nav_file = os.path.join(base_dir, "components", "Navbar.js")

if os.path.exists(nav_file):
    with open(nav_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if "โครงสร้างการกำกับดูแลกิจการ" in line:
            continue
        if "Governance Structure" in line:
            continue
        new_lines.append(line)
        
    with open(nav_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# Also delete the old html files to keep it clean
th_file = os.path.join(base_dir, "การกำกับดูแลและเศรษฐกิจ", "โครงสร้างการกำกับดูแลกิจการ.html")
en_file = os.path.join(base_dir, "en", "การกำกับดูแลและเศรษฐกิจ", "โครงสร้างการกำกับดูแลกิจการ.html")

if os.path.exists(th_file):
    os.remove(th_file)
if os.path.exists(en_file):
    os.remove(en_file)

print("Done removing from nav and deleting old files")
