from hk import *
from folk2 import goblin_head

def bandit():
    f = Fig()
    f.legs('wide', pants='brown', boots='leather')
    f.torso('leather', wt=6.8)
    f.add(f.Pp([(19, 17), (29, 17), (28, 30), (20, 30)]), 'red', bias=-.05)          # vest
    f.add(f.C([(30, 18), (19, 29)], 1), 'dleather'); f.px([(26, 21), (23, 24.5)], '#a0a8b4')
    f.belt(29.6, 'dleather'); f.mask(f.E(29, 31.5, 1.6, 1.8), P['leather'][3]); f.px([(29, 31)], GOLD)
    f.arm((31, 19.5), (36, 22), (37, 26), 'leather', 'leather')
    f.dagger((37, 26), (41, 20))
    f.arm((17, 19.5), (12, 18), (10, 13), 'leather', 'leather')
    f.sword((10, 13), (3, 2), w=1.2)
    f.head('skin'); f.hood('brown')
    f.mask(f.Pp([(19.4, 12.6), (28.6, 12.6), (28, 17), (20, 17)]), P['red'][2])        # face scarf
    f.px([(20, 13), (22, 14), (26, 13)], P['red'][1])
    f.face(mood='angry', eye='#2a1a0a', mouth=P['red'][2], brow=INK)
    return f

def banditcaptain():
    f = Fig()
    f.cape('crimson', lining='gold', side='right')
    f.legs('wide', pants='black', boots='boot', cuff=GOLD)
    f.torso('black', wt=7)
    f.add(f.Pp([(20.5, 17), (27.5, 17), (26, 29), (22, 29)]), 'white', bias=.05)       # shirt
    for y in (19, 22, 25): f.px([(24, y)], GOLD)
    f.mask(f.C([(18, 17.6), (18, 29)], .5) | f.C([(30, 17.6), (30, 29)], .5), GOLD)
    f.add(f.C([(17, 29.5), (31, 29.5)], 1.4), 'crimson', flat=3)                        # sash
    f.add(f.C([(30, 30), (33, 35)], 1, .6), 'crimson')
    f.arm((31, 19.5), (35, 24), (32.5, 28), 'black', 'leather')
    f.arm((17, 19.5), (11, 21), (7, 17), 'black', 'leather')
    f.sword((7, 17), (0, 6), w=1.2)
    f.head('skin'); f.hair('black', 'long')
    f.beard('black', length=8)
    f.face(mood='sly', eye='#2a1a0a')
    f.px([(26, 9), (27, 9), (28, 10)], INK)
    # wide plumed hat
    f.add(f.Pp([(18.5, 7), (29.5, 7), (28, 2.4), (20, 2.4)]), 'black', soft=1)
    f.add(f.E(24, 7, 11, 1.8), 'black', bias=-.05)
    f.mask(f.Pp([(18.6, 5.6), (29.4, 5.6), (29.4, 6.8), (18.6, 6.8)]), P['crimson'][4])
    f.add(f.C([(28, 4), (33, 0), (37, 1)], 1.4, .5), 'white', bias=.1)
    f.px([(30, 11), (31, 12)], GOLD)
    return f

def cutpurse():
    f = Fig(k=.92)
    f.legs('crouch', pants='dleather', boots='boot')
    f.torso('gray', wt=6.4, wb=5.6)
    f.add(f.C([(18, 18), (30, 29)], .9), 'dleather')
    for x, y in ((20, 26), (27, 27), (22, 29)): f.mask(f.E(x, y, 1.4, 1.5), P['leather'][3]); f.px([(x, y - 1)], GOLD)   # stolen purses
    f.belt(29.6, 'dleather', buckle=None)
    f.arm((31, 19.5), (36, 20), (39, 16), 'gray', 'leather')
    f.add(f.E(40, 13.8, 2.4, 2.6), 'leather', bias=.05); f.px([(40, 11.5), (39, 13), (41, 14)], GOLD)   # purse held up
    for d in [(-4, -4), (3, -5), (0, -7)]: f.px([(40 + d[0], 13 + d[1])], '#f2d27a', 200)
    f.arm((17, 19.5), (13, 24), (16, 27), 'gray', 'leather')
    f.dagger((16, 27), (12, 33))
    f.head('pale'); f.hood('gray')
    f.face(mood='sly', eye='#3a6a3a', skin='pale')
    f.px([(21, 15), (22, 15.6)], '#5a5450')
    return f

