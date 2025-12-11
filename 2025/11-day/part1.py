#parti1

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

    

par = {"you" : [None]}

openlist = ["you"]


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

from  functools import *
@cache
def getss(end,start):


        if end == start:
            return 1

        su = 0
        for p in par[end]:

            su += getss(p,start)

        return su


res = getss("out","you")

print(res)