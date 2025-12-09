#parti2
from Gif import *
G = GifMaker(r'Source_Code_Pro\PressStart2P-Regular.ttf',8,(500,500))


file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")



m = []
# for l in range(len(datalist)):
#     m.append([])
#     for c in range(len(datalist[l])):
#         m[l].append(datalist[l][c])
from Matrix import *
m = Matrix(datalist).get().list

print(len(m))
print(len(m[0]))

Dir8 = [
    (1,0),
    (1,-1),
    (0,-1),
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
],

p = 0
vali = 0
while True:
    p+=1
    print(p)
    G.crate_image()
    G.writeText((10,10),Matrix(m).__str__(),fontsize=30)
    G.checkImage(100)
    s = set()
    for i in range(len(m)):
        for j in range(len(m[i])):

            v = m[i][j]
            if v == "@":
                cptr=0
                for d in Dir8[0]:
                    newi = i+ d[1]
                    newj = j + d[0]

                    if newi >= 0 and newi < len(m) and newj >= 0 and newj < len(m):
                        if m[newi][newj] == "@":
                            cptr += 1

                if cptr < 4:
                    vali +=1
                    s.add((i,j))

    if len(s) == 0:
        break

    for c in s:
        m[c[0]][c[1]] = "x"
        

    G.crate_image()
    G.writeText((10,10),Matrix(m).__str__(),fontsize=30)
    G.checkImage(100)


    for c in s:
        m[c[0]][c[1]] = "."

    
    

G.creatGIF("gifday4p2d")
print(vali)




