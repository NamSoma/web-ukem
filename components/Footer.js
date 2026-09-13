class MainFooter extends HTMLElement {
    connectedCallback() {
        const depthAttr = this.getAttribute('depth') || '';
        const depth = depthAttr === '' ? 0 : parseInt(depthAttr);
        let prefix = '';
        for(let i=0; i<depth; i++) {
            prefix += '../';
        }
        const lang = this.getAttribute('lang') || 'th';
        const isEn = lang === 'en';
        
        // Base paths for links
        const linkBase = isEn ? prefix + 'en/' : prefix;

        // Texts
        const t = {
            companyName: isEn ? "Union Petrochemical Public Company Limited" : "บริษัท ยูเนี่ยน ปิโตรเคมีคอล จำกัด (มหาชน)",
            address: isEn ? "728 Union House Bldg., Borommaratchachonnani Rd., Bangbamru, Bangplad, Bangkok 10700" : "728 อาคาร ยูเนี่ยนเฮ้าส์ ถนนบรมราชชนนี แขวงบางบำหรุ เขตบางพลัด กรุงเทพฯ 10700",
            phone: isEn ? "Phone :" : "โทรศัพท์ :",
            fax: isEn ? "Fax :" : "แฟกซ์ :",
            email: isEn ? "Email :" : "อีเมล :",
            overview: isEn ? "Sustainability Overview" : "ภาพรวมความยั่งยืน",
            env: isEn ? "Environment" : "สิ่งแวดล้อม",
            social: isEn ? "Social" : "สังคม",
            gov: isEn ? "Governance" : "การกำกับดูแล",
            awards: isEn ? "Awards and Successes" : "รางวัลและความสำเร็จ",
        };

        this.innerHTML = `
            <style>
                .footer-wrapper {
                    display: flex; flex-direction: column; margin-top: 60px; font-family: 'Sarabun', sans-serif;
                }
                .footer-main {
                    display: flex; flex-wrap: wrap; width: 100%;
                }
                .footer-col-left {
                    flex: 1 1 50%;
                    background-color: var(--primary);
                    padding: 60px 20px;
                    display: flex;
                    justify-content: flex-end;
                    min-width: 320px;
                    box-sizing: border-box;
                }
                .footer-col-right {
                    flex: 1 1 50%;
                    background-color: #f1f5f9;
                    padding: 60px 20px;
                    display: flex;
                    justify-content: flex-start;
                    min-width: 320px;
                    box-sizing: border-box;
                }
                .footer-inner-left {
                    width: 100%;
                    max-width: 580px;
                    color: white;
                }
                .footer-inner-right {
                    width: 100%;
                    max-width: 580px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                }
                .footer-bottom {
                    background-color: var(--primary);
                    color: rgba(255,255,255,0.9);
                    border-top: 1px solid rgba(255,255,255,0.2);
                }
                .footer-bottom-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 15px 20px;
                    display: flex;
                    justify-content: space-between;
                    flex-wrap: wrap;
                    gap: 15px;
                    font-size: 13px;
                }
                @media (max-width: 800px) {
                    .footer-col-left, .footer-col-right {
                        justify-content: center;
                    }
                    .footer-inner-left {
                        max-width: 100%;
                    }
                }
            </style>
            <footer class="footer-wrapper">
                <div class="footer-main">
                    
                    <!-- Left Column: Address -->
                    <div class="footer-col-left">
                        <div class="footer-inner-left">
                            <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 20px; margin-top: 0; color: white;">${t.companyName}</h3>
                            <p style="margin-bottom: 12px; font-size: 16px;">${t.address}</p>
                            <p style="margin-bottom: 12px; font-size: 16px;"><strong>${t.phone}</strong> 02-881-8288</p>
                            <p style="margin-bottom: 12px; font-size: 16px;"><strong>${t.fax}</strong> 02-433-7243</p>
                            <p style="margin-bottom: 0; font-size: 16px;"><strong>${t.email}</strong> inquiry@unionpetrochemical.com</p>
                        </div>
                    </div>
                    
                    <!-- Right Column: QR Code -->
                    <div class="footer-col-right">
                        <div class="footer-inner-right">
                            <div style="background-color: white; padding: 15px; border-radius: 0px; margin-bottom: 20px; border: 1px solid #e5e7eb; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                                <!-- Generated QR Code for @UnionUPC -->
                                <img src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=https://line.me/R/ti/p/%40unionupc" alt="LINE QR Code" style="width: 160px; height: 160px; object-fit: contain; display: block;" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg'">
                            </div>
                            <p style="color: #64748b; font-size: 16px; margin: 0; font-weight: 500;">LINE Official Account : @UnionUPC</p>
                        </div>
                    </div>
                </div>
                
                <!-- Bottom Bar -->
                <div class="footer-bottom">
                    <div class="footer-bottom-container">
                        <div>
                            Copyright © 2021 Union Petrochemical All rights reserved.
                        </div>
                        <div style="text-align: right;">
                            <a href="${linkBase}ภาพรวมความยั่งยืน/สารจากประธานกรรมการบริษัท.html" style="color: rgba(255,255,255,0.9); text-decoration: none; margin: 0 5px; transition: 0.3s;" onmouseover="this.style.color='var(--secondary)'" onmouseout="this.style.color='rgba(255,255,255,0.9)'">${t.overview}</a> | 
                            <a href="${linkBase}สิ่งแวดล้อม/การบริหารจัดการสิ่งแวดล้อม.html" style="color: rgba(255,255,255,0.9); text-decoration: none; margin: 0 5px; transition: 0.3s;" onmouseover="this.style.color='var(--secondary)'" onmouseout="this.style.color='rgba(255,255,255,0.9)'">${t.env}</a> | 
                            <a href="${linkBase}สังคม/นโยบายและการปฏิบัติด้านสังคม.html" style="color: rgba(255,255,255,0.9); text-decoration: none; margin: 0 5px; transition: 0.3s;" onmouseover="this.style.color='var(--secondary)'" onmouseout="this.style.color='rgba(255,255,255,0.9)'">${t.social}</a> | 
                            <a href="${linkBase}การกำกับดูแลและเศรษฐกิจ/นโยบายการกำกับดูแลกิจการ.html" style="color: rgba(255,255,255,0.9); text-decoration: none; margin: 0 5px; transition: 0.3s;" onmouseover="this.style.color='var(--secondary)'" onmouseout="this.style.color='rgba(255,255,255,0.9)'">${t.gov}</a> | 
                            <a href="${linkBase}รางวัลและความสำเร็จ.html" style="color: rgba(255,255,255,0.9); text-decoration: none; margin: 0 5px; transition: 0.3s;" onmouseover="this.style.color='var(--secondary)'" onmouseout="this.style.color='rgba(255,255,255,0.9)'">${t.awards}</a>
                        </div>
                    </div>
                </div>
            </footer>
        `;
    }
}

customElements.define('main-footer', MainFooter);
