from hk import *
import base64, io, json

def bust(skin, clothes, mood='calm', eye='#2a3a4a', jaw=1.0, rx=10.5, ry=12, hx=24, hy=21, brow='#2a1a10', behind=None):
    f = Fig()
    if behind: behind(f)
    S = P[skin] if isinstance(skin, str) else skin
    f.add(f.Pp([(2, 48), (46, 48), (42, 38), (32, 34), (16, 34), (6, 38)]), clothes, soft=1.2)          # shoulders
    f.add(f.C([(hx, hy + 8), (hx, 36)], 4.4), S)                                                         # neck
    f.add(f.E(hx - rx - .4, hy + 1, 2, 3) | f.E(hx + rx + .4, hy + 1, 2, 3), S, bias=-.05)              # ears
    f.add(f.E(hx, hy, rx, ry) | f.E(hx, hy + ry * .5, rx * .82 * jaw, ry * .62), S, soft=1.6)           # head and jaw
    f._hx, f._hy, f._S = hx, hy, S
    return f

def eyes(f, eye, mood='calm', brow='#2a1a10', spread=5.5, y=None, size=1):
    hx, hy = f._hx, (y if y is not None else f._hy)
    for s in (-1, 1):
        cx = hx + s * spread
        f.mask(f.E(cx, hy, 2.3 * size, 1.5 * size), WHITE)
        px_ = cx + (0 if mood != 'sly' else -s * .6)
        f.mask(f.E(px_, hy + .2, 1.1 * size, 1.3 * size), eye)
        f.px([(px_, hy + .1)], '#0a0a0e'); f.px([(px_ - .6, hy - .5)], '#ffffff')
        f.mask(f.C([(cx - 2.4, hy - 1.4), (cx + 2.4, hy - 1.4)], .35), f._S[1])                         # upper lid line
        by = hy - 3.4
        if mood in ('angry', 'stern'): pts = [(cx - s * 2.8, by - 1), (cx + s * 2.2, by + .8)]
        elif mood == 'sly': pts = [(cx - 2.6, by + (s > 0) * .8), (cx + 2.6, by - (s > 0) * .6)]
        elif mood == 'kind': pts = [(cx - 2.6, by + .3), (cx, by - .7), (cx + 2.6, by + .3)]
        else: pts = [(cx - 2.6, by), (cx + 2.6, by)]
        f.mask(f.C(pts, .7), brow)

def nose(f, big=1.0):
    hx, hy, S = f._hx, f._hy, f._S
    f.mask(f.C([(hx + .6, hy + 1), (hx + 1.2, hy + 4.6 * big)], .55), S[2])
    f.px([(hx - 1, hy + 5 * big), (hx + 1.8, hy + 5 * big)], S[1])

def mouth(f, kind='smile', y=None, w=3.4):
    hx, hy = f._hx, f._hy; my = y if y is not None else hy + 8
    lip = '#5a1a14'
    if kind == 'smile': f.mask(f.C([(hx - w, my - 1), (hx, my + .8), (hx + w, my - 1)], .5), lip)
    elif kind == 'grin':
        f.mask(f.Pp([(hx - w, my - 1), (hx + w, my - 1), (hx + w * .6, my + 2), (hx - w * .6, my + 2)]), '#3a0a08')
        f.mask(f.Pp([(hx - w + .6, my - .8), (hx + w - .6, my - .8), (hx + w - 1, my + .2), (hx - w + 1, my + .2)]), WHITE)
    elif kind == 'frown': f.mask(f.C([(hx - w, my + 1), (hx, my - .4), (hx + w, my + 1)], .5), lip)
    elif kind == 'flat': f.mask(f.C([(hx - w, my), (hx + w, my)], .45), lip)
    elif kind == 'smirk': f.mask(f.C([(hx - w * .8, my), (hx + w * .4, my), (hx + w, my - 1.4)], .45), lip)

