"""Deep monsters for floors 13 to 30: giants, demons, elementals, constructs, eldritch horrors
and elder dragons. One builder per kind, and each monster is a short description of its
colours and details.

    python3 deep.py      # writes deep.png (preview sheet) and deep.json (data URIs)
"""
import os, sys, base64, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pxlib
from pxlib import *

# ---------- palettes ----------
SK = {
    'tan': ['#3a2414', '#6a4428', '#9a6a40', '#c8966a', '#ecc49a'],
    'frost': ['#1a2e44', '#2e5476', '#5a8cb4', '#9cc8e8', '#e0f4ff'],
    'fire': ['#3a0c06', '#7a1e0a', '#b8401a', '#e8762e', '#ffb860'],
    'stone': ['#24242a', '#44444c', '#686872', '#94949e', '#c4c4cc'],
    'storm': ['#1e2450', '#343e86', '#5866b8', '#8e9ee4', '#d0d8ff'],
    'olive': ['#26301a', '#44522c', '#687a44', '#94a466', '#c4d09a'],
    'titan': ['#3a3018', '#6a5a2a', '#a48c44', '#d8c070', '#fff0b0'],
    'cyclops': ['#3a2a2a', '#6a4a44', '#9a7068', '#c89c90', '#f0c8bc'],
    'demon': ['#2a0608', '#580c12', '#8c1a20', '#c03a34', '#f07a60'],
    'ash': ['#141214', '#2c2628', '#48403e', '#6e6460', '#a09890'],
    'flayer': ['#3a0a1a', '#6a1430', '#a0284a', '#d05070', '#ff98b0'],
    'cinder': ['#200804', '#4a1208', '#802a10', '#c0501e', '#ff9a40'],
    'abyss': ['#06061a', '#10123a', '#1e2266', '#343c9a', '#6a78d8'],
    'brimstone': ['#2a1a08', '#4e3010', '#7a4e18', '#b07a2a', '#e8b050'],
}
CLOTH = {'brown': ['#2a1a0c', '#4a3018', '#6e4a26', '#94683a'], 'fur': ['#3a3a40', '#5e5e66', '#8a8a94', '#bcbcc4'],
         'red': ['#3a0c0c', '#6a1a1a', '#9a2a26', '#c84a40'], 'blue': ['#101a3a', '#1e2e6a', '#34489a', '#5a70c8'],
         'gold': ['#4a3008', '#8a5c10', '#c89424', '#f0cc5a'], 'black': ['#08080c', '#14141c', '#22222e', '#343444']}
IRON = ['#1e2228', '#3a4048', '#5c646e', '#8a929c', '#bcc4cc']
WOOD = ['#2a1808', '#4a2e14', '#6e4820', '#946630']
BONE = ['#4a4438', '#7a7262', '#aaa290', '#d8d0bc']
GOLD = CLOTH['gold']


def X(side):
    return (lambda x: x) if side == 1 else (lambda x: W - x)


