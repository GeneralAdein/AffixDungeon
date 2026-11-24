"""Oozes, slimes and jellies: 59 sprites for the 'ooze' family.

Every ooze is a short description (a body shape, a palette, a face, how see-through it is,
and a list of extras like bubbles, drips, a crown, bones inside, crystals or many eyes)
and one builder draws them all, so they share a look but each is its own thing.

    python3 oozes.py      # writes oozes.png (preview sheet) and oozes.json (data URIs)
"""
import base64, io, json
import numpy as np
from pxlib import *

rng = np.random.default_rng(11)

P = {  # palettes, dark to light
    'green': ['#123a14', '#1f6a24', '#3aa03a', '#78d860', '#c8ff9c'],
    'lime': ['#2a4a08', '#4e7e10', '#86b81c', '#c4e84a', '#f0ffa0'],
    'gray': ['#2a2c30', '#4a4e54', '#727880', '#a0a6ae', '#d0d4d8'],
    'ochre': ['#4a2e08', '#7e5212', '#b8821e', '#e4b448', '#fff0a0'],
    'black': ['#050508', '#0e0e14', '#1a1a24', '#2c2c3a', '#4a4a60'],
    'clear': ['#2a5a5a', '#4a8a88', '#7cbab4', '#b0e4dc', '#e8fffa'],
    'acid': ['#2a4a00', '#4e8a00', '#86d000', '#c4ff3a', '#f4ffb0'],
    'toxic': ['#1e3a10', '#3a6a14', '#62a01a', '#9ad83a', '#d8ff8a'],
    'purple': ['#2a0c3a', '#4e1a6a', '#7a32a0', '#ac62d0', '#e4b0ff'],
    'blood': ['#30040a', '#5c0a14', '#8e1622', '#c83038', '#ff7a6a'],
    'lava': ['#3a0a02', '#801a04', '#d0400a', '#ff8a1a', '#fff06a'],
    'frost': ['#1a3a5a', '#2e6694', '#5aa0d0', '#a4dcf8', '#f0fcff'],
    'shadow': ['#04030a', '#0c0a18', '#1a1430', '#2c2250', '#463878'],
    'arcane': ['#140a40', '#28187a', '#4a32c0', '#7e6aff', '#d0c4ff'],
    'venom': ['#2a0c30', '#541a5a', '#8a2e86', '#c45ab8', '#ffaaf0'],
    'tar': ['#030303', '#0a0a0a', '#151515', '#242424', '#3c3c3c'],
    'mud': ['#2a1a0c', '#4a3018', '#6e4a26', '#94683a', '#bc9060'],
    'sludge': ['#1e2214', '#363c22', '#545c34', '#78804a', '#a4aa70'],
    'plague': ['#2a2a0a', '#4e4a14', '#7a7022', '#aca040', '#e0d47a'],
    'ecto': ['#0c3a20', '#1a6a3a', '#30a858', '#6ae08a', '#c4ffd4'],
    'necro': ['#0e1a14', '#1e3428', '#34523e', '#527a5a', '#86ac86'],
    'crystal': ['#2a1a4a', '#4a3a8a', '#7a6ad0', '#b4a8ff', '#f4f0ff'],
    'metal': ['#2a2e34', '#4e545e', '#7c848e', '#b4bcc4', '#f0f4f8'],
    'silver': ['#3a4048', '#6a727c', '#a0a8b0', '#d4dae0', '#ffffff'],
    'magma': ['#200602', '#5a1004', '#a82a08', '#f0601a', '#ffd04a'],
    'sewer': ['#1e2210', '#3a3e1c', '#5c602c', '#868a46', '#b8b870'],
    'swamp': ['#0e2a1e', '#1a4a32', '#2e6e4a', '#4e9a66', '#86c890'],
    'abyss': ['#02020a', '#060a24', '#0c1648', '#18287a', '#3a52b0'],
    'void': ['#000000', '#05030c', '#0c0818', '#16102a', '#241a44'],
    'psychic': ['#3a0a3a', '#6a1a6a', '#a42e9a', '#e05ac8', '#ffb0f0'],
    'flesh': ['#4a1a1a', '#7a2e2a', '#b0504a', '#dc8478', '#ffc0b0'],
    'bone': ['#4a4436', '#7a7260', '#aaa28c', '#d8d0b8', '#fffaea'],
    'parasite': ['#2a1a2a', '#4e2e4a', '#7a4a6e', '#aa7498', '#dcaac8'],
    'pink': ['#4a1a3a', '#7e2e60', '#b84a8e', '#e47ab8', '#ffc0e4'],
    'amber': ['#4a2200', '#8a4200', '#c86e08', '#f0a42a', '#ffdc80'],
    'sap': ['#3a2a04', '#6a5010', '#a07e22', '#d0b046', '#f8e48a'],
    'quick': ['#4a525c', '#7c8692', '#b0bac4', '#e0e8ee', '#ffffff'],
    'chaos': ['#3a0a2a', '#7a1a3a', '#c03a2a', '#f0a020', '#fff070'],
    'royal': ['#0a2a4a', '#14487a', '#2a72b0', '#5aa8e0', '#b0e0ff'],
    'queen': ['#3a0a3a', '#6a1462', '#a02a90', '#d85ac0', '#ffb0ec'],
    'primordial': ['#0a1a10', '#123a20', '#1e5a2e', '#36844a', '#6abc72'],
    'teal': ['#0a3034', '#145a5e', '#24888a', '#4cbcb4', '#a8f0e4'],
}
GOLD = ['#4a3008', '#8a5c10', '#c89424', '#f0cc5a', '#fff2b0']
BONE = P['bone'][:4]
IRON = ['#2a2e34', '#4e545e', '#7c848e', '#b4bcc4']


