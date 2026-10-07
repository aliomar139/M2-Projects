from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from collections import Counter
from copy import deepcopy
import re, json, html, posixpath

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
NS = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
U = 9525
z = ZipFile(ROOT / 'Big Data Infographics by Slidesgo.pptx')
theme_part='ppt/slides/slide1.xml'
theme_chain=[]
for typ in ['slideLayout','slideMaster','theme']:
    folder,name=posixpath.split(theme_part)
    rel=E.fromstring(z.read(folder+'/_rels/'+name+'.rels'))
    target=next(r.get('Target') for r in rel if r.get('Type').endswith('/'+typ))
    theme_part=posixpath.normpath(posixpath.join(folder,target))
    theme_chain.append(theme_part)
print('Theme chain:',theme_chain)
theme = E.fromstring(z.read(theme_part))
COLORS = {}
for e in theme.find('a:themeElements/a:clrScheme', NS):
    c = e[0]
    COLORS[E.QName(e).localname] = c.get('val') if E.QName(c).localname == 'srgbClr' else c.get('lastClr')
COLORS.update({'bg1':'FFFFFF', 'tx1':'000000', 'bg2':'FFFFFF','tx2':'435D74'})

def clr(e, default='none'):
    if e is None: return default
    if e.find('a:noFill', NS) is not None: return 'none'
    f=e.find('a:solidFill',NS)
    if f is None: return default
    c=f[0]
    return '#' + (c.get('val') if E.QName(c).localname=='srgbClr' else COLORS.get(c.get('val'),'435D74'))

def path_str(p):
    s=[]
    for e in p:
        typ=E.QName(e).localname
        pts=[(v.get('x'),v.get('y')) for v in e]
        if typ=='close': s.append('Z')
        elif typ in ('moveTo','lnTo'): s.append(('M' if typ=='moveTo' else 'L') + ' '.join(pts[0]))
        elif typ=='cubicBezTo': s.append('C'+' '.join(' '.join(v) for v in pts))
    return ' '.join(s)

