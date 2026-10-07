from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from copy import deepcopy
from lxml import etree as E
from PIL import ImageFont, Image, ImageDraw
import re, json, html, math, posixpath
def svg_doc(content):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540">'+content+'</svg>' 

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
OUT=ROOT/'prescriptive-analytics-presentation-original-revised.pptx'
PRE=BASE/'previews-original-revised'; PRE.mkdir(exist_ok=True)
U=9525; W=960; H=540
A='http://schemas.openxmlformats.org/drawingml/2006/main'
P='http://schemas.openxmlformats.org/presentationml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PR='http://schemas.openxmlformats.org/package/2006/relationships'
CT='http://schemas.openxmlformats.org/package/2006/content-types'
NS={'a':A,'p':P,'r':R}
T={'ink':'435D74','deep':'294559','muted':'6D8495','cyan':'5FD0DB','cyanDark':'007D8B','orange':'FF8001','paper':'F3F6F8','line':'D8E2E8','white':'FFFFFF','blue':'869FB2'}
FH='Fira Sans Extra Condensed'; FB='Roboto'
FONTDIR=Path('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts')
FONTS={(FH,False):FONTDIR/'FiraSansExtraCondensed-Regular.ttf',(FH,True):FONTDIR/'FiraSansExtraCondensed-SemiBold.ttf',(FB,False):FONTDIR/'Roboto-Regular.ttf',(FB,True):FONTDIR/'Roboto-Bold.ttf'}

def el(tag,**attrs):
    nsmap=attrs.pop('nsmap',None)
    return E.Element(tag,nsmap=nsmap,**{k:str(v) for k,v in attrs.items()})
def sub(parent,tag,**attrs):return E.SubElement(parent,tag,**{k:str(v) for k,v in attrs.items()})
def aq(t):return '{'+A+'}'+t
def pq(t):return '{'+P+'}'+t
def color(c):return T.get(c,c).lstrip('#')
def fill(parent,c):
    if c is None:sub(parent,aq('noFill'))
    else:sub(sub(parent,aq('solidFill')),aq('srgbClr'),val=color(c))
def wrap(txt,w,size,family=FB,bold=False):
    f=ImageFont.truetype(str(FONTS[(family,bold)]),round(size*2))
    lines=[]
    for para in txt.split('\n'):
        line=''
        for word in para.split():
            test=(line+' '+word).strip()
            if line and f.getlength(test)/2>w:
                lines.append(line);line=word
            else:line=test
        lines.append(line)
    return lines

