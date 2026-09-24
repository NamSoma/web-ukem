import os
import shutil

src = r"C:\Users\UNIONIT\Downloads\อบรมการประหยัดพลังงานให้กับพนักงาน.jpg"
dst = r"f:\Back up อีก HDD\งาน\ลองทำ\assets\รูปกิจกรรม\energy_saving_training.jpg"

if os.path.exists(src):
    shutil.copy(src, dst)
else:
    pass
