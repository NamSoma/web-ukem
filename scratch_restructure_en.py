import re

# Read Thai file
with open('เกี่ยวกับ UKEM.html', 'r', encoding='utf-8') as f:
    th_html = f.read()

# Extract sections from Thai
org_match = re.search(r'<!-- Organization Structure Section -->(.*?)(?=<!-- Business Groups Section -->|<!-- Milestones Section -->)', th_html, re.DOTALL)
milestones_match = re.search(r'<!-- Milestones Section -->(.*?)(?=<style>\s*@media)', th_html, re.DOTALL)

org_html = org_match.group(0) if org_match else ""
milestones_html = milestones_match.group(0) if milestones_match else ""

# Translate Org Structure
org_html = org_html.replace('โครงสร้างองค์กร', 'Organization Structure')
org_html = org_html.replace('ประธานกรรมการบริษัท', 'Chairman of the Board')
org_html = org_html.replace('คณะกรรมการตรวจสอบ<br>และส่วนงานตรวจสอบภายใน', 'Audit Committee<br>& Internal Audit')
org_html = org_html.replace('คณะกรรมการบริหารความเสี่ยง', 'Risk Management Committee')
org_html = org_html.replace('คณะกรรมการบริหาร', 'Executive Committee')
org_html = org_html.replace('ประธานกรรมการบริหาร', 'Chairman of Executive Committee')
org_html = org_html.replace('กรรมการผู้จัดการ', 'Managing Director')
org_html = org_html.replace('รองกรรมการผู้จัดการ', 'Deputy Managing Director')

org_html = org_html.replace('ฝ่ายวางแผน<br>การตลาด<br>และจัดซื้อ', 'Marketing &<br>Procurement<br>Dept.')
org_html = org_html.replace('ส่วนงานขาย', 'Sales Div.')
org_html = org_html.replace('ส่วนงานการตลาด<br>และจัดซื้อ', 'Marketing &<br>Procurement Div.')
org_html = org_html.replace('ส่วนงาน<br>ลูกค้าสัมพันธ์', 'Customer<br>Relations Div.')

org_html = org_html.replace('ฝ่ายบัญชี<br>และการเงิน', 'Accounting &<br>Finance Dept.')
org_html = org_html.replace('ส่วนงานบัญชี<br>และการเงิน', 'Accounting &<br>Finance Div.')
org_html = org_html.replace('ส่วนงานสินเชื่อ', 'Credit Div.')

org_html = org_html.replace('ฝ่ายพัฒนาธุรกิจ', 'Business<br>Development Dept.')
org_html = org_html.replace('ส่วนงาน<br>พัฒนาธุรกิจ', 'Business<br>Development Div.')

org_html = org_html.replace('ฝ่ายบริหาร<br>งานบุคคล', 'Human<br>Resources Dept.')
org_html = org_html.replace('ส่วนงาน<br>บริหารบุคคล', 'HR Div.')

org_html = org_html.replace('ฝ่ายคลังสินค้า<br>และขนส่ง', 'Warehouse &<br>Transport Dept.')
org_html = org_html.replace('ส่วนงาน<br>คลังสินค้า', 'Warehouse Div.')
org_html = org_html.replace('ส่วนงานขนส่ง', 'Transport Div.')

org_html = org_html.replace('ฝ่ายไอทีและ<br>ธุรกิจดิจิทัล', 'IT & Digital<br>Business Dept.')
org_html = org_html.replace('ส่วนงานไอที', 'IT Div.')
org_html = org_html.replace('ส่วนงาน<br>ระบบดิจิทัล', 'Digital Systems Div.')


# Translate Milestones
milestones_html = milestones_html.replace('การเปลี่ยนแปลงและพัฒนาการที่สำคัญ', 'Key Milestones & Developments')
milestones_html = milestones_html.replace('ก้าวสำคัญที่ผลักดันความสำเร็จและการเติบโตอย่างยั่งยืนของ UKEM', 'Significant steps driving UKEM\'s success and sustainable growth')

milestones_html = milestones_html.replace('ปี 2568', '2025')
milestones_html = milestones_html.replace('23 พ.ค. 68:', 'May 23, 2025:')
milestones_html = milestones_html.replace('ผ่านการทวนสอบและรับรองรายงานปริมาณก๊าซเรือนกระจกตามมาตรฐาน ISO 14064-1 โดย สถาบันรับรองมาตรฐานไอเอสโอ', 'Verified and certified greenhouse gas emissions report according to ISO 14064-1 standard by MASCI')
milestones_html = milestones_html.replace('24 มิ.ย. 68:', 'Jun 24, 2025:')
milestones_html = milestones_html.replace('ได้รับการรับรองเครื่องหมายคาร์บอนฟุตพริ้นท์ขององค์กร (CFO) จากองค์การบริหารจัดการก๊าซเรือนกระจก', 'Received Carbon Footprint of Organization (CFO) certification from Thailand Greenhouse Gas Management Organization (TGO)')

