#parti1

from  functools import *

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

ss = None
m = []
for l in range(len(datalist)):
    m.append([])
    for c in range(len(datalist[l])):
        if datalist[l][c] == "S":
            ss = (l,c)
        m[l].append(datalist[l][c])

@cache
def prg(l,s):

    if s[0]+1 == len(m):
        return 1
    
    v = m[s[0]+1][s[1]]

    su = 0
    if v == "^":
        su += prg(l+1,(s[0]+1,s[1]-1))
        su += prg(l+1,(s[0]+1,s[1]+1))
    else:
        su += prg(l+1,(s[0]+1,s[1]))

    return su



cpt = prg(l,ss)


print(cpt)