def tobin():
    f = bust('skin', 'brown', jaw=1.08)
    f.add(f.Pp([(14, 48), (34, 48), (32, 36), (16, 36)]), ['#a8a090', '#c8c0b0', '#e8e0d0'], flat=1)             # apron bib
    f.mask(f.C([(17, 36), (19, 48)], .4) | f.C([(31, 36), (29, 48)], .4), '#8a8070')
    f.add(f.E(24, 11, 10, 4) & (yy < f.T(0, 12)[1]) & ~f.E(24, 9, 6, 3), 'brown')                              # balding fringe
    f.add(f.E(13.5, 15, 2.4, 4) | f.E(34.5, 15, 2.4, 4), 'brown')
    eyes(f, '#3a5a2a', 'kind'); nose(f, 1.2)
    f.mask((f.E(18.5, 21, 3, 2.6) & ~f.E(18.5, 21, 2.2, 1.8)) | (f.E(29.5, 21, 3, 2.6) & ~f.E(29.5, 21, 2.2, 1.8)) | f.C([(21.5, 20.6), (26.5, 20.6)], .4), '#9a7a3a')   # spectacles
    f.add(f.Pp([(18, 27), (24, 26), (30, 27), (28, 29.4), (24, 28.4), (20, 29.4)]), 'brown', bias=.05)          # mustache
    mouth(f, 'smile', 31.2, 2.6)
    f.mask(f.E(16.5, 26, 2, 1.2) | f.E(31.5, 26, 2, 1.2), '#c86a5a', 120)
    return f

def hanna():
    f = bust('skinlt', 'green', jaw=1.05)
    f.add(f.C([(8, 40), (20, 36), (22, 48)], 2.6), 'white', bias=.1)                                           # towel
    f.add(f.E(24, 12, 12.5, 7.6) & (yy < f.T(0, 17)[1]), 'orange', dither=True, noise=.5)                    # curly hair
    for (x, y) in ((11, 18), (37, 18), (10, 24), (38, 24), (13, 29), (35, 29)): f.add(f.E(x, y, 3, 3.2), 'orange', dither=True)
    eyes(f, '#2a6a3a', 'kind'); nose(f)
    for p in [(18, 24), (20, 25), (29, 25), (31, 24), (19, 26.5), (30, 26.5)]: f.px([p], '#b06a3a')               # freckles
    f.mask(f.E(17, 26, 2.4, 1.4) | f.E(31, 26, 2.4, 1.4), '#e07a6a', 140)
    mouth(f, 'grin', 30, 3.8)
    return f

def aldric():
    f = bust('skinlt', 'royal')
    f.mask(f.C([(12, 40), (24, 46), (36, 40)], .9), GOLD); f.mask(f.E(24, 46, 2, 2), GOLD); f.px([(24, 46)], '#c8303a')   # chain of office
    f.add(f.E(24, 12, 11, 5.4) & (yy < f.T(0, 14.5)[1]), 'gray')                                               # swept-back hair
    f.add(f.E(13.6, 16, 2, 4) | f.E(34.4, 16, 2, 4), 'gray')
    eyes(f, '#2a3a6a', 'stern', brow='#5a5a62'); nose(f, 1.3)
    f.add(f.Pp([(16, 27), (32, 27), (30, 35), (24, 37.5), (18, 35)]), 'gray', bias=.08)                       # trimmed beard
    mouth(f, 'flat', 29.4, 2.6)
    f.mask(f.C([(17.5, 14.5), (17.5, 16)], .3) | f.C([(30.5, 14.5), (30.5, 16)], .3), P['skinlt'][2])
    return f

def brakka():
    f = bust('skin', 'leather', jaw=1.15, rx=11.2)
    for x in (9, 39): f.add(f.E(x, 39, 6, 4), 'steel', bias=.1)                                                # pauldrons
    eyes(f, '#4a3a20', 'angry', brow='#1a0e08')
    f.mask(f.E(29.5, 21, 3.6, 3.2), '#0a0806'); f.mask(f.C([(13, 15), (35, 17), (36, 23)], .4) | f.C([(26, 18), (14, 24)], .35), '#0a0806')   # eyepatch
    f.mask(f.C([(16, 15), (19, 28)], .45), '#8a3a30'); f.px([(15, 18), (17, 18), (16, 22), (18, 22)], '#8a3a30')                         # scar
    nose(f, 1.3)
    f.mask(f.E(24, 31, 8.6, 5) & (yy > f.T(0, 27)[1]) & (BAYER_T > 0), '#3a3028', 200)                           # stubble
    mouth(f, 'frown', 30)
    f.add(f.E(24, 9.6, 9.4, 3.4) & (yy < f.T(0, 10)[1]), 'skin', bias=.15)                                       # shine on a bald head
    return f

