import os

def insert_news(filepath, new_block):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target_str = '<div class="news-grid">'
    if target_str in content:
        parts = content.split(target_str, 1)
        new_content = parts[0] + target_str + '\n' + new_block + '\n' + parts[1]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"Could not find news-grid in {filepath}")

th_block = """                <!-- New Activity -->
                <div class="news-card" data-category="csr">
                    <div class="news-img">
                        <img src="images/ร่วมพิธีบำเพ็ญกุศล_วัดปากน้ำ.jpg" alt="ร่วมพิธีบำเพ็ญกุศล ณ วัดปากน้ำ ภาษีเจริญ">
                    </div>
                    <div class="news-content">
                        <div class="news-category csr">กิจกรรมเพื่อสังคม (CSR)</div>
                        <h3 class="news-title">ร่วมพิธีบำเพ็ญกุศล ณ วัดปากน้ำ ภาษีเจริญ</h3>
                        <p class="news-desc">
                            บริษัท ยูเนี่ยน ปิโตรเคมีคอล จำกัด (มหาชน) ได้เข้าร่วมพิธีบำเพ็ญกุศล ณ วัดปากน้ำ ภาษีเจริญ เพื่อความเป็นสิริมงคลและส่งเสริมพระพุทธศาสนา
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">ปี 2569</div>
                    </div>
                </div>"""

en_block = """                <!-- New Activity -->
                <div class="news-card" data-category="csr">
                    <div class="news-img">
                        <img src="../images/ร่วมพิธีบำเพ็ญกุศล_วัดปากน้ำ.jpg" alt="Attended a merit-making ceremony at Wat Paknam Bhasicharoen">
                    </div>
                    <div class="news-content">
                        <div class="news-category csr">CSR</div>
                        <h3 class="news-title">Attended a merit-making ceremony at Wat Paknam Bhasicharoen</h3>
                        <p class="news-desc">
                            Union Petrochemical Public Company Limited attended a merit-making ceremony at Wat Paknam Bhasicharoen to promote auspiciousness and support Buddhism.
                        </p>
                        <div style="margin-top: 20px; font-size: 14px; color: #888;">2026</div>
                    </div>
                </div>"""

insert_news('ข่าวสารและกิจกรรม.html', th_block)
insert_news('en/ข่าวสารและกิจกรรม.html', en_block)
