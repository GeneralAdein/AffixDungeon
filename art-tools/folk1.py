from hk import *

def knight():
    f = Fig()
    f.cape('royal', lining='gold', side='left')
    f.legs('wide', pants='steel', boots='steel')
    f.torso('steel')
    f.add(f.Pp([(19.5, 18), (28.5, 18), (28, 34), (24, 36), (20, 34)]), 'royal', soft=1)   # tabard
    f.mask(f.C([(24, 20), (24, 31)], .6) | f.C([(21.5, 24), (26.5, 24)], .6), GOLD)
    f.belt(28.8, 'leather')
    f.pauldron(17.5, 18.6); f.pauldron(30.5, 18.6)
    f.arm((31, 20), (35, 24), (34, 28), 'steel', 'steel')
    f.shield((35.5, 30), 'kite', 'royal', 'steel', emblem='sun')
    f.arm((17, 20), (13, 16), (14, 11), 'steel', 'steel')
    f.sword((14, 11), (6, -2), w=1.5)
    # great helm with plume
    f.add(f.E(24, 10.6, 5.6, 6.4), 'steel', soft=1.2)
    f.add(f.C([(24, 4), (27, 1), (31, 2), (33, 5)], 1.4, .7), 'royal', bias=.1)
    f.mask(f.Pp([(19.4, 10), (28.6, 10), (28.6, 11.2), (19.4, 11.2)]), '#050608')
    f.px([(21, 10.5), (27, 10.5)], '#7fd8ff')
    f.px([(24, 12.5), (24, 13.5), (24, 14.5)], P['steel'][2]); f.px([(22, 14), (26, 14), (22, 15), (26, 15)], '#050608')
    f.px([(21, 7), (22, 6)], '#ffffff')
    return f

def dreadknight():
    f = Fig(k=1.04, w=1.08)
    f.cape('black', lining='violet', side='right')
    f.legs('wide', pants='dsteel', boots='dsteel')
    f.torso('dsteel', wt=7.4, wb=6.4)
    f.mask(f.C([(24, 19), (24, 29)], .5), '#7a3ab8'); f.px([(22, 21), (26, 21), (23, 22), (25, 22)], '#7a3ab8')
    # spiked pauldrons
    for x, s in ((17, -1), (31, 1)):
        f.add(f.E(x, 18.4, 3.8, 2.8), 'dsteel', bias=.1)
        f.add(f.Pp([(x - 1, 16.5), (x + s * 4, 12), (x + 1.5, 17)]), 'dsteel', bias=.2)
    f.belt(29, 'dleather', buckle='#7a3ab8')
    f.add(f.Pp([(18, 29), (30, 29), (31.5, 35), (27, 33), (24, 36), (21, 33), (16.5, 35)]), 'dsteel', bias=-.05)
    # two-handed greatsword held point-down in front, both hands on the hilt
    f.arm((17, 20), (16, 25), (22, 27.5), 'dsteel', 'dsteel')
    f.arm((31, 20), (32, 25), (26, 27.5), 'dsteel', 'dsteel')
    f.sword((24, 27), (24, 45.5), blade=['#140a1c', '#26143a', '#3a2058', '#523078', '#6c44a0', '#8c60c8'], guard='#3a2058', pommel='#b070ff', w=1.7, gleam=False)
    f.add(f.C([(24, 27), (24, 23)], .9), 'dleather'); f.px([(24, 22)], '#b070ff')
    # horned helm, glowing eye slit
    f.add(f.E(24, 10.4, 5.6, 6.4), 'dsteel', soft=1.2)
    f.add(f.C([(19.6, 7), (15.5, 3), (14.5, -1)], 1.3, .4) | f.C([(28.4, 7), (32.5, 3), (33.5, -1)], 1.3, .4), 'bone', bias=-.1)
    f.mask(f.Pp([(19.4, 10), (28.6, 10), (27.6, 11.4), (20.4, 11.4)]), '#050508')
    f.px([(21, 10.6), (22, 10.6), (26, 10.6), (27, 10.6)], '#c070ff'); f.px([(20, 10.6), (28, 10.6)], '#c070ff', 120)
    f.px([(22, 14), (24, 14.5), (26, 14)], '#050508')
    return f

def squire():
    f = Fig(k=.9)
    f.legs('lunge', pants='pants', boots='leather', cuff=GOLD)
    f.torso('blue', wt=6.5, wb=5.6)
    f.add(f.Pp([(20, 17), (28, 17), (27.5, 31), (20.5, 31)]), 'white', bias=.05)          # tabard
    f.mask(f.E(24, 23, 1.8, 2.4), '#2e66aa'); f.px([(24, 21)], GOLD)
    f.belt(29.6, 'leather')
    f.arm((31, 19.5), (35, 23), (35.5, 27), 'blue')
    f.shield((36, 27.5), 'round', 'wood', 'steel', r=5)
    f.mask(f.C([(36, 23), (36, 32)], .6), '#2e66aa')
    f.arm((17, 19.5), (12, 21), (9, 19), 'blue')
    f.sword((9, 19), (1, 12), w=1.2)
    f.head('skinlt'); f.hair('wood', 'swept', hi='#c08a50')
    f.add(f.E(24, 6.6, 5.4, 2.6) & (yy < f.T(0, 8)[1]), 'steel')
    f.face(mood='angry', eye='#2a5a9a', skin='skinlt', teeth=True)
    f.px([(21, 13.5), (27, 13.5)], '#d88070')
    return f

