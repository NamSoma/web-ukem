import os

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
