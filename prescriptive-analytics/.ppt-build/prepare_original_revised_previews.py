from pathlib import Path
p=Path(__file__).parent
s=(p/'finish_previews.py').read_text()
s=s.replace("PRE=BASE/'previews'", "PRE=BASE/'previews-original-revised'")
s=s.replace('5*(thumbh+30)','6*(thumbh+30)').replace('deck-contact.png','deck-contact-original-revised.png').replace('15 final','16 final')
exec(compile(s,str(p/'finish_original_revised.py'),'exec'))
