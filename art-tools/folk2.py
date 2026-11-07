from hk import *

def goblin_head(f, skin='goblin', hy=11, eye='#ffc93c', grin=True, ears=True):
    if ears:
        f.add(f.Pp([(19.5, hy - 1), (8, hy - 5), (11, hy - 1), (19, hy + 3)]) | f.Pp([(28.5, hy - 1), (40, hy - 5), (37, hy - 1), (29, hy + 3)]), skin, bias=.05)
        f.mask(f.Pp([(18.5, hy - .5), (11, hy - 3.5), (18.5, hy + 1.5)]) | f.Pp([(29.5, hy - .5), (37, hy - 3.5), (29.5, hy + 1.5)]), '#7a3a30')
    f.add(f.E(24, hy, 5.6, 5), skin, soft=1.2)
    f.add(f.Pp([(23, hy + 1), (25, hy + 1), (24.5, hy + 5), (23.5, hy + 5)]), skin, bias=.15)   # long nose
    f.px([(20, hy - 2), (21, hy - 2), (22, hy - 1), (28, hy - 2), (27, hy - 2), (26, hy - 1)], INK)
    f.px([(21, hy), (22, hy), (26, hy), (27, hy)], eye); f.px([(22, hy), (26, hy)], INK)
    if grin:
        f.mask(f.Pp([(19.5, hy + 3), (28.5, hy + 3), (26.5, hy + 5.5), (21.5, hy + 5.5)]), '#2a0808')
        f.px([(20, hy + 3), (22, hy + 3), (26, hy + 3), (28, hy + 3), (21, hy + 4), (27, hy + 4), (23, hy + 5), (25, hy + 5)], '#e8dcb8')

def orc_head(f, skin='orc', hy=11, eye='#ff3b2e'):
    f.add(f.E(24, hy - .5, 5.6, 5.4), skin, soft=1.2)
    f.add(f.E(24, hy + 3.4, 5.6, 3.2), skin, bias=.06)          # heavy jaw
    f.mask(f.C([(19, hy - 2), (29, hy - 2)], .7), P[skin][1] if isinstance(skin, str) else skin[1])   # brow ridge
    f.px([(21, hy - .8), (22, hy - .8), (26, hy - .8), (27, hy - .8)], eye); f.px([(22, hy - .8), (26, hy - .8)], '#300808')
    f.px([(23, hy + 1.4), (25, hy + 1.4)], INK)
    f.mask(f.C([(20.5, hy + 4.4), (27.5, hy + 4.4)], .5), '#200606')
    f.px([(20.5, hy + 3.4), (20.5, hy + 2.4), (27.5, hy + 3.4), (27.5, hy + 2.4)], '#f0e6c8'); f.px([(20.5, hy + 4.4), (27.5, hy + 4.4)], '#c8bc9c')

def snout_head(f, skin, hy=11, eye='#ffd040', snout=(3, 3.6), horns=None, crest=None, ears=None, mane=None):
    if mane: f.add(f.E(24, hy + 2, 7, 6), mane, dither=False, bias=-.1)
    if ears == 'hyena':
        f.add(f.Pp([(19.5, hy - 2), (17, hy - 9), (22, hy - 4)]) | f.Pp([(28.5, hy - 2), (31, hy - 9), (26, hy - 4)]), skin)
        f.mask(f.Pp([(19.5, hy - 3), (18, hy - 7), (21, hy - 4)]) | f.Pp([(28.5, hy - 3), (30, hy - 7), (27, hy - 4)]), '#3a2010')
    if horns: f.add(f.C([(21, hy - 3), (18, hy - 7), (16.5, hy - 9)], 1.1, .4) | f.C([(27, hy - 3), (30, hy - 7), (31.5, hy - 9)], 1.1, .4), horns, bias=.1)
    if crest: f.add(f.Pp([(22.5, hy - 4), (24, hy - 9), (25.5, hy - 4)]) | f.Pp([(24, hy - 5), (27, hy - 8), (26.5, hy - 3)]), crest, bias=.1)
    f.add(f.E(24, hy - .4, 5, 4.6), skin, soft=1.2)
    f.add(f.E(24, hy + 3.6, snout[0], snout[1]), skin, bias=.12)
    f.px([(23, hy + 5.4), (25, hy + 5.4)], INK)
    f.mask(f.C([(21.5, hy + 6.8), (26.5, hy + 6.8)], .45), '#2a0808')
    f.px([(22, hy + 6.2), (24, hy + 6.2), (26, hy + 6.2)], '#ece0c0')
    f.px([(20.5, hy - .6), (21.5, hy - .6), (26.5, hy - .6), (27.5, hy - .6)], eye); f.px([(21.5, hy - .6), (26.5, hy - .6)], INK)
    f.px([(20, hy - 2), (21, hy - 2.4), (28, hy - 2), (27, hy - 2.4)], INK)

