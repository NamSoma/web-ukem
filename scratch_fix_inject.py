import os
import re

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"

# 1. Update ข่าวสารและกิจกรรม.html
news_th = os.path.join(base_dir, "ข่าวสารและกิจกรรม.html")
cards_th = """
                <!-- Activity 10 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="assets/รูปสังคม/ประชุมคุณพล.jpg" alt="การสื่อสารภายในองค์กร" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>รอรูปภาพ</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">สวัสดิการพนักงาน</div>
                        <h3 class="news-title">การสื่อสารภายในองค์กร</h3>
                        <p class="news-desc">
                            บริษัทฯ ได้สร้างการมีส่วนร่วมในการปฏิบัติงานทุกระดับด้วยการจัดตั้งคณะกรรมการความปลอดภัย อาชีวอนามัย และสภาพแวดล้อมในการทำงาน ซึ่งประกอบด้วยผู้แทนในระดับบังคับบัญชาและผู้แทนลูกจ้าง เพื่อร่วมกันสำรวจสภาพการทำงานที่ไม่ปลอดภัย พิจารณาแผนงานและนโยบายด้านความปลอดภัย อาชีวอนามัย และสิ่งแวดล้อม การติดตามการดำเนินงานให้สอดคล้องกับกฎหมาย รวมถึงการสื่อสารเพื่อป้องกัน
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">ปี 2569</div>
                    </div>
                </div>

                <!-- Activity 11 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="assets/รูปสังคม/2ตรวจสุขภาพประจำปี 2568.jpg" alt="การจัดกิจกรรมส่งเสริมสุขภาพ" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>รอรูปภาพ</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">สวัสดิการพนักงาน</div>
                        <h3 class="news-title">การจัดกิจกรรมส่งเสริมสุขภาพ</h3>
                        <p class="news-desc">
                            บริษัทฯ จัดให้มีการตรวจสุขภาพสำหรับพนักงานเข้าใหม่ การตรวจสุขภาพประจำปีให้กับพนักงานทุกคนตามปัจจัยเสี่ยงในงานและเฝ้าระวังผลกระทบที่อาจเกิดจากการปฏิบัติงาน เช่นการตรวจสมรรถภาพปอด การตรวจสมรรถภาพการได้ยิน การตรวจสายตาอาชีวอนามัย และการตรวจหาสารโลหะหนักในร่างกาย ภายใต้ระบบฐานข้อมูลด้านสุขภาพและการเจ็บป่วยของพนักงาน นอกจากนี้ ยังดำเนินกิจกรรมส่งเสริมสุขภาพตามหลัก Happy Workplace
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">ปี 2569</div>
                    </div>
                </div>

                <!-- Activity 12 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="assets/รูปสังคม/ซ้อมดับเพลิง.jpg" alt="การสร้างความตระหนักและวัฒนธรรมด้านความปลอดภัยขององค์กร" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>รอรูปภาพ</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">สวัสดิการพนักงาน</div>
                        <h3 class="news-title">การสร้างความตระหนักและวัฒนธรรมด้านความปลอดภัยขององค์กร</h3>
                        <p class="news-desc">
                            การสร้างความตระหนักและวัฒนธรรมด้านความปลอดภัยเป็นหัวใจสำคัญของการดำเนินธุรกิจในอุตสาหกรรมเคมีภัณฑ์ บริษัทฯ จึงให้ความสำคัญกับการปลูกฝังแนวคิด “ความปลอดภัยเป็นหน้าที่ของทุกคน” ผ่านการฝึกอบรมอย่างต่อเนื่อง มาตรการป้องกันเชิงรุก และการส่งเสริมการมีส่วนร่วมของพนักงานในทุกระดับ นอกจากนี้ ยังนำเทคโนโลยีและมาตรฐานสากลมาปรับใช้ เพื่อเสริมสร้างสภาพแวดล้อมการทำงานที่ปลอดภัยและลดความเสี่ยงในการปฏิบัติงาน
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">ปี 2569</div>
                    </div>
                </div>
"""

with open(news_th, 'r', encoding='utf-8') as f:
    c = f.read()
    if '<!-- Activity 10 -->' not in c:
        # Find the closing tag of news-grid. It's followed by </div> then <div class="pagination"> usually, or similar
        # Since I know the grid ends with a </div>, let's insert it right after the last activity
        c = re.sub(r'(<!-- Activity 9 -->.*?</div>\s*</div>)', r'\1\n' + cards_th, c, flags=re.DOTALL)
        with open(news_th, 'w', encoding='utf-8') as f:
            f.write(c)

# 2. Update en/ข่าวสารและกิจกรรม.html
news_en = os.path.join(base_dir, "en", "ข่าวสารและกิจกรรม.html")
cards_en = """
                <!-- Activity 10 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="../assets/รูปสังคม/ประชุมคุณพล.jpg" alt="Internal Communication" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>Waiting for image</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">Employee Welfare</div>
                        <h3 class="news-title">Internal Communication</h3>
                        <p class="news-desc">
                            The Company engages employees at all levels by establishing the Occupational Safety, Health and Environment Committee. This committee comprises representatives from management and employees to jointly survey unsafe working conditions, consider safety policies and plans, monitor legal compliance, and communicate preventive measures.
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">Year 2026</div>
                    </div>
                </div>

                <!-- Activity 11 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="../assets/รูปสังคม/2ตรวจสุขภาพประจำปี 2568.jpg" alt="Organizing Health Promotion Activities" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>Waiting for image</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">Employee Welfare</div>
                        <h3 class="news-title">Organizing Health Promotion Activities</h3>
                        <p class="news-desc">
                            The Company arranges health check-ups for new employees and annual health check-ups for all employees based on occupational risk factors, monitoring potential impacts from operations. This includes lung function tests, hearing tests, occupational vision tests, and heavy metal screening, managed under the employee health and illness database system. Additionally, health promotion activities are conducted in accordance with Happy Workplace principles.
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">Year 2026</div>
                    </div>
                </div>

                <!-- Activity 12 -->
                <div class="news-card" data-category="welfare">
                    <div class="news-img">
                        <img src="../assets/รูปสังคม/ซ้อมดับเพลิง.jpg" alt="Building Corporate Safety Awareness and Culture" onerror="this.style.display='none'; this.parentNode.innerHTML='<span style=\\'color:#999; font-weight: 500;\\'>Waiting for image</span>';">
                    </div>
                    <div class="news-content">
                        <div class="news-category welfare">Employee Welfare</div>
                        <h3 class="news-title">Building Corporate Safety Awareness and Culture</h3>
                        <p class="news-desc">
                            Building corporate safety awareness and culture is a core element of operating in the chemical industry. The Company places great importance on instilling the concept of "Safety is Everyone's Responsibility" through continuous training, proactive preventive measures, and promoting employee participation at all levels. Furthermore, international standards and technologies are adopted to enhance a safe working environment and reduce operational risks.
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">Year 2026</div>
                    </div>
                </div>
"""
with open(news_en, 'r', encoding='utf-8') as f:
    c = f.read()
    if '<!-- Activity 10 -->' not in c:
        c = re.sub(r'(<!-- Activity 9 -->.*?</div>\s*</div>)', r'\1\n' + cards_en, c, flags=re.DOTALL)
        with open(news_en, 'w', encoding='utf-8') as f:
            f.write(c)

print("Done injecting")