class Slide:
    def __init__(self,n,title,dark=False):
        self.n=n;self.title=title;self.dark=dark;self.id=1;self.svg=[];self.texts=[];self.metrics=[]
        self.root=el(pq('sld'),showMasterSp='0',nsmap=NS)
        cs=sub(self.root,pq('cSld'),name=title)
        bg=sub(cs,pq('bg')); bp=sub(bg,pq('bgPr'));fill(bp,'ink' if dark else 'white');sub(bp,aq('effectLst'))
        self.tree=sub(cs,pq('spTree')); nv=sub(self.tree,pq('nvGrpSpPr'));sub(nv,pq('cNvPr'),id='1',name='Root');sub(nv,pq('cNvGrpSpPr'));sub(nv,pq('nvPr'))
        gp=sub(self.tree,pq('grpSpPr'));x=sub(gp,aq('xfrm'));sub(x,aq('off'),x=0,y=0);sub(x,aq('ext'),cx=0,cy=0);sub(x,aq('chOff'),x=0,y=0);sub(x,aq('chExt'),cx=0,cy=0)
        self.svg.append(f'<rect width="960" height="540" fill="#{color("ink" if dark else "white")}"/>')
        sub(sub(self.root,pq('clrMapOvr')),aq('masterClrMapping'))
        if n not in [1,16]:self.text(title,52,38,858,58,42,family=FH,bold=True,c='white' if dark else 'ink')
        if n!=16:self.footer()
    def newid(self):self.id+=1;return self.id
    def geom(self,name,x,y,w,h,geom='rect',c=None,stroke=None,sw=1):
        e=sub(self.tree,pq('sp'));nv=sub(e,pq('nvSpPr'));sub(nv,pq('cNvPr'),id=self.newid(),name=name);sub(nv,pq('cNvSpPr'));sub(nv,pq('nvPr'))
        sp=sub(e,pq('spPr'));xf=sub(sp,aq('xfrm'));sub(xf,aq('off'),x=round(x*U),y=round(y*U));sub(xf,aq('ext'),cx=round(w*U),cy=round(h*U))
        pg=sub(sp,aq('prstGeom'),prst=geom);av=sub(pg,aq('avLst'))
        if geom=='roundRect':sub(av,aq('gd'),name='adj',fmla='val 10000')
        fill(sp,c);ln=sub(sp,aq('ln'),w=round(sw*U));fill(ln,stroke)
        if geom=='ellipse':self.svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{("#"+color(c)) if c else "none"}" stroke="{("#"+color(stroke)) if stroke else "none"}" stroke-width="{sw}"/>')
        else:self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(w,h)*.1 if geom=="roundRect" else 0}" fill="{("#"+color(c)) if c else "none"}" stroke="{("#"+color(stroke)) if stroke else "none"}" stroke-width="{sw}"/>')
        return e
    def rect(self,x,y,w,h,c=None,stroke=None,r=False,sw=1,name='Panel'):
        return self.geom(name,x,y,w,h,'roundRect' if r else 'rect',c,stroke,sw)
    def circle(self,x,y,d,c=None,stroke=None,sw=1):return self.geom('Circle',x,y,d,d,'ellipse',c,stroke,sw)
    def path(self,pts,c=None,stroke='ink',sw=2,close=False,name='Vector'):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];x,y=min(xs),min(ys);w,h=max(xs)-x,max(ys)-y
        w=max(w,.01);h=max(h,.01)
        e=sub(self.tree,pq('sp'));nv=sub(e,pq('nvSpPr'));sub(nv,pq('cNvPr'),id=self.newid(),name=name);sub(nv,pq('cNvSpPr'));sub(nv,pq('nvPr'))
        sp=sub(e,pq('spPr'));xf=sub(sp,aq('xfrm'));sub(xf,aq('off'),x=round(x*U),y=round(y*U));sub(xf,aq('ext'),cx=round(w*U),cy=round(h*U))
        cg=sub(sp,aq('custGeom'));sub(cg,aq('avLst'));sub(cg,aq('gdLst'));sub(cg,aq('ahLst'));sub(cg,aq('cxnLst'));sub(cg,aq('rect'),l='l',t='t',r='r',b='b')
        pl=sub(cg,aq('pathLst'));pa=sub(pl,aq('path'),w=round(w*U),h=round(h*U))
        for j,(xx,yy) in enumerate(pts):sub(sub(pa,aq('moveTo' if j==0 else 'lnTo')),aq('pt'),x=round((xx-x)*U),y=round((yy-y)*U))
        if close:sub(pa,aq('close'))
        fill(sp,c);ln=sub(sp,aq('ln'),w=round(sw*U),cap='rnd');fill(ln,stroke);sub(ln,aq('round'))
        d='M'+' L'.join(f'{xx} {yy}' for xx,yy in pts)+(' Z' if close else '')
        self.svg.append(f'<path d="{d}" fill="{("#"+color(c)) if c else "none"}" stroke="{("#"+color(stroke)) if stroke else "none"}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>')
        return e
    def line(self,x1,y1,x2,y2,c='line',sw=1,arrow=False):
        # Native connectors remain editable and can be re-attached in PowerPoint.
        e=sub(self.tree,pq('cxnSp'));nv=sub(e,pq('nvCxnSpPr'));sub(nv,pq('cNvPr'),id=self.newid(),name='Connector');sub(nv,pq('cNvCxnSpPr'));sub(nv,pq('nvPr'))
        sp=sub(e,pq('spPr'));xf=sub(sp,aq('xfrm'))
        if x2<x1:xf.set('flipH','1')
        if y2<y1:xf.set('flipV','1')
        sub(xf,aq('off'),x=round(min(x1,x2)*U),y=round(min(y1,y2)*U));sub(xf,aq('ext'),cx=round(max(abs(x2-x1),.01)*U),cy=round(max(abs(y2-y1),.01)*U))
        sub(sub(sp,aq('prstGeom'),prst='line'),aq('avLst'));ln=sub(sp,aq('ln'),w=round(sw*U));fill(ln,c)
        if arrow:sub(ln,aq('tailEnd'),type='triangle',w='sm',len='sm')
        self.svg.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#{color(c)}" stroke-width="{sw}" fill="none"/>')
        if arrow:
            a=math.atan2(y2-y1,x2-x1);r=6
            ps=[(x2,y2),(x2-r*math.cos(a-.5),y2-r*math.sin(a-.5)),(x2-r*math.cos(a+.5),y2-r*math.sin(a+.5))]
            self.svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in ps)+f'" fill="#{color(c)}"/>')
    def text(self,txt,x,y,w,h=None,size=21,c='ink',bold=False,family=FB,align='l',lh=None,name='Text'):
        lines=wrap(txt,w,size,family,bold);lh=lh or size*1.25;needed=lh*len(lines);h=h or needed+4
        if needed>h: h=needed+2
        e=self.geom(name,x,y,w,h,c=None)
        e.find(pq('nvSpPr')+'/'+pq('cNvSpPr')).set('txBox','1')
        tb=sub(e,pq('txBody'));bp=sub(tb,aq('bodyPr'),wrap='none',anchor='t',lIns=0,tIns=0,rIns=0,bIns=0);sub(bp,aq('noAutofit'));sub(tb,aq('lstStyle'))
        for line in lines:
            p=sub(tb,aq('p'));pp=sub(p,aq('pPr'),algn=align,marL=0,indent=0)
            sub(sub(pp,aq('lnSpc')),aq('spcPts'),val=round(lh*75));sub(sub(pp,aq('spcAft')),aq('spcPts'),val=0);sub(pp,aq('buNone'))
            r=sub(p,aq('r'));rp=sub(r,aq('rPr'),lang='en-US',sz=round(size*75),b='1' if bold else '0');fill(rp,c)
            for f in ['latin','ea','cs']:sub(rp,aq(f),typeface=family)
            sub(r,aq('t')).text=line;sub(p,aq('endParaRPr'),lang='en-US',sz=round(size*75))
        self.texts.append({'text':txt,'lines':lines,'x':x,'y':y,'w':w,'h':h,'size':size,'lh':lh,'c':color(c),'bold':bold,'family':family,'align':align})
        self.metrics.append({'id':self.id,'text':txt,'box':[x,y,w,h],'lines':len(lines),'fontPx':size})
        return needed
    def icon(self,index,x,y,size,c='ink'):
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
    def footer(self):
        cc='blue' if self.dark else 'muted'
        self.line(52,500,908,500,c='blue' if self.dark else 'line',sw=.65)
        self.text('Prescriptive analytics',52,511,290,18,11,c=cc)
        self.text(f'{self.n:02} / 16',845,511,63,18,11,c=cc,align='r')
    def note(self,txt):self.notes=txt
    def export(self):
        (PRE/f'slide-{self.n:02}.svg').write_text(svg_doc(''.join(self.svg)),encoding='utf-8')
        (PRE/f'slide-{self.n:02}.text.json').write_text(json.dumps(self.texts,ensure_ascii=False),encoding='utf-8')
        return E.tostring(self.root,encoding='UTF-8',xml_declaration=True,standalone=True)

