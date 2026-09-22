import fitz
import os

pdf_path = r"f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf"
output_path = r"f:\Back up อีก HDD\งาน\ลองทำ\images\ukem-or-2025-page4.png"

doc = fitz.open(pdf_path)
page = doc.load_page(3) # 0-indexed, so 3 is page 4
pix = page.get_pixmap(dpi=150) # Use 150 dpi for decent quality
pix.save(output_path)
print("Saved page 4 to:", output_path)
doc.close()
