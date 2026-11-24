"""Ghosts and spirits: 40 sprites for the 'spirit' family.

Each ghost is built from a few shared shapes (a sheet body, a hooded robe, a long-haired
figure, armor, flame or smoke tails) plus its own colours and details. The lower body fades
to see-through after rendering, so they read as ghosts in the game.

    python3 ghosts.py      # writes ghosts.png (preview sheet) and ghosts.json (data URIs)
"""
import base64, io, json
import numpy as np
from pxlib import *

# ---------- palettes (dark to light) ----------
PALE = ['#2c3650', '#56688a', '#8ea4c4', '#c8d8ec', '#eef6ff']
MIST = ['#3a4252', '#667286', '#9aa6b8', '#cdd6e2', '#f2f6fa']
TEAL = ['#123a40', '#22646a', '#3f9a98', '#7cccc0', '#c4f0e4']
ECTO = ['#103a18', '#1f6a2a', '#3da848', '#82dc6e', '#d2ffb0']
VIOLET = ['#1c1430', '#36265a', '#584090', '#8a6cc4', '#c4aef0']
SHADOW = ['#060509', '#100d18', '#1c1828', '#2a2540', '#3c3658']
RED = ['#3a0a10', '#6e141c', '#a8262a', '#dc5040', '#ff9a78']
GOLD = ['#4a3008', '#8a5c10', '#c89424', '#f0cc5a', '#fff2b0']
FIRE = ['#4a0c04', '#9a2408', '#e0541a', '#ffa030', '#fff07a']
BLUEFIRE = ['#0c1a4a', '#1a3c9a', '#2a78e0', '#62c4ff', '#d8f8ff']
SMOKE = ['#142040', '#24407a', '#3a68b0', '#6ea0dc', '#b8daf8']
WHITE = ['#6a6a78', '#a0a0ae', '#cacad4', '#e8e8ee', '#ffffff']
HAIR = ['#050406', '#0e0c12', '#1a1720', '#2a2632']
SKIN_PALE = ['#7c8c94', '#a8b8bc', '#ccdad8', '#eef6f2']
IRON = ['#1e2228', '#3a4048', '#5c646e', '#8a929c', '#bcc4cc']
RUST = ['#2a1810', '#4e2e1a', '#7a4a28', '#a8743e']
BONE = ['#4a4438', '#7a7262', '#aaa290', '#d8d0bc']
BLOODRED = ['#30060a', '#5c0c12', '#8c1820', '#c03030']
GREENSKIN = ['#1c2a24', '#34483c', '#566e5a', '#86a084']
EMBER = '#ffd25a'


def fade_alpha(img, start, end=47, low=0.35, dither=True):
    """Fade the sprite to see-through from row `start` down to row `end`."""
    a = np.array(img)
    for y in range(start, 48):
        t = min(1, (y - start) / max(1, end - start))
        k = 1 - (1 - low) * t
        row = a[y, :, 3].astype(float) * k
        if dither:
            row = np.where((BAYER_T[y] + 0.5) > k * 1.15, row * 0.6, row)
        a[y, :, 3] = row.astype(np.uint8)
    return Image.fromarray(a, 'RGBA')


def wavy_hem(cx, top, hw, bottom, flare=3, tails=4, depth=5, lean=0):
    """A sheet-ghost body: dome head, straight sides, a scalloped bottom edge."""
    pts = [(cx - hw, top + hw)]
    xs = np.linspace(cx - hw - flare, cx + hw + flare, tails * 2 + 1)
    for i, x in enumerate(xs):
        pts.append((x + lean * (i % 2), bottom if i % 2 == 0 else bottom - depth))
    pts.append((cx + hw, top + hw))
    return ellipse(cx, top + hw, hw, hw) | poly(pts)


def tail_body(cx, top, hw, bottom, curl=1, hw2=1.5):
    """A body that tapers into a curling tail, for spirits that float on smoke or flame."""
    pts = [(cx, top), (cx + 2 * curl, (top + bottom) / 2), (cx - 3 * curl, bottom - 6), (cx + 5 * curl, bottom)]
    m = chain(pts, hw, hw2)
    return m


def robe(cx=24, top=4, bottom=46, hw=10, flare=10, tails=5):
    pts = [(cx, top), (cx + hw * .7, top + 4), (cx + hw, top + 14), (cx + hw + flare * .5, top + 28)]
    hem = []
    xs = np.linspace(cx + hw + flare, cx - hw - flare, tails * 2 + 1)
    for i, x in enumerate(xs):
        hem.append((x, bottom if i % 2 == 0 else bottom - 5))
    pts += hem + [(cx - hw - flare * .5, top + 28), (cx - hw, top + 14), (cx - hw * .7, top + 4)]
    return poly(pts)


def eyes(s, cx, y, kind='hollow', color='#9ff4ff', gap=3, size=1):
    L, R_ = cx - gap - 1, cx + gap
    if kind == 'hollow':
        for x in (L, R_):
            s.px([(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1), (x, y + 2), (x + 1, y + 2)], '#0a0a14')
    elif kind == 'glow':
        for x in (L, R_):
            s.px([(x, y), (x + 1, y)], color)
            if size > 1: s.px([(x, y + 1), (x + 1, y + 1)], color)
    elif kind == 'angry':
        s.px([(L - 1, y - 1), (L, y), (L + 1, y), (R_, y), (R_ + 1, y), (R_ + 2, y - 1)], '#0a0a14')
        s.px([(L, y + 1), (L + 1, y + 1), (R_, y + 1), (R_ + 1, y + 1)], color)
    elif kind == 'sad':
        for x in (L, R_):
            s.px([(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)], '#0a0a14')
        s.px([(L - 1, y - 1), (R_ + 2, y - 1)], '#0a0a14')
    elif kind == 'tear':
        eyes(s, cx, y, 'sad', gap=gap)
        s.px([(L, y + 3), (L, y + 4), (R_ + 1, y + 3), (R_ + 1, y + 5)], '#8ad8ff')


