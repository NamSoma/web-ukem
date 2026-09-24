import os

# 1. Update Thai News
file_th = r"f:\Back up อีก HDD\งาน\ลองทำ\ข่าวสารและกิจกรรม.html"
with open(file_th, 'r', encoding='utf-8') as f:
    html_th = f.read()

old_title_th = "โครงการปล่อยปูม้าคืนสู่ธรรมชาติ และฟื้นฟูระบบนิเวศชายฝั่ง"
new_title_th = "โครงการปล่อยปูม้าคืนสู่ธรรมชาติ"
html_th = html_th.replace(old_title_th, new_title_th)

with open(file_th, 'w', encoding='utf-8') as f:
    f.write(html_th)

# 2. Update Thai CSR Page
file_csr = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\การมีส่วนร่วมและพัฒนาชุมชน.html"
with open(file_csr, 'r', encoding='utf-8') as f:
    html_csr = f.read()

html_csr = html_csr.replace(old_title_th, new_title_th)

with open(file_csr, 'w', encoding='utf-8') as f:
    f.write(html_csr)

# 3. Update English News
file_en = r"f:\Back up อีก HDD\งาน\ลองทำ\en\ข่าวสารและกิจกรรม.html"
with open(file_en, 'r', encoding='utf-8') as f:
    html_en = f.read()

old_title_en = "Blue Swimming Crab Release and Coastal Ecosystem Restoration Project"
new_title_en = "Blue Swimming Crab Release to Nature Project"
html_en = html_en.replace(old_title_en, new_title_en)

with open(file_en, 'w', encoding='utf-8') as f:
    f.write(html_en)

print("Updated text successfully.")
