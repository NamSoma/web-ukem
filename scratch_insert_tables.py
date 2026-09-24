import os

# 1. Update Occupational Health and Safety
safety_file = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\อาชีวอนามัยและความปลอดภัย.html"
with open(safety_file, 'r', encoding='utf-8') as f:
    safety_html = f.read()

target_safety_str = """            <card-grid style="margin-top: 40px; margin-bottom: 40px;">
                <div class="card-item-blue" style="text-align: center;">
                    <div class="safety-stat-value" style="color: var(--primary);">0</div>
                    <div class="safety-stat-label">อัตราความถี่ของการบาดเจ็บจากการทำงาน (LTIFR)</div>
                    <div class="safety-stat-label" style="font-size: 12px; margin-top: 5px;">(ต่อ 1,000,000 ชั่วโมงการทำงาน)</div>
                </div>
                <div class="card-item-blue" style="text-align: center;">
                    <div class="safety-stat-value" style="color: var(--primary);">0</div>
                    <div class="safety-stat-label">จำนวนผู้เสียชีวิตจากการทำงาน (ราย)</div>
                </div>
            </card-grid>"""

replacement_safety_str = """            <style>
                .esg-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 40px 0;
                    background-color: var(--white);
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    overflow: hidden;
                }
                .esg-table th, .esg-table td {
                    padding: 15px 20px;
                    text-align: center;
                    border-bottom: 1px solid var(--border-color);
                }
                .esg-table th {
                    background-color: #f8f9fa;
                    color: var(--text-main);
                    font-weight: 600;
                    text-align: center;
                }
                .esg-table th:first-child, .esg-table td:first-child {
                    text-align: left;
                }
                .esg-table tr:last-child td {
                    border-bottom: none;
                }
                .esg-table tr:hover td {
                    background-color: rgba(0,0,0,0.02);
                }
            </style>
            
            <section-header title="สถิติความปลอดภัยในการทำงาน (3 ปีย้อนหลัง)"></section-header>
            <div style="overflow-x: auto; margin-bottom: 40px;">
                <table class="esg-table">
                    <thead>
                        <tr>
                            <th>ตัวชี้วัดด้านอาชีวอนามัยและความปลอดภัย</th>
                            <th>หน่วย</th>
                            <th>ปี 2566</th>
                            <th>ปี 2567</th>
                            <th>ปี 2568</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>จำนวนชั่วโมงการทำงาน - พนักงาน</td>
                            <td>ชั่วโมง</td>
                            <td>325,836</td>
                            <td>316,625</td>
                            <td>307,992</td>
                        </tr>
                        <tr>
                            <td>จำนวนชั่วโมงการทำงาน - ผู้รับเหมา</td>
                            <td>ชั่วโมง</td>
                            <td>37,427</td>
                            <td>37,427</td>
                            <td>37,427</td>
                        </tr>
                        <tr>
                            <td>อัตราความถี่ของการบาดเจ็บ (TRIFR)</td>
                            <td>ราย / 1 ล้านชั่วโมง</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                        </tr>
                        <tr>
                            <td>อัตราการบาดเจ็บถึงขั้นหยุดงาน (LTIFR)</td>
                            <td>ราย / 1 ล้านชั่วโมง</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                            <td style="color: var(--primary); font-weight: bold;">0</td>
                        </tr>
                    </tbody>
                </table>
            </div>"""

if target_safety_str in safety_html:
    safety_html = safety_html.replace(target_safety_str, replacement_safety_str)
    with open(safety_file, 'w', encoding='utf-8') as f:
        f.write(safety_html)
    print("Updated safety file successfully.")
else:
    print("Target string not found in safety file.")


# 2. Update Human Rights and Labor
hr_file = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html"
with open(hr_file, 'r', encoding='utf-8') as f:
    hr_html = f.read()

target_hr_str = """            </card-grid>"""

