from monsters import *

def ant():
    s = Sprite('#0c0605')
    s.add(ellipse(24, 11, 9, 7), R['chitin_d'], dither=True)
    for y in (9, 12):
        s.maskpx(ellipse(24, y, 8, 1) & ellipse(24, 11, 8.5, 6.5), '#2c100c')
    s.add(mir(chain([(19, 21), (11, 14), (4, 20), (2, 30)], 1.2, 0.6)), R['chitin_d'])
    s.add(mir(chain([(19, 23), (10, 24), (6, 36), (5, 45)], 1.3, 0.6)), R['chitin_d'])
    s.add(ellipse(24, 20, 5.5, 4.5), R['chitin'])
    s.add(mir(chain([(19, 27), (13, 33), (14, 40), (12, 46)], 1.4, 0.6)), R['chitin'])
    s.add(mir(chain([(21, 23), (17, 13), (11, 6), (7, 6)], 0.9, 0.5)), R['chitin_d'], bias=0.1)
    head = ellipse(24, 29, 10.5, 8) | ellipse(24, 24, 7, 5)
    s.add(head, R['chitin'], soft=1.4)
    s.add(mir(chain([(19, 35), (16, 39), (17, 43), (21, 45), (24, 44)], 1.9, 0.5)), R['chitin_d'], bias=0.15)
    for (x, y) in [(17, 40), (18, 43)]:
        s.pxm([(x + 1, y)], '#140807')
    s.add(mir(ellipse(16, 28, 3, 3.6)), ['#060303', '#100606', '#1f0b0a', '#3a1611'], lo=-0.7)
    s.pxm([(15, 26), (16, 26)], '#d89c80')
    s.pxm([(15, 27)], '#8a4a3a')
    s.pxm([(22, 24), (21, 25)], '#d4845a')
    s.px([(23, 31), (24, 31), (25, 31)], '#3d1610')
    return s

