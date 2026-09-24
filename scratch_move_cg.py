import os

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
about_file = os.path.join(base_dir, "เกี่ยวกับ UKEM.html")

cg_content = """
    <!-- Corporate Governance Section -->
    <section id="corporate-governance" class="cg-section" style="padding: 80px 0; background-color: transparent;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 50px;">
                <h2 class="section-title">โครงสร้างการกำกับดูแลกิจการ</h2>
                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 20px;"></div>
            </div>
            
            <div style="margin-bottom: 30px; background: var(--card-bg, #f8f9fa); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <h3 class="text-h3" style="margin: 0; color: var(--primary);">อำนาจหน้าที่ของคณะกรรมการบริษัท</h3>
                </div>
                <ul class="styled-list" style="font-size: 16px; line-height: 1.8; color: var(--text-color, #333);">
                    <li><strong style="color: var(--primary);">การเลือกตั้งและมอบหมาย:</strong> เลือกตั้งประธานกรรมการ รองประธานกรรมการ และมอบหมายหน้าที่</li>
                    <li><strong style="color: var(--primary);">การจัดการทั่วไป:</strong> จัดการบริษัทให้เป็นไปตามวัตถุประสงค์ ข้อบังคับ และมติที่ประชุมผู้ถือหุ้น</li>
                    <li><strong style="color: var(--primary);">การแต่งตั้งคณะกรรมการชุดย่อย:</strong> แต่งตั้งกรรมการตรวจสอบ กรรมการบริหาร กรรมการผู้จัดการ พร้อมกำหนดอำนาจหน้าที่และค่าตอบแทน</li>
                </ul>
            </div>

            <div style="margin-bottom: 30px; background: var(--card-bg, #f8f9fa); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <h3 class="text-h3" style="margin: 0; color: var(--primary);">บทบาทหน้าที่และความรับผิดชอบของคณะกรรมการ</h3>
                </div>
                <ul class="styled-list" style="font-size: 16px; line-height: 1.8; color: var(--text-color, #333);">
                    <li><strong style="color: var(--primary);">กำกับดูแลตามกฎหมาย:</strong> ดูแลบริษัทให้เป็นไปตามกฎหมาย ข้อบังคับ และมติผู้ถือหุ้น</li>
                    <li><strong style="color: var(--primary);">กำหนดทิศทางองค์กร:</strong> กำหนดวิสัยทัศน์ กลยุทธ์ นโยบายหลัก และอนุมัติงบประมาณ/โครงการลงทุน</li>
                    <li><strong style="color: var(--primary);">ติดตามและควบคุม:</strong> ควบคุมให้การดำเนินงานเป็นไปตามแผน และจัดให้มีระบบควบคุมภายใน/ตรวจสอบภายใน</li>
                    <li><strong style="color: var(--primary);">บริหารความเสี่ยงและความขัดแย้ง:</strong> ดูแลเรื่องความขัดแย้งทางผลประโยชน์ และกำหนดแนวทางบริหารความเสี่ยง</li>
                    <li><strong style="color: var(--primary);">ความโปร่งใสและเป็นผู้นำ:</strong> เปิดเผยข้อมูลอย่างถูกต้อง โปร่งใส เป็นแบบอย่างที่ดี และแต่งตั้งเลขานุการบริษัท</li>
                </ul>
            </div>

            <div style="margin-top: 40px; background: var(--white); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <h3 class="text-h3" style="color: var(--primary); margin-bottom: 20px; text-align: center;">เอกสารดาวน์โหลดที่เกี่ยวข้อง</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/1.-โครงสร้างองค์กรBoard-Skill-Matrix-2569-Th.-ผสาน.pdf" title="โครงสร้างองค์กรและ Board Skill Matrix" meta="PDF"></doc-card>
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-1-แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ-26-2-68.pdf" title="แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ" meta="PDF"></doc-card>
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-2-กฎบัตรคณะกรรมการตรวจสอบ-14-11-67.pdf" title="กฎบัตรคณะกรรมการตรวจสอบ" meta="PDF"></doc-card>
                </div>
            </div>
        </div>
    </section>

"""

if os.path.exists(about_file):
    with open(about_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert script if not exists
    if 'DocDownload.js' not in content:
        content = content.replace('<script src="components/Footer.js" defer></script>',
                                  '<script src="components/Footer.js" defer></script>\n    <script src="components/DocDownload.js" defer></script>')

    # 2. Insert content
    if 'id="corporate-governance"' not in content:
        content = content.replace('<!-- Business Groups Section -->', cg_content + '    <!-- Business Groups Section -->')

    with open(about_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update Navbar.js
nav_file = os.path.join(base_dir, "components", "Navbar.js")
if os.path.exists(nav_file):
    with open(nav_file, 'r', encoding='utf-8') as f:
        nav_content = f.read()
    
    # Replace for TH
    nav_content = nav_content.replace(
        '<a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html">โครงสร้างการกำกับดูแลกิจการ</a>',
        '<a href="${linkBase}เกี่ยวกับ UKEM.html#corporate-governance">โครงสร้างการกำกับดูแลกิจการ</a>'
    )
    
    # Replace for EN
    nav_content = nav_content.replace(
        '<a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html">Governance Structure</a>',
        '<a href="${linkBase}About UKEM.html#corporate-governance">Governance Structure</a>'
    )
    
    with open(nav_file, 'w', encoding='utf-8') as f:
        f.write(nav_content)

print("Done updating")
