import os

def update_first_occurrence(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated " + filepath)
    else:
        print("Not found in " + filepath)

# Thai
update_first_occurrence(
    'ข่าวสารและกิจกรรม.html',
    '<div class="news-category csr">กิจกรรมเพื่อสังคม (CSR)</div>',
    '<div class="news-category csr">ข่าวสาร</div>'
)

# English
update_first_occurrence(
    'en/ข่าวสารและกิจกรรม.html',
    '<div class="news-category csr">CSR</div>',
    '<div class="news-category csr">News</div>'
)