def mouth(s, cx, y, kind='o', color='#0a0a14'):
    if kind == 'o':
        s.px([(cx - 1, y), (cx, y), (cx - 1, y + 1), (cx, y + 1), (cx - 1, y + 2), (cx, y + 2)], color)
    elif kind == 'scream':
        for yy_ in range(y, y + 5):
            w = 1 if yy_ in (y, y + 4) else 2
            s.px([(x, yy_) for x in range(cx - w, cx + w)], color)
    elif kind == 'grin':
        s.px([(x, y) for x in range(cx - 4, cx + 4)], color)
        s.px([(cx - 5, y - 1), (cx + 4, y - 1)], color)
        s.px([(cx - 3, y + 1), (cx - 1, y + 1), (cx + 1, y + 1), (cx + 3, y + 1)], color)
    elif kind == 'line':
        s.px([(x, y) for x in range(cx - 2, cx + 2)], color)
    elif kind == 'frown':
        s.px([(cx - 2, y), (cx - 1, y - 1), (cx, y - 1), (cx + 1, y)], color)


def hands(s, pts_l, ramp, r=1.6):
    for side in (1, -1):
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(x), y) for x, y in pts_l], r, r * 0.7), ramp, bias=0.05)


def sparkles(s, pts, color):
    for x, y in pts:
        s.px([(x, y)], color)


def hair_curtain(cx, top, hw, bottom):
    pts = [(cx - hw + 1, top + 2), (cx, top - 1), (cx + hw - 1, top + 2), (cx + hw + 1, top + 10), (cx + hw + 2, bottom),
           (cx + hw - 2, bottom - 3), (cx + hw - 3, bottom + 1), (cx - hw + 3, bottom + 1), (cx - hw + 2, bottom - 3),
           (cx - hw - 2, bottom), (cx - hw - 1, top + 10)]
    return poly(pts)


def woman(s, dress, hair_bottom=30, face=SKIN_PALE, cx=24, head_y=12, arms=True, hem=44):
    """A long-haired spirit woman in a long dress: yurei, onryo, banshee, la llorona..."""
    s.add(hair_curtain(cx, head_y - 7, 8, hair_bottom), HAIR, flat=1)  # long hair, behind her
    body = poly([(cx - 5, head_y + 6), (cx + 5, head_y + 6), (cx + 9, 30), (cx + 12, hem), (cx + 7, hem - 4), (cx + 4, hem + 1),
                 (cx, hem - 4), (cx - 4, hem + 1), (cx - 7, hem - 4), (cx - 12, hem), (cx - 9, 30)])
    s.add(body, dress, dither=True, soft=1.6)
    if arms:
        hands(s, [(cx - 6, head_y + 9), (cx - 10, head_y + 15), (cx - 9, head_y + 20)], dress, 2.2)
        s.add(mir(ellipse(cx - 9, head_y + 21, 1.8, 1.6)) if cx == 24 else ellipse(cx - 9, head_y + 21, 1.8, 1.6), face)
    s.add(ellipse(cx, head_y, 4.2, 5.2), face, soft=1.2)
    # a fringe and two locks falling in front, framing the face
    s.add(ellipse(cx, head_y - 4, 4.6, 2.2) | mir(chain([(cx - 4, head_y - 2), (cx - 5, head_y + 6), (cx - 4, head_y + 14)], 1.3, 0.9)), HAIR, flat=1)
    return body


def armor_torso(s, ramp, cx=24, top=14, bottom=34, hw=9):
    t = poly([(cx - hw, top), (cx + hw, top), (cx + hw - 1, bottom - 6), (cx + 5, bottom), (cx - 5, bottom), (cx - hw + 1, bottom - 6)])
    s.add(t, ramp, soft=1.2)
    s.add(mir(ellipse(cx - hw - 1, top + 2, 4, 3.4)), ramp, bias=0.1)
    return t


# ---------- the ghosts ----------
def apparition():
    s = Sprite('#0a1020')
    s.add(wavy_hem(24, 6, 12, 44, flare=3, tails=4), PALE, soft=2.2, dither=True, bias=.1)
    hands(s, [(13, 24), (8, 28), (6, 32)], PALE, 2.2)
    eyes(s, 24, 15, 'hollow', gap=4); mouth(s, 24, 21, 'o')
    return s, 30


def poltergeist():
    s = Sprite('#0a1020')
    s.add(wavy_hem(24, 12, 9, 40, flare=2, tails=3, depth=4), MIST, soft=2, dither=True, bias=.1)
    eyes(s, 24, 19, 'angry', '#ffe070', gap=3); mouth(s, 24, 25, 'grin')
    # things it throws: a plate, a chair, a candlestick, a book
    s.add(ellipse(8, 10, 5, 2.2, -15), ['#5a5a66', '#9a9aa6', '#d4d4dc', '#ffffff'])
    s.add(rect(37, 6, 44, 8) | rect(37, 8, 39, 15) | rect(42, 8, 44, 15) | rect(37, 4, 39, 7), RUST)
    s.add(capsule(7, 30, 9, 40, 1), GOLD); s.px([(8, 28), (8, 29)], '#ffcf5a')
    s.add(rect(37, 28, 45, 34), BLOODRED); s.px([(x, 31) for x in range(38, 45)], '#e8d8b0')
    sparkles(s, [(14, 6), (33, 16), (13, 36), (34, 38), (20, 4)], '#d4e8ff')
    return s, 32


def specter():
    s = Sprite('#06080e')
    s.add(robe(24, 4, 46, 9, 9, 5), PALE, dither=True, soft=2)
    s.add(ellipse(24, 14, 5.5, 6.5), BONE, soft=1)
    s.px([(21, 13), (22, 13), (21, 14), (22, 14), (26, 13), (27, 13), (26, 14), (27, 14)], '#06080e')
    s.px([(21, 14), (27, 14)], '#7ff0ff')
    s.px([(23, 17), (25, 17), (22, 19), (23, 19), (24, 19), (25, 19), (26, 19)], '#06080e')
    hands(s, [(15, 22), (9, 26), (7, 30)], BONE, 1.2)
    s.add(chain([(30, 32), (36, 36), (40, 34), (44, 38)], 0.9), IRON, flat=2)
    return s, 32


