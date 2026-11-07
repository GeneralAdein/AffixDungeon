import os, sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import pxlib; pxlib.FLAT['on']=True
from humans import humanoid, CL, STEEL, DSTEEL, WOOD, GOLDR
N = {
 'knight':dict(skin='human',armor='plate',cape='blue',headgear='fullhelm',helm_ramp=STEEL,plume='blue',weapon='sword',off='kite',shield=CL['blue'],emblem='#d4a944',eyes='#1a1a20'),
 'dreadknight':dict(skin='pale',k=1.04,w=1.1,armor='darkplate',cape='black',headgear='fullhelm',plume='purple',weapon='bigsword',blade=['#140a1c','#26143a','#3a2058','#523078','#6c44a0','#8c60c8'],off='kite',shield=DSTEEL,emblem='#7a3ab8',eyes='#b070ff'),
 'squire':dict(skin='human',k=.88,body='blue',headgear='helm',weapon='sword',off='round',shield=WOOD,eyes='#1a0f0a'),
 'bowman':dict(skin='tan',body='green',headgear='hood',hood='green',weapon='bow',eyes='#1a0f0a'),
 'pikeman':dict(skin='human',armor='plate',headgear='helm',weapon='spear',eyes='#1a0f0a',beard='brown'),
 'swordsman':dict(skin='tan',body='red',hair='black',weapon='bigsword',eyes='#1a0f0a'),
 'jester':dict(skin='pale',body='purple',legs=CL['red'],headgear='jester',weapon='dagger',off='dagger',eyes='#1a0f0a',sigil='#f2d27a'),
 'mage':dict(skin='human',body='blue',robe=True,headgear='witchhat',hat='blue',beard='white',weapon='staff',orb='#7fe0ff',eyes='#7fe0ff'),
 'priest':dict(skin='human',body='white',robe=True,hair='brown',weapon='staff',orb='#ffe08a',off='book',eyes='#1a0f0a',sigil='#d4a944'),
}
if __name__=='__main__':
    from pxlib import sheet
    import base64,io,json
    imgs={k:humanoid(v).render() for k,v in N.items()}
    sheet(list(imgs.values()),scale=5,cols=5).save('newfolk.png')
    out={}
    for k,im in imgs.items():
        b=io.BytesIO(); im.save(b,'PNG',optimize=True); out[k]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out,open('newfolk.json','w'))
