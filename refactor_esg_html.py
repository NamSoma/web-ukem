import os
import glob
from bs4 import BeautifulSoup
import re

css_addition = """
/* =========================================
   ESG ACCORDION (PROGRESSIVE DISCLOSURE)
========================================= */
details.esg-accordion {
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    overflow: hidden;
    transition: all 0.3s ease;
}

details.esg-accordion[open] {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border-color: var(--primary-light);
}

details.esg-accordion > summary {
    padding: 18px 20px;
    cursor: pointer;
    font-weight: 600;
    font-size: 18px;
    color: var(--primary);
    background-color: #f8fafc;
    list-style: none;
    position: relative;
    display: flex;
    align-items: center;
    gap: 10px;
}

details.esg-accordion > summary::-webkit-details-marker {
    display: none;
}

details.esg-accordion > summary::before {
    content: '+';
    font-size: 24px;
    font-weight: 400;
    color: var(--primary);
    margin-right: 5px;
    transition: transform 0.3s ease;
}

details.esg-accordion[open] > summary::before {
    content: '−';
    transform: rotate(180deg);
}

details.esg-accordion > summary:hover {
    background-color: #f1f5f9;
}

details.esg-accordion .accordion-content {
    padding: 20px;
    border-top: 1px solid var(--border-color);
    background: #ffffff;
    color: var(--text-muted);
    line-height: 1.7;
}

/* Skimmable text styling */
.skimmable-bold {
    color: var(--text-main);
    font-weight: 600;
}
"""

def inject_css(workspace_dir):
    css_path = os.path.join(workspace_dir, "css", "global.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "ESG ACCORDION" not in content:
            with open(css_path, "a", encoding="utf-8") as f:
                f.write("\n" + css_addition)
            print("Injected CSS into global.css")
    else:
        print(f"Could not find CSS at {css_path}")

def make_skimmable(p_tag, soup):
    # Try to bold the first sentence or first chunk of text to make it skimmable
    text = p_tag.get_text()
    if len(text) > 100 and not p_tag.find('strong'):
        # Find first space after 50 chars, or first break
        split_idx = -1
        space_idx = text.find(' ', 60)
        if space_idx != -1 and space_idx < 150:
            split_idx = space_idx
        else:
            split_idx = min(80, len(text))
        
        # We need to preserve HTML inside p_tag, so this is tricky. 
        # A simpler approach: if p_tag has no children tags, we can replace its string.
        if len(p_tag.find_all(True)) == 0:
            first_part = text[:split_idx]
            rest = text[split_idx:]
            p_tag.clear()
            strong_tag = soup.new_tag('strong', attrs={'class': 'skimmable-bold'})
            strong_tag.string = first_part
            p_tag.append(strong_tag)
            p_tag.append(rest)

def process_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # 1. Convert .activity-card to accordion
    activity_cards = soup.find_all('div', class_='activity-card')
    for card in activity_cards:
        h4 = card.find('h4')
        if h4:
            details = soup.new_tag('details', attrs={'class': 'esg-accordion'})
            summary = soup.new_tag('summary')
            summary.string = h4.get_text(strip=True)
            details.append(summary)
            
            content_div = soup.new_tag('div', attrs={'class': 'accordion-content'})
            # Move all p tags inside
            for p in card.find_all('p'):
                make_skimmable(p, soup)
                content_div.append(p.extract())
            
            details.append(content_div)
            # Replace card content
            card.clear()
            # Remove styles from card so it doesn't interfere
            card['style'] = "margin-bottom: 20px; padding: 0; background: transparent; border: none; box-shadow: none;"
            card.append(details)
            modified = True

    # 2. Find h4 tags that are followed by p tags (like in Environmental Mgmt)
    # and group them into accordions.
    h4_tags = soup.find_all('h4')
    for h4 in h4_tags:
        # Check if parent is already an accordion or activity card
        if h4.find_parent('details') or h4.find_parent(class_='activity-card'):
            continue
            
        next_sib = h4.find_next_sibling()
        if next_sib and next_sib.name in ['p', 'ul']:
            # We found a section that can be an accordion
            details = soup.new_tag('details', attrs={'class': 'esg-accordion'})
            summary = soup.new_tag('summary')
            summary.string = h4.get_text(strip=True)
            details.append(summary)
            
            content_div = soup.new_tag('div', attrs={'class': 'accordion-content'})
            
            # Gather siblings until next heading
            sibs_to_move = []
            curr = next_sib
            while curr and curr.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'table']:
                sibs_to_move.append(curr)
                curr = curr.find_next_sibling()
                
            for sib in sibs_to_move:
                if sib.name == 'p':
                    make_skimmable(sib, soup)
                content_div.append(sib.extract())
                
            details.append(content_div)
            h4.replace_with(details)
            modified = True
            
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Refactored: {file_path}")

def main():
    workspace = r"c:\Users\Admin\.gemini\antigravity-ide\scratch\web-ukem"
    inject_css(workspace)
    
    targets = [
        "ภาพรวมความยั่งยืน",
        "สิ่งแวดล้อม",
        "สังคม",
        "การกำกับดูแลและเศรษฐกิจ",
        "en/ภาพรวมความยั่งยืน",
        "en/สิ่งแวดล้อม",
        "en/สังคม",
        "en/การกำกับดูแลและเศรษฐกิจ"
    ]
    
    for target in targets:
        dir_path = os.path.join(workspace, target)
        if os.path.exists(dir_path):
            for file_path in glob.glob(os.path.join(dir_path, "*.html")):
                process_html_file(file_path)

if __name__ == "__main__":
    main()
