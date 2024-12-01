#parti2


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")
l1 = [None] * len(datalist)
l2 = l1[:]

for i in range(len(datalist)):
    dd = datalist[i].split("   ")
    l1[i] = int(dd[0])
    l2[i] = int(dd[1])

cptd = dict()

for v in l2:

    if v in cptd:
        cptd[v] += 1
    else:
        cptd[v] = 1

score = 0
for v in l1:
    if v in cptd:
        mu = cptd[v]
        score+= v*mu


    
print(score)
