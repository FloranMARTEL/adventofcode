#parti1


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")



m = []
# for l in range(len(datalist)):
#     m.append([])
#     for c in range(len(datalist[l])):
#         m[l].append(datalist[l][c])
from Matrix import *
m = Matrix(datalist).get().list

Dir8 = [
    (1,0),
    (1,-1),
    (0,-1),
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
]

vali = 0
for i in range(len(m)):
    for j in range(len(m[i])):

        v = m[i][j]
        if v == "@":
            cptr=0
            for d in Dir8:
                newi = i+ d[1]
                newj = j + d[0]

                if newi >= 0 and newi < len(m) and newj >= 0 and newj < len(m):
                    if m[newi][newj] == "@":
                        cptr += 1

            if cptr < 4:
                vali +=1


print(vali)




