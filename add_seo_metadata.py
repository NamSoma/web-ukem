import os
import glob

workspace = r'f:\Back up อีก HDD\งาน\ลองทำ'

meta_tags = '''
    <meta property="og:site_name" content="Union Petrochemical Public Company Limited">
    <meta property="og:title" content="UKEM Sustainability">
'''

json_ld_th = '''
    <script type="application/ld+json">
    {
      "@context" : "https://schema.org",
      "@type" : "WebSite",
      "name" : "Union Petrochemical Public Company Limited",
      "alternateName" : ["UKEM", "บริษัท ยูเนี่ยน ปิโตรเคมีคอล จำกัด (มหาชน)"],
      "url" : "https://union-esg.web.app/"
    }
    </script>
'''

json_ld_en = '''
    <script type="application/ld+json">
    {
      "@context" : "https://schema.org",
      "@type" : "WebSite",
      "name" : "Union Petrochemical Public Company Limited",
      "alternateName" : "UKEM",
      "url" : "https://union-esg.web.app/en/"
    }
    </script>
'''

html_files = glob.glob(os.path.join(workspace, '**', '*.html'), recursive=True)

count = 0
for file_path in html_files:
    if 'node_modules' in file_path or '.gemini' in file_path:
        continue
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-16') as f:
                content = f.read()
        except:
            print(f"Failed to read {file_path}")
            continue
        
    # Check if already has og:site_name
    if 'og:site_name' in content:
        continue
        
    # Inject meta tags
    if '</title>' in content:
        content = content.replace('</title>', '</title>' + meta_tags)
    elif '</head>' in content:
        content = content.replace('</head>', meta_tags + '</head>')
        
    # Inject JSON-LD to homepages
    filename = os.path.basename(file_path)
    if filename == 'เกี่ยวกับ UKEM.html' and '\\en\\' not in file_path:
        content = content.replace('</head>', json_ld_th + '</head>')
    elif filename == 'About UKEM.html' and '\\en\\' in file_path:
        content = content.replace('</head>', json_ld_en + '</head>')
        
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    except:
        pass
        
print(f"Updated {count} HTML files with SEO metadata.")
