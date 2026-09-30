import os

# 1. Update Navbar.js
nav_path = r'f:\Back up อีก HDD\งาน\ลองทำ\components\Navbar.js'
with open(nav_path, 'r', encoding='utf-8') as f:
    nav_c = f.read()

nav_c = nav_c.replace('href="${prefix}นโยบายและเอกสารดาวน์โหลด.html"', 'href="${prefix}เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"')
nav_c = nav_c.replace('href="${prefix}en/นโยบายและเอกสารดาวน์โหลด.html"', 'href="${prefix}en/เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"')

with open(nav_path, 'w', encoding='utf-8') as f:
    f.write(nav_c)

# 2. Update the moved HTML file
page_path = r'f:\Back up อีก HDD\งาน\ลองทำ\เอกสารและนโยบาย\นโยบายและเอกสารดาวน์โหลด.html'
with open(page_path, 'r', encoding='utf-8') as f:
    page_c = f.read()

page_c = page_c.replace('href="css/global.css"', 'href="../css/global.css"')
page_c = page_c.replace('src="components/', 'src="../components/')
page_c = page_c.replace('href="components/', 'href="../components/')
page_c = page_c.replace('href="assets/', 'href="../assets/')
page_c = page_c.replace('image-url="assets/', 'image-url="../assets/')
page_c = page_c.replace('depth="0"', 'depth="1"')
page_c = page_c.replace('path="นโยบายและเอกสารดาวน์โหลด.html"', 'path="เอกสารและนโยบาย/นโยบายและเอกสารดาวน์โหลด.html"')
page_c = page_c.replace('href="ukem-or-2025-th.pdf"', 'href="../ukem-or-2025-th.pdf"')
page_c = page_c.replace('href="assets/เอกสารกำกับดูแล/', 'href="../assets/เอกสารกำกับดูแล/')
page_c = page_c.replace('href="assets/เอกสารดาวน์โหลด/', 'href="../assets/เอกสารดาวน์โหลด/')
page_c = page_c.replace('href="assets/เอกสารภาพรวมความยั่งยืน/', 'href="../assets/เอกสารภาพรวมความยั่งยืน/')

with open(page_path, 'w', encoding='utf-8') as f:
    f.write(page_c)
