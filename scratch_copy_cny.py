import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\กิจกรรมเฉลิมฉลองเทศกาลตรุษจีน.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปสังคม\cny_activity.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("Copy successful")
else:
    print("Source file not found")
