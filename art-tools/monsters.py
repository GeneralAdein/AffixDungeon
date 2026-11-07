from pxlib import *

R = {
 'chitin': ['#1c0c0a', '#3d1610', '#66241a', '#8f3a26', '#b45a36', '#d4845a'],
 'chitin_d': ['#140807', '#2c100c', '#4a1b14', '#6b2a1c', '#8f3f28'],
 'fur': ['#171413', '#2a2522', '#3f3732', '#594e46', '#76695e', '#968779'],
 'fur_d': ['#100e0e', '#1f1b1a', '#2f2926', '#433a35', '#5a4e47'],
 'pink': ['#3a1f22', '#5e3236', '#86494c', '#a8676a', '#c48a86'],
 'leather': ['#140f17', '#251b2a', '#38283c', '#4f3850', '#6a4c62', '#86656f'],
 'membrane': ['#1a1219', '#2d1f2a', '#43303c', '#5a4150', '#755866'],
 'slime': ['#0d1c10', '#16331b', '#23502a', '#357039', '#4f914a', '#7db363'],
 'cap': ['#1a0b0a', '#361412', '#58201a', '#7a3020', '#9c4a2e', '#ba6e48'],
 'stem': ['#25201b', '#423a30', '#655a4a', '#8a7d68', '#ad9f86', '#cbbfa4'],
 'bone': ['#1d1a16', '#38322a', '#5a5246', '#82786a', '#aaa08e', '#d0c8b2'],
 'rust': ['#1a110c', '#352116', '#5a351f', '#7d4c2a', '#9c6a3c'],
 'steel': ['#16181c', '#2c3038', '#474d58', '#6a7280', '#949cab', '#c2c8d2'],
 'wood': ['#140c07', '#2b1a0e', '#472b16', '#64401f', '#83582c', '#a07440'],
 'spider': ['#0c0a0f', '#19151f', '#2a2432', '#3d3448', '#52475e', '#6b5f77'],
 'gob': ['#11180d', '#203019', '#344a26', '#4b6434', '#667e46', '#86995e'],
 'cloth': ['#07080d', '#0f121b', '#191e2c', '#252c40', '#353f58', '#4a5672'],
 'stone': ['#121211', '#262523', '#3e3c39', '#58554f', '#76726a', '#98938a'],
 'ghoul': ['#141611', '#282c22', '#40453a', '#5d6352', '#7c816c', '#9da18a'],
 'wolf': ['#0f0e10', '#1e1c20', '#312e33', '#48444a', '#625d62', '#807a7c'],
 'amber': ['#180e07', '#331d0c', '#532f13', '#78461c', '#9d6227', '#c38a3f'],
 'robe': ['#100608', '#200c11', '#36141c', '#4f1f2a', '#6b2d3a', '#874152'],
 'skin': ['#2a1d17', '#4a342a', '#6d4f40', '#8f6c58', '#b08d74'],
 'gold': ['#2a1d06', '#54390c', '#80591a', '#ab7f2a', '#d4a944', '#f2d27a'],
 'tongue': ['#2a0a10', '#4e1420', '#782232', '#9e3646', '#c0565f'],
 'dark': ['#050405', '#0b090b', '#120f12'],
}
EYE_R = '#ff3b2e'
EYE_Y = '#ffc93c'
EYE_C = '#9ff5ff'


