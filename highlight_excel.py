import os
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# Define HTML directories
html_dirs = [
    r'C:\Users\UNIONIT\Desktop\ลองทำ\สิ่งแวดล้อม',
    r'C:\Users\UNIONIT\Desktop\ลองทำ\สังคม',
    r'C:\Users\UNIONIT\Desktop\ลองทำ\การกำกับดูแลและเศรษฐกิจ',
    r'C:\Users\UNIONIT\Desktop\ลองทำ\ภาพรวมความยั่งยืน'
]

# Read all HTML files and aggregate text
all_text = ""
for d in html_dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        if f.endswith('.html'):
            with open(os.path.join(d, f), 'r', encoding='utf-8') as file:
                all_text += file.read() + " "

all_text = all_text.lower()

# Dictionary of keywords mapping to concepts
# If any keyword in the list is found in the HTML, we mark the indicator as found.
# For more generic indicators, we will check if the indicator text itself (or parts of it) exist.

def is_met(indicator):
    ind = indicator.lower()
    
    # Specific known strengths (Green)
    if 'scope 1' in ind and 'scope 1' in all_text: return True
    if 'scope 2' in ind and 'scope 2' in all_text: return True
    if 'iso 14001' in ind and 'iso 14001' in all_text: return True
    if 'coso' in ind and 'coso' in all_text: return True
    if 'กรรมการอิสระ' in ind and 'กรรมการอิสระ' in all_text: return True
    if 'ความหลากหลาย' in ind and 'ความหลากหลาย' in all_text: return True
    if 'iso 9001' in ind and 'iso 9001' in all_text: return True
    if 'แรงงานเด็ก' in ind and 'แรงงานเด็ก' in all_text: return True
    if 'แรงงานบังคับ' in ind and 'บังคับ' in all_text: return True
    if 'pdpa' in ind and 'pdpa' in all_text: return True
    
    # Check if a significant part of the indicator string exists in the text
    # Split indicator into meaningful words
    words = [w for w in ind.replace('/', ' ').replace('(', ' ').replace(')', ' ').split() if len(w) > 4]
    if not words:
        return False
        
    # If at least 2 key words are found in the text, mark as met
    matches = 0
    for w in words:
        if w in all_text:
            matches += 1
            
    if matches >= min(2, len(words)):
        return True
        
    return False

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
    'การประเมินความเสี่ยง', 'ต่อต้านคอร์รัปชัน', 'ความขัดแย้งทางผลประโยชน์'
]

def evaluate(indicator):
    ind = indicator.lower()
    for red in manual_reds:
        if red in ind:
            return False
    for green in manual_greens:
        if green in ind:
            return True
    return is_met(indicator)

file_path = r'C:\Users\UNIONIT\Downloads\FTSE Update 22.7.26.xlsx'
out_path = r'C:\Users\UNIONIT\Downloads\FTSE_Update_Highlighted.xlsx'

try:
    wb = load_workbook(file_path)

    green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

    for sheet_name in wb.sheetnames[:3]:
        ws = wb[sheet_name]
        for row in ws.iter_rows(min_row=2, max_row=120):
            indicator_cell = row[1] # Column B
            if indicator_cell.value:
                met = evaluate(str(indicator_cell.value))
                fill_color = green_fill if met else red_fill
                # Highlight the entire row up to col C
                for cell in row[:3]:
                    cell.fill = fill_color

    wb.save(out_path)
    print(f"Saved highlighted Excel to {out_path}")
except Exception as e:
    print(f"Error processing Excel: {e}")