def assassin():
    f = Fig()
    f.cape('black', side='left')
    f.legs('lunge', pants='black', boots='boot')
    f.torso('black', wt=6.8)
    f.add(f.C([(18, 18), (30, 29)], .9) | f.C([(30, 18), (18, 29)], .9), 'dleather')
    f.px([(21, 21), (24, 23.5), (27, 21), (27, 26)], '#a0a8b4')
    f.belt(29.6, 'dleather', buckle='#c83a2a')
    # twin daggers, one held reverse-grip
    f.arm((17, 19.5), (12, 22), (9, 19), 'black', 'black')
    f.dagger((9, 19), (4, 13), blade=['#0a200a', '#18401a', '#28602a', '#3a803a', '#58a058', '#90d090'])
    f.arm((31, 19.5), (36, 23), (35, 27), 'black', 'black')
    f.dagger((35, 27), (39, 33), blade=['#0a200a', '#18401a', '#28602a', '#3a803a', '#58a058', '#90d090'])
    for p in [(39, 34), (40, 36), (5, 12)]: f.px([p], '#60e060', 200)
    f.head('pale'); f.hood('black', deep=True)
    f.mask(f.Pp([(19.4, 12.6), (28.6, 12.6), (28, 17), (20, 17)]), P['black'][2])
    f.px([(21, 11.4), (22, 11.4), (26, 11.4), (27, 11.4)], '#ff3b2e'); f.px([(20, 11.4), (28, 11.4)], '#ff3b2e', 110)
    return f

def thug():
    f = Fig(k=1.02, w=1.16)
    f.legs('wide', pants='brown', boots='boot')
    f.torso('skin', wt=7.8, wb=6.4)
    f.px([(21, 22), (22, 23), (26, 22), (27, 23), (23, 26), (25, 26), (24, 28)], P['skin'][2])
    f.add(f.Pp([(17.5, 17), (21, 17), (20.5, 29), (18.5, 29)]) | f.Pp([(30.5, 17), (27, 17), (27.5, 29), (29.5, 29)]), 'dleather', bias=.05)  # open vest
    f.mask(f.C([(25, 20), (27, 24)], .4), '#2a3a5a')   # tattoo
    f.belt(29.4, 'dleather', buckle='#a0a8b4')
    f.arm((31, 19.5), (37, 24), (37, 29), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.3)
    f.add(f.C([(37, 29), (39, 30)], .8), 'steel')    # knuckles
    f.arm((17, 19.5), (11, 18), (10, 12), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.3)
    f.add(f.C([(10, 14), (8, 1)], 1.3, 2.6), 'wood', bias=.05)
    for d in [(-2, -11), (1, -12), (-1, -8), (2, -9)]: f.px([(9 + d[0], 12 + d[1])], '#b8c0cc')
    f.head('skin', rx=5.4); f.face(mood='mad', eye='#2a1a0a')
    f.px([(20, 8), (21, 9), (21, 10), (22, 11)], '#8a3a30'); f.px([(19, 11)], '#5a2a20')
    f.px([(22, 6), (23, 5.6), (26, 6)], P['skin'][4])
    return f

def cultfanatic():
    f = Fig()
    f.robe('crimson', wb=10)
    f.mask(f.C([(17, 45.4), (31, 45.4)], .5), '#1e0408')
    f.mask(f.C([(24, 22), (24, 30)], .5) | f.C([(21, 25), (27, 25)], .5) | f.C([(22, 28), (26, 22)], .4), '#e8c040')   # sigil
    f.add(f.C([(18, 29.5), (30, 29.5)], .9), 'black', flat=2)
    for x in (19, 21.5, 26.5, 29): f.add(f.C([(x, 30), (x, 34)], .5), 'black')
    f.head('pale', hy=14.5); f.hood('crimson', hy=14.5)
    f.face(hy=14.5, mood='mad', eye='#ff3b2e', glow=True, skin='pale')
    f.mask(f.Pp([(21, 18.4), (27, 18.4), (26, 20), (22, 20)]), '#200408'); f.px([(22, 18.4), (24, 18.4), (26, 18.4)], WHITE)
    # ritual dagger raised high above the head in both hands
    f.arm((17, 20.5), (12, 14), (21.5, 9), 'crimson', 'pale')
    f.arm((31, 20.5), (36, 14), (26.5, 9), 'crimson', 'pale')
    f.add(f.E(24, 9, 2.2, 1.8), 'pale', bias=.1)
    f.dagger((24, 8), (24, 0.5), blade=['#2a0606', '#4e0c0c', '#781414', '#a02020', '#c83a2a', '#ff6040'])
    for p in [(20, 3), (28, 2), (22, 0), (26, 5)]: f.px([p], '#ff6040', 170)
    return f