def ant():
    s = Sprite('#0c0605')
    s.add(ellipse(24, 15, 12, 9.5), R['chitin_d'], dither=True)
    s.px([(19, 9), (20, 9), (21, 10)], '#b45a36')
    # back legs
    for pts in [[(17, 22), (9, 16), (3, 30)], [(18, 27), (8, 26), (4, 44)]]:
        s.add(mir(chain(pts, 1.6, 1.0)), R['chitin_d'])
    s.add(ellipse(24, 25, 7, 5.5), R['chitin'])
    for pts in [[(18, 30), (10, 34), (11, 45)]]:
        s.add(mir(chain(pts, 1.8, 1.0)), R['chitin'])
    # antennae
    s.add(mir(chain([(20, 24), (15, 12), (7, 6), (5, 8)], 1.0, 0.6)), R['chitin_d'])
    head = ellipse(24, 31, 9, 8) | ellipse(24, 26, 6.5, 5)
    s.add(head, R['chitin'], soft=1.3)
    # mandibles
    s.add(mir(chain([(20, 37), (17, 41), (19, 45), (22, 44)], 1.8, 0.7)), R['chitin_d'], bias=0.1)
    # compound eyes
    for (cx, cy) in [(17.5, 29)]:
        s.add(mir(ellipse(cx, cy, 2.6, 3.2)), ['#070404', '#140808', '#2a1010', '#4a1c18'], lo=-0.6)
    s.pxm([(16, 27)], '#e0a080')
    s.pxm([(23, 22), (22, 23)], '#d4845a')
    s.px([(24, 34)], '#3d1610')
    return s


def spider():
    s = Sprite('#060508')
    s.add(ellipse(24, 15, 14, 11), R['spider'], dither=True, noise=0.15)
    # marking
    s.maskpx(poly([(24, 9), (27, 14), (24, 19), (21, 14)]), '#7a1712')
    s.maskpx(poly([(24, 11), (25.5, 14), (24, 17), (22.5, 14)]), '#a8261c')
    legs = [
        [(17, 24), (9, 8), (2, 22), (1, 30)],
        [(17, 27), (7, 16), (2, 38), (2, 44)],
        [(18, 30), (9, 24), (6, 44)],
        [(19, 32), (13, 30), (12, 45)],
    ]
    for i, pts in enumerate(legs):
        s.add(mir(chain(pts, 1.8, 0.9)), R['spider'], bias=0.05 * i)
    s.add(ellipse(24, 29, 9.5, 7.5), R['spider'], soft=1.3, bias=0.05)
    # fangs
    s.add(mir(chain([(21.5, 34), (21, 39), (22.5, 42)], 1.6, 0.6)), R['bone'][1:], bias=-0.1)
    # eye cluster
    s.pxm([(21, 26), (22, 26), (21, 27), (22, 27)], EYE_R)
    s.pxm([(19, 28), (20, 28.6)], '#c2221a')
    s.pxm([(23, 29)], '#c2221a')
    s.pxm([(21, 26)], '#ffb0a0')
    return s


def bat():
    s = Sprite('#08060a')
    wing = poly([(20, 22), (12, 10), (4, 9), (1, 14), (2, 24), (4, 30), (7, 28), (9, 33), (12, 31), (14, 35), (17, 32), (20, 34)])
    s.add(mir(wing), R['membrane'], bias=-0.05, soft=2)
    # finger bones
    for pts in [[(20, 22), (12, 10), (4, 9)], [(12, 10), (2, 22)], [(12, 10), (7, 27)], [(12, 10), (12, 30)]]:
        s.maskpx(mir(chain(pts, 0.6)), '#755866')
    s.pxm([(4, 9), (3, 9), (2, 10)], '#c9b8a8')
    s.add(ellipse(24, 28, 6, 8), R['leather'], dither=True)
    s.add(mir(poly([(19, 19), (18, 9), (23, 17)])), R['leather'])
    s.maskpx(mir(poly([(19.5, 17), (19, 12), (21.5, 16)])), '#5a3f55')
    s.add(ellipse(24, 20, 5.5, 4.8), R['leather'])
    s.add(ellipse(24, 23, 2.5, 1.8), R['leather'][1:], bias=-0.1)
    s.pxm([(21, 19)], EYE_R)
    s.pxm([(22, 25)], '#e8e0d0')
    s.pxm([(22, 26)], '#b8b0a0')
    s.add(mir(chain([(22, 35), (21, 39), (20, 41)], 1.0, 0.5)), R['leather'])
    return s