def render(e, include_text=True):
    typ=E.QName(e).localname
    if typ=='grpSp':
        x=e.find('p:grpSpPr/a:xfrm',NS)
        if x is None: return ''
        off,ext,ch,ce=[x.find('a:'+v,NS) for v in ['off','ext','chOff','chExt']]
        sx=int(ext.get('cx'))/max(1,int(ce.get('cx')))
        sy=int(ext.get('cy'))/max(1,int(ce.get('cy')))
        trans=f'translate({int(off.get("x"))/U} {int(off.get("y"))/U}) scale({sx} {sy}) translate({-int(ch.get("x"))/U} {-int(ch.get("y"))/U})'
        return f'<g transform="{trans}">' + ''.join(render(v,include_text) for v in e if E.QName(v).localname in ['sp','grpSp','cxnSp'])+'</g>'
    if typ not in ['sp','cxnSp']: return ''
    sp=e.find('p:spPr',NS)
    if sp is None:return ''
    x=sp.find('a:xfrm',NS)
    if x is None:return ''
    off,ext=x.find('a:off',NS),x.find('a:ext',NS)
    xx,yy=int(off.get('x'))/U,int(off.get('y'))/U
    w,h=int(ext.get('cx'))/U,int(ext.get('cy'))/U
    fill=clr(sp)
    ln=sp.find('a:ln',NS)
    stroke=clr(ln)
    sw=float(ln.get('w','9525'))/U if ln is not None else 0
    angle=int(x.get('rot','0'))/60000
    rotate=f'rotate({angle} {w/2} {h/2})' if angle else ''
    flip=''
    if x.get('flipH')=='1':flip+=f'translate({w} 0) scale(-1 1) '
    if x.get('flipV')=='1':flip+=f'translate(0 {h}) scale(1 -1) '
    attrs=f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"'
    pieces=[]
    cu=sp.find('a:custGeom',NS)
    pg=sp.find('a:prstGeom',NS)
    if cu is not None:
        for p in cu.findall('a:pathLst/a:path',NS):
            pw,ph=float(p.get('w','1')),float(p.get('h','1'))
            pieces.append(f'<g transform="scale({w/pw} {h/ph})"><path d="{path_str(p)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw/max(w/pw,h/ph,0.000001)}" /></g>')
    elif pg is not None:
        geom=pg.get('prst')
        if geom=='ellipse':pieces.append(f'<ellipse cx="{w/2}" cy="{h/2}" rx="{w/2}" ry="{h/2}" {attrs}/>')
        elif geom in ['straightConnector1','bentConnector2','bentConnector3']:pieces.append(f'<path d="M0 0 L{w} {h}" {attrs}/>')
        elif geom in ['triangle','rightArrow','homePlate']:
            points=f'0,0 {w},{h/2} 0,{h}'
            pieces.append(f'<polygon points="{points}" {attrs}/>')
        else:
            rr=min(w,h)*0.15 if 'round' in geom.lower() else 0
            pieces.append(f'<rect width="{w}" height="{h}" rx="{rr}" {attrs}/>')
    if include_text:
        tx=e.find('p:txBody',NS)
        if tx is not None:
            body=tx.find('a:bodyPr',NS)
            inset=int(body.get('lIns','91440'))/U if body is not None else 5
            top=int(body.get('tIns','45720'))/U if body is not None else 3
            ph=e.find('p:nvSpPr/p:nvPr/p:ph',NS)
            title=ph is not None and ph.get('type') in ['title','ctrTitle']
            for p in tx.findall('a:p',NS):
                texts=p.findall('a:r',NS)
                string=''.join(r.findtext('a:t','',NS) for r in texts)
                if not string:continue
                rp=texts[0].find('a:rPr',NS) if texts else None
                er=p.find('a:endParaRPr',NS)
                fs=float((rp.get('sz') if rp is not None else None) or (er.get('sz') if er is not None else None) or (3200 if title else 1100))/75
                fn=(rp.find('a:latin',NS) if rp is not None else None)
                family=fn.get('typeface') if fn is not None else ('Fira Sans Extra Condensed' if title else 'Roboto')
                color=clr(rp,clr(er,'#435D74'))
                pp=p.find('a:pPr',NS)
                align=pp.get('algn','l') if pp is not None else 'l'
                anchor='middle' if align=='ctr' else 'end' if align=='r' else 'start'
                xp=w/2 if anchor=='middle' else w-inset if anchor=='end' else inset
                # Native paragraph runs are combined only for source preview inspection.
                pieces.append(f'<text x="{xp}" y="{top+fs}" font-family="{html.escape(family)}" font-size="{fs}" text-anchor="{anchor}" fill="{color}">{html.escape(string)}</text>')
                top+=fs*1.2
    return f'<g transform="translate({xx} {yy}) {rotate} {flip}">' + ''.join(pieces)+'</g>'

def svg(body,w=960,h=540):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>{body}</svg>'

assets=[]
for i in range(1,35):
    root=E.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
    st=root.find('p:cSld/p:spTree',NS)
    (BASE/'source'/f'slide-{i:02}.svg').write_text(svg(''.join(render(e) for e in st)),encoding='utf-8')
    for g in st.findall('.//p:grpSp',NS):
        if g.xpath('.//a:t[text()]',namespaces=NS):continue
        x=g.find('p:grpSpPr/a:xfrm',NS)
        if x is None:continue
        ex=x.find('a:ext',NS);w,h=int(ex.get('cx'))/U,int(ex.get('cy'))/U
        if not (15<w<105 and 15<h<105 and .65<w/h<1.5):continue
        custom=g.findall('.//a:custGeom',NS)
        if not custom:continue
        gc=deepcopy(g)
        off=gc.find('p:grpSpPr/a:xfrm/a:off',NS);off.set('x','0');off.set('y','0')
        out=BASE/'assets';out.mkdir(exist_ok=True)
        idx=len(assets)
        (out/f'icon-{idx:03}.xml').write_bytes(E.tostring(gc))
        (out/f'icon-{idx:03}.svg').write_text(svg(render(gc,False),w,h),encoding='utf-8')
        assets.append({'index':idx,'sourceSlide':i,'id':g.find('p:nvGrpSpPr/p:cNvPr',NS).get('id'),'w':w,'h':h})

(BASE/'template-assets.json').write_text(json.dumps({'colors':COLORS,'icons':assets},indent=2),encoding='utf-8')
print(json.dumps({'colors':COLORS,'iconCount':len(assets)}))
