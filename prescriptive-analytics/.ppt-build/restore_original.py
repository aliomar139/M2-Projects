from pathlib import Path
B=Path(__file__).parent
s=(B/'build_deck.py').read_text(encoding='utf-8')
s=s[s.index('from pathlib'):]
s=s.replace('from template_inspect import render as render_group, svg as svg_doc, COLORS', '''def svg_doc(content):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540">'+content+'</svg>' ''')
s=s.replace('presentation-designed.pptx','presentation-original-revised.pptx').replace("PRE=BASE/'previews'", "PRE=BASE/'previews-original-revised'")
f=(B/'build_final.py').read_text(encoding='utf-8')
a=s.index('    def icon(');b=s.index('    def footer(',a)
icon=f[f.index('    def icon('):f.index('    def footer(')]
s=s[:a]+icon+s[b:]
s=s.replace('if n!=1:self.text(title', 'if n not in [1,16]:self.text(title').replace('        self.footer()', '        if n!=16:self.footer()')
s=s.replace("        self.text('Template artwork: Slidesgo',570,511,250,18,11,c=cc,align='r')\n",'').replace('{self.n:02} / 15','{self.n:02} / 16')
# Light cover with the original palette and diagram.
a=s.index("s=Slide(1,");b=s.index('slides.append(s)',a)
s=s[:a]+'''s=Slide(1,'Prescriptive analytics')
s.text('Prescriptive analytics',52,48,856,75,54,c='ink',bold=True,family=FH,name='Slide title')
s.text('Decision-making in the\\ndata science life cycle',54,207,440,70,26)
s.text('Uses data, goals, and limits\\nto suggest what to do.',54,347,440,66,24,c='cyanDark')
for y,label,ico in [(145,'Data',0),(250,'Goals',26),(355,'Limits',53)]:
    s.rect(544,y,140,71,c='paper',r=True);s.icon(ico,559,y+20,30,c='cyanDark');s.text(label,600,y+18,76,45,23,c='ink',bold=True,family=FH)
    s.line(689,y+35,750,y+35,c='blue',sw=2)
s.line(750,180,750,390,c='blue',sw=2);s.line(750,285,795,285,c='cyanDark',sw=2,arrow=True)
s.circle(802,242,92,c='paper');s.icon(54,827,264,43,c='cyanDark')
s.text('Suggested action',743,366,184,49,29,c='ink',bold=True,family=FH,align='ctr')
''' +s[b:]
# Slide 10 uses the same white background, slate text, and teal accents as the light slides.
a=s.index("s=Slide(10,");b=s.index('slides.append(s)',a)
part=s[a:b].replace(",dark=True",'').replace("c='white'", "c='ink'").replace("c='cyan'", "c='cyanDark'").replace("c='deep',ink='white'", "c='paper',ink='ink'")
s=s[:a]+part+s[b:]
s=s.replace("s.text('Thank you',52,456,300,34,24,family=FH,bold=True)\n",'').replace("s.text('Design and vector artwork by Slidesgo',535,459,373,27,14,c='muted',align='r')\n",'')
s=s.replace('assert len(slides)==15', "s=Slide(16,'Thank you');s.text('Thank you',52,229,856,82,54,bold=True,family=FH,align='ctr',name='Slide title');slides.append(s)\nassert len(slides)==16")
s=s.replace('for i,s in enumerate(slides):', 'for i,s in enumerate(slides[:15]):')
s=s.replace("+'\\n\\nDesign and native vector artwork adapted from Big Data Infographics by Slidesgo.'",'')
s=s.replace('def relationships(rows):', "slides[-1].note('Thank you')\n\ndef relationships(rows):")
s=s.replace("sub(r,aq('rPr'),lang='en-US',sz=1200);sub(r,aq('t')).text=line", "rp=sub(r,aq('rPr'),lang='en-US',sz=1200);sub(rp,aq('latin'),typeface=FB);sub(r,aq('t')).text=line")
package=(B/'clean_package.py.txt').read_text(encoding='utf-8').replace('layout-audit-final.json','layout-audit-original-revised.json').replace('original icons, Roboto, monochrome.','original blue-and-cyan design, light background.')
s=s[:s.index('src=ZipFile(')]+package
(B/'build_original_revised.py').write_text(s,encoding='utf-8')
