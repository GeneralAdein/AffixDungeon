from pxlib import *
import numpy as np
D='#0b0909'
def P(*c): return list(c)

# ---------- spiders (parametric) ----------
def spider_base(body, abd, legs, abd_r=(14,11), ceph_r=(9.5,7.5), leg_w=(1.8,0.9), leg_set=None, eyes='#ff3b2e', fangs=True, outline='#060508', hair=0.15):
    s=Sprite(outline)
    s.add(ellipse(24,15,*abd_r),abd,dither=True,noise=hair)
    legs_pts=leg_set or [[(17,24),(9,8),(2,22),(1,30)],[(17,27),(7,16),(2,38),(2,44)],[(18,30),(9,24),(6,44)],[(19,32),(13,30),(12,45)]]
    for i,pts in enumerate(legs_pts): s.add(mir(chain(pts,*leg_w)),legs,bias=.05*i,dither=hair>0.2)
    s.add(ellipse(24,29,*ceph_r),body,soft=1.3,bias=.05,dither=hair>0.2)
    if fangs: s.add(mir(chain([(21.5,34),(21,39),(22.5,42)],1.6,.6)),['#1d1a16','#38322a','#5a5246','#82786a'],bias=-.1)
    s.pxm([(21,26),(22,26),(21,27),(22,27)],eyes); s.pxm([(19,28),(20,28)],eyes); s.pxm([(21,26)],'#ffd0c0')
    return s

def tarantula():
    BR=['#120c08','#24180f','#3a2817','#533a22','#6e4f30','#8c6844']
    s=spider_base(BR,BR,BR,abd_r=(15,12),ceph_r=(10.5,8),leg_w=(2.6,1.6),hair=.4,eyes='#c0302a')
    for y in (16,22,28,33):  # knee bands
        for x in (5,8,11): s.pxm([(x,y)],'#b89a74',200)
    for (x,y) in [(14,10),(18,7),(28,8),(32,12),(24,6),(20,13),(30,16),(17,18)]: s.px([(x,y)],'#a08060',180)
    return s

def redwidow():
    RD=['#1e0606','#3e0c0c','#661614','#8f2420','#b83a2e','#d8604a']
    BK=['#060506','#0f0d10','#1b181d','#2a262e','#3c3742']
    s=spider_base(RD,BK,RD,abd_r=(13,12),ceph_r=(8,6.5),leg_w=(1.5,.7),eyes='#ffd040')
    for (x,y,r) in [(24,9,1.8),(19,14,1.3),(29,14,1.3),(24,19,1.6)]: s.maskpx(ellipse(x,y,r,r),'#d0302a')
    return s

def wolfspider():
    G=['#100e0c','#221e1a','#38322b','#50483e','#6a6054','#867a6c']
    s=spider_base(G,G,G,abd_r=(13,10.5),ceph_r=(10,8),leg_w=(2.2,1.2),hair=.35,eyes='#2a2a30')
    for x in (23,24,25): s.px([(x,y) for y in range(8,23)],'#7d7262' if x==24 else '#5a5044')
    s.maskpx(mir(ellipse(21,26.5,1.8,1.8)),'#0a0a0e'); s.pxm([(20,26)],'#c8f0ff'); s.pxm([(21,27)],'#58a0c0')
    s.pxm([(18,29),(19,29)],'#0a0a0e')
    return s

def daddylonglegs():
    T=['#1a1410','#33281e','#4e3e2e','#6c573f','#8a7254']
    pts=[[(21,24),(12,6),(1,20),(0,40)],[(21,26),(8,14),(1,32),(1,47)],[(22,28),(12,22),(5,40),(6,47)],[(22,29),(16,30),(13,47)]]
    s=Sprite('#070504')
    for i,p in enumerate(pts): s.add(mir(chain(p,.9,.55)),T,bias=.05*i)
    s.add(ellipse(24,26,6,5.2),T,soft=1.2,bias=.1)
    s.pxm([(22,24),(23,24)],'#0a0605'); s.pxm([(22,24)],'#d0b080')
    return s

def recluse():
    TN=['#1c140c','#382818','#5a4128','#7c5c3a','#9c7a50','#b8986c']
    s=spider_base(TN,TN,TN,abd_r=(11,9.5),ceph_r=(8.5,7),leg_w=(1.4,.7),eyes='#e0d8c0',fangs=True)
    s.maskpx(poly([(24,24),(26,27),(25,31),(24,33),(23,31),(22,27)]),'#2a1a0e')
    s.maskpx(ellipse(24,26,1.6,1.2),'#2a1a0e')
    return s