def phantom():
    s = Sprite('#05040a')
    cape = poly([(24, 10), (36, 16), (42, 44), (34, 40), (28, 46), (20, 40), (13, 46), (8, 40), (6, 44), (12, 16)])
    s.add(cape, SHADOW, soft=1.8)
    s.add(poly([(17, 16), (31, 16), (33, 34), (15, 34)]), VIOLET, soft=1.2)
    s.add(ellipse(24, 11, 6, 7), WHITE, soft=1)
    s.add(rect(15, 4, 33, 6) | rect(18, 0, 30, 5), ['#05040a', '#0e0c14', '#1a1724', '#2a2538'], flat=2)  # top hat
    s.px([(x, 3) for x in range(18, 30)], '#6a2a8a')
    s.add(poly([(24, 5), (30, 7), (30, 15), (24, 17)]), ['#8a8a94', '#c4c4cc', '#ececf0', '#ffffff'], flat=3)  # half mask
    s.px([(26, 10), (27, 10), (26, 11)], '#05040a'); s.px([(21, 10)], '#c86cff'); s.px([(22, 10)], '#c86cff')
    mouth(s, 23, 15, 'line', '#3a1a3a')
    s.px([(16, 34), (17, 35), (31, 34), (30, 35)], '#e0c060')
    return s, 34


def shade():
    s = Sprite('#020104')
    body = wavy_hem(24, 5, 11, 45, flare=6, tails=5, depth=6)
    s.add(body, SHADOW, soft=2.4, dither=True)
    hands(s, [(14, 22), (7, 26), (4, 33)], SHADOW, 2)
    s.px([(19, 15), (20, 15), (27, 15), (28, 15)], '#b48cff'); s.px([(19, 14), (28, 14)], '#6a4aa8')
    s.erase |= body & (yy > 36) & (NOISE > 0.55)
    return s, 26


def revenant():
    s = Sprite('#040608')
    s.add(wavy_hem(24, 24, 8, 45, flare=4, tails=3, depth=4), MIST, dither=True, soft=2)
    armor_torso(s, RUST, top=16, bottom=34)
    s.add(ellipse(24, 10, 5.5, 6), GREENSKIN, soft=1)
    s.add(poly([(17, 9), (31, 9), (30, 4), (24, 1), (18, 4)]), IRON, soft=1)  # helm
    s.px([(21, 10), (22, 10), (26, 10), (27, 10)], '#ff5a3a')
    s.add(chain([(36, 26), (40, 10), (42, 2)], 1.2, 0.8), IRON, flat=3)  # sword up
    s.add(rect(36, 24, 44, 26), RUST); s.add(ellipse(36, 27, 2.4, 2.4), GREENSKIN)
    s.add(chain([(14, 20), (10, 28), (11, 33)], 2), RUST)
    return s, 36


def banshee():
    s = Sprite('#08080e')
    body = woman(s, WHITE, hair_bottom=38, arms=False)
    hands(s, [(19, 20), (10, 14), (5, 8)], WHITE, 2)
    # wild white hair streaming upward
    hp = [(17, 8), (10, 2), (14, 9), (8, 6), (16, 14)]
    s.add(poly(hp) | poly(mirpts(hp)), MIST, bias=.2)
    eyes(s, 24, 11, 'hollow', gap=2); mouth(s, 24, 15, 'scream')
    sparkles(s, [(6, 20), (40, 22), (4, 30), (43, 14)], '#d4e8ff')
    return s, 32


def lost_soul():
    s = Sprite('#0a1020')
    s.add(ellipse(24, 26, 9, 9) | tail_body(24, 28, 6, 46, curl=1.4), PALE, soft=1.8, dither=True, bias=.15)
    eyes(s, 24, 24, 'tear', gap=2); mouth(s, 24, 30, 'frown')
    sparkles(s, [(12, 14), (36, 18), (30, 10), (14, 36)], '#bcd8ff')
    return s, 34


def vengeful_spirit():
    s = Sprite('#140406')
    s.add(wavy_hem(24, 6, 12, 44, flare=5, tails=5, depth=6), RED, soft=2, dither=True)
    hands(s, [(13, 22), (6, 18), (3, 12)], RED, 2.2)
    for side in (1, -1):  # claws
        X = (lambda x: x) if side == 1 else (lambda x: W - 1 - x)
        s.px([(X(1), 9), (X(2), 10), (X(3), 8), (X(4), 9), (X(5), 8)], '#ffe0c0')
    eyes(s, 24, 15, 'angry', '#ffec80', gap=4); mouth(s, 24, 22, 'grin', '#1a0204')
    return s, 32


def guardian_spirit():
    s = Sprite('#2a1a04')
    for side in (1, -1):  # wings
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(poly([(X(18), 18), (X(4), 6), (X(2), 16), (X(6), 26), (X(4), 30), (X(16), 28)]), GOLD, bias=.15, dither=True)
    s.add(robe(24, 8, 46, 7, 7, 4), ['#6a5a3a', '#a8946a', '#dccaa0', '#fff4d8', '#ffffff'], soft=1.6, bias=.1)
    s.add(ellipse(24, 13, 4.5, 5), SKIN_PALE)
    s.add(ellipse(24, 4, 6, 1.6) & ~ellipse(24, 4, 4, 0.8), GOLD, flat=4)  # halo
    eyes(s, 24, 12, 'glow', '#fff4b0', gap=2)
    s.add(chain([(31, 44), (34, 10)], 0.9), GOLD, flat=3); s.add(ellipse(34, 8, 2.2, 2.2), ['#fff8c0'] * 4, flat=3)
    return s, 36