def band(s,txt,y=441,c='paper',ink='ink',x=52,w=856,size=20):
    s.rect(x,y,w,42,c=c,r=True);s.text(txt,x+18,y+8,w-36,31,size,c=ink)
def step(s,number,title,body,x,y,w=248,ico=None,accent='ink'):
    s.text(f'{number:02}',x,y,55,55,42,c=accent,family=FH,bold=True)
    if ico is not None:s.icon(ico,x+w-45,y+3,35,c=accent)
    s.text(title,x,y+65,w,55,29,family=FH,bold=True)
    s.text(body,x,y+160,w,85,19)
def numbered_row(s,n,title,body,y,icon=None,w=790):
    s.circle(52,y,42,c='paper');s.text(str(n),52,y+4,42,40,26,c='cyanDark',bold=True,family=FH,align='ctr')
    s.text(title,112,y-2,w,36,28,family=FH,bold=True);s.text(body,112,y+37,w,54,19)
    if icon is not None:s.icon(icon,840,y,42)

slides=[]
s=Slide(1,'Prescriptive analytics')
s.text('Prescriptive analytics',52,48,856,75,54,c='ink',bold=True,family=FH,name='Slide title')
s.text('Decision-making in the\ndata science life cycle',54,207,440,70,26)
s.text('Uses data, goals, and limits\nto suggest what to do.',54,347,440,66,24,c='cyanDark')
for y,label,ico in [(145,'Data',0),(250,'Goals',26),(355,'Limits',53)]:
    s.rect(544,y,140,71,c='paper',r=True);s.icon(ico,559,y+20,30,c='cyanDark');s.text(label,600,y+18,76,45,23,c='ink',bold=True,family=FH)
    s.line(689,y+35,750,y+35,c='blue',sw=2)
s.line(750,180,750,390,c='blue',sw=2);s.line(750,285,795,285,c='cyanDark',sw=2,arrow=True)
s.circle(802,242,92,c='paper');s.icon(54,827,264,43,c='cyanDark')
s.text('Suggested action',758,366,190,49,25,c='ink',bold=True,family=FH,align='ctr')
slides.append(s)

