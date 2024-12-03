from copy import deepcopy

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

for i in range(len(datalist)):
    intli = []
    for j in range(len(datalist[i])):
        intli.append(int(datalist[i][j]))
    datalist[i] = intli



tli = []
for l in range(len(datalist)):
    tli.append([])
    for e in range(len(datalist[l])):
        tli[l].append(False)

        


add = True
while add == True:
    add = False
    for i,l in enumerate(datalist):
            
        for j,e in enumerate(l):

            if (j == 0 or j == len(l)-1 or i == 0 or i == len(datalist)-1) and tli[i][j] != True:
                tli[i][j] = True
                add = True

            
            if tli[i][j] == True:

                h = datalist[i][j]

                if i+1 < len(datalist):
                    n = datalist[i+1][j]

                    if n > h and tli[i+1][j] != True:
                        tli[i+1][j] = True
                        add = True

                if i-1 >= 0:
                    s = datalist[i-1][j]

                    if s > h and tli[i-1][j] != True:
                        tli[i-1][j] = True
                        add = True

                if j+1 < len(l):
                    e = datalist[i][j+1]

                    if e > h and tli[i][j+1] != True:
                        tli[i][j+1] = True
                        add = True


                if j-1 >= 0:
                    w = datalist[i][j-1]

                    if w > h and tli[i][j-1] != True:
                        tli[i][j-1] = True
                        add = True


cpt = 0
for l in tli:
    for e in l:
        if e==True:
            cpt+=1

print(cpt) 
            