def goblinarcher():
    f = Fig(k=.84)
    f.legs('crouch', pants='brown', boots='leather')
    f.torso('leather', wt=6.4, wb=5.6)
    f.add(f.C([(30, 18), (19, 29)], 1), 'dleather'); f.belt(29.4, 'dleather', buckle=None)
    f.add(f.Pp([(15, 15), (20, 13), (21, 26), (16, 27)]), 'leather', bias=.05)   # quiver on the back
    for x in (16, 17.5, 19): f.add(f.C([(x, 14), (x - .5, 9)], .45), 'wood'); f.px([(x - .5, 8)], '#c83a2a')
    f.arm((31, 19), (36, 19), (40, 19), 'leather', 'goblin')
    f.bow(40, 19, h=18, draw=True)
    f.add(f.C([(41, 19), (27, 19)], .45), 'wood'); f.spearhead((42, 19), (1, 0))
    f.arm((17, 19), (21, 21), (27, 19.5), 'leather', 'goblin')
    goblin_head(f)
    f.add(f.E(24, 6.6, 5.6, 2.4) & (yy < f.T(0, 8)[1]), 'forest')
    f.add(f.C([(27, 6), (31, 3)], .6), 'forest'); f.px([(31, 2), (32, 1)], '#c83a2a')
    return f

def goblinshaman():
    f = Fig(k=.84)
    f.robe('brown', wb=9)
    f.add(f.Pp([(16.5, 17), (31.5, 17), (30, 24), (18, 24)]), 'fur', bias=.05)    # fur mantle
    for x in range(17, 31, 2): f.px([(x, 24.5)], P['fur'][1])
    for i, x in enumerate((20, 22, 24, 26, 28)): f.px([(x, 26 - abs(24 - x) * .3)], '#e8dcb8' if i % 2 else '#d84a3a')
    f.mask(f.E(24, 27.5, 1.6, 1.4), '#e8dcb8'); f.px([(23.5, 27.5), (24.5, 27.5)], '#60ff80')
    f.arm((17, 19), (13, 23), (12, 27), 'brown', 'goblin')
    f.staff((12, 45), (11, 5), head='skull', orb=('#208040', '#60ff80', '#d0ffd8'))
    for d in [(-3, -1), (3, 0), (0, -5), (-2, -7), (2, 2)]: f.px([(11 + d[0], 2 + d[1])], '#60ff80', 180)
    f.arm((31, 19), (36, 17), (37, 13), 'brown', 'goblin')
    f.flame((37, 12), ('#208040', '#60ff80', '#d0ffd8'), big=.8)
    goblin_head(f, eye='#80ff60')
    for x, c in ((20, '#c8302a'), (23, '#e8c040'), (26, '#3a7ac8'), (28, '#e8e0c8')):
        f.add(f.C([(x, 6.4), (x + (x - 24) * .4, -1)], .9, .35), [c, c], flat=1)
    f.mask(f.C([(19, 6.6), (29, 6.6)], .6), '#5a3a1a')
    return f