s=Slide(2,'The data science life cycle')
centers=[(160,197),(475,197),(790,197),(630,315),(320,315)]
labels=[('Understand\nthe problem',12),('Prepare\nthe data',0),('Build\na model',2),('Check\nthe results',54),('Use results\nin practice',56)]
s.line(210,197,425,197,'blue',2,True);s.line(525,197,740,197,'blue',2,True)
s.path([(840,197),(925,197),(925,315),(680,315)],stroke='blue',sw=2);s.line(700,315,680,315,'blue',2,True)
s.line(580,315,370,315,'blue',2,True);s.path([(270,315),(30,315),(30,197),(110,197)],stroke='blue',sw=2);s.line(90,197,110,197,'blue',2,True)
for j,((cx,cy),(label,ico)) in enumerate(zip(centers,labels)):
    s.circle(cx-43,cy-43,86,c='paper');s.icon(ico,cx-21,cy-21,42,c='cyanDark' if j in [2,4] else 'ink')
    s.text(label,cx-108,cy+53,216,61,26,family=FH,bold=True,align='ctr')
band(s,'Teams can return to earlier stages when data, goals, or results change.',y=443,size=18)
slides.append(s)

s=Slide(3,'Four types of analytics')
rows=[('Descriptive','What happened?','Show last month\'s sales for each store.',34),('Diagnostic','Why did it happen?','Check if missing products caused lower sales.',12),('Predictive','What may happen?','Predict next month\'s demand.',35),('Prescriptive','What should we do?','Decide how much stock to send to each store.',26)]
for j,(name,q,body,ico) in enumerate(rows):
    y=114+j*79
    if j==3:s.rect(52,y-4,856,74,c='ink',r=True)
    cc='white' if j==3 else 'ink';s.icon(ico,68,y+10,38,c='cyan' if j==3 else 'cyanDark')
    s.text(name,129,y+2,196,42,29,c=cc,bold=True,family=FH)
    s.text(q,325,y+3,232,39,22,c='cyan' if j==3 else 'ink',bold=True)
    s.text(body,568,y+2,322,59,18,c=cc)
    if j<3:s.line(129,y+69,908,y+69)
s.text('Stock = products available. Demand = how much customers want to buy.',52,451,856,34,17,c='muted')
slides.append(s)

s=Slide(4,'The role of prescriptive analytics')
s.rect(52,126,356,130,c='paper',r=True);s.icon(35,78,151,46,c='cyanDark');s.text('Prediction',145,145,236,49,32,family=FH,bold=True);s.text('Estimates what may happen.',78,207,307,38,21)
s.line(432,193,507,193,'cyanDark',3,True)
s.rect(530,126,378,130,c='ink',r=True);s.icon(26,555,151,46,c='cyan');s.text('Recommendation',624,145,259,49,32,c='white',family=FH,bold=True);s.text('Suggests what to do.',555,207,321,38,21,c='white')
s.text('Stores',52,302,382,42,29,bold=True,family=FH);s.text('Use expected demand to decide\nhow much stock to send.',52,352,388,74,22)
s.text('Delivery',530,302,378,42,29,bold=True,family=FH);s.text('Use predicted travel times to\nchoose roads for on-time delivery.',530,352,378,74,22)
band(s,'Show the action, the expected result, and the limits behind the choice.',y=443,size=18)
slides.append(s)

s=Slide(5,'The decision model')
items=[('Decision variables','What can change?','Products sent to each store',0,52,128),('Objective','What should improve?','Meet as much demand as possible',26,505,128),('Constraints','What rules must we follow?','Available stock and store limits',53,52,290),('Inputs','What information is available?','Expected demand and current stock',35,505,290)]
for title,q,b,ico,x,y in items:
    s.icon(ico,x,y,42,c='cyanDark');s.text(title,x+63,y-3,337,50,31,bold=True,family=FH);s.text(q,x+63,y+49,337,36,21,bold=True);s.text(b,x+63,y+91,337,40,19,c='muted')
s.line(480,130,480,421);s.line(52,272,908,272)
band(s,'Feasible = follows the rules. Optimal = best result within the model.',y=443,size=18)
slides.append(s)

s=Slide(6,'The recommendation process')
process=[('Define','Agree on the decision,\ngoal, and rules.',12),('Prepare','Prepare data and\nestimate future conditions.',0),('Model','Connect choices,\nresults, and limits.',2),('Compare','Check plans and\nwhat the model assumes.',34),('Act','Use the plan and\nmeasure the result.',54)]
for j,(t,b,ico) in enumerate(process):
    x=52+j*174
    s.circle(x+39,145,78,c='ink' if j==4 else 'paper');s.icon(ico,x+61,165,35,c='cyan' if j==4 else 'cyanDark')
    s.text(f'{j+1:02}  {t}',x,250,160,47,30,bold=True,family=FH,align='ctr');s.text(b,x+1,315,158,91,18,align='ctr')
    if j<4:s.line(x+122,184,x+169,184,'blue',2,True)
