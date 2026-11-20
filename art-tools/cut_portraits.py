import numpy as np, json, base64, io
from PIL import Image
A = np.array(Image.open('source-art/portraits-set-1.jpg').convert('RGB')).astype(float)
COLS = [(22, 507), (531, 1012), (1037, 1520), (1545, 2027)]; ROWS = [(207, 859), (1116, 1699)]
NAMES = [['guild', 'smithy', 'temple', 'yard'], ['tavern', 'apothecary', 'cartographer', 'shop']]
def grid(edges, lo, hi):
    best = None
    for p in np.arange(lo, hi, 0.02):
        for ph in np.arange(0, p, 0.25):
            idx = np.round(np.arange(ph, len(edges) - 1, p)).astype(int)
            sc = edges[idx].mean() / (edges.mean() + 1e-6)
            if best is None or sc > best[0]: best = (sc, p, ph)
    return best[1], best[2]
out = {}; prev = []
for r, (y0, y1) in enumerate(ROWS):
    for c, (x0, x1) in enumerate(COLS):
        k = NAMES[r][c]
        ix0, ix1, iy0, iy1 = x0 + 26, x1 - 26, y0 + 26, y1 - 26
        w = ix1 - ix0; h = iy1 - iy0
        top = iy0 + int((h - w) * .25)
        cr = A[top:top + w, ix0:ix1]
        gx = np.abs(np.diff(cr, axis=1)).sum(-1).sum(0); gy = np.abs(np.diff(cr, axis=0)).sum(-1).sum(1)
        px, phx = grid(gx, 9, 17); py, phy = grid(gy, 9, 17)
        xs = np.arange(phx, cr.shape[1] - 1, px); ys = np.arange(phy, cr.shape[0] - 1, py)
        Wn, Hn = len(xs) - 1, len(ys) - 1
        res = np.zeros((Hn, Wn, 3), np.uint8)
        for j in range(Hn):
            for i in range(Wn):
                a0, a1 = int(round(xs[i])) + 2, int(round(xs[i + 1])) - 2
                b0, b1 = int(round(ys[j])) + 2, int(round(ys[j + 1])) - 2
                res[j, i] = np.median(cr[b0:b1, a0:a1].reshape(-1, 3), axis=0)
        n = min(Wn, Hn); res = res[:n, :n]
        im = Image.fromarray(res)
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
        out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
        prev.append(im); print(k, 'grid', round(px, 2), round(py, 2), 'size', n)
json.dump(out, open('faces.json', 'w'))
S = 6; sz = max(p.width for p in prev) * S
sh = Image.new('RGB', (4 * (sz + 8) + 8, 2 * (sz + 8) + 8), (20, 22, 30))
for i, p in enumerate(prev): sh.paste(p.resize((p.width * S, p.height * S), Image.NEAREST), (8 + (i % 4) * (sz + 8), 8 + (i // 4) * (sz + 8)))
sh.save('faces_preview.png')