milestones_html = milestones_html.replace('ปี 2567', '2024')
milestones_html = milestones_html.replace('5 มิ.ย. 67:', 'Jun 5, 2024:')
milestones_html = milestones_html.replace('โครงการซื้อหุ้นคืนสิ้นสุดลง โดยรวมสะสมแล้วจำนวน 78.15 ล้านหุ้น คิดเป็น 6.73%', 'The share repurchase program ended with an accumulated total of 78.15 million shares, accounting for 6.73%')

milestones_html = milestones_html.replace('ปี 2566', '2023')
milestones_html = milestones_html.replace('20 ก.พ. 66:', 'Feb 20, 2023:')
milestones_html = milestones_html.replace('ที่ประชุมวิสามัญผู้ถือหุ้นมีมติอนุมัติจำหน่ายหุ้นสามัญของ GIFT ทั้งหมด', 'The EGM resolved to approve the sale of all ordinary shares in GIFT')
milestones_html = milestones_html.replace('30 พ.ย. 66:', 'Nov 30, 2023:')
milestones_html = milestones_html.replace('อนุมัติโครงการซื้อหุ้นคืนเพื่อบริหารวงเงินสูงสุด 66 ล้านบาท', 'Approved a share repurchase program for financial management with a maximum limit of 66 million baht')

milestones_html = milestones_html.replace('ปี 2565', '2022')
milestones_html = milestones_html.replace('31 ธ.ค. 65:', 'Dec 31, 2022:')
milestones_html = milestones_html.replace('คณะกรรมการบริษัทมีมติอนุมัติการขายเงินลงทุนในบริษัท แกรททิทูด อินฟินิท จำกัด (มหาชน) (GIFT)', 'The Board of Directors approved the sale of investment in Gratitude Infinite Public Company Limited (GIFT)')

milestones_html = milestones_html.replace('ปี 2564', '2021')
milestones_html = milestones_html.replace('30 ก.ย. 64:', 'Sep 30, 2021:')
milestones_html = milestones_html.replace('ดำเนินการซื้อหุ้นสามัญคืนสะสมจำนวน 74.23 ล้านหุ้น', 'Accumulated share repurchase of 74.23 million shares')
milestones_html = milestones_html.replace('20 ธ.ค. 64:', 'Dec 20, 2021:')
milestones_html = milestones_html.replace('จดทะเบียนลดทุนชำระแล้วสำหรับหุ้นสามัญซื้อคืนที่ไม่สามารถจำหน่ายได้หมด', 'Registered a decrease in paid-up capital for unsold repurchased shares')

milestones_html = milestones_html.replace('ปี 2563', '2020')
milestones_html = milestones_html.replace('24 มี.ค. 63:', 'Mar 24, 2020:')
milestones_html = milestones_html.replace('จดทะเบียนเพิ่มทุนจากการเสนอขายใบสำคัญแสดงสิทธิ UKEM-W2', 'Registered capital increase from the offering of UKEM-W2 warrants')
milestones_html = milestones_html.replace('12 พ.ย. 63:', 'Nov 12, 2020:')
milestones_html = milestones_html.replace('อนุมัติโครงการซื้อหุ้นคืน 123 ล้านหุ้น เพื่อบริหารทางการเงิน', 'Approved a share repurchase program of 123 million shares for financial management')
milestones_html = milestones_html.replace('25 ธ.ค. 63:', 'Dec 25, 2020:')
milestones_html = milestones_html.replace('ได้รับการรับรองมาตรฐานบริหารคุณภาพ ISO 9001:2015 จากบริษัท เอส จี เอส (ประเทศไทย) จำกัด', 'Certified for ISO 9001:2015 Quality Management Standard by SGS (Thailand) Ltd.')


# Read EN file
with open('en/About UKEM.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

# Extract sections from EN
about_match = re.search(r'(<!-- About Section -->.*?</section>)', en_html, re.DOTALL)
business_match = re.search(r'(<!-- Business Groups Section -->.*?</section>)', en_html, re.DOTALL)
leadership_match = re.search(r'(<!-- Leadership Section -->.*?</section>)', en_html, re.DOTALL)

if about_match and business_match and leadership_match:
    about_html = about_match.group(1)
    business_html = business_match.group(1)
    leadership_html = leadership_match.group(1)
    
    # Reassemble EN file
    # We replace everything between <!-- About Section --> and </style>\n    <main-footer depth="1" lang="en"></main-footer>
    start_idx = en_html.find('<!-- About Section -->')
    end_idx = en_html.find('<style>\n        .pillar-card:hover')
    
    if start_idx != -1 and end_idx != -1:
        new_content = en_html[:start_idx] + about_html + '\n\n    ' + leadership_html + '\n\n    ' + org_html + '\n\n    ' + business_html + '\n\n    ' + milestones_html + '\n\n    ' + en_html[end_idx:]
        
        with open('en/About UKEM.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully reassembled en/About UKEM.html")
    else:
        print("Could not find start or end index for replacement")
else:
    print("Could not find all sections in EN file")