def rat():
    s = Sprite('#0a0807')
    s.add(chain([(34, 38), (42, 34), (45, 26), (42, 18), (38, 20)], 1.4, 0.6), R['pink'])
    s.add(ellipse(24, 30, 15, 12), R['fur'], dither=True, noise=0.25)
    # fur strokes
    for x0 in range(12, 37, 4):
        s.px([(x0, 24 + (x0 % 3)), (x0 + 1, 25 + (x0 % 3))], '#2a2522')
    s.add(mir(ellipse(16, 21, 4, 4.5, -20)), R['fur'])
    s.add(mir(ellipse(16.5, 21.5, 2.2, 2.8, -20)), R['pink'], bias=-0.1)
    s.add(ellipse(24, 30, 8, 7) | ellipse(24, 36, 5, 4.5), R['fur'], soft=1.5, bias=0.05)
    s.add(ellipse(24, 38.5, 2.2, 1.6), R['pink'])
    # paws
    s.add(mir(chain([(17, 38), (16, 43)], 2.2, 1.6)), R['fur'])
    s.pxm([(14, 45), (16, 45), (18, 45)], '#c8bfb0')
    s.pxm([(20, 30), (21, 30)], EYE_R)
    s.pxm([(20, 29)], '#ffb0a0')
    s.px([(23, 41), (24, 41), (23, 42), (24, 42)], '#d8c690')
    s.px([(24, 42)], '#a8965a')
    s.pxm([(17, 37), (15, 36), (13, 36)], '#b3a698', 160)
    return s


def slime():
    s = Sprite('#060d07')
    body = ellipse(24, 34, 19, 11) | ellipse(24, 26, 12, 12) | ellipse(15, 39, 7, 6) | ellipse(34, 38, 8, 7)
    s.add(body, R['slime'], soft=2.2, dither=True)
    # suspended skull and bones (dimmed)
    sk = ellipse(22, 31, 5, 4.5) | rect(19, 33, 25, 37)
    s.maskpx(sk, '#5c8a4f')
    s.px([(20, 31), (21, 31), (20, 32), (24, 31), (23, 31), (24, 32), (22, 34), (20, 36), (22, 36), (24, 36)], '#1f3f22')
    s.maskpx(chain([(30, 30), (36, 36)], 0.8), '#6e9b5c')
    s.px([(30, 29), (29, 30), (37, 36), (36, 37)], '#6e9b5c')
    s.maskpx(chain([(10, 37), (16, 41)], 0.6), '#5c8a4f')
    # gloss
    s.px([(17, 18), (18, 17), (19, 17), (16, 19), (16, 20)], '#c8e6a0')
    s.px([(9, 31), (9, 32), (39, 30)], '#a6d083')
    for (x, y) in [(28, 22), (31, 26), (14, 34), (27, 40)]:
        s.px([(x, y)], '#9fcc7a')
    s.px([(12, 44), (13, 45), (36, 45)], '#357039')
    return s


def sporeling():
    s = Sprite('#0b0605')
    s.add(chain([(16, 42), (10, 46)], 1.5, 0.8) | chain([(32, 42), (39, 46)], 1.5, 0.8) | chain([(24, 42), (25, 47)], 1.4, 0.8), R['stem'])
    s.add(mir(chain([(16, 24), (10, 33), (9, 40)], 2.4, 1.4)), R['stem'], bias=-0.1)
    s.pxm([(8, 41), (9, 42), (10, 41)], '#cbbfa4')
    s.add(ellipse(24, 32, 9, 12), R['stem'], dither=True, noise=0.2)
    gills = ellipse(24, 19, 17, 4)
    s.add(gills, ['#3a2e24', '#5a4836', '#7a654c'], flat=1)
    for x in range(9, 40, 2):
        s.px([(x, 19), (x, 20)], '#2a2018')
    s.add(ellipse(24, 13, 18, 9) & (yy < 19), R['cap'], dither=True, soft=1.6)
    for (x, y, r) in [(16, 10, 1.6), (27, 7, 1.3), (33, 12, 1.8), (21, 14, 1), (9, 15, 1)]:
        s.maskpx(ellipse(x, y, r, r * 0.8), '#cbbfa4')
    # hollow face
    s.pxm([(20, 28), (21, 28), (20, 29), (21, 29)], '#120c08')
    s.pxm([(21, 28)], '#c9d870')
    s.px([(22, 34), (23, 34), (24, 34), (25, 34), (23, 35), (24, 35)], '#120c08')
    return s


