#parti1
import numpy as np
import re
from copy import deepcopy

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

nn =[]
for i in range(len(datalist)):
    nn.append([])
    for j in range(len(datalist[i])):
        nn[i].append(datalist[i][j])


a = np.array(nn).T

va = []
for i in range(len(a)):
    t = ""
    for j in range(len(a[i])):
        t+=a[i][j]
    va.append(t)

##

diago = []

for i in range(len(datalist)+len(datalist[0])):
    diago.append([None]*len(datalist[0]))

for i in range(len(datalist)):
    for j in range(len(datalist[0])):
        
        diago[i-j+len(datalist[0])-1][j] = datalist[i][j]

cpt = 0

#
diago2 = []

for i in range(len(datalist)+len(datalist[0])):
    diago2.append([None]*len(datalist[0]))

for i in range(len(datalist)):
    for j in range(len(datalist[0])):
        j2 = abs(len(datalist[0])-1-j)
        diago2[i-j2+len(datalist[0])-1][j] = datalist[i][j]

par = [diago]

for i in range(1,len(nn)-1):
    for j in range(1,len(nn[0])-1):
        v = nn[i][j]
        if v == "A":

            d1 = False

            if (nn[i+1][j+1] == "M" and nn[i-1][j-1] == "S") or (nn[i+1][j+1] == "S" and nn[i-1][j-1] == "M"):
                d1 = True
            
            d2 = False

            if (nn[i-1][j+1] == "M" and nn[i+1][j-1] == "S") or (nn[i-1][j+1] == "S" and nn[i+1][j-1] == "M"):
                d2 = True
            
            if d1 and d2:

                cpt+=1

        



print(cpt)