def necromancer():
    f = Fig()
    f.robe('black', wb=11)
    f.add(f.Pp([(16, 16), (32, 16), (30, 22), (18, 22)]), 'violet', bias=-.05)
    for x in range(17, 32, 3): f.px([(x, 22.5)], P['violet'][1])
    for i, x in enumerate((20, 22, 24, 26, 28)):
        f.mask(f.E(x, 24.5 + abs(24 - x) * -.2, .9, .9), '#d0c8b2')     # finger-bone necklace
    f.mask(f.E(24, 27, 1.8, 1.6), '#d0c8b2'); f.px([(23, 27), (25, 27)], '#60ff80')
    f.arm((17, 19.5), (12, 24), (12, 28), 'black', 'pale')
    f.staff((12, 45), (11, 6), ramp='bone', head='skull', orb=('#208040', '#60ff80', '#d0ffd8'))
    f.add(f.C([(9, 3), (8, 0), (10, -1)], .5) | f.C([(13, 3), (14, 0), (12, -1)], .5), 'bone')   # skull horns
    f.arm((31, 19.5), (36, 18), (38, 13), 'black', 'pale')
    f.flame((38, 12), ('#208040', '#60ff80', '#d0ffd8'), big=1)
    for p in [(34, 6), (41, 8), (37, 3)]: f.px([p], '#60ff80', 170)
    f.head('pale'); f.hood('violet', deep=True)
    f.px([(21, 11.2), (22, 11.2), (26, 11.2), (27, 11.2)], '#60ff80'); f.px([(20, 11.2), (28, 11.2)], '#60ff80', 100)
    f.mask(f.E(24, 14.6, 3.4, 2.2) & ~f.E(24, 13.6, 3.4, 2), P['pale'][3])
    f.px([(22, 15), (24, 15.4), (26, 15)], INK)
    return f

def hedgewitch():
    f = Fig()
    f.robe('green', wb=10)
    f.add(f.Pp([(15.5, 17), (32.5, 17), (31, 26), (17, 26)]), 'brown', bias=-.05)     # shawl
    for x in range(17, 32, 2): f.px([(x, 26.4)], P['brown'][1])
    for x, c in ((20, '#c070ff'), (24, '#e8c040'), (28, '#60c0ff')): f.px([(x, 28.5)], c)
    f.arm((17, 19.5), (12, 24), (12, 28), 'green', 'pale')
    f.add(f.C([(12, 45), (11, 30), (13, 18), (10, 8), (12, 4)], .9), 'wood')            # twisted staff
    f.add(f.E(12, 2, 2.4, 2.4), ['#40106a', '#7030b0', '#c070ff'], soft=1); f.px([(11, 1)], '#ffffff')
    for p in [(9, 0), (15, 2), (12, -1)]: f.px([p], '#c070ff', 170)
    f.arm((31, 19.5), (35, 23), (37, 22), 'green', 'pale')
    f.mask(f.C([(37, 22), (40, 20), (42, 21)], .4), P['pale'][3])   # crooked finger
    f.head('pale'); f.hair('gray', 'long')
    f.add(f.Pp([(23.5, 12), (25, 12), (26.5, 16), (24.5, 15)]), 'pale', bias=.15)       # hooked nose
    f.px([(26.5, 15.6)], '#4a6a3a')                                                      # wart
    f.face(mood='grin', eye='#80ff60', skin='pale')
    f.px([(22, 15.6), (23, 15.6), (25, 15.6)], INK)
    f.add(f.Pp([(18.5, 7), (29.5, 7), (27, 1), (30, -3), (24, 0), (21, 2)]), 'black', soft=1)
    f.add(f.E(24, 7.2, 10.6, 1.8), 'black', bias=-.05)
    f.mask(f.Pp([(19, 5.6), (29, 5.6), (29, 6.6), (19, 6.6)]), '#5a2a8a'); f.px([(26, 6)], GOLD)
    return f