# ---------- giants ----------
def giant(skin, cloth='brown', hair=None, beard=None, weapon='club', eyes='#ffffff', one_eye=False, two_heads=False,
          horns=False, crown=False, flame_hair=False, armor=None, glow=None):
    s = Sprite('#08060a'); S_ = SK[skin]; C_ = CLOTH[cloth]
    s.add(rect(14, 34, 21, 47) | rect(27, 34, 34, 47), S_, soft=1)           # legs
    s.add(rect(12, 44, 22, 47) | rect(26, 44, 36, 47), C_)                     # feet wraps
    s.add(poly([(10, 12), (38, 12), (40, 26), (35, 36), (13, 36), (8, 26)]), S_, soft=1.6)  # torso
    if armor:
        s.add(poly([(12, 14), (36, 14), (37, 26), (33, 34), (15, 34), (11, 26)]), armor, soft=1.2)
    s.add(poly([(12, 30), (36, 30), (37, 40), (32, 38), (24, 41), (16, 38), (11, 40)]), C_, dither=True)  # loincloth / kilt
    for side in (1, -1):
        x = X(side)
        s.add(chain([(x(10), 14), (x(5), 24), (x(5), 33)], 4.2, 3.4), S_)    # arms
        s.add(ellipse(x(5), 35, 3.6, 3.4), S_)                                  # fists
    heads = [(17, 7), (31, 7)] if two_heads else [(24, 7)]
    for (hx, hy) in heads:
        r = 5.2 if two_heads else 6.5
        s.add(ellipse(hx, hy, r, r + .5), S_, soft=1)
        if one_eye:
            s.px([(hx - 1, hy - 1), (hx, hy - 1), (hx + 1, hy - 1), (hx - 1, hy), (hx + 1, hy), (hx - 1, hy + 1), (hx, hy + 1), (hx + 1, hy + 1)], '#f4f0e0')
            s.px([(hx, hy)], '#a01818')
        else:
            s.px([(hx - 3, hy - 1), (hx + 2, hy - 1)], eyes)
            s.px([(hx - 2, hy - 2), (hx - 3, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 2)], S_[0])
        s.px([(hx - 1, hy + 3), (hx, hy + 3), (hx + 1, hy + 3)], S_[0])
        if hair:
            s.add(ellipse(hx, hy - 5, r * .9, 2.6) & (yy < hy - 3), hair, flat=1)
        if beard:
            s.add(poly([(hx - 5, hy + 2), (hx + 5, hy + 2), (hx + 3, hy + 10), (hx, hy + 12), (hx - 3, hy + 10)]), beard, bias=.15)
        if horns:
            for side in (1, -1):
                x = (lambda v, side=side: hx + side * v)
                s.add(chain([(x(4), hy - 4), (x(8), hy - 8), (x(8), hy - 12)], 1.6, .5), BONE, bias=.1)
        if crown:
            s.add(poly([(hx - 6, hy - 4), (hx - 6, hy - 9), (hx - 3, hy - 6), (hx, hy - 10), (hx + 3, hy - 6), (hx + 6, hy - 9), (hx + 6, hy - 4)]), GOLD, soft=.8)
        if flame_hair:
            s.add(poly([(hx - 6, hy - 3), (hx - 5, hy - 11), (hx - 2, hy - 6), (hx, hy - 13), (hx + 2, hy - 6), (hx + 5, hy - 11), (hx + 6, hy - 3)]), SK['fire'], bias=.3)
    w = weapon
    if w == 'club':
        s.add(chain([(41, 36), (44, 12)], 2.2, 3.6), WOOD, bias=.05)
        for (x, y) in [(43, 16), (45, 22), (42, 26)]: s.px([(x, y)], '#d8d0bc')
    elif w == 'axe':
        s.add(chain([(41, 38), (43, 6)], 1.1), WOOD)
        s.add(poly([(43, 6), (47, 4), (47, 16), (43, 13)]), IRON, bias=.2)
    elif w == 'hammer':
        s.add(chain([(41, 38), (43, 10)], 1.1), WOOD)
        s.add(rect(37, 4, 47, 12), IRON, soft=1)
    elif w == 'spear':
        s.add(chain([(41, 40), (44, 2)], .9), WOOD)
        s.add(poly([(42, 6), (46, 6), (44, 0)]), SK['frost'], bias=.3)
    elif w == 'sword':
        s.add(chain([(41, 36), (44, 2)], 1.2), IRON, flat=3)
        s.add(rect(38, 34, 45, 36), GOLD)
    elif w == 'boulder':
        s.add(ellipse(42, 4, 5.5, 4.5), SK['stone'], soft=1.4)
        s.add(chain([(39, 30), (40, 14), (42, 8)], 3, 2.6), SK['stone'])  # arm raised to throw
    elif w == 'lightning':
        s.add(poly([(42, 0), (46, 0), (43, 8), (47, 8), (40, 22), (42, 12), (38, 12)]), ['#a07a10', '#f0c030', '#fff070', '#ffffc0'], bias=.3)
    if glow:
        for (x, y) in glow: s.px([(x, y)], '#ffd860')
    return s


