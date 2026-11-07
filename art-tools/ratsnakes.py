from pxlib import *
D='#0b0909'

# ---------- rats ----------
def rat_head(s, cx, cy, head, flesh, eye, k=1.0, ears=True, teeth='#cdb46c', big_teeth=False):
    if ears:
        s.add(ellipse(cx-7.5*k,cy-4*k,3.2*k,3.6*k,-25)|ellipse(cx+7.5*k,cy-4*k,3.2*k,3.6*k,25),head)
        s.add(ellipse(cx-7.2*k,cy-3.7*k,1.7*k,2.2*k,-25)|ellipse(cx+7.2*k,cy-3.7*k,1.7*k,2.2*k,25),flesh[:3],bias=-.2)
    s.add(ellipse(cx,cy,7*k,6*k)|ellipse(cx,cy+5*k,4.5*k,4.5*k)|ellipse(cx,cy+8*k,2.6*k,2.4*k),head,soft=1.4,dither=True)
    s.add(ellipse(cx,cy+9.3*k,1.8*k,1.2*k),flesh)
    ex=round(3.5*k)
    s.px([(cx-ex-1,cy-1),(cx-ex,cy-1),(cx+ex,cy-1),(cx+ex+1,cy-1)],eye)
    s.px([(cx-ex,cy-2),(cx+ex+1,cy-2)],'#ffd0c0')
    ty=round(cy+11*k)
    if big_teeth:
        s.px([(cx-1,ty),(cx,ty),(cx-1,ty+1),(cx,ty+1),(cx-1,ty+2),(cx,ty+2),(cx-1,ty+3),(cx,ty+3)],teeth); s.px([(cx,ty+1),(cx,ty+3)],'#8f7a3a')
    else:
        s.px([(cx-1,ty),(cx,ty),(cx-1,ty+1),(cx,ty+1)],teeth)