def ancestral_spirit():
    s = Sprite('#06161a')
    s.add(robe(24, 6, 46, 9, 8, 4), TEAL, soft=1.8, dither=True)
    s.add(ellipse(24, 13, 5, 5.5), TEAL[1:] + ['#e0fff8'], soft=1)
    s.add(poly([(19, 16), (29, 16), (27, 27), (24, 30), (21, 27)]), ['#8ab8b0', '#bcdcd4', '#e4f4ee', '#ffffff'], bias=.2)  # beard
    s.px([(21, 12), (22, 12), (26, 12), (27, 12)], '#e0fff8')
    s.add(chain([(12, 44), (11, 6)], 1.1), RUST, bias=.1)
    s.add(ellipse(11, 5, 2.6, 2.6), ['#3a9a90', '#7cd8c8', '#c4fff0', '#ffffff'], flat=2)
    s.add(chain([(16, 24), (13, 26)], 1.8), TEAL)
    return s, 34


def crisis_apparition():
    s = Sprite('#0a1020')
    body = poly([(20, 10), (28, 10), (31, 30), (34, 46), (14, 46), (17, 30)])
    s.add(body, MIST, dither=True, soft=1.5)
    s.add(ellipse(24, 8, 4.5, 5), MIST, soft=1)
    s.add(chain([(28, 13), (37, 15), (44, 13)], 1.8, 1.3), MIST)  # reaching out to you
    s.add(chain([(20, 13), (17, 24), (18, 30)], 1.8, 1.3), MIST)
    s.px([(22, 8), (26, 8)], '#0a1020'); mouth(s, 24, 11, 'o')
    for y in range(0, 48, 3):  # it flickers: missing scanlines
        s.erase |= (yy > y) & (yy < y + 1) & (NOISE > 0.4)
    return s, 24


def doppelganger():
    s = Sprite('#06040a')
    # a copy of the adventurer, but grey and wrong
    s.add(rect(18, 33, 22, 46) | rect(26, 33, 30, 46), SHADOW, soft=1)
    s.add(poly([(16, 16), (32, 16), (33, 34), (15, 34)]), ['#2a2a32', '#4a4a56', '#6e6e7c', '#9a9aa8'], soft=1.2)
    s.add(chain([(16, 18), (12, 28), (12, 33)], 2.2), ['#2a2a32', '#4a4a56', '#6e6e7c', '#9a9aa8'])
    s.add(chain([(33, 18), (37, 26), (40, 20)], 2.2), ['#2a2a32', '#4a4a56', '#6e6e7c', '#9a9aa8'])
    s.add(chain([(40, 22), (44, 4)], 1), IRON, flat=3)  # a shortsword like yours
    s.add(ellipse(24, 10, 5.5, 6.5), ['#5a5a66', '#8a8a96', '#b4b4c0', '#d8d8e0'], soft=1)
    s.add(poly([(18, 8), (30, 8), (30, 4), (24, 2), (18, 4)]), ['#2a1a10', '#4a2e1a', '#6a4426', '#8a5a34'])
    s.px([(21, 10), (22, 10), (26, 10), (27, 10)], '#f0f0f0'); mouth(s, 24, 14, 'grin', '#0a0a10')
    return s, 47


def intelligent_spirit():
    s = Sprite('#0c0a20')
    s.add(robe(24, 10, 46, 9, 8, 4), VIOLET, dither=True, soft=1.8)
    s.add(ellipse(24, 12, 8, 7), ['#3a2a6a', '#6a4ab0', '#9a7ae0', '#ccb8ff', '#f4eaff'], soft=1.4)  # a big glowing head
    for x, y in [(19, 8), (24, 6), (29, 8), (21, 13), (27, 12)]:  # thought-lines on its brow
        s.px([(x, y), (x + 1, y)], '#f4eaff')
    eyes(s, 24, 14, 'glow', '#ffffff', gap=3)
    s.add(poly([(14, 26), (22, 28), (22, 34), (14, 32)]) | poly([(34, 26), (26, 28), (26, 34), (34, 32)]), ['#4a2a10', '#7a4a20', '#e8dcc0', '#fff8e8'], bias=.3)  # an open book
    sparkles(s, [(8, 6), (40, 8), (6, 20), (42, 22), (36, 2)], '#ccb8ff')
    return s, 34


def residual_haunting():
    s = Sprite('#101420')
    # a faded figure caught mid-step, repeating forever
    s.add(rect(19, 32, 22, 46) | chain([(27, 32), (30, 46)], 1.6), MIST, soft=1)
    s.add(poly([(17, 14), (31, 14), (32, 33), (16, 33)]), MIST, soft=1.2, dither=True)
    s.add(ellipse(24, 9, 4.5, 5.5), MIST)
    s.add(chain([(31, 16), (35, 26), (34, 30)], 1.8), MIST)
    s.add(chain([(30, 30), (31, 36)], 1), GOLD)  # carrying a candle
    s.px([(31, 28)], '#ffcf5a')
    for y in range(1, 48, 2):  # it's only an echo: every other line is missing
        s.erase |= (yy > y) & (yy < y + 1)
    return s, 6


def shadow_person():
    s = Sprite('#000000')
    body = poly([(20, 12), (28, 12), (30, 30), (29, 46), (26, 46), (24, 32), (22, 46), (19, 46), (18, 30)])
    s.add(body | ellipse(24, 8, 5, 6), SHADOW, flat=1)
    s.add(chain([(19, 14), (15, 26), (14, 34)], 1.6) | chain([(29, 14), (33, 26), (34, 34)], 1.6), SHADOW, flat=1)
    s.add(poly([(16, 6), (32, 6), (29, 3), (19, 3)]) | rect(19, 0, 29, 4), SHADOW, flat=2)  # a hat
    s.px([(22, 8), (26, 8)], '#ff2020'); s.px([(21, 8), (27, 8)], '#600808')
    s.erase |= (body & (yy > 40) & (NOISE > 0.5))
    return s, 30


def orb():
    s = Sprite('#06142a')
    s.add(ellipse(24, 24, 11, 11), BLUEFIRE, soft=2.6, bias=.15, dither=True)
    s.add(ellipse(24, 24, 6, 6), ['#62c4ff', '#a8e4ff', '#e4faff', '#ffffff'], soft=1.2, bias=.3, ao=False)
    s.px([(21, 20), (22, 20), (21, 21)], '#ffffff')
    for x, y in [(10, 10), (38, 12), (8, 36), (40, 38), (24, 6), (24, 42), (6, 24), (42, 24)]:
        s.px([(x, y)], '#8ad8ff')
    return s, 48


