import fitz  # PyMuPDF
import re

pdf_path = r"C:\Users\UNIONIT\.gemini\antigravity-ide\brain\8477bb63-df3b-49d6-9df9-b0b0d4626097\.tempmediaStorage\media_1790129143688.pdf"

try:
    doc = fitz.open(pdf_path)
    results = []
    
    keywords = ['ลาออก', 'เลิกจ้าง', 'หมุนเวียนพนักงาน', 'turnover', 'turn over', 'อัตราการ', 'พนักงาน']
    
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        
        lines = text.split('\n')
        for line_num, line in enumerate(lines):
            if any(kw in line.lower() for kw in keywords):
                if 'ลาออก' in line or 'เลิกจ้าง' in line or 'turnover' in line.lower():
                    results.append(f"Page {i+1}: {line.strip()}")
    
    with open('scratch_pdf_search_results.txt', 'w', encoding='utf-8') as f:
        if not results:
            f.write("No direct matches for turnover/resignation found.\nShowing occurrences of 'พนักงาน' (first 10):\n")
            emp_count = 0
            for i in range(len(doc)):
                text = doc[i].get_text()
                lines = text.split('\n')
                for line in lines:
                    if 'พนักงาน' in line:
                        if emp_count < 10:
                            f.write(f"Page {i+1}: {line.strip()}\n")
                        emp_count += 1
        else:
            f.write("Matches found:\n")
            for r in results:
                f.write(r + "\n")
except Exception as e:
    with open('scratch_pdf_search_results.txt', 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
