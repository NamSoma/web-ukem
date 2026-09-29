import pandas as pd

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
df = pd.read_excel(excel_path, sheet_name='Checklis 322')

# Filter for rows where either 'Unnamed: 6' or 'สถานะการกรอกข้อมูล' contains "One Report" or "56-1"
mask1 = df['Unnamed: 6'].astype(str).str.contains('One Report|56-1|รายงานประจำปี', case=False, na=False)
mask2 = df['สถานะการกรอกข้อมูล'].astype(str).str.contains('One Report|56-1|รายงานประจำปี', case=False, na=False)

filtered_df = df[mask1 | mask2]

# Perform Gap analysis on this filtered dataset
theme_stats = []
grouped = filtered_df.groupby('Theme TH')

for theme, group in grouped:
    total_items = len(group)
    done_count = group['สถานะ'].astype(str).str.contains('ดำเนินการแล้ว', na=False).sum()
    not_done_count = group['สถานะ'].astype(str).str.contains('ยังไม่ได้ดำเนินการ', na=False).sum()
    
    theme_stats.append({
        'Theme': theme,
        'Pillar': group['Pillar TH'].iloc[0],
        'Total Items': total_items,
        'Done (from Excel)': done_count,
        'Not Started (from Excel)': not_done_count
    })

stats_df = pd.DataFrame(theme_stats)
if not stats_df.empty:
    stats_df['% Not Started'] = round((stats_df['Not Started (from Excel)'] / stats_df['Total Items']) * 100, 1)
    stats_df = stats_df.sort_values(by=['Not Started (from Excel)', 'Total Items'], ascending=[False, False])

with open('onereport_gap.txt', 'w', encoding='utf-8') as f:
    f.write(f"=== ESG GAP ANALYSIS (ONLY FOR ITEMS REQUIRING 'ONE REPORT') ===\n")
    f.write(f"Total Checklist Items related to One Report: {len(filtered_df)}\n\n")
    if stats_df.empty:
        f.write("No items found matching 'One Report'.\n")
    else:
        for _, row in stats_df.iterrows():
            f.write(f"Pillar: {row['Pillar']} | Theme: {row['Theme']}\n")
            f.write(f"  - Total Items for One Report: {row['Total Items']}\n")
            f.write(f"  - Marked as 'Done' internally: {row['Done (from Excel)']}\n")
            f.write(f"  - 🔴 NOT STARTED (Missing): {row['Not Started (from Excel)']} ({row['% Not Started']}% of this theme)\n")
            f.write("-" * 40 + "\n")
