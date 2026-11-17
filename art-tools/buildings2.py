from hk import *
import base64, io, json

PLASTER = ['#3a3428', '#6a5e48', '#a8987a', '#cdbf9e', '#e6dcbf']
BEAM = ['#120a06', '#24160c', '#3a2414', '#52341c']
THATCH = ['#2a1e0a', '#4e3a14', '#7a5a1e', '#a07a2c', '#c49a40']
STONE = ['#1a1a20', '#2e2e36', '#46464f', '#605f68', '#7c7a82', '#9a98a0']
MARBLE = ['#4a4a52', '#7a7a84', '#a8a8b2', '#cfcfd6', '#ececf0']
WARM = ['#3a2008', '#8a5010', '#e09a30', '#ffd070', '#fff0b0']
SLATE = ['#10141c', '#1c2230', '#2a3346', '#3a465e', '#4c5a76']

def window(f, x, y, w=4, h=4, glow=True, cross=True):
    f.add(f.Pp([(x, y), (x + w, y), (x + w, y + h), (x, y + h)]), WARM if glow else SLATE, flat=3 if glow else 1)
    f.mask(f.C([(x - .4, y - .2), (x + w + .4, y - .2)], .45) | f.C([(x - .4, y + h + .2), (x + w + .4, y + h + .2)], .45), BEAM[0])
    if cross: f.mask(f.C([(x + w / 2, y), (x + w / 2, y + h)], .3) | f.C([(x, y + h / 2), (x + w, y + h / 2)], .3), BEAM[1])

def door(f, x, y, w=6, h=9, arch=True, ramp='wood'):
    pts = [(x, y + h), (x + w, y + h), (x + w, y + 2), (x + w / 2, y), (x, y + 2)] if arch else [(x, y + h), (x + w, y + h), (x + w, y), (x, y)]
    f.add(f.Pp(pts), ramp, bias=-.1)
    f.mask(f.C([(x + w / 2, y + 1), (x + w / 2, y + h)], .3), '#140a04')
    f.px([(x + w - 1.5, y + h * .6)], GOLD)

def barrel(f, x, y):
    f.add(f.E(x, y, 2.6, 3.2), 'wood', bias=.05); f.mask(f.C([(x - 2.4, y - 1.2), (x + 2.4, y - 1.2)], .3) | f.C([(x - 2.4, y + 1.4), (x + 2.4, y + 1.4)], .3), '#4a4a52')

def crate(f, x, y, s=4):
    f.add(f.Pp([(x, y), (x + s, y), (x + s, y + s), (x, y + s)]), 'wood', bias=.1); f.mask(f.C([(x, y), (x + s, y + s)], .3), BEAM[1])

def lantern(f, x, y):
    f.add(f.Pp([(x - 1, y), (x + 1, y), (x + 1, y + 2), (x - 1, y + 2)]), WARM, flat=4); f.px([(x, y - 1)], '#14141a')

