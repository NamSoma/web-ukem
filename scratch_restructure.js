const fs = require('fs');

const mapping = {
    "การกำกับดูแลและเศรษฐกิจ/นโยบายการกำกับดูแลกิจการ.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2022/06/1.-นโยบายกำกับดูแลกิจการที่ดี.pdf" title="นโยบายกำกับดูแลกิจการที่ดี" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2022/06/2.-จรรยาบรรณธุรกิจ.pdf" title="จรรยาบรรณธุรกิจ" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-02-นโยบายต่อต้านคอร์รัปชัน-26-2-68.pdf" title="นโยบายต่อต้านคอร์รัปชัน" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-02-คู่มือมาตรการต่อต้านคอร์รัปชัน-26-2-68.pdf" title="คู่มือมาตรการต่อต้านคอร์รัปชัน" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารกำกับดูแล/นโยบายการบัญชี_การเงิน_ภาษี_และงบประมาณ.pdf" title="นโยบายการบัญชี การเงิน ภาษี และงบประมาณ (ฉบับปี 2567)" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "การกำกับดูแลและเศรษฐกิจ/การบริหารจัดการความเสี่ยง.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารกำกับดูแล/นโยบายบริหารความเสี่ยง.pdf" title="นโยบายบริหารความเสี่ยง (ฉบับปี 2565)" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/03/กฎบัตรคณะกรรมการบริหารความเสี่ยง.pdf" title="กฎบัตรคณะกรรมการบริหารความเสี่ยง" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2024/05/RiskManagementTH.pdf" title="คู่มือการบริหารความเสี่ยง" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/1.-โครงสร้างองค์กรBoard-Skill-Matrix-2569-Th.-ผสาน.pdf" title="โครงสร้างองค์กรและ Board Skill Matrix" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-1-แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ-26-2-68.pdf" title="แนวทางปฏิบัติสำหรับคณะกรรมการตรวจสอบ" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2025/05/ฉบับที่-2-กฎบัตรคณะกรรมการตรวจสอบ-14-11-67.pdf" title="กฎบัตรคณะกรรมการตรวจสอบ" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "สิ่งแวดล้อม/การบริหารจัดการสิ่งแวดล้อม.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสิ่งแวดล้อม/นโยบายการจัดการสิ่งแวดล้อม การป้องกันมลพิษ และการใช้ทรัพยากรอย่างมีประสิทธิภาพ.pdf" title="นโยบายการจัดการสิ่งแวดล้อม การป้องกันมลพิษ และการใช้ทรัพยากรอย่างมีประสิทธิภาพ" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสิ่งแวดล้อม/นโยบายความหลากหลายทางชีวภาพ 2569.pdf" title="นโยบายความหลากหลายทางชีวภาพ 2569" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "สิ่งแวดล้อม/การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสิ่งแวดล้อม/นโยบายการเปลี่ยนแปลงสภาพภูมิอากาศและการลดการปล่อยคาร์บอน.pdf" title="นโยบายการเปลี่ยนแปลงสภาพภูมิอากาศและการลดการปล่อยคาร์บอน" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "สังคม/สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสังคม/นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฎิบัติ.pdf" title="นโยบายแรงงาน สิทธิมนุษยชน และการไม่เลือกปฏิบัติ" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสังคม/บันทึกตรวจสอบและรับรองข้อมูลสัดส่วนผู้หญิงในตำแหน่งบริหาร.pdf" title="บันทึกตรวจสอบและรับรองข้อมูลสัดส่วนผู้หญิงในตำแหน่งบริหาร ประจำปี 2569" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารสังคม/บันทึกผลการตรวจสอบแรงงานข้ามชาติ.pdf" title="บันทึกผลการตรวจสอบแรงงานข้ามชาติ ประจำปี 2569" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "สังคม/ความรับผิดชอบต่อลูกค้าและคู่ค้า.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน.pdf" title="นโยบายจัดซื้อจัดจ้างอย่างยั่งยืน" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2026/06/PDPA.pdf" title="นโยบายคุ้มครองข้อมูลส่วนบุคคล (PDPA)" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="https://www.unionpetrochemical.com/wp-content/uploads/2021/12/Take-down-Complaint-Form.pdf" title="Take Down Notice & Complaint" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`,
    "ภาพรวมความยั่งยืน/การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html": `
    <section style="padding: 40px 0; background-color: var(--bg-light);">
        <div class="container">
            <h2 class="section-title">เอกสารดาวน์โหลด</h2>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารภาพรวมความยั่งยืน/ประกาศแต่งตั้งคณะทำงานการพัฒนาอย่างยั่งยืน.pdf" title="ประกาศ เรื่อง แต่งตั้งคณะทำงานการพัฒนาอย่างยั่งยืน" meta="PDF"></doc-card>
            </div>
            <div style="margin-bottom: 15px;">
                <doc-card url="../assets/เอกสารภาพรวมความยั่งยืน/ประกาศแก้ไขเพิ่มเติมขอบเขตอำนาจหน้าที่ของคณะทำงานการพัฒนาอย่างยั่งยืน.pdf" title="ประกาศ เรื่อง แก้ไขเพิ่มเติมขอบเขตอำนาจหน้าที่ของคณะทำงานการพัฒนาอย่างยั่งยืน" meta="PDF"></doc-card>
            </div>
        </div>
    </section>
`
};