def bowman():
    f = Fig()
    f.cape('forest', side='center')
    f.legs('wide', pants='brown', boots='leather')
    f.torso('forest', wt=6.6)
    f.add(f.C([(30, 18), (19, 29)], 1.1), 'leather', bias=.1)     # quiver strap
    f.add(f.Pp([(28, 13), (33, 13), (33.5, 25), (28.5, 25)]), 'leather', bias=.05)  # quiver
    for x in (29, 30.5, 32): f.add(f.C([(x, 13), (x + .5, 8)], .5), 'wood'); f.px([(x + .5, 7), (x + .5, 6)], '#e8e0d0')
    f.belt(29.5, 'leather')
    # drawing the bow: left arm out with bow, right hand at the cheek
    f.arm((17, 19.5), (11, 20), (6, 20), 'forest', 'leather')
    f.bow(6, 20, h=20, draw=True)
    f.add(f.C([(6, 20), (19, 18.5)], .45), 'wood'); f.spearhead((5, 20), (-1, 0)); f.px([(19, 17.5), (19, 19.5)], '#c83a2a')
    f.arm((31, 19.5), (27, 21), (21, 18.5), 'forest', 'leather')
    f.head('skin'); f.hood('forest')
    f.face(mood='cold', eye='#2a4a1a', teeth=False)
    f.px([(20, 12.5), (21, 13.5)], '#5a7a2a')
    return f

def pikeman():
    f = Fig()
    f.legs('lunge', pants='pants', boots='boot')
    f.torso('steel', wt=6.8)
    f.add(f.Pp([(19, 21), (29, 21), (28.5, 30), (19.5, 30)]), 'crimson', bias=.05)
    f.mask(f.C([(19.5, 24), (28.5, 24)], .4) | f.C([(19.5, 27), (28.5, 27)], .4), P['crimson'][1])
    f.belt(29.6, 'leather'); f.tails('pants', 30)
    f.pauldron(17.5, 18.6); f.pauldron(30.5, 18.6)
    # pike leveled diagonally across the body
    f.arm((17, 20), (14, 26), (17, 29), 'steel', 'leather')
    f.arm((31, 20), (34, 22), (31, 23.5), 'steel', 'leather')
    f.haft((20, 33), (47, 7), 'wood', .9)
    f.spearhead((47, 7), (.72, -.69))
    f.add(f.C([(38.5, 14.5), (40, 16)], 1.2), 'crimson')
    f.head('skin')
    f.add(f.E(24, 7.4, 6.6, 3.6) & (yy < f.T(0, 9)[1]) | f.E(24, 8.8, 7.6, 1), 'steel', bias=.05)   # kettle helm
    f.add(f.E(24, 5.2, 1.4, 1.2), 'steel')
    f.beard('brown', length=8)
    f.face(mood='angry', eye='#3a2a1a')
    return f

def jester():
    f = Fig()
    f.legs('crouch', pants='red', boots='purple')
    f.px([(14, 46), (35, 46)], GOLD)
    # split motley body
    f.torso('purple', wt=6.6, wb=5.8)
    f.mask(f.Pp([(24, 17), (30.6, 17), (29.8, 30), (24, 30)]), P['red'][3])
    f.mask(f.Pp([(24, 17), (30.6, 17), (30.3, 20), (24, 20)]), P['red'][4])
    for y, x in ((20, 22), (24, 26), (27, 21)): f.px([(x, y), (x + 1, y)], GOLD)
    f.add(f.Pp([(17, 16.5), (31, 16.5), (29, 19), (26, 18), (24, 19.5), (22, 18), (19, 19)]), 'white', bias=.1)  # ruff
    f.belt(29.6, 'leather', buckle=None)
    # arms flung wide, dagger in one hand, juggling ball above the other
    f.arm((17, 19.5), (12, 18), (8, 14), 'red')
    f.dagger((8, 14), (4, 8))
    f.arm((31, 19.5), (36, 17), (39, 13), 'purple')
    f.mask(f.E(39, 8, 1.5, 1.5), '#e8c040'); f.mask(f.E(35, 5, 1.4, 1.4), '#3a9aff'); f.mask(f.E(42, 4, 1.4, 1.4), '#ff4a5a')
    f.head('pale')
    # jester hat: two drooping points with bells
    f.add(f.C([(21, 7), (16, 3), (12, 5), (11, 9)], 1.8, .7), 'red', bias=.05)
    f.add(f.C([(27, 7), (32, 3), (36, 5), (37, 9)], 1.8, .7), 'purple', bias=.05)
    f.add(f.E(24, 6.6, 5.6, 2.6) & (yy < f.T(0, 8.4)[1]), 'red')
    f.mask(f.E(24, 6.6, 5.6, 2.6) & (yy < f.T(0, 8.4)[1]) & (xx > f.T(24, 0)[0]), P['purple'][3])
    f.mask(f.E(11, 10, 1.3, 1.3) | f.E(37, 10, 1.3, 1.3), GOLD)
    # painted face: diamond eyes, huge grin
    f.face(mood='grin', eye='#1a1a2a', skin='pale', brow='#2a1a3a')
    f.px([(21, 9.5), (21, 12), (27, 9.5), (27, 12)], '#1a1a2a')
    f.px([(19, 14), (29, 14), (20, 15), (28, 15)], INK); f.px([(22, 13), (26, 13)], '#d84060')
    return f