def shop():
    f = Fig()
    f.add(f.Pp([(6, 46), (42, 46), (42, 20), (6, 20)]), PLASTER, soft=.6)                          # walls
    for x in (6, 15, 33, 42): f.mask(f.C([(x, 20), (x, 46)], .6), BEAM[1])                       # timber frame
    f.mask(f.C([(6, 20), (42, 20)], .6) | f.C([(6, 31), (42, 31)], .6), BEAM[1])
    f.mask(f.C([(6, 20), (15, 31)], .45) | f.C([(42, 20), (33, 31)], .45), BEAM[2])
    f.add(f.Pp([(3, 21), (24, 4), (45, 21)]), ['#2a0a08', '#5a1610', '#8a2418', '#b0361f', '#cc4a2c'], soft=1)   # roof
    for y in (9, 13, 17): f.mask(f.C([(24 - (y - 4) * 1.2, y), (24 + (y - 4) * 1.2, y)], .3), '#3a0c08')
    window(f, 20.5, 22, 7, 6)                                                                  # upper window
    f.add(f.Pp([(7, 33), (25, 33), (24, 36), (8, 36)]), ['#e8e0d0'], flat=0)                   # striped awning
    for x in range(8, 25, 4): f.add(f.Pp([(x, 33), (x + 2, 33), (x + 2, 36), (x, 36)]), ['#c8303a'], flat=0)
    f.add(f.Pp([(9, 37), (23, 37), (23, 44), (9, 44)]), WARM, flat=3)                          # shop window full of goods
    for (x, c) in ((11, '#d8423a'), (14, '#3a7ac8'), (17, '#e8c040'), (20, '#6ad27c')): f.mask(f.E(x, 42, 1.2, 1.6), c)
    f.mask(f.C([(13, 38), (19, 41)], .4), '#c8d0dc')
    door(f, 30, 36, 7, 10)
    f.add(f.C([(37, 30), (41, 30)], .4), 'dsteel'); f.add(f.Pp([(38, 30.5), (44, 30.5), (44, 35), (38, 35)]), 'wood', bias=.1)  # hanging sign
    f.mask(f.E(41, 33, 1.6, 1.4), GOLD)
    crate(f, 2, 42); barrel(f, 45, 43)
    lantern(f, 28.5, 34)
    return f

def tavern():
    f = Fig()
    f.add(f.Pp([(3, 46), (45, 46), (45, 22), (3, 22)]), ['#2a1a0c', '#4a2e16', '#6a4422', '#8a5a30', '#a6703e'], soft=.6)   # log walls
    for y in range(24, 46, 3): f.mask(f.C([(3, y), (45, y)], .3), '#24160a')
    f.add(f.Pp([(0, 23), (24, 5), (48, 23)]), THATCH, soft=1.2, dither=True)                     # thatched roof
    f.mask(f.C([(0, 23), (48, 23)], .6), '#2a1e0a')
    f.add(f.Pp([(33, 4), (38, 4), (38, 14), (33, 14)]), STONE, bias=.05)                         # chimney
    window(f, 7, 26, 6, 5); window(f, 35, 26, 6, 5); window(f, 7, 35, 6, 5); window(f, 35, 35, 6, 5)
    window(f, 21.5, 14, 5, 4)
    door(f, 20, 33, 8, 13)
    lantern(f, 18, 32); lantern(f, 30, 32)
    f.add(f.C([(24, 24), (24, 28)], .3), 'dsteel')                                             # hanging mug sign
    f.add(f.Pp([(21, 28), (27, 28), (27, 31.5), (21, 31.5)]), 'wood', bias=.1)
    f.add(f.Pp([(22.6, 28.6), (25, 28.6), (25, 31), (22.6, 31)]), 'gold', flat=3); f.px([(22.8, 28.2), (24, 28)], '#ffffff')
    barrel(f, 4, 43); barrel(f, 9, 44); barrel(f, 6.5, 39.5)
    f.add(f.Pp([(34, 43), (44, 43), (44, 44.5), (34, 44.5)]), 'wood')                          # bench
    return f

