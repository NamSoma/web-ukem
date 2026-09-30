import os
import re
import urllib.request
import urllib.parse
from pathlib import Path

workspace = Path(r"f:\Back up อีก HDD\งาน\ลองทำ")
download_dir = workspace / "assets" / "เอกสารดาวน์โหลด"
download_dir.mkdir(parents=True, exist_ok=True)

# Regex to find unionpetrochemical PDF links
pattern = re.compile(r'(https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+\.pdf)', re.IGNORECASE)

url_map = {}

def get_relative_path(html_path, target_path):
    # html_path is like workspace / "dir" / "file.html"
    # target_path is workspace / "assets" / "เอกสารดาวน์โหลด" / "file.pdf"
    
    # number of parents from html_path to workspace
    rel_dir = html_path.parent.relative_to(workspace)
    depth = len(rel_dir.parts)
    
    prefix = "../" * depth
    if depth == 0:
        prefix = ""
        
    return f"{prefix}assets/เอกสารดาวน์โหลด/{target_path.name}"

for root, dirs, files in os.walk(workspace):
    # Exclude unwanted directories
    dirs[:] = [d for d in dirs if d not in ['.agent', 'scratch', 'node_modules', 'ลองทำ']]
    
    for file in files:
        if file.endswith('.html'):
            html_path = Path(root) / file
            
            try:
                with open(html_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                pass
                continue
                
            matches = pattern.findall(content)
            if not matches:
                continue
                
            new_content = content
            modified = False
            
            for url in matches:
                if url not in url_map:
                    # Download it
                    try:
                        # Some URLs might have Thai characters, need to unquote to get a nice filename
                        parsed = urllib.parse.urlparse(url)
                        filename = urllib.parse.unquote(Path(parsed.path).name)
                        
                        # Clean filename just in case
                        filename = filename.replace('\n', '').replace('\r', '')
                        
                        target_file = download_dir / filename
                        
                        print("Downloading a file...")
                        
                        # To download, we might need to properly quote the URL if it contains literal Thai characters
                        # but requests handles it better. Since we use urllib:
                        encoded_url = urllib.parse.quote(url, safe=":/")
                        
                        req = urllib.request.Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req) as response, open(target_file, 'wb') as out_file:
                            out_file.write(response.read())
                            
                        url_map[url] = target_file
                    except Exception as e:
                        print(f"Failed to download a file: {e}")
                        continue
                
                # Replace in HTML
                if url in url_map:
                    target_file = url_map[url]
                    rel_path = get_relative_path(html_path, target_file)
                    new_content = new_content.replace(url, rel_path)
                    modified = True
                    
            if modified:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("Updated a file.")

print("Done downloading and updating links!")
