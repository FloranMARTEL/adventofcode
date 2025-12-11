#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


d = dict()

for l in datalist:

    el = l.split(":")

    s = el[0]

    o = el[1].split()

    d[s] = []
    for oi in o:
        d[s].append(oi)

    

par = {"svr" : [None]}

openlist = ["svr"]


clo = set()
while len(openlist) != 0:

    curent = openlist.pop()

    if curent in clo or curent == "out":
        continue
    clo.add(curent)

    nei = d[curent]

    for n in nei:

        if n in par:
            par[n].append(curent)
        else:
            par[n] = [curent]

        openlist.append(n)        

cpt = 0
from  functools import *
@cache
def getss(end,start,ff=False,cc=False):


        if end == start:
            # print("la")
            if ff == True and cc == True:    
                return 1
            else:
                return 0

        su = 0
        for p in par[end]:
            
            ff2 = ff
            cc2 = cc
            if p == "fft":
                ff2 = True
            if p == "dac":
                cc2 = True

            l = getss(p,start,ff2,cc2)
            su += l
            # for e in range(len(l)):

                
            #     l[e].add(p)

            #     lich.append(set(l[e]))
            
            # myset = myset.union(getss(p,start,parent))

        return su

print("ici")
res = getss("out","svr")

print(res)
# for i,r in enumerate(res):
#     if "fft" in r and "dac" in r:
#         print(i)
#         cpt +=1


print(cpt)