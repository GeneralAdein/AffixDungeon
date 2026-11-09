from hk import *
def trap():
    f = Fig()
    f.add(f.Pp([(4, 30), (44, 30), (46, 46), (2, 46)]), 'gray', soft=.6, bias=-.1)
    f.add(f.Pp([(9, 33), (39, 33), (41, 44), (7, 44)]), ['#050506', '#0c0c10', '#16161c'], flat=0, ao=False)
    for x in range(10, 40, 4): f.add(f.Pp([(x, 44), (x + 1.6, 35), (x + 3.2, 44)]), 'steel', bias=.15)
    for x in (12, 24, 36): f.px([(x, 36), (x + 1, 35)], '#8a1a14')
    for y, s in ((14, -1), (20, 1), (26, -1)):
        f.add(f.C([(24 + s * 12, y), (24 + s * 4, y + 2)], .6), 'wood'); f.px([(24 + s * 3.4, y + 2.2)], '#d4e2f0')
    return f
def entrance():
    f = Fig()
    f.add(f.Pp([(8, 46), (8, 18), (14, 10), (24, 6), (34, 10), (40, 18), (40, 46)]), 'gray', soft=1)
    f.add(f.Pp([(14, 46), (14, 20), (18, 15), (24, 13), (30, 15), (34, 20), (34, 46)]), ['#3a2a14', '#6a4a1c', '#a87830', '#e8b850', '#ffe8a0'], soft=2, bias=.15)
    for i, y in enumerate((40, 34, 28)): f.add(f.Pp([(14 + i * 2, y), (34 - i * 2, y), (34 - i * 2, y + 1.4), (14 + i * 2, y + 1.4)]), 'gray', flat=2)
    return f
if __name__ == '__main__':
    import base64, io, json
    out = {}
    imgs = []
    for k, fn in (('trap', trap), ('entrance', entrance)):
        im = fn().render(); imgs.append(im)
        b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    sheet(imgs, scale=6, cols=2).save('objects2.png')
    json.dump(out, open('objects2.json', 'w'))
