class MainNav extends HTMLElement {
    connectedCallback() {
        const depthAttr = this.getAttribute('depth') || '';
        const depth = depthAttr === '' ? 0 : parseInt(depthAttr);
        const lang = this.getAttribute('lang') || 'th';
        const currentPath = this.getAttribute('path') || 'index.html';
        
        let prefix = '';
        for(let i=0; i<depth; i++) {
            prefix += '../';
        }

        const isEn = lang === 'en';
        const linkBase = isEn ? prefix + 'en/' : prefix;
        
        const thUrl = prefix + currentPath;
        const enUrl = prefix + 'en/' + currentPath;

        const navHtml = isEn ? this.getEnNav(linkBase, thUrl, enUrl, prefix) : this.getThNav(linkBase, thUrl, enUrl, prefix);
        
        this.innerHTML = navHtml;

        const dropdowns = this.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            const content = dropdown.querySelector('.dropdown-content');
            if (content) {
                dropdown.addEventListener('click', (e) => {
                    e.stopPropagation();
                    dropdowns.forEach(d => {
                        if (d !== dropdown) d.classList.remove('active');
                    });
                    dropdown.classList.toggle('active');
                });
            }
        });

        document.addEventListener('click', () => {
            dropdowns.forEach(d => d.classList.remove('active'));
        });

        // Theme Toggle Logic
        const themeToggle = this.querySelector('#theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => {
                const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                themeToggle.textContent = newTheme === 'light' ? '🌙' : '☀️';
            });
        }
    }

    getThNav(linkBase, thUrl, enUrl, prefix) {
        return `
            <nav class="main-nav">
                <a href="${linkBase}index.html" class="nav-logo">
                    <img src="${prefix}components/union-logo.png" alt="UKEM Sustainability">
                </a>
                
                <div class="nav-links">
                    <a href="${linkBase}index.html" class="dropdown">หน้าแรก</a>
                    <a href="https://www.unionpetrochemical.com/th/" target="_blank" class="dropdown">กลับไปที่เว็บไซต์หลัก</a>
                    
                    <div class="dropdown">
                        ภาพรวมความยั่งยืน
                        <div class="dropdown-content">
                            <a href="${linkBase}ภาพรวมความยั่งยืน/สารจากประธานกรรมการบริษัท.html">สารจากประธานกรรมการบริษัท</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html">การขับเคลื่อนธุรกิจเพื่อความยั่งยืน</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/ห่วงโซ่คุณค่าของธุรกิจ.html">ห่วงโซ่คุณค่าของธุรกิจ</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/การประเมินประเด็นด้านความยั่งยืนที่สำคัญ.html">การประเมินประเด็นด้านความยั่งยืนที่สำคัญ</a>
                        </div>
                    </div>

                    <div class="dropdown">
                        สิ่งแวดล้อม
                        <div class="dropdown-content">
                            <a href="${linkBase}สิ่งแวดล้อม/การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html">การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ</a>
                            <a href="${linkBase}สิ่งแวดล้อม/การบริหารจัดการสิ่งแวดล้อม.html">การบริหารจัดการสิ่งแวดล้อม</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        สังคม
                        <div class="dropdown-content">
                            <a href="${linkBase}สังคม/นโยบายและการปฏิบัติด้านสังคม.html">นโยบายและการปฏิบัติด้านสังคม</a>
                            <a href="${linkBase}สังคม/สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html">สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน</a>
                            <a href="${linkBase}สังคม/อาชีวอนามัยและความปลอดภัย.html">อาชีวอนามัยและความปลอดภัย</a>
                            <a href="${linkBase}สังคม/ความรับผิดชอบต่อลูกค้าและคู่ค้า.html">ความรับผิดชอบต่อลูกค้าและคู่ค้า</a>
                            <a href="${linkBase}สังคม/การมีส่วนร่วมและพัฒนาชุมชน.html">กิจกรรมเพื่อสังคมและการมีส่วนร่วมในชุมชน</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        การกำกับดูแล
                        <div class="dropdown-content">
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/นโยบายการกำกับดูแลกิจการ.html">นโยบายการกำกับดูแลกิจการ</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html">โครงสร้างการกำกับดูแลกิจการ</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/การบริหารจัดการความเสี่ยง.html">การบริหารจัดการความเสี่ยง</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/การควบคุมภายใน.html">การควบคุมภายใน</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/ข้อมูลทางการเงิน.html">ข้อมูลทางการเงิน</a>
                        </div>
                    </div>
                    <a href="${linkBase}รางวัลและความสำเร็จ.html" class="dropdown">รางวัลและความสำเร็จ</a>
                </div>

                <div class="lang-switcher" style="display: flex; gap: 10px; align-items: center; margin-left: 20px; font-weight: bold;">
                    <button id="theme-toggle" style="background: none; border: none; cursor: pointer; font-size: 1.2rem; margin-right: 10px;" title="Toggle Dark Mode">
                        ${document.documentElement.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙'}
                    </button>
                    <a href="${thUrl}" style="color: var(--primary); text-decoration: none;">TH</a>
                    <span style="color: #ccc;">|</span>
                    <a href="${enUrl}" style="color: var(--text-muted); text-decoration: none;">EN</a>
                </div>
            </nav>
        `;
    }

    getEnNav(linkBase, thUrl, enUrl, prefix) {
        return `
            <nav class="main-nav">
                <a href="${linkBase}index.html" class="nav-logo">
                    <img src="${prefix}components/union-logo.png" alt="UKEM Sustainability">
                </a>
                
                <div class="nav-links">
                    <a href="${linkBase}index.html" class="dropdown">Home</a>
                    <a href="https://www.unionpetrochemical.com/en/" target="_blank" class="dropdown">Back to Main Website</a>
                    
                    <div class="dropdown">
                        Sustainability Overview
                        <div class="dropdown-content">
                            <a href="${linkBase}ภาพรวมความยั่งยืน/สารจากประธานกรรมการบริษัท.html">Message from Chairman</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/การขับเคลื่อนธุรกิจเพื่อความยั่งยืน.html">Sustainability Strategy</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/ห่วงโซ่คุณค่าของธุรกิจ.html">Value Chain</a>
                            <a href="${linkBase}ภาพรวมความยั่งยืน/การประเมินประเด็นด้านความยั่งยืนที่สำคัญ.html">Materiality Assessment</a>
                        </div>
                    </div>

                    <div class="dropdown">
                        Environment
                        <div class="dropdown-content">
                            <a href="${linkBase}สิ่งแวดล้อม/การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html">Energy & Climate Change</a>
                            <a href="${linkBase}สิ่งแวดล้อม/การบริหารจัดการสิ่งแวดล้อม.html">Environmental Management</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        Social
                        <div class="dropdown-content">
                            <a href="${linkBase}สังคม/นโยบายและการปฏิบัติด้านสังคม.html">Social Policies & Practices</a>
                            <a href="${linkBase}สังคม/สิทธิมนุษยชนและการปฏิบัติต่อแรงงาน.html">Human Rights & Labor Practices</a>
                            <a href="${linkBase}สังคม/อาชีวอนามัยและความปลอดภัย.html">Occupational Health & Safety</a>
                            <a href="${linkBase}สังคม/ความรับผิดชอบต่อลูกค้าและคู่ค้า.html">Responsibility to Customers & Partners</a>
                            <a href="${linkBase}สังคม/การมีส่วนร่วมและพัฒนาชุมชน.html">CSR & Community Engagement</a>
                        </div>
                    </div>
                    <div class="dropdown">
                        Governance
                        <div class="dropdown-content">
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/นโยบายการกำกับดูแลกิจการ.html">Corporate Governance Policy</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/โครงสร้างการกำกับดูแลกิจการ.html">Governance Structure</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/การบริหารจัดการความเสี่ยง.html">Risk Management</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/การควบคุมภายใน.html">Internal Control</a>
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/ข้อมูลทางการเงิน.html">Financial Information</a>
                        </div>
                    </div>
                    <a href="${linkBase}รางวัลและความสำเร็จ.html" class="dropdown">Awards & Successes</a>
                </div>

                <div class="lang-switcher" style="display: flex; gap: 10px; align-items: center; margin-left: 20px; font-weight: bold;">
                    <button id="theme-toggle" style="background: none; border: none; cursor: pointer; font-size: 1.2rem; margin-right: 10px;" title="Toggle Dark Mode">
                        ${document.documentElement.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙'}
                    </button>
                    <a href="${thUrl}" style="color: var(--text-muted); text-decoration: none;">TH</a>
                    <span style="color: #ccc;">|</span>
                    <a href="${enUrl}" style="color: var(--primary); text-decoration: none;">EN</a>
                </div>
            </nav>
        `;
    }
}

customElements.define('main-nav', MainNav);