def warlock():
    f = Fig()
    f.cape('black', lining='violet', side='center')
    f.robe('violet', wb=9.5)
    f.add(f.C([(19, 17.4), (19, 45)], .7) | f.C([(29, 17.4), (29, 45)], .7), 'gold', flat=3)
    f.mask(f.E(24, 24, 2.4, 2.4) & ~f.E(24, 24, 1.4, 1.4), '#c070ff'); f.px([(24, 24)], '#c070ff')   # eldritch eye sigil
    f.add(f.C([(17.5, 29.4), (30.5, 29.4)], .9), 'black', flat=2)
    # both hands up, hurling eldritch fire
    f.arm((17, 19.5), (11, 17), (8, 11), 'violet', 'pale')
    f.arm((31, 19.5), (37, 17), (40, 11), 'violet', 'pale')
    f.flame((8, 10), ('#5a1ab0', '#a060ff', '#f0e0ff'), big=1.15)
    f.flame((40, 10), ('#5a1ab0', '#a060ff', '#f0e0ff'), big=1.15)
    f.mask(f.C([(11, 8), (24, 3), (37, 8)], .4), '#a060ff', 150)
    f.head('pale'); f.hood('black', deep=True)
    f.add(f.C([(19.6, 4.6), (17, 0), (15, -1)], 1, .35) | f.C([(28.4, 4.6), (31, 0), (33, -1)], 1, .35), 'bone', bias=-.1)
    f.px([(21, 11.4), (22, 11.4), (26, 11.4), (27, 11.4)], '#c070ff'); f.px([(20, 11.4), (28, 11.4)], '#c070ff', 110)
    f.px([(22, 15), (23, 15.5), (24, 15.5), (25, 15.5), (26, 15)], '#c070ff', 160)
    return f

def pyromancer():
    f = Fig()
    f.robe('orange', wb=10)
    f.add(f.Pp([(17, 32), (31, 32), (34.5, 46), (13.5, 46)]), 'red', bias=-.08)          # flame-scorched hem
    for x in range(14, 35, 3): f.add(f.Pp([(x, 46), (x + 1.5, 41), (x + 3, 46)]), 'saffron', bias=.1)
    f.belt(29.5, 'dleather', buckle='#ffb040')
    f.arm((17, 19.5), (12, 15), (11, 9), 'orange', 'skin')
    f.flame((11, 8), big=1.5)
    f.arm((31, 19.5), (36, 23), (37, 27), 'orange', 'skin')
    f.flame((37, 27), big=.9)
    for p in [(16, 3), (7, 2), (14, 0), (6, 6), (19, 6)]: f.px([p], '#ffb040', 190)
    f.head('skin'); f.hair('red', 'wild', hi='#ff8a3a')
    f.mask(f.Pp([(18.6, 8), (29.4, 8), (29.4, 9.2), (18.6, 9.2)]), '#ffb040')
    f.face(mood='mad', eye='#ffb040', glow=True)
    f.px([(19.6, 13), (20.6, 13.6)], '#3a1a10'); f.px([(27.4, 13), (28.4, 12.6)], '#3a1a10')   # soot
    return f

def madmonk():
    f = Fig()
    f.legs('lunge', pants='saffron', boots=None)
    for x in (13, 15, 27, 29): f.px([(x, 46)], P['skin'][3])
    f.torso('skin', wt=6.8, wb=5.8)
    f.px([(21, 22), (22, 23), (26, 22), (27, 23), (23, 26), (25, 26)], P['skin'][2])
    f.add(f.Pp([(17, 17), (22, 17), (31, 30), (25, 31)]), 'saffron', bias=.05)          # robe draped over one shoulder
    f.add(f.C([(17.5, 29.5), (30.5, 29.5)], 1.1), 'red', flat=3)
    for i, x in enumerate(range(19, 30, 2)): f.mask(f.E(x, 18 + abs(24 - x) * .35, .8, .8), '#5a3a1a')  # prayer beads
    # mid-strike: one fist thrust forward, the other cocked back
    f.arm((31, 19.5), (35, 17), (38, 13), 'skin', 'white', hand_r=2.2)
    f.arm((17, 19.5), (12, 23), (14, 26), 'skin', 'white', hand_r=2.2)
    for p in [(41, 11), (42, 13), (41, 15), (43, 9)]: f.px([p], '#ffffff', 170)          # impact lines
    f.head('skin'); f.face(mood='mad', eye='#ff6a3a')
    f.mask(f.Pp([(18.6, 7.6), (29.4, 7.6), (29.4, 8.8), (18.6, 8.8)]), '#b4403a')
    f.add(f.C([(29, 8), (33, 10), (35, 9)], .7, .4), 'red')
    f.px([(22, 5.6), (23, 5.4), (25, 5.6)], P['skin'][4])
    f.px([(20, 12.4), (20, 13.4), (21, 14.4)], '#8a3a30')
    return f

