from iso import *
import base64, io, json, math

def lot(I, half=24):
    I.ground(-half, -half, half, half, cobble(4))

def solid(rp, lv):
    return lambda *a: (rp, lv)

def tri(I, pts, rp, lv):
    m = I._mask([I.P(*p) for p in pts]); ys, xs = np.nonzero(m)
    for py, px in zip(ys, xs): I.rgb[py, px] = R[rp][lv + (int(py) % 3 == 0)]; I.a[py, px] = True

def smithy(I):
    I.box(-14, -13, 0, 6, 6, 36, right=stonewall(bw=4), left=stonewall(bw=4))
    I.gable_y(-16, -14, 14, 10, 18, 14,
              timber(30, 18, openings=[(4, 2.2, 17, 13, 'open'), (20, 2.2, 26, 12, 'door'), (10, 20, 14, 25, 'window')]),
              timber(24, 18, openings=[(9, 7, 14, 12, 'window')]), tiles('rooftile'))
    I.box(-14, -13, 30, 6, 6, 9, top=solid('stone', 1), right=stonewall(bw=4), left=stonewall(bw=4))
    fx, fy = I.P(-7, 10, 4); I.flame(fx, fy, 1.5); I.ellipse(fx, fy + 1, 4, 1.4, 'fire', 2, False)
    for d in ((-3, -9), (2, -11), (-1, -13), (4, -7)): I.put(fx + d[0], fy + d[1], R['fire'][4])
    I.box(-2, 13, 0, 2.4, 2.4, 3.4, left=solid('iron', 2), right=solid('iron', 1), top=solid('iron', 3))
    I.box(-4.5, 12.5, 3.4, 7, 3.4, 1.8, left=solid('iron', 3), right=solid('iron', 2), top=solid('iron', 4))
    ax, ay = I.P(-1, 14, 5.3); I.rect(ax - 2, ay - 1, ax + 3, ay, R['fire'][3]); I.put(ax + 3, ay - 1, R['fire'][5])
    I.barrel(17, 14); I.barrel(19, 9, s=.9)
    wx, wy = I.P(19, 9, 5.4); I.ellipse(wx, wy, 2.2, .9, 'water', 3, False)
    I.crate(-21, 6); I.crate(-20, 10.5, 3)
    sx, sy = I.P(14, 12, 12); I.rect(sx - 1, sy - 2, sx + 7, sy + 4, R['wood'][3]); I.rect(sx + 1, sy, sx + 5, sy + 2, R['iron'][4]); I.line((sx + 3, sy + 2), (sx + 3, sy + 3), R['wood'][1])
    return I

def shop(I):
    I.gable_x(-16, -14, 14, 10, 20, 13,
              timber(30, 20, openings=[(3, 2.2, 14, 8.5, 'window'), (17, 2.2, 23, 11, 'door'), (5, 12, 10, 17, 'window'), (20, 12, 25, 17, 'window')]),
              timber(24, 20, openings=[(9, 11, 15, 16, 'window')]), tiles('rooftile'))
    for i in range(12):
        c = R['cloth_red'][4] if i % 2 == 0 else R['white'][4]
        for t in range(5):
            px, py = I.P(-13 + i, 10 + t * .8, 10.2 - t * .7); I.put(px, py, c); I.put(px, py + 1, c)
    for (x, c) in ((-11, 'cloth_red'), (-8.5, 'cloth_blue'), (-6, 'gold'), (-3.5, 'leaf')):
        px, py = I.P(x, 10, 4.8); I.ellipse(px, py, 1.1, 1.4, c, 4, False)
    I.crate(-21, 11); I.crate(-20, 14.5, 3); I.barrel(17, 14)
    sx, sy = I.P(14, 11, 14); I.line((sx - 2, sy - 1), (sx + 3, sy - 1), R['iron'][2]); I.rect(sx, sy, sx + 6, sy + 5, R['wood'][3]); I.ellipse(sx + 3, sy + 2.5, 1.6, 1.4, 'gold', 4, False)
    I.lamp(1, 10.5, 13)
    return I

