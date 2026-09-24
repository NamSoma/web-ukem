import os

target_file = r"f:\Back up อีก HDD\งาน\ลองทำ\สังคม\การมีส่วนร่วมและพัฒนาชุมชน.html"

with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to insert a new project-card before the closing </div> of the project-grid.
# Let's find the third project card to append after it.
target_str = """                        <div class="project-content">
                            <h3>3. สนับสนุนกิจกรรม 7 วัน อันตราย ช่วงเทศกาลปีใหม่</h3>
                            <p><span style="white-space: nowrap;">บริษัทฯ</span> ตระหนักถึงความปลอดภัยในการเดินทางของประชาชนในช่วงเทศกาล จึงได้สนับสนุนสิ่งอุปโภคบริโภคที่จำเป็นให้แก่เจ้าหน้าที่เทศบาลตะเคียนเตี้ย ณ จุดบริการประชาชน เพื่ออำนวยความสะดวกและเสริมสร้างขวัญกำลังใจให้แก่เจ้าหน้าที่ในการปฏิบัติงานช่วง 7 วันอันตราย กิจกรรมนี้มุ่งหวังที่จะเป็นส่วนหนึ่งในการลดอุบัติเหตุและดูแลความปลอดภัยแก่ผู้สัญจรบนท้องถนน เพื่อให้ทุกคนเดินทางกลับภูมิลำเนาและท่องเที่ยวอย่างมีความสุขและปลอดภัย</p>
                            <div class="text-small" style="text-align: right; margin-top: 15px;  color: #6c757d;">
                                <span style="display: inline-flex; align-items: center; gap: 5px;">
                                    
                                    ปี 2568
                                </span>
                            </div>
                        </div>
                    </div>"""

replacement_str = target_str + """
                    
                    <div class="project-card">
                        <div class="project-img-wrapper">
                            <img src="../assets/รูปสังคม/crab_release.png" alt="กิจกรรมปล่อยปู">
                        </div>
                        <div class="project-content">
                            <h3>4. กิจกรรมเพื่อสังคม (CSR) ปล่อยปูม้าคืนสู่ธรรมชาติ</h3>
                            <p><span style="white-space: nowrap;">บริษัทฯ</span> ได้จัดกิจกรรมเพื่อสังคม (CSR) นำโดยผู้บริหารและพนักงาน ร่วมกันปล่อยปูม้าคืนสู่ธรรมชาติ ณ ศูนย์เรียนรู้ธนาคารสัตว์ทะเลเกาะสีชังโดยชุมชน เพื่อเป็นการอนุรักษ์ ฟื้นฟู และเพิ่มปริมาณสัตว์น้ำในระบบนิเวศทางทะเล ตลอดจนเป็นการสร้างจิตสำนึกที่ดีให้พนักงานในการร่วมกันดูแลรักษาสิ่งแวดล้อมและทรัพยากรธรรมชาติให้มีความอุดมสมบูรณ์และยั่งยืนต่อไป</p>
                            <div class="text-small" style="text-align: right; margin-top: 15px;  color: #6c757d;">
                                <span style="display: inline-flex; align-items: center; gap: 5px;">
                                    
                                    ปี 2568
                                </span>
                            </div>
                        </div>
                    </div>"""

if target_str in html:
    html = html.replace(target_str, replacement_str)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added crab release project.")
else:
    print("Target string not found!")
