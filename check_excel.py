import pandas as pd
import sys
import io

# Fix encoding issue for Windows console (to print Thai characters properly)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = r'C:\Users\UNIONIT\Downloads\FTSE Update 22.7.26.xlsx'

try:
    xl = pd.ExcelFile(file_path)
    print("=== Sheet Names ===")
    print(xl.sheet_names)
    
    for sheet in xl.sheet_names[:3]:
        print(f"\n=== Sheet: {sheet} (First 10 rows) ===")
        df = pd.read_excel(file_path, sheet_name=sheet, nrows=10)
        print(df.to_string())
except Exception as e:
    print(f"Error: {e}")