def tavern(I):
    I.box(4, -12, 0, 5, 5, 38, right=stonewall(bw=4), left=stonewall(bw=4))
    up_l = timber(32, 17, openings=[(3, 9.5, 8, 14, 'window'), (12, 9.5, 18, 14, 'window'), (24, 9.5, 29, 14, 'window'), (13, 18, 19, 23, 'window')])
    lo_l = stonewall(bw=5, openings=[(3, 2.2, 8, 6.5, 'window'), (13, 0, 20, 8.5, 'door'), (24, 2.2, 29, 6.5, 'window')])
    up_r = timber(26, 17, openings=[(5, 9.5, 10, 14, 'window'), (16, 9.5, 21, 14, 'window')])
    lo_r = stonewall(bw=5, openings=[(10, 2.2, 15, 6.5, 'window')])
    I.gable_y(-17, -15, 15, 11, 20, 15,
              lambda x, y, z, u, v: up_l(x, y, z, u, v) if v > 8 else lo_l(x, y, z, u, v),
              lambda x, y, z, u, v: up_r(x, y, z, u, v) if v > 8 else lo_r(x, y, z, u, v), thatch())
    I.box(4, -12, 32, 5, 5, 8, top=solid('stone', 1), right=stonewall(bw=4), left=stonewall(bw=4))
    for x in (-5, 5): I.lamp(x, 11.5, 9)
    sx, sy = I.P(-1, 12, 15); I.line((sx - 3, sy - 1), (sx + 3, sy - 1), R['iron'][2]); I.rect(sx - 2, sy, sx + 4, sy + 5, R['wood'][3])
    I.rect(sx - 1, sy + 1, sx + 2, sy + 4, R['gold'][4]); I.put(sx + 2, sy + 2, R['gold'][3]); I.put(sx, sy + 1, R['white'][5])
    I.barrel(-20, 12); I.barrel(-16.5, 15); I.barrel(-19, 15.5, s=.9)
    I.box(8, 13, 0, 7, 2, 2, left=solid('wood', 3), right=solid('wood', 2), top=solid('wood', 4))
    return I

