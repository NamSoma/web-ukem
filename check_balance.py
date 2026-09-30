import os
with open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', encoding='utf-8') as f:
    content = f.read()

risk_part = content.split('<div id="gov_risk"')[1].split('<div id="gov_control"')[0]
open_divs = risk_part.count('<div')
close_divs = risk_part.count('</div')

print(f"Risk part open divs: {open_divs}")
print(f"Risk part close divs: {close_divs}")
