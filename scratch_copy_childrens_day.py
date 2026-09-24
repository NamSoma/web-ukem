import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\สนับสนุนกิจกรรมวันเด็กแห่งชาติ โรงเรียนวัดขุมทอง.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปสังคม\childrens_day.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("Copy successful")
else:
    print("Source file not found")