def rat_variant(body, head, flesh, eye, tail=True, k=1.0, outline='#090706', fur_lines='#5a4e47', ears=True, big_teeth=False, noise=.35):
    s=Sprite(outline)
    if tail: s.add(chain([(33,38),(41,37),(45,30),(44,22),(40,18)],1.3,.5),flesh)
    s.add(ellipse(24,28,14*k,11*k)|ellipse(24,22,9*k,7*k),body,dither=True,noise=noise)
    for x0 in range(13,36,3): s.px([(x0,19+abs(24-x0)//3),(x0+1,20+abs(24-x0)//3)],fur_lines)
    s.add(mir(chain([(17,33),(15,39),(16,44)],2.2,1.4)),body)
    for kk in range(3): s.pxm([(13+kk*2,45),(13+kk*2,46)],'#cfc6b4')
    rat_head(s,24,32,head,flesh,eye,1.0,ears,big_teeth=big_teeth)
    return s

FLESH=['#24181a','#3a272a','#563a3c','#704e4e','#8a6460']
def plaguerat():
    B=['#0f110b','#1e2216','#2f3522','#434a30','#5a6040','#727852']
    s=rat_variant(B,B,['#1e2214','#3a3a22','#5a5432','#7a6e44','#988a58'],'#c8f050',fur_lines='#727852')
    for (x,y) in [(15,26),(31,24),(28,30),(18,22),(34,31)]:
        s.px([(x,y)],'#8a2a20'); s.px([(x+1,y)],'#c8b040')
    for (x,y,a) in [(8,16,150),(40,14,140),(12,10,110),(36,8,110),(43,20,90)]: s.px([(x,y)],'#b8e070',a)
    return s

def blackrat():
    B=['#07070a','#0f0f14','#18181f','#23232c','#30303b','#40404c']
    return rat_variant(B,B,FLESH,'#ff3b2e',fur_lines='#40404c',noise=.25)

def giantrat():
    B=['#130e0b','#251b15','#3a2b20','#52402f','#6c5640','#887054']
    s=Sprite('#090605')
    s.add(chain([(36,40),(43,38),(46,30),(45,20),(41,15)],1.8,.7),FLESH)
    s.add(ellipse(24,28,18,14)|ellipse(24,20,12,9),B,dither=True,noise=.4)
    for x0 in range(10,39,3): s.px([(x0,16+abs(24-x0)//3),(x0+1,17+abs(24-x0)//3)],'#6c5640')
    s.maskpx(chain([(14,22),(19,30)],.5)|chain([(30,20),(35,26)],.5),'#7a3a30')
    s.add(mir(chain([(15,35),(12,41),(13,46)],2.8,1.8)),B)
    for kk in range(4): s.pxm([(9+kk*2,46),(9+kk*2,47)],'#cfc6b4')
    rat_head(s,24,31,B,FLESH,'#ff3b2e',1.15)
    s.maskpx(mir(chain([(19,27),(22,29)],.4)),'#130e0b')
    return s

def molerat():
    PK=['#3a1e1c','#5e3430','#844e48','#a86a60','#c88a7c','#e0a898']
    s=Sprite('#120806')
    s.add(ellipse(24,32,15,12),PK,soft=2,dither=True)
    for y in (26,30,34,38): s.maskpx(ellipse(24,32,14,11)&(yy>y)&(yy<y+1)&(BAYER_T>-.1),'#844e48')
    s.add(mir(chain([(15,37),(12,42),(13,46)],2.3,1.5)),PK)
    for kk in range(3): s.pxm([(10+kk*2,46),(10+kk*2,47)],'#f0dccc')
    s.add(ellipse(24,22,9,8),PK,soft=1.6,dither=True,bias=.05)
    for y in (17,20): s.maskpx(ellipse(24,22,8,7)&(yy>y)&(yy<y+1),'#844e48')
    s.add(ellipse(24,28,5.5,3.5),PK,bias=.1)
    s.pxm([(19,20)],'#1a0806')
    for (x,y) in [(22,31),(23,31),(25,31),(26,31),(22,32),(23,32),(25,32),(26,32),(22,33),(23,33),(25,33),(26,33),(22,34),(23,34),(25,34),(26,34)]:
        s.px([(x,y)],'#f2e6c4')
    s.px([(24,31),(24,32),(24,33),(24,34)],'#5e3430')
    s.px([(23,27),(25,27)],'#3a1e1c')
    return s

def ratking():
    B=['#120f0d','#231d19','#372e28','#4e433a','#675a4e','#827264']
    s=Sprite('#080605')
    s.add(ellipse(24,38,16,8),B,dither=True,noise=.4)
    knot=chain([(10,44),(18,40),(26,46),(32,40),(38,45)],1.2,1.2)|chain([(14,46),(22,42),(30,47),(36,42)],1.1)
    s.add(knot,FLESH)
    for (cx,cy,k) in [(13,24,.8),(35,24,.8)]:
        s.add(ellipse(cx,cy+7,6,6),B,dither=True,noise=.3)
        rat_head(s,cx,cy,B,FLESH,'#ff3b2e',k)
    s.add(ellipse(24,25,8,8),B,dither=True,noise=.3)
    rat_head(s,24,18,B,FLESH,'#ffd23a',.95)
    s.px([(20,9),(21,8),(23,8),(25,8),(27,8),(28,9),(22,9),(24,9),(26,9)],'#d4a944')
    s.px([(21,9),(24,8),(27,9)],'#f2d27a')
    return s

# ---------- snakes ----------
def snake(ramp, belly, eye='#e8c030', thick=1.0, hood=None, rattle=False, pattern=None, head='round', mouth=False, outline='#070605', tongue=True):
    s=Sprite(outline)
    if rattle:
        s.add(chain([(37,42),(42,36),(43,28)],1.8,1.6),['#3a2a16','#5c4626','#7e6638','#a08a50','#c0aa6c'])
        for y in (30,33,36): s.px([(42,y),(43,y),(44,y)],'#2a1e10')
    t=thick
    s.add(ellipse(24,41,18*t if t<1.1 else 19,5.2*t),ramp,soft=1.6,dither=True)
    s.add(ellipse(23,36,14*t,4.6*t),ramp,soft=1.4,dither=True,bias=.03)
    s.add(ellipse(25,31.5,10*t,4*t),ramp,soft=1.3,dither=True,bias=.06)
    if hood: s.add(ellipse(24,17,10,9.5)&(yy>8),hood,soft=1.8,dither=True)
    s.add(chain([(27,31),(30,26),(25,21),(24,15)],2.8*t,2.4*t),ramp,soft=1.2,dither=True,bias=.08)
    s.add(chain([(27.5,31),(30.5,26),(25.5,21),(24.5,16)],1.1*t,1.0*t),belly,bias=.1)
    if head=='viper': hm=poly([(17,11),(20,7.5),(28,7.5),(31,11),(28,15),(24,17.5),(20,15)])
    elif head=='slim': hm=ellipse(24,12,4,4.4)
    else: hm=ellipse(24,12,5.4,4.6)
    s.add(hm,ramp,soft=1,bias=.12)
    s.pxm([(20,11),(21,11)],eye); s.pxm([(21,11)],'#100804')
    if mouth:
        s.maskpx(poly([(21.5,14),(26.5,14),(25.5,18),(22.5,18)]),'#050405')
        s.px([(22,14),(26,14)],'#e8e0d0')
    if tongue:
        s.px([(24,17),(24,18),(23,19),(25,19)],'#c8283a')
    if pattern: pattern(s)
    return s

def garter():
    G=['#0a140c','#142616','#203c22','#2e5630','#40703e','#5a8c50']
    def pat(s):
        coils=ellipse(24,41*1,18*.85,5.2*.85)|ellipse(23,36,14*.85,4.6*.85)|ellipse(25,31.5,10*.85,4*.85)
        from scipy import ndimage
        inner=ndimage.binary_erosion(coils,iterations=2)
        s.maskpx(inner&(ellipse(24,41,18,1)|ellipse(23,36,14,1)|ellipse(25,31.5,10,.9)),'#d8c050')
        s.maskpx(chain([(29.5,26),(25,21),(24,16)],.5),'#d8c050')
    return snake(G,['#2a2a10','#4a4a1c','#6e6a2c','#928c40'],eye='#d8c050',thick=.85,head='slim',pattern=pat)

def copperhead():
    C=['#1c0e06','#38200c','#5a3414','#7e4c20','#a26830','#c08848']
    def pat(s):
        for x in range(8,42,7): s.maskpx((ellipse(24,41,18,5.2)|ellipse(23,36,14,4.6)|ellipse(25,31.5,10,4))&(abs(xx-x)<1.6+abs(yy-36)*.12),'#3a1a0a')
    return snake(C,['#5a4a30','#7a6648','#9a8462','#b8a27e'],eye='#e8a020',head='viper',pattern=pat)

def rattlesnake():
    R=['#1a140c','#322616','#4e3c22','#6c5432','#8a6e44','#a88a5c']
    def pat(s):
        for x in range(8,42,6):
            s.maskpx((ellipse(24,41,18,5.2)|ellipse(23,36,14,4.6)|ellipse(25,31.5,10,4))&(abs(xx-x)+abs((yy-36)*.4)<2.2),'#2a1e10')
    return snake(R,['#6a5a40','#8a785a','#aa9676','#c8b494'],eye='#f0c040',head='viper',rattle=True,pattern=pat)

def coral():
    K=['#0a0606','#140c0c','#201414','#2e1c1c','#3e2828']
    def pat(s):
        coils=ellipse(24,41,17,5)|ellipse(23,36,13.4,4.4)|ellipse(25,31.5,9.6,3.8)
        seq=['#b82a24','#e0c840','#0e0a0a','#e0c840']
        for i,x in enumerate(range(6,44,3)):
            c=seq[i%4]
            if c=='#0e0a0a': continue
            s.maskpx(coils&(xx>=x)&(xx<x+(3 if c!='#e0c840' else 1.5)),c)
        s.maskpx(chain([(29.5,26),(25,21)],1.2)&(yy<24),'#c8302a')
        s.maskpx(ellipse(24,12,5,2)&(yy>12),'#e8d040')
    return snake(K,['#2a1010','#4a1c1c','#6a2a2a','#8a3a3a'],eye='#e8e0d0',thick=.85,head='slim',pattern=pat)

def cobra():
    C=['#120e08','#241c10','#3a2e1a','#524226','#6c5834','#887046']
    hood=['#120e08','#241c10','#3a2e1a','#524226','#6c5834']
    def pat(s):
        s.maskpx(mir(chain([(18,14),(20,22)],.5)),'#2a1e10')
    return snake(C,['#6a5a3c','#8a7854','#aa9670','#c4b28c'],eye='#e04020',hood=hood,pattern=pat,mouth=True,tongue=False)

def python():
    P=['#14100a','#2a2214','#44381e','#5e4e2a','#7a6838','#96844c']
    def pat(s):
        coils=ellipse(24,41,20,6.5)|ellipse(23,35,15.5,5.5)|ellipse(25,29.5,11,4.8)
        for (x,y) in [(9,41),(16,43),(24,40),(32,42),(38,40),(13,35),(21,36),(30,34),(18,30),(28,29)]:
            s.maskpx(coils&ellipse(x,y,2.6,1.4),'#1e1608'); s.maskpx(coils&ellipse(x,y,1.4,.7),'#a8925c')
    s=Sprite('#080604')
    s.add(ellipse(24,41,20,6.5),P,soft=1.8,dither=True)
    s.add(ellipse(23,35,15.5,5.5),P,soft=1.6,dither=True,bias=.03)
    s.add(ellipse(25,29.5,11,4.8),P,soft=1.4,dither=True,bias=.06)
    s.add(chain([(28,29),(32,23),(26,17),(24,12)],3.6,3),P,soft=1.4,dither=True,bias=.08)
    s.add(ellipse(24,9,6,4.8),P,soft=1.1,bias=.12)
    s.pxm([(20,8),(21,8)],'#e0b040'); s.pxm([(21,8)],'#100804')
    s.px([(24,13),(24,14),(23,15),(25,15)],'#c8283a')
    pat(s)
    return s

def mamba():
    M=['#0c0c0e','#18181c','#26262c','#36363e','#484852','#5c5c68']
    return snake(M,['#3a3a34','#56564c','#727266','#8e8e80'],eye='#c8c8b0',thick=.8,head='slim',mouth=True,tongue=False)

ALL={'plaguerat':plaguerat,'blackrat':blackrat,'giantrat':giantrat,'molerat':molerat,'ratking':ratking,
     'garter':garter,'copperhead':copperhead,'rattlesnake':rattlesnake,'coral':coral,'cobra':cobra,'python':python,'mamba':mamba}
if __name__=='__main__':
    imgs={k:f().render() for k,f in ALL.items()}
    sheet(list(imgs.values()),scale=5,cols=6).save('rs.png')
    import base64,io,json
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('rs.json','w'))