def maren():
    f = bust('skinlt', 'white')
    f.add(f.E(24, 19, 14, 15.5) & ~f.E(24, 22, 10, 12) | f.Pp([(9, 30), (39, 30), (44, 48), (4, 48)]) & ~f.E(24, 22, 10, 12), 'white', soft=1.4)   # hood
    f.mask(f.E(24, 19, 14, 15.5) & ~f.E(24, 19, 13, 14.5) & (yy < f.T(0, 22)[1]), GOLD)
    eyes(f, '#3a6aa0', 'kind', brow='#8a6a4a'); nose(f, .9)
    mouth(f, 'smile', 29.6, 2.4)
    f.mask(f.E(17.5, 26, 2, 1.2) | f.E(30.5, 26, 2, 1.2), '#e8a090', 110)
    f.mask(f.E(24, 4.6, 7, 1.8) & ~f.E(24, 4.6, 5.6, .9), '#ffe08a')
    return f

def wenna():
    f = bust('skinlt', 'forest', jaw=.94)
    f.add(f.Pp([(4, 40), (44, 40), (46, 48), (2, 48)]), 'brown', bias=-.05)                                   # shawl
    f.add(f.E(24, 11, 11, 6) & (yy < f.T(0, 14)[1]) | f.E(24, 5, 4.6, 4), 'gray', bias=.05)                   # gray bun
    for (a, b) in (((16, 24), (19, 25)), ((29, 25), (32, 24)), ((20, 30), (22, 31)), ((26, 31), (28, 30))): f.mask(f.C([a, b], .3), P['skinlt'][2])   # wrinkles
    eyes(f, '#3a5a2a', 'sly', brow='#9a9aa0', size=1.2)
    f.mask((f.E(18.5, 21, 3.6, 3.4) & ~f.E(18.5, 21, 2.8, 2.6)) | (f.E(29.5, 21, 3.6, 3.4) & ~f.E(29.5, 21, 2.8, 2.6)) | f.C([(22, 20.6), (26, 20.6)], .4), '#c8a040')   # round spectacles
    nose(f, 1.4); f.mask(f.E(26, 25.6, .9, .9), '#6a8a4a')                                                   # wart
    mouth(f, 'smirk', 30)
    return f

def durik():
    f = bust('skin', 'red', jaw=1.2, rx=12, ry=11)
    for x in (15, 33): f.mask(f.C([(x, 36), (x, 48)], 1), '#3a2414')                                         # apron straps
    f.add(f.E(24, 11.6, 11.6, 5) & (yy < f.T(0, 13.5)[1]), 'orange')
    eyes(f, '#3a2a1a', 'stern', brow='#a04a1a')
    f.mask(f.C([(14.5, 16.4), (21, 17.6)], 1) | f.C([(33.5, 16.4), (27, 17.6)], 1), '#c8601e')               # bushy brows
    nose(f, 1.4)
    f.add(f.Pp([(12, 24), (36, 24), (34, 38), (28, 46), (20, 46), (14, 38)]), 'orange', bias=.05)             # huge beard
    for x in (21, 27): f.add(f.C([(x, 42), (x, 48)], 1.3), 'orange', bias=.1); f.px([(x, 45)], GOLD); f.px([(x, 46)], GOLDD)   # braids with rings
    f.mask(f.C([(19, 27.4), (29, 27.4)], .5), '#3a0a08')
    for p in [(17, 15), (30, 24), (19, 26), (33, 19)]: f.px([p], '#2a2020')                                   # soot
    return f

