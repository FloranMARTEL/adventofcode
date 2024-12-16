#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


li = []
for i in range(len(datalist)):
    li.append([])
    for j in range(len(datalist[i])):
        li[i].append(int(datalist[i][j]))


pos = [(1,0),(-1,0),(0,-1),(0,1)]

def getscore(i,j,val):


    s = 0

    for p in pos:

        x = i+p[0]
        y = j+p[1]

        if x >= 0 and x < len(li) and y >=0 and y < len(li[0]):
            v = li[x][y]
            if v == val+1:

                if v == 9:
                    s += 1
                else:
                    s += getscore(x,y,v)
    
    return s
            




su = 0
for i in range(len(li)):
    for j in range(len(li[i])):
        val = li[i][j]

        if val == 0:
            point = set()
            re = getscore(i,j,val)
            su+=re

print(su)