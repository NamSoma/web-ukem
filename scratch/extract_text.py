import fitz
import json

doc = fitz.open(r"f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf")
output = {}
for i in range(2, 7):
    output[f"Page_{i+1}_(Index_{i})"] = doc.load_page(i).get_text()[:200]

with open(r"f:\Back up อีก HDD\งาน\ลองทำ\scratch\pdf_pages.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
