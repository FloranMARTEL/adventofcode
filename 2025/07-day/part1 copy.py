#parti1

from Gif import *
from Matrix import *

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

ss = None
m = []
for l in range(len(datalist)):
    m.append([])
    for c in range(len(datalist[l])):
        if datalist[l][c] == "S":
            ss = (l,c)
        m[l].append(datalist[l][c])


gi = GifMaker(r'Source_Code_Pro\PressStart2P-Regular.ttf',8,(1300,2000))
f = set([ss])
cpt = 0
l = 0
while l < len(m)-1:
    print(l)
    if l %5 == 0:
        gi.crate_image()

    newf = set()
    for fi in f:

        v = m[fi[0]+1][fi[1]]
        if v == "^":
            newf.add((fi[0]+1,fi[1]-1))
            newf.add((fi[0]+1,fi[1]+1))
            cpt += 1
        else:
            newf.add((fi[0]+1,fi[1]))

    for fi in newf:
        m[fi[0]][fi[1]] = "|"
    
    f = newf
    ma = Matrix(m)

    if l %2 == 0:
        gi.writeText((10,10),str(ma))

        gi.checkImage()

    l+=1

gi.creatGIF("p2")
print(l)
print(cpt)
