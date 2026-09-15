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
            <section-header title="${title}" style="margin-top: 60px;"></section-header>
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
        const downloadIcon = isPlaceholder ? '⬇️' : '⬇️';
        
        this.innerHTML = `
            <a href="${url}" target="_blank" class="doc-card">
                <div class="doc-icon">📄</div>
                <div class="doc-info">
                    <div class="doc-title">${title}</div>
                    <div class="doc-meta">${meta}</div>
                </div>
                <div class="doc-download">${downloadIcon}</div>
            </a>
        `;
    }
}
customElements.define('doc-card', DocCard);
