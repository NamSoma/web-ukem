class StakeholderCard extends HTMLElement {
    connectedCallback() {
        const title = this.getAttribute('title') || 'Stakeholder';
        
        // Extract content from slots BEFORE overwriting innerHTML
        const col1Content = this.querySelector('[slot="col1"]')?.innerHTML.trim() || '';
        const col2Content = this.querySelector('[slot="col2"]')?.innerHTML.trim() || '';
        const col3Content = this.querySelector('[slot="col3"]')?.innerHTML.trim() || '';
        
        // Determine language
        const lang = document.documentElement.lang || 'th';
        
        // Column headers (allow overriding via attributes, fallback to stakeholder defaults)
        const col1Title = this.hasAttribute('col1-title') ? this.getAttribute('col1-title') : (lang === 'en' ? 'Engagement Channels' : 'ช่องทางการมีส่วนร่วม');
        const col2Title = this.hasAttribute('col2-title') ? this.getAttribute('col2-title') : (lang === 'en' ? 'Stakeholder Issues' : 'ประเด็นผู้มีส่วนได้เสีย');
        const col3Title = this.hasAttribute('col3-title') ? this.getAttribute('col3-title') : (lang === 'en' ? 'Related Sustainability Issues' : 'ประเด็นการพัฒนาที่ยั่งยืนที่เกี่ยวข้อง');
        
        // Count active columns
        let colCount = 0;
        if (col1Content) colCount++;
        if (col2Content) colCount++;
        if (col3Content) colCount++;
        
        let colsHtml = '';
        if (col1Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col1Title ? `<h5 class="sh-col-title">${col1Title}</h5>` : ''}
                    <div class="sh-col-content">${col1Content}</div>
                </div>
            `;
        }
        if (col2Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col2Title ? `<h5 class="sh-col-title">${col2Title}</h5>` : ''}
                    <div class="sh-col-content">${col2Content}</div>
                </div>
            `;
        }
        if (col3Content) {
            colsHtml += `
                <div class="sh-col">
                    ${col3Title ? `<h5 class="sh-col-title">${col3Title}</h5>` : ''}
                    <div class="sh-col-content">${col3Content}</div>
                </div>
            `;
        }

        this.innerHTML = `
            <div class="sh-row">
                <div class="sh-title-col" ${this.hasAttribute('title-width') ? `style="flex: 0 0 ${this.getAttribute('title-width')}%;"` : ''}>
                    <h4 class="sh-title">${title}</h4>
                </div>
                <div class="sh-content-col" ${this.hasAttribute('title-width') ? `style="flex: 0 0 ${100 - parseInt(this.getAttribute('title-width'))}%;"` : ''}>
                    <div class="sh-grid sh-grid-${colCount}">
                        ${colsHtml}
                    </div>
                </div>
            </div>
        `;
    }
}

customElements.define('stakeholder-card', StakeholderCard);
