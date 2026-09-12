import pandas as pd
import json

file_path = r'C:\Users\UNIONIT\Downloads\FTSE Update 22.7.26.xlsx'

try:
    df = pd.read_excel(file_path, sheet_name='Checklist_300')
    
    # We only need Pillar, Theme, and Indicator
    # According to previous output:
    # Pillar TH, Theme TH, Indicator / Checklist ภาษาไทย
    
    relevant_cols = ['Pillar', 'Pillar TH', 'Theme', 'Theme TH', 'Indicator / Checklist ภาษาไทย']
    
    # Filter only available columns
    available_cols = [c for c in relevant_cols if c in df.columns]
    
    df_filtered = df[available_cols].dropna(subset=['Indicator / Checklist ภาษาไทย'])
    
    # Group by Pillar -> Theme -> List of Indicators
    result = {}
    for _, row in df_filtered.iterrows():
        pillar = str(row.get('Pillar', 'Unknown')) + " (" + str(row.get('Pillar TH', '')) + ")"
        theme = str(row.get('Theme', 'Unknown')) + " (" + str(row.get('Theme TH', '')) + ")"
        indicator = str(row.get('Indicator / Checklist ภาษาไทย', ''))
        
        if pillar not in result:
            result[pillar] = {}
        if theme not in result[pillar]:
            result[pillar][theme] = []
            
        result[pillar][theme].append(indicator)
        
    with open('checklist_dump.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    print("Checklist successfully dumped to checklist_dump.json")
except Exception as e:
    print(f"Error: {e}")
