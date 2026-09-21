import os

files = ['components/StatsCard.js', 'components/DocDownload.js', 'components/SectionHeader.js', 'components/InnerHero.js', 'components/HeroBanner.js']
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if "this.removeAttribute('title');" not in content:
            content = content.replace("getAttribute('title') || '';", "getAttribute('title') || '';\n        this.removeAttribute('title');")
            content = content.replace("getAttribute('title') || 'Title';", "getAttribute('title') || 'Title';\n        this.removeAttribute('title');")
            content = content.replace("getAttribute('title') || 'ชื่อเอกสารที่ (รออัปโหลด)';", "getAttribute('title') || 'ชื่อเอกสารที่ (รออัปโหลด)';\n        this.removeAttribute('title');")
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Updated {f}')
