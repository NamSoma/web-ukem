import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')

file_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
df = pd.read_excel(file_path, sheet_name='Checklis 322')

keywords = ['software', 'copyright', 'cyber', 'intellectual property', 'ทรัพย์สินทางปัญญา', 'ซอฟต์แวร์', 'ลิขสิทธิ์', 'piracy']

results = []
for index, row in df.iterrows():
    row_str = str(row.values).lower()
    for kw in keywords:
        if kw in row_str:
            indicator = row.get('Indicator Name', '')
            theme = row.get('FTSE Themes', '')
            desc = row.get('Description', '')
            if pd.notna(indicator) or pd.notna(theme):
                results.append(f"Row {index+2}: [{theme}] {indicator} - {desc}")
            break

for r in results:
    print(r)
