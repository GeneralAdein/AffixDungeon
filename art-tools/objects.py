from hk import *

def chest():
    f = Fig()
    f.add(f.Pp([(8, 26), (40, 26), (41, 44), (7, 44)]), 'wood', soft=.8)
    f.add(f.Pp([(8, 26), (40, 26), (38, 16), (10, 16)]) | f.E(24, 18, 15, 5) & (yy < f.T(0, 20)[1]), 'wood', bias=.1)
    for x in (13, 33): f.add(f.Pp([(x, 14), (x + 3, 14), (x + 3, 44), (x, 44)]), 'gold', bias=.05)
    f.add(f.Pp([(7, 25), (41, 25), (41, 28), (7, 28)]), 'gold', bias=-.05)
    f.add(f.Pp([(21, 27), (27, 27), (27, 34), (21, 34)]), 'gold', bias=.1); f.mask(f.E(24, 30, 1, 1.4), INK)
    f.px([(10, 18), (11, 17), (37, 18)], '#fff0b0')
    return f

def stairs():
    f = Fig()
    f.add(f.Pp([(6, 30), (42, 30), (46, 46), (2, 46)]), 'gray', soft=.6, bias=-.1)
    f.add(f.Pp([(10, 32), (38, 32), (41, 44), (7, 44)]), ['#020203', '#060608', '#0c0c10'], flat=0, ao=False)
    for i, y in enumerate((34, 37, 40)):
        f.add(f.Pp([(12 + i * 2, y), (36 - i * 2, y), (36 - i * 2, y + 1.6), (12 + i * 2, y + 1.6)]), 'gray', flat=3 - i)
    for x in (9, 39): f.add(f.C([(x, 31), (x, 18)], .7), 'wood'); f.flame((x, 17), big=.55)
    return f

def shrine():
    f = Fig()
    f.add(f.Pp([(12, 38), (36, 38), (38, 46), (10, 46)]), 'gray', soft=.8)
    f.add(f.Pp([(16, 16), (32, 16), (31, 38), (17, 38)]), 'gray', soft=1)
    f.mask(f.C([(24, 20), (24, 33)], .7) | f.C([(20, 24), (28, 24)], .7), '#7fe0ff')
    f.add(f.E(24, 11, 5, 5), ['#0a3a5a', '#2a7aaa', '#7fe0ff', '#e0f8ff'], soft=1)
    f.px([(22, 9)], '#ffffff')
    for p in [(16, 6), (32, 5), (24, 2), (13, 12), (35, 13), (19, 3), (29, 2)]: f.px([p], '#a0f0ff', 200)
    return f

def campfire():
    f = Fig()
    f.add(f.C([(12, 44), (36, 40)], 1.8) | f.C([(12, 40), (36, 44)], 1.8), 'wood', bias=.1)
    for x in (10, 15, 20, 28, 33, 38): f.add(f.E(x, 44.5, 2.2, 1.6), 'gray', bias=.1)
    f.flame((24, 40), ('#ff5020', '#ffa030', '#fff0a0'), big=2.3)
    for p in [(18, 18), (30, 15), (24, 12), (21, 8), (28, 6)]: f.px([p], '#ffb040', 170)
    return f

def merchant():
    f = Fig()
    f.add(f.Pp([(28, 15), (39, 13), (41, 34), (30, 36)]), 'leather', soft=1)               # huge backpack
    for y in (18, 25, 31): f.mask(f.C([(29, y), (40, y - 1)], .35), P['leather'][1])
    f.add(f.C([(36, 13), (38, 6)], .6), 'wood'); f.add(f.E(38, 5, 2, 2.2), 'dsteel'); f.mask(f.E(38, 5.6, 1, 1.2), '#ffd060')
    f.robe('brown', wb=9.5)
    f.add(f.C([(18, 29.5), (30, 29.5)], .9), 'leather', flat=2)
    for x, c in ((20, '#e8c040'), (22, '#c83a2a'), (26, '#3a7ac8')): f.mask(f.E(x, 32, 1, 1.2), c)
    f.arm((17, 19.5), (12, 24), (14, 27), 'brown', 'skin')
    f.add(f.E(14, 29, 2.4, 2.6), 'leather', bias=.05); f.px([(14, 27)], GOLD)
    f.arm((31, 19.5), (35, 23), (33, 26), 'brown', 'skin')
    f.head('skin'); f.hood('brown')
    f.face(mood='sly', eye='#2a1a0a')
    f.beard('gray', length=7)
    return f

OBJ = {'chest': chest, 'stairs': stairs, 'shrine': shrine, 'campfire': campfire, 'merchant': merchant}
if __name__ == '__main__':
    import base64, io, json
    imgs = {k: fn().render() for k, fn in OBJ.items()}
    sheet(list(imgs.values()), scale=5, cols=5).save('objects.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('objects.json', 'w'))