def spider_old():
    S=['#0c0a0f','#19151f','#2a2432','#3d3448','#52475e','#6b5f77']
    s=spider_base(S,S,S,hair=.15)
    s.maskpx(poly([(24,9),(27,14),(24,19),(21,14)]),'#7a1712'); s.maskpx(poly([(24,11),(25.5,14),(24,17),(22.5,14)]),'#a8261c')
    return s

# ---------- flyers ----------
WING=['#3c4a52','#58707a','#7c98a2','#a6c0c8','#cde0e6']
def wings(s, top, mid, alpha=150, color='#b8d4dc'):
    m=mir(top)
    s.maskpx(m, color, alpha)
    s.maskpx(mir(mid) & m, '#ffffff', 90)

def bee():
    Y=['#2a1a02','#5a3a06','#8c600e','#c08e1a','#e8b830','#f8d860']
    s=Sprite('#0a0703')
    w=ellipse(13,14,10,6,-25); wings(s,w,ellipse(12,13,6,3,-25))
    s.add(ellipse(24,31,9,11),Y,soft=1.6)
    for y in (26,31,36): s.maskpx(ellipse(24,31,9,11)&(yy>y)&(yy<y+2.5),'#140c02')
    s.add(chain([(24,41),(24,46)],1.2,.3),['#140c02','#2a1a04','#4a3a20'])
    s.add(mir(chain([(18,30),(11,36),(9,42)],1,.6)),['#140c02','#2a1a04','#3a2a10'])
    s.add(ellipse(24,19,7,6),['#120a04','#24180a','#3a2a14','#523c20','#6a5030'],dither=True,noise=.3)
    s.add(mir(ellipse(19.5,19,2.6,3.4)),['#06050a','#120e18','#241c30','#3a2e4a'],lo=-.6)
    s.pxm([(19,17)],'#c8c0e0')
    s.add(mir(chain([(21,14),(17,7),(15,6)],.7,.5)),['#140c02','#2a1a04'])
    return s

def wasp():
    Y=['#2a1a00','#5a3a00','#8c6000','#c09000','#e8c020','#f8e050']
    s=Sprite('#0a0703')
    w=ellipse(12,16,10,4.5,-15); wings(s,w,ellipse(11,15,6,2,-15),alpha=140)
    s.add(ellipse(24,36,7,9),Y,soft=1.4)
    for y in (32,37,41): s.maskpx(ellipse(24,36,7,9)&(yy>y)&(yy<y+2),'#100800')
    s.maskpx(mir(poly([(22,33),(24,35),(22,36)])),'#100800')
    s.add(chain([(24,44),(24,47)],1,.3),['#100800','#2a1a04','#5a4a30'])
    s.add(ellipse(24,25,5.5,4.5),Y,soft=1.2,bias=-.1)
    s.maskpx(ellipse(24,25,5.5,4.5)&(yy<24),'#100800')
    s.add(mir(chain([(19.5,25),(13,31),(10,38)],.9,.5)),['#100800','#2a1a04','#4a3a10'])
    s.add(ellipse(24,17,6.5,5),Y,soft=1.2)
    s.add(mir(ellipse(20.3,16.5,2.4,3.2)),['#05040a','#100c16','#201a2c','#342a46'],lo=-.6)
    s.pxm([(20,15)],'#c8c0e0')
    s.maskpx(mir(chain([(22.5,21),(23.3,23)],.6)),'#100800')
    s.add(mir(chain([(22,12),(18,6),(17,3)],.6,.4)),['#100800','#2a1a04'])
    s.maskpx(mir(chain([(19,13),(22,14.5)],.5)),'#100800')
    return s

def mosquito():
    B=['#14100e','#2a221e','#423630','#5c4c42','#786458']
    s=Sprite('#070505')
    w=ellipse(12,16,10,3.5,-20); wings(s,w,ellipse(11,15,6,1.5,-20),alpha=120,color='#c8d8e0')
    for pts in [[(21,24),(10,22),(3,34),(1,46)],[(22,26),(14,32),(9,47)],[(22,25),(12,14),(4,6)]]:
        s.add(mir(chain(pts,.6,.4)),B)
    s.add(ellipse(24,33,4.5,9),['#2a0606','#4a0c0c','#741812','#9c2a1c','#c04030'],soft=1.4)
    s.add(ellipse(24,22,4,4),B,soft=1)
    s.add(ellipse(24,16,3.5,3.2),B,soft=1)
    s.pxm([(22,15)],'#ff4030')
    s.add(chain([(24,18),(24,9),(23,4)],.5,.4),['#140c0a','#2a1a14','#4a3020'])
    s.add(mir(chain([(23,14),(19,9),(17,8)],.5,.4)),B)
    return s

