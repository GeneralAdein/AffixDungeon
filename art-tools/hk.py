import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pxlib
pxlib.FLAT['on'] = True
from pxlib import *

# ---------- palettes ----------
P = {
 'skin':['#2a1810','#4e3020','#76492e','#9c6640','#bc8456','#d8a270'],
 'skinlt':['#3a2418','#62402c','#8c6044','#b4825e','#d4a27a','#ecc49a'],
 'skindk':['#160c08','#2e1a10','#4a2c1c','#6a4028','#8a5636','#a87048'],
 'pale':['#262428','#46424a','#6a646e','#908894','#b4acb6','#d4ccd4'],
 'goblin':['#0c1608','#18300f','#284a18','#3c6624','#548232','#72a046'],
 'hob':['#1c0a04','#3a1608','#5e260e','#843a16','#a8521e','#c86e30'],
 'orc':['#0c1408','#1a2c10','#2a4418','#3c5e22','#52782e','#6c943e'],
 'kobold':['#1c0806','#3a120a','#5c1e10','#802e18','#a24222','#c05c30'],
 'gnoll':['#1a1208','#362410','#56381a','#784e24','#9a6832','#b88644'],
 'lizard':['#08140c','#102a16','#1a4422','#286030','#3a7e40','#529c54'],
 'trog':['#0e1014','#1c2026','#2c323a','#40484f','#566068','#707a82'],
 'drow':['#0c0812','#181024','#261a38','#36264e','#483466','#5e4482'],
 'dwarf':['#1e1210','#3a241e','#5a382e','#7c4e40','#9c6854','#ba846c'],
 'fur':['#140c06','#2a1a0c','#422a14','#5c3e1e','#78562a','#94703a'],
 'crimson':['#1e0408','#3c0a10','#64121c','#8c1e2a','#b4303a','#d84c50'],
 'red':['#1c0604','#3a0c08','#601610','#88241a','#ae3624','#cc5034'],
 'navy':['#05081a','#0c1432','#16224e','#22346c','#30488c','#4460a8'],
 'blue':['#06101e','#0c1e3a','#163460','#204c86','#2e66aa','#4688c8'],
 'royal':['#0a0a24','#141648','#1e2470','#2a3698','#3a4cbc','#5466d8'],
 'green':['#06120a','#0c2414','#143a20','#1e522c','#2a6c3a','#3c8a4c'],
 'forest':['#0a1206','#14220c','#203614','#2e4c1e','#3e6428','#527e36'],
 'purple':['#0e0618','#1c0c30','#2c1450','#3e1e70','#542c90','#6e40b0'],
 'violet':['#140a1c','#281438','#40205a','#5a2e7c','#783e9e','#9454bc'],
 'black':['#050507','#0c0c10','#16161c','#222228','#303038','#42424c'],
 'gray':['#101012','#202024','#323238','#46464e','#5e5e68','#7a7a84'],
 'white':['#2e2c2a','#504c48','#7a7670','#a6a29a','#cecac2','#eeeae2'],
 'orange':['#1e0c02','#3c1a04','#602a08','#86400e','#ac5a18','#d07a28'],
 'saffron':['#241402','#4a2a06','#74440c','#9e6214','#c6841e','#e8a830'],
 'brown':['#140c06','#2a180c','#422614','#5c381e','#784c2a','#94643a'],
 'leather':['#140a04','#2c1608','#4a2810','#6a3c1a','#8a5426','#a86e38'],
 'dleather':['#0a0604','#160e08','#24180e','#342416','#46321e','#5a4228'],
 'tan':['#1e1408','#3c2810','#5c4018','#7e5a22','#a0762e','#c09440'],
 'steel':['#14181e','#2a3240','#46546a','#6c7e96','#9cb0c6','#d4e2f0'],
 'dsteel':['#08090c','#14161c','#20242c','#30343e','#444a56','#5c6474'],
 'bronze':['#1c1006','#3a200a','#5c3410','#82501a','#a86e28','#cc9040'],
 'gold':['#2a1a04','#543408','#805010','#ab7420','#d49c34','#f2c858'],
 'wood':['#140c07','#2b1a0e','#472b16','#64401f','#83582c','#a07440'],
 'bone':['#1d1a16','#38322a','#5a5246','#82786a','#aaa08e','#d0c8b2'],
 'pants':['#0e0a08','#1c1410','#2c2018','#3c2c20','#4e3a2a'],
 'boot':['#060506','#0e0c0e','#1a171a','#282428','#3a3438'],
}
GOLD = '#e8b83a'; GOLDD = '#9c6c10'; WHITE = '#f8f2e8'; INK = '#1a0a06'

