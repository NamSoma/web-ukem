import fitz  # PyMuPDF

pdf_path = r"C:\Users\UNIONIT\.gemini\antigravity-ide\brain\8477bb63-df3b-49d6-9df9-b0b0d4626097\.tempmediaStorage\media_1790129143688.pdf"

try:
    doc = fitz.open(pdf_path)
    # Page 56 in PDF (index 55)
    page = doc[55]
    text = page.get_text()
    
    with open('scratch_page56.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        
except Exception as e:
    with open('scratch_page56.txt', 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