def guild():
    f = Fig()
    f.add(f.Pp([(8, 46), (40, 46), (40, 12), (8, 12)]), STONE, soft=.8)                           # keep
    for x in range(8, 41, 4): f.add(f.Pp([(x, 8), (x + 2.4, 8), (x + 2.4, 12), (x, 12)]), STONE, bias=.05)   # crenellations
    for y in range(15, 46, 4):
        for x in range(9 + (y % 8 == 3) * 2, 40, 4): f.px([(x, y)], STONE[1])
    for x in (11, 33):                                                                          # long banners
        f.add(f.Pp([(x, 14), (x + 5, 14), (x + 5, 34), (x + 2.5, 31), (x, 34)]), 'royal', soft=.6)
        f.mask(f.E(x + 2.5, 20, 1.6, 1.6), GOLD); f.mask(f.C([(x + 2.5, 23), (x + 2.5, 28)], .4), GOLD)
    f.add(f.Pp([(18, 46), (30, 46), (30, 32), (24, 27), (18, 32)]), ['#0a0806', '#140e0a', '#24180e', '#3a2614'], bias=-.1)   # great door
    f.mask(f.C([(24, 28), (24, 46)], .35), '#0a0604'); f.px([(22.5, 38), (25.5, 38)], GOLD)
    f.add(f.Pp([(16, 46), (32, 46), (31, 44), (17, 44)]), STONE, bias=.15)                       # steps
    window(f, 21.5, 15, 5, 7, cross=True)
    for x in (16, 32): f.add(f.C([(x, 28), (x, 24)], .5), 'dsteel'); f.flame((x, 23), big=.5)
    f.add(f.C([(24, 8), (24, -1)], .4), 'wood'); f.add(f.Pp([(24, -1), (32, 1), (24, 3.5)]), 'royal'); f.px([(27, 1)], GOLD)
    return f

def yard():
    f = Fig()
    f.add(f.Pp([(2, 26), (46, 26), (46, 46), (2, 46)]), ['#4a3a1e', '#6a5428', '#8a7036', '#a68a48'], dither=True, noise=.4, soft=.4)   # packed sand
    f.add(f.Pp([(30, 8), (46, 8), (46, 22), (30, 22)]), ['#2a1a0c', '#4a2e16', '#6a4422', '#8a5a30'], bias=.05)   # shed
    f.add(f.Pp([(28, 9), (38, 2), (48, 9)]), SLATE, bias=.05)
    for i, x in enumerate((32, 35, 38, 41, 44)): f.add(f.C([(x, 21), (x - .4, 11)], .5), 'steel' if i % 2 else 'wood', bias=.15)   # weapon rack
    f.mask(f.C([(31, 14), (45, 14)], .5), BEAM[1])
    for x0 in (6, 18):                                                                            # straw dummies
        f.add(f.C([(x0, 44), (x0, 24)], .9), 'wood'); f.add(f.C([(x0 - 6, 29), (x0 + 6, 29)], 1.1), 'wood')
        f.add(f.E(x0, 32, 4.4, 5.6), THATCH, dither=True); f.add(f.E(x0, 22, 3, 3.2), THATCH)
        f.mask(f.E(x0, 32, 1.6, 1.6) & ~f.E(x0, 32, .7, .7), '#b02a20')
    f.mask(f.C([(4, 33), (8, 31)], .3), '#2a1a0c')
    f.add(f.E(36, 36, 6, 6.4), ['#e8e0d0'], flat=0); f.mask(f.E(36, 36, 4.4, 4.8) & ~f.E(36, 36, 3, 3.3), '#c8303a'); f.mask(f.E(36, 36, 1.4, 1.4), '#c8303a')   # archery target
    for (x, y) in ((35, 34), (38, 37), (34, 38)): f.mask(f.C([(x, y), (x + 3, y - 2)], .3), '#3a2a14'); f.px([(x + 3, y - 2.4)], '#e8e0d0')
    f.add(f.C([(36, 42), (36, 46)], .8), 'wood')
    for x in range(1, 48, 5): f.add(f.C([(x, 46), (x, 41)], .7), 'wood')                         # low fence
    f.mask(f.C([(1, 43), (47, 43)], .4), P['wood'][2])
    return f