# ---------- demons ----------
def demon(skin, wings=None, horns='curl', tail=True, flame=False, chains=False, eyes='#ffe040', weapon=None, armor=None, crown=False):
    s = Sprite('#0a0204'); S_ = SK[skin]
    if wings:
        for side in (1, -1):
            x = X(side)
            s.add(poly([(x(18), 16), (x(6), 2), (x(1), 10), (x(4), 16), (x(0), 24), (x(6), 24), (x(4), 32), (x(16), 26)]), wings, bias=-.05)
    if tail:
        s.add(chain([(28, 36), (38, 42), (44, 36), (45, 30)], 1.4, .8), S_)
        s.add(poly([(45, 30), (42, 26), (47, 26)]), S_, bias=.2)
    s.add(chain([(20, 34), (18, 40), (21, 44), (19, 47)], 2.4, 1.8) | chain([(28, 34), (30, 40), (27, 44), (29, 47)], 2.4, 1.8), S_)  # digitigrade legs
    s.add(poly([(15, 14), (33, 14), (32, 28), (29, 36), (19, 36), (16, 28)]), S_, soft=1.4)
    if armor:
        s.add(poly([(16, 15), (32, 15), (31, 26), (17, 26)]), armor, soft=1)
    for side in (1, -1):
        x = X(side)
        s.add(chain([(x(15), 16), (x(10), 24), (x(9), 31)], 2.4, 1.8), S_)
        s.px([(x(8), 33), (x(9), 34), (x(10), 33)], '#e8e0c8')
    s.add(ellipse(24, 9, 5, 5.5), S_, soft=1)
    if horns == 'curl':
        for side in (1, -1):
            x = X(side)
            s.add(chain([(x(20), 6), (x(16), 2), (x(13), 4), (x(14), 8)], 1.4, .6), BONE, bias=.1)
    elif horns == 'tall':
        for side in (1, -1):
            x = X(side)
            s.add(chain([(x(21), 5), (x(18), -1), (x(19), -5)], 1.6, .5), BONE, bias=.1)
    elif horns == 'many':
        for (a, b) in [(18, 0), (21, -2), (27, -2), (30, 0), (24, -3)]:
            s.add(chain([(24 + (a - 24) * .5, 5), (a, b)], 1, .4), BONE, bias=.1)
    s.px([(21, 9), (22, 9), (26, 9), (27, 9)], eyes)
    s.px([(22, 12), (23, 13), (24, 13), (25, 13), (26, 12)], '#1a0204')
    s.px([(23, 13), (25, 13)], '#f4f0e0')
    if crown:
        s.add(poly([(19, 4), (19, 0), (21, 2), (24, -1), (27, 2), (29, 0), (29, 4)]), GOLD, soft=.8)
    if flame:
        for (x, y) in [(15, 12), (33, 12), (24, 2)]:
            s.add(poly([(x - 2, y + 2), (x + 2, y + 2), (x, y - 5)]), SK['fire'], bias=.3)
    if chains:
        s.add(chain([(10, 26), (4, 32), (8, 40), (3, 46)], .9) | chain([(38, 26), (44, 32), (40, 40), (45, 46)], .9), IRON, flat=2)
    if weapon == 'whip':
        s.add(chain([(39, 31), (44, 24), (46, 14), (42, 6)], .8, .5), SK['fire'], bias=.2)
    elif weapon == 'blade':
        s.add(chain([(39, 32), (45, 6)], 1.2), ['#1a0a0a', '#4a1414', '#a02a2a', '#ff6a4a'], flat=3)
    return s


