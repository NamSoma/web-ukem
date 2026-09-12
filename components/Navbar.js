class MainNav extends HTMLElement {
    connectedCallback() {
        const depth = this.getAttribute('depth') || '';
        const prefix = depth === '1' ? '../' : '';

        this.innerHTML = `
            <nav class="main-nav">
                <a href="${prefix}index.html" class="nav-logo">
                    <img src="${prefix}components/union-logo.png" alt="UKEM Sustainability">
                </a>
                
                <div class="nav-links">
                    <a href="${prefix}index.html" class="dropdown">หน้าแรก</a>
                    <a href="https://www.unionpetrochemical.com/th/" target="_blank" class="dropdown">กลับไปที่เว็บไซต์หลัก</a>
                    
                    <div class="dropdown">
                        ภาพรวมความยั่งยืน
                        <div class="dropdown-content">
                            <a href="${prefix}ภาพรวมความยั่งยืน/สารจากประธานกรรมการบริษัท.html">สารจากประธานกรรมการบริษัท</a>
                            <a href="${prefix}ภาพรวมความยั่งยืน/การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html">การขับเคลื่อนธุรกิจเพื่อความยั่งยืน</a>
                            <a href="${prefix}ภาพรวมความยั่งยืน/ห่วงโซ่คุณค่าของธุรกิจ.html">ห่วงโซ่คุณค่าของธุรกิจ</a>
                            <a href="${prefix}ภาพรวมความยั่งยืน/การประเมินประเด็นด้านความยั่งยืนที่สำคัญ.html">การประเมินประเด็นด้านความยั่งยืนที่สำคัญ</a>
                        </div>
                    </div>

                    <div class="dropdown">
                        สิ่งแวดล้อม
                        <div class="dropdown-content">
                            <a href="${prefix}สิ่งแวดล้อม/การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html">การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ</a>
                            <a href="${prefix}สิ่งแวดล้อม/การบริหารจัดการสิ่งแวดล้อม.html">การบริหารจัดการสิ่งแวดล้อม</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        สังคม
                        <div class="dropdown-content">
                            <a href="${prefix}สังคม/นโยบายและการปฏิบัติด้านสังคม.html">นโยบายและการปฏิบัติด้านสังคม</a>
                            <a href="${prefix}สังคม/สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html">สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน</a>
                            <a href="${prefix}สังคม/อาชีวอนามัยและความปลอดภัย.html">อาชีวอนามัยและความปลอดภัย</a>
                            <a href="${prefix}สังคม/ความรับผิดชอบต่อลูกค้าและคู่ค้า.html">ความรับผิดชอบต่อลูกค้าและคู่ค้า</a>
                            <a href="${prefix}สังคม/การมีส่วนร่วมและพัฒนาชุมชน.html">การมีส่วนร่วมและพัฒนาชุมชน</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        การกำกับดูแล
                        <div class="dropdown-content">
                            <a href="${prefix}การกำกับดูแลและเศรษฐกิจ/นโยบายการกำกับดูแลกิจการ.html">นโยบายการกำกับดูแลกิจการ</a>
                            <a href="${prefix}การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html">โครงสร้างการกำกับดูแลกิจการ</a>
                            <a href="${prefix}การกำกับดูแลและเศรษฐกิจ/การบริหารจัดการความเสี่ยง.html">การบริหารจัดการความเสี่ยง</a>
                            <a href="${prefix}การกำกับดูแลและเศรษฐกิจ/การควบคุมภายใน.html">การควบคุมภายใน</a>
                            <a href="${prefix}การกำกับดูแลและเศรษฐกิจ/ข้อมูลทางการเงิน.html">ข้อมูลทางการเงิน</a>
                        </div>
                    </div>
                    <a href="${prefix}รางวัลและความสำเร็จ.html" class="dropdown">รางวัลและความสำเร็จ</a>
                    <!-- <a href="${prefix}ศูนย์รวมการดาวน์โหลด.html" class="dropdown">ศูนย์รวมการดาวน์โหลด</a> -->

                </div>
            </nav>
        `;

        const dropdowns = this.querySelectorAll('.dropdown');
        
        dropdowns.forEach(dropdown => {
            const content = dropdown.querySelector('.dropdown-content');
            if (content) {
                dropdown.addEventListener('click', (e) => {
                    e.stopPropagation(); // prevent document click from closing it immediately
                        
                    // close all other dropdowns
                    dropdowns.forEach(d => {
                        if (d !== dropdown) d.classList.remove('active');
                    });
                    
                    dropdown.classList.toggle('active');
                });
            }
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', () => {
            dropdowns.forEach(d => d.classList.remove('active'));
        });
    }
}

customElements.define('main-nav', MainNav);
