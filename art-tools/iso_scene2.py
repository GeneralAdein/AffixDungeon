"""The town ground, repainted to sit under the building art: lush grass, cobbled streets, a plaza and better trees."""
from iso import *
import json, base64, io, math
from PIL import Image
from scipy import ndimage
W, H, OX, OY, S = 320, 440, 160, 142, 56
LOTS = {'guild':(0,0), 'temple':(0,S), 'cartographer':(S,0), 'square':(S,S), 'yard':(S,2*S), 'bank':(2*S,S),
        'garden':(2*S,2*S), 'shop':(2*S,3*S), 'tavern':(3*S,2*S), 'gate':(3*S,3*S), 'smithy':(3*S,4*S), 'apothecary':(4*S,3*S)}
rng = np.random.default_rng(3)
def smooth_noise(scale, seed):
    r = np.random.default_rng(seed).random((H // scale + 3, W // scale + 3))
    return ndimage.zoom(r, scale, order=3)[:H, :W]
N1, N2 = smooth_noise(24, 1), smooth_noise(7, 2)
GRASS = ramp('#1f3414', '#2b4518', '#38571d', '#466a23', '#557c2a', '#6a9232', '#82a93e')
STONE = ramp('#2e2c2e', '#47443f', '#5c5852', '#706b63', '#837d73', '#9a948a')
def world(px, py):
    d, e = px + .5 - OX, py + .5 - OY
    y = (e - d / 2); x = y + d
    return x, y
def cheb(x, y, c): return max(abs(x - c[0]), abs(y - c[1]))
img = np.zeros((H, W, 3), np.uint8)
for py in range(H):
    for px in range(W):
        x, y = world(px, py)
        d = min(cheb(x, y, c) for c in LOTS.values())
        jitter = (N2[py, px] - .5) * 4
        plaza = cheb(x, y, LOTS['square']) < 26
        if plaza or (23 + jitter < d < 31 + jitter and d < 80):
            # cobblestones in world space
            gx, gy = x / 4.4, y / 4.4; ix, iy = math.floor(gx), math.floor(gy)
            best, second, bid = 9, 9, None
            for ox in (-1, 0, 1):
                for oy in (-1, 0, 1):
                    cx = ix + ox + .2 + .6 * hsh(ix + ox, iy + oy); cy = iy + oy + .2 + .6 * hsh(iy + oy, ix + ox, 7)
                    dd = (gx - cx) ** 2 + (gy - cy) ** 2
                    if dd < best: second, best, bid = best, dd, (ix + ox, iy + oy)
                    elif dd < second: second = dd
            if second - best < .1: img[py, px] = STONE[0]
            else:
                lv = 2 + (hsh(*bid, 2) > .55) + (best < .04)
                img[py, px] = STONE[lv]
            continue
        n = N1[py, px] * .7 + N2[py, px] * .3
        lv = 1 + int(n * 3.4)
        t = hsh(px, py)
        if t > .985: lv += 1
        if t < .012: lv -= 1
        img[py, px] = GRASS[max(0, min(6, lv))]
# grass tufts and a few flowers on the grass only
def isgrass(px, py): return 0 <= px < W and 0 <= py < H and tuple(img[py, px]) in [tuple(c) for c in GRASS]
for i in range(1400):
    px, py = int(hsh(i, 21) * W), int(hsh(i, 22) * H)
    if not isgrass(px, py): continue
    if hsh(i, 23) < .9:
        c = GRASS[5] if hsh(i, 24) > .4 else GRASS[6]
        for (dx, dy) in ((0, 0), (-1, 1), (1, 1)):
            if isgrass(px + dx, py + dy): img[py + dy, px + dx] = c
        if isgrass(px, py + 2): img[py + 2, px] = GRASS[1]
    else:
        img[py, px] = hx(['#f0ead8', '#f2d45a', '#e0a0d0'][i % 3])
# trees: shadow, trunk and a three-tone canopy with an outline
OUTL = hx('#0c140a'); LEAF = ramp('#10200e', '#1c3416', '#2a4c1e', '#3a6626', '#4e8030', '#6a9c3c')
def put(px, py, c):
    if 0 <= px < W and 0 <= py < H: img[py, px] = c
def tree(cx, cy, r):
    for py in range(int(cy - r * .5), int(cy + r * .5) + 1):
        for px in range(int(cx - r * 1.3), int(cx + r * 1.3) + 1):
            if ((px - cx) / (r * 1.25)) ** 2 + ((py - cy) / (r * .45)) ** 2 <= 1: put(px, py, tuple((np.array(img[py, px]) * .6).astype(int)) if 0 <= px < W and 0 <= py < H else 0)
    for py in range(int(cy - r * 1.2), int(cy) + 1):
        put(int(cx), py, hx('#3a2614')); put(int(cx) - 1, py, hx('#2a1a0c'))
    blobs = [(cx, cy - r * 1.6, r), (cx - r * .6, cy - r * 1.2, r * .75), (cx + r * .6, cy - r * 1.25, r * .75)]
    canopy = np.zeros((H, W), bool); tone = {}
    for (bx, by, br) in blobs:
        for py in range(int(by - br) - 1, int(by + br) + 2):
            for px in range(int(bx - br) - 1, int(bx + br) + 2):
                if 0 <= px < W and 0 <= py < H and (px + .5 - bx) ** 2 + (py + .5 - by) ** 2 <= br * br:
                    canopy[py, px] = True
                    l = (px - bx) / br + (py - by) / br
                    tone[(px, py)] = max(tone.get((px, py), 0), 4 if l < -.7 else 3 if l < .3 else 2)
    edge = canopy & ~ndimage.binary_erosion(canopy)
    for (px, py), l in tone.items(): img[py, px] = LEAF[l + (hsh(px, py, 4) > .8)]
    ys, xs = np.nonzero(ndimage.binary_dilation(canopy) & ~canopy)
    for py, px in zip(ys, xs):
        if py > cy - r * 1.6: img[py, px] = OUTL
        else: img[py, px] = OUTL
spots = []
for i in range(900):
    x, y = -300 + hsh(i, 11) * 760, -300 + hsh(i, 12) * 760
    if min(cheb(x, y, c) for c in LOTS.values()) > 40:
        sx, sy = OX + (x - y), OY + (x + y) / 2
        if -10 < sx < W + 10 and -6 < sy < H + 16: spots.append((sy, sx, i))
for sy, sx, i in sorted(spots): tree(sx, sy, 4 + (i % 3))
# the garden lot: a few trees and a flower bed
gx, gy = OX + (LOTS['garden'][0] - LOTS['garden'][1]), OY + (LOTS['garden'][0] + LOTS['garden'][1]) / 2
for py in range(int(gy - 8), int(gy + 9)):
    for px in range(int(gx - 18), int(gx + 19)):
        if abs(px - gx) / 16 + abs(py - gy) / 8 <= 1 and hsh(px, py, 8) > .78:
            img[py, px] = hx(['#d8506a', '#f2d45a', '#f0ead8', '#b07ae0'][int(hsh(px, py, 9) * 4)])
for (dx, dy, r) in ((-14, -10, 5), (14, -8, 5), (0, -16, 6)): tree(gx + dx, gy + dy, r)
# lamp posts at street corners
lamps = []; corners = {}
for c in LOTS.values():
    for dx in (-28, 28):
        for dy in (-28, 28): corners[(c[0] + dx, c[1] + dy)] = corners.get((c[0] + dx, c[1] + dy), 0) + 1
for (x, y), n in sorted(corners.items(), key=lambda kv: kv[0][0] + kv[0][1]):
    if n >= 2:
        px, py = int(OX + (x - y)), int(OY + (x + y) / 2)
        for t in range(10): put(px, py - t, hx('#1a1a20'))
        for dx in (-1, 0, 1):
            for dy in (-12, -11, -10): put(px + dx, py + dy, hx('#ffd060'))
        put(px, py - 11, hx('#fff2b0')); lamps.append((px, py - 11))
a = img.astype(float)
yy, xx = np.mgrid[0:H, 0:W]
v = np.clip(((xx - W / 2) / (W * .72)) ** 2 + ((yy - H / 2) / (H * .72)) ** 2, 0, 1)
a = (a * (1 - .3 * v[..., None])).astype(np.uint8)
bg = Image.fromarray(a)
b = io.BytesIO(); bg.save(b, 'PNG', optimize=True)
pos = {}
for k, (x, y) in LOTS.items():
    pos[k] = {'x': OX + (x - y), 'y': OY + (x + y) / 2, 'wx': x, 'wy': y, 'door': [OX + (x - y - 30), OY + (x + y + 30) / 2]}
json.dump({'bg': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'W': W, 'H': H, 'OX': OX, 'OY': OY, 'pos': pos, 'lamps': lamps}, open('iso_scene2.json', 'w'))
bg.resize((W * 2, H * 2), Image.NEAREST).save('iso_scene2_bg.png')
print(len(b.getvalue()))
