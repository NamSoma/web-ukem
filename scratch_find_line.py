import os

file_path = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\อาชีวอนามัยและความปลอดภัย.html"
out_path = r"f:\Back up อีก HDD\งาน\ลองทำ\scratch_out.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(out_path, 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if "การสื่อสาร" in line:
            out.write(f"Line {i+1}: {line}")
