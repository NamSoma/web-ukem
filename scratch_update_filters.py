import os

def update_filters(filepath, filter_html, target_all_btn):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add filter button
    if target_all_btn in content:
        idx = content.find(target_all_btn)
        end_idx = content.find('\n', idx)
        
        if end_idx != -1:
            content = content[:end_idx] + '\n                  ' + filter_html + content[end_idx:]
    
    # 2. Change data-category="csr" to data-category="news" for the first card
    target_card = '<div class="news-card" data-category="csr">'
    content = content.replace(target_card, '<div class="news-card" data-category="news">', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# For Thai
update_filters(
    'ข่าวสารและกิจกรรม.html',
    '<button class="filter-btn" data-filter="news">ข่าวสาร</button>',
    '<button class="filter-btn active" data-filter="all">ทั้งหมด</button>'
)

# For English
update_filters(
    'en/ข่าวสารและกิจกรรม.html',
    '<button class="filter-btn" data-filter="news">News</button>',
    '<button class="filter-btn active" data-filter="all">All</button>'
)
