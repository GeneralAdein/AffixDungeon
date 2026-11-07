from pxlib import *

def ant_variant(body, dark, eye_ramp=None, abd=(24,11,9,7), head=(24,29,10.5,8), mand='curved', legs_w=1.3, stripes=True, outline='#0c0605', extra_back=None, extra_front=None, eye_glint='#d89c80', mid=None, jaw=None):
    s=Sprite(outline)
    if extra_back: extra_back(s)
    ax,ay,arx,ary=abd
    s.add(ellipse(ax,ay,arx,ary),dark,dither=True)
    if stripes:
        st=(ellipse(ax,ay-2,arx-1,.8)|ellipse(ax,ay+1.5,arx-1,.8))&ellipse(ax,ay,arx-.5,ary-.5)
        s.add(st,[dark[1]],flat=0,ao=False)
    if mid: mid(s)
    s.add(mir(chain([(19,21),(11,14),(4,20),(2,30)],legs_w*.92,.6)),dark)
    s.add(mir(chain([(19,23),(10,24),(6,36),(5,45)],legs_w,.6)),dark)
    s.add(ellipse(24,20,5.5,4.5),body)
    s.add(mir(chain([(19,27),(13,33),(14,40),(12,46)],legs_w*1.08,.6)),body)
    s.add(mir(chain([(21,23),(17,13),(11,6),(7,6)],.9,.5)),dark,bias=.1)
    hx,hy,hrx,hry=head
    s.add(ellipse(hx,hy,hrx,hry)|ellipse(hx,hy-5,hrx*.67,hry*.62),body,soft=1.4)
    J=jaw or [c for c in dark]
    if mand=='curved':
        s.add(mir(chain([(19,hy+5.5),(16,hy+9.5),(16.5,hy+13.5),(20.5,hy+15)],2.0,.45)),J,bias=.3)
    elif mand=='sickle':
        s.add(mir(chain([(19,hy+4),(11,hy+7),(9,hy+13),(13,hy+17),(20,hy+17)],2.4,.45)),J,bias=.3)
    elif mand=='trap':
        s.add(mir(chain([(20,hy+4),(10,hy+7),(3,hy+9)],1.9,1.2)),J,bias=.3)
        s.pxm([(2,hy+9),(2,hy+10),(3,hy+11),(3,hy+8)],'#e8dcc4')
    elif mand=='short':
        s.add(mir(chain([(20,hy+5.5),(19,hy+9),(21.5,hy+10.5)],2.0,.6)),J,bias=.3)
    er=eye_ramp or ['#060303','#100606','#1f0b0a','#3a1611']
    s.add(mir(ellipse(hx-8,hy-1,3,3.6)),er,lo=-.7)
    s.pxm([(hx-9,hy-3),(hx-8,hy-3)],eye_glint)
    if extra_front: extra_front(s)
    return s

def fireant():
    B=['#2a0804','#521208','#80200c','#b03a14','#d85a20','#f08a3a']
    Dk=['#1a0604','#360c06','#5a160a','#82240e','#a83a18']
    return ant_variant(B,Dk,eye_glint='#ffd0a0')

def armyant():
    B=['#1c0806','#38100a','#5a1c12','#7c2c1a','#9c4024','#b85a34']
    Dk=['#0e0504','#1e0a06','#34120c','#4e1c12','#683020']
    return ant_variant(B,Dk,abd=(24,12,7,5.5),head=(24,26,11,8),mand='sickle',jaw=['#2a1a0e','#5a3a1e','#8a6034','#b08850','#d0ac70'])

def bulletant():
    B=['#0c0806','#1a120c','#2c2016','#423222','#5a4632','#745c44']
    Dk=['#070505','#100c0a','#1c1612','#2a221c','#3a3028']
    def back(s):
        s.add(chain([(24,4),(24,0)],1,.3),['#0a0806','#1c1610','#3a3028'])
    s=ant_variant(B,Dk,abd=(24,11,10,8),head=(24,29,11,8.5),legs_w=1.5,extra_back=back)
    for (x,y) in [(18,8),(21,6),(28,7),(30,10),(15,12),(33,13)]: s.px([(x,y)],'#8a7a60',160)
    return s