def temple():
    f = Fig()
    f.add(f.Pp([(8, 46), (40, 46), (40, 22), (8, 22)]), MARBLE, soft=.8)
    f.add(f.Pp([(5, 23), (24, 13), (43, 23)]), ['#0c1a3a', '#162a5a', '#22407e', '#2e56a0', '#4070c0'], soft=1)
    f.add(f.Pp([(19, 22), (29, 22), (29, 8), (19, 8)]), MARBLE, bias=.05)                          # bell tower
    f.add(f.Pp([(17.5, 9), (24, 0), (30.5, 9)]), ['#0c1a3a', '#162a5a', '#22407e', '#2e56a0'], bias=.05)
    f.mask(f.C([(24, -2), (24, 2)], .45) | f.C([(22.6, -.6), (25.4, -.6)], .45), GOLD)
    f.add(f.E(24, 13.5, 2.2, 2.4) & (yy > f.T(0, 11.5)[1]), ['#4a3a10', '#a07820', '#e0b040'], flat=2)   # bell
    f.add(f.E(24, 29, 5, 5), ['#1a0a2a'], flat=0)                                                     # rose window
    for i, c in enumerate(['#d83a4a', '#3a7ad8', '#e8c040', '#6ad27c', '#c070ff', '#d83a4a', '#3a7ad8', '#e8c040']):
        import math
        a = i / 8 * 6.283; f.mask(f.E(24 + 3 * math.cos(a), 29 + 3 * math.sin(a), 1.1, 1.1), c)
    f.mask(f.E(24, 29, 1.2, 1.2), '#fff4c0')
    for x in (11, 35): window(f, x - 1.5, 26, 3, 7, glow=True, cross=False)
    door(f, 20.5, 37, 7, 9, ramp='wood')
    f.add(f.Pp([(14, 46), (34, 46), (33, 44.4), (15, 44.4)]), MARBLE, bias=.15)
    for x in (16, 32): f.add(f.C([(x, 44), (x, 40.5)], .6), ['#e8e0c8']); f.flame((x, 40), ('#ff9a30', '#ffd060', '#fff4c0'), big=.4)
    return f

def apothecary():
    f = Fig()
    f.add(f.Pp([(9, 46), (39, 46), (37, 18), (11, 18)]), ['#1e2a18', '#34462a', '#4e663c', '#6a8450', '#86a066'], soft=.7)   # crooked mossy walls
    f.add(f.Pp([(6, 19), (19, 2), (26, 6), (42, 19)]), ['#1a0a24', '#2e1240', '#46205e', '#5e2e7c', '#7a40a0'], soft=1)       # leaning roof
    f.add(f.Pp([(14, 7), (18, 7), (18, 14), (14, 14)]), STONE)
    for p in [(16, 5), (15, 3), (17, 1)]: f.px([p], '#7af0a0', 170)                                # green smoke
    window(f, 13, 22, 7, 6); window(f, 28, 22, 7, 6)
    for (x, c) in ((15, '#4ad07a'), (17.5, '#c070ff'), (30, '#ff6a5a'), (33, '#4ad07a')): f.mask(f.E(x, 26.4, .9, 1.3), c)
    door(f, 20.5, 34, 7, 12)
    for (x, y) in ((11, 31), (13, 30), (37, 31), (35, 30)): f.mask(f.C([(x, y), (x, y + 3)], .35), '#6a8a3a')   # drying herbs
    f.mask(f.C([(10, 30), (14, 30)], .3) | f.C([(34, 30), (38, 30)], .3), BEAM[1])
    f.add(f.E(5, 42, 4.4, 3.4), 'dsteel', bias=.05); f.mask(f.E(5, 39.6, 3.6, 1.2), '#4ad07a')        # bubbling cauldron
    for p in [(4, 37), (6, 36), (5, 34)]: f.px([p], '#9affc0', 200)
    for x in (40, 44): f.add(f.Pp([(x - 1.6, 46), (x + 1.6, 46), (x + 1.2, 42), (x - 1.2, 42)]), 'red', bias=.05); f.add(f.E(x, 40.4, 2, 1.8), 'forest', bias=.1)   # herb pots
    f.add(f.E(31, 15, 2.6, 1.4), 'red', bias=.1); f.px([(30, 14.6), (32, 15)], '#f0e0d0'); f.add(f.C([(31, 16), (31, 18)], .6), ['#e8e0c8'])   # toadstool sign
    return f