class Fig:
    def __init__(self, outline='#080406', k=1.0, w=1.0, ox=0.0):
        self.s = Sprite(outline); self.k = k; self.w = w; self.ox = ox
    # coordinate transform: ground stays at y=46
    def T(self, x, y): return (24 + self.ox + (x - 24) * self.w * self.k, 46 - (46 - y) * self.k)
    def E(self, cx, cy, rx, ry, rot=0):
        x, y = self.T(cx, cy); return ellipse(x, y, rx * self.w * self.k, ry * self.k, rot)
    def C(self, pts, r1, r2=None):
        return chain([self.T(*p) for p in pts], r1 * self.k, (r2 if r2 is not None else r1) * self.k)
    def Pp(self, pts): return poly([self.T(*p) for p in pts])
    def add(self, mask, ramp, **kw):
        if isinstance(ramp, str): ramp = P[ramp]
        return self.s.add(mask, ramp, **kw)
    def px(self, pts, c, a=255):
        self.s.px([tuple(int(round(v)) for v in self.T(x, y)) for x, y in pts], c, a)
    def mask(self, m, c, a=255): self.s.maskpx(m, c, a)
    def render(self): return self.s.render()

    # ---------- body ----------
    def legs(self, stance='stand', pants='pants', boots='boot', cuff=None, hip=30):
        L = {'stand': ([(21, hip), (20.5, 38), (20, 45)], [(27, hip), (27.5, 38), (28, 45)]),
             'wide': ([(21, hip), (17.5, 38), (15, 45)], [(27, hip), (30.5, 38), (33, 45)]),
             'lunge': ([(21, hip), (16, 37), (13, 45)], [(27, hip), (29, 38), (28.5, 45)]),
             'crouch': ([(21, hip), (16, 36), (17, 45)], [(27, hip), (32, 36), (31, 45)])}[stance]
        l, r = L
        self.add(self.C(l, 2.6, 2.2) | self.C(r, 2.6, 2.2), pants)
        if boots:
            self.add(self.C([l[1], l[2]], 2.7, 2.7) & (yy > self.T(0, 39.5)[1]) | self.C([r[1], r[2]], 2.7, 2.7) & (yy > self.T(0, 39.5)[1]), boots)
            if cuff: self.px([(l[1][0] - 1 + (l[2][0] - l[1][0]) * .3, 40), (l[1][0] + (l[2][0] - l[1][0]) * .3, 40), (r[1][0] + (r[2][0] - r[1][0]) * .3, 40), (r[1][0] + 1 + (r[2][0] - r[1][0]) * .3, 40)], cuff)
        return l[2], r[2]

    def torso(self, ramp, top=17, bot=30, wt=7, wb=6, cx=24):
        self.add(self.Pp([(cx - wt, top), (cx + wt, top), (cx + wb, bot), (cx - wb, bot)]), ramp, soft=1.3)

    def robe(self, ramp, top=17, wt=7, wb=10.5, hem=46, cx=24, slit=True):
        self.add(self.Pp([(cx - wt, top), (cx + wt, top), (cx + wb, hem), (cx - wb, hem)]), ramp, soft=1.6)
        if slit: self.mask(self.C([(cx, 31), (cx, hem)], .45), P[ramp][1] if isinstance(ramp, str) else ramp[1])

    def tails(self, ramp, y=29, cx=24):
        self.add(self.Pp([(cx - 6, y), (cx + 6, y), (cx + 8.5, y + 7), (cx + 3, y + 5), (cx, y + 7), (cx - 3, y + 5), (cx - 8.5, y + 7)]), ramp, bias=-.08)

    def belt(self, y=29.5, ramp='leather', buckle=GOLD, cx=24, w=6.2):
        self.add(self.C([(cx - w, y), (cx + w, y)], 1.1), ramp, flat=1)
        if buckle: self.px([(cx - 1, y - .5), (cx, y - .5), (cx + 1, y - .5), (cx - 1, y + .5), (cx + 1, y + .5)], buckle)

    def arm(self, sh, el, hand, ramp, hand_ramp='skin', hand_r=1.9, r1=2.2, r2=1.8):
        self.add(self.C([sh, el, hand], r1, r2), ramp, bias=.05)
        self.add(self.E(hand[0], hand[1], hand_r, hand_r), hand_ramp, bias=.12)

    def pauldron(self, x, y, ramp='steel', rx=3.4, ry=2.4):
        self.add(self.E(x, y, rx, ry), ramp, bias=.1); self.px([(x - 1, y - 1)], '#ffffff', 200)

    def cape(self, ramp, lining=None, side='right', top=17):
        if side == 'right':
            pts = [(18, top), (30, top), (37, top + 7), (43, top + 19), (45, 46), (38, 42), (33, 46), (29, 38), (22, 34)]
            lin = [(37, top + 13), (43, top + 19), (45, 46), (41, 42)]
        elif side == 'left':
            pts = [(30, top), (18, top), (11, top + 7), (5, top + 19), (3, 46), (10, 42), (15, 46), (19, 38), (26, 34)]
            lin = [(11, top + 13), (5, top + 19), (3, 46), (7, 42)]
        else:
            pts = [(17, top), (31, top), (36, 46), (30, 43), (24, 46), (18, 43), (12, 46)]
            lin = None
        self.add(self.Pp(pts), ramp, soft=1.6)
        if lining and lin: self.add(self.Pp(lin), lining, bias=-.05)

    # ---------- heads ----------
    def head(self, ramp, hx=24, hy=11, rx=5, ry=5.8, jaw=True):
        self.add(self.E(24 + (hx - 24), hy, rx, ry), ramp, soft=1.2)
        if jaw: self.add(self.E(hx, hy + 4, rx * .74, 2), ramp, bias=.05)

    def face(self, hx=24, hy=11, mood='angry', eye=None, brow=INK, mouth=INK, skin='skin', teeth=False, glow=False):
        sk = P[skin] if isinstance(skin, str) else skin
        ey = hy + .2
        if glow:
            self.px([(hx - 2.5, ey), (hx + 2.5, ey)], eye)
            self.px([(hx - 3.5, ey), (hx + 3.5, ey)], eye, 120)
        else:
            self.px([(hx - 3, ey), (hx - 2, ey), (hx + 2, ey), (hx + 3, ey)], WHITE)
            pc = eye or '#14222e'
            if mood in ('sly', 'cold'): self.px([(hx - 3, ey), (hx + 2, ey)], pc)
            else: self.px([(hx - 2, ey), (hx + 2, ey)], pc)
        by = hy - 1.6
        if mood in ('angry', 'mad', 'grin'):
            self.px([(hx - 4, by), (hx - 3, by), (hx - 2, by + 1), (hx + 4, by), (hx + 3, by), (hx + 2, by + 1)], brow)
        elif mood == 'sly':
            self.px([(hx - 4, by + 1), (hx - 3, by), (hx - 2, by), (hx + 2, by + 1), (hx + 3, by + 1), (hx + 4, by + 1)], brow)
        elif mood == 'sad':
            self.px([(hx - 4, by + 1), (hx - 3, by), (hx + 4, by + 1), (hx + 3, by)], brow)
        elif mood != 'none':
            self.px([(hx - 4, by), (hx - 3, by), (hx - 2, by), (hx + 2, by), (hx + 3, by), (hx + 4, by)], brow)
        self.px([(hx, hy + 2), (hx, hy + 3)], sk[2])
        my = hy + 4.6
        if mood == 'grin' or teeth:
            self.px([(hx - 2, my), (hx - 1, my), (hx, my), (hx + 1, my), (hx + 2, my)], mouth)
            self.px([(hx - 1, my), (hx, my), (hx + 1, my)], WHITE)
        elif mood == 'mad':
            self.px([(hx - 2, my), (hx - 1, my + .6), (hx, my), (hx + 1, my + .6), (hx + 2, my)], mouth); self.px([(hx - 1, my), (hx + 1, my)], WHITE)
        elif mood == 'sly':
            self.px([(hx - 1, my), (hx, my), (hx + 1, my), (hx + 2, my - 1)], mouth)
        elif mood == 'sad':
            self.px([(hx - 1, my), (hx, my - .5), (hx + 1, my)], mouth)
        elif mood != 'none':
            self.px([(hx - 1.5, my), (hx - .5, my), (hx + .5, my), (hx + 1.5, my)], mouth)

    def hair(self, ramp, style='short', hx=24, hy=11, hi=None):
        top = hy - 4.4
        if style == 'short': m = self.E(hx, top, 5.6, 3.2) & (yy < self.T(0, hy - 2.6)[1])
        elif style == 'swept': m = (self.E(hx, top, 6, 3.4) & (yy < self.T(0, hy - 2.8)[1])) | self.Pp([(hx + 2, top - 2), (hx + 9, top + 1), (hx + 5, top + 3)]) | self.Pp([(hx - 6, top + 1), (hx - 7.5, hy + 1), (hx - 5, top + 3)])
        elif style == 'long': m = (self.E(hx, top + .6, 6, 3.8) & (yy < self.T(0, hy - 2)[1])) | self.Pp([(hx - 5.8, top + 1), (hx - 7, hy + 9), (hx - 4.4, hy + 6), (hx - 4.6, top + 3)]) | self.Pp([(hx + 5.8, top + 1), (hx + 7, hy + 9), (hx + 4.4, hy + 6), (hx + 4.6, top + 3)])
        elif style == 'topknot': m = (self.E(hx, top + 1, 5.4, 2.6) & (yy < self.T(0, hy - 2.6)[1])) | self.E(hx, top - 2.2, 1.8, 1.8)
        elif style == 'mohawk': m = self.Pp([(hx - 1.4, top - 4), (hx + 1.4, top - 4), (hx + 1.6, hy - 2), (hx - 1.6, hy - 2)])
        elif style == 'wild': m = (self.E(hx, top, 6.4, 3.6) & (yy < self.T(0, hy - 2.4)[1])) | self.Pp([(hx - 6, top), (hx - 9, top - 2), (hx - 6.5, top + 3)]) | self.Pp([(hx + 6, top), (hx + 9, top - 3), (hx + 6.5, top + 3)]) | self.Pp([(hx - 1, top - 2), (hx + 1, top - 5), (hx + 3, top - 1)])
        self.add(m, ramp, soft=1)
        if hi: self.px([(hx - 2, top - 1), (hx - 1, top - 1.4), (hx + 2, top - 1)], hi)

    def beard(self, ramp, hx=24, hy=11, length=10, braid=False):
        m = self.Pp([(hx - 5, hy + 1.5), (hx + 5, hy + 1.5), (hx + 4, hy + length * .6), (hx + 1.5, hy + length), (hx - 1.5, hy + length), (hx - 4, hy + length * .6)])
        self.add(m, ramp, soft=1)
        self.px([(hx - 1.5, hy + 4.4), (hx - .5, hy + 4.4), (hx + .5, hy + 4.4), (hx + 1.5, hy + 4.4)], INK)
        if braid: self.px([(hx, hy + length + 1), (hx, hy + length + 2)], GOLD)

    def hood(self, ramp, hx=24, hy=11, deep=False):
        r = P[ramp] if isinstance(ramp, str) else ramp
        self.add(self.E(hx, hy - .4, 7, 7.6) & ~self.E(hx, hy + 1.4, 4.4, 5) | self.Pp([(hx - 6.6, hy + 2), (hx + 6.6, hy + 2), (hx + 8, hy + 8), (hx - 8, hy + 8)]) & ~self.E(hx, hy + 1.4, 4.4, 5), ramp, soft=1.4)
        self.mask(self.E(hx, hy - 1.4, 4.6, 1.6) & (yy < self.T(0, hy - 1)[1]), r[0])
        if deep: self.mask(self.E(hx, hy + 1, 4.4, 4.6) & (yy < self.T(0, hy + 1)[1]), r[0])

    # ---------- weapons ----------
    def sword(self, hand, tip, blade='steel', guard=GOLD, pommel='#c8203a', w=1.4, gleam=True):
        hx, hy = hand; tx, ty = tip
        L = ((tx - hx) ** 2 + (ty - hy) ** 2) ** .5; ux, uy = (tx - hx) / L, (ty - hy) / L
        self.add(self.C([(hx + ux * 1.5, hy + uy * 1.5), tip], w, w * .5), blade, bias=.15)
        self.mask(self.C([(hx + ux * 2.5 + uy * .4, hy + uy * 2.5 - ux * .4), (tx - ux * 1.5, ty - uy * 1.5)], .35), '#e8f2ff')
        gx, gy = hx + ux * 1.5, hy + uy * 1.5
        self.add(self.C([(gx - uy * 3.2, gy + ux * 3.2), (gx + uy * 3.2, gy - ux * 3.2)], .9), [GOLDD, guard, '#f8dc80'] if guard == GOLD else [guard, guard, guard], flat=1)
        self.add(self.C([(hx, hy), (hx - ux * 2.6, hy - uy * 2.6)], .9), 'leather')
        self.px([(hx - ux * 3.4, hy - uy * 3.4)], pommel)
        if gleam:
            gx2, gy2 = tx - ux * 3, ty - uy * 3
            for d, a in [((0, 0), 255), ((1, 0), 255), ((-1, 0), 255), ((0, 1), 255), ((0, -1), 255), ((2, 0), 120), ((-2, 0), 120), ((0, 2), 120), ((0, -2), 120)]:
                self.px([(gx2 + d[0], gy2 + d[1])], '#ffffff', a)

    def dagger(self, hand, tip, blade='steel'):
        self.sword(hand, tip, blade=blade, w=1.0, gleam=False, pommel=GOLDD)

    def haft(self, a, b, ramp='wood', r=.85): self.add(self.C([a, b], r), ramp)

    def axehead(self, top, side=-1, ramp='steel', big=False):
        x, y = top; s = side; h = 7 if big else 5; wd = 8 if big else 6
        self.add(self.Pp([(x, y - 1), (x + s * wd, y - h * .6), (x + s * (wd + 1), y + h * .5), (x + s * wd * .6, y + h * .9), (x, y + h * .4)]), ramp, bias=.1)
        self.mask(self.C([(x + s * (wd + .4), y - h * .5), (x + s * (wd + .6), y + h * .4)], .4), '#e8f2ff')

    def spearhead(self, tip, d=(0, -1), ramp='steel'):
        x, y = tip; dx, dy = d
        self.add(self.Pp([(x + dx * 5 - dy * 1.6, y + dy * 5 + dx * 1.6), (x, y), (x + dx * 5 + dy * 1.6, y + dy * 5 - dx * 1.6), (x + dx * 6.5, y + dy * 6.5)]), ramp, bias=.1)

    def shield(self, c, kind='round', ramp='wood', rim='steel', emblem=None, emblem_c=GOLD, r=6):
        x, y = c
        if kind == 'round':
            self.add(self.E(x, y, r * .9, r), ramp, soft=1.3)
            self.mask(self.E(x, y, r * .9, r) & ~self.E(x, y, r * .9 - 1.1, r - 1.1), P[rim][3])
            self.mask(self.E(x, y, 1.4, 1.4), P[rim][4]); self.px([(x - .5, y - .5)], '#ffffff')
        elif kind == 'kite':
            m = self.Pp([(x - 5, y - 7), (x + 5, y - 7), (x + 5, y), (x, y + 8), (x - 5, y)])
            self.add(m, ramp, soft=1)
            self.mask(m & ~self.Pp([(x - 4, y - 6), (x + 4, y - 6), (x + 4, y - .2), (x, y + 6.6), (x - 4, y - .2)]), P[rim][3])
            if emblem == 'cross': self.mask(self.C([(x, y - 5), (x, y + 4)], .6) | self.C([(x - 3, y - 2), (x + 3, y - 2)], .6), emblem_c)
            if emblem == 'skull': self.px([(x - 1, y - 3), (x, y - 3), (x + 1, y - 3), (x - 1, y - 2), (x + 1, y - 2), (x, y - 1)], emblem_c)
            if emblem == 'sun':
                self.mask(self.E(x, y - 2, 1.8, 1.8), emblem_c)
                self.px([(x, y - 5), (x - 3, y - 2), (x + 3, y - 2), (x, y + 1), (x - 2, y - 4), (x + 2, y - 4)], emblem_c)
        elif kind == 'buckler':
            self.add(self.E(x, y, 3.6, 3.6), ramp, bias=.05); self.mask(self.E(x, y, 1.1, 1.1), P[rim][4])

    def bow(self, cx, cy, h=15, ramp='wood', draw=False):
        pts = [(cx + 2, cy - h / 2), (cx - 1, cy - h / 4), (cx - 2, cy), (cx - 1, cy + h / 4), (cx + 2, cy + h / 2)]
        self.add(self.C(pts, 1, .7), ramp, bias=.1)
        if draw:
            self.mask(self.C([(cx + 2, cy - h / 2), (cx + 7, cy), (cx + 2, cy + h / 2)], .3), '#e8e0c8', 220)
        else:
            self.mask(self.C([(cx + 2, cy - h / 2), (cx + 2, cy + h / 2)], .3), '#e8e0c8', 220)

    def staff(self, bottom, top, ramp='wood', orb=None, orb_r=2.6, head='orb'):
        self.add(self.C([bottom, top], .9), ramp)
        x, y = top
        if head == 'orb' and orb:
            self.add(self.E(x, y - orb_r, orb_r, orb_r), [orb[0], orb[1], orb[2]], soft=1)
            self.px([(x - 1, y - orb_r - 1)], '#ffffff')
            for d in [(-3, -2), (3, -3), (0, -6), (-2, -6), (2, 0)]: self.px([(x + d[0], y - orb_r + d[1])], orb[1], 170)
        elif head == 'skull':
            self.add(self.E(x, y - 2.6, 2.8, 2.6), 'bone', bias=.1)
            self.px([(x - 1, y - 2.6), (x + 1, y - 2.6)], orb[1] if orb else '#60ff80'); self.px([(x, y - 1)], INK)
        elif head == 'crook':
            self.add(self.C([top, (x - 1, y - 4), (x + 2, y - 6), (x + 4, y - 4)], .9), ramp)

    def flame(self, c, cols=('#ff6020', '#ffb040', '#fff0a0'), big=1.0):
        x, y = c
        self.mask(self.E(x, y - 2 * big, 3 * big, 4 * big), cols[0]); self.mask(self.E(x, y - 1.6 * big, 2 * big, 2.8 * big), cols[1]); self.mask(self.E(x, y - 1.2 * big, 1 * big, 1.6 * big), cols[2])
        for d in [(-3, -6), (2, -7), (0, -9), (-1, -11), (3, -4)]: self.px([(x + d[0] * big, y + d[1] * big)], cols[1], 190)