s.path([(838,417),(838,452),(131,452),(131,416)],stroke='cyanDark',sw=1.5)
s.line(131,444,131,416,'cyanDark',1.5,True)
s.rect(312,433,340,38,c='white');s.text('Use results to improve the next decision.',312,440,340,31,17,align='ctr',c='cyanDark')
slides.append(s)

s=Slide(7,'Methods used in prescriptive analytics')
step(s,1,'Mathematical\noptimization','Finds the best result for a goal\nwhile following the rules.',52,125,260,26)
step(s,2,'Constraint\nprogramming','Finds a plan that follows\ndetailed rules.',355,125,260,53)
step(s,3,'Simulation','Tests possible results when\nconditions change.',658,125,250,35)
s.line(330,127,330,421);s.line(633,127,633,421)
s.text('Share limited stock',52,360,260,54,20,c='cyanDark',bold=True);s.text('Plan working hours',355,360,260,54,20,c='cyanDark',bold=True);s.text('Compare staff plans',658,360,250,54,20,c='cyanDark',bold=True)
band(s,'Simulation tests plans; a rule or optimization method selects a plan.',y=443,size=18)
slides.append(s)

s=Slide(8,'What does the model produce?')
s.text('An action the team can use',52,112,856,49,31,family=FH,bold=True,c='cyanDark')
outputs=[('Work plan','Who works and when',36,52,198),('Order plan','What to buy and how much',0,502,198),('Request list','Which requests to answer first',55,52,332),('Plan options','Several plans and expected results',34,502,332)]
for t,b,ico,x,y in outputs:
    s.icon(ico,x,y,50,c='ink');s.text(t,x+75,y-2,325,43,30,family=FH,bold=True);s.text(b,x+75,y+53,325,62,21)
band(s,'The team should also see the main reasons behind the suggestion.',y=447,size=18)
slides.append(s)

s=Slide(9,'Decisions prescriptive analytics can support')
questions=[('What should we buy?','Choose products and order amounts.',0),('When should work happen?','Choose times for tasks or repairs.',1),('Where should products go?','Decide how much each store receives.',32),('Which request should come first?','Choose the order for answering requests.',55)]
for j,(q,b,ico) in enumerate(questions):
    y=120+j*83
    s.icon(ico,62,y+7,39,c='cyanDark');s.text(q,129,y,360,47,27,family=FH,bold=True)
    s.line(522,y+26,560,y+26,'blue',1.5,True);s.text(b,588,y+1,320,66,20)
    if j<3:s.line(129,y+73,908,y+73)
s.text('Each answer leads to a choice the team can act on.',52,461,856,32,19,c='muted')
slides.append(s)

s=Slide(10,'The meaning of the best choice')
s.text('The best choice depends on the goal.',52,110,856,45,28,c='cyanDark',family=FH,bold=True)
goals=[('Lower cost','Spend less money',10,52,193),('Faster service','Reduce waiting time',1,505,193),('Less waste','Avoid unnecessary materials',0,52,316),('Better service','Meet more customer needs',12,505,316)]
for t,b,ico,x,y in goals:
    s.icon(ico,x,y,44,c='cyanDark');s.text(t,x+67,y-1,334,45,30,c='ink',family=FH,bold=True);s.text(b,x+67,y+51,334,55,21,c='ink')
s.line(480,193,480,421,c='blue');band(s,'The business balances its goals and keeps the rules the plan must follow.',y=449,c='paper',ink='ink',size=18)
slides.append(s)

s=Slide(11,'Short-term and long-term decisions')
s.line(97,248,862,248,c='blue',sw=3)
time=[('Today','Choose which tasks\nto complete first.',1),('Next week','Plan working\nhours.',36),('Next month','Decide how much stock\neach store receives.',0),('Next year','Choose where to add\nstorage space.',32)]
for j,(t,b,ico) in enumerate(time):
    cx=115+j*243
    s.icon(ico,cx-22,135,44,c='cyanDark');s.circle(cx-8,240,16,c='ink');s.text(t,cx-78,194,156,43,29,bold=True,family=FH,align='ctr');s.text(b,cx-83,290,184,92,20,align='ctr')
band(s,'Long-term decisions need estimates about conditions further in the future.',y=443,size=18)
slides.append(s)

s=Slide(12,'Connected decisions')
s.text('One decision can affect another.',52,110,856,40,28,family=FH,bold=True,c='cyanDark')
links=[('More products','More storage space',0),('More sales','More workers',12),('Faster delivery','Possibly higher cost',1)]
for j,(left,right,ico) in enumerate(links):
    y=174+j*80
    s.icon(ico,67,y+3,43,c='ink');s.text(left,142,y+3,306,45,27,bold=True,family=FH)
    s.line(456,y+26,515,y+26,'cyanDark',2,True);s.text(right,550,y+3,356,45,27,bold=True,family=FH)
    if j<2:s.line(142,y+64,908,y+64)