def moth():
    W=['#14100c','#2a2018','#423426','#5c4a36','#76624a','#927c62']
    s=Sprite('#090705')
    wing=ellipse(13,19,12,10,20)|ellipse(13,33,9,7,-20)
    s.add(mir(wing),W,dither=True,noise=.4,soft=2,bias=-.05)
    s.maskpx(mir(wing)&~mir(ellipse(13,19,10.5,8.5,20)|ellipse(13,33,7.5,5.5,-20)),'#1e1812')
    for (x,y) in [(10,20)]:
        s.maskpx(mir(ellipse(x,y,2.6,2.6)),'#5a3a1a'); s.maskpx(mir(ellipse(x,y,1.4,1.4)),'#0a0604')
    for (a1,b1) in [((20,14),(5,9)),((20,24),(4,26)),((20,30),(9,38))]:
        s.maskpx(mir(chain([a1,b1],.45)),'#241c14')
    for (x,y) in [(7,14),(15,12),(6,30),(14,37),(9,24)]: s.pxm([(x,y)],'#a89474',170)
    FUR=['#1e1610','#3a2c20','#5a4634','#7a624a','#9a8064']
    s.add(ellipse(24,27,4,11),FUR,dither=True,noise=.4)
    s.add(ellipse(24,16,4,3.6),FUR,dither=True)
    s.pxm([(22,16)],'#1a0a04'); s.pxm([(22,15)],'#e0b060')
    for (x,y) in [(21,12),(19,9),(17,7),(15,6)]:
        s.pxm([(x,y)],'#5a4634'); s.pxm([(x-1,y+1)],'#3a2c20')
    return s

def firefly():
    B=['#0c0a0e','#1a161e','#2c2632','#423a4a','#5a5064']
    s=Sprite('#06050a')
    w=ellipse(13,20,10,5,-25); wings(s,w,ellipse(12,19,6,2.5,-25),alpha=110,color='#a0a8b8')
    s.add(ellipse(24,22,7,6),B,soft=1.2)
    s.maskpx(ellipse(24,22,7,6)&(xx<20),'#a02a20')
    s.maskpx(ellipse(24,22,7,6)&(xx>28),'#a02a20')
    s.add(ellipse(24,15,5,4),B)
    s.maskpx(ellipse(24,13.5,4.5,2.5),'#b8302a')
    s.pxm([(21,15)],'#e0e0f0')
    s.add(mir(chain([(19,25),(13,31),(11,37)],.8,.5)),B)
    s.add(ellipse(24,33,6,9),B,soft=1.3)
    glow=ellipse(24,37,5.5,5.5)&ellipse(24,33,6,9)
    s.maskpx(glow,'#d8f070'); s.maskpx(ellipse(24,38,3,3)&glow,'#f8ffc0')
    for (x,y,a) in [(15,40,140),(33,39,140),(18,45,110),(30,46,110),(24,46,170),(12,35,90),(36,34,90)]:
        s.px([(x,y)],'#e8ff90',a)
    s.add(mir(chain([(22,12),(19,5),(16,3)],.6,.4)),B)
    return s

# ---------- crawlers ----------
def slug():
    S=['#121209','#262513','#3f3c1c','#5c5627','#7b7336','#9c924c']
    s=Sprite('#070704')
    body=ellipse(24,38,19,6.5)|ellipse(24,32,11,8)|ellipse(24,25,6.5,6)
    s.add(body,S,soft=2.2,dither=True)
    s.maskpx(ellipse(24,32,10,6)&(BAYER_T>.3),'#4a4520',255)
    s.add(mir(chain([(21,21),(18,11)],1.1,.8)),S)
    s.add(mir(chain([(22.5,23),(21,17)],.8,.6)),S)
    s.maskpx(mir(ellipse(18,10,1.6,1.6)),'#0a0a06'); s.pxm([(17,9)],'#e8e0b0')
    for (x,y) in [(14,33),(15,32),(30,29),(31,29),(19,27),(36,36),(10,37),(27,24)]:
        s.px([(x,y)],'#d8d8b0',200)
    for x in range(5,44,3): s.px([(x,45)],'#5c5627',150)
    return s

def worm():
    F=['#1e0e0c','#3c1c18','#5e2e26','#824436','#a65e4a','#c47c64']
    s=Sprite('#0a0504')
    s.add(ellipse(24,45,17,3),['#140e08','#261a10','#3a2a1a'],flat=1)
    s.add(chain([(24,44),(20,36),(22,26),(28,19),(29,12)],6,4.6),F,soft=1.8)
    for (x,y,r) in [(21,38,5),(21,32,5),(24,25,4.8),(27,20,4.6)]:
        s.maskpx(ellipse(x,y,r+.8,1)&(xx>x-r)&(xx<x+r),'#4a221c')
    s.add(ellipse(29,10,5,3.8),F,bias=.1)
    s.maskpx(ellipse(29,10,3.2,2.4),'#1a0606')
    for (x,y) in [(27,9),(29,8),(31,9),(30,12),(28,12)]: s.px([(x,y)],'#e8dcc4')
    for (x,y) in [(20,34),(23,27),(26,21)]: s.px([(x,y)],'#e8b0a0',180)
    return s

