import re

filepath = 'f:/Back up อีก HDD/งาน/ลองทำ/en/นโยบายและเอกสารดาวน์โหลด.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_gov_policy = content.find('<div id="gov_policy" class="category-section active">')
start_sustainability = content.find('<div id="sustainability" class="category-section">')

if start_gov_policy != -1 and start_sustainability != -1:
    clean_content = """<div id="gov_policy" class="category-section active">
                    <h2 class="section-title">Corporate Governance Policy</h2>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>Corporate Governance Policy</h4>
                                <p>Last Updated: 2024 | PDF File</p>
                            </div>
                        </div>
                        <a href="../การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/1.-นโยบายกำกับดูแลกิจการที่ดี.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> Download</a>
                    </div>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>Anti-Corruption Policy</h4>
                                <p>Last Updated: 2024 | PDF File</p>
                            </div>
                        </div>
                        <a href="../การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> Download</a>
                    </div>
                </div>

                <!-- Category: Risk Management -->
                <div id="gov_risk" class="category-section">
                    <h2 class="section-title">Risk Management Policy</h2>
                    
                    <div class="doc-item">
                        <div class="doc-info">
                            <div class="doc-icon"><i data-feather="file-text"></i></div>
                            <div class="doc-text">
                                <h4>Risk Management Policy</h4>
                                <p>Last Updated: 2024 | PDF File</p>
                            </div>
                        </div>
                        <a href="../การกำกับดูแลและเศรษฐกิจ/เอกสารPDF/นโยบายบริหารความเสี่ยง.pdf" target="_blank" class="doc-download-btn"><i data-feather="download"></i> Download</a>
                    </div>
                </div>

                <!-- Category: Internal Control -->
                <div id="gov_control" class="category-section">
                    <h2 class="section-title">Internal Control</h2>
                    <!-- No PDF files available -->
                </div>

                <!-- Category: Sustainability -->
                """
    
    new_content = content[:start_gov_policy] + clean_content + content[start_sustainability + len('<div id="sustainability" class="category-section">'):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed EN")
else:
    print("Failed to find boundaries in EN")