def pell():
    f = bust('pale', 'purple', jaw=.86, rx=9.6, ry=12.6)
    f.add(f.Pp([(14, 34), (20, 37), (24, 34), (28, 37), (34, 34), (32, 40), (16, 40)]), 'white', bias=.1)     # high collar
    f.add(f.Pp([(13, 11), (35, 11), (34, -2), (14, -2)]), 'black', soft=1); f.add(f.E(24, 11, 15, 2), 'black', bias=-.05)   # top hat
    f.mask(f.Pp([(13.5, 7.6), (34.5, 7.6), (34.5, 9.6), (13.5, 9.6)]), '#8a1a20')
    eyes(f, '#2a2a3a', 'sly', brow='#1a1a20')
    f.mask(f.E(29.5, 21, 3, 3) & ~f.E(29.5, 21, 2.3, 2.3), GOLD); f.mask(f.C([(32, 23), (35, 34)], .3), GOLD)   # monocle and chain
    nose(f, 1.1)
    f.mask(f.C([(19, 27.4), (23.4, 26.6)], .4) | f.C([(24.6, 26.6), (29, 27.4)], .4), '#1a1a20')               # pencil mustache
    mouth(f, 'smirk', 29.6, 2.6)
    return f

def ysolde():
    def hair_back(f):
        # long hair falling behind the head and over the shoulders
        f.add(f.Pp([(12, 12), (36, 12), (39, 30), (37, 44), (30, 40), (18, 40), (11, 44), (9, 30)]), 'red', soft=1.2, bias=-.08)
        for x in (13, 17, 31, 35): f.mask(f.C([(x, 22), (x - .5, 40)], .3), P['red'][1])
    f = bust('skinlt', 'forest', jaw=.9, rx=9.8, ry=11.6, behind=hair_back)
    f.add(f.C([(10, 37), (38, 48)], 1.2), 'leather')                                                         # map satchel strap
    f.add(f.E(24, 12.4, 10.4, 5.4) & (yy < f.T(0, 15.5)[1]), 'red', bias=.05)                                # hairline
    f.add(f.Pp([(14.5, 11), (21, 11), (18, 17.5), (15, 18.5)]), 'red', bias=.08)                              # side-swept fringe
    f.add(f.Pp([(10, 12), (38, 12), (34, 4), (14, 4)]), 'brown', soft=1); f.add(f.E(24, 12, 16, 2.2), 'brown', bias=-.05)   # wide hat
    f.mask(f.Pp([(14.4, 9.6), (33.6, 9.6), (33.6, 10.8), (14.4, 10.8)]), '#3a2414')                          # hat band
    f.add(f.C([(32, 7), (40, 0), (45, 1)], 1.6, .5), 'crimson', bias=.1)                                      # feather
    eyes(f, '#2a7a5a', 'kind', brow='#9a3a1a')
    for sx in (-1, 1): f.mask(f.C([(24 + sx * 5.5 - 2.6, 19.4), (24 + sx * 5.5 + 2.6 * sx, 18.8)], .35), '#1a0e0a')   # lashes
    nose(f, .85)
    for p in [(18, 25), (20.5, 25.5), (27.5, 25.5), (30, 25)]: f.px([p], '#d8946e')                         # freckles
    f.mask(f.C([(21.4, 29.2), (24, 30.4), (26.6, 29.2)], .55), '#b03a3a'); f.px([(24, 28.8)], '#c85a50')        # smiling lips
    f.mask(f.E(13.6, 23.4, .8, .8) | f.E(34.4, 23.4, .8, .8), GOLD)                                           # earrings
    return f

ALL = {'tobin':tobin, 'hanna':hanna, 'aldric':aldric, 'brakka':brakka, 'maren':maren, 'wenna':wenna, 'durik':durik, 'pell':pell, 'ysolde':ysolde}
if __name__ == '__main__':
    imgs = {k: fn().render().crop((6, 3, 42, 39)) for k, fn in ALL.items()}
    from PIL import Image
    S=6; sh=Image.new('RGBA',(5*(36*S+8)+8,2*(36*S+8)+8),(28,30,40,255))
    for i,im in enumerate(imgs.values()): sh.alpha_composite(im.resize((36*S,36*S),Image.NEAREST),(8+(i%5)*(36*S+8),8+(i//5)*(36*S+8)))
    sh.save('portraits.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('portraits.json', 'w'))