def mercenary():
    f = Fig()
    f.legs('wide', pants='pants', boots='boot')
    f.torso('steel', wt=7)
    f.add(f.Pp([(18, 20), (30, 20), (29.5, 30), (18.5, 30)]), 'blue', bias=-.05)         # gambeson
    for y in (22, 25, 28): f.mask(f.C([(18.5, y), (29.5, y)], .3), P['blue'][1])
    f.belt(29.6, 'leather'); f.tails('blue', 30)
    f.pauldron(17.5, 18.6); f.pauldron(30.5, 18.6)
    f.add(f.C([(30, 18), (18, 29)], .8), 'leather'); f.mask(f.E(26, 21, 1.4, 1.6), P['leather'][3]); f.px([(26, 20)], GOLD)  # coin pouch
    f.arm((31, 19.5), (35, 24), (34, 28), 'steel', 'leather')
    f.shield((35.5, 29), 'kite', 'blue', 'steel', emblem='cross')
    f.arm((17, 19.5), (12, 23), (11, 27), 'steel', 'leather')
    f.sword((11, 27), (7, 6), w=1.4)
    f.head('skin'); f.hair('brown', 'short'); f.beard('brown', length=7)
    f.face(mood='cold', eye='#3a2a1a')
    f.add(f.E(24, 6.8, 5.8, 2.8) & (yy < f.T(0, 8.2)[1]), 'steel'); f.px([(24, 8.4), (24, 9.4), (24, 10.4)], P['steel'][3])
    f.px([(27, 13), (28, 14)], '#8a3a30')
    return f

def fallenknight():
    f = Fig()
    f.cape(['#100406', '#22080c', '#3a0e14', '#561620', '#70202c', '#8c2c38'], side='left')
    for p in [(5, 40), (8, 44), (11, 38)]: f.px([p], '#08060a')   # tattered holes
    f.legs('wide', pants='dsteel', boots='dsteel')
    f.torso('dsteel', wt=7)
    f.add(f.Pp([(19.5, 18), (28.5, 18), (28, 34), (24, 36), (20, 34)]), ['#100406', '#22080c', '#3a0e14', '#561620', '#70202c'], soft=1)
    f.mask(f.C([(24, 20), (24, 31)], .6) | f.C([(21.5, 24), (26.5, 24)], .6), '#9c2a24')
    for p in [(21, 33), (27, 32), (25, 35)]: f.px([p], '#08060a')
    f.belt(29, 'dleather', buckle='#9c2a24')
    f.pauldron(17.5, 18.6, 'dsteel'); f.pauldron(30.5, 18.6, 'dsteel')
    f.arm((31, 19.5), (35, 24), (34, 28), 'dsteel', 'dsteel')
    f.shield((35.5, 30), 'kite', 'dsteel', 'dsteel', emblem='cross', emblem_c='#9c2a24')
    f.mask(f.C([(32, 25), (36, 33)], .4), '#08060a')     # crack
    f.arm((17, 19.5), (12, 23), (12, 28), 'dsteel', 'dsteel')
    f.sword((12, 28), (8, 4), blade='dsteel', guard='#3a3e48', pommel='#ff3b2e', w=1.7, gleam=False)
    f.add(f.E(24, 10.6, 5.6, 6.4), 'dsteel', soft=1.2)
    f.add(f.C([(24, 4), (21, 0), (17, -1)], 1.3, .6), ['#100406', '#3a0e14', '#70202c'], bias=.1)
    f.mask(f.Pp([(19.4, 10), (28.6, 10), (28.6, 11.2), (19.4, 11.2)]), '#050506')
    f.px([(21, 10.5), (22, 10.5), (26, 10.5), (27, 10.5)], '#ff3b2e'); f.px([(20, 10.5), (28, 10.5)], '#ff3b2e', 110)
    f.mask(f.C([(26, 6), (27, 9)], .35), '#050506')
    for p in [(16, 3), (32, 8), (20, 0)]: f.px([p], '#9c2a24', 140)   # embers
    return f

