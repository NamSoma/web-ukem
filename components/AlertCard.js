class AlertCard extends HTMLElement {
    constructor() {
        super();
        const textContent = this.innerHTML;
        this.innerHTML = '';
        
        const shadow = this.attachShadow({ mode: 'open' });
        
        const style = document.createElement('style');
        style.textContent = `
            .alert-card {
                background: var(--alert-bg, linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%));
                border: 1px solid var(--alert-border, #bae6fd);
                border-radius: 0px;
                padding: 30px;
                margin-top: 30px;
                box-shadow: none;
                font-family: inherit;
            }
        `;
        
        const container = document.createElement('div');
        container.className = 'alert-card';
        
        const slot = document.createElement('slot');
        container.appendChild(slot);
        
        shadow.appendChild(style);
        shadow.appendChild(container);

        this.innerHTML = textContent;
    }
}

customElements.define('alert-card', AlertCard);