def smithy():
    f = Fig()
    f.add(f.Pp([(4, 46), (44, 46), (44, 20), (4, 20)]), STONE, soft=.6)
    f.add(f.Pp([(2, 21), (46, 21), (40, 13), (8, 13)]), SLATE, bias=.05)
    f.add(f.Pp([(34, 0), (41, 0), (41, 14), (34, 14)]), STONE, bias=.05)
    f.px([(37, -1), (38, -3), (36, -4)], '#8a8a90', 160)
    f.add(f.Pp([(8, 46), (28, 46), (28, 25), (8, 25)]), ['#0a0604', '#140a06', '#200e08'], flat=1, ao=False)   # open forge front
    f.add(f.E(18, 40, 7, 4), ['#3a0a04', '#a02a08', '#ff6a10', '#ffb040', '#fff0a0'], soft=1.6)         # glowing coals
    f.flame((18, 38), big=1.1)
    f.mask(f.C([(8, 25), (28, 25)], .6), BEAM[1])
    for i, x in enumerate((10, 12.5, 15)): f.add(f.C([(x, 34), (x, 27)], .45), 'steel', bias=.2)      # tools on the wall
    f.add(f.Pp([(30, 38), (42, 38), (40, 41), (37, 41), (37, 46), (35, 46), (35, 41), (32, 41)]), 'dsteel', bias=.15)   # anvil
    f.add(f.Pp([(33, 36.5), (38, 35.5), (38.6, 37.6), (33.4, 38)]), ['#a02a08', '#ff6a10', '#ffb040'], flat=1)     # hot blade
    f.add(f.C([(39, 30), (43, 35)], .6), 'wood'); f.add(f.Pp([(37, 28.5), (41, 28.5), (41, 31.5), (37, 31.5)]), 'steel')   # hammer
    barrel(f, 45, 43); f.mask(f.E(45, 40.6, 2, .7), '#3a7ac8')
    for p in [(22, 33), (16, 31), (20, 30), (25, 34)]: f.px([p], '#ffb040', 210)
    return f

def bank():
    f = Fig()
    f.add(f.Pp([(5, 46), (43, 46), (43, 22), (5, 22)]), MARBLE, soft=.8)
    f.add(f.Pp([(2, 23), (24, 9), (46, 23)]), MARBLE, bias=.1)                                      # pediment
    f.mask(f.C([(2, 23), (46, 23)], .7), GOLD)
    f.mask(f.E(24, 18, 3, 3), GOLD); f.mask(f.E(24, 18, 1.8, 1.8), '#9c6c10'); f.px([(24, 17), (24, 19)], GOLD)
    for x in (9, 15, 33, 39): f.add(f.Pp([(x - 1.8, 44), (x + 1.8, 44), (x + 1.8, 25), (x - 1.8, 25)]), MARBLE, bias=.15); f.mask(f.C([(x, 26), (x, 43)], .25), MARBLE[1])
    f.add(f.Pp([(19, 44), (29, 44), (29, 30), (24, 27), (19, 30)]), ['#2a2a30', '#46464f', '#6a6a74', '#8a8a96'], bias=.05)   # vault door
    f.mask(f.E(24, 36, 3.6, 3.6) & ~f.E(24, 36, 2.6, 2.6), GOLD); f.mask(f.C([(24, 32.5), (24, 39.5)], .3) | f.C([(20.5, 36), (27.5, 36)], .3), GOLD)
    for y in (31, 41): f.mask(f.C([(19.5, y), (28.5, y)], .4), '#2a2a30')
    f.add(f.Pp([(3, 46), (45, 46), (44, 44), (4, 44)]), MARBLE, bias=.15)
    for (x, y) in ((5, 42), (43, 42)): f.mask(f.E(x, y, 1.6, 1), GOLD)
    return f

