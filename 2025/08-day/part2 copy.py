#parti1

from Gif import *
from PIL import Image, ImageFont, ImageDraw


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()
import math

def dit(a,b):
    p = a[0]-b[0]
    o = a[1]-b[1]
    i = a[2]-b[2]

    di = math.sqrt(p*p+o*o+i*i)
    # di = abs(p)+abs(o)+abs(i)
    return di

datalist = data.split("\n")

size = (2000,2000)
gi = GifMaker(None,None,size)

mix = None
miy = None
max = None
may = None
for i in range(len(datalist)):
    ci = list(map(int,datalist[i].split(",")))

    if mix == None or ci[0] < mix:
        mix = ci[0]
    
    if miy == None or ci[1] < miy:
        miy = ci[1]
    

    if max == None or ci[0] > max:
        max = ci[0]
    
    if may == None or ci[1] > may:
        may = ci[1]


coefx = ((size[0]-10)/(max-mix))
coefy = ((size[1]-10)/(may-miy))
def conv_interval(co):

    x = int((co[0]-mix)*coefx)
    y = int((co[1]-miy)*coefy)

    return (x,y)

def drawpoint(image,co):

    color = (255,255,255)
    co = conv_interval(co)

    s = 2

    for i in range(-1*s,1*s):
        for j in range(-1*s,1*s):
            image.putpixel((co[0]+i,co[1]+j),color)

def bet(d,f,v):

    if d <= f:
        return d <= v < f
    else:
        return f < v <= d


def drawligne(image,co1,co2):

    color = (255,255,0)
    co1 = conv_interval(co1)
    co2 = conv_interval(co2)

    
    difx = co2[0] - co1[0]
    dify = co2[1] - co1[1]

    
    if dify == 0:
        rx = difx
    else:
        rx = difx/dify

    if difx == 0:
        ry = dify
    else:
        ry = dify/difx


    if (difx < 0 and rx > 0) or (difx > 0 and rx < 0):
        rx *= -1
    
    if (dify < 0 and ry > 0) or (dify > 0 and ry < 0):
        ry *= -1

    vc1 = co1[0]
    vc2 = co1[1]
    while bet(co1[0],co2[0],vc1) and bet(co1[1],co2[1],vc2) :

        vc1 += rx
        vc2 += ry

        if not(bet(co1[0],co2[0],vc1) and bet(co1[1],co2[1],vc2) ):
            break

        image.putpixel((math.floor(vc1),math.floor(vc2)),color)




cos = []
gi.crate_image()
for i in range(len(datalist)):
    ci = list(map(int,datalist[i].split(",")))

    drawpoint(gi.image,ci)
        

    for j in range(i+1,len(datalist)):
        if i != j:
            cj = list(map(int,datalist[j].split(",")))
            cos.append((i,j,dit(ci,cj)))




# print(m)

cos.sort(key=lambda x : x[2])
nb = 0

s = []

while len(s) == 0 or len(s[0]) != len(datalist):
    mi = None
    co = (None,None)

    v = cos.pop(0)
    co = (v[0],v[1])

    ci = list(map(int,datalist[v[0]].split(",")))
    cj = list(map(int,datalist[v[1]].split(",")))

    drawligne(gi.image,ci,cj)
    
    t = False
    nbs = 0
    ls = [None,None]
    ids1 = None
    ids = None
    for ii,ss in enumerate(s):
        if co[0] in s[ii] or co[1] in s[ii]:

            if not(co[0] in s[ii] and co[1] in s[ii]):
                lco = co


            s[ii].add(co[0])
            s[ii].add(co[1])
            t = True
            ls[nbs] = s[ii]

            if ids1 == None:
                ids1 = ii

            ids = ii
            nbs+=1

            if nbs == 2:
                s[ids1] = ls[0].union(ls[1])
                del s[ids]
                break
    
    if t == False:
        s.append(set([co[0],co[1]]))
    

    if  nb % 100 == 0:
        gi.checkImage()

    nb+=1


r = int(datalist[lco[0]].split(",")[0])*int(datalist[lco[1]].split(",")[0])

gi.creatGIF("p2")
print(r)


