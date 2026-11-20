"""Cut buildings out of an AI pixel-art sheet at their true pixel resolution.

The sheet is pixel art drawn at roughly 8 screen pixels per art pixel, saved as a JPEG. Instead of
averaging (which blurs), find the art's pixel grid for each building and take the median colour of
each grid cell, which gives back the original crisp pixels and drops the JPEG noise.
"""
import numpy as np, json, base64, io, sys
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1] if len(sys.argv) > 1 else 'source-art/buildings-set-1.jpg'
A = np.array(Image.open(SRC).convert('RGB')).astype(float)
BG = np.array([32, 26, 40.])
BOX = {'guild': (14, 106, 703, 917), 'smithy': (726, 168, 1365, 917), 'temple': (1377, 62, 2046, 914),
       'yard': (86, 1094, 1002, 1812), 'tavern': (1045, 1047, 1888, 1812)}

def grid(edges):
    """Best (period, phase) for a 1-D edge-strength profile."""
    best = None
    for p in np.arange(7.4, 8.61, 0.01):
        for ph in np.arange(0, p, 0.25):
            idx = np.round(np.arange(ph, len(edges) - 1, p)).astype(int)
            score = edges[idx].mean() / (edges.mean() + 1e-6)
            if best is None or score > best[0]: best = (score, p, ph)
    return best[1], best[2]

def mask_for(c):
    d = np.sqrt(((c - BG) ** 2).sum(-1)); lab, _ = ndimage.label(d < 30)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fg = ~np.isin(lab, list(edge))
    lab2, n2 = ndimage.label(fg); sizes = ndimage.sum(fg, lab2, range(1, n2 + 1))
    return ndimage.binary_fill_holes(lab2 == 1 + int(np.argmax(sizes)))

out, prev = {}, []
for k, (x0, y0, x1, y1) in BOX.items():
    c = A[y0:y1, x0:x1]; fg = mask_for(c)
    gx = np.abs(np.diff(c, axis=1)).sum(-1)[fg[:, 1:]].sum() if False else np.abs(np.diff(c, axis=1)).sum(-1).sum(0)
    gy = np.abs(np.diff(c, axis=0)).sum(-1).sum(1)
    px, phx = grid(gx); py, phy = grid(gy)
    xs = np.arange(phx, c.shape[1] - 1, px); ys = np.arange(phy, c.shape[0] - 1, py)
    W, H = len(xs) - 1, len(ys) - 1
    res = np.zeros((H, W, 4), np.uint8)
    for j in range(H):
        for i in range(W):
            a0, a1 = int(round(xs[i])) + 1, int(round(xs[i + 1])) - 1
            b0, b1 = int(round(ys[j])) + 1, int(round(ys[j + 1])) - 1
            if a1 <= a0 or b1 <= b0: continue
            cm = fg[b0:b1, a0:a1]
            if cm.mean() < .5: continue
            res[j, i, :3] = np.median(c[b0:b1, a0:a1][cm], axis=0); res[j, i, 3] = 255
    im = Image.fromarray(res, 'RGBA')
    bb = im.getbbox(); im = im.crop(bb); res = np.array(im)
    m = res[..., 3] > 0; H, W = m.shape
    rows = [y for y in range(int(H * .5), H) if m[y].any()]
    widest = max(rows, key=lambda y: np.ptp(np.nonzero(m[y])[0]))
    xw = np.nonzero(m[widest])[0]; island = xw.max() - xw.min() + 1
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    out[k] = {'src': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'w': W, 'h': H,
              'ax': round((xw.min() + xw.max() + 1) / 2, 1), 'ay': widest, 'island': int(island)}
    prev.append(im); print(k, 'grid', round(px, 2), round(py, 2), 'size', W, H, 'island', island)
json.dump(out, open('user_buildings2.json', 'w'))
S = 4; tw = sum(p.width * S + 10 for p in prev); th = max(p.height for p in prev) * S + 10
sh = Image.new('RGBA', (tw, th), (20, 22, 30, 255)); x = 5
for p in prev: sh.alpha_composite(p.resize((p.width * S, p.height * S), Image.NEAREST), (x, 5)); x += p.width * S + 10
sh.save('user_buildings2.png')
