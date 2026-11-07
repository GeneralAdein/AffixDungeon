import numpy as np
from scipy import ndimage
from PIL import Image, ImageDraw

W = 48
yy, xx = np.mgrid[0:W, 0:W] + 0.5
BAYER = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0 - 0.5
BAYER_T = np.tile(BAYER, (W // 4, W // 4))
rng = np.random.default_rng(7)
NOISE = rng.random((W, W))


def hexc(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ellipse(cx, cy, rx, ry, rot=0):
    c, s = np.cos(np.radians(rot)), np.sin(np.radians(rot))
    dx, dy = xx - cx, yy - cy
    u = dx * c + dy * s
    v = -dx * s + dy * c
    return (u / rx) ** 2 + (v / ry) ** 2 <= 1


def capsule(x1, y1, x2, y2, r1, r2=None):
    r2 = r1 if r2 is None else r2
    vx, vy = x2 - x1, y2 - y1
    L2 = vx * vx + vy * vy or 1e-6
    t = np.clip(((xx - x1) * vx + (yy - y1) * vy) / L2, 0, 1)
    px, py = x1 + t * vx, y1 + t * vy
    r = r1 + (r2 - r1) * t
    return (xx - px) ** 2 + (yy - py) ** 2 <= r * r


def chain(pts, r1, r2=None):
    r2 = r1 if r2 is None else r2
    segs = list(zip(pts[:-1], pts[1:]))
    lens = [np.hypot(b[0] - a[0], b[1] - a[1]) for a, b in segs]
    tot = sum(lens) or 1
    m = np.zeros((W, W), bool)
    acc = 0
    for (a, b), L in zip(segs, lens):
        ra = r1 + (r2 - r1) * acc / tot
        acc += L
        rb = r1 + (r2 - r1) * acc / tot
        m |= capsule(a[0], a[1], b[0], b[1], ra, rb)
    return m


def poly(pts):
    im = Image.new('L', (W, W), 0)
    ImageDraw.Draw(im).polygon([(x, y) for x, y in pts], fill=1)
    return np.array(im).astype(bool)


def rect(x0, y0, x1, y1):
    return (xx >= x0) & (xx < x1) & (yy >= y0) & (yy < y1)


def mir(m):
    return m | m[:, ::-1]


def mirpts(pts):
    return [(W - x, y) for x, y in pts]


class Part:
    def __init__(self, mask, ramp, bias=0.0, dither=False, noise=0.0, soft=1.0, flat=None, ao=True, lo=-0.25, hi=0.95):
        self.mask, self.ramp, self.bias, self.dither = mask, [hexc(c) for c in ramp], bias, dither
        self.noise, self.soft, self.flat, self.ao, self.lo, self.hi = noise, soft, flat, ao, lo, hi


FLAT = {'on': False}

def shade_levels(p, light=(-0.55, -0.8, 0.75)):
    mask = p.mask
    n = len(p.ramp)
    if p.flat is not None:
        lv = np.full((W, W), float(p.flat))
    else:
        d = ndimage.distance_transform_edt(np.pad(mask, 2))[2:-2, 2:-2]
        h = np.sqrt(d)
        h = ndimage.gaussian_filter(h, p.soft)
        gy, gx = np.gradient(h)
        nx, ny, nz = -gx, -gy, np.full_like(h, 0.55)
        nl = np.sqrt(nx * nx + ny * ny + nz * nz)
        L = np.array(light) / np.linalg.norm(light)
        dot = (nx * L[0] + ny * L[1] + nz * L[2]) / nl
        val = (dot - p.lo) / (p.hi - p.lo)
        val = np.clip(val + p.bias + (NOISE - 0.5) * p.noise, 0, 1)
        lv = val * (n - 1)
    if FLAT['on'] and p.flat is None:
        v = lv / max(1, n - 1)
        sh, base, hi = round((n-1)*.3), round((n-1)*.6), round((n-1)*.85)
        if n <= 3: sh, base, hi = 0, min(1, n-1), n-1
        out = np.where(v < .36, sh, np.where(v < .74, base, hi))
        return out.astype(int)
    if p.dither:
        lv = lv + BAYER_T * 0.9
    lv = np.clip(np.round(lv), 0, n - 1).astype(int)
    return lv


class Sprite:
    def __init__(self, outline='#0b0809'):
        self.parts = []
        self.details = []
        self.outline = hexc(outline)
        self.erase = np.zeros((W, W), bool)

    def add(self, mask, ramp, **kw):
        p = Part(mask, ramp, **kw)
        self.parts.append(p)
        return p

    def px(self, pts, color, alpha=255):
        c = hexc(color)
        for x, y in pts:
            self.details.append((int(x), int(y), c, alpha))

    def pxm(self, pts, color, alpha=255):
        self.px(pts, color, alpha)
        self.px([(W - 1 - x, y) for x, y in pts], color, alpha)

    def maskpx(self, mask, color, alpha=255):
        ys, xs = np.nonzero(mask)
        self.px(list(zip(xs, ys)), color, alpha)

    def render(self):
        pid = np.full((W, W), -1)
        lev = np.zeros((W, W), int)
        levels = []
        for i, p in enumerate(self.parts):
            lv = shade_levels(p)
            levels.append(lv)
            pid[p.mask] = i
            lev[p.mask] = lv[p.mask]
        pid[self.erase] = -1
        # ambient occlusion: pixel of an earlier part touching a later (front) part
        ao = np.zeros((W, W), bool)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            sh = np.roll(np.roll(pid, dy, 0), dx, 1)
            ao |= (pid >= 0) & (sh > pid)
        img = np.zeros((W, W, 4), np.uint8)
        for y in range(W):
            for x in range(W):
                i = pid[y, x]
                if i < 0:
                    continue
                p = self.parts[i]
                l = lev[y, x]
                if ao[y, x] and p.ao:
                    l = 0 if FLAT['on'] else max(0, l - 1)
                img[y, x, :3] = p.ramp[l]
                img[y, x, 3] = 255
        filled = pid >= 0
        nb = np.zeros((W, W), bool)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nb |= np.roll(np.roll(filled, dy, 0), dx, 1)
        outl = nb & ~filled
        outl[0, :] = outl[-1, :] = False
        outl[:, 0] = outl[:, -1] = False
        img[outl, :3] = self.outline
        img[outl, 3] = 255
        for x, y, c, a in self.details:
            if 0 <= x < W and 0 <= y < W:
                img[y, x, :3] = c
                img[y, x, 3] = a
        return Image.fromarray(img, 'RGBA')


def sheet(imgs, scale=5, cols=5, bg=(28, 30, 40)):
    rows = (len(imgs) + cols - 1) // cols
    S = W * scale
    out = Image.new('RGBA', (cols * (S + 8) + 8, rows * (S + 8) + 8), bg + (255,))
    for i, im in enumerate(imgs):
        r, c = divmod(i, cols)
        big = im.resize((S, S), Image.NEAREST)
        out.alpha_composite(big, (8 + c * (S + 8), 8 + r * (S + 8)))
    return out
