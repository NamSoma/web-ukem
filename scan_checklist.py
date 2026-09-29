import pandas as pd
import os
import re
import fitz

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
website_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
pdf_path = r'f:\Back up อีก HDD\งาน\ลองทำ\ukem-or-2025-th.pdf'

# Load checklist
df = pd.read_excel(excel_path, sheet_name='Checklis 322')
checklist_items = df['Indicator / Checklist ภาษาไทย'].dropna().tolist()

# Load PDF text
pdf_text = ''
try:
    doc = fitz.open(pdf_path)
    pdf_text = ''.join([page.get_text() for page in doc])
except Exception as e:
    print(f"Error loading PDF: {e}")

# Load all website HTML text
website_text = ''
html_files = []
for dirpath, _, filenames in os.walk(website_dir):
    for f in filenames:
        if f.endswith('.html'):
            path = os.path.join(dirpath, f)
            html_files.append(path)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    website_text += ' ' + file.read()
            except:
                pass

results = []

for item in checklist_items:
    # simplify the search string: remove special chars, keep only words
    search_term = str(item).strip()
    if not search_term or search_term.lower() == 'nan': continue
    
    # Check website
    in_website = search_term in website_text
    
    # Check PDF
    in_pdf = search_term in pdf_text
    
    results.append({
        'Checklist Item': search_term,
        'Found in Website': in_website,
        'Found in PDF': in_pdf
    })

res_df = pd.DataFrame(results)

# Let's count totals
total = len(res_df)
found_anywhere = len(res_df[(res_df['Found in Website'] == True) | (res_df['Found in PDF'] == True)])

print(f"Total Items: {total}")
print(f"Found exactly as written: {found_anywhere}")

# Let's try more flexible search for those not found, since exact match might fail due to spaces/newlines
missing_items = res_df[(res_df['Found in Website'] == False) & (res_df['Found in PDF'] == False)]['Checklist Item'].tolist()

with open('missing_items.txt', 'w', encoding='utf-8') as f:
    for m in missing_items:
        f.write(f"{m}\n")
        
with open('found_items.txt', 'w', encoding='utf-8') as f:
    found_items = res_df[(res_df['Found in Website'] == True) | (res_df['Found in PDF'] == True)]
    for _, row in found_items.iterrows():
        f.write(f"{row['Checklist Item']} (Web: {row['Found in Website']}, PDF: {row['Found in PDF']})\n")