def hobgoblin():
    f = Fig()
    f.legs('wide', pants='pants', boots='boot', cuff=GOLD)
    f.torso('red', wt=7)
    f.add(f.Pp([(17.5, 18), (30.5, 18), (29.5, 28), (18.5, 28)]), 'bronze', bias=.05)   # scale cuirass
    for y in (20, 22.5, 25): 
        for x in range(19, 30, 2): f.px([(x + (y % 2), y)], P['bronze'][1])
    f.belt(29, 'leather'); f.tails('red', 29.5)
    f.pauldron(17.5, 18.4, 'bronze'); f.pauldron(30.5, 18.4, 'bronze')
    f.arm((31, 19.5), (35, 24), (34, 28), 'red', 'hob')
    f.shield((35.5, 29), 'kite', 'red', 'bronze', emblem='skull', emblem_c='#e8dcb8')
    f.arm((17, 19.5), (12.5, 18), (11, 13), 'red', 'hob')
    f.sword((11, 13), (5, 0), w=1.4)
    goblin_head(f, skin='hob', grin=False)
    f.mask(f.C([(21, 15.5), (27, 15.5)], .5), '#2a0808'); f.px([(21, 14.5), (27, 14.5)], '#e8dcb8')
    f.add(f.E(24, 7, 6, 3) & (yy < f.T(0, 8.4)[1]), 'bronze')
    f.add(f.C([(24, 4), (24, 1)], .9), 'red')
    return f

def bugbear():
    f = Fig(k=1.08, w=1.16)
    f.legs('wide', pants='fur', boots='fur')
    for x in (13, 15, 33, 35): f.px([(x, 46)], '#e8dcb8')
    f.torso('fur', wt=7.6, wb=6.6)
    f.add(f.Pp([(19, 20), (29, 20), (28.5, 29), (19.5, 29)]), 'leather', bias=.05)
    f.add(f.C([(17, 18), (31, 29)], 1), 'dleather'); f.px([(22, 21), (26, 25)], '#a0a8b4')
    f.belt(29.4, 'dleather', buckle='#a0a8b4')
    f.arm((31, 19), (36, 24), (36, 29), 'fur', 'fur', hand_r=2.2)
    f.arm((17, 19), (11, 18), (9, 12), 'fur', 'fur', hand_r=2.2)
    # spiked club raised overhead
    f.add(f.C([(9, 14), (6, 2)], 1.3, 2.8), 'wood', bias=.05)
    for d in [(-3, -9), (2, -10), (-2, -6), (3, -7), (0, -12)]: f.px([(8 + d[0], 12 + d[1])], '#b8c0cc')
    DF = ['#0e0804','#1e1208','#32200e','#4a3016','#62421e','#7c5628']
    f.add(f.Pp([(18, 7), (16, 1), (21.5, 5)]) | f.Pp([(30, 7), (32, 1), (26.5, 5)]), DF)
    f.mask(f.Pp([(18.4, 6), (17.2, 3), (20.4, 5.2)]) | f.Pp([(29.6, 6), (30.8, 3), (27.6, 5.2)]), '#4a1a10')
    f.add(f.E(24, 10.5, 6.8, 6.2), DF, soft=1.2)
    f.add(f.Pp([(17.6, 11), (30.4, 11), (29, 19), (24, 21.5), (19, 19)]), DF, bias=-.08)
    f.add(f.E(24, 13, 3.6, 2.6), 'fur', bias=.12)
    f.px([(23, 11.6), (24, 11.4), (25, 11.6)], INK)
    f.mask(f.C([(19.4, 7.4), (22.6, 9)], .55) | f.C([(28.6, 7.4), (25.4, 9)], .55), INK)
    f.px([(21, 9.4), (22, 9.4), (26, 9.4), (27, 9.4)], '#ffb020'); f.px([(22, 9.4), (26, 9.4)], '#400a00')
    f.mask(f.Pp([(20, 14.6), (28, 14.6), (26.8, 18.2), (21.2, 18.2)]), '#2a0606')
    f.px([(20.5, 14.6), (20.5, 15.6), (27.5, 14.6), (27.5, 15.6), (22.5, 14.6), (25.5, 14.6), (22, 18), (26, 18)], '#ece0c0')
    return f