def ectoplasmic_spirit():
    s = Sprite('#04140a')
    body = wavy_hem(24, 6, 12, 40, flare=2, tails=4, depth=4)
    s.add(body, ECTO, soft=2, dither=True)
    for x, L in [(14, 6), (20, 3), (27, 7), (33, 4)]:  # slime dripping off it
        s.add(capsule(x, 38, x, 38 + L, 1.4, 1), ECTO, bias=.1)
    eyes(s, 24, 15, 'hollow', gap=4); mouth(s, 24, 22, 'o', '#0a2a10')
    s.px([(16, 12), (17, 11), (30, 26), (14, 30)], '#e8ffd0')
    return s, 48


def elemental_spirit():
    s = Sprite('#200604')
    body = ellipse(24, 18, 9, 10) | tail_body(24, 22, 7, 46, curl=-1.2, hw2=1)
    s.add(body, FIRE, soft=1.6, dither=True, bias=.1)
    for side in (1, -1):
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(poly([(X(17), 12), (X(13), 2), (X(20), 9)]), FIRE, bias=.25)
        s.add(chain([(X(16), 20), (X(9), 24), (X(6), 18)], 2, 1.2), FIRE)
    eyes(s, 24, 17, 'glow', '#fff8c0', gap=3, size=2)
    s.add(ellipse(24, 20, 3, 4), ['#ffd040', '#ffe880', '#fff8c0', '#ffffff'], flat=3, ao=False)
    eyes(s, 24, 16, 'glow', '#4a0c04', gap=3)
    return s, 40


def inhuman_spirit():
    s = Sprite('#020204')
    body = poly([(24, 4), (32, 10), (36, 26), (44, 46), (34, 40), (28, 46), (20, 40), (14, 46), (4, 46), (12, 26), (16, 10)])
    s.add(body, ['#0e0e12', '#1c1a22', '#2c2a36', '#423e4e'], dither=True, soft=2)
    for side in (1, -1):  # too-long arms with too many joints
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(14), 16), (X(6), 22), (X(10), 30), (X(3), 38), (X(5), 44)], 1.3, 0.7), ['#1c1a22', '#2c2a36', '#423e4e', '#5a566a'])
    s.add(ellipse(24, 13, 5, 6), ['#d8d4c8', '#e8e4d8', '#f4f0e8', '#ffffff'], flat=2)  # a blank white face
    s.px([(21, 12), (22, 12), (21, 13), (26, 12), (27, 12), (27, 13)], '#000000')
    mouth(s, 24, 17, 'line', '#000000')
    return s, 38


def demonic_entity():
    s = Sprite('#140000')
    s.add(wavy_hem(24, 10, 11, 45, flare=5, tails=4, depth=5), BLOODRED + ['#e04040'], soft=2, dither=True)
    for side in (1, -1):
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(17), 12), (X(11), 6), (X(10), 0)], 2, 0.6), BONE, bias=.1)  # horns
        s.add(chain([(X(14), 26), (X(6), 30), (X(3), 24)], 2.4, 1.4), BLOODRED + ['#e04040'])
        s.px([(X(2), 22), (X(3), 21), (X(4), 22)], '#ffe0b0')
    eyes(s, 24, 18, 'angry', '#ffff60', gap=4)
    mouth(s, 24, 25, 'grin', '#0a0000')
    s.px([(21, 26), (23, 26), (25, 26), (27, 26)], '#ffe8d0')
    sparkles(s, [(6, 40), (42, 42), (10, 44), (38, 36)], EMBER)
    return s, 34


def attachment_spirit():
    s = Sprite('#0a1020')
    s.add(ellipse(24, 20, 9, 8) | tail_body(24, 22, 6, 44, curl=-1), PALE, soft=1.8, dither=True)
    for side in (1, -1):  # it clings with long tendrils
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(17), 24), (X(8), 30), (X(4), 40), (X(8), 46)], 1.2, 0.5), PALE)
    eyes(s, 24, 18, 'glow', '#ff9ad0', gap=3, size=2); mouth(s, 24, 24, 'o')
    s.add(chain([(31, 20), (38, 14), (44, 16)], 0.8), IRON, flat=2)  # a chain it trails
    return s, 32


def portal_spirit():
    s = Sprite('#06041a')
    ring = ellipse(24, 22, 16, 16) & ~ellipse(24, 22, 11, 11)
    s.add(ring, VIOLET, soft=1.4, dither=True, bias=.1)
    s.add(ellipse(24, 22, 11, 11), ['#030210', '#0a0624', '#140c3a', '#201450'], flat=1, ao=False)
    s.add(ellipse(24, 22, 5, 3.4), ['#ffd040', '#ffe880', '#fff8c0', '#ffffff'], soft=1, ao=False)  # an eye inside
    s.add(ellipse(24, 22, 1.6, 3), ['#000000'] * 4, flat=0, ao=False)
    for a in range(0, 360, 45):  # sparks around the rim
        x, y = 24 + 18 * np.cos(np.radians(a)), 22 + 18 * np.sin(np.radians(a))
        s.px([(int(x), int(y))], '#c4aef0')
    s.add(chain([(14, 34), (8, 42), (12, 46)], 1.4, 0.6) | chain([(34, 34), (40, 42), (36, 46)], 1.4, 0.6), VIOLET)
    return s, 48


def yurei():
    s = Sprite('#08080e')
    woman(s, WHITE, hair_bottom=34)
    s.add(poly([(21, 4), (27, 4), (24, 8)]), ['#c8c8d0', '#e8e8ee', '#ffffff', '#ffffff'], flat=2)  # the triangle headband
    s.px([(22, 12), (26, 12)], '#08080e'); s.px([(22, 13), (26, 13)], '#08080e')
    s.add(poly([(19, 16), (29, 16), (27, 22), (21, 22)]), ['#a0a0ae', '#cacad4', '#e8e8ee', '#ffffff'])  # kimono collar
    s.px([(24, 17), (24, 18), (24, 19), (24, 20)], '#6a6a78')
    return s, 34


