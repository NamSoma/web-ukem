from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.stack.append(tag)
        d = dict(attrs)
        if d.get('id') in ['gov_policy', 'gov_risk', 'gov_control', 'sustainability', 'hr', 'partner']:
            print(f"Depth at {d.get('id')}:", len(self.stack))
    def handle_endtag(self, tag):
        if tag == 'div':
            if self.stack:
                self.stack.pop()

parser = MyParser()
parser.feed(open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', encoding='utf-8').read())
print('Final depth:', len(parser.stack))
