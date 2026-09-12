class HeroBanner extends HTMLElement {
    connectedCallback() {
        const title = this.getAttribute('title') || 'Title';
        const bgImage = this.getAttribute('bg-image') || '';
        
        this.innerHTML = `
            <header class="inner-hero" style="background-image: url('${bgImage}'); background-size: cover; background-position: center; position: relative; height: 350px; display: flex; flex-direction: column; justify-content: center; align-items: center; border-radius: 0; margin-top: 0;">
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.4); z-index: 1;"></div>
                <div class="inner-hero-content" style="position: relative; z-index: 2; max-width: 800px; text-align: center;">
                    <h1 style="color: white; font-size: 48px; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">${title}</h1>
                </div>
            </header>
        `;
    }
}
customElements.define('hero-banner', HeroBanner);