def gladiator():
    f = Fig()
    f.legs('lunge', pants='leather', boots='leather', cuff=GOLD)
    f.torso('tan', wt=7, wb=6)
    f.px([(21, 22), (22, 23), (26, 22), (27, 23), (23, 26), (25, 26)], P['tan'][2])
    f.add(f.C([(18, 18), (30, 29)], 1), 'leather')
    f.add(f.Pp([(17.5, 29), (30.5, 29), (32, 37), (16, 37)]), 'red', bias=-.05)
    for x in (17, 19.5, 22, 24.5, 27, 29.5): f.mask(f.C([(x, 29.5), (x + .3, 36.5)], .3), P['red'][1])
    f.belt(29.2, 'bronze', buckle=None)
    f.add(f.E(30.5, 18.6, 3.8, 3), 'bronze', bias=.1); f.px([(29.5, 17.6)], '#ffffff', 200)   # manica shoulder
    f.arm((31, 19.5), (35, 23), (34, 27), 'bronze', 'tan')
    f.shield((34.5, 27), 'buckler', 'bronze', 'gold')
    f.arm((17, 19.5), (12, 20), (9, 15), 'tan', 'tan')
    f.haft((10, 22), (6, -1), 'steel', .8)
    for dx in (-2.4, 0, 2.4): f.add(f.C([(6 + dx, -1), (6 + dx * 1.1, -5)], .6, .3), 'steel', bias=.1)
    f.add(f.C([(3.4, -1), (8.6, -1)], .6), 'steel')
    f.head('tan')
    f.add(f.E(24, 9, 6, 5.6) & (yy < f.T(0, 12.6)[1]), 'bronze', soft=1)
    f.add(f.C([(18, 4), (24, 1), (30, 4)], 1.6, 1), 'red', bias=.05)                     # crest
    f.mask(f.Pp([(20, 10), (28, 10), (28, 12), (20, 12)]) & ~f.C([(24, 10), (24, 12)], .5), '#120a04')
    f.px([(21.5, 11), (26.5, 11)], '#ffd060')
    f.face(mood='grin', eye='#ffd060', skin='tan')
    return f

def executioner():
    f = Fig(k=1.04, w=1.18)
    f.legs('wide', pants='black', boots='boot')
    f.torso('skin', wt=7.8, wb=6.4)
    f.px([(21, 22), (22, 23), (26, 22), (27, 23), (23, 26), (25, 26), (24, 28)], P['skin'][2])
    f.add(f.Pp([(17.5, 22), (30.5, 22), (31, 37), (17, 37)]) & (yy > f.T(0, 25)[1]), 'dleather', bias=-.05)   # leather apron
    f.mask(f.C([(17.5, 25), (30.5, 25)], .7), P['dleather'][1])
    for p in [(22, 31), (27, 34), (20, 35)]: f.px([p], '#5a0a0a')
    # massive greataxe held across the body
    f.arm((17, 19.5), (13, 25), (17, 29), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.3)
    f.arm((31, 19.5), (35, 22), (31, 21), 'skin', 'skin', r1=2.6, r2=2.2, hand_r=2.3)
    f.haft((14, 34), (36, 12), 'wood', 1.2)
    f.add(f.Pp([(33, 13), (38, 4), (45, 8), (44, 17), (38, 18)]), 'steel', bias=.05)
    f.mask(f.C([(39, 4.6), (45, 8.4), (44.4, 16)], .45), '#e8f2ff')
    f.px([(41, 12), (42, 14)], '#5a0a0a')
    f.head('black', rx=5.6, ry=6.4)
    f.add(f.Pp([(19, 14), (29, 14), (30, 19), (18, 19)]), 'black')
    f.mask(f.E(21.5, 10.6, 1.4, 1) | f.E(26.5, 10.6, 1.4, 1), '#050505')
    f.px([(21.5, 10.6), (26.5, 10.6)], '#ff3b2e')
    return f

