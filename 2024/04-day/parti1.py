#parti1
import numpy as np
import re
from copy import deepcopy

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
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

cdata = deepcopy(datalist)
cpt = 0
for i in range(len(cdata)):
    while True:
        rv = re.search(r"X(.*)M(.*)A(.*)S",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

cdata = deepcopy(datalist)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"S(.*)A(.*)M(.*)X",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

####HHHHHHHHH
# print(va)
cdata = deepcopy(va)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"X(.*)M(.*)A(.*)S",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

cdata = deepcopy(va)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"S(.*)A(.*)M(.*)X",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break


######
diago = []

for i in range(len(datalist)+len(datalist[0])):
    diago.append([None]*len(datalist[0]))

for i in range(len(datalist)):
    for j in range(len(datalist[0])):
        
        diago[i-j+len(datalist[0])-1][j] = datalist[i][j]

vdiago = []
for i in range(len(diago)):
    t = ""
    for j in range(len(diago[i])):
        if diago[i][j] != None:
            t+=diago[i][j]
    vdiago.append(t)

# print(vdiago)


######

cdata = deepcopy(vdiago)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"X(.*)M(.*)A(.*)S",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

cdata = deepcopy(vdiago)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"S(.*)A(.*)M(.*)X",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break


#dzqiubdqiuzdbuiqzbduibqzd
diago = []

for i in range(len(datalist)+len(datalist[0])):
    diago.append([None]*len(datalist[0]))

for i in range(len(datalist)):
    for j in range(len(datalist[0])):
        j2 = abs(len(datalist[0])-1-j)
        diago[i-j2+len(datalist[0])-1][j] = datalist[i][j]

vdiago = []
for i in range(len(diago)):
    t = ""
    for j in range(len(diago[i])):
        if diago[i][j] != None:
            t+=diago[i][j]
    vdiago.append(t)

# print(vdiago)


######

cdata = deepcopy(vdiago)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"X(.*)M(.*)A(.*)S",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

cdata = deepcopy(vdiago)
for i in range(len(cdata)):
    while True:
        rv = re.search(r"S(.*)A(.*)M(.*)X",cdata[i])
        if rv != None:
            end = rv.span(0)[0]
            cdata[i] = cdata[i][end+1:]

            v = [rv.group(1),rv.group(2),rv.group(3)]
            valide = True
            for vv in v:
                if "X" in vv or "M" in vv or "A" in vv or "S" in vv:
                    valide = False

            if valide:
                cpt+=1
                # print(i)
                # print(rv)
        else:
            break

print(cpt)