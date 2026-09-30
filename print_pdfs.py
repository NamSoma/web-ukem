import urllib.parse, re, os, pathlib

workspace = pathlib.Path(r'f:\Back up อีก HDD\งาน\ลองทำ')
urls = set()

for r, d, fs in os.walk(workspace):
    if any(x in r for x in ['.agent', 'scratch', 'node_modules', 'ลองทำ\\ลองทำ']):
        continue
    for f in fs:
        if f.endswith('.html'):
            try:
                content = open(os.path.join(r, f), encoding='utf-8').read()
                matches = re.findall(r'https?://(?:www\.)?unionpetrochemical\.com/[^\s"\'\>]+(?:\.pdf|\.PDF)', content, re.IGNORECASE)
                urls.update(matches)
            except:
                pass

with open('pdf_list.txt', 'w', encoding='utf-8') as out:
    for u in urls:
        filename = urllib.parse.unquote(u.split('/')[-1])
        out.write(filename + '\n')
