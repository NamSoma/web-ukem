import re

filepath = 'f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I want to find the start of 'gov_policy' and the end of 'gov_control' (which is before 'sustainability')
start_gov_policy = content.find('<div id="gov_policy" class="category-section active">')
start_sustainability = content.find('<div id="sustainability" class="category-section">')

if start_gov_policy != -1 and start_sustainability != -1:
    clean_content = """<div id="gov_policy" class="category-section active">
                    <h2 class="section-title">นโยบายการกำกับดูแลกิจการ</h2>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>นโยบายการกำกับดูแลกิจการที่ดี</h4>
                                <p>อัปเดตล่าสุด: ปี 2567 | ไฟล์ PDF</p>
                            </div>
                        </div>
                        <a href="การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/1.-นโยบายกำกับดูแลกิจการที่ดี.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> ดาวน์โหลด</a>
                    </div>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>นโยบายต่อต้านการทุจริตคอร์รัปชัน</h4>
                                <p>อัปเดตล่าสุด: ปี 2567 | ไฟล์ PDF</p>
                            </div>
                        </div>
                        <a href="การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> ดาวน์โหลด</a>
                    </div>
                </div>

                <!-- Category: Risk Management -->
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
                    <!-- ไม่มีไฟล์ PDF ที่หน้าดาวน์โหลด -->
                </div>

                <!-- Category: Sustainability -->
                """
    
    new_content = content[:start_gov_policy] + clean_content + content[start_sustainability + len('<div id="sustainability" class="category-section">'):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed TH")
else:
    print("Failed to find boundaries in TH")
