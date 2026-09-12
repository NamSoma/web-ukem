import os
import re

base_dir = r"f:\Back up อีก HDD\งาน\ลองทำ"

for root, dirs, files in os.walk(base_dir):
    # skip .git, components, css, etc
    if any(x in root for x in [".git", "components", "css", "assets", ".vscode"]):
        continue

    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # calculate relative path from base_dir
            rel_path = os.path.relpath(file_path, base_dir)
            # convert windows backslashes to forward slashes for URLs
            rel_path = rel_path.replace("\\", "/")
            
            is_en = rel_path.startswith("en/")
            lang = "en" if is_en else "th"
            
            # the logical path should not include 'en/' so that TH and EN correspond
            logical_path = rel_path[3:] if is_en else rel_path
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Regex to find <main-nav ...> or <main-nav>
            # and inject path="..." and lang="..."
            
            # First remove existing path or lang attributes to avoid duplicates
            content = re.sub(r'(<main-nav[^>]*) path="[^"]*"', r'\1', content)
            content = re.sub(r'(<main-nav[^>]*) lang="[^"]*"', r'\1', content)
            
            # Now add them
            def add_attrs(match):
                tag = match.group(1)
                # handle self closing just in case, though usually it's <main-nav>
                if tag.endswith('/'):
                    tag = tag[:-1].rstrip()
                return f'{tag} path="{logical_path}" lang="{lang}">'
            
            new_content = re.sub(r'(<main-nav[^>]*)>', add_attrs, content)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {rel_path}")

print("Done.")
