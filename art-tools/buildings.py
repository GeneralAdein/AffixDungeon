from hk import *

def house(roof='red', wall='brown', roof_kind='gable', w=15, door=True, sign=None, chimney=False, extra=None):
    f = Fig()
    f.add(f.Pp([(24 - w, 46), (24 + w, 46), (24 + w, 24), (24 - w, 24)]), wall, soft=.8)
    for y in (30, 36, 42): f.mask(f.C([(24 - w + .5, y), (24 + w - .5, y)], .3), P[wall][1])
    if chimney: f.add(f.Pp([(30, 10), (34, 10), (34, 20), (30, 20)]), 'gray', bias=.05); f.px([(32, 8), (31, 6), (33, 4)], '#8a8a90', 160)
    if roof_kind == 'gable': f.add(f.Pp([(24 - w - 3, 25), (24, 8), (24 + w + 3, 25)]), roof, soft=1)
    elif roof_kind == 'flat': f.add(f.Pp([(24 - w - 2, 25), (24 + w + 2, 25), (24 + w, 19), (24 - w, 19)]), roof, soft=1)
    elif roof_kind == 'dome': f.add(f.E(24, 24, w + 1, 12) & (yy < f.T(0, 25)[1]), roof, soft=1.4)
    elif roof_kind == 'spire':
        f.add(f.Pp([(24 - w - 2, 25), (24, 14), (24 + w + 2, 25)]), roof, soft=1)
        f.add(f.Pp([(20, 16), (28, 16), (24, 0)]), roof, bias=.1)
    if door:
        f.add(f.Pp([(20.5, 46), (27.5, 46), (27.5, 37), (24, 34), (20.5, 37)]), 'wood', bias=-.1)
        f.px([(26, 41)], GOLD)
    for x in (12, 33):
        if 24 - w < x < 24 + w: f.add(f.Pp([(x, 29), (x + 4, 29), (x + 4, 33), (x, 33)]), ['#3a2a10', '#a07020', '#f0c050', '#ffe8a0'], flat=2); f.mask(f.C([(x + 2, 29), (x + 2, 33)], .3), '#3a2a10')
    if sign: sign(f)
    if extra: extra(f)
    return f

def signboard(f, draw):
    f.add(f.Pp([(15, 34), (33, 34), (33, 40), (15, 40)]) if False else f.Pp([(30, 31), (40, 31), (40, 39), (30, 39)]), 'wood', bias=.05)
    f.mask(f.C([(35, 26), (35, 31)], .3), '#2a1a0c'); draw(f, 35, 35)

def shop():
    def s(f, x, y): f.mask(f.E(x, y + .5, 2.6, 2.4), GOLD); f.px([(x, y - 2), (x - 1, y - 2), (x + 1, y - 2)], GOLDD)
    return house('red', 'tan', sign=lambda f: signboard(f, s))
def tavern():
    def s(f, x, y): f.add(f.Pp([(x - 2.5, y - 2.5), (x + 1.5, y - 2.5), (x + 1.5, y + 3), (x - 2.5, y + 3)]), 'gold', flat=3); f.mask(f.C([(x + 1.5, y - 1), (x + 3, y), (x + 1.5, y + 1.5)], .5), P['gold'][3]); f.px([(x - 2, y - 3), (x - 1, y - 3.5), (x, y - 3)], '#ffffff')
    return house('green', 'brown', chimney=True, sign=lambda f: signboard(f, s))
def guild():
    def e(f):
        for x in (14, 34): f.add(f.Pp([(x - 3, 25), (x + 3, 25), (x + 3, 37), (x, 34), (x - 3, 37)]), 'royal', bias=.05); f.px([(x, 28), (x, 30)], GOLD)
        f.add(f.C([(24, 8), (24, 1)], .4), 'wood'); f.add(f.Pp([(24, 1), (31, 2.5), (24, 4.5)]), 'crimson')
    return house('royal', 'gray', roof_kind='flat', w=17, extra=e)
def yard():
    f = Fig()
    f.add(f.Pp([(2, 46), (46, 46), (46, 40), (2, 40)]), 'tan', soft=.6, bias=-.1)
    for x in range(3, 46, 6): f.add(f.C([(x, 46), (x, 33)], .8), 'wood'); f.px([(x, 32)], P['wood'][4])
    f.add(f.C([(2, 36), (46, 36)], .6), 'wood')
    f.add(f.C([(24, 44), (24, 22)], 1.2), 'wood')                      # training dummy
    f.add(f.E(24, 30, 6, 6.5), 'tan', soft=1.2); f.mask(f.C([(19, 30), (29, 30)], .5), '#5a3a1a')
    f.add(f.C([(16, 27), (32, 27)], 1.2), 'tan')
    f.add(f.E(24, 19, 3.6, 3.6), 'tan', bias=.05); f.mask(f.E(24, 19, 1.4, 1.4) & ~f.E(24, 19, .6, .6), '#b02a20')
    f.sword((9, 28), (5, 8), w=1.1, gleam=False); f.sword((39, 28), (43, 8), w=1.1, gleam=False)
    return f
