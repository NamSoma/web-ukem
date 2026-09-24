import os

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
about_file = os.path.join(base_dir, "en", "About UKEM.html")

cg_content = """
    <!-- Corporate Governance Section -->
    <section id="corporate-governance" class="cg-section" style="padding: 80px 0; background-color: transparent;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 50px;">
                <h2 class="section-title">Corporate Governance Structure</h2>
                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 20px;"></div>
            </div>
            
            <div style="margin-bottom: 30px; background: var(--card-bg, #f8f9fa); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <h3 class="text-h3" style="margin: 0; color: var(--primary);">Authority and Duties of the Board of Directors</h3>
                </div>
                <ul class="styled-list" style="font-size: 16px; line-height: 1.8; color: var(--text-color, #333);">
                    <li><strong style="color: var(--primary);">Election and Assignment:</strong> Elect the Chairman, Vice Chairmen, and assign duties.</li>
                    <li><strong style="color: var(--primary);">General Management:</strong> Manage the company in accordance with its objectives, Articles of Association, and shareholder resolutions.</li>
                    <li><strong style="color: var(--primary);">Sub-committee Appointment:</strong> Appoint Audit, Executive, and Managing Directors, and define their authority and remuneration.</li>
                </ul>
            </div>

            <div style="margin-bottom: 30px; background: var(--card-bg, #f8f9fa); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <h3 class="text-h3" style="margin: 0; color: var(--primary);">Roles, Duties, and Responsibilities of the Board</h3>
                </div>
                <ul class="styled-list" style="font-size: 16px; line-height: 1.8; color: var(--text-color, #333);">
                    <li><strong style="color: var(--primary);">Legal Compliance:</strong> Supervise the company in compliance with laws, Articles of Association, and shareholder resolutions.</li>
                    <li><strong style="color: var(--primary);">Strategic Direction:</strong> Define vision, strategy, main policies, and approve budgets/investment projects.</li>
                    <li><strong style="color: var(--primary);">Monitoring and Control:</strong> Oversee implementation of plans and ensure effective internal control/audit systems.</li>
                    <li><strong style="color: var(--primary);">Risk & Conflict Management:</strong> Supervise conflict of interest matters and ensure comprehensive risk management systems.</li>
                    <li><strong style="color: var(--primary);">Transparency and Leadership:</strong> Ensure accurate information disclosure, act as role models, and appoint the Company Secretary.</li>
                </ul>
            </div>

            <div style="margin-top: 40px; background: var(--white); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <h3 class="text-h3" style="color: var(--primary); margin-bottom: 20px; text-align: center;">Download Documents</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/1.-โครงสร้างองค์กรBoard-Skill-Matrix-2569-Th.-ผสาน.pdf" title="โครงสร้างองค์กรและ Board Skill Matrix (Organization Structure and Board Skill Matrix)" meta="PDF"></doc-card>
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-1-แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ-26-2-68.pdf" title="แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ (Audit Committee Practice Guidelines)" meta="PDF"></doc-card>
                    <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-2-กฎบัตรคณะกรรมการตรวจสอบ-14-11-67.pdf" title="กฎบัตรคณะกรรมการตรวจสอบ (Audit Committee Charter)" meta="PDF"></doc-card>
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
        content = content.replace('<script src="../components/Footer.js" defer></script>',
                                  '<script src="../components/Footer.js" defer></script>\n    <script src="../components/DocDownload.js" defer></script>')

    # 2. Insert content
    if 'id="corporate-governance"' not in content:
        content = content.replace('<!-- Business Groups Section -->', cg_content + '    <!-- Business Groups Section -->')

    with open(about_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating EN")
