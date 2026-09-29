import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')

file_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
if not os.path.exists(file_path):
    # Try current dir
    file_path = r'Link FTSE_Master_Checklist-9.24.xlsx'
    
if not os.path.exists(file_path):
    print("Could not find Excel file.")
    exit(1)

df = pd.read_excel(file_path, sheet_name='Checklist 322')

keywords = ['software', 'copyright', 'cyber', 'it', 'information technology', 'intellectual property', 'ทรัพย์สินทางปัญญา', 'ซอฟต์แวร์', 'ลิขสิทธิ์', 'security', 'piracy']

results = []
for index, row in df.iterrows():
    row_str = str(row.values).lower()
    for kw in keywords:
        if kw in row_str:
            indicator = row.get('Indicator Name', '')
            theme = row.get('FTSE Themes', '')
            desc = row.get('Description', '')
            results.append(f"Row {index+2}: [{theme}] {indicator} - {desc}")
            break

for r in results:
    print(r)
