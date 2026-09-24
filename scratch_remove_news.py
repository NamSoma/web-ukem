import os

target_file = r"f:\Back up อีก HDD\งาน\ลองทำ\เกี่ยวกับ UKEM.html"

with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

target_str = """    <!-- News and Activities Section -->
    <section id="news-activities" class="news-section" style="padding: 80px 0; background-color: #f9fafb;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 50px;">
                <h2 class="section-title">ข่าวสารและกิจกรรม</h2>
                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 20px;"></div>
                <p style="color: var(--text-muted); font-size: 18px;">กิจกรรมเพื่อสังคมและพนักงาน (CSR & Employee Engagement)</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
                <!-- Activity 1 -->
                <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
                    <div style="height: 250px; overflow: hidden;">
                        <img src="assets/รูปสังคม/crab_release.png" alt="กิจกรรมปล่อยปูม้า" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    </div>
                    <div style="padding: 25px;">
                        <div style="color: var(--primary); font-size: 14px; font-weight: 600; margin-bottom: 10px;">กิจกรรมเพื่อสังคม (CSR)</div>
                        <h3 style="color: var(--text-color); font-size: 20px; font-weight: 700; margin-top: 0; margin-bottom: 15px; line-height: 1.4;">ปล่อยปูม้าคืนสู่ธรรมชาติ</h3>
                        <p style="color: var(--text-muted); line-height: 1.6; margin: 0; font-size: 15px;">
                            ผู้บริหารและพนักงาน ร่วมกันปล่อยปูม้าคืนสู่ธรรมชาติ ณ ศูนย์เรียนรู้ธนาคารสัตว์ทะเลเกาะสีชังโดยชุมชน เพื่อเป็นการอนุรักษ์ ฟื้นฟู และเพิ่มปริมาณสัตว์น้ำในระบบนิเวศทางทะเล ตลอดจนเป็นการสร้างจิตสำนึกที่ดีให้พนักงาน
                        </p>
                    </div>
                </div>

                <!-- Activity 2 -->
                <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
                    <div style="height: 250px; overflow: hidden;">
                        <img src="assets/รูปสังคม/saturday_lunch.png" alt="กิจกรรมเลี้ยงอาหารกลางวันพนักงาน" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    </div>
                    <div style="padding: 25px;">
                        <div style="color: var(--secondary); font-size: 14px; font-weight: 600; margin-bottom: 10px;">สวัสดิการพนักงาน</div>
                        <h3 style="color: var(--text-color); font-size: 20px; font-weight: 700; margin-top: 0; margin-bottom: 15px; line-height: 1.4;">เลี้ยงอาหารกลางวันพนักงานวันเสาร์</h3>
                        <p style="color: var(--text-muted); line-height: 1.6; margin: 0; font-size: 15px;">
                            กิจกรรมส่งเสริมความผูกพันอย่างต่อเนื่อง โดยการจัดเลี้ยงอาหารกลางวันพิเศษให้แก่พนักงานที่ปฏิบัติงานในวันเสาร์ เพื่อเป็นการแสดงความขอบคุณ สร้างความผ่อนคลาย และส่งเสริมความสัมพันธ์อันดี นำไปสู่ Happy Workplace
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Milestones Section -->"""

replacement_str = """    <!-- Milestones Section -->"""

if target_str in html:
    html = html.replace(target_str, replacement_str)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully removed News section from About UKEM.")
else:
    print("Target string not found!")
