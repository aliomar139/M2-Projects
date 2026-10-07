from pathlib import Path
import re
B=Path(__file__).parent
s=(B/'build_deck.py').read_text(encoding='utf-8')
s=s[s.index('from pathlib'):]
s=s.replace('from template_inspect import render as render_group, svg as svg_doc, COLORS', '''def svg_doc(content):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540">'+content+'</svg>' ''')
s=s.replace("presentation-designed.pptx", "presentation-final.pptx").replace("PRE=BASE/'previews'", "PRE=BASE/'previews-final'")
s=re.sub(r"T=\{[^\n]+", "T={'ink':'303030','deep':'F3F3F3','muted':'666666','cyan':'303030','cyanDark':'303030','orange':'303030','paper':'F3F3F3','line':'DDDDDD','white':'FFFFFF','blue':'888888'}",s)
s=s.replace("FH='Fira Sans Extra Condensed'; FB='Roboto'", "FH='Roboto'; FB='Roboto'")
s=s.replace("self.n=n;self.title=title;self.dark=dark", "dark=False;self.n=n;self.title=title;self.dark=dark")
s=s.replace("if n!=1:self.text(title,52,38,858,58,42,family=FH,bold=True,c='white' if dark else 'ink')", "if n not in [1,16]:self.text(title,52,38,858,58,36,family=FH,bold=True,name='Slide title')")
s=s.replace('        self.footer()', '        if n!=16:self.footer()')
a=s.index('    def icon('); b=s.index('    def footer(',a)
s=s[:a]+'''    def icon(self,index,x,y,size,c='ink'):
        # Original editable line artwork drawn on a common 48-unit grid.
        k=size/48
        def p(points,closed=False): self.path([(x+u*k,y+v*k) for u,v in points],stroke=c,sw=2*k,close=closed,name='Original icon')
        def box(u,v,w,h):self.rect(x+u*k,y+v*k,w*k,h*k,stroke=c,sw=2*k)
        def circ(u,v,d):self.circle(x+u*k,y+v*k,d*k,stroke=c,sw=2*k)
        if index==0:
            box(7,8,34,32);p([(7,18),(41,18)]);p([(19,8),(19,18),(29,18),(29,8)]);p([(14,33),(23,33)])
        elif index==1:
            circ(8,10,32);p([(24,15),(24,26),(32,30)]);p([(19,4),(29,4)]);p([(24,4),(24,10)])
        elif index==26:
            circ(5,5,38);circ(13,13,22);circ(21,21,6);p([(24,24),(42,6)]);p([(35,6),(42,6),(42,13)])
        elif index==53:
            p([(24,5),(40,11),(38,29),(32,38),(24,44),(16,38),(10,29),(8,11)],True);p([(16,24),(22,30),(33,18)])
        elif index==54:
            circ(5,5,38);p([(14,24),(21,31),(34,17)])
        elif index==32:
            p([(24,44),(10,25),(8,17),(12,9),(20,5),(28,5),(36,9),(40,17),(38,25)],True);circ(18,13,12)
        elif index in [12,36]:
            circ(17,5,14);p([(8,42),(10,30),(17,25),(31,25),(38,30),(40,42)]);p([(14,42),(34,42)])
            if index==36:circ(29,29,16);p([(37,32),(37,37),(40,39)])
        elif index in [35,56]:
            box(5,6,38,29);p([(24,35),(24,42),(14,42),(34,42)]);p([(12,27),(20,21),(27,24),(37,13)])
        elif index==34:
            box(7,26,7,15);box(20,18,7,23);box(33,7,7,34)
        elif index==55:
            box(10,5,29,38);p([(16,14),(32,14)]);p([(16,23),(32,23)]);p([(16,32),(28,32)])
        elif index==10:
            circ(6,6,36);p([(31,14),(19,14),(16,18),(19,24),(29,24),(32,30),(29,34),(17,34)]);p([(24,9),(24,39)])
        else:
            box(6,6,12,12);box(30,6,12,12);box(18,30,12,12);p([(12,18),(12,24),(36,24),(36,18)]);p([(24,24),(24,30)])
''' +s[b:]
s=s.replace("        self.text('Template artwork: Slidesgo',570,511,250,18,11,c=cc,align='r')\n",'').replace("{self.n:02} / 15", "{self.n:02} / 16")
# Every text uses dark ink; filled panels stay pale on all slides.
s=s.replace("c='white'", "c='ink'").replace("ink='white'", "ink='ink'")
s=s.replace("cc='white' if j==3 else 'ink'", "cc='ink'")
s=s.replace("c='ink',r=True", "c='paper',r=True")
s=s.replace("c='ink' if j==4 else 'paper'", "c='paper'").replace("c='ink' if j==2 else 'paper'", "c='paper'")
s=s.replace("s.rect(312,433,340,38,c='ink')", "s.rect(312,433,340,38,c='white')")
# Title on one line and a spacious cover.
s=s.replace("s.text('Prescriptive\\nanalytics',52,78,455,166,72,c='ink',bold=True,family=FH,lh=76)","s.text('Prescriptive analytics',52,48,856,64,48,bold=True,name='Slide title')")
s=s.replace("54,272,440,70,26", "54,196,440,80,26").replace("54,380,440,66,24", "54,327,440,66,24")
s=s.replace("Suggested\\naction", "Suggested action").replace("784,321,132,73,31", "730,380,210,40,23")
s=s.replace("s.circle(802,213,92,c='cyan')", "s.circle(802,213,92,c='paper')")
s=s.replace("The role of prescriptive analytics", "From prediction to action").replace("Methods used in prescriptive analytics", "Prescriptive methods").replace("Decisions prescriptive analytics can support", "Decisions it can support").replace("Short-term and long-term decisions", "Decisions over time")
# Readable labels and consistent item alignment with the wider font.
s=s.replace("216,61,26", "216,61,22").replace("196,42,29", "196,42,25").replace("232,39,22", "232,39,20")
s=s.replace("259,49,32", "259,49,25").replace("337,50,31", "337,50,26").replace("160,47,30", "160,47,22")
s=s.replace("325,43,30", "325,43,26").replace("360,47,27", "360,47,22").replace("156,43,29", "156,43,23")
s=s.replace("306,45,27", "306,45,24").replace("356,45,27", "356,45,24").replace("355,39,29", "355,39,24")
s=s.replace("253,49,31", "253,49,24").replace("470,78,30", "470,78,26")
s=s.replace("c='ink' if dark else 'white'", "c='white'")
# Replace the methods columns with three aligned rows.
a=s.index("step(s,1,'Mathematical");b=s.index("slides.append(s)",a)
s=s[:a]+'''methods=[('Mathematical optimization','Finds the best result for a goal while following the rules.','Share limited stock',26),('Constraint programming','Finds a plan that follows detailed rules.','Plan working hours',53),('Simulation','Tests possible results when conditions change.','Compare staff plans',35)]
for j,(t,b,e,ico) in enumerate(methods):
    y=121+j*102
    s.rect(52,y,856,88,c='paper',r=True)
    s.icon(ico,72,y+23,40)
    s.text(t,134,y+13,420,36,25,bold=True)
    s.text(b,134,y+50,470,33,17)
    s.text('Example',660,y+13,220,25,14,c='muted')
    s.text(e,660,y+39,220,43,19,bold=True)
band(s,'Simulation tests plans; a rule or optimization method selects a plan.',y=443,size=18)
''' +s[b:]
s=s.replace("s.text('Thank you',52,456,300,34,24,family=FH,bold=True)\n",'')
s=s.replace("s.text('Design and vector artwork by Slidesgo',535,459,373,27,14,c='muted',align='r')\n",'')
s=s.replace('assert len(slides)==15', "s=Slide(16,'Thank you');s.text('Thank you',52,233,856,80,54,bold=True,align='ctr',name='Slide title');slides.append(s)\nassert len(slides)==16")
s=s.replace("for i,s in enumerate(slides):", "for i,s in enumerate(slides[:15]):")
s=s.replace("+'\\n\\nDesign and native vector artwork adapted from Big Data Infographics by Slidesgo.'",'')
s=s.replace('def relationships(rows):', "slides[-1].note('Thank you')\n\ndef relationships(rows):")
s=s.replace("sub(r,aq('rPr'),lang='en-US',sz=1200);sub(r,aq('t')).text=line", "rp=sub(r,aq('rPr'),lang='en-US',sz=1200);sub(rp,aq('latin'),typeface=FB);sub(r,aq('t')).text=line")
# Packaging is generated independently, using an empty master/layout and no template artwork.
s=s[:s.index("src=ZipFile(")]+(B/'clean_package.py.txt').read_text(encoding='utf-8')
(B/'build_final.py').write_text(s,encoding='utf-8')