def onryo():
    s = Sprite('#140406')
    woman(s, ['#4a0a10', '#801820', '#b42c30', '#e05048', '#ff9080'], hair_bottom=40)
    s.px([(21, 12), (22, 12), (26, 12), (27, 12)], '#000000'); s.px([(22, 12), (26, 12)], '#ff2a2a')
    s.px([(20, 11), (28, 11)], '#000000'); mouth(s, 24, 15, 'frown', '#2a0004')
    s.add(rect(17, 28, 31, 31), ['#1a1418', '#2a2228', '#3a3038', '#4a3e48'])  # obi sash
    sparkles(s, [(8, 10), (40, 12), (6, 30), (42, 34)], '#ff6a4a')
    return s, 36


def yokai():
    s = Sprite('#140a04')
    # a one-eyed umbrella yokai hopping on one leg
    s.add(poly([(24, 2), (42, 18), (36, 17), (30, 19), (24, 17), (18, 19), (12, 17), (6, 18)]), ['#5a2a10', '#9a4a1c', '#d8742c', '#ffb050'], soft=1.2)
    for x in (12, 18, 24, 30, 36):
        s.px([(x, y) for y in range(18 - abs(24 - x) // 4, 18)], '#3a1a08')
    s.add(chain([(24, 18), (24, 38)], 1.1), RUST, flat=2)
    s.add(chain([(24, 38), (23, 44), (26, 46)], 1.8), ['#5a3a20', '#9a6a3a', '#d4a46a', '#f4d4a0'])
    s.add(ellipse(24, 9, 4, 3.4), ['#e8e8e8', '#f4f4f4', '#ffffff', '#ffffff'], flat=2, ao=False)
    s.add(ellipse(24, 9, 1.6, 2), ['#1a1a1a'] * 4, flat=0, ao=False)
    s.add(chain([(24, 13), (25, 16), (23, 19), (25, 22)], 1.2, 0.8), ['#801820', '#c02c30', '#e85048', '#ff8070'])  # its long tongue
    return s, 47


def dybbuk():
    s = Sprite('#06040e')
    s.add(ellipse(24, 16, 8, 9) | tail_body(24, 20, 6.5, 46, curl=1.6), ['#1c1430', '#36265a', '#56408a', '#7a64b0', '#a894d8'], soft=1.8, dither=True)
    hands(s, [(16, 20), (10, 18), (8, 12)], ['#1c1430', '#36265a', '#56408a', '#7a64b0'], 1.6)
    eyes(s, 24, 14, 'glow', '#ffe060', gap=3)
    mouth(s, 24, 20, 'scream', '#06040e')
    for x, y in [(6, 6), (40, 8), (38, 20)]:  # Hebrew-letter-like marks of the binding
        s.px([(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)], '#ffd060')
    return s, 30


def jinn():
    s = Sprite('#040a1a')
    s.add(tail_body(24, 26, 7, 46, curl=-1.6, hw2=1), SMOKE, dither=True, soft=2)
    s.add(poly([(15, 14), (33, 14), (31, 30), (17, 30)]), SMOKE, soft=1.3)
    for side in (1, -1):  # arms folded across its chest
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(15), 16), (X(11), 22), (X(21), 24), (X(30), 22)], 2.2, 1.8), SMOKE)
        s.add(ellipse(X(14.5), 16, 3.2, 1.2), GOLD, flat=3)  # gold armbands
    s.add(ellipse(24, 9, 5, 5.5), SMOKE, soft=1)
    s.add(ellipse(24, 4, 6.5, 3.4), ['#5a1a6a', '#8a2a9a', '#c04ac8', '#f08af0'], soft=1)  # turban
    s.add(ellipse(24, 3, 1.6, 1.6), ['#ff2a2a', '#ff6a6a', '#ffaaaa', '#ffffff'], flat=2)
    s.px([(22, 9), (26, 9)], '#fff8c0'); mouth(s, 24, 12, 'line', '#142040')
    s.add(poly([(22, 12), (26, 12), (25, 16), (23, 16)]), ['#0a1424', '#142040', '#1e2e58', '#2a3e70'])  # beard
    return s, 34


def ifrit():
    s = Sprite('#200400')
    s.add(tail_body(24, 26, 8, 46, curl=1.6, hw2=1), FIRE, dither=True, soft=1.6, bias=.1)
    s.add(poly([(14, 14), (34, 14), (31, 31), (17, 31)]), ['#3a0a04', '#7a1a08', '#b8340e', '#e86a24'], soft=1.2)
    for side in (1, -1):
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(14), 16), (X(7), 22), (X(6), 14)], 2.8, 2.2), ['#3a0a04', '#7a1a08', '#b8340e', '#e86a24'])
        s.add(ellipse(X(6), 12, 2.6, 2.6), FIRE, bias=.2)  # fists of flame
        s.add(chain([(X(19), 6), (X(15), 2), (X(16), 0)], 1.6, 0.6), ['#1a1010', '#3a2a24', '#5a4a40', '#8a7a6a'])  # horns
    s.add(ellipse(24, 9, 5.5, 5.5), ['#3a0a04', '#7a1a08', '#b8340e', '#e86a24'], soft=1)
    eyes(s, 24, 8, 'glow', '#fff070', gap=2); mouth(s, 24, 12, 'grin', '#200400')
    s.add(poly([(18, 4), (21, -2), (24, 3), (27, -2), (30, 4), (24, 6)]), FIRE, bias=.3)  # burning hair
    sparkles(s, [(4, 30), (44, 26), (10, 40), (40, 42)], EMBER)
    return s, 34