def kobold():
    f = Fig(k=.74)
    f.add(f.C([(27, 33), (35, 38), (40, 34), (41, 28)], 2, .6), 'kobold')     # tail
    f.legs('crouch', pants='kobold', boots=None)
    for x in (15, 17, 31, 33): f.px([(x, 46)], '#e8dcb8')
    f.torso('kobold', wt=6, wb=5.4)
    f.add(f.E(24, 25, 3.6, 5), P['kobold'][2:], bias=.15)
    f.add(f.Pp([(18, 22), (30, 22), (31, 31), (17, 31)]), 'brown', bias=-.05)       # rag tunic
    for x in (18, 21, 25, 28, 30): f.px([(x, 31.5)], P['brown'][1])
    f.arm((17, 19.5), (13, 23), (12, 27), 'kobold', 'kobold')
    f.haft((12.5, 40), (10.5, 3), 'wood', .8); f.spearhead((10.5, 3), (-.05, -1))
    f.add(f.C([(10.8, 7), (12, 8.5)], .9), 'red')
    f.arm((31, 19.5), (35, 22), (35, 26), 'kobold', 'kobold')
    snout_head(f, 'kobold', horns='bone', eye='#ffd040')
    return f

def koboldtrapper():
    f = Fig(k=.74)
    f.add(f.C([(27, 33), (35, 38), (40, 34), (41, 28)], 2, .6), P['kobold'][0:1] + P['kobold'][:5])
    f.legs('crouch', pants='kobold', boots=None)
    f.torso('dleather', wt=6, wb=5.4)
    for y in (21, 24, 27): f.px([(19, y), (20, y), (28, y), (29, y)], '#8a6a3a')     # pouches
    f.belt(29.6, 'leather', buckle=None)
    f.add(f.C([(30, 18), (19, 29)], 1), 'tan')                                     # rope coil strap
    f.add(f.E(30, 27, 3, 2.6) & ~f.E(30, 27, 1.6, 1.3), 'tan')
    f.arm((31, 19.5), (36, 23), (37, 28), 'kobold', 'kobold')
    f.add(f.E(38, 32, 4.2, 2.2), 'steel')                                          # bear trap
    for x in range(34, 43, 2): f.px([(x, 30), (x + 1, 31)], '#d4e2f0')
    f.arm((17, 19.5), (12, 19), (10, 15), 'kobold', 'kobold')
    f.dagger((10, 15), (6, 9))
    snout_head(f, P['kobold'][:1] + P['kobold'][:5], horns='bone', eye='#ffd040')
    f.add(f.E(24, 7.4, 5, 2.4) & (yy < f.T(0, 8.4)[1]), 'green'); f.add(f.C([(28.5, 7.6), (32, 10)], .7, .3), 'green')
    return f

def orcgrunt():
    f = Fig(w=1.1)
    f.legs('wide', pants='pants', boots='boot')
    f.torso('leather', wt=7.4, wb=6.4)
    f.add(f.Pp([(18, 18), (30, 18), (29, 25), (19, 25)]), 'dsteel', bias=.05)         # iron chest plate
    f.px([(20, 20), (28, 20), (20, 23), (28, 23)], '#a0a8b4')
    f.belt(29.4, 'dleather', buckle='#a0a8b4'); f.tails('leather', 30)
    f.pauldron(17, 18.6, 'dsteel', 3.8, 2.8)
    for d in [(-1, -2), (1, -2.6)]: f.px([(17 + d[0], 18.6 + d[1])], '#d4e2f0')
    f.arm((31, 19.5), (35, 24), (34, 28.5), 'orc', 'orc', hand_r=2.1)
    f.shield((35, 29.5), 'round', 'wood', 'dsteel', r=6.2)
    f.mask(f.C([(31, 26), (39, 33)], .7), '#8a2a1a')
    f.arm((17, 19.5), (12, 21), (11, 15), 'orc', 'orc', hand_r=2.1)
    f.haft((11.5, 19), (10, 2)); f.axehead((10, 4), -1)
    orc_head(f)
    f.add(f.E(24, 6.4, 6, 3) & (yy < f.T(0, 8)[1]), 'dsteel'); f.px([(24, 8), (24, 9), (24, 10)], P['dsteel'][3])
    return f

