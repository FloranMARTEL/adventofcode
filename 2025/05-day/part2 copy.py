#parti2

from Gif import GifMaker
from PIL import Image, ImageFont, ImageDraw

def drawinter(image,d,f,l,color):

    m = 5
    image.putpixel((d,l*m-2),color)
    image.putpixel((d,l*m-1),color)
    image.putpixel((d,l*m),color)
    image.putpixel((d,l*m+1),color)
    image.putpixel((d,l*m+2),color)

    for i in range(f-d):
        image.putpixel((d+i,l*m-1),color)
        image.putpixel((d+i,l*m),color)
        image.putpixel((d+i,l*m+1),color)
    
    image.putpixel((f,l*m-2),color)
    image.putpixel((f,l*m-1),color)
    image.putpixel((f,l*m),color)
    image.putpixel((f,l*m+1),color)
    image.putpixel((f,l*m+2),color)


    


g = GifMaker(None,None,(1501,1000))

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

[p,ids] = data.split("\n\n")


p = p.split("\n")
ids = ids.split("\n")


plage = []
mi = None
ma = None
for o in p:

    [d,f] = o.split("-")
    (d,f) = (int(d),int(f))

    if mi == None or d < mi:
        mi = d

    if ma == None or f > ma:
        ma = f

    plage.append((d,f))


coef = (1500/(ma-mi))
def conv_interval(x):

    x = int((x-mi)*coef)

    return x

g.crate_image()
for i,a in enumerate(plage):
    drawinter(g.image,conv_interval(a[0]),conv_interval(a[1]),i,(255,255,255))
g.checkImage(1000)

s = set()

pok = []
plage.sort(key=lambda x: x[1]-x[0],reverse=True)
g.crate_image()
for i,a in enumerate(plage):
    drawinter(g.image,conv_interval(a[0]),conv_interval(a[1]),i+5,(255,255,255))
g.checkImage(1000)

imcop = g.image.copy()

for ii,p in enumerate(plage):

    (pd,pf) = p

    ok = True
    for po in pok:

        if pd >= po[0] and pd <= po[1]:
            pd = po[1]+1
        
        if pf >= po[0] and pf <= po[1]:
            pf = po[0]-1
        
        if pf < pd:
            ok = False
            break


    
    if ok == True:
        drawinter(g.image,conv_interval(pd),conv_interval(pf),ii+5,(255,0,0))
        drawinter(g.image,conv_interval(pd),conv_interval(pf),198,(0,255,255))
        g.checkImage()
        pok.append((pd,pf))
g.checkImage(2000)

cpt=0
s2 = set()
for po in pok:
    
    if po[1] in s2 or po[0] in s2:
        print("errer")
    
    s2.add(po[1])
    s2.add(po[0])

    # print((po[1]-po[0])+1)
    cpt += (po[1]-po[0])+1
    
    
print(cpt)
g.creatGIF("p2")


