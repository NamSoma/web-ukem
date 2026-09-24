import os
import shutil

# Base paths
base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
old_img_dir = os.path.join(base_dir, "assets", "รูปสังคม")
new_img_dir = os.path.join(base_dir, "assets", "รูปกิจกรรม")

# Create new directory if not exists
os.makedirs(new_img_dir, exist_ok=True)
print(f"Created directory: {new_img_dir}")

# Images to move
images = [
    "crab_release.jpg",
    "saturday_lunch.jpg",
    "cny_activity.jpg",
    "luangtanoi.jpg",
    "childrens_day.jpg",
    "medicine_donation.jpg",
    "beach_cleanup.jpg"
]

# Move images
for img in images:
    src = os.path.join(old_img_dir, img)
    dst = os.path.join(new_img_dir, img)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {img}")
    else:
        print(f"Skipped {img} (not found in source)")

# Update HTML files
html_files = [
    os.path.join(base_dir, "ข่าวสารและกิจกรรม.html"),
    os.path.join(base_dir, "en", "ข่าวสารและกิจกรรม.html"),
    os.path.join(base_dir, "สังคม", "การมีส่วนร่วมและพัฒนาชุมชน.html"),
    os.path.join(base_dir, "สังคม", "สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html")
]

for file_path in html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the old path with the new path
        # In root files, path is assets/รูปสังคม/ or assets/รูปกิจกรรม/
        # In subfolder files, path might be ../assets/รูปสังคม/
        
        updated = content.replace("assets/รูปสังคม/crab_release", "assets/รูปกิจกรรม/crab_release")
        updated = updated.replace("assets/รูปสังคม/saturday_lunch", "assets/รูปกิจกรรม/saturday_lunch")
        updated = updated.replace("assets/รูปสังคม/cny_activity", "assets/รูปกิจกรรม/cny_activity")
        updated = updated.replace("assets/รูปสังคม/luangtanoi", "assets/รูปกิจกรรม/luangtanoi")
        updated = updated.replace("assets/รูปสังคม/childrens_day", "assets/รูปกิจกรรม/childrens_day")
        updated = updated.replace("assets/รูปสังคม/medicine_donation", "assets/รูปกิจกรรม/medicine_donation")
        updated = updated.replace("assets/รูปสังคม/beach_cleanup", "assets/รูปกิจกรรม/beach_cleanup")
        
        if updated != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            
        print(f"Updated paths in {os.path.basename(file_path)}")
