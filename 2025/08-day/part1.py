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

while nb < 1000:
    print(nb)
    mi = None
    co = (None,None)

    v = cos.pop(0)
    co = (v[0],v[1])
    # for i in range(len(m)):
    #     for j in range(len(m[i])):
            
    #         if i != j and m[i][j] != None:
    #             if mi == None or m[i][j] < mi:
    #                 mi = m[i][j]
    #                 co = (i,j)
    
    # m[co[0]][co[1]] = None
    # m[co[1]][co[0]] = None

    if 2 in co:
        print("ici")

    t = False
    nbs = 0
    ls = [None,None]
    ids1 = None
    ids = None
    for ii,ss in enumerate(s):
        if co[0] in ss or co[1] in ss:
            s[ii].add(co[0])
            s[ii].add(co[1])
            t = True
            ls[nbs] = ss

            if ids1 == None:
                ids1 = ii

            ids = ii
            nbs+=1

            # for e in ss:
            #     m[e][co[1]] = None
            #     m[co[0]][e] = None
            #     m[co[1]][e] = None
            #     m[e][co[0]] = None
    
    if nbs == 2:
        s[ids1] = ls[0].union(ls[1])
        del s[ids]

        # for e in s[ids1]:
        #     for e2 in s[ids1]:
        #         m[e][e2] = None
        #         m[e2][e] = None

    if t == False:
        s.append(set([co[0],co[1]]))
        # m[co[0]][co[1]] = None
        # m[co[1]][co[0]] = None
        

    nb+=1


ne = list(map(len,s))

ne.sort(reverse=True)
print(ne)

muu = 1
for i in range(3):
    muu*=ne[i]

print(muu)