# ---------- elementals ----------
def elemental(kind):
    s = Sprite('#08060a')
    if kind == 'magma':
        R = ['#1a1414', '#2e2626', '#443a38', '#5e524e', '#7a6c66']
        body = poly([(12, 14), (36, 14), (40, 30), (34, 38), (14, 38), (8, 30)]) | ellipse(24, 9, 7, 6)
        legs = rect(14, 36, 21, 47) | rect(27, 36, 34, 47)
        arms = chain([(10, 16), (4, 26), (6, 36)], 4.4, 3.6) | chain([(38, 16), (44, 26), (42, 36)], 4.4, 3.6)
        s.add(legs | arms | body, R, soft=1.4)
        for pts in [[(14, 18), (20, 24), (17, 32)], [(30, 16), (26, 24), (31, 34)], [(6, 26), (8, 32)], [(42, 24), (40, 32)], [(18, 40), (17, 46)], [(30, 40), (31, 46)]]:
            s.maskpx(chain(pts, .7) & (legs | arms | body), '#ff8a1a')
            s.maskpx(chain(pts, .3) & (legs | arms | body), '#fff070')
        s.px([(21, 8), (22, 8), (26, 8), (27, 8)], '#fff070')
    elif kind == 'tempest':
        cloud = ellipse(24, 14, 13, 9) | ellipse(14, 18, 8, 7) | ellipse(34, 18, 8, 7) | chain([(24, 22), (22, 32), (26, 40), (23, 46)], 6, 1.5)
        s.add(cloud, SK['storm'], soft=2, dither=True, bias=.1)
        s.add(poly([(10, 22), (14, 22), (11, 30), (15, 30), (6, 44), (9, 33), (5, 33)]), ['#a07a10', '#f0c030', '#fff070', '#ffffc0'], bias=.3)
        s.add(poly([(36, 20), (40, 20), (37, 27), (41, 27), (33, 40), (35, 30), (31, 30)]), ['#a07a10', '#f0c030', '#fff070', '#ffffc0'], bias=.3)
        s.px([(20, 14), (21, 14), (27, 14), (28, 14)], '#ffffff')
        s.px([(22, 18), (23, 18), (24, 18), (25, 18), (26, 18)], '#1e2450')
    elif kind == 'glacier':
        ICE = ['#1a3a5a', '#2e6694', '#5aa0d0', '#a4dcf8', '#f0fcff']
        body = poly([(10, 16), (38, 16), (42, 34), (34, 44), (14, 44), (6, 34)])
        s.add(body, ICE, soft=1.2, bias=.1)
        for (x, y, h) in [(14, 18, 10), (22, 16, 14), (30, 17, 11), (38, 22, 8), (8, 24, 7)]:
            s.add(poly([(x - 3, y + 2), (x + 3, y + 2), (x, y - h)]), ICE, bias=.25, soft=.6)
        s.add(rect(14, 42, 21, 47) | rect(27, 42, 34, 47), ICE)
        s.px([(19, 26), (20, 26), (28, 26), (29, 26)], '#0a2a4a')
        s.px([(19, 25), (29, 25)], '#ffffff')
    elif kind == 'earth':
        R = SK['stone']
        chunks = [ellipse(24, 26, 13, 12), ellipse(24, 10, 7, 6), ellipse(10, 22, 6, 7), ellipse(38, 22, 6, 7), ellipse(8, 34, 5, 5), ellipse(40, 34, 5, 5), rect(14, 36, 21, 47), rect(27, 36, 34, 47)]
        m = np.zeros((W, W), bool)
        for c in chunks: m |= c
        s.add(m, R, soft=1.6, dither=True)
        for pts in [[(14, 20), (18, 28)], [(32, 18), (29, 30)], [(22, 34), (26, 40)]]:
            s.maskpx(chain(pts, .5) & m, '#1a1a1e')
        s.add(ellipse(24, 26, 3, 3), ['#2a5a1a', '#4a9a2a', '#8ad84a', '#d0ff9a'], ao=False)  # a glowing core
        s.px([(21, 10), (22, 10), (26, 10), (27, 10)], '#8ad84a')
        for (x, y) in [(6, 44), (12, 46), (36, 46), (44, 44)]: s.px([(x, y), (x + 1, y)], '#686872')
    return s


