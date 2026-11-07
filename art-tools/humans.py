from pxlib import *

SKIN = {
 'human':['#2a1a12','#4a3022','#6c4a36','#8e664c','#ae8466','#c8a282'],
 'tan':['#24160c','#422a18','#644024','#865a34','#a87648','#c4925e'],
 'pale':['#22201e','#3e3a36','#5e5852','#807870','#a29a90','#bfb8ae'],
 'goblin':['#11180d','#203019','#344a26','#4b6434','#667e46','#86995e'],
 'hob':['#1e0c06','#3a1a0c','#5c2c14','#80421e','#a05a2c','#bc7640'],
 'orc':['#141a0e','#26321a','#3a4a26','#526634','#6c8244','#88a058'],
 'orcdark':['#0e120a','#1c2414','#2c3820','#3e4e2c','#52663a','#6a804a'],
 'kobold':['#1e0c08','#3a1a10','#5a2a18','#7c3e22','#9c5630','#b87044'],
 'gnoll':['#1e160c','#3a2a18','#5a4226','#7a5c36','#9a7848','#b8945e'],
 'lizard':['#0c160e','#16301a','#244a28','#346838','#4a864a','#66a462'],
 'trog':['#121418','#22262c','#363c44','#4c545e','#646e7a','#808a96'],
 'drow':['#0e0a14','#1a1424','#2a2238','#3a3050','#4c406a','#605284'],
 'dwarf':['#1c1614','#342a26','#504440','#6e605a','#8c7e76','#aa9c92'],
 'bugfur':['#150e08','#2a1c10','#42301c','#5c4428','#785c38','#94764c'],
}
CL = {
 'brown':['#140c06','#28180c','#3e2614','#56381e','#704c2a','#8a623a'],
 'green':['#0a1208','#142414','#1e3a1e','#2a5028','#386834','#4a8244'],
 'gray':['#121214','#222226','#34343a','#48484f','#5e5e66','#76767e'],
 'black':['#060608','#0e0e12','#18181e','#22222a','#2e2e38','#3c3c48'],
 'red':['#1a0606','#360c0c','#561414','#781e1e','#982c28','#b4403a'],
 'crimson':['#140408','#2a0810','#46101c','#641a2a','#82263a','#9c344c'],
 'purple':['#0e0814','#1c1028','#2c1a40','#3e2658','#523472','#68468c'],
 'orange':['#1e0e04','#3c1c08','#5e2e0e','#824416','#a45c20','#c27a32'],
 'leather':['#140c08','#261810','#3a2618','#523622','#6a482e','#84603e'],
 'darkleather':['#0a0706','#16100c','#241a14','#34261c','#463426','#5a4432'],
 'white':['#2a2a2c','#4a4a4e','#707076','#9a9aa0','#c2c2c6','#e2e2e4'],
 'blue':['#08101a','#101e32','#1a2e4a','#264264','#34587e','#467098'],
}
STEEL=['#16181c','#2c3038','#474d58','#6a7280','#949cab','#c2c8d2']
DSTEEL=['#0c0d10','#181a20','#262a32','#363b46','#4a505e','#626a7a']
WOOD=['#140c07','#2b1a0e','#472b16','#64401f','#83582c','#a07440']
BONE=['#1d1a16','#38322a','#5a5246','#82786a','#aaa08e','#d0c8b2']
GOLDR=['#2a1d06','#54390c','#80591a','#ab7f2a','#d4a944','#f2d27a']

