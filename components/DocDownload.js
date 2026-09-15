class DocSection extends HTMLElement {
    connectedCallback() {
        // Prevent double rendering if already rendered
        if (this.hasAttribute('rendered')) return;
        this.setAttribute('rendered', 'true');

        const titleTh = this.getAttribute('title-th') || 'เอกสารดาวน์โหลดที่เกี่ยวข้อง';
        const titleEn = this.getAttribute('title-en') || 'Related Documents for Download';
        const lang = this.getAttribute('lang') || 'th';
        
        const title = lang === 'en' ? titleEn : titleTh;
        
        // Save children content
        const innerContent = this.innerHTML.trim();
        
        // Wrap children in doc-grid and add section-header
        this.innerHTML = `
            <section-header title="${title}"></section-header>
            <div class="doc-grid">
                ${innerContent}
            </div>
        `;
    }
}
customElements.define('doc-section', DocSection);

class DocCard extends HTMLElement {
    connectedCallback() {
        if (this.hasAttribute('rendered')) return;
        this.setAttribute('rendered', 'true');

        const title = this.getAttribute('title') || 'ชื่อเอกสารที่ (รออัปโหลด)';
        const url = this.getAttribute('url') || '#';
        const meta = this.getAttribute('meta') || 'PDF • - MB';
        
        const isPlaceholder = url === '#' || url === '';
        
        // Use text instead of arrow icon. Check language from parent doc-section if possible, 
        // but since doc-card doesn't have lang attribute directly, we can check document language or closest doc-section
        const lang = this.closest('doc-section')?.getAttribute('lang') || document.documentElement.lang || 'th';
        
        let downloadText = lang === 'en' ? 'Download' : 'ดาวน์โหลด';
        
        if (isPlaceholder) {
            downloadText = lang === 'en' ? 'Pending' : 'รออัปโหลด';
        }
        
        this.innerHTML = `
            <a href="${url}" target="_blank" class="doc-card">
                <div class="doc-icon">📄</div>
                <div class="doc-info">
                    <div class="doc-title">${title}</div>
                    <div class="doc-meta">${meta}</div>
                </div>
                <div class="doc-download" style="font-size: 14px; font-weight: 500; background: var(--primary); color: white; padding: 4px 12px; border-radius: 4px;">${downloadText}</div>
            </a>
        `;
    }
}
customElements.define('doc-card', DocCard);
