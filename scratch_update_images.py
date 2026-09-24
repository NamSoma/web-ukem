import os
import shutil

# Paths
downloads_dir = r"C:\Users\UNIONIT\Downloads"
assets_dir = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปสังคม"

lunch_src = os.path.join(downloads_dir, "กิจกรรมเลี้ยงข้าวกลางวันพนักงานที่ทำงานวันเสาร์.jpg")
crab_src = os.path.join(downloads_dir, "กิจกรรมปล่อยปู.jpg")

lunch_dst = os.path.join(assets_dir, "saturday_lunch.jpg")
crab_dst = os.path.join(assets_dir, "crab_release.jpg")

# Copy files
if os.path.exists(lunch_src):
    shutil.copy(lunch_src, lunch_dst)
    print("Copied lunch image successfully.")
else:
    print(f"File not found: {lunch_src}")

if os.path.exists(crab_src):
    shutil.copy(crab_src, crab_dst)
    print("Copied crab image successfully.")
else:
    print(f"File not found: {crab_src}")

# Update HTML files
html_files = [
    r"f:\Back up อีก HDD\งาน\ลองทำ\ข่าวสารและกิจกรรม.html",
    r"f:\Back up อีก HDD\งาน\ลองทำ\en\ข่าวสารและกิจกรรม.html",
    r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\การมีส่วนร่วมและพัฒนาชุมชน.html",
    r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html"
]

for file_path in html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace .png with .jpg
        updated = content.replace("saturday_lunch.png", "saturday_lunch.jpg")
        updated = updated.replace("crab_release.png", "crab_release.jpg")
        
        if updated != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Updated paths in {file_path}")
    else:
        print(f"HTML file not found: {file_path}")