def guild(I):
    st = stonewall(bw=5, bh=3, openings=[(11, 0, 19, 13, 'door'), (12, 17, 18, 24, 'window')])
    I.box(-15, -15, 0, 30, 28, 28, left=st, right=stonewall(bw=5, openings=[(10, 16, 16, 23, 'window')]))
    I.box(-15, -15, 28, 30, 28, .1, top=lambda x, y, z, u, v: ('roofslate', 1 if (x % 4 < .6 or (y + (2 if int(x // 4) % 2 else 0)) % 4 < .6) else 3))
    for i in range(0, 30, 4):
        I.box(-15 + i, 11, 28, 2.4, 2, 3, left=stonewall(bw=3), right=stonewall(bw=3), top=solid('stone', 3))
    for i in range(0, 26, 4):
        I.box(13, -15 + i, 28, 2, 2.4, 3, left=stonewall(bw=3), right=stonewall(bw=3), top=solid('stone', 3))
    for x0 in (-12, 6):
        for t in range(18):
            for w in range(5):
                if t > 15 and abs(w - 2) > 2 - (t - 15): continue
                px, py = I.P(x0 + w, 13.2, 25 - t); I.put(px, py, R['cloth_blue'][3 + (w == 0) - (w == 4)])
        bx, by = I.P(x0 + 2.5, 13.2, 19); I.ellipse(bx, by, 1.6, 1.6, 'gold', 4, False)
    for x in (-5, 5): fx, fy = I.P(x, 13.4, 12); I.flame(fx, fy, .8)
    px, py = I.P(13, 11, 31)
    for t in range(12): I.put(px, py - t, R['wood'][3])
    for t in range(5):
        for w in range(7 - t): I.put(px + 1 + w, py - 11 + t, R['cloth_blue'][4])
    return I

def yard(I):
    I.ground(-22, -22, 22, 22, lambda x, y, z, u, v: ('dirt', 3 + (hsh(int(x), int(y)) > .7) - (hsh(int(x), int(y), 4) > .9)))
    I.gable_x(-20, -20, -4, -10, 12, 6, logs(), logs(), tiles('roofslate'))
    for i, x in enumerate(range(-19, -6, 2)):
        px, py = I.P(x, -9.5, 3)
        for t in range(8): I.put(px, py - t, R['iron'][4] if i % 2 else R['wood'][4])
    for (dx, dy) in ((-6, 6), (6, -4)):
        cx, cy = I.P(dx, dy, 0)
        for t in range(14): I.put(cx, cy - t, R['wood'][3])
        I.ellipse(cx, cy - 9, 3.4, 4.2, 'thatch', 3); I.ellipse(cx, cy - 15, 2.4, 2.4, 'thatch', 4)
        I.line((cx - 6, cy - 11), (cx + 6, cy - 11), R['wood'][3])
        I.ellipse(cx, cy - 9, 1.2, 1.2, 'cloth_red', 4, False)
    tx, ty = I.P(14, 8, 0)
    for t in range(6): I.put(tx, ty - t, R['wood'][3])
    I.ellipse(tx, ty - 11, 5, 5.4, 'white', 4, False); I.ellipse(tx, ty - 11, 3.6, 3.8, 'cloth_red', 4, False); I.ellipse(tx, ty - 11, 2.2, 2.4, 'white', 5, False); I.ellipse(tx, ty - 11, 1, 1, 'cloth_red', 4, False)
    for d in ((-1, -1), (2, 1)): I.line((tx + d[0], ty - 11 + d[1]), (tx + d[0] + 3, ty - 13 + d[1]), R['wood'][2])
    for i in range(-22, 23, 4):
        for (x, y) in ((i, 22), (22, i)):
            px, py = I.P(x, y, 0)
            for t in range(5): I.put(px, py - t, R['wood'][3 + (t == 4)])
    for e in range(-22, 23):
        for (x, y) in ((e, 22), (22, e)):
            px, py = I.P(x, y, 3); I.put(px, py, R['wood'][2])
    return I

def temple(I):
    I.gable_x(-16, -12, 12, 10, 19, 10,
              stonewall('marble', bw=6, openings=[(3, 5, 6, 13, 'window'), (22, 5, 25, 13, 'window'), (11, 0, 17, 11, 'door')]),
              stonewall('marble', bw=6, openings=[(9.5, 5, 12.5, 12, 'window')]), tiles('roofblue'))
    I.box(4, -16, 0, 9, 9, 34, left=stonewall('marble', bw=4, openings=[(2.5, 24, 6.5, 30, 'dark')]), right=stonewall('marble', bw=4, openings=[(2.5, 24, 6.5, 30, 'dark')]))
    sp = (8.5, -11.5, 50)
    tri(I, [(4, -7, 34), (13, -7, 34), sp], 'roofblue', 3)
    tri(I, [(13, -7, 34), (13, -16, 34), sp], 'roofblue', 2)
    cx, cy = I.P(*sp)
    for t in range(5): I.put(cx, cy - t, R['gold'][4])
    I.line((cx - 2, cy - 3), (cx + 2, cy - 3), R['gold'][4])
    bx, by = I.P(13, -11.5, 27); I.ellipse(bx, by, 1.6, 1.8, 'gold', 4, False)
    rx, ry = I.P(12, -1, 20)
    I.ellipse(rx, ry, 3.6, 3.8, 'dark', 3, False)
    for i, c in enumerate(['cloth_red', 'cloth_blue', 'gold', 'leaf', 'roofpurple', 'cloth_red', 'cloth_blue', 'gold']):
        a = i / 8 * 6.283; I.put(rx + 2.4 * math.cos(a), ry + 2.4 * math.sin(a), R[c][4])
    I.put(rx, ry, R['glow'][5])
    for x in (-6, 6): fx, fy = I.P(x, 13, 0); I.rect(fx, fy - 4, fx + 1, fy, R['white'][5]); I.flame(fx, fy - 4, .5)
    return I

def apothecary(I):
    def moss(base):
        return lambda x, y, z, u, v: ('moss', 3 + (hsh(int(u), int(v)) > .7)) if (v < 4 and hsh(int(u), int(v), 2) > .6) else base(x, y, z, u, v)
    I.box(-12, -10, 0, 4, 4, 36, right=stonewall(bw=3), left=stonewall(bw=3))
    I.gable_y(-15, -12, 11, 9, 17, 16,
              moss(timber(26, 15, base='moss', openings=[(3, 5, 8, 10, 'window'), (17, 5, 22, 10, 'window'), (10, 2.2, 15, 11, 'door'), (11, 17, 15, 21, 'window')])),
              moss(timber(21, 15, base='moss', openings=[(8, 6, 13, 11, 'window')])), tiles('roofpurple'))
    I.box(-12, -10, 30, 4, 4, 6, top=solid('stone', 1), right=stonewall(bw=3), left=stonewall(bw=3))
    cx, cy = I.P(-12, -8, 38)
    for d in ((0, -1), (1, -3), (-1, -5)): I.put(cx + d[0], cy + d[1], R['leaf'][5])
    kx, ky = I.P(-8, 15, 0)
    I.ellipse(kx, ky - 3, 4.2, 3.2, 'iron', 2); I.ellipse(kx, ky - 5, 3.4, 1.2, 'leaf', 5, False)
    for d in ((-1, -8), (1, -10), (0, -12)): I.put(kx + d[0], ky + d[1], R['leaf'][5])
    for i in range(3): px, py = I.P(-11 + i * 3, 15.5, 0); I.put(px, py, R['fire'][3 + i % 2])
    for (x, y, c) in ((15, 6, 'cloth_red'), (15, 10, 'roofpurple'), (13.5, 13, 'cloth_red')):
        px, py = I.P(x, y, 0); I.rect(px - 2, py - 3, px + 2, py, R[c][3]); I.ellipse(px, py - 4, 2.4, 1.8, 'leaf', 4)
    for (x, c) in ((-11, 'leaf'), (-9, 'roofpurple'), (5, 'cloth_red'), (7, 'leaf')):
        px, py = I.P(x, 9, 7); I.ellipse(px, py, .8, 1.1, c, 5, False)
    return I

def bank(I):
    I.gable_x(-16, -12, 14, 10, 20, 7,
              stonewall('marble', bw=7, bh=4, openings=[(11, 0, 19, 13, 'door')]),
              stonewall('marble', bw=7, bh=4), tiles('marble', trim='gold'))
    for x in (-13, -8, 6, 11):
        for z in range(0, 18):
            for w in range(3):
                px, py = I.P(x + w * .7, 12, z); I.put(px, py, R['marble'][4 + (w == 0) - (w == 2) - (z % 5 == 0)])
    for x10 in range(-160, 141):
        px, py = I.P(x10 / 10, 12, 18); I.put(px, py, R['gold'][4])
    gx, gy = I.P(14, -1, 21); I.ellipse(gx, gy, 2.4, 2.4, 'gold', 4)
    vx, vy = I.P(0, 10, 6.5); I.ellipse(vx, vy, 3, 3, 'gold', 3, False); I.ellipse(vx, vy, 2, 2, 'iron', 3, False); I.put(vx, vy, R['gold'][5])
    for x in (-18, 18): px, py = I.P(x, 13, 0); I.rect(px - 1, py - 6, px + 2, py, R['iron'][3]); I.ellipse(px, py - 7, 1.6, 1.2, 'gold', 4, False)
    return I

def cartographer(I):
    I.box(-10, -10, 0, 18, 18, 30, left=stonewall('wood', bw=8, bh=3, openings=[(6, 0, 12, 10, 'door'), (6, 16, 12, 22, 'window')]),
          right=stonewall('wood', bw=8, bh=3, openings=[(6, 16, 12, 22, 'window')]))
    cx, cy = I.P(-1, -1, 30)
    I.ellipse(cx, cy - 2, 13, 9, 'roofpurple', 3)
    for py in range(int(cy - 11), int(cy - 1)): I.put(cx, py, R['roofpurple'][1])
    I.line((cx + 2, cy - 7), (cx + 12, cy - 14), R['gold'][3]); I.line((cx + 2, cy - 6), (cx + 12, cy - 13), R['gold'][2]); I.put(cx + 12, cy - 14, R['water'][5])
    for d in ((-14, -14), (-6, -18), (14, -4), (-16, -6)): I.put(cx + d[0], cy + d[1], R['glow'][5])
    rx, ry = I.P(8, -1, 16); I.ellipse(rx, ry, 3.4, 3.6, 'thatch', 4, False); I.line((rx, ry - 3), (rx, ry + 3), R['beam'][1]); I.line((rx - 3, ry), (rx + 3, ry), R['beam'][1]); I.put(rx, ry - 3, R['cloth_red'][4])
    I.box(10, 2, 0, 4, 9, 10, left=solid('wood', 3), right=lambda x, y, z, u, v: ('thatch', 4) if (int(u) % 3 == 1 and int(v) % 3 == 1) else ('wood', 2), top=solid('wood', 4))
    ex, ey = I.P(-14, 13, 0); I.line((ex, ey), (ex + 2, ey - 9), R['wood'][3]); I.line((ex + 5, ey), (ex + 3, ey - 9), R['wood'][3])
    I.rect(ex - 1, ey - 11, ex + 7, ey - 5, R['thatch'][4]); I.line((ex, ey - 7), (ex + 3, ey - 9), R['cloth_red'][4]); I.line((ex + 3, ey - 9), (ex + 6, ey - 8), R['cloth_red'][4])
    return I

def square(I):
    cx, cy = I.P(0, 0, 0)
    I.ellipse(cx, cy, 22, 11, 'stone', 3); I.ellipse(cx, cy - 1, 18, 9, 'water', 3, False); I.ellipse(cx - 4, cy - 3, 6, 2, 'water', 5, False)
    I.rect(cx - 2, cy - 14, cx + 3, cy - 1, R['stone'][3]); I.rect(cx - 2, cy - 14, cx, cy - 1, R['stone'][4])
    I.ellipse(cx, cy - 14, 5, 2, 'stone', 4)
    I.ellipse(cx, cy - 20, 2, 2.2, 'gold', 3); I.rect(cx - 2, cy - 18, cx + 3, cy - 14, R['gold'][3])
    I.line((cx + 2, cy - 19), (cx + 5, cy - 25), R['gold'][3]); I.ellipse(cx + 5, cy - 26, 1.3, 1.3, 'glow', 5, False)
    for s in (-1, 1):
        for t in range(14):
            a = t / 13; px = cx + s * (2 + a * 12); py = cy - 13 + (a * 2.4 - 1) ** 2 * 6 - 5
            I.put(px, py, R['water'][5])
    for d in ((-8, 2), (6, 3), (-2, 4), (10, 0)): I.put(cx + d[0], cy + d[1], R['gold'][5])
    for (x, y) in ((-18, 12), (18, -12)): I.bush(x, y, 3.4)
    return I

def garden(I):
    I.ground(-20, -20, 20, 20, grass())
    for (x, y, h, r) in ((-10, -8, 12, 7), (8, -12, 11, 6), (10, 8, 13, 7)): I.tree(x, y, h, r)
    for i in range(70):
        x, y = -18 + hsh(i, 1) * 36, -18 + hsh(i, 2) * 36
        px, py = I.P(x, y, 0); I.put(px, py, R[['cloth_red', 'gold', 'roofpurple', 'white', 'cloth_blue'][i % 5]][4])
    for (x, y) in ((-14, 12), (2, 14), (16, -2)): I.bush(x, y, 3)
    return I

def gate(I):
    I.ground(-22, -22, 22, 22, lambda x, y, z, u, v: ('dirt', 2 + (hsh(int(x), int(y)) > .6) - (hsh(int(x), int(y), 3) > .9)))
    I.face([(-12, -10, 0), (10, -10, 0), (10, 10, 0), (-12, 10, 0)], ('p', 0, 0, 0), lambda x, y, z, u, v: ('dark', 0 if y < 2 else 1))
    for i in range(4):
        y0 = 9 - i * 2.4
        I.face([(-10, y0 - 2.4, 0), (8, y0 - 2.4, 0), (8, y0, 0), (-10, y0, 0)], ('p', 0, 0, 0), lambda x, y, z, u, v, i=i: ('stone', 3 - i) if i < 3 else ('dark', 2))
    for (x, y) in ((-3, 0), (2, 1)): px, py = I.P(x, y, 0); I.put(px, py, R['fire'][4]); I.put(px + 1, py, R['fire'][4])
    # a full stone archway over the steps, with a skull keystone
    for x in (-14, 9):
        I.box(x, 10, 0, 4, 4, 16, left=stonewall(bw=3, bh=2), right=stonewall(bw=3, bh=2), top=solid('stone', 3))
    for t in range(25):
        a = t / 24 * math.pi
        x = -1.5 - 10.5 * math.cos(a); z = 16 + 9 * math.sin(a)
        I.box(x - 1.6, 10, z - 1.6, 3.2, 4, 3.2, left=solid('stone', 3 if t % 4 else 2), right=solid('stone', 2), top=solid('stone', 4))
    sx, sy = I.P(-1.5, 14, 25.5); I.ellipse(sx, sy, 2.6, 2.4, 'white', 3, False); I.put(sx - 1, sy, R['fire'][4]); I.put(sx + 1, sy, R['fire'][4]); I.put(sx, sy + 2, R['dark'][0])
    for (x, z) in ((-12, 12), (10, 9)):
        px, py = I.P(x, 14, z)
        for t in range(5): I.put(px, py + t, R['iron'][3] if t % 2 else R['iron'][1])
    for x in (-18, 16):
        px, py = I.P(x, 14, 0)
        for t in range(7): I.put(px, py - t, R['iron'][2])
        I.rect(px - 2, py - 9, px + 3, py - 7, R['iron'][3]); I.flame(px, py - 9, .9)
    for (x, y) in ((-20, -18), (19, -14), (-17, 4)): px, py = I.P(x, y, 0); I.put(px, py, R['cloth_red'][2])
    return I

PIECES = {'smithy': smithy, 'shop': shop, 'tavern': tavern, 'guild': guild, 'yard': yard, 'temple': temple,
          'apothecary': apothecary, 'bank': bank, 'cartographer': cartographer, 'square': square, 'garden': garden, 'gate': gate}

def build(k, preview=False):
    I = Iso(96, 96, 48, 70)
    if preview and k not in ('yard', 'garden', 'gate'): lot(I)
    PIECES[k](I); I.outline()
    return I.image()

if __name__ == '__main__':
    import sys
    keys = sys.argv[1:] or list(PIECES)
    imgs = [build(k, True) for k in keys]
    S = 4; W = 96; cols = 4; rows = (len(imgs) + cols - 1) // cols
    sh = Image.new('RGBA', (cols * (W * S + 6) + 6, rows * (W * S + 6) + 6), (20, 22, 30, 255))
    for i, im in enumerate(imgs): sh.alpha_composite(im.resize((W * S, W * S), Image.NEAREST), (6 + (i % cols) * (W * S + 6), 6 + (i // cols) * (W * S + 6)))
    sh.save('iso_preview.png')
    if not sys.argv[1:]:
        out = {}
        for k in PIECES:
            im = build(k); b = io.BytesIO(); im.save(b, 'PNG', optimize=True); out[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
        json.dump(out, open('iso_town.json', 'w'))
