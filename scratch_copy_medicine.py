import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\โครงการ “ส่งต่อยา ส่งต่อชีวิต”.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปกิจกรรม\medicine_donation.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
else:
    # try without quotes in filename in case it was a typo in user's prompt
    src2 = r"C:\Users\UNIONIT\Downloads\โครงการ ส่งต่อยา ส่งต่อชีวิต.jpg"
    if os.path.exists(src2):
        shutil.copy(src2, dst)
    else:
        pass