def skeleton():
    s = Sprite('#09080a')
    B = R['bone']
    # sword (viewer left)
    s.add(chain([(11, 33), (9, 4)], 1.2, 0.7), R['rust'] + ['#b08050'], bias=0.1)
    s.add(chain([(6, 33), (16, 34)], 1.0), R['rust'])
    s.add(chain([(11, 35), (11.5, 40)], 1.0), R['wood'])
    # shield (viewer right)
    sh = ellipse(37, 33, 7.5, 9)
    s.add(sh, R['wood'], dither=True)
    s.maskpx(ellipse(37, 33, 7.5, 9) & ~ellipse(37, 33, 6.3, 7.8), '#3a3a40')
    s.maskpx(ellipse(37, 33, 1.6, 1.6), '#6a7280')
    # legs
    s.add(mir(chain([(21, 36), (19, 41), (19, 46)], 1.3)), B)
    s.pxm([(18, 46), (17, 46), (20, 46)], '#aaa08e')
    s.add(mir(ellipse(21, 35, 4, 2.5)), B)
    # spine + ribs
    s.add(chain([(24, 22), (24, 35)], 1.3), B)
    for i, y in enumerate([24, 27, 30]):
        s.add(mir(chain([(24, y), (18 + i * 0.5, y + 1.5), (19 + i, y + 3)], 0.9)), B)
    # arms
    s.add(chain([(18, 22), (14, 28), (12, 34)], 1.3, 1.1), B)
    s.add(chain([(30, 22), (33, 27), (34, 30)], 1.3, 1.1), B)
    s.add(mir(ellipse(18.5, 22, 3, 2)), B)
    # skull
    s.add(ellipse(24, 13, 6.5, 7) | rect(21, 17, 27, 21), B, soft=1.2)
    s.pxm([(20, 12), (21, 12), (22, 12), (20, 13), (21, 13), (22, 13), (21, 14)], '#0e0b0a')
    s.pxm([(21, 13)], '#ff5a2a')
    s.px([(24, 16), (23, 17), (24, 17)], '#0e0b0a')
    s.px([(21, 19), (23, 19), (25, 19), (27, 19)], '#2c261f')
    s.px([(22, 8), (23, 8)], '#2c261f')
    # tattered cloth
    s.add(poly([(17, 33), (31, 33), (30, 38), (28, 36), (26, 40), (24, 36), (21, 39), (19, 36), (18, 38)]), R['robe'], bias=-0.1, dither=True)
    return s


def goblin():
    s = Sprite('#0a0d07')
    G = R['gob']
    # cleaver (viewer right)
    s.add(poly([(38, 20), (45, 20), (45, 30), (40, 30)]), R['steel'], bias=-0.05)
    s.maskpx(chain([(45, 20), (45, 30)], 0.5), '#c2c8d2')
    s.px([(42, 26), (43, 27)], '#5a1a14')
    s.add(chain([(39, 31), (37, 36)], 1.1), R['wood'])
    # body hunched
    s.add(ellipse(24, 37, 11, 10), R['leather'][:1] + R['rust'], dither=True)
    s.maskpx(chain([(15, 31), (32, 43)], 0.7), '#2b1a0e')
    s.px([(22, 36), (23, 36), (22, 37), (23, 37)], '#80591a')
    s.add(chain([(15, 32), (11, 39), (12, 44)], 2.2, 1.6), G)
    s.add(chain([(33, 32), (36, 36), (37, 34)], 2.2, 1.6), G)
    s.pxm([(10, 45), (12, 46), (14, 45)], '#d8d0b0')
    # ears
    s.add(mir(poly([(16, 18), (1, 13), (5, 17), (15, 25)])), G, bias=0.05)
    s.maskpx(mir(poly([(14, 19), (5, 15.5), (14, 22)])), '#4a3020')
    # head
    s.add(ellipse(24, 21, 10, 9.5) | ellipse(24, 26, 7, 5), G, soft=1.4)
    s.add(ellipse(24, 22, 2.3, 3.6), G, bias=0.15)
    # brow + eyes
    s.maskpx(mir(chain([(16, 16), (21, 18.5)], 0.7)), '#203019')
    s.pxm([(18, 19), (19, 19), (20, 19)], EYE_Y)
    s.pxm([(19, 19)], '#1a0a05')
    # grin
    s.maskpx(poly([(17, 27), (31, 27), (28, 30), (20, 30)]), '#1a0a08')
    s.px([(18, 27), (20, 27), (22, 27), (25, 27), (27, 27), (29, 27), (21, 28), (27, 28)], '#d8cfa8')
    s.px([(19, 29), (23, 29), (26, 29)], '#b0a780')
    return s


