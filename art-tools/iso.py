"""Isometric pixel-art engine.

World axes: x runs down-right, y runs down-left, z is up. One world unit = 1 px across, 0.5 px down.
Every face is drawn pixel by pixel: each screen pixel is mapped back to the world point on that face,
and a texture function picks a palette ramp and a shade for it. Face lighting then shifts the shade.
"""
import numpy as np
from PIL import Image, ImageDraw

def hx(c): return tuple(int(c[i:i+2], 16) for i in (1, 3, 5))
def ramp(*cs): return [hx(c) for c in cs]

R = {
 'plaster': ramp('#2e281e', '#544a38', '#8a7c5e', '#b8a882', '#d8caa2', '#ece0bc'),
 'beam': ramp('#0e0806', '#1e120a', '#301e12', '#46301c', '#5c4226', '#74563a'),
 'rooftile': ramp('#1a0a0e', '#2e1218', '#461c24', '#5e2830', '#76363c', '#90484a'),
 'roofblue': ramp('#0a0e1c', '#121a32', '#1c284c', '#283a68', '#384e86', '#4c66a4'),
 'roofslate': ramp('#0c0e14', '#161a24', '#222836', '#30384a', '#404a60', '#545e76'),
 'roofpurple': ramp('#120a1c', '#20123a', '#301c54', '#42286e', '#563888', '#6c4ca2'),
 'roofgreen': ramp('#0a140c', '#122216', '#1c3420', '#28482c', '#365e38', '#4a7648'),
 'thatch': ramp('#1e1608', '#3a2a10', '#5a4218', '#7c5c22', '#9c7a30', '#bc9a44'),
 'stone': ramp('#121216', '#22222a', '#34343e', '#484852', '#5e5e6a', '#787884'),
 'marble': ramp('#3a3a42', '#5e5e68', '#86868e', '#acacb4', '#cfcfd6', '#ececf2'),
 'wood': ramp('#140c06', '#28180c', '#3e2614', '#56361e', '#6e482a', '#8a5e38'),
 'cobble': ramp('#16161a', '#24242a', '#34343c', '#45454e', '#575762', '#6c6c78'),
 'dirt': ramp('#1a140c', '#2a2014', '#3c2e1c', '#4e3e26', '#605032', '#746440'),
 'grass': ramp('#0e1a0e', '#162816', '#1e381e', '#284a26', '#345e30', '#44743c'),
 'leaf': ramp('#08140a', '#0e2212', '#16341c', '#204a26', '#2c6232', '#3e7c40'),
 'glow': ramp('#3a1a06', '#7a3a0a', '#c06a14', '#e8a030', '#ffd060', '#fff0b0'),
 'fire': ramp('#5a0a04', '#a02408', '#e05a10', '#ff8a20', '#ffc040', '#fff2a0'),
 'water': ramp('#061428', '#0c2444', '#163a66', '#22548a', '#3672aa', '#5c96c8'),
 'gold': ramp('#2a1a04', '#543408', '#805010', '#ab7420', '#d49c34', '#f2c858'),
 'iron': ramp('#0c0d10', '#181a20', '#262a32', '#363b46', '#4a505e', '#626a7a'),
 'cloth_blue': ramp('#060a1c', '#0e1838', '#182a5c', '#243e82', '#3254a6', '#466ec4'),
 'cloth_red': ramp('#1a0406', '#360a0e', '#561418', '#781e22', '#982c2c', '#b44038'),
 'white': ramp('#2e2c2a', '#504c48', '#7a7670', '#a6a29a', '#cecac2', '#eeeae2'),
 'moss': ramp('#141c10', '#22301a', '#344626', '#4a6034', '#627a44', '#7c9456'),
 'dark': ramp('#000000', '#030304', '#07070a', '#0c0c10', '#121218', '#18181e'),
}
OUT = hx('#060406')

def hsh(*a):
    h = 0
    for v in a: h = (h * 1000003) ^ int(v * 7919 + 13) & 0xFFFFFFFF
    h = (h ^ (h >> 13)) * 0x5bd1e995 & 0xFFFFFFFF
    return ((h ^ (h >> 15)) & 0xFFFF) / 65535.0

