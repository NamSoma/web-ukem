from bs4 import BeautifulSoup

html = open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

gov_control = soup.find(id='gov_control')
if gov_control:
    parents = [p.name + (f"#{p.get('id')}" if p.get('id') else "") + (f".{'.'.join(p.get('class', []))}" if p.get('class') else "") for p in gov_control.parents if p.name != '[document]']
    print("Parents of gov_control:", parents)
else:
    print("gov_control not found")