def humanoid(sp):
    k=sp.get('k',1.0); w=sp.get('w',1.0)
    def T(x,y): return (24+(x-24)*w*k, 46-(46-y)*k)
    def E(cx,cy,rx,ry,rot=0):
        x,y=T(cx,cy); return ellipse(x,y,rx*w*k,ry*k,rot)
    def C(pts,r1,r2=None): return chain([T(*p) for p in pts], r1*k, (r2 if r2 is not None else r1)*k)
    def Pp(pts): return poly([T(*p) for p in pts])
    def px(pts,c,a=255): s.px([tuple(int(round(v)) for v in T(x,y)) for x,y in pts],c,a)
    def pxm(pts,c,a=255):
        px(pts,c,a); px([(48-1-x - (0) ,y) for x,y in []],c,a)
        for x,y in pts:
            X,Y=T(x,y); s.px([(int(round(47-X)),int(round(Y)))],c,a)
    s=Sprite(sp.get('outline','#0a0706'))
    skin=SKIN[sp['skin']]; body=CL.get(sp.get('body','brown'),sp.get('body')) if isinstance(sp.get('body','brown'),str) else sp['body']
    if sp.get('armor')=='plate': body=STEEL
    if sp.get('armor')=='darkplate': body=DSTEEL
    sleeve=skin if sp.get('bare') else body
    # cape / back items
    if sp.get('cape'): s.add(Pp([(15,19),(33,19),(37,45),(11,45)]),CL[sp['cape']],dither=True,bias=-.15)
    wpn=sp.get('weapon')
    if wpn=='bow':
        s.add(C([(10,14),(7,20),(6,27),(7,34),(10,40)],1.0,1.0),WOOD,bias=.1)
        s.maskpx(C([(10,14),(10,40)],.3),'#d8d0b8',200)
    # legs / robe
    if sp.get('robe'):
        s.add(Pp([(17,19),(31,19),(34.5,46),(13.5,46)]),body,dither=True,soft=1.6)
        s.maskpx(C([(24,30),(24,46)],.4),body[0])
    else:
        legc=sp.get('legs',CL['leather'] if not sp.get('armor','').endswith('plate') else body)
        s.add(mir(C([(21,33),(20.5,45)],2.4,2.2)),legc,dither=True)
        s.add(mir(C([(20.5,42.5),(20.5,45.5)],2.6,2.6)),CL['darkleather'] if not sp.get('armor','').endswith('plate') else body,bias=-.1)
    # torso
    torso=Pp([(16,19),(32,19),(30.5,34),(17.5,34)])
    if sp.get('bare'):
        s.add(torso,skin,soft=1.4,dither=True)
        px([(22,24),(23,25),(26,24),(25,25)],skin[1])
        if sp.get('paint'): s.maskpx(C([(18,22),(22,28)],.6)|C([(30,22),(26,28)],.6),sp['paint'])
        if sp.get('straps'): s.maskpx(C([(17,20),(30,32)],.8),CL['leather'][2])
    else:
        s.add(torso,body,soft=1.4,dither=sp.get('armor') not in ('plate','darkplate'))
        if sp.get('armor') in ('plate','darkplate'):
            px([(24,21),(24,23),(24,25),(24,27)],body[1])
            s.maskpx(E(18.5,20,3,2.2)|E(29.5,20,3,2.2),body[4])
    if not sp.get('robe'): s.add(C([(17.5,33),(30.5,33)],.9),CL['darkleather'],flat=1)
    if sp.get('belt_gold'): px([(23,33),(24,33)],'#d4a944')
    # arms
    raised=sp.get('raised')
    if raised: s.add(C([(16.5,20),(12.5,15),(11.5,9)],2.2,1.8),sleeve,dither=True)
    else: s.add(C([(16.5,20),(13.5,27),(12.5,32)],2.2,1.8),sleeve,dither=True)
    s.add(C([(31.5,20),(34.5,27),(35.5,32)],2.2,1.8),sleeve,dither=True)
    hand_l=(11.5,8) if raised else (12.5,33)
    s.add(E(*hand_l,1.8,1.8)|E(35.5,33,1.8,1.8),skin,bias=.1)
    # neck + head
    head=sp.get('head','human')
    s.add(E(24,18,2.2,1.6),skin)
    if head=='goblin':
        s.add(Pp([(19,11),(8,7),(12,12),(19,15)])|Pp([(29,11),(40,7),(36,12),(29,15)]),skin,bias=.05)
    if head=='elf':
        s.add(C([(19,12),(13,7)],1,.3)|C([(29,12),(35,7)],1,.3),skin)
    if head=='gnoll':
        s.add(Pp([(19,9),(17,1),(22,7)])|Pp([(29,9),(31,1),(26,7)]),skin)
    if head=='bugbear':
        s.add(E(17.5,6.5,2.4,2.4)|E(30.5,6.5,2.4,2.4),skin)
    hrx,hry={'goblin':(6.2,5.4),'bugbear':(7,6.6),'orc':(6.2,6),'kobold':(4.6,4.6),'gnoll':(5,5),'lizard':(4.8,5),'trog':(6,5.4)}.get(head,(5.4,6))
    s.add(E(24,12,hrx,hry),skin,soft=1.3)
    if head=='orc': s.add(E(24,15.2,5.4,3.2),skin,bias=.05)
    if head=='gnoll': s.add(E(24,15.5,3,3.8),skin,bias=.1); px([(23,18),(24,18),(25,18)],'#0a0605'); px([(23,19),(25,19)],'#e8e0d0')
    if head=='lizard':
        s.add(E(24,15.5,3.2,4.2),skin,bias=.1)
        s.add(Pp([(23,4),(24,1),(25,4),(25,9),(23,9)]),CL['red'],bias=.1)
    if head=='kobold':
        s.add(E(24,15,2.6,3),skin,bias=.1)
        s.add(C([(21,9),(18,5),(17,3)],1,.4)|C([(27,9),(30,5),(31,3)],1,.4),BONE,bias=.1)
    if head=='trog':
        s.add(Pp([(21,7),(24,3),(27,7)]),skin,bias=-.1); s.add(E(24,15,5,2.6),skin,bias=.05)
    if head=='bugbear': s.add(Pp([(18,13),(30,13),(28,20),(24,22),(20,20)]),skin,dither=True,bias=-.05)
    if sp.get('beard'): s.add(Pp([(19.5,14),(28.5,14),(27,24),(24,27),(21,24)]),CL[sp['beard']] if sp['beard'] in CL else sp['beard_ramp'],dither=True,bias=.05)
    if sp.get('hair'): s.add(E(24,8.5,5.6,3.2)&(yy<T(0,10)[1]),CL[sp['hair']])
    if sp.get('mohawk'): s.add(C([(24,4),(24,9)],1.2),CL['red'],bias=.1)
    # eyes / mouth
    ec=sp.get('eyes','#1a0f0a'); ey=sp.get('eye_y',11.5)
    ex={'goblin':21.5,'orc':21.5,'bugbear':21.5,'kobold':22,'gnoll':22,'lizard':22,'trog':21.5}.get(head,22)
    pxm([(ex,ey)],ec)
    if sp.get('glint'): pxm([(ex,ey-1)],sp['glint'])
    if head=='orc' or sp.get('tusks'):
        px([(21,15),(21,14),(27,15),(27,14)],'#e8dcc4')
    if head in ('goblin',): px([(22,15),(23,15),(24,15),(25,15),(26,15)],'#1a0a08'); px([(23,15),(25,15)],'#d8cfa8')
    if head in ('human','elf','hob') and not sp.get('nomouth'): px([(23,15),(24,15),(25,15)],skin[1])
    if sp.get('scar'): px([(21,10),(22,11),(22,12),(23,13)],'#7a3a30')
    if sp.get('mask'): s.add(E(24,15,5,2.6)&(yy>T(0,13)[1]),CL[sp['mask']],flat=2)
    # headgear
    hg=sp.get('headgear')
    if hg=='hood':
        hc=CL[sp.get('hood','brown')]
        s.add(E(24,11.5,7.2,8)&~E(24,13.2,4.4,5),hc,soft=1.6,dither=True)
        s.maskpx(E(24,11.5,4.6,1.5)&(yy<T(0,11)[1]),hc[0])
    if hg=='helm': s.add(E(24,9,6,4)&(yy<T(0,11)[1]),sp.get('helm_ramp',STEEL)); px([(24,10),(24,11),(24,12)],STEEL[2])
    if hg=='fullhelm':
        s.add(E(24,11.5,6.2,6.8),sp.get('helm_ramp',DSTEEL),soft=1.2)
        s.maskpx(E(24,11.5,4.8,.9),'#050505'); pxm([(21.5,11.5)],sp.get('eyes','#ff3b2e'))
        if sp.get('plume'): s.add(C([(24,5),(27,1),(31,2)],1.2,.6),CL[sp['plume']])
    if hg=='executioner':
        s.add(E(24,11.5,6.2,7),CL['black'],soft=1.2)
        pxm([(21.5,11.5)],'#050505'); pxm([(21.5,11)],'#c83a2a')
    if hg=='witchhat':
        hc=CL[sp.get('hat','black')]
        s.add(Pp([(19,8),(29,8),(27,1),(22,-1),(25,2)]),hc)
        s.add(E(24,8,10,1.6),hc,bias=-.05)
    if hg=='widehat':
        hc=CL[sp.get('hat','black')]
        s.add(Pp([(19,8),(29,8),(28,3),(20,3)]),hc); s.add(E(24,8,11,1.8),hc,bias=-.05)
        if sp.get('hatband'): s.maskpx(Pp([(19,7),(29,7),(29,8),(19,8)]),sp['hatband'])
    if hg=='bandana':
        s.add(E(24,8.5,5.8,3)&(yy<T(0,10)[1]),CL[sp.get('bandana_c','red')]); s.add(C([(29,8),(32,11)],.8,.4),CL[sp.get('bandana_c','red')])
    if hg=='headband': s.maskpx(Pp([(18.6,8),(29.4,8),(29.4,9.4),(18.6,9.4)]),sp.get('band','#b4403a'))
    if hg=='jester':
        s.add(C([(20,8),(15,4),(12,7)],1.6,.8),CL['red'],bias=.05)
        s.add(C([(28,8),(33,4),(36,7)],1.6,.8),CL['purple'],bias=.05)
        s.add(E(24,8,5.8,2.6)&(yy<T(0,10)[1]),CL['red'])
        s.maskpx(E(24,8,5.8,2.6)&(yy<T(0,10)[1])&(xx>T(24,0)[0]),CL['purple'][3])
        px([(12,8),(36,8)],'#f2d27a'); px([(12,9),(36,9)],'#d4a944')
    if hg=='bonecrown':
        for x in (19,22,24,26,29): s.add(C([(x,8),(x+(x-24)*.3,2 if x==24 else 4)],.9,.3),BONE,bias=.1)
    if hg=='gladhelm':
        s.add(E(24,10,6,5)&(yy<T(0,13)[1]),GOLDR); s.add(C([(24,4),(24,8)],1.4),CL['red'])
    if hg=='feathers':
        for i,(x,c) in enumerate([(21,'#c8302a'),(24,'#e8c040'),(27,'#3a7ac8')]): s.add(C([(x,7),(x+(x-24)*.6,0)],.9,.4),[c,c],flat=1)
    # weapon in left hand
    hx,hy=hand_l
    if wpn=='sword':
        s.add(C([(hx,hy+3),(hx-1,hy-15)],1.1,.6),sp.get('blade',STEEL),bias=.1)
        s.add(C([(hx-3,hy-.5),(hx+3,hy-.5)],.8),GOLDR if sp.get('gold_guard') else STEEL)
    if wpn=='bigsword':
        s.add(C([(hx,hy+3),(hx-1.5,hy-22)],1.5,.8),sp.get('blade',STEEL),bias=.1)
        s.add(C([(hx-4,hy-.5),(hx+4,hy-.5)],.9),sp.get('blade',STEEL))
    if wpn=='dagger': s.add(C([(hx,hy),(hx-.5,hy-7)],.9,.4),STEEL,bias=.15)
    if wpn=='axe':
        s.add(C([(hx,hy+4),(hx-1,hy-14)],.9),WOOD)
        s.add(Pp([(hx-1,hy-14),(hx-7,hy-17),(hx-8,hy-9),(hx-1,hy-10)]),STEEL,bias=.05)
    if wpn=='greataxe':
        s.add(C([(hx+.5,hy+8),(hx-1.5,hy-22)],1.1),WOOD)
        s.add(Pp([(hx-1,hy-22),(hx-9,hy-26),(hx-11,hy-13),(hx-1,hy-15)]),sp.get('blade',STEEL),bias=.05)
        s.add(Pp([(hx-1,hy-22),(hx+5,hy-24),(hx+5,hy-16),(hx-1,hy-16)]),sp.get('blade',STEEL),bias=-.05)
    if wpn=='spear':
        s.add(C([(hx+.5,hy+11),(hx-1.5,hy-26)],.8),WOOD)
        s.add(Pp([(hx-3,hy-25),(hx-1.5,hy-31),(hx,hy-25)]),STEEL,bias=.1)
    if wpn=='trident':
        s.add(C([(hx+.5,hy+11),(hx-1.5,hy-24)],.8),STEEL)
        for dx in (-2.5,0,2.5): s.add(C([(hx-1.5+dx,hy-24),(hx-1.5+dx,hy-29)],.6,.3),STEEL,bias=.1)
        s.add(C([(hx-4,hy-24),(hx+1,hy-24)],.6),STEEL)
    if wpn=='club':
        s.add(C([(hx,hy+2),(hx-2,hy-13)],1.2,2.6),WOOD,dither=True)
        for (dx,dy) in [(-3,-11),(-1,-13),(-3,-8),(0,-9)]: px([(hx+dx,hy+dy)],'#a0a8b4')
    if wpn in ('staff','skullstaff'):
        s.add(C([(hx+.5,hy+12),(hx-.5,hy-24)],.9),WOOD)
        if wpn=='staff':
            oc=sp.get('orb','#8ad0ff')
            s.add(E(hx-.5,hy-26,2.6,2.6),[oc,oc,oc],flat=1)
            px([(hx-1.5,hy-27)],'#ffffff')
        else:
            s.add(E(hx-.5,hy-26,2.8,2.6),BONE,bias=.1); px([(hx-1.5,hy-26),(hx+.5,hy-26)],sp.get('orb','#60ff80'))
    if wpn=='flame':
        fc=sp.get('flame',['#ff6020','#ffb040','#fff0a0'])
        s.maskpx(E(hx,hy-3,3,4),fc[0]); s.maskpx(E(hx,hy-2.5,2,2.8),fc[1]); s.maskpx(E(hx,hy-2,1,1.6),fc[2])
        for (dx,dy) in [(-3,-7),(2,-8),(0,-9),(-1,-11)]: px([(hx+dx,hy+dy)],fc[1],200)
    if wpn=='fists': s.add(E(*hand_l,2.2,2.2),CL['white'],bias=-.1)
    # offhand
    off=sp.get('off')
    if off=='round':
        sc=sp.get('shield',WOOD)
        s.add(E(36,29,5.5,6),sc,soft=1.3); s.maskpx(E(36,29,5.5,6)&~E(36,29,4.4,4.9),'#3a3a40'); s.maskpx(E(36,29,1.4,1.4),'#8a92a0')
    if off=='kite':
        sc=sp.get('shield',STEEL)
        s.add(Pp([(31,22),(41,22),(40.5,30),(36,37),(31.5,30)]),sc,soft=1)
        if sp.get('emblem'): s.maskpx(C([(36,24),(36,32)],.6)|C([(33.5,27),(38.5,27)],.6),sp['emblem'])
    if off=='buckler': s.add(E(36,31,3.6,3.6),GOLDR,bias=.05); s.maskpx(E(36,31,1,1),'#5a3a10')
    if off=='dagger': s.add(C([(35.5,33),(36.5,26)],.9,.4),STEEL,bias=.15)
    if off=='pouch': s.add(E(36,35,2.6,2.8),CL['leather'],bias=.05); px([(36,33),(35,36)],'#d4a944')
    if off=='book': s.add(Pp([(33,30),(39,30),(39,36),(33,36)]),CL['red']); s.maskpx(Pp([(33.5,30.5),(38.5,30.5),(38.5,35.5),(33.5,35.5)])&(xx>T(36,0)[0]),'#d8d0b8'); px([(36,33)],'#d4a944')
    if off=='trap':
        s.add(E(36,35,3.6,2),STEEL); px([(33,34),(34,33),(35,34),(36,33),(37,34),(38,33),(39,34)],'#c2c8d2')
    if off=='lantern':
        s.add(Pp([(34,31),(38,31),(38,37),(34,37)]),DSTEEL); s.maskpx(Pp([(34.7,32),(37.3,32),(37.3,36),(34.7,36)]),'#ffd060'); px([(36,34)],'#fff4c0')
    if off=='flame':
        fc=sp.get('flame',['#ff6020','#ffb040','#fff0a0'])
        s.maskpx(E(35.5,30,2.6,3.6),fc[0]); s.maskpx(E(35.5,30.5,1.6,2.4),fc[1]); s.maskpx(E(35.5,31,.8,1.2),fc[2])
    if sp.get('necklace'): px([(21,20),(22,21),(23,21),(25,21),(26,21),(27,20)],'#d0c8b2'); px([(24,22)],'#e8e0c8')
    if sp.get('sigil'): px([(24,25),(23,26),(25,26),(22,27),(26,27),(24,27),(24,28)],sp['sigil'])
    return s

