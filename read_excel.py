import pandas as pd
import sys

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'

with open('excel_output.txt', 'w', encoding='utf-8') as f:
    try:
        xl = pd.ExcelFile(excel_path)
        f.write(f"Sheets: {xl.sheet_names}\n")
        for sheet in xl.sheet_names:
            df = pd.read_excel(excel_path, sheet_name=sheet)
            f.write(f"\n--- Sheet: {sheet} ---\n")
            f.write(f"Columns: {list(df.columns)}\n")
            # Write all rows to see the checklist
            for i, row in df.iterrows():
                f.write(f"Row {i}: {row.to_dict()}\n")
    except Exception as e:
        f.write(f"Error: {e}\n")