def orcberserker():
    f = Fig(k=1.02, w=1.14)
    f.legs('lunge', pants='brown', boots='fur')
    f.torso('orc', wt=7.6, wb=6.2)
    f.px([(21, 22), (22, 23), (26, 22), (27, 23), (22, 26), (26, 26)], P['orc'][1])
    f.mask(f.C([(18, 20), (22, 27)], .6) | f.C([(30, 20), (26, 27)], .6) | f.C([(24, 18), (24, 22)], .5), '#b02a20')   # war paint
    f.add(f.Pp([(18, 28.6), (30, 28.6), (32, 36), (27, 34), (24, 37), (21, 34), (16, 36)]), 'fur', bias=-.05)
    f.belt(29.2, 'leather', buckle='#e8dcb8')
    # huge greataxe swung back over the shoulder, both hands
    f.arm((17, 19.5), (13, 17), (15, 12), 'orc', 'orc', hand_r=2.1)
    f.arm((31, 19.5), (30, 15), (20, 11), 'orc', 'orc', hand_r=2.1)
    f.haft((24, 13), (8, 6), 'wood', 1.1)
    f.axehead((9, 4), -1, big=True); f.axehead((9, 6), 1, ramp='steel')
    orc_head(f, eye='#ff2010')
    f.hair('red', 'mohawk')
    f.mask(f.C([(20, 9.5), (22, 11.5)], .45), '#b02a20'); f.mask(f.C([(28, 9.5), (26, 11.5)], .45), '#b02a20')
    f.mask(f.Pp([(20.5, 14), (27.5, 14), (26.5, 16.4), (21.5, 16.4)]), '#200606')
    return f

def orcwarchief():
    f = Fig(k=1.1, w=1.16)
    f.cape('red', lining='fur', side='right')
    f.add(f.Pp([(15, 16), (33, 16), (31, 21), (17, 21)]), 'fur', bias=.05)      # fur mantle
    f.legs('wide', pants='dsteel', boots='dsteel')
    f.torso('dsteel', wt=7.6, wb=6.6)
    f.mask(f.E(24, 23, 2.6, 2.6), '#e8dcb8'); f.px([(23, 22.6), (25, 22.6)], INK); f.px([(24, 24)], INK)   # skull boss
    f.belt(29.4, 'leather', buckle=GOLD)
    f.add(f.Pp([(18, 29.4), (30, 29.4), (31, 36), (24, 34), (17, 36)]), 'red', bias=-.08)
    for x, s in ((16.5, -1), (31.5, 1)):
        f.add(f.E(x, 18, 4, 3), 'dsteel', bias=.1)
        for j in range(3): f.add(f.Pp([(x - 1.5 + j * 1.5, 16), (x - 1 + j * 1.5 + s, 12), (x + j * 1.5, 16)]), 'bone', bias=.1)
    f.arm((31, 19.5), (36, 24), (37, 29), 'dsteel', 'orc', hand_r=2.2)
    f.arm((17, 19.5), (12, 22), (11, 27), 'dsteel', 'orc', hand_r=2.2)
    f.haft((11.5, 44), (10, 6), 'wood', 1.1); f.axehead((10, 6), -1, big=True, ramp='dsteel'); f.axehead((10, 6), 1, ramp='dsteel')
    f.add(f.C([(10, 6), (10, 1)], .8), 'dsteel')
    orc_head(f, skin=P['orc'][:1] + P['orc'][:5], eye='#ff2010')
    for x in (19, 21.5, 24, 26.5, 29):
        f.add(f.C([(x, 7), (x + (x - 24) * .35, 1.5 if x == 24 else 3)], 1, .35), 'bone', bias=.12)
    f.mask(f.C([(18.6, 7), (29.4, 7)], .7), GOLD)
    f.px([(19, 12), (20, 13), (20, 14)], '#e8dcb8')    # scar
    return f