def body_mask(shape, cx=24, base=44):
    if shape == 'puddle':
        return ellipse(cx, base - 4, 19, 7) | ellipse(cx, base - 8, 12, 7)
    if shape == 'tiny':
        return (ellipse(cx, base - 7, 9, 8) & (yy < base)) | ellipse(cx, base - 2, 11, 3)
    if shape == 'tall':
        return (ellipse(cx, base - 18, 12, 20) & (yy < base)) | ellipse(cx, base - 2, 15, 3.5)
    if shape == 'mound':
        return (ellipse(cx, base - 16, 21, 20) & (yy < base)) | ellipse(cx, base - 2, 23, 4)
    if shape == 'cube':
        return rect(cx - 15, base - 30, cx + 15, base)
    if shape == 'drop':
        return (ellipse(cx, base - 9, 11, 10) & (yy < base)) | poly([(cx - 6, base - 16), (cx + 6, base - 16), (cx + 1, base - 30)]) | ellipse(cx, base - 2, 13, 3)
    if shape == 'humanoid':
        return (ellipse(cx, base - 26, 9, 9) | poly([(cx - 10, base - 22), (cx + 10, base - 22), (cx + 13, base), (cx - 13, base)])
                | chain([(cx - 9, base - 22), (cx - 16, base - 12), (cx - 15, base - 4)], 3.4, 2.6)
                | chain([(cx + 9, base - 22), (cx + 16, base - 12), (cx + 15, base - 4)], 3.4, 2.6))
    if shape == 'hydra':
        m = (ellipse(cx, base - 9, 16, 11) & (yy < base)) | ellipse(cx, base - 2, 18, 3)
        return m
    if shape == 'mass':
        return (ellipse(cx - 8, base - 10, 11, 10) | ellipse(cx + 8, base - 12, 12, 12) | ellipse(cx, base - 20, 10, 10)) & (yy < base) | ellipse(cx, base - 2, 20, 3.5)
    return (ellipse(cx, base - 12, 16, 14) & (yy < base)) | ellipse(cx, base - 2, 18, 3.5)  # blob


