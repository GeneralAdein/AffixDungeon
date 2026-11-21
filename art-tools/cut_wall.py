import numpy as np, json, base64, io
from PIL import Image
from scipy import ndimage
A = np.array(Image.open('source-art/old-wall.jpg').convert('RGB')).astype(float)
BG = A[2:12, 2:12].reshape(-1, 3).mean(0)
def grid(edges, lo, hi):
    best = None
    for p in np.arange(lo, hi, 0.05):
        for ph in np.arange(0, p, 0.5):
            idx = np.round(np.arange(ph, len(edges) - 1, p)).astype(int)
            sc = edges[idx].mean() / (edges.mean() + 1e-6)
            if best is None or sc > best[0]: best = (sc, p, ph)
    return best[1], best[2]
def native(box, lo=13.5, hi=17, keep_bg=False):
    x0, y0, x1, y1 = box; c = A[y0:y1, x0:x1]
    d = np.sqrt(((c - BG) ** 2).sum(-1)); lab, _ = ndimage.label(d < 26)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fg = ndimage.binary_fill_holes(~np.isin(lab, list(edge)))
    gx = np.abs(np.diff(c, axis=1)).sum(-1).sum(0); gy = np.abs(np.diff(c, axis=0)).sum(-1).sum(1)
    px, phx = grid(gx, lo, hi); py, phy = grid(gy, lo, hi)
    xs = np.arange(phx, c.shape[1] - 1, px); ys = np.arange(phy, c.shape[0] - 1, py)
    W, H = len(xs) - 1, len(ys) - 1; res = np.zeros((H, W, 4), np.uint8)
    for j in range(H):
        for i in range(W):
            a0, a1 = int(round(xs[i])) + 2, int(round(xs[i + 1])) - 2; b0, b1 = int(round(ys[j])) + 2, int(round(ys[j + 1])) - 2
            cm = fg[b0:b1, a0:a1]
            if cm.mean() < .5: continue
            res[j, i, :3] = np.median(c[b0:b1, a0:a1][cm], axis=0); res[j, i, 3] = 255
    im = Image.fromarray(res, 'RGBA'); bb = im.getbbox()
    return im.crop(bb), (px, py)
wall, g = native((19, 16, 1906, 1125), 6.5, 10); print('wall', wall.size, g)
w = np.array(wall)
# holes: dark pixels inside the wall that don't touch its outside edge
lum = w[..., :3].astype(float) @ [.3, .59, .11]
dark = (lum < 62) & (w[..., 3] > 0)
lab, n = ndimage.label(dark); holes = []
for i, sl in enumerate(ndimage.find_objects(lab)):
    m = lab[sl] == i + 1; sz = m.sum()
    if sz < 500: continue
    if sl[0].start == 0 or sl[1].start == 0 or sl[0].stop >= w.shape[0] or sl[1].stop >= w.shape[1]: continue
    ys, xs = np.nonzero(lab == i + 1)
    holes.append({'cx': float(xs.mean() + .5), 'cy': float(ys.mean() + .5), 'x0': int(xs.min()), 'y0': int(ys.min()), 'x1': int(xs.max() + 1), 'y1': int(ys.max() + 1), 'size': int(sz)})
holes.sort(key=lambda h: (round(h['cy'] / (w.shape[0] / 2.5)), h['cx']))
print(len(holes), [(round(h['cx']), round(h['cy']), h['size']) for h in holes])
STONES = [('heart', (153, 1189, 524, 1474)), ('tide', (626, 1171, 856, 1520)), ('sun', (950, 1213, 1344, 1473)), ('dusk', (1411, 1172, 1707, 1505)),
          ('verdant', (139, 1541, 452, 1850)), ('sky', (521, 1577, 902, 1821)), ('rose', (992, 1498, 1254, 1860)), ('moon', (1341, 1558, 1778, 1848))]
out = {'wall': {}, 'stones': {}}
b = io.BytesIO(); wall.save(b, 'PNG', optimize=True); out['wall'] = {'src': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'w': wall.width, 'h': wall.height, 'holes': holes}
ims = []
for k, box in STONES:
    st, g = native((box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10)); ims.append(st); print(k, st.size, g)
    b = io.BytesIO(); st.save(b, 'PNG', optimize=True); out['stones'][k] = {'src': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'w': st.width, 'h': st.height}
json.dump(out, open('wall.json', 'w'))
# preview: wall with every stone set in its hole
S = 3; pv = Image.new('RGBA', (wall.width * S, wall.height * S + 140), (20, 22, 30, 255)); pv.alpha_composite(wall.resize((wall.width * S, wall.height * S), Image.NEAREST))
for (k, _), h, st in zip(STONES, holes, ims):
    hw, hh = h['x1'] - h['x0'], h['y1'] - h['y0']; s = min(hw / st.width, hh / st.height) * 1.05
    sw, sh = max(1, round(st.width * s * S)), max(1, round(st.height * s * S))
    pv.alpha_composite(st.resize((sw, sh), Image.NEAREST), (int(h['cx'] * S - sw / 2), int(h['cy'] * S - sh / 2)))
pv.save('wall_preview.png')
