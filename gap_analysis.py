import pandas as pd
import os

excel_path = r'C:\Users\UNIONIT\Downloads\Link FTSE_Master_Checklist-9.24.xlsx'
df = pd.read_excel(excel_path, sheet_name='Checklis 322')

# Group by Theme TH and see how many items each theme has, and how many are "ดำเนินการแล้ว" (Done)
theme_stats = []

grouped = df.groupby('Theme TH')
for theme, group in grouped:
    total_items = len(group)
    
    # Check 'สถานะบนเว็ป' if it contains 'ขึ้นแล้ว'
    on_web_count = group['สถานะบนเว็ป'].astype(str).str.contains('ขึ้นแล้ว', na=False).sum()
    
    # Check 'สถานะ' == 'ดำเนินการแล้ว'
    done_count = group['สถานะ'].astype(str).str.contains('ดำเนินการแล้ว', na=False).sum()
    not_done_count = group['สถานะ'].astype(str).str.contains('ยังไม่ได้ดำเนินการ', na=False).sum()
    
    theme_stats.append({
        'Theme': theme,
        'Pillar': group['Pillar TH'].iloc[0],
        'Total Items': total_items,
        'On Web (from Excel)': on_web_count,
        'Done (from Excel)': done_count,
        'Not Started (from Excel)': not_done_count
    })

# Convert to DataFrame
stats_df = pd.DataFrame(theme_stats)
stats_df['% Not Started'] = round((stats_df['Not Started (from Excel)'] / stats_df['Total Items']) * 100, 1)

# Sort by most missing (highest Not Started count)
stats_df = stats_df.sort_values(by=['Not Started (from Excel)', 'Total Items'], ascending=[False, False])

with open('gap_analysis.txt', 'w', encoding='utf-8') as f:
    f.write("=== ESG GAP ANALYSIS (Based on Excel Data) ===\n\n")
    for _, row in stats_df.iterrows():
        f.write(f"Pillar: {row['Pillar']} | Theme: {row['Theme']}\n")
        f.write(f"  - Total Checklist Items: {row['Total Items']}\n")
        f.write(f"  - Marked as 'Done' internally: {row['Done (from Excel)']}\n")
        f.write(f"  - Marked as 'On Website': {row['On Web (from Excel)']}\n")
        f.write(f"  - 🔴 NOT STARTED (Missing): {row['Not Started (from Excel)']} ({row['% Not Started']}% of this theme)\n")
        f.write("-" * 40 + "\n")