for (const [filePath, injection] of Object.entries(mapping)) {
    if (fs.existsSync(filePath)) {
        let content = fs.readFileSync(filePath, 'utf8');
        if (!content.includes('เอกสารดาวน์โหลด')) {
            content = content.replace('</main>', injection + '\n    </main>');
            fs.writeFileSync(filePath, content, 'utf8');
            console.log('Updated ' + filePath);
        } else {
            console.log('Skipped ' + filePath);
        }
    } else {
        console.log('Warning: Not found ' + filePath);
    }
}

const dlFile = "ศูนย์รวมการดาวน์โหลด.html";
if (fs.existsSync(dlFile)) {
    let dlContent = fs.readFileSync(dlFile, 'utf8');
    const newDlHtml = `<div class="download-list">
    <div>
        <h2 class="section-label" style="margin-top: 20px;">รายงานและการดำเนินการด้าน ESG</h2>
    </div>
    <div style="margin-bottom: 15px;">
        <doc-card 
            url="assets/เอกสารภาพรวมความยั่งยืน/ESG_Report_2025.pdf" 
            title="รายงานผลการดำเนินงานด้าน ESG ประจำปี 2568" 
            meta="PDF">
        </doc-card>
    </div>
    <div style="margin-bottom: 15px;">
        <doc-card 
            url="ukem-or-2025-th.pdf" 
            title="แบบแสดงรายการข้อมูลประจำปี (One Report) 2568" 
            meta="PDF">
        </doc-card>
    </div>
    <div style="margin-bottom: 15px;">
        <doc-card 
            url="assets/เอกสารกำกับดูแล/ESG_Report_2025_Governance.pdf" 
            title="รายงาน ESG ประจำปี 2568 (หมวดกำกับดูแลกิจการ)" 
            meta="PDF">
        </doc-card>
    </div>
    <div style="margin-bottom: 15px;">
        <doc-card 
            url="assets/เอกสารสังคม/ESG_Report_2025_Social.pdf" 
            title="รายงาน ESG ประจำปี 2568 (หมวดสังคม)" 
            meta="PDF">
        </doc-card>
    </div>
    <div style="margin-bottom: 15px;">
        <doc-card 
            url="assets/เอกสารสิ่งแวดล้อม/ESG_Report_2025_Environment.pdf" 
            title="รายงาน ESG ประจำปี 2568 (หมวดสิ่งแวดล้อม)" 
            meta="PDF">
        </doc-card>
    </div>
</div>`;

    dlContent = dlContent.replace(/<div class="download-list">[\s\S]*?(?=<\/div>\s*<\/main>)/, newDlHtml);
    fs.writeFileSync(dlFile, dlContent, 'utf8');
    console.log('Updated ' + dlFile);
}
