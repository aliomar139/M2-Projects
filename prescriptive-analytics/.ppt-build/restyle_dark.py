from pathlib import Path
import re
B=Path(__file__).parent
s=(B/'build_final.py').read_text(encoding='utf-8')
s=s.replace('prescriptive-analytics-presentation-final.pptx','prescriptive-analytics-presentation-dark.pptx').replace("PRE=BASE/'previews-final'", "PRE=BASE/'previews-dark'")
s=re.sub(r'T=\{[^\n]+',"T={'ink':'FFFFFF','deep':'294559','muted':'CFDAE2','cyan':'5FD0DB','cyanDark':'5FD0DB','orange':'5FD0DB','paper':'294559','line':'869FB2','white':'435D74','blue':'A4B7C6'}",s)
s=s.replace("        # Original editable line artwork", "        c='cyan'\n        # Original editable line artwork")
s=s.replace("layout-audit-final.json", "layout-audit-dark.json")
s=s.replace("Built {OUT.name}: {len(slides)} slides, original icons, Roboto, monochrome.","Built {OUT.name}: {len(slides)} slides, original icons, Roboto, uniform slate background.")
s=s.replace("name='Monochrome'", "name='Slate and cyan'")
(B/'build_dark.py').write_text(s,encoding='utf-8')