def rat():
    s = Sprite('#090706')
    FL = ['#24181a', '#3a272a', '#563a3c', '#704e4e', '#8a6460']
    s.add(chain([(33, 38), (41, 37), (45, 30), (44, 22), (40, 18)], 1.3, 0.5), FL)
    s.add(ellipse(24, 28, 14, 11) | ellipse(24, 22, 9, 7), R['fur_d'], dither=True, noise=0.35)
    for x0 in range(13, 36, 3):
        s.px([(x0, 19 + abs(24 - x0) // 3), (x0 + 1, 20 + abs(24 - x0) // 3)], '#5a4e47')
    s.pxm([(23, 17), (22, 18), (23, 19)], '#433a35')
    s.add(mir(ellipse(16.5, 26, 3.2, 3.6, -25)), R['fur_d'])
    s.add(mir(ellipse(16.8, 26.3, 1.7, 2.2, -25)), FL[:3], bias=-0.2)
    s.erase |= mir(rect(13, 23, 14.5, 24.5))
    s.add(mir(chain([(17, 33), (15, 39), (16, 44)], 2.2, 1.4)), R['fur_d'])
    for k in range(3):
        s.pxm([(13 + k * 2, 45), (13 + k * 2, 46)], '#cfc6b4')
    s.add(ellipse(24, 32, 7, 6) | ellipse(24, 37, 4.5, 4.5) | ellipse(24, 40, 2.6, 2.4), R['fur'], soft=1.4, dither=True)
    s.add(ellipse(24, 41.3, 1.8, 1.2), FL)
    s.pxm([(20, 31), (21, 31)], EYE_R)
    s.pxm([(21, 30)], '#ffc0b0')
    s.maskpx(mir(chain([(21, 32), (19, 33)], 0.4)), '#171413')
    s.px([(23, 43), (24, 43), (23, 44), (24, 44), (23, 45), (24, 45)], '#cdb46c')
    s.px([(24, 44), (24, 45)], '#8f7a3a')
    s.pxm([(19, 40), (17, 40), (15, 41)], '#968779', 170)
    s.pxm([(20, 42), (18, 43)], '#968779', 170)
    s.px([(29, 24), (30, 25), (31, 26)], '#5a2a2a')
    return s

def sporeling():
    s = Sprite('#0a0605')
    ST = ['#1c1814', '#352e26', '#524738', '#71644f', '#918268', '#ac9e82']
    s.add(chain([(18, 42), (12, 46)], 1.4, 0.6) | chain([(30, 42), (37, 46)], 1.4, 0.6) | chain([(24, 43), (23, 47)], 1.3, 0.6), ST)
    s.add(mir(chain([(17, 25), (12, 33), (10, 41), (8, 44)], 2.0, 0.8)), ST, bias=-0.1)
    s.add(ellipse(24, 33, 8, 12) | ellipse(24, 26, 6, 5), ST, dither=True, noise=0.3)
    for x in (21, 24, 27):
        s.maskpx(chain([(x, 30), (x + (x - 24) * 0.3, 43)], 0.4), '#352e26')
    s.add(ellipse(24, 20, 17, 4.5) & (yy > 18), ['#2a221b', '#43382b', '#5c4c3a'], flat=1)
    for x in range(9, 40, 2):
        s.px([(x, 19), (x, 20), (x, 21)], '#1c1611')
    cap = (ellipse(24, 15, 18, 10) & (yy < 20)) | ellipse(7, 20, 2.5, 3) | ellipse(41, 20, 2.5, 3)
    s.add(cap, R['cap'], dither=True, soft=1.8, bias=-0.08)
    s.erase |= (yy > 19.5) & ((xx < 6) | (xx > 42)) & (NOISE > 0.4)
    for (x, y, r) in [(15, 11, 1.4), (30, 8, 1.1), (34, 14, 1.5), (21, 13, 0.9)]:
        s.maskpx(ellipse(x, y, r, r * 0.8), '#9a8a70')
    s.maskpx(mir(ellipse(20.5, 27, 1.8, 2.2)), '#070504')
    s.pxm([(20, 28)], '#9fd06a')
    s.maskpx(ellipse(24, 33, 1.1, 3), '#070504')
    for (x, y) in [(6, 28), (42, 25), (38, 33), (9, 36), (44, 40), (4, 12)]:
        s.px([(x, y)], '#b8d080', 200)
    return s

def wolf():
    s = Sprite('#070609')
    F = R['wolf']
    s.add(ellipse(24, 38, 15, 9), F, dither=True, noise=0.25)
    s.add(mir(chain([(16, 39), (15, 46)], 2.5, 2.0)), F)
    s.pxm([(13, 46), (15, 46), (17, 46)], '#cfc8b8')
    mane = poly([(24, 14), (33, 18), (38, 22), (35, 25), (40, 29), (35, 31), (37, 35), (30, 36), (24, 40), (18, 36), (11, 35), (13, 31), (8, 29), (13, 25), (10, 22), (15, 18)])
    s.add(mane, F, dither=True, noise=0.3, soft=1.6)
    s.add(mir(poly([(17, 17), (9, 8), (20, 13)])), F)
    s.maskpx(mir(poly([(16, 15), (12, 11), (18, 14)])), '#2a1f22')
    s.add(ellipse(24, 21, 8, 7), F, soft=1.4)
    s.add(poly([(19, 22), (29, 22), (27.5, 34), (20.5, 34)]) | ellipse(24, 33, 3.6, 2.5), F, soft=1.3, bias=0.06)
    s.add(ellipse(24, 34, 2.2, 1.4), ['#050405', '#141114', '#2e292c'])
    s.maskpx(mir(poly([(20.5, 29), (22.5, 30), (22.5, 36), (20.5, 33)])), '#2a0a10')
    s.pxm([(21, 30), (21, 31), (21, 32), (22, 34), (22, 35)], '#e6e0cc')
    s.maskpx(mir(chain([(18, 18), (22, 21)], 0.6)), '#0d0c0e')
    s.pxm([(20, 21), (21, 21)], EYE_Y)
    s.pxm([(21, 21)], '#2a1505')
    s.px([(24, 24), (24, 26), (24, 28)], '#625d62')
    return s

def ghoul():
    s = Sprite('#09090a')
    G = R['ghoul']
    s.add(mir(chain([(19, 34), (16, 40), (18, 46)], 2.0, 1.5)), G)
    s.add(ellipse(24, 29, 10, 9.5), G, dither=True)
    for y in [25, 28, 31]:
        s.maskpx(mir(chain([(21, y), (16, y + 1.5)], 0.45)), '#40453a')
    s.add(mir(chain([(16, 21), (9, 30), (7, 40), (8, 44)], 2.1, 1.2)), G, bias=0.03)
    for k in range(3):
        s.pxm([(5 + k * 2, 45), (5 + k * 2, 46), (5 + k * 2, 47)], '#d6d0b8')
    s.add(ellipse(24, 14, 6.5, 6.5) | poly([(19, 15), (29, 15), (27, 27), (21, 27)]), G, soft=1.2)
    s.maskpx(mir(ellipse(21.3, 13.5, 1.8, 1.5)), '#0d0e0b')
    s.pxm([(21, 13)], '#e8ecd8')
    s.maskpx(poly([(21.5, 18), (26.5, 18), (26, 26), (22, 26)]), '#120808')
    s.px([(22, 18), (24, 18), (26, 18), (22, 19), (26, 19), (23, 25), (25, 25), (23, 24)], '#d0c8a8')
    s.px([(24, 22), (24, 23)], '#4a1414')
    s.px([(24, 16)], '#282c22')
    return s

def scorpion():
    s = Sprite('#0b0704')
    A = R['amber']
    s.add(chain([(30, 30), (38, 22), (39, 11), (33, 4), (26, 7)], 2.8, 1.8), A, dither=True)
    for (x, y) in [(36, 25), (39, 17), (37, 8), (30, 4)]:
        s.px([(x, y), (x + 1, y)], '#331d0c')
    s.add(poly([(22, 8), (28, 5), (27, 11)]) | chain([(25, 9), (22, 14)], 1.1, 0.4), R['chitin_d'], bias=0.15)
    s.px([(22, 14), (22, 15)], '#e8d870')
    for pts in [[(17, 34), (9, 35), (5, 45)], [(18, 37), (12, 41), (10, 46)]]:
        s.add(mir(chain(pts, 1.5, 0.8)), A, bias=-0.1)
    s.add(ellipse(24, 34, 12, 8), A, dither=True)
    for x in [16, 20, 24, 28, 32]:
        s.px([(x, 30), (x, 31)], '#331d0c')
    for side in [1, -1]:
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(15), 33), (X(10), 28), (X(8), 24)], 2.1, 1.7), A)
        s.add(ellipse(X(8), 20, 4.6, 5.4, 15 * side), A, soft=1.3)
        s.add(chain([(X(5.5), 17), (X(4.5), 11), (X(6.5), 6)], 2.0, 0.5), A, bias=0.05)
        s.add(chain([(X(10), 16), (X(11.5), 11), (X(9.5), 7.5)], 1.6, 0.5), A, bias=0.1)
    s.pxm([(21, 32), (22, 32)], '#0b0704')
    s.pxm([(22, 32)], '#ffcf5a')
    return s