# ---------- constructs ----------
def construct(metal, glow='#40d0ff', kind='colossus'):
    s = Sprite('#06060a'); M = metal
    s.add(rect(13, 34, 21, 47) | rect(27, 34, 35, 47), M, soft=.8)
    s.add(rect(9, 12, 39, 36), M, soft=1)
    s.add(rect(17, 3, 31, 13), M, soft=.8)
    for side in (1, -1):
        x = X(side)
        s.add(rect(min(x(2), x(9)), 13, max(x(2), x(9)), 32), M, soft=.8)
        s.add(rect(min(x(1), x(10)), 30, max(x(1), x(10)), 37), M, soft=.8)
    s.px([(x, 8) for x in range(19, 30)], glow) if kind == 'sentinel' else s.px([(20, 8), (21, 8), (27, 8), (28, 8)], glow)
    if kind == 'colossus':
        for x in (14, 24, 34):
            s.maskpx(ellipse(x, 18, 1.4, 1.4), '#2a2e34')  # rivets
        s.maskpx(rect(10, 24, 38, 25), M[0])
    elif kind == 'clockwork':
        for (cx, cy, r) in [(18, 22, 5), (30, 26, 4)]:
            ring = ellipse(cx, cy, r, r) & ~ellipse(cx, cy, r - 1.4, r - 1.4)
            s.add(ring, GOLD, flat=3)
            for a in range(0, 360, 45):
                s.px([(int(cx + (r + 1) * np.cos(np.radians(a))), int(cy + (r + 1) * np.sin(np.radians(a))))], GOLD[2])
        s.add(chain([(24, 3), (24, 0)], .6), GOLD)
    elif kind == 'sentinel':
        for (x, y) in [(14, 16), (32, 18), (20, 30), (28, 28)]:
            s.px([(x, y), (x + 1, y + 1), (x + 2, y + 2)], '#8a4aff')
    elif kind == 'runic':
        for (x, y) in [(13, 16), (21, 20), (29, 16), (16, 28), (27, 28), (5, 20), (41, 20)]:
            s.px([(x, y), (x + 1, y), (x + 2, y), (x + 1, y - 1), (x + 1, y + 1)], glow)
    return s