def wraith():
    s = Sprite('#030407')
    C = R['cloth']
    robe = poly([(24, 3), (34, 8), (37, 20), (40, 34), (44, 46), (39, 42), (35, 47), (31, 42), (27, 47), (24, 43), (20, 47), (16, 42), (12, 47), (9, 42), (4, 46), (8, 34), (11, 20), (14, 8)])
    p = s.add(robe, C, dither=True, soft=2)
    # sleeves + hands
    s.add(mir(chain([(14, 20), (8, 28), (6, 32)], 3.2, 2.4)), C, dither=True)
    for side in [1, -1]:
        bx = 6 if side == 1 else 42
        for k, dx in enumerate([-2, 0, 2]):
            pts = [(bx, 33), (bx + dx * side * 0.6, 37 + k % 2), (bx + dx * side, 41)]
            s.maskpx(chain(pts, 0.5), '#9a9a8a')
    # hood interior
    s.add(ellipse(24, 15, 6.5, 7.5), R['dark'], flat=0, ao=False)
    s.pxm([(21, 15), (22, 15)], EYE_C)
    s.pxm([(21, 16)], '#4fb8c8')
    # dissolve hem
    hem = (yy > 40) & (BAYER_T > 0.1) & robe
    s.erase |= hem & (NOISE > 0.45)
    return s


def golem():
    s = Sprite('#0a0a09')
    ST = R['stone']
    s.add(mir(poly([(14, 36), (21, 36), (21, 46), (12, 46)])), ST, noise=0.35, dither=True)
    s.add(poly([(10, 14), (38, 14), (41, 36), (7, 36)]), ST, noise=0.35, dither=True, soft=0.6)
    s.add(mir(poly([(1, 14), (11, 13), (12, 30), (2, 32)])), ST, noise=0.35, soft=0.6)
    s.add(mir(poly([(0, 31), (11, 30), (12, 40), (1, 41)])), ST, noise=0.35, soft=0.6, bias=0.05)
    s.add(poly([(18, 4), (30, 4), (31, 15), (17, 15)]), ST, noise=0.3, soft=0.6)
    # cracks with glow
    glow = '#4be0ff'
    s.maskpx(chain([(24, 18), (21, 23), (25, 27), (22, 32)], 0.55), glow)
    s.maskpx(chain([(14, 20), (17, 25)], 0.5), '#2a9cbc')
    s.maskpx(chain([(35, 26), (32, 31)], 0.5), '#2a9cbc')
    s.px([(20, 9), (21, 9), (22, 9), (26, 9), (27, 9), (28, 9)], glow)
    s.px([(21, 10), (27, 10)], '#2a9cbc')
    for (x, y) in [(12, 22), (33, 18), (19, 30), (36, 33), (5, 20), (43, 36)]:
        s.px([(x, y), (x + 1, y)], '#262523')
    return s


