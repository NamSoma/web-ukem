import os

# 1. Update Navbar.js
nav_path = r'f:\Back up อีก HDD\งาน\ลองทำ\components\Navbar.js'
with open(nav_path, 'r', encoding='utf-8') as f:
    nav_c = f.read()

nav_c = nav_c.replace('href="${prefix}เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"', 'href="${prefix}นโยบายและเอกสารดาวน์โหลด.html"')
nav_c = nav_c.replace('href="${prefix}en/เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"', 'href="${prefix}en/นโยบายและเอกสารดาวน์โหลด.html"')

with open(nav_path, 'w', encoding='utf-8') as f:
    f.write(nav_c)

# 2. Update the HTML file back
page_path = r'f:\Back up อีก HDD\งาน\ลองทำ\นโยบายและเอกสารดาวน์โหลด.html'
try:
    with open(page_path, 'r', encoding='utf-8') as f:
        page_c = f.read()

    page_c = page_c.replace('href="../css/global.css"', 'href="css/global.css"')
    page_c = page_c.replace('src="../components/', 'src="components/')
    page_c = page_c.replace('href="../components/', 'href="components/')
    page_c = page_c.replace('href="../assets/', 'href="assets/')
    page_c = page_c.replace('image-url="../assets/', 'image-url="assets/')
    page_c = page_c.replace('depth="1"', 'depth="0"')
    page_c = page_c.replace('path="เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"', 'path="นโยบายและเอกสารดาวน์โหลด.html"')
    page_c = page_c.replace('href="../ukem-or-2025-th.pdf"', 'href="ukem-or-2025-th.pdf"')

    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(page_c)
except Exception as e:
    print("Could not read HTML file:", e)
