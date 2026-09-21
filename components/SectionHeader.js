class SectionHeader extends HTMLElement {
    connectedCallback() {
        const title = this.getAttribute('title') || '';
        this.removeAttribute('title');
        const id = this.getAttribute('id') || '';
        
        this.innerHTML = `
            <h3 ${id ? `id="${id}"` : ''} class="section-header-icon">
                ${title}
            </h3>
        `;
    }
}
customElements.define('section-header', SectionHeader);
