import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import pxlib; pxlib.FLAT['on']=True
from pxlib import *

def dragon(main, belly, wing, horn, eye='#ffd040', k=1.0, wings=True, front_legs=True, tail_tip='spade', breath=None, outline='#08060a', extra=None, neck_len=1.0, horns=2, bone=False):
    s=Sprite(outline)
    def T(x,y): return (24+(x-24)*k, 46-(46-y)*k)
    def E(cx,cy,rx,ry,rot=0): x,y=T(cx,cy); return ellipse(x,y,rx*k,ry*k,rot)
    def C(pts,r1,r2=None): return chain([T(*p) for p in pts], r1*k, (r2 if r2 is not None else r1)*k)
    def Pp(pts): return poly([T(*p) for p in pts])
    def px(pts,c,a=255): s.px([tuple(int(round(v)) for v in T(x,y)) for x,y in pts],c,a)
    # wings
    if wings:
        wm=Pp([(20,22),(11,7),(2,3),(4,11),(0,19),(6,21),(2,29),(10,27),(11,34),(18,29)])
        s.add(mir(wm),wing,bias=-.05)
        for tip in [(2,3),(0,19),(2,29),(11,34)]:
            s.maskpx(mir(C([(19,22),(11,7),tip],.45)) if tip==(2,3) else mir(C([(11,7),tip],.4)),horn[1])
        s.maskpx(mir(C([(19,22),(11,7)],.7)),main[1])
    # tail
    s.add(C([(29,40),(38,43),(44,38),(44,30),(41,25)],3,1.2),main)
    if tail_tip=='spade': s.add(Pp([(41,25),(38,21),(41,17),(44,21)]),horn)
    elif tail_tip=='stinger': s.add(Pp([(41,25),(39,18),(42,22)]),horn); px([(39,18),(39,17)],'#e0f080')
    # hind legs
    s.add(mir(C([(17,37),(14,43),(15,46)],3.4,2.6)),main)
    for x in (12,14,16): s.px([(int(T(x,46)[0]),int(T(x,46)[1])),(int(47-T(x,46)[0]),int(T(x,46)[1]))],'#e8e0c8')
    # body + belly
    s.add(E(24,34,10.5,9.5),main,soft=1.4)
    if bone:
        for y in (28,31,34,37): s.maskpx(E(24,y,8,.8)&E(24,34,9.5,8.5),'#e8e0c8')
        s.maskpx(C([(24,26),(24,42)],.8),'#d8d0b8')
    else:
        s.add(E(24,36,5.6,7.5),belly,soft=1.2,bias=.1)
        for y in (32,35,38,41): s.maskpx(E(24,y,5,.5)&E(24,36,5.4,7.2),belly[1])
    # front legs
    if front_legs:
        s.add(mir(C([(18.5,31),(15.5,36),(16.5,41)],2.3,1.8)),main,bias=.05)
        for x in (14,16,18): s.px([(int(T(x,42)[0]),int(T(x,42)[1])),(int(47-T(x,42)[0]),int(T(x,42)[1]))],'#e8e0c8')
    # neck
    ny=16-(neck_len-1)*6
    s.add(C([(24,30),(24.5,23),(24,ny+3)],3.8,3.0),main)
    if not bone:
        s.add(C([(24,29),(24.5,23),(24,ny+5)],1.4,1.2),belly,bias=.1)
        for y in range(int(ny+6),29,3): s.maskpx(C([(23,y),(26,y)],.35),belly[1])
    else: 
        for y in range(int(ny+4),30,3): px([(23,y),(24,y),(25,y)],'#e8e0c8')
    # head
    hy=ny-3
    if horns:
        s.add(mir(C([(20.5,hy-2),(17,hy-7),(13,hy-10)],1.6,.45)),horn,bias=.1)
        if horns>2: s.add(mir(C([(19.5,hy+1),(14,hy),(10,hy-2)],1.2,.35)),horn,bias=.05)
    s.add(Pp([(22.5,hy-4),(24,hy-7),(25.5,hy-4)]),horn,bias=.1)
    s.add(E(24,hy,6.4,5),main,soft=1.2,bias=.08)
    s.add(E(24,hy+4.6,4.4,3.6),main,bias=.14)
    px([(22,hy+3),(26,hy+3)],'#0a0605')
    mouth=Pp([(20.5,hy+5.5),(27.5,hy+5.5),(26.5,hy+8.5),(21.5,hy+8.5)])
    if breath:
        s.maskpx(mouth,breath[0]); s.maskpx(Pp([(22,hy+6),(26,hy+6),(25.5,hy+8),(22.5,hy+8)]),breath[1]); px([(24,hy+7),(23,hy+7)],breath[2])
    else:
        s.maskpx(mouth,'#140608')
    px([(21,hy+5),(23,hy+5),(25,hy+5),(27,hy+5),(22,hy+6),(26,hy+6),(22,hy+8),(24,hy+8),(26,hy+8)],'#ece4d0')
    s.maskpx(mir(E(20.6,hy-.6,1.5,1)),eye)
    s.maskpx(mir(C([(18.5,hy-2.6),(22.8,hy-1.2)],.5)),main[0])
    if breath:
        for (x,y,c) in [(19,hy+8,0),(29,hy+8,0),(18,hy+10,1),(30,hy+10,1),(24,hy+11,0),(21,hy+11,2),(27,hy+11,2)]:
            px([(x,y)],breath[c],200)
    if extra: extra(s,T,px)
    return s

