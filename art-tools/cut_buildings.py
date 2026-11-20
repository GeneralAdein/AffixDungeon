import numpy as np, json, base64, io
from PIL import Image
from scipy import ndimage
src = Image.open('source-art/buildings-set-1.jpg').convert('RGB')
A = np.array(src).astype(int)
BG = np.array([32, 26, 40])
BOX = {'guild': (14, 106, 703, 917), 'smithy': (726, 168, 1365, 917), 'temple': (1377, 62, 2046, 914),
       'yard': (86, 1094, 1002, 1812), 'tavern': (1045, 1047, 1888, 1812)}
LOT_W = 84                      # every island is scaled to the width of a town lot
out, prev = {}, []
for k, (x0, y0, x1, y1) in BOX.items():
    c = A[y0:y1, x0:x1]
    d = np.sqrt(((c - BG) ** 2).sum(-1))
    bgish = d < 30
    lab, n = ndimage.label(bgish)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(edge))
    fg = ~bg
    lab2, n2 = ndimage.label(fg)
    sizes = ndimage.sum(fg, lab2, range(1, n2 + 1))
    keep = 1 + int(np.argmax(sizes))
    fg = lab2 == keep
    fg = ndimage.binary_fill_holes(fg)
    ys, xs = np.nonzero(fg)
    bx0, bx1, by0, by1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    rgba = np.zeros((by1 - by0, bx1 - bx0, 4), np.uint8)
    rgba[..., :3] = c[by0:by1, bx0:bx1]; rgba[..., 3] = fg[by0:by1, bx0:bx1] * 255
    im = Image.fromarray(rgba, 'RGBA')
    # island width: the widest row of the lower third of the sprite
    m = fg[by0:by1, bx0:bx1]
    lower = m[int(m.shape[0] * .55):]
    w_island = max((np.ptp(np.nonzero(r)[0]) + 1) for r in lower if r.any())
    s = LOT_W / w_island
    W, H = max(1, round(im.width * s)), max(1, round(im.height * s))
    # downsample: average colour over opaque source pixels, keep pixels that are mostly covered
    pre = np.array(im).astype(float); a = pre[..., 3:4] / 255; pre[..., :3] *= a
    small = Image.fromarray(np.clip(pre, 0, 255).astype(np.uint8), 'RGBA').resize((W, H), Image.BOX)
    sm = np.array(small).astype(float)
    al = sm[..., 3:4] / 255
    rgb = np.where(al > 0, sm[..., :3] / np.maximum(al, 1e-6), 0)
    res = np.zeros((H, W, 4), np.uint8); res[..., :3] = np.clip(rgb, 0, 255); res[..., 3] = (al[..., 0] > .5) * 255
    res_im = Image.fromarray(res, 'RGBA')
    q = res_im.convert('RGB').quantize(colors=40, method=Image.Quantize.MEDIANCUT).convert('RGB')
    res[..., :3] = np.array(q)
    res_im = Image.fromarray(res, 'RGBA')
    # anchor: the centre of the island's top face (2:1 diamond sitting on a thin soil edge)
    mm = res[..., 3] > 0; ys2, xs2 = np.nonzero(mm)
    bottom = ys2.max()
    rows = [y for y in range(int(H * .5), H) if mm[y].any()]
    widest = max(rows, key=lambda y: np.ptp(np.nonzero(mm[y])[0]))
    xs_w = np.nonzero(mm[widest])[0]
    ax = (xs_w.min() + xs_w.max()) / 2; ay = widest - 1
    b = io.BytesIO(); res_im.save(b, 'PNG', optimize=True)
    out[k] = {'src': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), 'w': W, 'h': H, 'ax': round(float(ax), 1), 'ay': round(float(ay), 1)}
    prev.append(res_im); print(k, W, H, out[k]['ax'], out[k]['ay'], len(b.getvalue()))
json.dump(out, open('user_buildings.json', 'w'))
S = 5; tw = sum(p.width * S + 10 for p in prev); th = max(p.height for p in prev) * S + 10
sh = Image.new('RGBA', (tw, th), (20, 22, 30, 255)); x = 5
for p in prev: sh.alpha_composite(p.resize((p.width * S, p.height * S), Image.NEAREST), (x, 5)); x += p.width * S + 10
sh.save('user_buildings.png')
