import pandas as pd
import json

# Manual overrides based on Gap Analysis
manual_reds = [
    'scope 3', 'tcfd', 'issb', 'net zero', 'sbti', 're100', 'cdp', 
    'tax', 'ภาษี', 'whistleblow', 'แจ้งเบาะแส', 'supplier code', 
    'due diligence', 'nps', 'ความผูกพันพนักงาน', 'water stress',
    'biodiversity', 'ความหลากหลายทางชีวภาพ'
]

manual_greens = [
    'การลดก๊าซเรือนกระจก', 'การประหยัดพลังงาน', 'การจัดการของเสีย',
    'การใช้น้ำ', 'ความปลอดภัย', 'ชุมชน', 'โครงสร้างคณะกรรมการ', 
    'การประเมินความเสี่ยง', 'ต่อต้านคอร์รัปชัน', 'ความขัดแย้งทางผลประโยชน์',
    'scope 1', 'scope 2', 'iso 14001', 'coso', 'กรรมการอิสระ', 
    'ความหลากหลาย', 'iso 9001', 'แรงงานเด็ก', 'บังคับ', 'pdpa'
]

def evaluate(indicator):
    ind = str(indicator).lower()
    for red in manual_reds:
        if red in ind:
            return False
    for green in manual_greens:
        if green in ind:
            return True
    return False

file_path = r'C:\Users\UNIONIT\Downloads\FTSE Update 22.7.26.xlsx'
out_path = r'C:\Users\UNIONIT\Downloads\FTSE_Update_Highlighted.xlsx'

try:
    print("Reading Excel...")
    xl = pd.ExcelFile(file_path)
    
    # We will use ExcelWriter with styling
    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    
    for sheet_name in xl.sheet_names[:3]:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        
        green_format = workbook.add_format({'bg_color': '#C6EFCE'})
        red_format = workbook.add_format({'bg_color': '#FFC7CE'})
        
        # Apply formatting based on column 1 (Indicator)
        for row_num, row_data in enumerate(df.values):
            indicator_val = row_data[1] if len(row_data) > 1 else ""
            met = evaluate(indicator_val)
            fmt = green_format if met else red_format
            
            # Write row with format
            for col_num, cell_value in enumerate(row_data):
                if pd.isna(cell_value):
                    cell_value = ""
                worksheet.write(row_num + 1, col_num, cell_value, fmt)

    writer.close()
    print(f"Saved highlighted Excel to {out_path}")
except Exception as e:
    print(f"Error: {e}")
