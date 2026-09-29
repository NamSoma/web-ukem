import pandas as pd

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
output_excel = r'C:\Users\UNIONIT\Downloads\OneReport_Gap_Analysis.xlsx'

# Load checklist
df = pd.read_excel(excel_path, sheet_name='Checklis 322')

# Filter for One Report
mask1 = df['Unnamed: 6'].astype(str).str.contains('One Report|56-1|รายงานประจำปี', case=False, na=False)
mask2 = df['สถานะการกรอกข้อมูล'].astype(str).str.contains('One Report|56-1|รายงานประจำปี', case=False, na=False)

onereport_df = df[mask1 | mask2]

# Separate into Missing vs All
missing_df = onereport_df[onereport_df['สถานะ'].astype(str).str.contains('ยังไม่ได้ดำเนินการ', na=False)]

# Create Excel writer
try:
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        missing_df.to_excel(writer, sheet_name='Missing in One Report (17)', index=False)
        onereport_df.to_excel(writer, sheet_name='All One Report Items (102)', index=False)
    print(f"Successfully generated: {output_excel}")
except Exception as e:
    print(f"Failed to generate Excel: {e}")