band(s,'Considering the connections helps avoid creating a new problem.',y=443,size=18)
slides.append(s)

s=Slide(13,'How machine learning helps')
s.rect(52,116,395,52,c='paper',r=True);s.text('Machine learning estimates',72,127,355,39,29,family=FH,bold=True)
s.rect(510,116,398,52,c='ink',r=True);s.text('Prescriptive model suggests',530,127,355,39,29,c='white',family=FH,bold=True)
ml=[('How much customers will buy','How much stock to order',0),('When a machine may fail','When to plan a repair',2),('How many requests may arrive','How many workers to assign',12)]
for j,(l,r,ico) in enumerate(ml):
    y=200+j*75
    s.icon(ico,65,y,35,c='cyanDark');s.text(l,120,y-1,316,62,20);s.line(456,y+22,496,y+22,'blue',1.5,True);s.text(r,531,y-1,355,62,20)
band(s,'Predictions are inputs. Estimates can also come from people or other methods.',y=443,size=17.5)
slides.append(s)

s=Slide(14,'Levels of automation')
s.text('Automation = allowing a computer to do an action.',52,107,856,40,23,c='cyanDark')
auto=[('Suggestion only','System gives options.\nA person chooses and acts.',12),('Approval needed','System prepares a plan.\nA person approves it.',54),('Automatic action','System acts within agreed rules\nand records its actions.',2)]
for j,(t,b,ico) in enumerate(auto):
    x=52+j*302
    s.circle(x+82,170,82,c='ink' if j==2 else 'paper');s.icon(ico,x+105,192,35,c='cyan' if j==2 else 'cyanDark')
    s.text(t,x,282,253,49,31,family=FH,bold=True,align='ctr');s.text(b,x,351,253,72,19,align='ctr')
    if j<2:s.line(x+207,210,x+282,210,'blue',2,True)
band(s,'Choose the level carefully and provide a way to stop automatic actions.',y=443,size=18)
slides.append(s)

s=Slide(15,'Fairness in decision-making')
s.text('A plan can meet a business goal\nand still affect people unfairly.',52,120,470,78,30,family=FH,bold=True)
s.text('A work plan might give the same workers\nthe busiest hours every week.',52,238,460,81,23)
s.text('Include fairness in the goals or rules.',52,365,467,61,25,c='cyanDark',bold=True,family=FH)
s.rect(567,118,341,317,c='paper',r=True);s.icon(36,695,137,58,c='cyanDark')
for y,t in [(232,'Breaks'),(291,'Reasonable working hours'),(350,'Sharing difficult tasks fairly')]:
    s.circle(591,y+5,17,c='cyan');s.text(t,624,y,262,67,22)
slides.append(s)

s=Slide(16,'Thank you');s.text('Thank you',52,229,856,82,54,bold=True,family=FH,align='ctr',name='Slide title');slides.append(s)
assert len(slides)==16
markdown=(ROOT/'prescriptive-analytics-presentation.md').read_text(encoding='utf-8')
script=(ROOT/'prescriptive-analytics-script.md').read_text(encoding='utf-8')
blocks=re.split(r'(?m)^<!-- Slide \d+ -->\s*',markdown)[1:]
scripts=re.split(r'(?m)^## Slide \d+: [^\n]+\n',script)[1:]
assert len(blocks)==len(scripts)==15
for i,s in enumerate(slides[:15]):
    full=re.sub(r'<!--.*?-->',lambda m:'\n'+m.group(0)[4:-3].strip()+'\n',blocks[i],flags=re.S)
    s.note(scripts[i].strip()+'\n\n--- Full content from the approved Markdown ---\n'+full.strip())

slides[-1].note('Thank you')

def relationships(rows):
    root=el('{'+PR+'}Relationships',nsmap={None:PR})
    for ident,typ,target in rows:sub(root,'{'+PR+'}Relationship',Id=ident,Type=R+'/'+typ,Target=target)
    return E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
def notes(s):
    n=el(pq('notes'),nsmap=NS);cs=sub(n,pq('cSld'));st=sub(cs,pq('spTree'))
    nv=sub(st,pq('nvGrpSpPr'));sub(nv,pq('cNvPr'),id=1,name='');sub(nv,pq('cNvGrpSpPr'));sub(nv,pq('nvPr'));sub(st,pq('grpSpPr'))
    sp=sub(st,pq('sp'));nv=sub(sp,pq('nvSpPr'));sub(nv,pq('cNvPr'),id=2,name='Speaker notes');sub(nv,pq('cNvSpPr'));sub(sub(nv,pq('nvPr')),pq('ph'),type='body',idx=1);sub(sp,pq('spPr'))
    tx=sub(sp,pq('txBody'));sub(tx,aq('bodyPr'));sub(tx,aq('lstStyle'))
    for line in s.notes.splitlines():
        p=sub(tx,aq('p'));r=sub(p,aq('r'));rp=sub(r,aq('rPr'),lang='en-US',sz=1200);sub(rp,aq('latin'),typeface=FB);sub(r,aq('t')).text=line
    sub(sub(n,pq('clrMapOvr')),aq('masterClrMapping'))
    return E.tostring(n,encoding='UTF-8',xml_declaration=True,standalone=True)

