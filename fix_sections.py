import re

with open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken replacement from earlier first!
# I'll just use regex to extract the doc-items and rebuild the sections.

# Find the start of gov_risk
start_gov_risk = content.find('<div id="gov_risk" class="category-section">')
start_gov_control = content.find('<div id="gov_control" class="category-section">')
start_sustainability = content.find('<div id="sustainability" class="category-section">')

if start_gov_risk != -1 and start_gov_control != -1 and start_sustainability != -1:
    # We want to replace everything from start_gov_risk to start_sustainability
    
    # Let's extract the doc items for gov_risk
    # It contains "นโยบายบริหารความเสี่ยง.pdf"
    
    new_gov_risk = """                <!-- Category: Risk Management -->
                <div id="gov_risk" class="category-section">
                    <h2 class="section-title">นโยบายบริหารจัดการความเสี่ยง</h2>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>นโยบายการบริหารจัดการความเสี่ยง</h4>
                                <p>อัปเดตล่าสุด: ปี 2567 | ไฟล์ PDF</p>
                            </div>
                        </div>
                        <a href="การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/นโยบายบริหารความเสี่ยง.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> ดาวน์โหลด</a>
                    </div>
                </div>

                <!-- Category: Internal Control -->
                <div id="gov_control" class="category-section">
                    <h2 class="section-title">การควบคุมภายใน</h2>
                    <!-- ไม่มีไฟล์ PDF -->
                </div>

"""
    
    new_content = content[:start_gov_risk] + new_gov_risk + content[start_sustainability:]
    
    with open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed TH")
else:
    print("Could not find sections in TH")

