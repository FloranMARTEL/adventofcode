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


cos = []

for i in range(len(datalist)):
    for j in range(i+1,len(datalist)):
        if i != j:
            ci = list(map(int,datalist[i].split(",")))
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
        

    nb+=1


r = int(datalist[lco[0]].split(",")[0])*int(datalist[lco[1]].split(",")[0])


print(r)


