class FooterNote extends HTMLElement {
    constructor() {
        super();
        const textContent = this.innerHTML;
        this.innerHTML = '';
        
        const shadow = this.attachShadow({ mode: 'open' });
        
        const style = document.createElement('style');
        style.textContent = `
            .footer-note {
                margin-top: 40px;
                padding: 20px;
                background: var(--bg-light, #f8fafc); 
                border: 1px dashed rgba(76, 175, 80, 0.4);
                text-align: center;
                font-size: 18px;
                color: var(--text-muted, #64748b);
                font-family: inherit;
                line-height: 1.6;
            }
            .footer-note ::slotted(a) {
                color: var(--primary, #1e3a8a);
                font-weight: 600;
                text-decoration: underline;
            }
            /* Dark mode adaptation if variables are not passed through correctly */
            @media (prefers-color-scheme: dark) {
                :host-context([data-theme="dark"]) .footer-note {
                    background: var(--bg-light);
                    color: var(--text-muted);
                }
            }
        `;
        
        const container = document.createElement('div');
        container.className = 'footer-note';
        
        const slot = document.createElement('slot');
        container.appendChild(slot);
        
        shadow.appendChild(style);
        shadow.appendChild(container);

        // Put the original content back into the slot
        this.innerHTML = textContent;
    }
}

customElements.define('footer-note', FooterNote);
