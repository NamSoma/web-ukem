import re
with open(r'เกี่ยวกับ UKEM.html', 'r', encoding='utf-8') as f:
    content = f.read()
for img in re.findall(r'<img.*?src="(.*?)"', content):
    print(img.encode('utf-8'))
