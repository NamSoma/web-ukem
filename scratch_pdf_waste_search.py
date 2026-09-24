import fitz  # PyMuPDF

pdf_path = r"C:\Users\UNIONIT\.gemini\antigravity-ide\brain\8477bb63-df3b-49d6-9df9-b0b0d4626097\.tempmediaStorage\media_1790129143688.pdf"
out_path = "scratch_pdf_waste_search.txt"

try:
    doc = fitz.open(pdf_path)
    waste_keywords = ['ของเสีย', 'ขยะ', 'ฝังกลบ', 'รีไซเคิล']
    
    with open(out_path, 'w', encoding='utf-8') as f:
        found = False
        for i in range(len(doc)):
            text = doc[i].get_text()
            if any(kw in text for kw in waste_keywords) and ('2566' in text or '2567' in text or '2568' in text):
                lines = text.split('\n')
                # Just find if there's a table structure for waste
                for line in lines:
                    if any(kw in line for kw in waste_keywords):
                        f.write(f"Page {i+1}: {line.strip()}\n")
                found = True
        
        if not found:
            f.write("No waste stats found with years.\n")
            
except Exception as e:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