def wraith():
    s = Sprite('#030407')
    C = R['cloth']
    robe = poly([(24, 3), (34, 8), (37, 20), (40, 34), (44, 46), (39, 42), (35, 47), (31, 42), (27, 47), (24, 43), (20, 47), (16, 42), (12, 47), (9, 42), (4, 46), (8, 34), (11, 20), (14, 8)])
    s.add(robe, C, dither=True, soft=2)
    s.add(mir(chain([(14, 20), (8, 28), (6, 31)], 3.4, 2.6)), C, dither=True)
    BN = ['#2e2c28', '#56524a', '#827c70', '#aaa494']
    for side in [1, -1]:
        X = (lambda x: x) if side == 1 else (lambda x: W - 1 - x)
        for pts in [[(6, 32), (3, 37), (2, 42)], [(7, 33), (6, 39), (6, 44)], [(8, 32), (10, 37), (10, 42)]]:
            s.add(chain([(X(x), y) for x, y in pts], 0.8, 0.5), BN, bias=0.1)
    s.add(ellipse(24, 15, 6.5, 7.5), R['dark'], flat=0, ao=False)
    s.pxm([(21, 15), (22, 15)], EYE_C)
    s.pxm([(21, 16)], '#4fb8c8')
    hem = (yy > 40) & robe
    s.erase |= hem & (NOISE > 0.5)
    return s

def slime():
    s = Sprite('#060d07')
    body = ellipse(24, 34, 19, 11) | ellipse(24, 25, 12, 12) | ellipse(15, 39, 7, 6) | ellipse(34, 38, 8, 7)
    s.add(body, R['slime'], soft=2.2, dither=True, bias=-0.05)
    TB = ['#203a22', '#35573a', '#567a50', '#7c9c6a']
    s.add(ellipse(22, 30, 5, 4.5) | rect(19.5, 32, 25, 36.5), TB, bias=0.05)
    s.px([(20, 30), (21, 30), (20, 31), (21, 31), (23, 30), (24, 30), (23, 31), (24, 31)], '#0d1c10')
    s.px([(22, 33), (20, 35), (22, 35), (24, 35)], '#0d1c10')
    s.add(chain([(30, 30), (36, 36)], 0.9), TB)
    s.add(chain([(11, 37), (16, 41)], 0.7), TB)
    s.maskpx(body & (BAYER_T > 0.3) & ((xx - 22) ** 2 + (yy - 32) ** 2 < 40), '#357039', 200)
    s.px([(17, 16), (18, 15), (19, 15), (16, 17), (16, 18)], '#c8e6a0')
    s.px([(9, 31), (9, 32), (39, 30)], '#a6d083')
    for (x, y) in [(28, 20), (31, 25), (14, 33), (27, 40), (18, 24)]:
        s.px([(x, y)], '#9fcc7a')
    s.px([(12, 45), (13, 46), (36, 46), (30, 46)], '#357039')
    return s

import monsters
for f in [ant, rat, sporeling, wolf, ghoul, scorpion, wraith, slime]:
    monsters.ALL[f.__name__] = f
imgs = {k: f().render() for k, f in monsters.ALL.items()}
sheet(list(imgs.values()), scale=5, cols=5).save('sheet2.png')
for k, im in imgs.items(): im.save(f'{k}.png')
