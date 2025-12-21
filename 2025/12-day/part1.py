#parti1
from Matrix import *

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


f = datalist[-1]

matlist = []
for d in datalist[:-1]:

    [id,mat] = d.split(":\n")

    mat = Matrix(mat.split("\n"))

    matlist.append(mat)
    # print(mat) 

f = f.split("\n")

si = []
for l in f:

    aa = l.split(":")
    s,n = aa[0],aa[1]

    sit = list(map(int,s.split("x")))

    n = list(map(int,n.split()))

    si.append((sit,n))

cptf = 0
for s in si:
    su = 0
    for ii,t in enumerate(s[1]):
        su += t*matlist[ii].nbd

    a = s[0][0] * s[0][1]

    if su > a:
        cptf +=1

print(cptf)
print(len(si))
print(len(si)-cptf)

    