H = {
 'goblinarcher':dict(skin='goblin',k=.82,head='goblin',body='leather',headgear='hood',hood='green',weapon='bow',eyes='#ffc93c'),
 'goblinshaman':dict(skin='goblin',k=.82,head='goblin',body='brown',robe=True,headgear='feathers',weapon='skullstaff',orb='#60ff80',eyes='#80ff60',necklace=True),
 'hobgoblin':dict(skin='hob',head='goblin',armor='plate',headgear='helm',weapon='sword',off='round',shield=CL['red'],eyes='#ffc93c'),
 'bugbear':dict(skin='bugfur',k=1.06,w=1.18,head='bugbear',body='leather',weapon='club',eyes='#ffc93c'),
 'kobold':dict(skin='kobold',k=.72,head='kobold',body='brown',weapon='spear',eyes='#ffd040'),
 'koboldtrapper':dict(skin='kobold',k=.72,head='kobold',body='darkleather',headgear='bandana',bandana_c='green',weapon='dagger',off='trap',eyes='#ffd040'),
 'orcgrunt':dict(skin='orc',w=1.1,head='orc',body='leather',headgear='helm',weapon='axe',off='round',eyes='#ff6a3a'),
 'orcberserker':dict(skin='orc',k=1.02,w=1.14,head='orc',bare=True,paint='#b02a20',mohawk=True,weapon='greataxe',eyes='#ff3b2e',legs=CL['brown']),
 'orcwarchief':dict(skin='orcdark',k=1.1,w=1.18,head='orc',armor='darkplate',cape='red',headgear='bonecrown',weapon='greataxe',eyes='#ff3b2e'),
 'bandit':dict(skin='human',body='leather',headgear='hood',hood='brown',mask='brown',weapon='sword',off='dagger',eyes='#1a0f0a'),
 'banditcaptain':dict(skin='tan',body='darkleather',cape='red',headgear='widehat',hat='black',hatband='#b4403a',beard='black',weapon='sword',gold_guard=True,belt_gold=True,eyes='#1a0f0a'),
 'cutpurse':dict(skin='pale',k=.92,body='darkleather',headgear='hood',hood='gray',weapon='dagger',off='pouch',eyes='#1a0f0a',glint='#c8c8b0'),
 'assassin':dict(skin='pale',body='black',headgear='hood',hood='black',mask='black',weapon='dagger',off='dagger',eyes='#ff3b2e'),
 'thug':dict(skin='human',k=1.02,w=1.16,bare=True,legs=CL['brown'],weapon='club',scar=True,eyes='#1a0f0a'),
 'mercenary':dict(skin='human',armor='plate',headgear='helm',weapon='sword',off='kite',shield=CL['blue'],emblem='#d4a944',eyes='#1a0f0a',beard='brown'),
 'fallenknight':dict(skin='pale',armor='darkplate',cape='crimson',headgear='fullhelm',plume='crimson',weapon='bigsword',blade=DSTEEL,off='kite',shield=DSTEEL,emblem='#9c2a24',eyes='#ff3b2e'),
 'gladiator':dict(skin='tan',bare=True,straps=True,legs=CL['leather'],headgear='gladhelm',weapon='trident',off='buckler',eyes='#1a0f0a'),
 'executioner':dict(skin='human',k=1.04,w=1.16,bare=True,legs=CL['black'],headgear='executioner',weapon='greataxe',nomouth=True),
 'cultfanatic':dict(skin='pale',body='crimson',robe=True,headgear='hood',hood='crimson',weapon='dagger',raised=True,sigil='#e8c040',eyes='#ff3b2e'),
 'necromancer':dict(skin='pale',body='black',robe=True,headgear='hood',hood='purple',weapon='skullstaff',orb='#60ff80',eyes='#60ff80',sigil='#60ff80'),
 'hedgewitch':dict(skin='pale',body='green',robe=True,headgear='witchhat',hat='black',weapon='staff',orb='#c070ff',eyes='#80ff60',hair='gray'),
 'warlock':dict(skin='pale',body='purple',robe=True,headgear='hood',hood='black',weapon='flame',raised=True,flame=['#6a2ac0','#a060ff','#e8d0ff'],eyes='#c070ff',off='flame'),
 'pyromancer':dict(skin='tan',body='orange',robe=True,headgear='headband',band='#ffb040',weapon='flame',raised=True,off='flame',eyes='#ffb040'),
 'madmonk':dict(skin='tan',body='orange',robe=True,headgear='headband',band='#b4403a',weapon='fists',eyes='#ff6a3a',scar=True),
 'gnoll':dict(skin='gnoll',k=1.04,head='gnoll',body='leather',weapon='spear',eyes='#ffc93c'),
 'lizardfolk':dict(skin='lizard',head='lizard',bare=True,legs=CL['leather'],weapon='spear',off='round',eyes='#ffd040'),
 'troglodyte':dict(skin='trog',k=.95,w=1.12,head='trog',bare=True,legs=CL['brown'],weapon='club',eyes='#e8f0a0'),
 'darkelf':dict(skin='drow',head='elf',body='black',hair='white',weapon='sword',blade=['#20102a','#3a1e4a','#5a2e6e','#7a4290','#9c5ab0','#c080d8'],off='dagger',eyes='#ff3b2e'),
 'deepdwarf':dict(skin='dwarf',k=.8,w=1.28,armor='plate',headgear='helm',beard='gray',weapon='axe',off='round',shield=STEEL,eyes='#ffb040'),
 'inquisitor':dict(skin='human',body='crimson',cape='black',headgear='widehat',hat='black',hatband='#d4a944',weapon='sword',off='lantern',eyes='#1a0f0a',sigil='#d4a944'),
}

if __name__=='__main__':
    imgs={k:humanoid(v).render() for k,v in H.items()}
    sheet(list(imgs.values()),scale=4,cols=6).save('humans.png')
    import base64,io,json
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('humans.json','w'))
    print(len(out))