def beetle():
    C=['#06090a','#0e1a1c','#16302e','#1e4a40','#2a6650','#3c8a62']
    s=Sprite('#040606')
    for pts in [[(17,27),(8,24),(3,32)],[(17,32),(8,36),(5,45)],[(19,36),(13,42),(12,47)]]:
        s.add(mir(chain(pts,1.4,.8)),['#060808','#101414','#1c2222','#2a3232'])
    s.add(ellipse(24,32,14,12),C,soft=2)
    s.maskpx(chain([(24,21),(24,44)],.5),'#040606')
    s.px([(16,26),(17,25),(18,25),(30,25),(31,25),(32,26)],'#9ae0b0')
    s.px([(15,27),(33,27)],'#5ab890')
    s.add(ellipse(24,19,8,5),C,soft=1.2,bias=-.1)
    s.add(chain([(24,18),(24,9),(28,4)],2.2,.8),C,bias=.15)
    s.pxm([(18,19),(19,19)],'#c8f0d0')
    s.add(mir(chain([(18,16),(13,10)],.6,.4)),['#060808','#101414','#1c2222'])
    return s

def walkingstick():
    W=['#1a1208','#33240e','#4e3a18','#6c5224','#8a6c34','#a68848']
    s=Sprite('#080502')
    for pts in [[(23,22),(14,14),(6,4)],[(23,26),(12,28),(4,44)],[(23,30),(16,38),(12,47)]]:
        s.add(mir(chain(pts,.9,.6)),W)
    for (x,y) in [(14,14),(12,28),(16,38)]: s.pxm([(x,y),(x+1,y)],'#33240e')
    s.add(chain([(24,8),(24,46)],2.2,1.6),W,dither=True,noise=.3)
    for y in (14,22,30,38): s.px([(23,y),(24,y),(25,y)],'#33240e')
    s.add(ellipse(24,8,2.8,3),W,bias=.1)
    s.pxm([(22,7)],'#e0c860')
    s.add(mir(chain([(23,6),(16,1),(8,0)],.5,.4)),W)
    return s

def mantis():
    G=['#08120a','#122812','#1e421c','#2e5e28','#447c36','#62a04a']
    s=Sprite('#040804')
    for pts in [[(20,34),(11,37),(7,47)],[(21,37),(15,43),(14,47)]]:
        s.add(mir(chain(pts,1,.6)),G)
    s.maskpx(mir(ellipse(18,36,5,10,12)),'#7aa860',80)
    s.add(ellipse(24,36,6,10),G,soft=1.4,dither=True)
    for y in (31,35,39,43): s.px([(x,y) for x in range(20,29)],'#1e421c')
    s.add(chain([(24,26),(24,14)],2,2.2),G)
    s.add(mir(chain([(22,20),(13,27),(11,14)],2.1,1.9)),G,bias=.05)
    s.add(mir(chain([(11,14),(13,8),(17,9)],1.6,.6)),G,bias=.18)
    for (x,y) in [(10,22),(10,19),(10,16)]: s.pxm([(x,y)],'#a8d880')
    s.pxm([(17,9),(18,10)],'#d8f0b0')
    s.add(poly([(16.5,5),(31.5,5),(24,14)]),G,soft=.8,bias=.1)
    s.add(mir(ellipse(18.2,6.5,2.6,2.2)),['#0e1a08','#2a4a12','#5a8a28','#9ad050'],lo=-.4)
    s.pxm([(18,6)],'#0a1004')
    s.px([(23,12),(24,12),(25,12)],'#122812')
    s.add(mir(chain([(21,5),(16,0)],.5,.4)),G)
    return s

ALLBUGS={'slug':slug,'worm':worm,'bee':bee,'mosquito':mosquito,'beetle':beetle,'moth':moth,'wasp':wasp,'firefly':firefly,'walkingstick':walkingstick,
 'tarantula':tarantula,'redwidow':redwidow,'wolfspider':wolfspider,'daddylonglegs':daddylonglegs,'recluse':recluse,'mantis':mantis}
if __name__=='__main__':
    imgs={k:f().render() for k,f in ALLBUGS.items()}
    sheet(list(imgs.values()),scale=5,cols=5).save('bugs.png'); sheet([imgs['moth'],imgs['mantis']],scale=7,cols=2).save('bugzoom.png')
    import base64,io,json
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('bugs.json','w'))
