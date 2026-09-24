import os

target_file = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html"

with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

target_str = """            <section-header title="การสร้างความผูกพันกับพนักงาน"></section-header>
            <div class="intro-text">
                <div  style="margin-bottom: 20px;">
                    <p style="margin: 0; color: var(--text-muted); line-height: 1.7;">
                        <strong class="skimmable-bold">พนักงานคือทรัพยากรที่มีค่าสูงสุด:</strong> ความผูกพันของพนักงาน (Employee Engagement) ช่วยเสริมสร้างประสิทธิภาพในการดำเนินงาน ความมั่นคง และการเติบโตอย่างยั่งยืน
                    </p>
                </div>
            </div>"""

replacement_str = target_str + """

            <style>
                .engagement-card {
                    background: var(--white);
                    border: 1px solid var(--border-color);
                    border-radius: 0px;
                    overflow: hidden;
                    display: flex;
                    flex-direction: row;
                    margin-bottom: 40px;
                }
                .engagement-img {
                    flex: 0 0 400px;
                    height: 280px;
                }
                .engagement-img img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }
                .engagement-content {
                    padding: 30px;
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
                @media (max-width: 768px) {
                    .engagement-card {
                        flex-direction: column;
                    }
                    .engagement-img {
                        flex: auto;
                        height: 250px;
                    }
                }
            </style>
            
            <div class="engagement-card">
                <div class="engagement-img">
                    <img src="../assets/รูปสังคม/saturday_lunch.png" alt="กิจกรรมเลี้ยงอาหารกลางวันพนักงาน">
                </div>
                <div class="engagement-content">
                    <h3 style="color: var(--primary); font-size: 20px; font-weight: 700; margin-top: 0; margin-bottom: 15px;">สวัสดิการและกิจกรรม: เลี้ยงอาหารกลางวันพนักงาน</h3>
                    <p style="color: var(--text-muted); line-height: 1.7; margin: 0;">
                        <span style="white-space: nowrap;">บริษัทฯ</span> ให้ความสำคัญกับขวัญกำลังใจของบุคลากร โดยจัดให้มีสวัสดิการและกิจกรรมส่งเสริมความผูกพันอย่างต่อเนื่อง เช่น การจัดเลี้ยงอาหารกลางวันพิเศษให้แก่พนักงานที่เสียสละมาปฏิบัติงานในวันเสาร์ เพื่อเป็นการแสดงความขอบคุณ สร้างความผ่อนคลาย และส่งเสริมความสัมพันธ์อันดีระหว่างเพื่อนร่วมงาน นำไปสู่บรรยากาศการทำงานที่มีความสุข (Happy Workplace)
                    </p>
                </div>
            </div>"""

if target_str in html:
    html = html.replace(target_str, replacement_str)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added saturday lunch activity.")
else:
    print("Target string not found!")