def cartographer():
    f = Fig()
    f.add(f.Pp([(12, 46), (36, 46), (34, 14), (14, 14)]), ['#2a1e14', '#4a3624', '#6a5034', '#8a6a46', '#a6845a'], soft=.8)   # tall tower
    f.add(f.E(24, 14, 12, 9) & (yy < f.T(0, 15)[1]), ['#1a0e2a', '#2e1a4a', '#46286a', '#5e388a', '#7a4cac'], soft=1.4)     # observatory dome
    f.mask(f.C([(24, 5), (24, 14)], .5), '#120a1c')
    f.add(f.C([(26, 9), (37, 2)], 1.1, .8), 'bronze', bias=.1); f.mask(f.E(37.5, 1.6, 1, 1), '#c8e0ff')                        # telescope
    for (x, y) in ((10, 4), (16, 2), (42, 8), (5, 12)): f.px([(x, y)], '#fff4c0', 200)
    window(f, 21, 18, 6, 5)
    f.add(f.E(24, 29, 4.6, 4.6), ['#5a4a30', '#a08a60', '#e0d0a8'], flat=2)                         # compass rose
    f.mask(f.C([(24, 25), (24, 33)], .35) | f.C([(20, 29), (28, 29)], .35), '#3a2a14'); f.px([(24, 25.6)], '#c8303a')
    door(f, 20.5, 36, 7, 10)
    f.add(f.Pp([(37, 32), (46, 32), (46, 46), (37, 46)]), 'wood', bias=.05)                            # scroll rack
    for y in (34.5, 38.5, 42.5):
        for x in (39, 42, 45): f.add(f.E(x, y, 1.2, 1.2), PLASTER, bias=.1)
    f.add(f.Pp([(2, 40), (10, 39), (11, 46), (3, 46)]), ['#5a4a30', '#8a7650', '#c0a878'], flat=2)       # map on an easel
    f.mask(f.C([(4, 44), (6, 41), (9, 43)], .3), '#b02a20')
    return f

def square():
    f = Fig()
    f.add(f.E(24, 40, 20, 6.4), STONE, soft=1, bias=-.05)
    f.add(f.E(24, 39.4, 15.6, 4.6), ['#081a30', '#103460', '#1e5a90', '#3a86c0', '#7ac0e8'], soft=1.2)
    f.mask(f.E(24, 40, 20, 6.4) & ~f.E(24, 40, 18.6, 5.4), STONE[4])
    f.add(f.Pp([(21, 38), (27, 38), (26, 26), (22, 26)]), STONE, bias=.1)                             # pedestal
    f.add(f.E(24, 26, 6, 1.8), STONE, bias=.1)
    f.add(f.E(24, 20, 2.4, 2.6), 'bronze', bias=.1); f.add(f.Pp([(21.5, 22), (26.5, 22), (27, 25.4), (21, 25.4)]), 'bronze')   # statue
    f.add(f.C([(26.5, 22), (30, 16)], .7), 'bronze'); f.mask(f.E(30.4, 14.6, 1.6, 1.6), '#ffd060'); f.px([(30, 14)], '#fff4c0')   # raised torch
    for (a, b) in (((22, 27), (13, 37)), ((26, 27), (35, 37))): f.mask(f.C([a, ((a[0] + b[0]) / 2, a[1] - 3), b], .45), '#a8e0ff', 230)   # water arcs
    for p in [(16, 39), (31, 40), (24, 42), (19, 41)]: f.px([p], GOLD)                                # coins in the water
    for x in (3, 45): f.add(f.Pp([(x - 2.4, 46), (x + 2.4, 46), (x + 2, 42), (x - 2, 42)]), STONE, bias=.05); f.add(f.E(x, 40.6, 3, 2.4), 'forest', bias=.05)
    return f

B = {'shop': shop, 'tavern': tavern, 'guild': guild, 'yard': yard, 'temple': temple, 'apothecary': apothecary, 'smithy': smithy, 'bank': bank, 'cartographer': cartographer, 'square': square}
if __name__ == '__main__':
    imgs = {k: fn().render() for k, fn in B.items()}
    sheet(list(imgs.values()), scale=5, cols=5).save('buildings2.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('buildings2.json', 'w'))
