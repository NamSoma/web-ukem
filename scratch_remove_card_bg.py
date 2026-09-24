import os
import re

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"
about_th = os.path.join(base_dir, "เกี่ยวกับ UKEM.html")
about_en = os.path.join(base_dir, "en", "About UKEM.html")

def remove_card_backgrounds(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the first two cards
        content = content.replace(
            'background: var(--card-bg, #f8f9fa); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);',
            'background: transparent; padding: 0 0 20px 0; border-radius: 0; box-shadow: none;'
        )
        # Replace the third card
        content = content.replace(
            'background: var(--white); padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);',
            'background: transparent; padding: 20px 0 0 0; border-radius: 0; box-shadow: none;'
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

remove_card_backgrounds(about_th)
remove_card_backgrounds(about_en)

print("Card backgrounds removed")
