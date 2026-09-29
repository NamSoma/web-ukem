import pandas as pd
import os

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
website_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
output_excel = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24_Updated.xlsx'

# Load checklist
df = pd.read_excel(excel_path, sheet_name='Checklis 322')

# Load all website HTML text
website_text = ''
for dirpath, _, filenames in os.walk(website_dir):
    for f in filenames:
        if f.endswith('.html'):
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    website_text += ' ' + file.read()
            except:
                pass

# Custom known mappings that we added manually but might not match perfectly
custom_matches = [
    "Reskill", "Upskill", "ประเมินผลอย่างเป็นธรรม", "Human Rights Due Diligence"
]

updated_count = 0

for i, row in df.iterrows():
    item = str(row['Indicator / Checklist ภาษาไทย']).strip()
    if not item or item.lower() == 'nan': continue
    
    found = False
    
    # 1. Exact match
    if item in website_text:
        found = True
        
    # 2. Check custom keywords if they are in the item name
    if not found:
        for keyword in custom_matches:
            if keyword.lower() in item.lower() and keyword in website_text:
                found = True
                break
                
    # Update Excel
    if found:
        if pd.isna(row['สถานะบนเว็ป']) or str(row['สถานะบนเว็ป']).strip() == '':
            df.at[i, 'สถานะบนเว็ป'] = 'ขึ้นแล้ว'
            updated_count += 1

# Export to a new Excel file
try:
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Checklis 322', index=False)
    print(f"Successfully updated {updated_count} items and saved to: {output_excel}")
except Exception as e:
    print(f"Failed to save Excel: {e}")
