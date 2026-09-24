import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\มอบเงินสนับสนุนมูลนิธิหลวงตาน้อย.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปสังคม\luangtanoi.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("Copy successful")
else:
    print("Source file not found")
