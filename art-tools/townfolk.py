from hk import *
import base64, io, json

def pit():
    f = Fig()
    # cracked earth mound around a hole that drops into the dark
    f.add(f.E(24, 36, 23, 11), ['#1a120c','#2a1c12','#3a2818','#4a3420','#5a4028'], soft=1.6, dither=True, noise=.4)
    f.add(f.E(24, 37, 16, 7), ['#000000','#030203','#070507'], flat=0, ao=False)
    for i, y in enumerate((32.5, 35, 37.5)):
        w = 13 - i * 2.6
        f.add(f.Pp([(24 - w, y), (24 + w, y), (24 + w - 1, y + 1.4), (24 - w + 1, y + 1.4)]), 'gray', flat=max(0, 2 - i))
    # a broken stone arch half-sunk into the ground
    f.add(f.C([(8, 37), (8, 18), (12, 10), (18, 6)], 3, 2.6), 'gray', bias=-.05)
    f.add(f.C([(40, 37), (40, 18), (36, 10), (30, 6)], 3, 2.6), 'gray', bias=-.05)
    f.add(f.Pp([(18, 3), (30, 3), (31, 9), (17, 9)]), 'gray', bias=.05)
    for p in [(9, 24), (10, 25), (38, 14), (39, 15), (21, 6), (22, 7)]: f.px([p], '#0a0a0e')
    # skull on the keystone
    f.add(f.E(24, 6, 3, 2.6), 'bone', bias=.1); f.px([(23, 6), (25, 6)], '#ff3020'); f.px([(24, 8)], '#1a1410')
    # braziers burning red, chains, and eyes in the dark
    for x in (4, 44):
        f.add(f.Pp([(x - 2.5, 30), (x + 2.5, 30), (x + 1.5, 33), (x - 1.5, 33)]), 'dsteel')
        f.add(f.C([(x, 33), (x, 44)], .7), 'dsteel')
        f.flame((x, 29), ('#a01008', '#ff4020', '#ffb070'), big=.9)
    f.mask(f.C([(11, 12), (14, 20), (13, 28)], .35), '#4a4a52'); f.mask(f.C([(37, 12), (34, 20), (35, 28)], .35), '#4a4a52')
    f.px([(21, 39), (22, 39), (27, 40), (28, 40)], '#ff3020')
    for p in [(16, 44), (31, 45), (6, 41), (42, 42)]: f.px([p], '#5a0a0a')
    return f

def brakka():
    f = Fig()
    f.legs('wide', pants='pants', boots='boot')
    f.torso('leather', wt=7.4, wb=6.4)
    f.add(f.C([(17, 18), (31, 29)], 1), 'dleather'); f.belt(29.5, 'dleather', buckle='#a0a8b4')
    f.pauldron(17, 18.4, 'steel', 3.6, 2.6)
    # arms crossed
    f.add(f.C([(17, 20), (19, 25), (29, 24)], 2.4, 2), 'skin'); f.add(f.C([(31, 20), (29, 26), (19, 25.5)], 2.4, 2), 'skin')
    f.px([(22, 24), (26, 25)], P['skin'][2])
    f.head('skin', rx=5.4); f.face(mood='angry', eye='#3a2a1a')
    f.mask(f.Pp([(25, 9), (29, 9), (29, 12), (25, 12)]), '#0a0806'); f.mask(f.C([(19, 8), (29, 7)], .35), '#0a0806')   # eyepatch
    f.px([(20, 13), (21, 14), (21, 15)], '#8a3a30')
    f.beard('gray', length=6)
    return f

def maren():
    f = Fig()
    f.robe('white', wb=10)
    f.add(f.Pp([(21.5, 17), (26.5, 17), (26.5, 46), (21.5, 46)]), 'gold', bias=.05)
    f.arm((17, 19.5), (19, 25), (22, 27), 'white', 'skinlt'); f.arm((31, 19.5), (29, 25), (26, 27), 'white', 'skinlt')
    f.add(f.C([(24, 27), (24, 21)], 1.1), [ '#c8c0a8','#e8e0c8','#fff8e0'], flat=2)
    f.flame((24, 20), ('#ff9a30', '#ffd060', '#fff4c0'), big=.6)
    f.head('skinlt'); f.hood('white'); f.face(mood='calm', eye='#3a6aa0', skin='skinlt')
    f.mask(f.E(24, 3.4, 4, .9) & ~f.E(24, 3.4, 3, .3), '#ffe08a')
    return f

def wenna():
    f = Fig()
    f.robe('brown', wb=9.5)
    f.add(f.Pp([(15.5, 17), (32.5, 17), (31, 26), (17, 26)]), 'forest', bias=-.05)
    for x in range(17, 32, 2): f.px([(x, 26.4)], P['forest'][1])
    f.arm((17, 19.5), (13, 24), (14, 28), 'brown', 'skinlt'); f.arm((31, 19.5), (35, 22), (35, 18), 'brown', 'skinlt')
    f.add(f.E(35, 15, 2.6, 3), ['#0a3a1a','#1a7a3a','#4ad07a','#b0ffc8'], soft=1); f.add(f.C([(35, 12), (35, 10)], .7), 'steel')
    for p in [(33, 9), (37, 8), (35, 6)]: f.px([p], '#7af0a0', 180)
    f.head('skinlt'); f.hair('gray', 'topknot')
    f.face(mood='sly', eye='#3a5a2a', skin='skinlt')
    f.mask((f.E(21.5, 11.2, 1.8, 1.5) & ~f.E(21.5, 11.2, 1, .7)) | (f.E(26.5, 11.2, 1.8, 1.5) & ~f.E(26.5, 11.2, 1, .7)) | f.C([(23.3, 11), (24.7, 11)], .3), '#c8a040')
    return f