def darkelf():
    f = Fig()
    f.cape('purple', side='right')
    f.legs('lunge', pants='black', boots='black', cuff='#c070ff')
    f.torso('black', wt=6.4, wb=5.4)
    f.mask(f.C([(20, 18), (24, 23), (28, 18)], .5) | f.C([(24, 23), (24, 29)], .5), '#7a3ab8')   # filigree
    f.belt(29.6, 'black', buckle='#c070ff')
    f.add(f.Pp([(18.6, 29), (29.4, 29), (31, 37), (24, 34), (17, 37)]), 'black', bias=-.05)
    blade = ['#20102a', '#3a1e4a', '#5a2e6e', '#7a4290', '#9c5ab0', '#c080d8']
    f.arm((17, 19.5), (11, 21), (7, 17), 'black', 'drow')
    f.add(f.C([(7, 17), (2, 11), (1, 4)], 1.1, .5), blade, bias=.15)                       # curved scimitar
    f.mask(f.C([(6, 16), (2.4, 11), (1.6, 6)], .3), '#e0c0ff')
    f.add(f.C([(4.5, 19), (9.5, 15)], .8), 'gold', flat=3)
    f.arm((31, 19.5), (36, 23), (37, 27), 'black', 'drow')
    f.dagger((37, 27), (40, 33), blade=blade)
    f.add(f.C([(19.6, 10), (13, 5)], 1.1, .3) | f.C([(28.4, 10), (35, 5)], 1.1, .3), 'drow')   # long ears
    f.head('drow'); f.hair('white', 'long')
    f.face(mood='cold', eye='#ff3b2e', skin='drow', brow='#e8e8f0')
    f.mask(f.C([(20, 14), (21, 15.6)], .3), '#c070ff')
    return f

def deepdwarf():
    f = Fig(k=.82, w=1.3)
    f.legs('wide', pants='dsteel', boots='dsteel')
    f.torso('dsteel', wt=7.6, wb=7)
    f.mask(f.C([(18, 24), (30, 24)], .4), P['dsteel'][4])
    f.belt(29.4, 'leather', buckle=GOLD)
    f.pauldron(17, 18.4, 'dsteel', 3.6, 2.8); f.pauldron(31, 18.4, 'dsteel', 3.6, 2.8)
    f.arm((31, 19.5), (35, 24), (34.5, 28), 'dsteel', 'dsteel', hand_r=2.2)
    f.shield((35.5, 29), 'round', 'dsteel', 'bronze', r=6.4)
    f.mask(f.E(35.5, 29, 3.4, 3.6) & ~f.E(35.5, 29, 2.4, 2.6), P['bronze'][4])
    f.arm((17, 19.5), (12, 19), (11, 13), 'dsteel', 'dsteel', hand_r=2.2)
    f.haft((11.5, 18), (10, 3)); f.add(f.Pp([(5, 1), (16, 1), (16, 6), (5, 6)]), 'dsteel', bias=.05)   # warhammer head
    f.mask(f.C([(5.5, 1.6), (5.5, 5.4)], .45), '#c8d0dc')
    for x in (7, 10, 13): f.px([(x, 3.5)], '#ffb040')    # glowing runes
    f.head('dwarf')
    f.beard('gray', length=16, braid=True)
    f.face(mood='angry', eye='#ffb040', glow=True, skin='dwarf')
    f.add(f.E(24, 6.8, 6.2, 3.2) & (yy < f.T(0, 8.6)[1]), 'dsteel')
    f.add(f.Pp([(18, 7), (13, 3), (19, 5)]) | f.Pp([(30, 7), (35, 3), (29, 5)]), 'bronze', bias=.1)
    f.px([(24, 5), (24, 6)], '#ffb040')
    return f

def inquisitor():
    f = Fig()
    f.cape('black', lining='crimson', side='left')
    f.legs('stand', pants='black', boots='boot', cuff=GOLD)
    f.robe('crimson', wb=8.5, slit=False)
    f.mask(f.C([(24, 18), (24, 40)], .6), GOLD)
    f.mask(f.E(24, 23, 2, 2) & ~f.E(24, 23, 1, 1), GOLD)
    f.add(f.C([(18, 29.5), (30, 29.5)], 1), 'black', flat=2)
    f.add(f.C([(17, 18), (31, 18)], 1.3), 'black', flat=2)
    f.arm((31, 19.5), (35, 24), (34, 28), 'crimson', 'black')
    f.add(f.C([(34, 29), (34, 31)], .4), 'dsteel')
    f.add(f.Pp([(32, 31), (36, 31), (36, 37), (32, 37)]), 'dsteel'); f.mask(f.Pp([(32.7, 32), (35.3, 32), (35.3, 36), (32.7, 36)]), '#ffd060'); f.px([(34, 34)], '#fff4c0')
    for d in [(-3, 0), (3, -1), (0, 4), (-2, 5)]: f.px([(34 + d[0], 34 + d[1])], '#ffd060', 140)
    f.arm((17, 19.5), (12, 18), (10, 13), 'crimson', 'black')
    f.sword((10, 13), (4, 1), w=1.3)
    f.head('skin'); f.face(mood='cold', eye='#3a2a1a')
    f.mask(f.C([(20, 15.2), (28, 15.2)], .3), P['skin'][1])
    f.add(f.Pp([(18.5, 7.4), (29.5, 7.4), (28, 2), (20, 2)]), 'black', soft=1)
    f.add(f.E(24, 7.6, 11.6, 1.8), 'black', bias=-.05)
    f.mask(f.Pp([(18.6, 6), (29.4, 6), (29.4, 7.2), (18.6, 7.2)]), GOLD)
    f.mask(f.E(24, 6.6, .9, .9), '#ffffff')
    return f

