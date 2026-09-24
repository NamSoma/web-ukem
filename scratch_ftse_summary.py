import pandas as pd

excel_path = r"C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist_Update.xlsx"
out_path = "scratch_ftse_summary.txt"

try:
    xls = pd.ExcelFile(excel_path)
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Total items in checklist: {len(df)}\n\n")
        
        # Group by Pillar TH and Theme TH
        if 'Pillar TH' in df.columns and 'Theme TH' in df.columns:
            grouped = df.groupby(['Pillar', 'Pillar TH', 'Theme TH']).size().reset_index(name='Count')
            
            f.write("สรุปหัวข้อทั้งหมดใน Checklist ที่เว็บเรายังไม่มีการเปิดเผยข้อมูล:\n")
            f.write("-" * 50 + "\n")
            
            for index, row in grouped.iterrows():
                f.write(f"[{row['Pillar']}] {row['Pillar TH']} - {row['Theme TH']} : {row['Count']} ข้อ\n")
        else:
            f.write("Columns not found. Here are the columns:\n")
            f.write(str(df.columns))
            
except Exception as e:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
