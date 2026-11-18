from iso import *
import json, base64, io, math
from PIL import Image
W, H, OX, OY, S = 320, 440, 160, 142, 56
LOTS = {  # world lot centers on a diagonal lattice
 'guild':(0,0), 'temple':(0,S), 'cartographer':(S,0),
 'square':(S,S), 'yard':(S,2*S), 'bank':(2*S,S),
 'garden':(2*S,2*S), 'shop':(2*S,3*S), 'tavern':(3*S,2*S),
 'gate':(3*S,3*S), 'smithy':(3*S,4*S), 'apothecary':(4*S,3*S),
}
I = Iso(W, H, OX, OY)
def cheb(x, y, c): return max(abs(x - c[0]), abs(y - c[1]))
def ground(x, y, z, u, v):
    d = min(cheb(x, y, c) for c in LOTS.values())
    if d <= 23: return cobble(4)(x, y, z, u, v)
    if d <= 33:
        n = hsh(int(x), int(y))
        if (x % 7 < 1 or y % 7 < 1) and n > .3: return ('dirt', 1)
        return ('dirt', 3 + (n > .7) - (n > .92))
    return grass()(x, y, z, u, v)
I.ground(-400, -400, 600, 600, ground)
# trees and bushes on the grass, back to front
spots = []
for i in range(700):
    x, y = -260 + hsh(i, 11) * 700, -260 + hsh(i, 12) * 700
    if min(cheb(x, y, c) for c in LOTS.values()) > 38:
        sx, sy = I.P(x, y)
        if -10 < sx < W + 10 and -10 < sy < H + 20: spots.append((x + y, x, y, i))
for _, x, y, i in sorted(spots):
    if i % 3: I.tree(x, y, 8 + (i % 5), 5 + (i % 3))
    else: I.bush(x, y, 3)
# lamp posts at road corners between lots
lamps = []
corners = {}
for c in LOTS.values():
    for dx in (-28, 28):
        for dy in (-28, 28): corners[(c[0] + dx, c[1] + dy)] = corners.get((c[0] + dx, c[1] + dy), 0) + 1
for (x, y), n in sorted(corners.items(), key=lambda kv: kv[0][0] + kv[0][1]):
    if n >= 2:
        px, py = I.P(x, y)
        for t in range(9): I.put(px, py - t, R['iron'][1])
        I.rect(px - 1, py - 11, px + 2, py - 8, R['glow'][4]); lamps.append((round(px, 1), round(py - 10, 1)))
# soft vignette
img = I.image().convert('RGB'); a = np.array(img).astype(float)
yy, xx = np.mgrid[0:H, 0:W]
v = np.clip(((xx - W / 2) / (W * .7)) ** 2 + ((yy - H / 2) / (H * .7)) ** 2, 0, 1)
a = (a * (1 - .35 * v[..., None])).astype(np.uint8)
bg = Image.fromarray(a)
b = io.BytesIO(); bg.save(b, 'PNG', optimize=True)
# positions: every lot's screen anchor, plus the door point on the road in front of it
pos = {}
for k, (x, y) in LOTS.items():
    sx, sy = I.P(x, y); dx, dy = I.P(x, y + 30)
    pos[k] = {'x': round(sx, 1), 'y': round(sy, 1), 'wx': x, 'wy': y, 'door': [round(dx, 1), round(dy, 1)]}
# chimney smoke offsets inside each 96x96 sprite (origin 48,70)
spr = Iso(96, 96, 48, 70)
smoke = {'smithy': spr.P(-11, -10, 39), 'tavern': spr.P(6.5, -9.5, 40), 'apothecary': spr.P(-10, -8, 37)}
json.dump({'CW': 216, 'CH': 300, 'bg': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'W': W, 'H': H, 'OX': OX, 'OY': OY, 'pos': pos, 'lamps': lamps, 'smoke': smoke}, open('iso_scene.json', 'w'))
# preview with the buildings placed
pieces = json.load(open('iso_town.json'))
prev = bg.convert('RGBA')
for k in sorted(LOTS, key=lambda k: pos[k]['y']):
    im = Image.open(io.BytesIO(base64.b64decode(pieces[k].split(',')[1]))).convert('RGBA')
    prev.alpha_composite(im, (int(pos[k]['x'] - 48), int(pos[k]['y'] - 70)))
prev.resize((W * 3, H * 3), Image.NEAREST).save('iso_scene_preview.png')
print(len(b.getvalue()))
