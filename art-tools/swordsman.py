import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import pxlib; pxlib.FLAT['on']=True
from pxlib import *
CRIM=['#1e0408','#3c0a10','#64121c','#8c1e2a','#b4303a','#d84c50']
NAVY=['#05081a','#0c1432','#16224e','#22346c','#30488c','#4460a8']
HAIR=['#140604','#341206','#5a200c','#823414','#a84c1e','#cc6a2c']
SKIN=['#2a1810','#4e3020','#76492e','#9c6640','#bc8456','#d8a270']
PANT=['#0e0a08','#1c1410','#2c2018','#3c2c20','#4e3a2a']
BOOT=['#060506','#0e0c0e','#1a171a','#282428','#3a3438']
LEATH=['#140a04','#2c1608','#4a2810','#6a3c1a','#8a5426']
STEEL=['#14181e','#2a3240','#46546a','#6c7e96','#9cb0c6','#d4e2f0']
GOLD='#e8b83a'; GOLDD='#9c6c10'
def swordsman():
    s=Sprite('#080406')
    # cape billowing to the right, with crimson lining
    cape=poly([(18,17),(30,17),(37,24),(44,36),(46,46),(39,42),(33,46),(29,38),(22,34)])
    s.add(cape,NAVY,soft=1.6)
    s.add(poly([(38,30),(44,36),(46,46),(42,42)]),CRIM,bias=-.05)
    # headband tails flowing right
    s.add(chain([(29,8),(34,7),(39,9),(42,7)],1.2,.5),CRIM,bias=.1)
    s.add(chain([(29,9),(33,11),(37,13)],1,.4),CRIM)
    # legs in a wide stance
    s.add(chain([(21,30),(17.5,38),(15,45)],2.6,2.3),PANT)
    s.add(chain([(27,30),(30.5,38),(33,45)],2.6,2.3),PANT)
    s.add(chain([(17,40),(14.5,45.5)],2.8,2.8)|chain([(31,40),(33.5,45.5)],2.8,2.8),BOOT)
    s.px([(15,39),(16,39),(17,39),(18,39),(30,39),(31,39),(32,39),(33,39)],GOLD)
    s.px([(12,46),(13,46),(36,46),(35,46)],'#3a3438')
    # coat tails
    s.add(poly([(18,29),(30,29),(32.5,36),(27,34),(24,36),(21,34),(15.5,36)]),CRIM,bias=-.08)
    # doublet torso
    s.add(poly([(17,17),(31,17),(30,30),(18,30)]),CRIM,soft=1.3)
    s.add(poly([(21.5,17),(26.5,17),(24,22)]),SKIN,flat=3)
    s.px([(21,17),(22,18),(23,19),(27,17),(26,18),(25,19)],GOLD)
    s.maskpx(chain([(24,22),(24,29)],.5),GOLD)
    for y in (23,26): s.px([(23,y),(25,y)],GOLDD)
    # sash and belt
    s.add(chain([(30,18),(19,29)],1.2),LEATH,bias=.1)
    s.add(chain([(18,29.5),(30,29.5)],1.1),LEATH,flat=1)
    s.px([(23,29),(24,29),(25,29),(23,30),(25,30)],GOLD); s.px([(24,30)],GOLDD)
    # pauldron on sword side
    s.add(ellipse(17.5,18.8,3.2,2.2),STEEL,bias=.1)
    s.px([(16,18)],'#e8f2ff')
    # free arm: fist planted on hip
    s.add(chain([(31,19),(35,23),(32,27.5)],2.2,1.9),CRIM,bias=.05)
    s.add(ellipse(31.5,28,2,2),LEATH,bias=.1)
    # sword arm: grips the hilt in front of the chest
    s.add(chain([(17,20),(14,25),(17,27)],2.2,1.9),CRIM,bias=.05)
    # sword raised diagonally, blade up to the top left
    s.add(chain([(16,26),(5,5)],1.5,.8),STEEL,bias=.15)
    s.maskpx(chain([(15,25),(5.5,6)],.35),'#e8f2ff')
    s.add(chain([(12.5,28),(19.5,24)],.9),[GOLDD,GOLD,'#f8dc80'],flat=1)
    s.add(chain([(17,27),(19,30)],1),LEATH)
    s.maskpx(ellipse(19.6,30.6,1.1,1.1),GOLD); s.px([(19,30)],'#c8203a')
    s.add(ellipse(17,27,2,2),LEATH,bias=.15)
    # glint near the tip
    for p in [(7,6),(6,7),(8,7),(7,8),(7,5),(5,7),(9,7),(7,9)]: s.px([p],'#ffffff',255 if p in [(7,6),(6,7),(8,7),(7,8)] else 150)
    # neck and head
    s.add(ellipse(24,17,2.2,1.4),SKIN)
    s.add(ellipse(24,11.4,5.2,6),SKIN,soft=1.2)
    s.add(ellipse(24,15.4,3.8,2),SKIN,bias=.05)
    # swept hair, spiky fringe falling to one side
    hair=(ellipse(24,6.6,6.2,3.6)&(yy<8.2))|poly([(17.6,6),(16,11),(19,8.5)])|poly([(26,4),(33,7),(29.5,9),(27.5,7)])|poly([(22,5),(25,5),(23.5,9),(21.5,8.5)])
    s.add(hair,HAIR,soft=1)
    s.px([(21,3),(22,3),(25,3),(27,4),(31,6)],'#e08a40')
    # red headband with knot tails
    s.maskpx(poly([(18.6,7.2),(29.6,7.2),(29.4,8.6),(18.8,8.6)]),CRIM[4]); s.px([(19,8),(29,8)],CRIM[2])
    # fierce face: brows slanting down to the center, a hard glare, a crooked smirk, a scar
    s.px([(20,9),(21,9),(22,10),(28,9),(27,9),(26,10)],'#200a04')
    s.px([(21,11),(22,11),(26,11),(27,11),(21,12),(27,12)],'#f8f2e8')
    s.px([(22,12),(26,12)],'#14222e')
    s.px([(24,13),(24,14)],SKIN[2]); s.px([(25,14)],SKIN[1])
    s.px([(22,16),(23,16),(24,16),(25,16)],'#2a0e06'); s.px([(26,15)],'#2a0e06'); s.px([(23,16),(24,16)],'#3a1208')
    s.px([(19,12),(20,13),(20,14),(21,15)],'#a8362c')
    s.px([(29,12)],GOLD)
    return s
if __name__=='__main__':
    import base64,io,json
    im=swordsman().render()
    sheet([im],scale=10,cols=1).save('swordsman.png')
    b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    json.dump({'swordsman':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()},open('swordsman.json','w'))
