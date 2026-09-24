import glob
import re
for f in glob.glob('**/*.html', recursive=True):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = content.replace('https://www.unionpetrochemical.com/th/', 'https://www.unionpetrochemical.com/')
        new_content = new_content.replace('https://www.unionpetrochemical.com/en/', 'https://www.unionpetrochemical.com/')
        
        # Also let's fix the missing titles for Business Groups that I accidentally wiped earlier
        if 'id="business-groups"' in new_content:
            if '4 กลุ่มธุรกิจหลัก' not in new_content and 'ปัจจุบันบริษัทมีการประกอบธุรกิจหลัก 4' in new_content:
                new_content = new_content.replace(
                    '<p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; text-align: left; font-weight: 500;">\n                    ปัจจุบันบริษัทมีการประกอบธุรกิจหลัก 4 กลุ่มธุรกิจหลัก',
                    '<h2 class="section-title">4 กลุ่มธุรกิจหลัก</h2>\n                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 40px;"></div>\n                <p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; text-align: left; font-weight: 500;">\n                    ปัจจุบันบริษัทมีการประกอบธุรกิจหลัก 4 กลุ่มธุรกิจหลัก'
                )
            if '4 Main Business Groups' not in new_content and 'Currently, the company operates in 4 main business groups:' in new_content:
                new_content = new_content.replace(
                    '<p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; text-align: left; font-weight: 500;">\n                    Currently, the company operates in 4 main business groups:',
                    '<h2 class="section-title">4 Main Business Groups</h2>\n                <div style="width: 60px; height: 3px; background: var(--primary); margin: 20px auto 40px;"></div>\n                <p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; text-align: left; font-weight: 500;">\n                    Currently, the company operates in 4 main business groups:'
                )

        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
    except Exception as e:
        pass