def durik():
    f = Fig(k=.84, w=1.28)
    f.legs('wide', pants='pants', boots='boot')
    f.torso('red', wt=7.4, wb=6.8)
    f.add(f.Pp([(19, 20), (29, 20), (29.5, 36), (18.5, 36)]), 'dleather', bias=.05)   # leather apron
    for p in [(21, 26), (27, 31), (23, 33)]: f.px([p], '#2a1a0c')
    f.arm((17, 19.5), (12, 22), (11, 16), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.2)
    f.haft((11.5, 18), (10, 6)); f.add(f.Pp([(6, 3), (15, 3), (15, 8), (6, 8)]), 'dsteel', bias=.05); f.mask(f.C([(6.5, 3.6), (6.5, 7.4)], .45), '#c8d0dc')
    f.arm((31, 19.5), (35, 24), (34, 28), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.2)
    f.head('skin'); f.beard('orange', length=15, braid=True)
    f.face(mood='calm', eye='#3a2a1a')
    f.hair('orange', 'short'); f.px([(20, 13), (22, 12), (27, 14)], '#2a2020')
    return f

def pell():
    f = Fig()
    f.cape('black', side='center')
    f.legs('stand', pants='black', boots='boot')
    f.torso('purple', wt=6.6)
    f.add(f.Pp([(21, 17), (27, 17), (26, 29), (22, 29)]), 'white', bias=.05)
    for y in (20, 23, 26): f.px([(24, y)], GOLD)
    f.mask(f.C([(27, 22), (30, 25)], .35), GOLD)
    f.arm((17, 19.5), (13, 24), (16, 27), 'purple', 'white')
    f.add(f.Pp([(12, 25), (19, 24), (19.5, 30), (12.5, 31)]), 'crimson'); f.mask(f.C([(13, 27.5), (19, 27)], .3), GOLD)   # ledger
    f.arm((31, 19.5), (35, 24), (34, 28), 'purple', 'white')
    f.head('skinlt'); f.face(mood='sly', eye='#2a2a3a', skin='skinlt')
    f.mask(f.E(26.5, 11.2, 1.8, 1.6) & ~f.E(26.5, 11.2, 1.1, .9), GOLD); f.mask(f.C([(28, 12), (29, 18)], .25), GOLD)   # monocle and chain
    f.px([(22, 15.6), (23, 15.6), (25, 15.6), (26, 15.6)], '#3a2a1a')   # thin mustache
    f.add(f.Pp([(19, 6.6), (29, 6.6), (28.4, -1), (19.6, -1)]), 'black', soft=1)                       # top hat
    f.add(f.E(24, 6.8, 8.4, 1.4), 'black', bias=-.05); f.mask(f.Pp([(19.2, 4.4), (28.8, 4.4), (28.8, 5.6), (19.2, 5.6)]), '#8a1a20')
    return f

def ysolde():
    f = Fig()
    f.cape('forest', lining='tan', side='right')
    f.legs('stand', pants='brown', boots='leather', cuff=GOLD)
    f.torso('tan', wt=6.6)
    f.add(f.C([(30, 18), (19, 29)], 1), 'leather'); f.belt(29.5, 'leather')
    f.arm((17, 19.5), (13, 22), (15, 25), 'tan', 'skin'); f.arm((31, 19.5), (35, 22), (33, 25), 'tan', 'skin')
    f.add(f.Pp([(13, 23), (35, 23), (34, 30), (14, 30)]), ['#5a4a30','#8a7650','#c0a878','#e8d8b0'], flat=3)   # unrolled map
    f.mask(f.C([(16, 28), (20, 25), (24, 27), (28, 24), (32, 26)], .35), '#b02a20'); f.px([(32, 26)], '#b02a20')
    f.mask(f.C([(13, 23), (13, 30)], .8) | f.C([(35, 23), (35, 30)], .8), '#8a7650')
    f.head('skin'); f.hair('red', 'long'); f.face(mood='calm', eye='#2a6a4a')
    f.add(f.Pp([(18.5, 7.4), (29.5, 7.4), (28, 3), (20, 3)]), 'brown', soft=1); f.add(f.E(24, 7.6, 10, 1.6), 'brown', bias=-.05)
    f.add(f.C([(27, 5), (32, 1), (36, 1)], 1.1, .4), 'crimson', bias=.1)
    return f

ALL = {'gate_pit':pit, 'npc_yard':brakka, 'npc_temple':maren, 'npc_apothecary':wenna, 'npc_smithy':durik, 'npc_bank':pell, 'npc_cartographer':ysolde}
if __name__ == '__main__':
    imgs = {k: fn().render() for k, fn in ALL.items()}
    sheet(list(imgs.values()), scale=5, cols=7).save('townfolk.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b,'PNG',optimize=True); out[k] = 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('townfolk.json','w'))
