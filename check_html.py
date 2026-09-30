from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.in_gov_risk = False
        
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            attrs_dict = dict(attrs)
            if attrs_dict.get('id') == 'gov_risk':
                self.in_gov_risk = True
                print("--- ENTERED gov_risk ---")
            
            if self.in_gov_risk:
                print(f"[{self.getpos()[0]}] + <{tag} id='{attrs_dict.get('id', '')}' class='{attrs_dict.get('class', '')}'>")
                
            self.stack.append((tag, self.getpos()[0], attrs_dict.get('id', ''), attrs_dict.get('class', '')))
            
    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            if self.stack and self.stack[-1][0] == tag:
                popped = self.stack.pop()
                if self.in_gov_risk:
                    print(f"[{self.getpos()[0]}] - </{tag}> (closed <{popped[0]} class='{popped[3]}'> from line {popped[1]})")
                if popped[2] == 'gov_risk':
                    self.in_gov_risk = False
                    print("--- EXITED gov_risk ---")

p = P()
p.feed(open('f:/Back up อีก HDD/งาน/ลองทำ/นโยบายและเอกสารดาวน์โหลด.html', encoding='utf-8').read())
