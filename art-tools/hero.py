from hk import *
def hero():
    f = Fig()
    f.cape(['#2a0e04','#5a2008','#8a3a10','#b85a1c','#e0743a','#f09a5a'], side='left')
    f.legs('stand', pants='pants', boots='leather', cuff=GOLD)
    f.torso('leather', wt=6.6)
    f.add(f.C([(30, 18), (19, 29)], 1), 'dleather'); f.belt(29.5, 'dleather')
    f.arm((31, 19.5), (34, 24), (33, 28), 'leather', 'skin')
    f.arm((17, 19.5), (14, 24), (14, 28), 'leather', 'skin')
    f.sword((14, 28), (12, 38), w=1.2, gleam=False)
    f.head('skin'); f.hair('brown', 'swept', hi='#c08a50'); f.face(mood='calm', eye='#2a4a6a')
    return f
if __name__=='__main__':
    import base64, io, json
    im = hero().render(); sheet([im],scale=6,cols=1).save('hero.png')
    b = io.BytesIO(); im.save(b,'PNG',optimize=True); json.dump({'hero':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()},open('hero.json','w'))