def ghoul():
    s = Sprite('#09090a')
    G = R['ghoul']
    s.add(mir(chain([(19, 34), (16, 40), (18, 46)], 2.0, 1.5)), G)
    s.add(ellipse(24, 28, 10, 10), G, dither=True)
    for y in [24, 27, 30]:
        s.maskpx(mir(chain([(20, y), (16, y + 1.5)], 0.45)), '#40453a')
    s.add(mir(chain([(16, 20), (9, 30), (7, 40), (8, 44)], 2.1, 1.2)), G, bias=0.03)
    for k in range(3):
        s.pxm([(5 + k * 2, 45), (5 + k * 2, 46)], '#d6d0b8')
    s.add(ellipse(24, 16, 7, 7.5) | ellipse(24, 21, 5.5, 4), G, soft=1.3)
    s.maskpx(mir(ellipse(21, 15, 1.8, 1.4)), '#0d0e0b')
    s.pxm([(21, 15)], '#e8ecd8')
    s.maskpx(poly([(19, 20), (29, 20), (27, 25), (21, 25)]), '#120808')
    s.px([(20, 20), (22, 20), (24, 20), (26, 20), (28, 20), (21, 24), (23, 24.5), (25, 24.5), (27, 24)], '#d0c8a8')
    s.px([(22, 22), (26, 22)], '#3a1010')
    return s


def wolf():
    s = Sprite('#08070a')
    F = R['wolf']
    s.add(ellipse(24, 36, 17, 11), F, dither=True, noise=0.25)
    for x0 in range(9, 40, 3):
        s.px([(x0, 31 + x0 % 4), (x0, 32 + x0 % 4)], '#1e1c20')
    s.add(mir(chain([(15, 38), (14, 46)], 2.6, 2.2)), F)
    s.pxm([(12, 46), (14, 46), (16, 46)], '#cfc8b8')
    s.add(mir(poly([(15, 18), (11, 5), (21, 14)])), F, bias=0.05)
    s.maskpx(mir(poly([(15, 15), (13, 9), (18, 14)])), '#3a2a2a')
    s.add(ellipse(24, 21, 10.5, 9) , F, dither=True, soft=1.5)
    s.add(ellipse(24, 29, 6, 6), F, soft=1.4, bias=0.08)
    s.add(ellipse(24, 26.5, 2.4, 1.6), ['#050405', '#141114', '#2a2528'])
    # snarl
    s.maskpx(poly([(19, 31), (29, 31), (27, 35), (21, 35)]), '#2a0a10')
    s.px([(20, 31), (28, 31), (20, 32), (28, 32), (20, 33), (28, 33)], '#e8e2d0')
    s.px([(22, 31), (24, 31), (26, 31), (23, 35), (25, 35)], '#c8c2b0')
    s.maskpx(mir(chain([(17, 17), (21, 20)], 0.6)), '#0f0e10')
    s.pxm([(19, 20), (20, 20)], EYE_Y)
    s.pxm([(20, 20)], '#2a1505')
    return s


def scorpion():
    s = Sprite('#0b0704')
    A = R['amber']
    # tail arching over
    s.add(chain([(30, 30), (38, 22), (38, 10), (31, 4), (25, 8)], 2.6, 1.6), A, dither=True)
    s.add(poly([(22, 9), (27, 6), (26, 11)]) | chain([(25, 9), (23, 13)], 1.0, 0.4), R['chitin_d'], bias=0.15)
    s.px([(23, 13), (23, 14)], '#e0d070')
    # legs
    for pts in [[(17, 34), (9, 36), (5, 45)], [(18, 37), (11, 41), (9, 46)]]:
        s.add(mir(chain(pts, 1.5, 0.9)), A, bias=-0.1)
    s.add(ellipse(24, 33, 12, 8), A, dither=True)
    for x in [16, 20, 24, 28, 32]:
        s.px([(x, 29), (x, 30)], '#331d0c')
    # pincers
    for side in [1, -1]:
        def X(x): return x if side == 1 else W - x
        s.add(chain([(X(15), 32), (X(9), 26), (X(7), 21)], 2.0, 1.6), A)
        s.add(ellipse(X(7), 17, 4.5, 5.5, 20 * side), A, soft=1.4)
        s.erase |= poly([(X(6.5), 11), (X(8.5), 16), (X(6), 18), (X(5), 12)])
    s.pxm([(21, 31), (22, 31)], '#0b0704')
    s.pxm([(22, 31)], '#ffcf5a')
    return s


