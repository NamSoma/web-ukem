import os
import shutil

file_path = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\อาชีวอนามัยและความปลอดภัย.html"
out_path = r"f:\Back up อีก HDD\งาน\ลองทำ\scratch_out.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