def gnoll():
    f = Fig(k=1.04)
    f.legs('lunge', pants='gnoll', boots=None)
    for x in (12, 14, 27, 29): f.px([(x, 46)], '#e8dcb8')
    f.torso('gnoll', wt=6.8, wb=5.8)
    for p in [(20, 20), (27, 21), (22, 25), (29, 26), (19, 27), (25, 28)]: f.px([p], P['gnoll'][1])   # spots
    f.add(f.C([(17, 18), (30, 29)], 1.2), 'leather'); f.px([(21, 21.5), (24, 24), (27, 26.5)], '#e8dcb8')   # bone bandolier
    f.add(f.Pp([(18, 29), (30, 29), (31, 35), (24, 33), (17, 35)]), 'leather', bias=-.05)
    f.arm((31, 19.5), (36, 22), (39, 19), 'gnoll', 'gnoll')
    for d in [(1, -2), (2, -1), (2, 1)]: f.px([(39 + d[0], 19 + d[1])], '#e8dcb8')
    f.arm((17, 19.5), (12, 23), (11, 27), 'gnoll', 'gnoll')
    f.haft((12, 44), (9, 2)); f.spearhead((9, 2), (-.1, -1)); f.add(f.C([(9.3, 6), (7, 8), (8, 10)], .6), 'red')
    for i, x in enumerate(range(17, 32, 2)):
        f.add(f.Pp([(x - 1.2, 9), (x + (x - 24) * .25, 2.5 + abs(24 - x) * .25), (x + 1.2, 9)]), 'fur', bias=-.05)
    f.add(f.E(19, 5.6, 2.4, 3) | f.E(29, 5.6, 2.4, 3), 'gnoll'); f.mask(f.E(19, 5.8, 1.2, 1.8) | f.E(29, 5.8, 1.2, 1.8), '#3a2010')
    f.add(f.E(24, 10.4, 5.4, 4.8), 'gnoll', soft=1.2)
    f.add(f.E(24, 14.4, 4, 3.2), 'gnoll', bias=.1)
    f.add(f.E(24, 12.4, 1.8, 1.2), ['#0a0605', '#1a0e08', '#2e1c10'])
    f.mask(f.Pp([(19.6, 15), (28.4, 15), (27, 18), (21, 18)]), '#2a0606')
    f.px([(20, 15), (22, 15), (24, 15), (26, 15), (28, 15), (21, 18), (23, 18), (25, 18), (27, 18)], '#ece0c0')
    f.px([(20.5, 9.6), (21.5, 9.6), (26.5, 9.6), (27.5, 9.6)], '#ffc93c'); f.px([(21.5, 9.6), (26.5, 9.6)], INK)
    f.mask(f.C([(19.6, 8.2), (22.4, 9)], .45) | f.C([(28.4, 8.2), (25.6, 9)], .45), INK)
    for p in [(21, 12), (27, 12.5), (22.5, 7.6)]: f.px([p], P['gnoll'][1])
    return f

