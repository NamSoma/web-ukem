import os
import shutil

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if 'นโยบายการกำกับดูแลกิจการ.html' in filename:
            filepath = os.path.join(dirpath, filename)
            if 'en\\' not in filepath: # skip english for now
                with open(filepath, 'r', encoding='utf-8') as f_in:
                    with open('temp_gov.txt', 'w', encoding='utf-8') as f_out:
                        f_out.write(filepath + '\n')
                        f_out.write(f_in.read())