def goblin():
    f = Fig(k=.82)
    f.legs('crouch', pants='brown', boots=None)
    for x in (16, 18, 30, 32): f.px([(x, 46)], P['goblin'][3])
    f.torso('brown', wt=6.2, wb=5.4)
    for x in (18, 21, 25, 29): f.px([(x, 30.5)], P['brown'][1])
    f.add(f.C([(18, 18), (30, 29)], .9), 'leather'); f.belt(29.4, 'leather', buckle=None)
    f.mask(f.E(29, 31, 1.6, 1.8), P['leather'][3]); f.px([(29, 30)], GOLD)
    f.arm((31, 19), (36, 21), (39, 18), 'brown', 'goblin')
    f.px([(41, 16), (42, 17), (41, 18)], P['goblin'][4])
    f.arm((17, 19), (12, 19), (9, 14), 'brown', 'goblin')
    f.add(f.Pp([(9, 14), (5, 4), (2, 6), (4, 12)]), 'steel', bias=.05)                 # rusty cleaver
    f.px([(4, 8), (5, 10)], '#8a3a20'); f.add(f.C([(9, 14), (10, 17)], .7), 'wood')
    goblin_head(f)
    return f

def cultist():
    f = Fig()
    f.robe('black', wb=10)
    f.mask(f.C([(17, 45.4), (31, 45.4)], .5), '#7a1018')
    f.mask(f.E(24, 24, 2.6, 2.6) & ~f.E(24, 24, 1.6, 1.6), '#c8202a'); f.px([(24, 24)], '#c8202a')
    f.add(f.C([(18, 29.5), (30, 29.5)], .9), 'crimson', flat=2)
    f.arm((17, 19.5), (13, 24), (17, 27), 'black', 'pale')
    f.arm((31, 19.5), (35, 24), (31, 27), 'black', 'pale')
    f.add(f.Pp([(19, 26), (29, 26), (28.5, 31), (19.5, 31)]), 'crimson')                # tome clutched to the chest
    f.mask(f.E(24, 28.5, 1.4, 1.4), GOLD)
    f.add(f.C([(16, 27), (16, 33)], .4), 'dsteel'); f.mask(f.E(16, 34, 1.3, 1.5), '#ffd060')   # hanging censer
    for p in [(15, 37), (17, 39), (16, 41)]: f.px([p], '#8a8a90', 160)
    f.head('pale'); f.hood('black', deep=True)
    f.add(f.E(24, 13, 3.6, 4) & (yy > f.T(0, 9.6)[1]), 'bone', bias=.1)                # bone mask
    f.px([(22, 12), (26, 12)], '#ff3b2e'); f.px([(23, 15), (24, 15.4), (25, 15)], INK)
    return f

FOLK3 = {'bandit': bandit, 'banditcaptain': banditcaptain, 'cutpurse': cutpurse, 'assassin': assassin, 'thug': thug,
         'cultfanatic': cultfanatic, 'necromancer': necromancer, 'hedgewitch': hedgewitch, 'warlock': warlock, 'pyromancer': pyromancer,
         'madmonk': madmonk, 'mercenary': mercenary, 'fallenknight': fallenknight, 'gladiator': gladiator, 'executioner': executioner,
         'darkelf': darkelf, 'deepdwarf': deepdwarf, 'inquisitor': inquisitor, 'goblin': goblin, 'cultist': cultist}

if __name__ == '__main__':
    imgs = [f().render() for f in FOLK3.values()]
    sheet(imgs, scale=4, cols=5).save('folk3.png')