def face_y(shape, base=44):
    return {'puddle': base - 10, 'tiny': base - 9, 'tall': base - 24, 'mound': base - 24, 'cube': base - 20, 'drop': base - 11,
            'humanoid': base - 27, 'hydra': base - 12, 'mass': base - 21}.get(shape, base - 16)


def draw_eyes(s, cx, y, kind, color):
    if kind == 'none':
        return
    if kind == 'dots':
        s.px([(cx - 4, y), (cx - 4, y + 1), (cx + 3, y), (cx + 3, y + 1)], '#08080c')
        s.px([(cx - 4, y)], '#ffffff'); s.px([(cx + 3, y)], '#ffffff')
    elif kind == 'big':
        for x in (cx - 6, cx + 2):
            s.px([(x + i, y + j) for i in range(4) for j in range(4) if not (i in (0, 3) and j in (0, 3))], '#f4f4f4')
            s.px([(x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2), (x + 2, y + 2)], '#08080c')
            s.px([(x + 1, y + 1)], '#ffffff')
    elif kind == 'glow':
        s.px([(cx - 5, y), (cx - 4, y), (cx + 3, y), (cx + 4, y)], color)
    elif kind == 'angry':
        s.px([(cx - 6, y - 1), (cx - 5, y), (cx - 4, y), (cx + 3, y), (cx + 4, y), (cx + 5, y - 1)], '#08080c')
        s.px([(cx - 5, y + 1), (cx - 4, y + 1), (cx + 3, y + 1), (cx + 4, y + 1)], color)
    elif kind == 'one':
        s.px([(cx - 2 + i, y - 1 + j) for i in range(5) for j in range(5) if (i - 2) ** 2 + (j - 2) ** 2 <= 5], '#f4f0e0')
        s.px([(cx - 1, y), (cx, y), (cx - 1, y + 1), (cx, y + 1), (cx, y + 2)], color)
    elif kind == 'many':
        for (x, yy_) in [(cx - 8, y + 2), (cx - 3, y - 2), (cx + 4, y), (cx + 9, y + 4), (cx - 10, y + 8), (cx + 1, y + 6), (cx + 6, y + 10), (cx - 5, y + 11)]:
            s.px([(x, yy_), (x + 1, yy_), (x, yy_ + 1), (x + 1, yy_ + 1)], '#f4f0e0'); s.px([(x + 1, yy_ + 1)], color)


def draw_mouth(s, cx, y, kind, color='#08080c'):
    if kind == 'none':
        return
    if kind == 'smile':
        s.px([(cx - 3, y), (cx - 2, y + 1), (cx - 1, y + 1), (cx, y + 1), (cx + 1, y + 1), (cx + 2, y)], color)
    elif kind == 'o':
        s.px([(cx - 1, y), (cx, y), (cx - 1, y + 1), (cx, y + 1)], color)
    elif kind == 'fangs':
        s.px([(x, y) for x in range(cx - 5, cx + 5)] + [(x, y + 1) for x in range(cx - 4, cx + 4)], color)
        s.px([(cx - 4, y + 1), (cx - 1, y + 1), (cx + 2, y + 1)], '#f4f0e0')
    elif kind == 'gape':
        for yy_ in range(y, y + 5):
            w = 3 if yy_ in (y, y + 4) else 5
            s.px([(x, yy_) for x in range(cx - w, cx + w)], color)
        s.px([(cx - 4, y + 1), (cx - 2, y + 1), (cx + 1, y + 1), (cx + 3, y + 1), (cx - 3, y + 3), (cx + 2, y + 3)], '#f4f0e0')
    elif kind == 'many':
        for (x, yy_) in [(cx - 9, y + 4), (cx + 5, y + 2), (cx - 2, y + 8), (cx + 8, y + 9)]:
            s.px([(x, yy_), (x + 1, yy_), (x + 2, yy_), (x + 3, yy_)], color); s.px([(x + 1, yy_ - 1), (x + 3, yy_ + 1)], '#f4f0e0')