def draugr():
    s = Sprite('#040608')
    s.add(rect(18, 34, 22, 46) | rect(26, 34, 30, 46), ['#1e2a30', '#34464e', '#4e6670', '#6e8a94'])
    armor_torso(s, ['#2a2a24', '#4a4636', '#6e684e', '#948c6a'], top=16, bottom=36, hw=10)
    s.add(chain([(14, 20), (10, 30), (12, 36)], 2.4), ['#1e2a30', '#34464e', '#4e6670', '#6e8a94'])
    s.add(ellipse(36, 30, 6, 7), ['#3a2410', '#5a3a1c', '#7a5028', '#9a6a3a'], soft=1)  # round shield
    s.add(ellipse(36, 30, 1.8, 1.8), IRON, flat=3)
    s.add(ellipse(24, 10, 6, 6.5), ['#1e2a30', '#34464e', '#4e6670', '#6e8a94'], soft=1)  # bloated blue-grey
    s.add(poly([(17, 8), (31, 8), (29, 3), (24, 1), (19, 3)]) | rect(23, 8, 25, 13), IRON, soft=1)
    s.px([(21, 10), (22, 10), (26, 10), (27, 10)], '#9ff4ff')
    s.add(poly([(20, 14), (28, 14), (26, 20), (22, 20)]), ['#6a6a62', '#8a8a80', '#aaaaa0', '#ccccc0'], bias=.1)  # frosted beard
    sparkles(s, [(8, 8), (40, 12), (6, 24), (44, 44)], '#cff4ff')
    return s, 47


def mare():
    s = Sprite('#04020a')
    # a night hag crouched as if on a sleeper's chest
    s.add(ellipse(24, 32, 15, 10), ['#0c0814', '#1a1228', '#2a1e3c', '#3e2e56'], dither=True, soft=2)
    s.add(hair_curtain(24, 8, 9, 32), HAIR, flat=1)
    s.add(ellipse(24, 16, 5.5, 6), ['#3a4a3a', '#5a6e5a', '#7e967c', '#a8bea4'], soft=1)
    s.px([(21, 15), (22, 15), (26, 15), (27, 15)], '#ffe040'); s.px([(24, 18), (24, 19)], '#2a3a2a')
    mouth(s, 24, 21, 'grin', '#0a0a0a')
    for side in (1, -1):  # long fingers gripping
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(14), 28), (X(8), 36), (X(10), 42)], 1.6, 0.8), ['#3a4a3a', '#5a6e5a', '#7e967c', '#a8bea4'])
        s.px([(X(9), 43), (X(11), 44), (X(12), 43)], '#d8d0c0')
    for x, y in [(6, 6), (40, 4), (44, 18)]:
        s.px([(x, y), (x + 1, y)], '#e0e0ff')  # stars of a bad night
    return s, 47


def fetch():
    s = Sprite('#0a1020')
    # a pale double of the hero: a death omen
    s.add(rect(18, 33, 22, 46) | rect(26, 33, 30, 46), MIST, soft=1)
    s.add(poly([(16, 16), (32, 16), (33, 34), (15, 34)]), MIST, soft=1.2, dither=True)
    s.add(chain([(16, 18), (13, 28), (14, 33)], 2.1) | chain([(32, 18), (35, 28), (34, 33)], 2.1), MIST)
    s.add(ellipse(24, 10, 5.5, 6.5), MIST, soft=1)
    s.add(poly([(18, 8), (30, 8), (30, 4), (24, 2), (18, 4)]), PALE)
    eyes(s, 24, 9, 'hollow', gap=2)
    s.px([(23, 14), (24, 14)], '#3a4252')
    return s, 30


def wight():
    s = Sprite('#020406')
    s.add(robe(24, 12, 46, 8, 8, 5), ['#0c1014', '#1a2228', '#2a363e', '#3e4e58'], dither=True, soft=1.8)
    armor_torso(s, IRON, top=16, bottom=30, hw=8)
    s.add(ellipse(24, 10, 5, 6), BONE, soft=1)
    s.add(poly([(18, 6), (20, 1), (22, 5), (24, 0), (26, 5), (28, 1), (30, 6)]) | rect(18, 5, 31, 7), GOLD, soft=.8)  # a barrow-king's crown
    s.px([(21, 10), (22, 10), (26, 10), (27, 10)], '#000000'); s.px([(21, 10), (27, 10)], '#6affd0')
    s.px([(22, 14), (24, 14), (26, 14)], '#1a1a14')
    hands(s, [(16, 20), (9, 24), (5, 20)], BONE, 1.2)
    s.add(chain([(5, 22), (7, 44)], 1), IRON, flat=3)  # a long blade held point down
    return s, 34


def pontianak():
    s = Sprite('#0e0206')
    woman(s, WHITE, hair_bottom=40, arms=False)
    for side in (1, -1):  # arms raised, long nails
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(19), 20), (X(12), 16), (X(9), 8)], 1.8, 1.4), SKIN_PALE)
        s.px([(X(7), 4), (X(8), 5), (X(9), 4), (X(10), 5), (X(11), 4)], '#3a0a10')
    s.px([(21, 12), (22, 12), (26, 12), (27, 12)], '#ff1a1a')
    mouth(s, 24, 15, 'grin', '#3a0a10'); s.px([(22, 16), (26, 16)], '#ffffff')
    s.px([(22, 22), (23, 23), (26, 24), (21, 26)], '#a01020')  # bloodstains on the dress
    return s, 34


def preta():
    s = Sprite('#0a0e06')
    # a hungry ghost: a swollen belly, a needle-thin neck and a tiny mouth
    s.add(ellipse(24, 32, 11, 9) | tail_body(24, 36, 5, 46, curl=1, hw2=1), GREENSKIN, soft=1.8, dither=True, bias=.05)
    s.add(chain([(24, 23), (24, 14)], 1.1), GREENSKIN)
    s.add(ellipse(24, 10, 5, 5.5), GREENSKIN, soft=1)
    for side in (1, -1):
        X = (lambda x: x) if side == 1 else (lambda x: W - x)
        s.add(chain([(X(15), 28), (X(9), 22), (X(8), 14)], 1, 0.7), GREENSKIN)
    s.px([(21, 9), (22, 9), (26, 9), (27, 9)], '#ffe080'); s.px([(21, 10), (27, 10)], '#000000')
    s.px([(24, 13)], '#000000')
    s.px([(x, 30) for x in range(18, 30, 3)] + [(x, 34) for x in range(17, 31, 4)], '#22322a')  # ribs on the belly
    return s, 38


