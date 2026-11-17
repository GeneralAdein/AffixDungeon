import numpy as np, base64, io, json
from PIL import Image
rng=np.random.default_rng(11)
W,H=180,290
def hx(c): return tuple(int(c[i:i+2],16) for i in (1,3,5))
img=np.zeros((H,W,3),np.uint8)
GR=[hx(c) for c in ['#16241a','#1c2e1e','#223823','#2a4429','#335030']]
n=rng.random((H,W))
for y in range(H):
    for x in range(W):
        v=n[y,x]; l=1 if v<.35 else 2 if v<.8 else 3 if v<.96 else 4
        if (x+y)%7==0 and v>.9: l=0
        img[y,x]=GR[l]
ST=[hx(c) for c in ['#24242c','#34343e','#424250','#50505e','#5e5e6c']]
def cobble(x0,y0,x1,y1):
    for y in range(max(0,y0),min(H,y1)):
        for x in range(max(0,x0),min(W,x1)):
            bx=(x+(3 if (y//4)%2 else 0))%6; by=y%4
            if bx==5 or by==3: img[y,x]=ST[0]
            else:
                l=2 if rng.random()<.6 else 3 if rng.random()<.8 else 1
                if by==0 and bx<4: l=min(4,l+1)
                img[y,x]=ST[l]
LX,CX,RX=4,66,128; ROWS=[16,80,144,208]
# horizontal streets under each row, vertical streets in the gaps, a road out the bottom
for ry in ROWS: cobble(2,ry+48,W-2,ry+60)
cobble(53,16,65,272); cobble(115,16,127,272)
cobble(80,256,100,H)
# plaza around the fountain (center of row 3)
cy,cx=144+30,90
for y in range(144-6,144+62):
    for x in range(54,126):
        if ((x-cx)/38)**2+((y-cy)/34)**2<=1:
            bx=(x+(3 if (y//4)%2 else 0))%6; by=y%4
            img[y,x]=ST[0] if (bx==5 or by==3) else ST[3 if rng.random()<.7 else 2]
# town wall along the top, with crenellations
WALL=[hx(c) for c in ['#1a1a20','#2c2c34','#3c3c46','#4c4c58']]
for y in range(0,16):
    for x in range(W):
        if y<4 and (x//6)%2==1: img[y,x]=GR[0]; continue
        bx=(x+(4 if (y//5)%2 else 0))%8; by=y%5
        img[y,x]=WALL[0] if (bx==7 or by==4) else WALL[2 if rng.random()<.7 else 1]
# trees and bushes along the edges and in corners
def tree(cx,cy,r=7):
    for y in range(cy-r-2,cy+r+5):
        for x in range(cx-r-1,cx+r+2):
            if 0<=x<W and 0<=y<H:
                if abs(x-cx)<=1 and cy<y<=cy+r+4: img[y,x]=hx('#3a2614')
                d=((x-cx)/r)**2+((y-cy)/(r*.9))**2
                if d<=1:
                    shade=0 if d>.75 else 1 if (x-cx)+(y-cy)>2 else 2
                    if rng.random()<.12: shade=max(0,shade-1)
                    img[y,x]=[hx('#0e2414'),hx('#163a1e'),hx('#22522a')][shade]
for (x,y,r) in [(2,72,5),(178,74,5),(2,138,5),(178,136,5),(2,202,5),(178,204,5),(14,282,8),(166,282,8),(40,284,6),(140,284,6)]: tree(x,y,r)
# a small garden fills the empty middle lot
for y in range(84,126):
    for x in range(70,110):
        if (x-90)**2/400+(y-105)**2/400<=1 and rng.random()<.5: img[y,x]=hx(rng.choice(['#2a5a2a','#3a6a30','#d84a5a','#e8c040','#c070ff','#f0f0e0']))
for (x,y,r) in [(76,92,7),(104,92,7),(90,112,8)]: tree(x,y,r)
# flowers
for _ in range(120):
    x,y=rng.integers(0,W),rng.integers(16,H)
    if tuple(img[y,x]) in GR: img[y,x]=hx(rng.choice(['#d84a5a','#e8c040','#c070ff','#7ab8ff','#f0f0e0']))
# lamp posts at street corners
LAMPS=[]
for ry in ROWS:
    for lx in (59,121):
        y0=ry+46
        for y in range(y0-8,y0): img[y,lx]=hx('#14141a')
        img[y0-9,lx-1:lx+2]=hx('#14141a'); img[y0-10,lx]=hx('#ffd060'); img[y0-9,lx]=hx('#ffe9a0')
        LAMPS.append((lx,y0-10))
# soft vignette
yy,xx=np.mgrid[0:H,0:W]
v=np.clip(((xx-W/2)/(W*.62))**2+((yy-H/2)/(H*.62))**2,0,1)
img=(img*(1-.45*v[...,None])).astype(np.uint8)
im=Image.fromarray(img)
im.resize((W*3,H*3),Image.NEAREST).save('townbg_big.png')
b=io.BytesIO(); im.save(b,'PNG',optimize=True)
json.dump({'bg':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode(),'lamps':LAMPS},open('townbg.json','w'))
print(len(b.getvalue()))
