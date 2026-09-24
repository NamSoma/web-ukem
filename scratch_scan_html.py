import os
import glob

dirs = ['สิ่งแวดล้อม', 'สังคม', 'การกำกับดูแลและเศรษฐกิจ']
base_path = r"f:\Back up อีก HDD\งาน\ลองทำ"

keywords = ['Scope', 'คาร์บอน', 'ก๊าซเรือนกระจก', 'พลังงาน', 'ของเสีย', 'ขยะ', 'น้ำ', 
            'สิทธิมนุษยชน', 'ความปลอดภัย', 'บาดเจ็บ', 'อบรม', 'คอร์รัปชัน', 'ความเสี่ยง', 
            'คณะกรรมการ', 'TGO', 'ISO', 'รีไซเคิล']

results = []

for d in dirs:
    d_path = os.path.join(base_path, d)
    if os.path.exists(d_path):
        for f in glob.glob(os.path.join(d_path, '*.html')):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                
                found_kw = [kw for kw in keywords if kw in content]
                results.append(f"[{d}] {os.path.basename(f)}: พบ {len(found_kw)} คำหลัก ({', '.join(found_kw)})")

with open(os.path.join(base_path, 'scratch_scan_html.txt'), 'w', encoding='utf-8') as f:
    f.write("\n".join(results))