def build(spec):
    shape = spec.get('shape', 'blob'); pal = P[spec['pal']]; cx = 24; base = 45
    s = Sprite(spec.get('outline', '#060608'))
    m = body_mask(shape, cx, base)
    extras = spec.get('x', [])
    if 'tentacles' in extras:
        for side in (1, -1):
            X = (lambda x: x) if side == 1 else (lambda x: W - x)
            s.add(chain([(X(12), base - 10), (X(5), base - 16), (X(3), base - 26), (X(7), base - 32)], 2.2, 0.7), pal, bias=.05)
    if shape == 'hydra':
        n = spec.get('heads', 3)
        for i in range(n):
            t = (i + 0.5) / n
            hx = cx - 14 + 28 * t; hy = base - 28 - 8 * np.sin(np.pi * t)
            s.add(chain([(cx - 6 + 12 * t, base - 14), (hx + (2 if t < .5 else -2), hy + 8), (hx, hy)], 3, 2.2), pal, soft=1.2)
            s.add(ellipse(hx, hy, 4, 3.4), pal, soft=1)
            s.px([(int(hx) - 2, int(hy) - 1), (int(hx) + 1, int(hy) - 1)], spec.get('eyec', '#ffe040'))
            s.px([(int(hx) - 1, int(hy) + 2), (int(hx), int(hy) + 2)], '#08080c')
    s.add(m, pal, soft=spec.get('soft', 2.2), dither=spec.get('dither', True), bias=spec.get('bias', 0.05))
    inner = ndimage.binary_erosion(m, iterations=3)
    content = np.zeros((W, W), bool)
    def inside(mask, ramp, **kw):
        nonlocal content
        mask = mask & inner; content |= mask; s.add(mask, ramp, **kw)
    # things inside a see-through body
    if 'skull' in extras:
        inside(ellipse(cx - 3, base - 10, 4, 3.6), BONE, soft=1)
        s.px([(cx - 5, base - 10), (cx - 2, base - 10)], '#1a1a14')
    if 'bones' in extras:
        inside(chain([(cx + 2, base - 6), (cx + 10, base - 12)], 1.1), BONE)
        inside(chain([(cx - 12, base - 14), (cx - 6, base - 7)], 1.1), BONE)
    if 'sword' in extras:
        inside(chain([(cx + 6, base - 4), (cx + 12, base - 22)], 0.9), IRON, flat=3)
        inside(rect(cx + 4, base - 7, cx + 10, base - 5), GOLD)
    if 'coins' in extras:
        for (x, y) in [(cx - 9, base - 5), (cx - 4, base - 4), (cx + 5, base - 6), (cx + 9, base - 3)]:
            inside(ellipse(x, y, 1.8, 1.3), GOLD, flat=3)
    if 'insect' in extras:
        inside(ellipse(cx + 3, base - 12, 3, 2) | chain([(cx + 1, base - 13), (cx - 2, base - 16)], 0.6) | chain([(cx + 5, base - 13), (cx + 8, base - 16)], 0.6), ['#1a0e04', '#3a2210', '#5a3a1c', '#7a5428'])
    if 'brain' in extras:
        inside(ellipse(cx, base - 16, 7, 5.5), P['pink'], soft=1)
        for x in range(cx - 5, cx + 6, 3): s.px([(x, base - 18), (x + 1, base - 16)], '#7e2e60')
    if 'nucleus' in extras:
        inside(ellipse(cx + 2, base - 13, 4.5, 4.5), spec.get('nuc', P['purple']), soft=1)
    if 'veins' in extras:
        for pts in [[(cx - 10, base - 6), (cx - 5, base - 14), (cx - 7, base - 22)], [(cx + 9, base - 5), (cx + 4, base - 12), (cx + 8, base - 20)]]:
            s.maskpx(chain(pts, 0.5) & m, '#5c0a14')
    if 'runes' in extras:
        for (x, y) in [(cx - 8, base - 8), (cx + 5, base - 6), (cx - 2, base - 4)]:
            s.px([(x, y), (x + 1, y), (x + 2, y), (x + 1, y - 1), (x + 1, y + 1)], '#d0c4ff')
    if 'stars' in extras:
        ys, xs = np.nonzero(inner)
        for i in rng.choice(len(xs), 9, replace=False): s.px([(xs[i], ys[i])], '#e8e0ff')
    if 'spots' in extras:
        ys, xs = np.nonzero(inner)
        for i in rng.choice(len(xs), 7, replace=False): s.px([(xs[i], ys[i]), (xs[i] + 1, ys[i])], spec.get('spotc', '#2a2a0a'))
    if 'bubbles' in extras:
        ys, xs = np.nonzero(inner & (yy < base - 4))
        for i in rng.choice(len(xs), 5, replace=False):
            s.px([(xs[i], ys[i]), (xs[i] + 1, ys[i]), (xs[i], ys[i] + 1)], pal[4])
    if 'chaos' in extras:
        for c, pts in [('#40a0ff', [(cx - 10, base - 10), (cx - 4, base - 18)]), ('#40ff80', [(cx + 2, base - 6), (cx + 9, base - 14)]), ('#c040ff', [(cx - 2, base - 20), (cx + 6, base - 22)])]:
            s.maskpx(chain(pts, 1.2) & m, c)
    # on the surface
    if 'drips' in extras:
        for x in (cx - 9, cx - 2, cx + 6, cx + 11):
            L = int(rng.integers(3, 6))
            s.add(capsule(x, base - 4, x, base - 4 + L, 1.3, 0.9) & (yy < 48), pal, bias=.05)
    if 'spikes' in extras or 'crystals' in extras:
        cr = P['crystal'] if 'crystals' in extras else pal
        for (x, y, h) in [(cx - 10, base - 18, 8), (cx - 2, base - 25, 11), (cx + 8, base - 20, 9), (cx + 14, base - 10, 6), (cx - 15, base - 8, 6)]:
            s.add(poly([(x - 2.5, y + 3), (x + 2.5, y + 3), (x, y - h)]), cr, bias=.2, soft=.6)
    if 'flames' in extras:
        for (x, y) in [(cx - 9, base - 22), (cx + 1, base - 27), (cx + 10, base - 20)]:
            s.add(poly([(x - 3, y + 4), (x + 3, y + 4), (x + 1, y - 5), (x, y - 1), (x - 1, y - 6)]), P['lava'], bias=.3)
    if 'icicles' in extras:
        for x in range(cx - 13, cx + 14, 5):
            s.add(poly([(x - 1.5, base - 3), (x + 1.5, base - 3), (x, base + 3)]), P['frost'], bias=.3)
        for (x, y) in [(cx - 8, base - 24), (cx + 6, base - 25)]:
            s.add(poly([(x - 2, y + 2), (x + 2, y + 2), (x, y - 5)]), P['frost'], bias=.3)
    if 'crown' in extras or 'tiara' in extras:
        y = {'mound': base - 37, 'tall': base - 39}.get(shape, base - 27)
        if 'crown' in extras:
            s.add(poly([(cx - 8, y + 4), (cx - 8, y - 3), (cx - 5, y + 1), (cx - 2, y - 5), (cx, y), (cx + 2, y - 5), (cx + 5, y + 1), (cx + 8, y - 3), (cx + 8, y + 4)]), GOLD, soft=.8)
            s.px([(cx - 2, y - 1), (cx + 2, y + 1)], '#ff3040'); s.px([(cx - 6, y + 1)], '#40a0ff')
        else:
            s.add(poly([(cx - 7, y + 4), (cx - 4, y), (cx, y - 5), (cx + 4, y), (cx + 7, y + 4)]), GOLD, soft=.8)
            s.px([(cx, y - 1)], '#ff60d0')
    if 'shell' in extras:  # a slime crawler's snail shell
        s.add(ellipse(cx + 5, base - 15, 9, 8), P['mud'], soft=1.2)
        for r_ in (6, 3): s.maskpx(ellipse(cx + 5, base - 15, r_, r_ * .9) & ~ellipse(cx + 5, base - 15, r_ - 1, r_ * .9 - 1), '#2a1a0c')
    if 'disguise' in extras:  # a mimic slime pretending to be a treasure chest
        s.add(rect(cx - 12, base - 22, cx + 12, base - 8), ['#3a2410', '#5a3a1c', '#7a5028', '#9a6a3a'], soft=1)
        s.add(rect(cx - 12, base - 16, cx + 12, base - 14), GOLD, flat=2)
        s.add(rect(cx - 2, base - 17, cx + 2, base - 12), GOLD, flat=3)
    if 'shine' not in spec.get('no', []):
        ys, xs = np.nonzero(m)
        top = ys.min(); left = xs[ys == top].min()
        hx, hy = (xs.min() + 4 if shape == 'cube' else cx - 8), (top + 4)
        s.px([(hx, hy), (hx + 1, hy), (hx, hy + 1), (hx + 2, hy - 1 if shape != 'cube' else hy)], spec.get('shinec', '#ffffff'))
    fy = spec.get('fy', face_y(shape, base)); fx = spec.get('fx', cx)
    draw_eyes(s, fx, fy, spec.get('eyes', 'dots'), spec.get('eyec', '#ffe040'))
    draw_mouth(s, fx, fy + 5, spec.get('mouth', 'none'), spec.get('mouthc', '#08080c'))
    img = s.render()
    a = spec.get('alpha')
    if a:  # see-through jelly: the body lets light through, what's inside stays solid
        arr = np.array(img)
        sel = m & ~content
        arr[..., 3] = np.where(sel & (arr[..., 3] == 255), a, arr[..., 3])
        img = Image.fromarray(arr, 'RGBA')
    return img


