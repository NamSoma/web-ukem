class InnerHero extends HTMLElement {
    connectedCallback() {
        const title = this.getAttribute('title') || '';
        const bgImage = this.getAttribute('bg-image') || this.getAttribute('image-url') || '';
        
        this.innerHTML = `
            <header class="inner-hero" style="background-image: url('${bgImage}'); background-size: cover; background-position: center; position: relative;">
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.2); z-index: 1;"></div>
                <div class="inner-hero-content" style="position: relative; z-index: 2;">
                    <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">${title}</h1>
                </div>
            </header>
        `;
    }
}
customElements.define('inner-hero', InnerHero);
