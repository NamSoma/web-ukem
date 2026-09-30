import re

filepaths = [
    'f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html',
    'f:/Back up อีก HDD/งาน/ลองทำ/en/นโยบายและเอกสารดาวน์โหลด.html'
]

for filepath in filepaths:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS to hide category-section by default, show if active
    # I'll just append it to the end of the <style> block before </style>
    if '.category-section { display: none; }' not in content:
        content = content.replace('</style>', '''
        .category-section { display: none; }
        .category-section.active { display: block; }
    </style>''', 1)
    
    # Remove the sticky scrolling offset if I added it previously (scroll-margin-top)
    content = re.sub(r'\.category-section\s*\{\s*scroll-margin-top:\s*[^}]*\}\s*', '', content)

    # 2. Replace Javascript with Tab logic
    js_logic = """
    <script>
        feather.replace();

        document.addEventListener('DOMContentLoaded', function() {
            const btns = document.querySelectorAll('.sidebar-btn');
            const sections = document.querySelectorAll('.category-section');

            btns.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    
                    // Remove active from all buttons and sections
                    btns.forEach(b => b.classList.remove('active'));
                    sections.forEach(s => s.classList.remove('active'));
                    
                    // Add active to clicked button and target section
                    this.classList.add('active');
                    const targetId = this.getAttribute('data-target');
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {
                        targetElement.classList.add('active');
                    }
                });
            });
        });
    </script>
</body>
"""

    # Replace the existing script block at the end
    content = re.sub(r'<script>.*?</script>\s*</body>', js_logic, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored tabs")