SPECS = {
    # floor 1
    'greenslime': dict(pal='green', x=['bubbles'], mouth='smile'),
    'sewerslime': dict(pal='sewer', x=['drips', 'spots'], eyes='glow', eyec='#e0e060', mouth='o'),
    'jellyspawn': dict(pal='pink', shape='tiny', x=['bubbles'], eyes='big', mouth='o', alpha=210),
    'slimecrawler': dict(pal='lime', shape='puddle', x=['shell'], eyes='dots', fx=16, fy=34),
    'livingsap': dict(pal='sap', shape='drop', x=['drips', 'bubbles'], mouth='smile', alpha=225),
    # floor 2
    'ooze': dict(pal='teal', x=['bubbles', 'drips'], eyes='dots', mouth='o'),
    'grayooze': dict(pal='gray', shape='puddle', x=['spots'], spotc='#3a3e44', eyes='glow', eyec='#d0f0ff'),
    'swampooze': dict(pal='swamp', x=['spots', 'drips'], spotc='#0e2a1e', eyes='glow', eyec='#e8ff60', mouth='o'),
    'acidslime': dict(pal='acid', x=['bubbles', 'drips'], eyes='angry', eyec='#ffff80', mouth='fangs'),
    'livingresin': dict(pal='amber', shape='drop', x=['insect'], eyes='dots', alpha=200),
    'toxicsludge': dict(pal='toxic', shape='puddle', x=['bubbles', 'skull'], eyes='glow', eyec='#f0ff40'),
    # floor 3
    'ochrejelly': dict(pal='ochre', shape='mass', x=['bubbles'], eyes='dots', alpha=225),
    'mudelemental': dict(pal='mud', shape='humanoid', x=['spots'], spotc='#2a1a0c', eyes='glow', eyec='#ffd060', mouth='o', soft=1.6),
    'venomjelly': dict(pal='venom', shape='tall', x=['nucleus', 'drips'], nuc=P['toxic'], eyes='dots', alpha=205),
    'tarmonster': dict(pal='tar', shape='humanoid', x=['bubbles', 'drips'], eyes='glow', eyec='#ff7a1a', mouth='gape', mouthc='#ff4a0a', soft=1.6),
    'frostslime': dict(pal='frost', x=['icicles'], eyes='dots', mouth='o', shinec='#ffffff'),
    'boneslime': dict(pal='clear', x=['skull', 'bones'], eyes='none', alpha=170),
    'mimicslime': dict(pal='purple', x=['disguise'], eyes='none', mouth='none', fy=26),
    # floor 4
    'gelatinouscube': dict(pal='clear', shape='cube', x=['skull', 'sword', 'coins'], eyes='none', alpha=150, dither=False),
    'corrosiveooze': dict(pal='acid', shape='mound', x=['drips', 'bubbles'], eyes='glow', eyec='#ffffff', mouth='gape', mouthc='#1a3000'),
    'bloodooze': dict(pal='blood', x=['veins', 'bubbles'], eyes='glow', eyec='#ffd0c0', mouth='fangs', mouthc='#200204'),
    'lavaslime': dict(pal='lava', x=['flames', 'bubbles'], eyes='glow', eyec='#fff8c0', mouth='smile', mouthc='#3a0a02'),
    'plagueslime': dict(pal='plague', x=['spots', 'drips', 'bones'], spotc='#3a2a0a', eyes='glow', eyec='#c0ff40', mouth='o'),
    'livingtar': dict(pal='tar', shape='mound', x=['bubbles', 'drips'], eyes='glow', eyec='#ffffff'),
    'sludgelurker': dict(pal='sludge', shape='puddle', x=['spots'], spotc='#1e2214', eyes='one', eyec='#ff3a1a'),
    # floor 5
    'blackpudding': dict(pal='black', shape='mound', x=['bubbles', 'drips'], eyes='none', mouth='none', shinec='#8a8aa0'),
    'crystalslime': dict(pal='crystal', x=['crystals'], eyes='big', mouth='smile', alpha=215),
    'ectoplasmicooze': dict(pal='ecto', shape='tall', x=['drips', 'skull'], eyes='glow', eyec='#e0fff0', alpha=180),
    'necroticslime': dict(pal='necro', x=['bones', 'drips', 'spots'], spotc='#0e1a14', eyes='glow', eyec='#60ff90', mouth='fangs'),
    'parasiticooze': dict(pal='parasite', shape='mass', x=['nucleus', 'veins', 'tentacles'], nuc=P['blood'], eyes='one', eyec='#ffe040'),
    'sludgebeast': dict(pal='sludge', shape='mound', x=['drips', 'spots'], spotc='#1e2214', eyes='angry', eyec='#ffb020', mouth='fangs'),
    'livingacid': dict(pal='acid', shape='drop', x=['bubbles', 'drips'], eyes='angry', eyec='#ffffff', alpha=200),
    # floor 6
    'shadowooze': dict(pal='shadow', x=['drips'], eyes='glow', eyec='#b48cff', mouth='none', shinec='#6a5aa0'),
    'arcaneooze': dict(pal='arcane', x=['runes', 'bubbles'], eyes='glow', eyec='#ffffff', alpha=215),
    'metallicooze': dict(pal='metal', x=['spikes'], eyes='dots', no=[], shinec='#ffffff'),
    'livingquicksilver': dict(pal='quick', shape='drop', x=['bubbles'], eyes='glow', eyec='#2a3a4a', shinec='#ffffff'),
    'fleshooze': dict(pal='flesh', shape='mass', x=['veins', 'many-eyes'], eyes='many', eyec='#3a0a0a', mouth='fangs', mouthc='#3a0a0a'),
    'shapeshiftingooze': dict(pal='purple', shape='humanoid', x=['bubbles'], eyes='glow', eyec='#ffffff', soft=1.6, alpha=220),
    'oblex': dict(pal='lime', shape='tall', x=['brain', 'drips'], eyes='none', alpha=190),
    # floor 7
    'magmaooze': dict(pal='magma', shape='mound', x=['flames', 'drips'], eyes='angry', eyec='#fff070', mouth='gape', mouthc='#2a0400'),
    'psychicooze': dict(pal='psychic', x=['brain', 'tentacles'], eyes='glow', eyec='#ffffff', alpha=200),
    'sludgegolem': dict(pal='sludge', shape='humanoid', x=['spots', 'drips'], spotc='#1e2214', eyes='glow', eyec='#ffe040', mouth='o', soft=1.6),
    'slimehydra': dict(pal='green', shape='hydra', heads=3, x=['bubbles'], eyes='none'),
    'gibberingmouther': dict(pal='flesh', shape='mass', x=[], eyes='many', eyec='#08080c', mouth='many'),
    'oozedevourer': dict(pal='toxic', shape='mound', x=['bones', 'coins'], eyes='angry', eyec='#ff3020', mouth='gape', alpha=215),
    # floor 8
    'chaosslime': dict(pal='chaos', x=['chaos', 'bubbles'], eyes='big', mouth='fangs'),
    'voidslime': dict(pal='void', x=['stars'], eyes='glow', eyec='#c4aef0', shinec='#6a5aa0'),
    'slimehorror': dict(pal='venom', shape='mound', x=['tentacles', 'drips'], eyes='many', eyec='#ffe040', mouth='gape'),
    'gelatinousabomination': dict(pal='clear', shape='mass', x=['skull', 'bones', 'sword', 'coins'], eyes='one', eyec='#ff3a3a', alpha=165, dither=False),
    'putridamalgamation': dict(pal='plague', shape='mass', x=['bones', 'spots', 'drips', 'veins'], spotc='#2a2a0a', eyes='many', eyec='#c0ff40', mouth='many'),
    # floor 9
    'abyssalooze': dict(pal='abyss', shape='mound', x=['tentacles', 'stars'], eyes='one', eyec='#40e0ff'),
    'amorphoushorror': dict(pal='black', shape='mass', x=['tentacles'], eyes='many', eyec='#ff2020', mouth='many', mouthc='#ff2020', shinec='#5a5a70'),
    'slimequeen': dict(pal='queen', shape='tall', x=['tiara', 'bubbles'], eyes='big', mouth='smile', alpha=225),
    'jellybehemoth': dict(pal='pink', shape='mound', x=['nucleus', 'bubbles', 'bones'], nuc=P['purple'], eyes='big', mouth='gape', alpha=210),
    # floor 10
    'slimeking': dict(pal='royal', shape='mound', x=['crown', 'bubbles', 'coins'], eyes='big', mouth='fangs', alpha=225),
    'sludgeleviathan': dict(pal='sludge', shape='hydra', heads=4, x=['drips'], eyec='#ff6020', eyes='none'),
    'shoggoth': dict(pal='black', shape='mound', x=['tentacles', 'bubbles'], eyes='many', eyec='#a0ff60', mouth='many', mouthc='#3aff60', shinec='#5a5a70'),
    # floor 11 and 12
    'primordialooze': dict(pal='primordial', shape='mound', x=['nucleus', 'tentacles', 'bubbles', 'stars'], nuc=P['lime'], eyes='one', eyec='#fff070'),
    'oozetitan': dict(pal='teal', shape='mound', x=['spikes', 'drips', 'bones', 'sword'], eyes='angry', eyec='#ffffff', mouth='gape', alpha=230),
}

if __name__ == '__main__':
    out, imgs = {}, []
    for k, spec in SPECS.items():
        im = build(spec)
        imgs.append(im)
        buf = io.BytesIO(); im.save(buf, 'PNG')
        out[k] = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    sheet(imgs, scale=4, cols=8).save('oozes.png')
    json.dump(out, open('oozes.json', 'w'))
    print(len(out), 'oozes')
