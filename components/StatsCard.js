class StatsGrid extends HTMLElement {
    connectedCallback() {
        if (this.hasAttribute('rendered')) return;
        this.setAttribute('rendered', 'true');
        
        const cols = this.getAttribute('cols') || '2';
        
        const innerContent = this.innerHTML;
        this.innerHTML = `
            <div class="stats-grid-container" style="display: grid; grid-template-columns: repeat(${cols}, 1fr); gap: 20px; margin-bottom: 30px; margin-top: 20px;">
                ${innerContent}
            </div>
        `;
        
        // Add responsiveness if needed
        if (!document.getElementById('stats-grid-style')) {
            const style = document.createElement('style');
            style.id = 'stats-grid-style';
            style.textContent = `
                @media (max-width: 768px) {
                    .stats-grid-container { grid-template-columns: 1fr !important; }
                }
            `;
            document.head.appendChild(style);
        }
    }
}
customElements.define('stats-grid', StatsGrid);

class StatCard extends HTMLElement {
    connectedCallback() {
        if (this.hasAttribute('rendered')) return;
        this.setAttribute('rendered', 'true');

        const title = this.getAttribute('title') || '';
        this.removeAttribute('title');
        const value = this.getAttribute('value') || '';
        const desc = this.getAttribute('desc') || '';
        const theme = this.getAttribute('theme') || ''; // 'blue', 'green'
        
        let valueClass = 'stat-value';
        if (theme === 'green') valueClass += ' green';
        
        let cardClass = 'stat-card';
        if (theme === 'blue') cardClass += ' blue';

        this.innerHTML = `
            <div class="${cardClass}">
                <div class="stat-title">${title}</div>
                <div class="${valueClass}">${value}</div>
                <div class="stat-desc">${desc}</div>
            </div>
        `;
    }
}
customElements.define('stat-card', StatCard);