def xml(e):return E.tostring(e,encoding='UTF-8',xml_declaration=True,standalone=True)
def empty_tree(cs):
    st=sub(cs,pq('spTree'));nv=sub(st,pq('nvGrpSpPr'));sub(nv,pq('cNvPr'),id=1,name='Root');sub(nv,pq('cNvGrpSpPr'));sub(nv,pq('nvPr'))
    gp=sub(st,pq('grpSpPr'));xf=sub(gp,aq('xfrm'))
    for t,attrs in [('off',{'x':0,'y':0}),('ext',{'cx':0,'cy':0}),('chOff',{'x':0,'y':0}),('chExt',{'cx':0,'cy':0})]:sub(xf,aq(t),**attrs)
def clrmap(parent):sub(parent,pq('clrMap'),bg1='lt1',tx1='dk1',bg2='lt2',tx2='dk2',accent1='accent1',accent2='accent2',accent3='accent3',accent4='accent4',accent5='accent5',accent6='accent6',hlink='hlink',folHlink='folHlink')
data={}
data['_rels/.rels']=relationships([('rId1','officeDocument','ppt/presentation.xml')])
pres=el(pq('presentation'),nsmap=NS);mi=sub(pres,pq('sldMasterIdLst'));sub(mi,pq('sldMasterId'),id=2147483648,**{'{'+R+'}id':'rIdMaster'})
ni=sub(pres,pq('notesMasterIdLst'));sub(ni,pq('notesMasterId'),**{'{'+R+'}id':'rIdNotesMaster'})
li=sub(pres,pq('sldIdLst'))
for i in range(1,17):sub(li,pq('sldId'),id=255+i,**{'{'+R+'}id':f'rIdSlide{i}'})
sub(pres,pq('sldSz'),cx=9144000,cy=5143500,type='screen16x9');sub(pres,pq('notesSz'),cx=6858000,cy=9144000)
ds=sub(pres,pq('defaultTextStyle'));pp=sub(ds,aq('defPPr'));dr=sub(pp,aq('defRPr'));sub(dr,aq('latin'),typeface=FB)
data['ppt/presentation.xml']=xml(pres)
data['ppt/_rels/presentation.xml.rels']=relationships([('rIdMaster','slideMaster','slideMasters/slideMaster1.xml'),('rIdNotesMaster','notesMaster','notesMasters/notesMaster1.xml')]+[(f'rIdSlide{i}','slide',f'slides/slide{i}.xml') for i in range(1,17)])
master=el(pq('sldMaster'),nsmap=NS);empty_tree(sub(master,pq('cSld'),name='Monochrome'));clrmap(master)
ll=sub(master,pq('sldLayoutIdLst'));sub(ll,pq('sldLayoutId'),id=2147483649,**{'{'+R+'}id':'rIdLayout'})
styles=sub(master,pq('txStyles'))
for typ in ['titleStyle','bodyStyle','otherStyle']:
    st=sub(styles,pq(typ));pp=sub(st,aq('lvl1pPr'));dr=sub(pp,aq('defRPr'),sz=1800);sub(dr,aq('latin'),typeface=FB);sub(dr,aq('ea'),typeface=FB);sub(dr,aq('cs'),typeface=FB)