def lizardfolk():
    f = Fig()
    f.add(f.C([(28, 32), (37, 39), (42, 36), (44, 30)], 2.4, .6), 'lizard')
    f.legs('wide', pants='lizard', boots=None)
    for x in (13, 15, 32, 34): f.px([(x, 46)], '#e8dcb8')
    f.torso('lizard', wt=6.8, wb=5.8)
    f.add(f.E(24, 25, 3.6, 5.4), ['#3a4a1a', '#5a6a2a', '#7e8c3e', '#a0ac58'], bias=.1)
    for y in (22, 25, 28): f.mask(f.C([(21, y), (27, y)], .3), '#5a6a2a')
    f.add(f.Pp([(18, 29), (30, 29), (31, 36), (24, 33), (17, 36)]), 'leather', bias=-.05)
    f.belt(29.4, 'leather', buckle='#e8dcb8')
    f.arm((31, 19.5), (35, 24), (34, 28), 'lizard', 'lizard')
    f.shield((35.5, 29), 'round', 'wood', 'bone', r=6)
    f.mask(f.C([(35.5, 24), (35.5, 34)], .6) | f.C([(30.5, 29), (40.5, 29)], .6), '#e8dcb8')
    f.arm((17, 19.5), (12, 21), (10, 16), 'lizard', 'lizard')
    f.haft((11, 22), (8, 1), 'wood', .8)
    for dx in (-2, 0, 2): f.add(f.C([(8 + dx, 1), (8 + dx * 1.2, -4)], .6, .3), 'bone', bias=.1)
    f.add(f.C([(5, 1), (11, 1)], .6), 'bone')
    snout_head(f, 'lizard', eye='#ffe040', snout=(3.2, 4.2), crest='red')
    f.px([(21.5, 10.4), (26.5, 10.4)], INK)
    return f

def troglodyte():
    f = Fig(k=.96, w=1.12)
    f.legs('crouch', pants='trog', boots=None)
    for x in (14, 16, 30, 32): f.px([(x, 46)], '#e8dcb8')
    f.torso('trog', wt=7.4, wb=6.2, top=19)
    f.px([(20, 23), (27, 22), (22, 27), (28, 26), (24, 24)], P['trog'][1])
    f.add(f.Pp([(18, 29), (30, 29), (30, 34), (18, 34)]), 'brown', bias=-.05)
    f.arm((17, 21), (12, 26), (10, 31), 'trog', 'trog', hand_r=2.2)
    f.add(f.C([(10, 33), (8, 22)], 1.2, 2.6), 'stone' if 'stone' in P else 'gray', bias=.05)
    for d in [(-2, -9), (1, -10), (-1, -6)]: f.px([(9 + d[0], 30 + d[1])], '#b8c0cc')
    f.arm((31, 21), (36, 25), (37, 30), 'trog', 'trog', hand_r=2.2)
    # hunched head with a ridge crest, bulging eyes and a wide maw
    f.add(f.Pp([(20, 8), (24, 2), (28, 8)]), 'trog', bias=-.08)
    f.add(f.E(24, 12, 6.4, 5.4), 'trog', soft=1.2)
    f.mask(f.E(20.5, 10.6, 1.6, 1.4) | f.E(27.5, 10.6, 1.6, 1.4), '#e8f0a0'); f.px([(21, 10.6), (27, 10.6)], INK)
    f.mask(f.Pp([(18.5, 14), (29.5, 14), (28, 17), (20, 17)]), '#200608')
    f.px([(19, 14), (21, 14), (23, 14), (25, 14), (27, 14), (29, 14), (20, 17), (24, 17), (28, 17)], '#d8d0b8')
    for d in [(-6, -3), (6, -2), (-5, 4), (7, 3)]: f.px([(24 + d[0], 12 + d[1])], '#9aa860', 160)   # stink
    return f

FOLK2 = {'goblinarcher': goblinarcher, 'goblinshaman': goblinshaman, 'hobgoblin': hobgoblin, 'bugbear': bugbear, 'kobold': kobold,
         'koboldtrapper': koboldtrapper, 'orcgrunt': orcgrunt, 'orcberserker': orcberserker, 'orcwarchief': orcwarchief,
         'gnoll': gnoll, 'lizardfolk': lizardfolk, 'troglodyte': troglodyte}

if __name__ == '__main__':
    imgs = [f().render() for f in FOLK2.values()]
    sheet(imgs, scale=5, cols=4).save('folk2.png')
