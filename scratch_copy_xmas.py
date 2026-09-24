import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\กิจกรรมเลี้ยงฉลองเทศกาลคริสต์มาสและวันขึ้นปีใหม่.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปกิจกรรม\xmas_newyear.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
else:
    pass
