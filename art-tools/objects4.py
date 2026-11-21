from hk import *
import base64, io, json
def hoard():
    f = Fig()
    f.add(f.E(24, 38, 18, 8), 'gold', soft=1.4, dither=True, noise=.4)
    f.add(f.E(24, 32, 12, 7), 'gold', soft=1.2, bias=.1)
    f.add(f.E(24, 27, 6, 4), 'gold', bias=.15)
    for (x, y) in ((14, 36), (20, 30), (28, 33), (33, 38), (24, 24), (17, 41), (31, 28)):
        f.mask(f.E(x, y, 1.6, 1), '#fff0a0'); f.px([(x - 1, y)], '#9c6c10')
    f.add(f.Pp([(34, 30), (40, 28), (41, 34), (35, 36)]), 'crimson', bias=.1); f.mask(f.E(37.5, 32, 1.2, 1.2), '#ffd0d0')   # a red gem
    for p in [(10, 20), (38, 16), (24, 12), (16, 14)]: f.px([p], '#fff6c0', 210)
    return f
def library():
    f = Fig()
    f.add(f.Pp([(8, 46), (40, 46), (40, 6), (8, 6)]), 'wood', bias=.05)
    for y in (16, 26, 36): f.add(f.Pp([(9, y), (39, y), (39, y + 1.6), (9, y + 1.6)]), 'wood', bias=.2)
    cols = ['crimson', 'royal', 'forest', 'purple', 'bronze', 'crimson', 'royal']
    for row, y0 in enumerate((7, 17, 27)):
        x = 10
        for i in range(7):
            w = 2.6 + (i * 7 + row) % 3 * .6; hgt = 8.4 - (i + row) % 3
            if x + w > 38.5: break
            f.add(f.Pp([(x, y0 + 9 - hgt), (x + w, y0 + 9 - hgt), (x + w, y0 + 9), (x, y0 + 9)]), cols[(i + row) % len(cols)], flat=2)
            f.mask(f.C([(x + .5, y0 + 9 - hgt + 1.5), (x + w - .5, y0 + 9 - hgt + 1.5)], .25), GOLD)
            x += w + .4
    f.add(f.Pp([(14, 37), (34, 37), (34, 45), (14, 45)]), ['#5a4a30', '#a08a60', '#e0d0a8'], flat=2)   # an open tome glowing
    f.mask(f.C([(24, 37), (24, 45)], .4), '#5a4a30'); f.mask(f.E(24, 41, 7, 3), '#b0f0ff', 120)
    for p in [(20, 33), (28, 32), (24, 30)]: f.px([p], '#c0f8ff', 220)
    return f
def portal():
    f = Fig()
    f.add(f.E(24, 38, 18, 7), 'gray', soft=1, bias=-.05)
    f.add(f.E(24, 38, 14, 5.2), ['#1a0a3a', '#3a1a7a', '#6a3ac0', '#a070ff', '#e0c8ff'], soft=2.2)
    f.mask(f.E(24, 38, 14, 5.2) & ~f.E(24, 38, 12.6, 4.4), '#e0c8ff')
    for a in range(8):
        import math
        t = a / 8 * 6.283; f.mask(f.E(24 + 16 * math.cos(t), 38 + 6 * math.sin(t), .9, .7), '#c8a0ff')
    for (x, y0) in ((18, 34), (24, 30), (30, 34), (21, 24), (27, 22)):
        f.mask(f.C([(x, y0), (x, y0 - 8)], .4), '#d0b8ff', 170)
    for p in [(14, 20), (34, 18), (24, 12), (19, 14), (30, 26)]: f.px([p], '#f0e0ff', 220)
    return f
ALL = {'hoard': hoard, 'library': library, 'portal': portal}
if __name__ == '__main__':
    imgs = {k: fn().render() for k, fn in ALL.items()}
    sheet(list(imgs.values()), scale=5, cols=3).save('objects4.png')
    out = {}
    for k, im in imgs.items():
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    json.dump(out, open('objects4.json', 'w'))