def la_llorona():
    s = Sprite('#06080e')
    woman(s, WHITE, hair_bottom=36)
    s.add(poly([(17, 4), (31, 4), (34, 22), (31, 16), (17, 16), (14, 22)]) & ~ellipse(24, 12.5, 5, 6), ['#8a8a9a', '#b8b8c8', '#dcdce8', '#f8f8ff'], dither=True, bias=.2)  # veil
    eyes(s, 24, 11, 'tear', gap=2); mouth(s, 24, 15, 'frown')
    s.add(ellipse(24, 46, 18, 3), ['#0a2a4a', '#164a7a', '#2a72a8', '#5aa4d4'], dither=True, flat=1, ao=False)  # the river at her feet
    sparkles(s, [(10, 46), (36, 45), (20, 47)], '#c8ecff')
    return s, 30


def will_o_wisp():
    s = Sprite('#04102a')
    s.add(ellipse(24, 18, 7, 7) | tail_body(24, 20, 5, 44, curl=-1.4, hw2=0.6), BLUEFIRE, soft=1.6, dither=True, bias=.2)
    s.add(ellipse(24, 18, 3.4, 3.4), ['#a8e4ff', '#e4faff', '#ffffff', '#ffffff'], flat=2, ao=False)
    for x, y in [(12, 8), (36, 10), (10, 28), (38, 30), (30, 4), (16, 40)]:
        s.px([(x, y)], '#62c4ff')
    s.px([(14, 6), (34, 8)], '#ffffff')
    return s, 44


def dullahan():
    s = Sprite('#020204')
    s.add(robe(24, 16, 46, 9, 8, 4), ['#08080c', '#141420', '#22222e', '#343444'], soft=1.6, dither=True)
    armor_torso(s, IRON, top=10, bottom=30, hw=9)
    s.px([(22, 10), (23, 10), (24, 10), (25, 10), (26, 10)], '#5a0a10')  # no head: just the neck
    s.add(ellipse(24, 9, 3, 1), BLOODRED)
    # it holds its own glowing head under one arm
    s.add(chain([(32, 14), (36, 22), (32, 28)], 2.2), IRON)
    s.add(ellipse(34, 26, 5, 5.5), ['#3a4a3a', '#5a6e5a', '#7e967c', '#a8bea4'], soft=1)
    s.px([(32, 25), (33, 25), (36, 25), (37, 25)], '#ffe040'); mouth(s, 35, 29, 'grin', '#0a0a0a')
    s.add(chain([(14, 12), (8, 4), (6, 2)], 1.2) | chain([(8, 4), (5, 14)], 0.8), BONE, bias=.1)  # a whip of spine
    return s, 40


def psychopomp():
    s = Sprite('#04040a')
    s.add(robe(24, 4, 46, 10, 9, 5), ['#0e0c16', '#1c1a2a', '#2e2a42', '#443e5e', '#5e5680'], dither=True, soft=2)
    s.add(poly([(20, 10), (28, 10), (31, 18), (24, 26), (17, 18)]), ['#2a2418', '#4a4030', '#8a7a58', '#d8c89a'], soft=1)  # a raven mask
    s.add(poly([(22, 18), (26, 18), (24, 30)]), ['#4a4030', '#8a7a58', '#c8b888', '#efe4c0'], bias=.2)  # the beak
    s.px([(21, 14), (22, 14), (26, 14), (27, 14)], '#7ff0ff')
    s.add(chain([(36, 24), (38, 32)], 0.8), IRON, flat=2)
    s.add(rect(35, 32, 42, 40), GOLD, soft=.8)  # a lantern to guide souls
    s.add(ellipse(38.5, 36, 2, 2.4), ['#7ff0ff', '#bff8ff', '#ffffff', '#ffffff'], flat=2, ao=False)
    s.add(chain([(31, 22), (36, 25)], 2), ['#0e0c16', '#1c1a2a', '#2e2a42', '#443e5e'])
    sparkles(s, [(8, 30), (6, 16), (12, 8), (44, 10)], '#7ff0ff')
    return s, 38


ALL = {
    'apparition': apparition, 'poltergeist': poltergeist, 'specter': specter, 'phantom': phantom, 'shade': shade,
    'revenant': revenant, 'banshee': banshee, 'lostsoul': lost_soul, 'vengefulspirit': vengeful_spirit,
    'guardianspirit': guardian_spirit, 'ancestralspirit': ancestral_spirit, 'crisisapparition': crisis_apparition,
    'doppelganger': doppelganger, 'intelligentspirit': intelligent_spirit, 'residualhaunting': residual_haunting,
    'shadowperson': shadow_person, 'orb': orb, 'ectoplasmicspirit': ectoplasmic_spirit, 'elementalspirit': elemental_spirit,
    'inhumanspirit': inhuman_spirit, 'demonicentity': demonic_entity, 'attachmentspirit': attachment_spirit,
    'portalspirit': portal_spirit, 'yurei': yurei, 'onryo': onryo, 'yokai': yokai, 'dybbuk': dybbuk, 'jinn': jinn,
    'ifrit': ifrit, 'draugr': draugr, 'mare': mare, 'fetch': fetch, 'wight': wight, 'pontianak': pontianak,
    'preta': preta, 'lallorona': la_llorona, 'willowisp': will_o_wisp, 'dullahan': dullahan, 'psychopomp': psychopomp,
}

if __name__ == '__main__':
    out, imgs = {}, []
    for k, f in ALL.items():
        s, fade_from = f()
        im = s.render()
        if fade_from < 47:
            im = fade_alpha(im, fade_from)
        imgs.append(im)
        buf = io.BytesIO(); im.save(buf, 'PNG')
        out[k] = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    sheet(imgs, scale=4, cols=8).save('ghosts.png')
    json.dump(out, open('ghosts.json', 'w'))
    print(len(out), 'ghosts')
