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

for li in par:


    for i in range(len(li)):
        m = False
        a = False

        s2 = False
        a2 = False
        for j in range(len(li[0])):
            oo = li[i]
            v=li[i][j]
            if v == "M" and not a:
                m = True
            elif v == "A" and m and not a:
                a = True
            elif v == "S" and a:
                
                cl = i+j-(len(li[0])-1)

                if (nn[cl-2][j] == "M" and nn[cl][j-2] == "S") or (nn[cl-2][j] == "S" and nn[cl][j-2] == "M"):
                    cpt+=1

                x = False
                m = False
                a = False
            elif v in ("M","A","S"):
                m = False
                a = False

                if v == "M":
                    x = True
            else:
                m = False
                a = False
                    
            
            #reverse
            if v == "S" and not a2:
                s2 = True
            elif v == "A" and s2 and not a2:
                a2 = True
            elif v == "M" and a2 :
                cl = i+j-(len(li[0])-1)

                print(nn[cl][j])

                if (nn[cl-2][j] == "M" and nn[cl][j-2] == "S") or (nn[cl-2][j] == "S" and nn[cl][j-2] == "M"):
                    cpt+=1

                s2 = False
                a2 = False
                m2 = False
            elif v in ("S","A","M"):
                s2 = False
                a2 = False

                if v == "S":
                    s2 = True
            else:
                s2 = False
                a2 = False


print(cpt)

