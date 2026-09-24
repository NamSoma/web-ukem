import fitz  # PyMuPDF
import re

pdf_path = r"C:\Users\UNIONIT\.gemini\antigravity-ide\brain\8477bb63-df3b-49d6-9df9-b0b0d4626097\.tempmediaStorage\media_1790129143688.pdf"
out_path = "scratch_pdf_stats_search.txt"

try:
    doc = fitz.open(pdf_path)
    results = []
    
    # Keywords for waste and injuries
    waste_keywords = ['ของเสีย', 'ขยะ', 'รีไซเคิล']
    injury_keywords = ['บาดเจ็บ', 'อุบัติเหตุ', 'สูญเสียเวลา', 'ชั่วโมงการทำงาน']
    
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        lines = text.split('\n')
        
        for line_num, line in enumerate(lines):
            # Check if line contains keyword
            has_waste = any(kw in line for kw in waste_keywords)
            has_injury = any(kw in line for kw in injury_keywords)
            
            # If a keyword is found, and there is a year nearby (2565, 2566, 2567, 2568)
            # OR we just extract a chunk of text around the match to manually inspect
            if has_waste or has_injury:
                # Let's check if the page seems to contain a table with years
                if '2566' in text or '2567' in text or '2565' in text:
                    results.append(f"Page {i+1}: {line.strip()}")
                    
    # Since extracting just the line might miss the table context, 
    # let's just find the pages that contain BOTH the keyword AND the years "2566" and "2567"
    # and print out the whole page text for those specific pages.
    pages_to_extract = set()
    for i in range(len(doc)):
        text = doc[i].get_text()
        has_waste = any(kw in text for kw in waste_keywords)
        has_injury = any(kw in text for kw in injury_keywords)
        has_years = ('2566' in text and '2567' in text) or ('2565' in text and '2566' in text)
        
        if (has_waste or has_injury) and has_years:
            pages_to_extract.add(i)
            
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Found {len(pages_to_extract)} pages with keywords and years.\n")
        f.write(f"Pages: {[p+1 for p in pages_to_extract]}\n\n")
        
        for p in list(pages_to_extract)[:5]: # Limit to 5 pages to avoid huge output
            f.write(f"--- Page {p+1} ---\n")
            f.write(doc[p].get_text())
            f.write("\n\n")
            
except Exception as e:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
