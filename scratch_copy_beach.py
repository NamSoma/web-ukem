import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\กิจกรรมเก็บขยะชายหาดจอมเทียน.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปกิจกรรม\beach_cleanup.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
else:
    pass