def mage():
    f = Fig()
    f.robe('royal', wb=11)
    f.add(f.Pp([(19.5, 17), (28.5, 17), (30, 46), (18, 46)]) & ~f.Pp([(21, 17), (27, 17), (27, 46), (21, 46)]), 'royal', bias=.12)
    for y in (20, 26, 32, 38, 44): f.px([(18.5 + (y - 20) * .06, y), (29.5 - (y - 20) * .06, y)], GOLD)
    f.mask(f.C([(17, 45.4), (31, 45.4)], .5), GOLD)
    f.add(f.C([(18, 26), (30, 26)], 1), 'gold', flat=3)
    # casting: free hand raised, crackling arcane energy
    f.arm((31, 19.5), (36, 15), (37, 9), 'royal')
    f.flame((37, 8), ('#3a8aff', '#8ad0ff', '#ffffff'), big=1.1)
    f.arm((17, 19.5), (12, 24), (11, 29), 'royal')
    f.staff((11, 45), (10, 5), orb=('#2a7aff', '#8ad0ff', '#ffffff'), orb_r=2.8)
    f.mask(f.C([(10, 5), (8, 3)], .4) | f.C([(10, 5), (12, 2.5)], .4), P['gold'][4])
    f.head('skinlt'); f.beard('white', length=13)
    # tall wizard hat with stars
    f.add(f.Pp([(18.5, 7.5), (29.5, 7.5), (28, 2), (31, -2), (25, 0), (22, 1)]), 'royal', soft=1)
    f.add(f.E(24, 7.6, 9.6, 1.6), 'royal', bias=-.05)
    f.px([(23, 3), (26, 5), (25, 1)], GOLD)
    f.face(mood='cold', eye='#7fe0ff', glow=True, skin='skinlt')
    f.px([(20, 9), (21, 9), (27, 9), (28, 9)], '#e8e8e8')
    return f

def priest():
    f = Fig()
    f.robe('white', wb=10)
    f.add(f.Pp([(21.5, 17), (26.5, 17), (26.5, 46), (21.5, 46)]), 'gold', bias=.05)    # stole
    f.mask(f.C([(24, 22), (24, 28)], .55) | f.C([(22, 24), (26, 24)], .55), '#ffffff')
    f.belt(29.5, 'gold', buckle=None)
    f.arm((17, 19.5), (13, 24), (13, 28), 'white')
    f.staff((13, 45), (12, 6), ramp='gold', head='orb', orb=('#d49c34', '#ffe08a', '#ffffff'), orb_r=2.4)
    f.mask(f.E(12, 3.6, 4.6, 4.6) & ~f.E(12, 3.6, 3.8, 3.8), '#ffe08a', 170)
    # open holy book held out, glowing
    f.arm((31, 19.5), (35, 24), (33, 27), 'white')
    f.add(f.Pp([(30, 25), (37, 24), (37.5, 28), (30.5, 29)]), 'crimson')
    f.mask(f.Pp([(30.7, 25.3), (33.8, 24.8), (34, 27.8), (31, 28.3)]) | f.Pp([(34.2, 24.8), (36.8, 24.4), (37, 27.6), (34.4, 27.8)]), '#f4ecd8')
    for d in [(-1, -4), (2, -5), (4, -3), (0, -6)]: f.px([(34 + d[0], 25 + d[1])], '#ffe08a', 200)
    f.head('skin'); f.hair('brown', 'short')
    f.mask(f.E(24, 6.6, 2.6, 1.2), P['skin'][3])         # tonsure
    f.face(mood='calm', eye='#3a2a1a')
    f.mask(f.E(24, 3.4, 4, .9) & ~f.E(24, 3.4, 3, .3), '#ffe08a')   # halo
    return f

FOLK1 = {'knight': knight, 'dreadknight': dreadknight, 'squire': squire, 'bowman': bowman, 'pikeman': pikeman, 'jester': jester, 'mage': mage, 'priest': priest}

if __name__ == '__main__':
    imgs = [f().render() for f in FOLK1.values()]
    sheet(imgs, scale=5, cols=4).save('folk1.png')