# ---------- eldritch horrors ----------
def horror(kind):
    s = Sprite('#020204')
    VOID = ['#04030a', '#0c0818', '#1a1430', '#2c2250', '#463878']
    if kind == 'eye':
        for a in range(0, 360, 40):
            ang = np.radians(a + 20); x0, y0 = 24 + 8 * np.cos(ang), 22 + 8 * np.sin(ang)
            s.add(chain([(x0, y0), (24 + 16 * np.cos(ang + .3), 22 + 16 * np.sin(ang + .3)), (24 + 22 * np.cos(ang + .1), 22 + 22 * np.sin(ang + .1))], 1.8, .5), ['#2a0c30', '#541a5a', '#8a2e86', '#c45ab8'])
        s.add(ellipse(24, 22, 12, 12), ['#3a0a2a', '#6a1a4a', '#a83a6a', '#e06a90'], soft=1.6)
        s.add(ellipse(24, 22, 8.5, 7), ['#c8c0b0', '#e0d8c8', '#f4f0e4', '#ffffff'], soft=1, ao=False)
        s.add(ellipse(24, 22, 4, 4.5), ['#5a4a08', '#a08010', '#e0c020', '#fff070'], ao=False)
        s.add(ellipse(24, 22, 1.6, 3.4), ['#000000'] * 4, flat=0, ao=False)
        for pts in [[(17, 20), (19, 23)], [(31, 21), (29, 24)]]: s.maskpx(chain(pts, .4), '#c03040')
    elif kind == 'dreameater':
        s.add(ellipse(24, 14, 13, 10), ['#1a2a5a', '#2e4a8a', '#5a7ac0', '#9ab4ec', '#e0ecff'], soft=2, dither=True, bias=.1)
        for x in (14, 19, 24, 29, 34):
            s.add(chain([(x, 20), (x + 2, 30), (x - 1, 38), (x + 1, 46)], 1.1, .4), ['#1a2a5a', '#2e4a8a', '#5a7ac0', '#9ab4ec'])
        s.add(chain([(24, 18), (24, 26), (21, 32)], 1.4, .6), ['#5a1a6a', '#8a2a9a', '#c04ac8', '#f08af0'])  # proboscis
        for (x, y) in [(16, 8), (22, 6), (28, 9), (32, 13), (18, 14)]: s.px([(x, y)], '#ffffff')
        s.px([(19, 13), (20, 13), (28, 13), (29, 13)], '#f08af0')
    elif kind == 'watcher':
        m = ellipse(24, 24, 18, 17)
        s.add(m, ['#2a1a1a', '#4a2e2a', '#7a4a44', '#a87068', '#d8a098'], soft=2, dither=True)
        rng = np.random.default_rng(5)
        spots = [(24, 22), (14, 16), (33, 15), (12, 28), (35, 28), (20, 33), (29, 35), (24, 11), (17, 23), (31, 22), (24, 40), (8, 21), (40, 21)]
        for i, (x, y) in enumerate(spots):  # big staring eyes, each looking a different way
            big = i == 0
            r = 3.6 if big else 2.2
            s.add(ellipse(x, y, r, r * .85), ['#a8a090', '#d0c8b8', '#f0ece0', '#ffffff'], flat=2, ao=False)
            dx = (i % 3) - 1
            s.px([(x + dx, y), (x + dx - 1, y)] + ([(x + dx, y - 1), (x + dx - 1, y - 1), (x + dx, y + 1), (x + dx - 1, y + 1)] if big else []), '#1a0a0a')
            s.px([(x + dx, y)], '#c02a2a' if big else '#1a0a0a')
    elif kind == 'maw':
        ring = ellipse(24, 24, 20, 18) & ~ellipse(24, 24, 11, 9)
        s.add(ring, ['#2a0a0a', '#4a1414', '#7a2424', '#a83a3a', '#d86060'], soft=1.6)
        s.add(ellipse(24, 24, 11, 9), ['#000000', '#050002', '#0a0004', '#100008'], flat=0, ao=False)
        for a in range(0, 360, 24):  # teeth, pointing in
            ang = np.radians(a)
            p1 = (24 + 11.5 * np.cos(ang - .12), 24 + 9.5 * np.sin(ang - .12)); p2 = (24 + 11.5 * np.cos(ang + .12), 24 + 9.5 * np.sin(ang + .12))
            p3 = (24 + 7 * np.cos(ang), 24 + 5.5 * np.sin(ang))
            s.add(poly([p1, p2, p3]), ['#8a8070', '#c8c0a8', '#ece4cc', '#ffffff'], flat=2, ao=False)
    elif kind == 'hollowking':
        robe = poly([(24, 8), (34, 14), (38, 30), (44, 46), (34, 42), (28, 47), (20, 42), (14, 47), (4, 46), (10, 30), (14, 14)])
        s.add(robe, CLOTH['black'] + ['#4a4a5e'], dither=True, soft=2)
        s.add(ellipse(24, 12, 6.5, 7.5), VOID, flat=0, ao=False)  # an empty face
        for (x, y) in [(21, 10), (23, 14), (26, 9), (27, 13), (24, 11)]: s.px([(x, y)], '#c4aef0')
        s.add(poly([(17, 6), (17, 0), (20, 3), (24, -1), (28, 3), (31, 0), (31, 6)]), GOLD, soft=.8)
        for side in (1, -1):
            x = X(side)
            s.add(chain([(x(14), 18), (x(8), 26), (x(6), 32)], 2, 1.2), CLOTH['black'] + ['#4a4a5e'])
            s.px([(x(5), 33), (x(6), 34), (x(7), 34)], '#c4aef0')
    elif kind == 'hungeringdark':
        m = ellipse(24, 22, 21, 17) | ellipse(10, 34, 9, 9) | ellipse(38, 34, 9, 9) | ellipse(24, 38, 12, 9)
        s.add(m, VOID, soft=2.4, dither=True)
        rng = np.random.default_rng(9)
        ys, xs = np.nonzero(ndimage.binary_erosion(m, iterations=2))
        for i in rng.choice(len(xs), 14, replace=False): s.px([(xs[i], ys[i])], '#e8e0ff')
        for (x, y) in [(15, 18), (30, 15), (22, 28), (34, 30)]:
            s.px([(x, y), (x + 1, y), (x + 2, y)], '#ff2020')
        for (x, y) in [(12, 32), (26, 38)]:
            s.px([(x + i, y) for i in range(6)], '#000000'); s.px([(x + 1, y - 1), (x + 3, y - 1), (x + 5, y - 1), (x + 2, y + 1), (x + 4, y + 1)], '#f4f0e0')
    return s