replacement_hr_str = """            </card-grid>

            <style>
                .esg-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 40px 0;
                    background-color: var(--white);
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    overflow: hidden;
                }
                .esg-table th, .esg-table td {
                    padding: 15px 20px;
                    text-align: center;
                    border-bottom: 1px solid var(--border-color);
                }
                .esg-table th {
                    background-color: #f8f9fa;
                    color: var(--text-main);
                    font-weight: 600;
                    text-align: center;
                }
                .esg-table th:first-child, .esg-table td:first-child {
                    text-align: left;
                }
                .esg-table tr:last-child td {
                    border-bottom: none;
                }
                .esg-table tr:hover td {
                    background-color: rgba(0,0,0,0.02);
                }
            </style>
            
            <section-header title="สถิติการฝึกอบรมและพัฒนาพนักงาน (3 ปีย้อนหลัง)"></section-header>
            <div style="overflow-x: auto; margin-bottom: 40px;">
                <table class="esg-table">
                    <thead>
                        <tr>
                            <th>ตัวชี้วัดการฝึกอบรมพนักงาน</th>
                            <th>หน่วย</th>
                            <th>ปี 2566</th>
                            <th>ปี 2567</th>
                            <th>ปี 2568</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>จำนวนพนักงานทั้งหมด</td>
                            <td>คน</td>
                            <td>127</td>
                            <td>125</td>
                            <td>124</td>
                        </tr>
                        <tr>
                            <td>จำนวนชั่วโมงการอบรมรวม</td>
                            <td>ชั่วโมง</td>
                            <td>937</td>
                            <td>1,000</td>
                            <td>984</td>
                        </tr>
                        <tr>
                            <td>ชั่วโมงการอบรมเฉลี่ยต่อคน</td>
                            <td>ชั่วโมง / คน / ปี</td>
                            <td>7.38</td>
                            <td>8.00</td>
                            <td>8.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>"""

if target_hr_str in hr_html:
    # Only replace the FIRST occurrence after the intro section if possible, or just the first overall.
    # The file has exactly one </card-grid> tag currently (lines 106-127). Wait, there's another one at line 189 inside the alert card.
    # So I shouldn't just replace all. I'll split and insert.
    pass

# Safe replacement for HR file
target_hr_exact = """                <div class="card-item" style="text-align: center;">
                    <div class="hr-stat-value">1 <span style="font-size: 24px;">คน</span></div>
                    <div class="hr-stat-label">แรงงานข้ามชาติ (ถูกกฎหมาย 100%)</div>
                </div>
            </card-grid>"""

replacement_hr_exact = """                <div class="card-item" style="text-align: center;">
                    <div class="hr-stat-value">1 <span style="font-size: 24px;">คน</span></div>
                    <div class="hr-stat-label">แรงงานข้ามชาติ (ถูกกฎหมาย 100%)</div>
                </div>
            </card-grid>

            <style>
                .esg-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 40px 0;
                    background-color: var(--white);
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    overflow: hidden;
                }
                .esg-table th, .esg-table td {
                    padding: 15px 20px;
                    text-align: center;
                    border-bottom: 1px solid var(--border-color);
                }
                .esg-table th {
                    background-color: #f8f9fa;
                    color: var(--text-main);
                    font-weight: 600;
                    text-align: center;
                }
                .esg-table th:first-child, .esg-table td:first-child {
                    text-align: left;
                }
                .esg-table tr:last-child td {
                    border-bottom: none;
                }
                .esg-table tr:hover td {
                    background-color: rgba(0,0,0,0.02);
                }
            </style>
            
            <section-header title="สถิติการฝึกอบรมและพัฒนาพนักงาน (3 ปีย้อนหลัง)"></section-header>
            <div style="overflow-x: auto; margin-bottom: 40px;">
                <table class="esg-table">
                    <thead>
                        <tr>
                            <th>ตัวชี้วัดการฝึกอบรมพนักงาน</th>
                            <th>หน่วย</th>
                            <th>ปี 2566</th>
                            <th>ปี 2567</th>
                            <th>ปี 2568</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>จำนวนพนักงานทั้งหมด</td>
                            <td>คน</td>
                            <td>127</td>
                            <td>125</td>
                            <td>124</td>
                        </tr>
                        <tr>
                            <td>จำนวนชั่วโมงการอบรมรวม</td>
                            <td>ชั่วโมง</td>
                            <td>937</td>
                            <td>1,000</td>
                            <td>984</td>
                        </tr>
                        <tr>
                            <td>ชั่วโมงการอบรมเฉลี่ยต่อคน</td>
                            <td>ชั่วโมง / คน / ปี</td>
                            <td>7.38</td>
                            <td>8.00</td>
                            <td>8.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>"""

if target_hr_exact in hr_html:
    hr_html = hr_html.replace(target_hr_exact, replacement_hr_exact)
    with open(hr_file, 'w', encoding='utf-8') as f:
        f.write(hr_html)
    print("Updated HR file successfully.")
else:
    print("Target string not found in HR file.")

