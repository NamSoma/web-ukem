import os

# 1. Update Thai News
file_th = r"f:\Back up อีก HDD\งาน\ลองทำ\ข่าวสารและกิจกรรม.html"
with open(file_th, 'r', encoding='utf-8') as f:
    html_th = f.read()

old_title_th = "ปล่อยปูม้าคืนสู่ธรรมชาติ ณ เกาะสีชัง"
new_title_th = "โครงการอนุรักษ์พันธุ์ปูและฟื้นฟูระบบนิเวศชายฝั่ง"
html_th = html_th.replace(old_title_th, new_title_th)

old_desc_th = "บริษัทฯ ได้จัดกิจกรรมเพื่อสังคม (CSR) นำโดยผู้บริหารและพนักงาน ร่วมกันปล่อยปูม้าคืนสู่ธรรมชาติ ณ ศูนย์เรียนรู้ธนาคารสัตว์ทะเลเกาะสีชังโดยชุมชน เพื่อเป็นการอนุรักษ์ ฟื้นฟู และเพิ่มปริมาณสัตว์น้ำในระบบนิเวศทางทะเล ตลอดจนเป็นการสร้างจิตสำนึกที่ดีให้พนักงานในการร่วมกันดูแลรักษาสิ่งแวดล้อมและทรัพยากรธรรมชาติให้มีความอุดมสมบูรณ์และยั่งยืนต่อไป"
new_desc_th = "ร่วมอนุบาลและปล่อยปูคืนสู่ธรรมชาติ เพื่อส่งเสริมการฟื้นฟูทรัพยากรทางทะเล"
html_th = html_th.replace(old_desc_th, new_desc_th)

with open(file_th, 'w', encoding='utf-8') as f:
    f.write(html_th)


# 2. Update Thai CSR Page
file_csr = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\การมีส่วนร่วมและพัฒนาชุมชน.html"
with open(file_csr, 'r', encoding='utf-8') as f:
    html_csr = f.read()

# Try to find and replace the title/desc in the CSR page as well
html_csr = html_csr.replace("โครงการอนุรักษ์และปล่อยปูม้าคืนสู่ธรรมชาติ", new_title_th) # Might have a different title there
html_csr = html_csr.replace("กิจกรรมปล่อยปูม้าคืนสู่ธรรมชาติ ณ ศูนย์เรียนรู้ธนาคารสัตว์ทะเลเกาะสีชังโดยชุมชน", new_desc_th) # Might have a different desc there
# Also try replacing the original ones in case they match
html_csr = html_csr.replace(old_title_th, new_title_th)
html_csr = html_csr.replace(old_desc_th, new_desc_th)

with open(file_csr, 'w', encoding='utf-8') as f:
    f.write(html_csr)


# 3. Update English News
file_en = r"f:\Back up อีก HDD\งาน\ลองทำ\en\ข่าวสารและกิจกรรม.html"
with open(file_en, 'r', encoding='utf-8') as f:
    html_en = f.read()

old_title_en = "Blue Swimming Crab Release at Koh Sichang"
new_title_en = "Crab Conservation and Coastal Ecosystem Restoration Project"
html_en = html_en.replace(old_title_en, new_title_en)

old_desc_en = "The company organized a CSR activity led by executives and employees to release blue swimming crabs back into the wild at the Koh Sichang Marine Animal Bank Learning Center. This initiative aims to conserve, restore, and increase marine life in the ecosystem, while fostering environmental awareness among employees for sustainable resource management."
new_desc_en = "Join in nursing and releasing crabs back to nature to promote the restoration of marine resources."
html_en = html_en.replace(old_desc_en, new_desc_en)

with open(file_en, 'w', encoding='utf-8') as f:
    f.write(html_en)

print("Updated text successfully.")
