import os

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated " + filepath)
    else:
        print("Not found in " + filepath)

th_old = "บริษัท ยูเนี่ยน ปิโตรเคมีคอล จำกัด (มหาชน) ได้เข้าร่วมพิธีบำเพ็ญกุศล ณ วัดปากน้ำ ภาษีเจริญ เพื่อความเป็นสิริมงคลและส่งเสริมพระพุทธศาสนา"
th_new = "เมื่อวันที่ 3 ตุลาคม 2569 ผู้บริหารและตัวแทนบริษัทฯ เข้าร่วมพิธีบำเพ็ญกุศล เนื่องในวันวิปัสสนาจารย์และอดีตธรรมกาย และวันคล้ายวันมรณกรรมครบ 1 ปี อาจารย์ตรีธา เนียมขำ ณ พระมหาเจดีย์มหารัชมงคล วัดปากน้ำ เขตภาษีเจริญ กรุงเทพมหานคร เพื่อร่วมแสดงความรำลึกและสืบสานกิจกรรมอันเป็นกุศล"

en_old = "Union Petrochemical Public Company Limited attended a merit-making ceremony at Wat Paknam Bhasicharoen to promote auspiciousness and support Buddhism."
en_new = "On October 3, 2026, executives and representatives of the Company attended a merit-making ceremony on the occasion of Vipassana Acharya and Former Dhammakaya Day, and the 1st anniversary of the passing of Ajahn Tritha Niamkham at the Maha Ratchamongkol Great Stupa, Wat Paknam Bhasicharoen, Bangkok, to commemorate and continue charitable activities."

replace_in_file('ข่าวสารและกิจกรรม.html', th_old, th_new)
replace_in_file('en/ข่าวสารและกิจกรรม.html', en_old, en_new)
