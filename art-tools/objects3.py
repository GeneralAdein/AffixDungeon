from hk import *
import base64, io, json
def vault():
    f = Fig()
    f.add(f.Pp([(6, 46), (42, 46), (42, 12), (34, 4), (14, 4), (6, 12)]), 'gray', soft=1)
    f.add(f.Pp([(11, 46), (37, 46), (37, 15), (31, 9), (17, 9), (11, 15)]), 'dsteel', soft=1, bias=.05)
    for x in (16, 24, 32): f.mask(f.C([(x, 11), (x, 45)], .5), P['dsteel'][1])
    for y in (18, 30, 41): f.mask(f.C([(11.5, y), (36.5, y)], .7), P['dsteel'][4])
    for (x, y) in ((14, 18), (34, 18), (14, 41), (34, 41)): f.px([(x, y)], '#c8d0dc')
    f.add(f.E(24, 29, 5, 5), 'gold', bias=.1); f.mask(f.E(24, 28, 1.4, 1.4) | f.Pp([(23.2, 28), (24.8, 28), (25.4, 32), (22.6, 32)]), '#1a1206')
    return f
def idol():
    f = Fig()
    G = ['#0e1a10', '#1e3220', '#2e4a30', '#426440', '#587e52']
    f.add(f.Pp([(12, 46), (36, 46), (34, 40), (14, 40)]), 'gray', bias=.05)
    f.add(f.Pp([(17, 40), (31, 40), (30, 22), (18, 22)]), G, soft=1)
    f.add(f.E(24, 16, 7, 7.5), G, soft=1.2)
    for s in (-1, 1): f.add(f.C([(24 + s * 6, 12), (24 + s * 10, 5), (24 + s * 9, 2)], 1.2, .4), 'bone', bias=.1)
    f.mask(f.E(21, 16, 1.4, 1.2) | f.E(27, 16, 1.4, 1.2), '#ff3020'); f.px([(21, 16), (27, 16)], '#ffd0a0')
    f.mask(f.C([(21, 20), (24, 21.4), (27, 20)], .5), '#0a140a')
    for (x, y) in ((19, 30), (29, 33), (24, 36)): f.mask(f.E(x, y, 1.6, 1.2), '#7a2aff')
    for p in [(10, 30), (38, 26), (8, 18), (40, 12)]: f.px([p], '#b070ff', 200)
    return f
def armory():
    f = Fig()
    f.add(f.Pp([(6, 46), (42, 46), (42, 43), (6, 43)]), 'wood', bias=.05)
    for x in (8, 40): f.add(f.C([(x, 44), (x, 14)], 1.3), 'wood')
    f.add(f.C([(7, 18), (41, 18)], 1.1), 'wood'); f.add(f.C([(7, 36), (41, 36)], 1.1), 'wood')
    f.sword((15, 40), (15, 10), w=1.2, gleam=False)
    f.haft((24, 42), (24, 12)); f.add(f.Pp([(20, 11), (24, 6), (28, 11), (24, 15)]), 'steel', bias=.15)
    f.haft((33, 42), (33, 16)); f.add(f.Pp([(33, 15), (38, 13), (38, 22), (33, 20)]), 'steel', bias=.1)
    return f
def harvest():
    f = Fig()
    f.add(f.E(24, 40, 15, 6), ['#1a120a', '#3a2a14', '#5a4020', '#7a5a2c'], soft=1, dither=True)
    for (x, y, c) in ((16, 34, '#d8d0b8'), (24, 31, '#c8c0a8'), (31, 35, '#e8e0c8')):
        f.add(f.E(x, y, 4.4, 3.6), [c, c, c], flat=1); f.mask(f.C([(x - 3, y), (x + 3, y - 1)], .3), '#8a8270')
    for (x, y) in ((12, 24), (20, 18), (30, 21), (36, 27)):
        f.add(f.C([(x, y + 8), (x, y + 2)], .7), ['#c8c0b0', '#e8e0d0']); f.add(f.E(x, y, 3.4, 2.2) & (yy < f.T(0, y + .6)[1]), 'red', bias=.1)
        f.px([(x - 1, y - 1), (x + 1, y - .4)], '#f0e8d8')
    for p in [(8, 14), (26, 10), (40, 16), (18, 8)]: f.px([p], '#a0ffb0', 200)
    return f
ALL = {'vault': vault, 'idol': idol, 'armory': armory, 'harvest': harvest}
if __name__ == '__main__':
    imgs = {k: fn().render() for k, fn in ALL.items()}
    sheet(list(imgs.values()), scale=5, cols=4).save('objects3.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('objects3.json', 'w'))
