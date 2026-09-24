import fitz  # PyMuPDF

pdf_path = r"C:\Users\UNIONIT\.gemini\antigravity-ide\brain\8477bb63-df3b-49d6-9df9-b0b0d4626097\.tempmediaStorage\media_1790129143688.pdf"

try:
    doc = fitz.open(pdf_path)
    # Extract first 15 pages which usually contains the Table of Contents
    with open('scratch_pdf_toc.txt', 'w', encoding='utf-8') as f:
        for i in range(min(15, len(doc))):
            f.write(f"--- Page {i+1} ---\n")
            f.write(doc[i].get_text())
            f.write("\n\n")
except Exception as e:
    with open('scratch_pdf_toc.txt', 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