data['ppt/slideMasters/slideMaster1.xml']=xml(master)
data['ppt/slideMasters/_rels/slideMaster1.xml.rels']=relationships([('rIdLayout','slideLayout','../slideLayouts/slideLayout1.xml'),('rIdTheme','theme','../theme/theme1.xml')])
layout=el(pq('sldLayout'),nsmap=NS,type='blank',preserve='1');empty_tree(sub(layout,pq('cSld'),name='Blank'));sub(sub(layout,pq('clrMapOvr')),aq('masterClrMapping'))
data['ppt/slideLayouts/slideLayout1.xml']=xml(layout)
data['ppt/slideLayouts/_rels/slideLayout1.xml.rels']=relationships([('rIdMaster','slideMaster','../slideMasters/slideMaster1.xml')])
nm=el(pq('notesMaster'),nsmap=NS);empty_tree(sub(nm,pq('cSld')));clrmap(nm);ns=sub(nm,pq('notesStyle'));pp=sub(ns,aq('lvl1pPr'));dr=sub(pp,aq('defRPr'),sz=1200);sub(dr,aq('latin'),typeface=FB)
data['ppt/notesMasters/notesMaster1.xml']=xml(nm)
data['ppt/notesMasters/_rels/notesMaster1.xml.rels']=relationships([('rIdTheme','theme','../theme/theme1.xml')])
theme=el(aq('theme'),nsmap={'a':A},name='Monochrome');te=sub(theme,aq('themeElements'));cs=sub(te,aq('clrScheme'),name='Monochrome')
for tag,c in [('dk1','303030'),('lt1','FFFFFF'),('dk2','666666'),('lt2','F3F3F3'),('accent1','303030'),('accent2','666666'),('accent3','888888'),('accent4','AAAAAA'),('accent5','CCCCCC'),('accent6','EEEEEE'),('hlink','303030'),('folHlink','666666')]:sub(sub(cs,aq(tag)),aq('srgbClr'),val=c)
fs=sub(te,aq('fontScheme'),name='Roboto')
for typ in ['majorFont','minorFont']:
    f=sub(fs,aq(typ))
    for tag in ['latin','ea','cs']:sub(f,aq(tag),typeface=FB)
fmt=sub(te,aq('fmtScheme'),name='Monochrome');fl=sub(fmt,aq('fillStyleLst'))
for j in range(3):sub(sub(fl,aq('solidFill')),aq('schemeClr'),val='phClr')
lns=sub(fmt,aq('lnStyleLst'))
for w in [9525,19050,28575]:
    ln=sub(lns,aq('ln'),w=w,cap='flat',cmpd='sng',algn='ctr');sub(sub(ln,aq('solidFill')),aq('schemeClr'),val='phClr');sub(ln,aq('prstDash'),val='solid')
effects=sub(fmt,aq('effectStyleLst'))
for j in range(3):sub(sub(effects,aq('effectStyle')),aq('effectLst'))
bg=sub(fmt,aq('bgFillStyleLst'))
for j in range(3):sub(sub(bg,aq('solidFill')),aq('schemeClr'),val='phClr')
data['ppt/theme/theme1.xml']=xml(theme)
for i,s in enumerate(slides,1):
    data[f'ppt/slides/slide{i}.xml']=s.export()
    data[f'ppt/slides/_rels/slide{i}.xml.rels']=relationships([('rId1','slideLayout','../slideLayouts/slideLayout1.xml'),('rId2','notesSlide',f'../notesSlides/notesSlide{i}.xml')])
    data[f'ppt/notesSlides/notesSlide{i}.xml']=notes(s)
    data[f'ppt/notesSlides/_rels/notesSlide{i}.xml.rels']=relationships([('rId1','notesMaster','../notesMasters/notesMaster1.xml'),('rId2','slide',f'../slides/slide{i}.xml')])
ct=el('{'+CT+'}Types',nsmap={None:CT});sub(ct,'{'+CT+'}Default',Extension='rels',ContentType='application/vnd.openxmlformats-package.relationships+xml');sub(ct,'{'+CT+'}Default',Extension='xml',ContentType='application/xml')
types={'ppt/presentation.xml':'presentation','ppt/slideMasters/slideMaster1.xml':'slideMaster','ppt/slideLayouts/slideLayout1.xml':'slideLayout','ppt/notesMasters/notesMaster1.xml':'notesMaster'}
for i in range(1,17):types[f'ppt/slides/slide{i}.xml']='slide';types[f'ppt/notesSlides/notesSlide{i}.xml']='notesSlide'
for part,t in types.items():sub(ct,'{'+CT+'}Override',PartName='/'+part,ContentType='application/vnd.openxmlformats-officedocument.presentationml.'+t+'.main+xml' if t=='presentation' else 'application/vnd.openxmlformats-officedocument.presentationml.'+t+'+xml')
sub(ct,'{'+CT+'}Override',PartName='/ppt/theme/theme1.xml',ContentType='application/vnd.openxmlformats-officedocument.theme+xml')
data['[Content_Types].xml']=xml(ct)
with ZipFile(OUT,'w',ZIP_DEFLATED) as z:
    for n,b in data.items():z.writestr(n,b)
assert all(b'slidesgo' not in b.lower() for b in data.values())
assert all(len(t['lines'])==1 for s in slides for t in s.texts if t['text']==s.title)
(BASE/'layout-audit-original-revised.json').write_text(json.dumps([{'slide':s.n,'title':s.title,'text':s.metrics} for s in slides],indent=2),encoding='utf-8')
print(f'Built {OUT.name}: {len(slides)} slides, original blue-and-cyan design, light background.')
