from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

BASE=Path(__file__).resolve().parent
PRE=BASE/'previews'
FD=Path('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts')
fonts={('Fira Sans Extra Condensed',False):FD/'FiraSansExtraCondensed-Regular.ttf',('Fira Sans Extra Condensed',True):FD/'FiraSansExtraCondensed-SemiBold.ttf',('Roboto',False):FD/'Roboto-Regular.ttf',('Roboto',True):FD/'Roboto-Bold.ttf'}
for jf in sorted(PRE.glob('*.text.json')):
    name=jf.name.replace('.text.json','')
    im=Image.open(PRE/(name+'.png')).convert('RGB')
    scale=im.width/960
    dr=ImageDraw.Draw(im)
    for t in json.loads(jf.read_text(encoding='utf-8')):
        f=ImageFont.truetype(str(fonts[(t['family'],t['bold'])]),round(t['size']*scale))
        for i,line in enumerate(t['lines']):
            xx=t['x']*scale
            if t['align']=='ctr':xx+=(t['w']*scale-dr.textlength(line,font=f))/2
            elif t['align']=='r':xx+=t['w']*scale-dr.textlength(line,font=f)
            # Align the visible glyphs consistently inside the authored text boxes.
            dr.text((xx,(t['y']+i*t['lh'])*scale),line,font=f,fill='#'+t['c'],anchor='lt')
    im.resize((1280,720),Image.Resampling.LANCZOS).save(PRE/(name+'-final.png'))

thumbw,thumbh=384,216
sheet=Image.new('RGB',(3*thumbw,5*(thumbh+30)),'#E4EBEF');d=ImageDraw.Draw(sheet)
for j,p in enumerate(sorted(PRE.glob('*-final.png'))):
    x=(j%3)*thumbw;y=(j//3)*(thumbh+30)
    sheet.paste(Image.open(p).resize((thumbw,thumbh),Image.Resampling.LANCZOS),(x,y))
    d.text((x+12,y+thumbh+7),p.name.replace('-final.png',''),fill='#294559')
sheet.save(BASE/'deck-contact.png')
print('Rendered and labelled 15 final slide previews.')
