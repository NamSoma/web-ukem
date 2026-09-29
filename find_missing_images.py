import os
import re
from urllib.parse import unquote

root_dir = r'f:\Back up อีก HDD\งาน\ลองทำ'
missing_images = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                continue

            # Find all image paths
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
            hero_bgs = re.findall(r'<inner-hero[^>]+(?:bg-image|image-url)=["\']([^"\']+)["\']', content)
            bg_urls = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', content)
            
            all_paths = img_srcs + hero_bgs + bg_urls
            
            for img_path in all_paths:
                if img_path.startswith('http') or img_path.startswith('data:') or not img_path.strip() or img_path.startswith('#'):
                    continue
                
                img_path_decoded = unquote(img_path)
                img_path_normalized = os.path.normpath(img_path_decoded)
                
                # Exclude javascript variables or react templates
                if '${' in img_path_normalized: continue
                
                abs_img_path = os.path.join(dirpath, img_path_normalized)
                abs_img_path = os.path.abspath(abs_img_path)
                
                if not os.path.exists(abs_img_path):
                    rel_html_path = os.path.relpath(filepath, root_dir)
                    missing_images.append((rel_html_path, img_path))

with open(r'f:\Back up อีก HDD\งาน\ลองทำ\missing_images.txt', 'w', encoding='utf-8') as out:
    if missing_images:
        for html_file, img in missing_images:
            out.write(f"File: {html_file} -> Missing: {img}\n")
    else:
        out.write("All image references are valid!\n")
