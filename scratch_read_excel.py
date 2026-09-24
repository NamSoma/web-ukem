import pandas as pd
import sys

excel_path = r"C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist_Update.xlsx"
out_path = "scratch_ftse_checklist.txt"

try:
    # Read all sheets
    xls = pd.ExcelFile(excel_path)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Sheets found: {xls.sheet_names}\n\n")
        
        for sheet in xls.sheet_names:
            f.write(f"--- Sheet: {sheet} ---\n")
            df = pd.read_excel(xls, sheet_name=sheet)
            # Just write the first 50 rows to avoid huge output, or write everything if small
            f.write(df.head(50).to_string())
            f.write("\n\n")
            
except Exception as e:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