def temple():
    def e(f):
        f.mask(f.C([(24, 1), (24, 7)], .5) | f.C([(21.5, 3), (26.5, 3)], .5), '#ffe08a')
        for x in (11, 37): f.add(f.Pp([(x - 2, 46), (x + 2, 46), (x + 2, 26), (x - 2, 26)]), 'white', bias=.1)
    return house('blue', 'white', roof_kind='spire', w=14, extra=e)
def apothecary():
    def s(f, x, y): f.add(f.E(x, y + 1, 2.8, 2.6), ['#3a0a10', '#8a1a20', '#d83a3a', '#ff8a7a'], flat=2); f.mask(f.C([(x, y - 3), (x, y - 1)], .7), '#c8d0dc')
    def e(f):
        for x, c in ((11, '#5ad07a'), (14, '#7aa8ff')): f.add(f.E(x, 43, 1.6, 2.4), [c, c, c], flat=1)
        f.add(f.C([(12, 22), (12, 15), (14, 11)], .8, .4), 'forest')
    return house('forest', 'tan', sign=lambda f: signboard(f, s), extra=e)
def smithy():
    def e(f):
        f.add(f.Pp([(28, 39), (42, 39), (40, 42), (37, 42), (37, 46), (33, 46), (33, 42), (30, 42)]), 'dsteel', bias=.1)   # anvil
        f.add(f.C([(31, 33), (38, 37)], .7), 'wood'); f.add(f.Pp([(29, 31), (34, 31), (34, 34), (29, 34)]), 'steel')
        f.flame((12, 40), big=1.1)
        for p in [(15, 34), (10, 32), (13, 30)]: f.px([p], '#ffb040', 200)
    return house('dsteel', 'gray', roof_kind='flat', chimney=True, door=False, extra=e)
def bank():
    def e(f):
        for x in (12, 18, 30, 36): f.add(f.Pp([(x - 1.5, 46), (x + 1.5, 46), (x + 1.5, 26), (x - 1.5, 26)]), 'white', bias=.1)
        f.add(f.Pp([(9, 26), (39, 26), (39, 23), (9, 23)]), 'white', bias=.05)
        f.mask(f.E(24, 17, 3, 3), GOLD); f.px([(24, 16), (24, 18)], GOLDD)
    return house('gold', 'white', roof_kind='gable', w=16, extra=e)
def cartographer():
    def s(f, x, y): f.add(f.Pp([(x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)]), ['#5a4a30', '#a08a60', '#e0d0a8'], flat=2); f.mask(f.C([(x - 2, y + 1), (x, y - 1), (x + 2, y + 1)], .3), '#b02a20')
    def e(f):
        f.add(f.E(24, 12, 4, 4), 'bronze', bias=.1); f.mask(f.C([(24, 9), (24, 15)], .4), '#2a1a0c'); f.mask(f.C([(21, 12), (27, 12)], .4), '#2a1a0c'); f.px([(24, 9)], '#d83a3a')
    return house('purple', 'tan', roof_kind='dome', sign=lambda f: signboard(f, s), extra=e)
def square():
    f = Fig()
    f.add(f.E(24, 40, 18, 6), 'gray', soft=1, bias=-.05)
    f.add(f.E(24, 39, 13, 4), ['#0a2a4a', '#1a5a8a', '#3a8ac0', '#7ac0e8'], soft=1)
    f.add(f.C([(24, 39), (24, 26)], 1.6), 'gray', bias=.1); f.add(f.E(24, 25, 4, 2), 'gray', bias=.1)
    for p in [(21, 22), (27, 21), (24, 19), (20, 28), (28, 29)]: f.px([p], '#a0e0ff', 210)
    return f

B = {'shop': shop, 'tavern': tavern, 'guild': guild, 'yard': yard, 'temple': temple, 'apothecary': apothecary, 'smithy': smithy, 'bank': bank, 'cartographer': cartographer, 'square': square}
if __name__ == '__main__':
    import base64, io, json
    imgs = {k: fn().render() for k, fn in B.items()}
    sheet(list(imgs.values()), scale=4, cols=5).save('buildings.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('buildings.json', 'w'))
