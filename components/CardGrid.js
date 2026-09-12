class CardGrid extends HTMLElement {
    connectedCallback() {
        // Apply styling directly or rely on global CSS
        if (!this.classList.contains('cards-grid')) {
            this.classList.add('cards-grid');
        }
    }
}
customElements.define('card-grid', CardGrid);

class CardItem extends HTMLElement {
    connectedCallback() {
        if (!this.classList.contains('card-item')) {
            this.classList.add('card-item');
        }
    }
}
customElements.define('card-item', CardItem);