R = {
 'red':(['#1e0604','#3e0c08','#68160e','#922418','#b83a24','#d85a38'],['#5a2a0e','#8a4a1a','#b8702c','#d89a48','#f0bc6a']),
 'blue':(['#060c1e','#0c1a3c','#14305e','#1e4a86','#2c66aa','#4486c8'],['#2a4a6a','#4a6e90','#6e94b4','#98bad4','#c0dcee']),
 'green':(['#06140a','#0c2a14','#164622','#226232','#328044','#48a05a'],['#3a4a1a','#5a6a2a','#7e8c3e','#a0ac58','#c0c878']),
 'black':(['#060608','#0e0e12','#18181e','#24242c','#32323c','#44444e'],['#2a2a1a','#44442a','#62623e','#828256','#a0a070']),
 'white':(['#3a4450','#5a6876','#8292a0','#aab8c4','#cdd8e0','#eef2f6'],['#6a7a8a','#8ea0b0','#b0c0cc','#d0dce4','#eef4f8']),
 'gold':(['#2a1a04','#543408','#805010','#ab7420','#d49c34','#f2c858'],['#6a4a14','#9a7020','#c89a34','#e8c050','#fae27a']),
 'shadow':(['#08040e','#12081e','#1e1030','#2c1848','#3e2262','#542e80'],['#1a0e2a','#2a183e','#3e2456','#563270','#70448c']),
 'bone':(['#2a2620','#4a443a','#6e6656','#948a76','#b8ae98','#d8d0bc'],['#4a443a','#6e6656','#948a76','#b8ae98','#d8d0bc']),
 'drake':(['#1e1006','#3c200c','#5e3414','#824a1e','#a6642c','#c48440'],['#5a4420','#7e6230','#a08446','#c0a460','#dcc282']),
 'wyvern':(['#0e120c','#1c2418','#2e3a26','#425236','#586c48','#72885e'],['#4a4a30','#6a6a46','#8a8a60','#aaa87c','#c8c49a']),
 'elder':(['#14060a','#2a0c14','#481620','#6a2030','#8e2e40','#b44458'],['#5a3a1a','#866030','#ae8846','#d0ae64','#ecd08a']),
}
WING = {k:[c for c in v[0][1:5]] for k,v in R.items()}
HORN=['#2a2620','#4a443a','#82786a','#b0a690','#d8d0bc']
D = {
 'wyrmling':dict(m='red',k=.72,breath=('#ff7020','#ffb040','#fff0a0')),
 'drake':dict(m='drake',wings=False,k=.92,horns=3),
 'wyvern':dict(m='wyvern',front_legs=False,tail_tip='stinger'),
 'reddragon':dict(m='red',breath=('#ff6020','#ffb040','#fff0a0')),
 'bluedragon':dict(m='blue',eye='#e0f4ff',breath=('#7fd8ff','#d0f0ff','#ffffff'),horns=3),
 'greendragon':dict(m='green',eye='#e8ff60',breath=('#80d040','#b8f070','#e8ffb0')),
 'blackdragon':dict(m='black',eye='#c8ff40',breath=('#a0c020','#d0e840','#f0ffa0'),horns=3),
 'whitedragon':dict(m='white',eye='#7fd8ff',breath=('#b8e8ff','#e0f6ff','#ffffff'),outline='#141a22'),
 'golddragon':dict(m='gold',eye='#fff4c0',breath=('#ffd040','#fff090','#ffffff'),horns=3),
 'shadowdragon':dict(m='shadow',eye='#c070ff',breath=('#6a2ac0','#a060ff','#e0c0ff')),
 'bonedragon':dict(m='bone',eye='#60ff80',bone=True,outline='#0a0a08',breath=('#40c060','#80ff90','#d0ffd8')),
 'elderdragon':dict(m='elder',k=1.0,horns=3,neck_len=1.15,breath=('#ff5020','#ffa040','#fff0a0'),eye='#ffe060'),
}
def make(key):
    d=D[key]; main,belly=R[d['m']]
    return dragon(main,belly,WING[d['m']] if d['m']!='bone' else ['#2a2620','#3e3a32','#5a544a','#767060'],HORN,
                  eye=d.get('eye','#ffd040'),k=d.get('k',1.0),wings=d.get('wings',True),front_legs=d.get('front_legs',True),
                  tail_tip=d.get('tail_tip','spade'),breath=d.get('breath'),outline=d.get('outline','#08060a'),neck_len=d.get('neck_len',1.0),horns=d.get('horns',2),bone=d.get('bone',False))
if __name__=='__main__':
    import base64,io,json
    imgs={k:make(k).render() for k in D}
    sheet(list(imgs.values()),scale=5,cols=6).save('dragons.png')
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('dragons.json','w'))
