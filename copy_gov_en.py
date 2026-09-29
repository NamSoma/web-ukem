import os

filepath = r'f:\Back up อีก HDD\งาน\ลองทำ\en\การกำกับดูแลและเศรษฐกิจ\นโยบายการกำกับดูแลกิจการ.html'
with open(filepath, 'r', encoding='utf-8') as f_in:
    with open('temp_gov_en.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(f_in.read())