def carpenterant():
    B=['#08080a','#121216','#1e1e24','#2c2c34','#3e3e48','#545460']
    return ant_variant(B,B,head=(24,29,12,9),mand='short',legs_w=1.5,eye_glint='#a0a8c0')

def leafcutter():
    B=['#1e0e06','#3a1c0c','#5c2e14','#80441e','#a05e2c','#bc7c40']
    Dk=['#140904','#28140a','#422010','#5e3018','#7a4422']
    LF=['#0c1a08','#163212','#22501c','#327028','#489038','#66ae4c']
    def front(s):
        leaf=poly([(30,30),(40,14),(46,6),(44,18),(38,30),(33,36)])
        s.add(leaf,LF,soft=1,bias=.05)
        s.maskpx(chain([(33,34),(44,9)],.4),'#163212')
        for (a,b) in [((36,28),(40,26)),((38,23),(42,20)),((40,18),(43,15))]: s.maskpx(chain([a,b],.3),'#22501c')
    return ant_variant(B,Dk,extra_front=front)

def trapjaw():
    B=['#1e1206','#3a220c','#5a3614','#7c4e1e','#9c682c','#ba8640']
    Dk=['#140c04','#281808','#40280e','#5a3a16','#764e20']
    return ant_variant(B,Dk,head=(24,25,9,9.5),mand='trap',jaw=['#2a1a0e','#5a3a1e','#8a6034','#b08850','#d0ac70'])

def honeypot():
    B=['#1e1206','#3a220c','#5a3614','#7c4e1e','#9c682c','#ba8640']
    HN=['#3a1e02','#6a3a06','#a0600c','#d08c18','#f0b838','#ffe080']
    s=Sprite('#0c0805')
    s.add(ellipse(24,13,15,12),HN,soft=2.2)
    s.maskpx(ellipse(24,13,15,12)&~ellipse(24,13,13.5,10.5),'#5a3206')
    for y in (8,14,19): s.maskpx(ellipse(24,13,14,.6)&(abs(yy-y)<.6)&ellipse(24,13,14,11),'#a0600c')
    s.px([(16,6),(17,5),(18,5),(15,7)],'#fff4c0')
    s2=ant_variant(B,B,abd=(24,11,0.1,0.1),stripes=False)
    for p in s2.parts[1:]: s.parts.append(p)
    s.details+=s2.details
    return s

def queenant():
    B=['#200a06','#40140c','#682414','#8c361e','#b04e2c','#cc6c42']
    Dk=['#140604','#2a0c08','#461610','#64221a','#843426']
    def mid(s):
        s.add(mir(ellipse(10,15,10,4.5,-20)),['#4a5862','#6a7c88','#8ea0aa','#b0c0c8'],soft=1.5,bias=.1)
        s.add(mir(chain([(18,16),(4,11)],.35)),['#3a4650'],flat=0,ao=False)
    s=ant_variant(B,Dk,abd=(24,10,13,9.5),head=(24,30,9.5,7.5),mid=mid,legs_w=1.4)
    s.px([(20,19),(21,18),(23,18),(25,18),(27,18),(28,19),(22,19),(24,19),(26,19)],'#d4a944')
    s.px([(21,19),(24,18),(27,19)],'#f2d27a')
    return s

ALL={'fireant':fireant,'armyant':armyant,'bulletant':bulletant,'carpenterant':carpenterant,'leafcutter':leafcutter,'trapjaw':trapjaw,'honeypot':honeypot,'queenant':queenant}
if __name__=='__main__':
    imgs={k:f().render() for k,f in ALL.items()}
    sheet(list(imgs.values()),scale=5,cols=4).save('ants.png')
    import base64,io,json
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('ants.json','w'))