class Iso:
    def __init__(self, W=96, H=96, ox=48, oy=72):
        self.W, self.H, self.ox, self.oy = W, H, ox, oy
        self.rgb = np.zeros((H, W, 3), np.uint8)
        self.a = np.zeros((H, W), bool)

    def P(self, x, y, z=0):
        return (self.ox + (x - y), self.oy + (x + y) / 2 - z)

    # --- low level ---
    def _mask(self, pts2d):
        im = Image.new('L', (self.W, self.H), 0)
        ImageDraw.Draw(im).polygon([(round(x), round(y)) for x, y in pts2d], fill=1, outline=1)
        return np.array(im).astype(bool)

    def put(self, x, y, c):
        x, y = int(round(x)), int(round(y))
        if 0 <= x < self.W and 0 <= y < self.H: self.rgb[y, x] = c; self.a[y, x] = True

    def face(self, pts, plane, tex, shift=0, u0=0):
        """pts: world polygon. plane: ('x',X0) | ('y',Y0) | ('p',a,b,c) meaning z = a*x + b*y + c."""
        m = self._mask([self.P(*p) for p in pts])
        ys, xs = np.nonzero(m)
        for py, px in zip(ys, xs):
            d = px + .5 - self.ox; e = py + .5 - self.oy
            if plane[0] == 'x':
                X0 = plane[1]; y = X0 - d; z = (X0 + y) / 2 - e; x = X0; u, v = y, z
            elif plane[0] == 'y':
                Y0 = plane[1]; x = d + Y0; z = (x + Y0) / 2 - e; y = Y0; u, v = x, z
            else:
                a, b, c = plane[1:]
                den = 1 - a - b
                if abs(den) < 1e-3: continue
                y = (e - d / 2 + a * d + c) / den; x = y + d; z = a * x + b * y + c; u, v = x, y
            r = tex(x, y, z, u - u0, v)
            if r is None: continue
            rp, lv = r
            rp = R[rp] if isinstance(rp, str) else rp
            lv = int(max(0, min(len(rp) - 1, round(lv + shift))))
            self.rgb[py, px] = rp[lv]; self.a[py, px] = True

    # --- shapes ---
    def box(self, x0, y0, z0, dx, dy, dz, top=None, left=None, right=None):
        x1, y1, z1 = x0 + dx, y0 + dy, z0 + dz
        if right: self.face([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], ('x', x1), right, -1, u0=y0)
        if left: self.face([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], ('y', y1), left, 0, u0=x0)
        if top: self.face([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], ('p', 0, 0, z1), top, 1)

    def gable_x(self, x0, y0, x1, y1, H, rise, wall_left, wall_right, roof, o=2):
        """Walls plus a gable roof whose ridge runs along x. The right wall carries the gable triangle."""
        yc = (y0 + y1) / 2; zt = H + rise; k = rise / (yc - y0)
        self.face([(x1, y0, 0), (x1, y1, 0), (x1, y1, H), (x1, yc, zt), (x1, y0, H)], ('x', x1), wall_right, -1, u0=y0)
        self.face([(x0, y1, 0), (x1, y1, 0), (x1, y1, H), (x0, y1, H)], ('y', y1), wall_left, 0, u0=x0)
        ze = H - o * k; L = yc - y0 + o
        self.face([(x0 - o, y0 - o, ze), (x1 + o, y0 - o, ze), (x1 + o, yc, zt), (x0 - o, yc, zt)], ('p', 0, k, zt - k * yc), lambda x, y, z, u, v: roof(u - x0 + o, y - (y0 - o), L), -1)
        self.face([(x0 - o, yc, zt), (x1 + o, yc, zt), (x1 + o, y1 + o, ze), (x0 - o, y1 + o, ze)], ('p', 0, -k, zt + k * yc), lambda x, y, z, u, v: roof(u - x0 + o, (y1 + o) - y, L), 0)
        return yc, zt

    def gable_y(self, x0, y0, x1, y1, H, rise, wall_left, wall_right, roof, o=2):
        """Walls plus a gable roof whose ridge runs along y. The left wall carries the gable triangle."""
        xc = (x0 + x1) / 2; zt = H + rise; k = rise / (xc - x0)
        self.face([(x1, y0, 0), (x1, y1, 0), (x1, y1, H), (x1, y0, H)], ('x', x1), wall_right, -1, u0=y0)
        self.face([(x0, y1, 0), (x1, y1, 0), (x1, y1, H), (xc, y1, zt), (x0, y1, H)], ('y', y1), wall_left, 0, u0=x0)
        ze = H - o * k; L = xc - x0 + o
        self.face([(x0 - o, y0 - o, ze), (xc, y0 - o, zt), (xc, y1 + o, zt), (x0 - o, y1 + o, ze)], ('p', k, 0, zt - k * xc), lambda x, y, z, u, v: roof(v - y0 + o, x - (x0 - o), L), 0)
        self.face([(xc, y0 - o, zt), (x1 + o, y0 - o, ze), (x1 + o, y1 + o, ze), (xc, y1 + o, zt)], ('p', -k, 0, zt + k * xc), lambda x, y, z, u, v: roof(v - y0 + o, (x1 + o) - x, L), -1)
        return xc, zt

    def ground(self, x0, y0, x1, y1, tex, thick=0):
        self.face([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], ('p', 0, 0, 0), tex, 0)

    # --- 2D helpers in screen space ---
    def ellipse(self, cx, cy, rx, ry, rp, lv=3, shade=True):
        rp = R[rp] if isinstance(rp, str) else rp
        for py in range(int(cy - ry - 1), int(cy + ry + 2)):
            for px in range(int(cx - rx - 1), int(cx + rx + 2)):
                dx, dy = (px + .5 - cx) / rx, (py + .5 - cy) / ry
                d = dx * dx + dy * dy
                if d <= 1:
                    l = lv + (1 if shade and dx + dy < -.5 else -1 if shade and dx + dy > .7 else 0)
                    self.put(px, py, rp[max(0, min(len(rp) - 1, l))])

    def rect(self, x0, y0, x1, y1, c):
        for py in range(int(y0), int(y1)):
            for px in range(int(x0), int(x1)): self.put(px, py, c)

    def line(self, a, b, c):
        (x0, y0), (x1, y1) = a, b
        n = int(max(abs(x1 - x0), abs(y1 - y0))) + 1
        for i in range(n + 1):
            t = i / max(1, n); self.put(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, c)

    # --- props ---
    def barrel(self, x, y, z=0, s=1.0):
        cx, cy = self.P(x, y, z)
        w, hgt = 3.2 * s, 6 * s
        for py in range(int(cy - hgt), int(cy) + 1):
            for px in range(int(cx - w), int(cx + w) + 1):
                t = (px + .5 - cx) / w
                if abs(t) <= 1:
                    lv = 3 if t < -.3 else 2 if t < .4 else 1
                    hoop = int(cy - py) in (1, int(hgt * .55), int(hgt) - 1)
                    self.put(px, py, R['iron'][lv + 1] if hoop else R['wood'][lv + 1])
        self.ellipse(cx, cy - hgt, w, w * .45, 'wood', 4, False)
        self.ellipse(cx, cy - hgt, w * .6, w * .25, 'wood', 2, False)

    def crate(self, x, y, s=4):
        self.box(x, y, 0, s, s, s, top=lambda *a: ('wood', 4 if (a[3] + a[4]) % 3 < 1 else 3), left=lambda *a: ('wood', 3 if a[3] % 2 < 1 else 2), right=lambda *a: ('wood', 3 if a[3] % 2 < 1 else 2))

    def bush(self, x, y, r=3.5, rp='leaf'):
        cx, cy = self.P(x, y, 0)
        self.ellipse(cx, cy - r * .7, r, r * .8, rp, 3)
        for i in range(4): self.put(cx - r * .5 + i * r * .35, cy - r * 1.1 + (i % 2), R[rp][5])

    def tree(self, x, y, h=10, r=6):
        cx, cy = self.P(x, y, 0)
        for py in range(int(cy - h), int(cy) + 1):
            self.put(cx, py, R['wood'][3]); self.put(cx - 1, py, R['wood'][2])
        self.ellipse(cx, cy - h - r * .3, r, r * .85, 'leaf', 3)
        self.ellipse(cx - r * .3, cy - h - r * .6, r * .55, r * .45, 'leaf', 4)

    def flame(self, cx, cy, s=1.0):
        self.ellipse(cx, cy - 2 * s, 2.2 * s, 3 * s, 'fire', 2, False)
        self.ellipse(cx, cy - 1.6 * s, 1.4 * s, 2 * s, 'fire', 4, False)
        self.put(cx, cy - 1, R['fire'][5])

    def lamp(self, x, y, z):
        cx, cy = self.P(x, y, z)
        self.rect(cx - 1, cy - 1, cx + 2, cy + 2, R['glow'][4]); self.put(cx, cy, R['glow'][5]); self.put(cx, cy - 2, R['iron'][1])

    # --- finishing ---
    def outline(self, c=OUT):
        a = self.a
        nb = np.zeros_like(a)
        nb[1:, :] |= a[:-1, :]; nb[:-1, :] |= a[1:, :]; nb[:, 1:] |= a[:, :-1]; nb[:, :-1] |= a[:, 1:]
        o = nb & ~a
        self.rgb[o] = c; self.a = self.a | o

    def image(self):
        out = np.zeros((self.H, self.W, 4), np.uint8)
        out[..., :3] = self.rgb; out[..., 3] = self.a * 255
        return Image.fromarray(out, 'RGBA')

