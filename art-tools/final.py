import revise, monsters
from monsters import *
from revise import ant as _a

def ant():
    s = Sprite('#0c0605')
    s.add(ellipse(24, 11, 9, 7), R['chitin_d'], dither=True)
    for y in (9, 12):
        s.maskpx(ellipse(24, y, 8, 1) & ellipse(24, 11, 8.5, 6.5), '#2c100c')
    s.add(mir(chain([(19, 21), (11, 14), (4, 20), (2, 30)], 1.2, 0.6)), R['chitin_d'])
    s.add(mir(chain([(19, 23), (10, 24), (6, 36), (5, 45)], 1.3, 0.6)), R['chitin_d'])
    s.add(ellipse(24, 20, 5.5, 4.5), R['chitin'])
    s.add(mir(chain([(19, 27), (13, 33), (14, 40), (12, 46)], 1.4, 0.6)), R['chitin'])
    s.add(mir(chain([(21, 23), (17, 13), (11, 6), (7, 6)], 0.9, 0.5)), R['chitin_d'], bias=0.1)
    s.add(ellipse(24, 29, 10.5, 8) | ellipse(24, 24, 7, 5), R['chitin'], soft=1.4)
    s.add(mir(chain([(19, 34.5), (16, 38.5), (16.5, 42.5), (20.5, 44)], 2.0, 0.45)), R['chitin_d'], bias=0.15)
    s.pxm([(17, 40), (18, 43)], '#140807')
    s.add(mir(ellipse(16, 28, 3, 3.6)), ['#060303', '#100606', '#1f0b0a', '#3a1611'], lo=-0.7)
    s.pxm([(15, 26), (16, 26)], '#d89c80')
    s.pxm([(15, 27)], '#8a4a3a')
    s.pxm([(22, 24), (21, 25)], '#d4845a')
    s.px([(23, 33), (24, 33), (25, 33)], '#3d1610')
    s.px([(23, 34), (24, 34), (25, 34)], '#5a1a14')
    return s

def wolf():
    s = Sprite('#070609')
    F = R['wolf']
    MZ = ['#262326', '#423d40', '#625b5c', '#857d7a', '#a69d96']
    s.add(ellipse(24, 38, 15, 9), F, dither=True, noise=0.25)
    s.add(mir(chain([(16, 39), (15, 46)], 2.5, 2.0)), F)
    s.pxm([(13, 46), (15, 46), (17, 46)], '#cfc8b8')
    mane = poly([(24, 14), (33, 18), (38, 22), (35, 25), (40, 29), (35, 31), (37, 35), (30, 36), (24, 40), (18, 36), (11, 35), (13, 31), (8, 29), (13, 25), (10, 22), (15, 18)])
    s.add(mane, F, dither=True, noise=0.3, soft=1.6)
    s.add(mir(poly([(17, 17), (9, 7), (20, 13)])), F)
    s.maskpx(mir(poly([(16, 15), (12, 10), (18, 14)])), '#2a1f22')
    s.add(ellipse(24, 21, 8.5, 7), F, soft=1.4, dither=True)
    s.add(poly([(21, 23), (27, 23), (28.5, 33), (19.5, 33)]) | ellipse(24, 33, 4, 2.6), MZ, soft=1.2)
    s.add(ellipse(24, 34, 2.2, 1.4), ['#050405', '#141114', '#2e292c'])
    s.maskpx(mir(poly([(19.5, 29), (21.5, 30), (22, 37), (20, 33.5)])), '#2a0a10')
    s.pxm([(20, 30), (20, 31), (21, 32), (21, 33), (21, 35), (21, 36)], '#e6e0cc')
    s.maskpx(mir(chain([(17, 17.5), (21.5, 19.5)], 0.6)), '#0d0c0e')
    s.pxm([(19, 20), (20, 20)], EYE_Y)
    s.pxm([(20, 20)], '#2a1505')
    s.px([(24, 22), (24, 24)], '#141114')
    return s

monsters.ALL['ant'] = ant
monsters.ALL['wolf'] = wolf
imgs = {k: f().render() for k, f in monsters.ALL.items()}
sheet(list(imgs.values()), scale=5, cols=5).save('sheet3.png'); sheet([imgs['ant'],imgs['wolf']],scale=8,cols=2).save('zoom.png')
import base64, io, json
out = {}
for k, im in imgs.items():
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
json.dump(out, open('art.json', 'w'))
print(sum(len(v) for v in out.values()))