def cultist():
    s = Sprite('#08040506'[:7])
    Rb = R['robe']
    s.add(poly([(24, 6), (33, 12), (35, 24), (39, 46), (9, 46), (13, 24), (15, 12)]), Rb, dither=True, soft=2)
    # trims
    s.maskpx(chain([(24, 24), (24, 46)], 0.6), '#200c11')
    s.maskpx(chain([(14, 44), (34, 44)], 0.5), '#80591a')
    # hood void + pale mask
    s.add(ellipse(24, 15, 6.5, 7), R['dark'], flat=0, ao=False)
    s.add(ellipse(24, 16, 4, 5) & (yy < 20), R['bone'][2:], bias=0.1)
    s.px([(22, 15), (26, 15)], '#120608')
    s.px([(22, 16), (26, 16)], '#ff4030')
    s.px([(24, 18)], '#5a5246')
    # arms + dagger
    s.add(mir(chain([(15, 22), (17, 30), (22, 33)], 2.6, 2.0)), Rb)
    s.add(ellipse(24, 33, 3, 2.4), R['skin'])
    s.add(chain([(24, 31), (24, 22)], 0.9, 0.4), R['steel'], bias=0.2)
    s.px([(22, 31), (23, 31), (25, 31), (26, 31)], '#ab7f2a')
    # sigil on chest
    s.px([(24, 38), (23, 39), (25, 39), (22, 40), (26, 40), (24, 40), (24, 41)], '#c0303a')
    return s


def mimic():
    s = Sprite('#0a0605')
    Wd = R['wood']
    # lid (open, tilted back)
    s.add(poly([(7, 6), (41, 6), (43, 17), (5, 17)]), Wd, dither=True, soft=0.8)
    s.maskpx(rect(5, 9, 43, 11), '#4c4c55')
    s.maskpx(rect(5, 9, 43, 10), '#7a7a85')
    # mouth interior
    s.add(poly([(6, 17), (42, 17), (42, 28), (6, 28)]), ['#100406', '#1e0709', '#2c0b0e'], flat=0, ao=False)
    # tongue
    s.add(chain([(24, 26), (20, 32), (14, 36), (11, 42)], 3.0, 1.6), R['tongue'])
    # box
    s.add(poly([(5, 28), (43, 28), (42, 45), (6, 45)]), Wd, dither=True, soft=0.8)
    for x0 in (11, 35):
        s.maskpx(rect(x0, 28, x0 + 3, 45), '#474d58')
        s.maskpx(rect(x0, 28, x0 + 1, 45), '#6a7280')
    s.maskpx(rect(21, 32, 27, 38), '#80591a')
    s.maskpx(rect(22, 33, 26, 37), '#d4a944')
    s.px([(24, 35), (24, 36)], '#2a1d06')
    # teeth top and bottom
    for x in range(7, 42, 3):
        s.px([(x, 17), (x + 1, 17), (x, 18), (x + 1, 18), (x, 19)], '#ddd3b8')
        s.px([(x + 1, 27), (x + 2, 27), (x + 1, 26), (x + 2, 26), (x + 2, 25)], '#c8bea2')
    # eyes in the dark
    s.px([(15, 21), (16, 21), (31, 21), (32, 21)], EYE_Y)
    s.px([(16, 21), (32, 21)], '#5a2a00')
    # coins spilling
    s.px([(9, 46), (10, 46), (38, 46), (40, 46), (39, 45)], '#d4a944')
    return s


ALL = {
 'ant': ant, 'rat': rat, 'bat': bat, 'slime': slime, 'sporeling': sporeling,
 'spider': spider, 'skeleton': skeleton, 'goblin': goblin, 'wolf': wolf, 'ghoul': ghoul,
 'scorpion': scorpion, 'cultist': cultist, 'wraith': wraith, 'mimic': mimic, 'golem': golem,
}

if __name__ == '__main__':
    import sys
    imgs = {k: f().render() for k, f in ALL.items()}
    sheet(list(imgs.values()), scale=5, cols=5).save('sheet.png')
    for k, im in imgs.items():
        im.save(f'{k}.png')
    print('ok')
