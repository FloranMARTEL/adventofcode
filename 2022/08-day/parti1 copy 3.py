from copy import deepcopy

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

d2 = []

for i in range(len(datalist)):
    d2.append([])
    for j in range(len(datalist[i])):
        d2[i].append(int(datalist[i][j]))

d3 = []

for i in range(len(datalist)):
    d3.append([])
    for j in range(len(datalist[i])):
        d3[i].append(False)


####################
for l in range(len(d2)):
    max = -1
    for c in range(len(d2)):
        if d2[l][c]>max:
            d3[l][c] = True
            max = d2[l][c]
        


for l in range(len(d2)):
    max = -1
    for c in range(len(d2)-1,-1,-1):
        if d2[l][c]>max:
            d3[l][c] = True
            max = d2[l][c]


for c in range(len(d2)):
    max = -1
    for l in range(len(d2)):
        if d2[l][c]>max:
            d3[l][c] = True
            max = d2[l][c]


for c in range(len(d2)):
    max = -1
    for l in range(len(d2)-1,-1,-1):
        if d2[l][c]>max:
            d3[l][c] = True
            max = d2[l][c]

cpt = 0
for l in d3:
    for e in l:
        if e == True:
            cpt+=1

print(cpt) 
            