# ---------- elder dragons (from dragons.py) ----------
def elder_dragon(main, belly, wing, horn, eye, **kw):
    import dragons
    return dragons.dragon(main, belly, wing, horn, eye=eye, k=1.05, **kw)


SPECS = {
    'hillgiant': lambda: giant('tan', 'brown', hair=['#2a1a0c', '#4a3018', '#6e4a26', '#94683a'], weapon='club'),
    'magmacolossus': lambda: elemental('magma'),
    'brimstonebrute': lambda: demon('brimstone', horns='tall', flame=True, tail=True),
    'frostgiant': lambda: giant('frost', 'fur', beard=['#a8c8e0', '#c8e0f0', '#e8f4ff', '#ffffff'], weapon='spear', eyes='#e0ffff'),
    'ironcolossus': lambda: construct(IRON, '#ff4020', 'colossus'),
    'eyeofthedeep': lambda: horror('eye'),
    'firegiant': lambda: giant('fire', 'black', flame_hair=True, beard=SK['fire'][1:], weapon='sword', eyes='#fff070', armor=IRON),
    'tempest': lambda: elemental('tempest'),
    'chaindemon': lambda: demon('ash', horns='curl', chains=True, eyes='#ff4020', tail=False),
    'elderfiredragon': lambda: elder_dragon(['#3a0806', '#7a140c', '#b82a14', '#e85a2a', '#ff9a5a'], ['#7a4a10', '#b8802a', '#e8b050', '#ffe090'], ['#2a0606', '#5a0e0e', '#8a1a14', '#b83020'], BONE, '#fff070', horns=3),
    'stonegiant': lambda: giant('stone', 'brown', weapon='boulder', eyes='#c8e0ff'),
    'dreameater': lambda: horror('dreameater'),
    'clockworkbehemoth': lambda: construct(['#2a1e10', '#5a4020', '#8a6430', '#b88a44', '#e8bc6a'], '#80ffb0', 'clockwork'),
    'ashentormentor': lambda: demon('ash', wings=['#0c0a0c', '#1e1a1c', '#2e2a2a', '#443e3e'], horns='tall', eyes='#ff7a1a', weapon='whip'),
    'cyclops': lambda: giant('cyclops', 'brown', one_eye=True, weapon='hammer'),
    'thousandeyedwatcher': lambda: horror('watcher'),
    'voiddragon': lambda: elder_dragon(['#04030a', '#0c0818', '#1a1430', '#2c2250', '#463878'], ['#1a1430', '#2c2250', '#463878', '#6a5aa0'], ['#020204', '#08060e', '#120c20', '#1e1636'], ['#3a2a6a', '#5a4aa0', '#8a7ad0', '#c4b8ff'], '#c4aef0', horns=3),
    'glacierelemental': lambda: elemental('glacier'),
    'flayerprince': lambda: demon('flayer', wings=['#2a0610', '#4e0e20', '#7a1a32', '#a42e48'], horns='many', eyes='#ffffff', weapon='blade', crown=False),
    'obsidiansentinel': lambda: construct(['#06060a', '#12121a', '#22222e', '#363646', '#5a5a74'], '#b080ff', 'sentinel'),
    'ettin': lambda: giant('olive', 'fur', two_heads=True, weapon='club', hair=['#1a1a10', '#2e2e1c', '#44442a', '#5e5e3a']),
    'mawofnothing': lambda: horror('maw'),
    'stormdragon': lambda: elder_dragon(['#101a4a', '#1e2e7a', '#34489a', '#5a70c8', '#9ab0f0'], ['#5a6a9a', '#8aa0d0', '#c0d0f0', '#eef4ff'], ['#0a1030', '#141e54', '#22307a', '#3446a0'], ['#a07a10', '#f0c030', '#fff070', '#ffffc0'], '#ffffff', horns=2),
    'earthshaker': lambda: elemental('earth'),
    'cinderduke': lambda: demon('cinder', wings=['#1a0602', '#3a0c04', '#5e1a08', '#86300e'], horns='curl', flame=True, crown=True, armor=['#1a1414', '#2e2626', '#443a38', '#5e524e']),
    'runicjuggernaut': lambda: construct(['#1a1e1a', '#2e362e', '#4a564a', '#6e7c6e', '#a0b0a0'], '#40ff90', 'runic'),
    'stormgiant': lambda: giant('storm', 'blue', beard=['#c0c8e8', '#dce2f8', '#f0f4ff', '#ffffff'], weapon='lightning', eyes='#ffffff', armor=['#1a2040', '#2e3870', '#4a58a0', '#7080d0']),
    'hollowking': lambda: horror('hollowking'),
    'bonedragon': lambda: elder_dragon(['#2a2820', '#4a4638', '#7a7462', '#aaa290', '#d8d0bc'], ['#4a4638', '#7a7462', '#aaa290', '#d8d0bc'], ['#14120e', '#242018', '#3a3428', '#524a3a'], ['#1a1a14', '#3a3a30', '#5a5a4a', '#7a7a66'], '#60ff90', horns=2, bone=True),
    'abyssalwarlord': lambda: demon('abyss', wings=['#020210', '#06061e', '#0c0e34', '#16184e'], horns='many', eyes='#40e0ff', weapon='blade', armor=IRON, crown=True),
    'titanwarden': lambda: giant('titan', 'gold', crown=True, beard=['#c8b070', '#e0cc90', '#f4e8b8', '#ffffff'], weapon='sword', eyes='#ffffff', armor=['#4a3a10', '#8a6c1c', '#c8a030', '#f0d060'], glow=[(16, 20), (32, 20), (24, 26)]),
    'hungeringdark': lambda: horror('hungeringdark'),
}

if __name__ == '__main__':
    out, imgs = {}, []
    for k, f in SPECS.items():
        pxlib.FLAT['on'] = False  # dragons.py switches the flat look on; keep the rest shaded
        if 'dragon' in k:
            pxlib.FLAT['on'] = True
        im = f().render()
        imgs.append(im)
        buf = io.BytesIO(); im.save(buf, 'PNG')
        out[k] = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    sheet(imgs, scale=4, cols=8).save('deep.png')
    json.dump(out, open('deep.json', 'w'))
    print(len(out), 'deep monsters')
