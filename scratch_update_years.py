import os

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"

# Update Thai file
th_file = os.path.join(base_dir, "ข่าวสารและกิจกรรม.html")
if os.path.exists(th_file):
    with open(th_file, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = content.replace("ปี 2568", "ปี 2569")
    if updated != content:
        with open(th_file, 'w', encoding='utf-8') as f:
            f.write(updated)

# Update English file
en_file = os.path.join(base_dir, "en", "ข่าวสารและกิจกรรม.html")
if os.path.exists(en_file):
    with open(en_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace 2025 with 2026, but careful not to replace anything else
    # We can replace 'color: #888;">2025</div>' to be safe
    updated = content.replace('color: #888;">2025</div>', 'color: #888;">2026</div>')
    if updated != content:
        with open(en_file, 'w', encoding='utf-8') as f:
            f.write(updated)
