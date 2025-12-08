#parti1

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


m = []
cos = []

for i in range(len(datalist)):
    m.append([])
    for j in range(i+1,len(datalist)):

        if i == j:
            m[i].append(0)
        else:

            ci = list(map(int,datalist[i].split(",")))
            cj = list(map(int,datalist[j].split(",")))

            m[i].append(dit(ci,cj))
            cos.append((i,j,dit(ci,cj)))



# print(m)

cos.sort(key=lambda x : x[2])
nb = 0

s = []

while len(cos) > 0:
    mi = None
    co = (None,None)

    v = cos.pop(0)
    co = (v[0],v[1])
    

    t = False
    nbs = 0
    ls = [None,None]
    ids1 = None
    ids = None
    for ii,ss in enumerate(s):
        if co[0] in ss or co[1] in ss:

            if (co[0] in ss and co[1] not in ss) or (co[0] not in ss and co[1] in ss):
                lco = co


            s[ii].add(co[0])
            s[ii].add(co[1])
            t = True
            ls[nbs] = ss

            if ids1 == None:
                ids1 = ii

            ids = ii
            nbs+=1
    
    

    if nbs == 2:
        s[ids1] = ls[0].union(ls[1])
        del s[ids]

    if t == False:
        s.append(set([co[0],co[1]]))
        

    nb+=1



r = int(datalist[lco[0]].split(",")[0])*int(datalist[lco[1]].split(",")[0])


print(r)


