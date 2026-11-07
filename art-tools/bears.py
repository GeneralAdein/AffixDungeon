from pxlib import *
BROWN=['#140c08','#2a1910','#452a19','#634026','#825a36','#a07a52']
BMUZ=['#2e2118','#4f3a2a','#725840','#927658','#b09474']
GRIZ=['#110c0a','#241a15','#3a2c23','#544234','#6e5a48','#8c7a66']
GMUZ=['#2a2019','#4a3a2d','#6c5a46','#8d7a62','#ad9a80']
POLAR=['#36404d','#56636f','#7d8a97','#a3aeb8','#c8d0d7','#e9eef1']
PMUZ=['#6b7682','#929ea9','#b7c0c8','#d8dee3','#f3f6f7']
CLAW='#d8cfb8'; DARK='#0b0909'

def brown():
    s=Sprite('#0a0605')
    s.add(ellipse(24,33,18,11)|ellipse(24,23,14,8),BROWN,dither=True,noise=.3,soft=1.8,bias=-.08)
    for x0 in range(9,40,3): s.px([(x0,21+abs(24-x0)//4),(x0,22+abs(24-x0)//4)],'#2a1910')
    s.add(mir(chain([(15,35),(14,45)],3.6,3.2)),BROWN,dither=True)
    for x in (11,13,15,17): s.pxm([(x,46),(x,47)],CLAW)
    s.add(mir(ellipse(16.5,19.5,3,3)),BROWN)
    s.add(mir(ellipse(16.7,19.8,1.4,1.4)),['#1a100a','#2a1910'],flat=0,ao=False)
    s.add(ellipse(24,26,9.5,8),BROWN,soft=1.5,dither=True,bias=.06)
    s.add(ellipse(24,31.5,5.4,4.4),BMUZ,soft=1.2)
    s.add(ellipse(24,29.6,2.4,1.5),['#050404','#141010','#2a2220'])
    s.maskpx(poly([(20.5,32),(27.5,32),(26.5,36),(21.5,36)]),'#2a0a0e')
    s.px([(21,32),(27,32),(21,33),(27,33),(22,35),(26,35)],'#e6dcc4')
    s.px([(23,34),(24,34),(25,34)],'#7a2a30')
    s.pxm([(20,24),(21,24),(20,25),(21,25)],DARK); s.pxm([(21,24)],'#e0a040')
    s.maskpx(mir(chain([(18,22.2),(21.8,23.2)],0.45)),'#1e120c')
    return s

def grizzly():
    s=Sprite('#090605')
    s.add(mir(chain([(19,38),(17,46)],3.8,3.4)),GRIZ,dither=True)
    for x in (13,15,17,19): s.pxm([(x,47)],CLAW)
    s.add(ellipse(24,32,12,12),GRIZ,dither=True,noise=.3)
    s.add(ellipse(24,33,6.5,8),GMUZ,dither=True,bias=-.1)
    s.add(ellipse(24,22,15,7),GRIZ,dither=True,noise=.3,soft=1.6)
    s.add(mir(chain([(12,23),(7,15),(6,7)],3.6,2.8)),GRIZ,dither=True)
    for i,(x,y) in enumerate([(3,3),(5,2),(7,2),(9,3)]):
        s.pxm([(x,y),(x,y+1),(x,y+2)],CLAW)
    s.add(mir(ellipse(17,11.5,2.6,2.6)),GRIZ)
    s.add(mir(ellipse(17.2,11.8,1.2,1.2)),['#1a120d','#241a15'],flat=0,ao=False)
    s.add(ellipse(24,17,8.5,7.5),GRIZ,soft=1.4,dither=True)
    s.add(ellipse(24,22.5,5.2,4.6),GMUZ,soft=1.2)
    s.add(ellipse(24,19.4,2.2,1.4),['#050404','#141010','#2a2220'])
    s.maskpx(poly([(21,22),(27,22),(26.2,27),(21.8,27)]),'#2a0a0e')
    s.px([(22,22),(26,22),(22,23),(26,23),(22,26),(26,26)],'#e6dcc4')
    s.px([(23,25),(24,25),(25,25)],'#8a2a32')
    s.pxm([(20,15),(21,15)],DARK); s.pxm([(20,15)],'#e0a030')
    s.maskpx(mir(chain([(18,13),(21.5,14.5)],0.5)),'#110c0a')
    for (x,y) in [(12,19),(15,17),(18,16),(30,16),(33,17),(36,19),(10,22),(38,22),(14,21),(34,21),(20,14),(28,14)]:
        s.px([(x,y)],'#b8ab98')
    return s

def polar():
    s=Sprite('#151a22')
    s.add(ellipse(24,31,18,11)|ellipse(24,23,12,7),POLAR,dither=True,soft=1.8,bias=-.18)
    s.add(mir(chain([(14,34),(13,45)],3.8,3.4)),POLAR,dither=True,bias=-.05)
    for x in (10,12,14,16): s.pxm([(x,46),(x,47)],'#1c1c22')
    s.add(mir(ellipse(18.2,21.5,2.2,2.2)),POLAR)
    s.add(mir(ellipse(18.3,21.7,1,1)),['#3a3440','#56505c'],flat=0,ao=False)
    s.add(ellipse(24,27,7.5,7),POLAR,soft=1.4,dither=True,bias=.12)
    s.add(ellipse(24,34,4.6,5.6),PMUZ,soft=1.2,bias=.05)
    s.add(ellipse(24,37.6,2.4,1.6),['#050506','#121316','#262a30'])
    s.maskpx(chain([(21.5,40.5),(26.5,40.5)],0.5),'#2a2e36')
    s.px([(22,41),(26,41)],'#e8eef2')
    s.pxm([(20,26),(21,26)],DARK); s.pxm([(21,26)],'#7fd8ff')
    s.maskpx(mir(chain([(18.5,24.3),(21.8,25)],0.4)),'#56636f')
    for (x,y,a) in [(19,43,230),(29,43,230),(17,44,180),(31,45,180),(22,44,150),(27,45,150),(15,42,120),(33,42,120)]:
        s.px([(x,y)],'#cfefff',a)
    return s

if __name__=='__main__':
    imgs=[brown().render(),grizzly().render(),polar().render()]
    sheet(imgs,scale=6,cols=3).save('bears.png')
    import base64,io,json
    out={}
    for k,im in zip(['brownbear','grizzly','polarbear'],imgs):
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('bears.json','w'))