# ---------- textures ----------
def timber(w, h, levels=(0.5,), bays=7, braces=True, base='plaster', beam='beam', openings=()):
    """Plaster panels framed by dark beams. openings: list of (u0, v0, u1, v1, kind)."""
    def t(x, y, z, u, v):
        for (u0, v0, u1, v1, kind) in openings:
            if u0 <= u <= u1 and v0 <= v <= v1: return opening(kind, u - u0, v - v0, u1 - u0, v1 - v0)
        if v < 2.2: return ('stone', 2 + (hsh(int(u / 3), int(v)) > .5))
        edge = min(u % bays, bays - u % bays)
        if edge < .9 or u < .9 or abs(u - w) < .9: return (beam, 3 if edge < .45 else 2)
        for lv in levels:
            if abs(v - h * lv) < .7: return (beam, 3)
        if abs(v - h) < .8 or abs(v - 2.2) < .7: return (beam, 2)
        if braces:
            cu = (u % bays) / bays; seg = h * levels[0]
            if v < seg:
                dv = v / seg
                if abs(cu - dv) < .11 and int(u / bays) % 2 == 0: return (beam, 2)
        return (base, 4 if hsh(int(u), int(v)) > .25 else 3)
    return t

def stonewall(rp='stone', bw=5, bh=3, openings=()):
    def t(x, y, z, u, v):
        for (u0, v0, u1, v1, kind) in openings:
            if u0 <= u <= u1 and v0 <= v <= v1: return opening(kind, u - u0, v - v0, u1 - u0, v1 - v0)
        row = int(v // bh); off = (bw / 2) * (row % 2)
        if v % bh < .7 or (u + off) % bw < .7: return (rp, 1)
        return (rp, 3 + (hsh(int((u + off) // bw), row) > .6) - (hsh(int((u + off) // bw), row, 3) > .85))
    return t

def logs(rp='wood', openings=()):
    def t(x, y, z, u, v):
        for (u0, v0, u1, v1, kind) in openings:
            if u0 <= u <= u1 and v0 <= v <= v1: return opening(kind, u - u0, v - v0, u1 - u0, v1 - v0)
        f = (v % 3) / 3
        return (rp, 1 if f < .2 else 4 if f > .65 else 3)
    return t

def opening(kind, du, dv, w, h):
    edge = du < .8 or dv < .6 or w - du < .8 or h - dv < .8
    if kind == 'door':
        if edge: return ('beam', 1)
        if abs(du - w * .5) < .45: return ('beam', 1)
        if abs(dv - h * .7) < .4 or abs(dv - h * .3) < .4: return ('iron', 3)
        return ('wood', 3 + (int(du) % 2))
    if kind == 'window':
        if edge: return ('beam', 1)
        if abs(du - w / 2) < .4 or abs(dv - h / 2) < .4: return ('beam', 2)
        return ('glow', 4 if dv > h * .5 else 3)
    if kind == 'darkwin':
        if edge: return ('beam', 1)
        return ('roofslate', 2 + (abs(du - w / 2) < .4))
    if kind == 'open':
        if edge and dv > .6: return ('beam', 2)
        return ('glow', 2 + int(3 * (1 - dv / h)) if dv < h * .8 else 1)
    if kind == 'dark':
        return ('dark', 1)
    return ('beam', 2)

def tiles(rp, tw=4, th=3, trim='wood'):
    def t(u, s, L):
        if s < 1 or s > L - .8: return (trim, 4 if s < 1 else 3)
        row = int((s - 1) // th); off = (tw / 2) * (row % 2)
        n = hsh(int((u + off) // tw), row)
        f = (s - 1) % th
        if f < .7: return (rp, 1)
        if (u + off) % tw < .6: return (rp, 2)
        lv = 3 + (n > .72) - (n < .14)
        if f > th - .9: lv += 1
        return (rp, lv)
    return t

def thatch(rp='thatch'):
    def t(u, s, L):
        if s < 1: return ('wood', 3)
        if s > L - 1.2: return (rp, 1)
        n = hsh(int(u), int(s // 2))
        return (rp, 2 + (n > .4) + (n > .8) + ((s % 2) > 1.3))
    return t

def cobble(scale=4):
    def t(x, y, z, u, v):
        gx, gy = x / scale, y / scale
        ix, iy = int(np.floor(gx)), int(np.floor(gy))
        best, second, bid = 9, 9, None
        for ox in (-1, 0, 1):
            for oy in (-1, 0, 1):
                cx, cy = ix + ox + .2 + .6 * hsh(ix + ox, iy + oy), iy + oy + .2 + .6 * hsh(iy + oy, ix + ox, 7)
                d = (gx - cx) ** 2 + (gy - cy) ** 2
                if d < best: second, best, bid = best, d, (ix + ox, iy + oy)
                elif d < second: second = d
        if second - best < .12: return ('cobble', 1)
        return ('cobble', 3 + (hsh(*bid, 2) > .55) - (hsh(*bid, 5) > .85))
    return t

def grass():
    def t(x, y, z, u, v):
        n = hsh(int(x), int(y))
        if n > .993: return ('white', 4) if hsh(int(x), int(y), 9) > .4 else ('gold', 4)
        return ('grass', 2 + (n > .5) + (n > .9))
    return t
