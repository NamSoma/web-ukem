class ValueChainCard extends HTMLElement {
    connectedCallback() {
        // Only run once
        if (this.hasAttribute('rendered')) return;
        this.setAttribute('rendered', 'true');

        const title = this.getAttribute('title') || '';
        this.removeAttribute('title');
        const content = this.innerHTML.trim();
        
        this.innerHTML = `
            <div class="vc-card">
                <div class="vc-card-header">
                    <h4>${title}</h4>
                </div>
                <div class="vc-card-body">
                    <ul>
                        ${content}
                    </ul>
                </div>
            </div>
        `;
    }
}

customElements.define('value-chain-card', ValueChainCard);
