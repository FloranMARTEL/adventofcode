#parti2
from copy import deepcopy

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

da = []

for i in range(len(datalist)):
    da.append([])
    for j in range(len(datalist[i])):
        da[i].append(datalist[i][j])

d = deepcopy(da)

anti = set()

for i in range(len(da)):
    for j in range(len(da[i])):
        val = da[i][j]
        if val != ".":

            for r in range(len(da)):
                for l in range(len(da[i])):

                    val2 = da[r][l]

                    if val==val2 and not(r==i and l==j):

                        k = 0
                        while True:

                            vr = i + ((i-r)*k)
                            vl = j + ((j-l)*k)


                            if vr >= 0 and vr < len(da) and vl >= 0 and vl < len(da[i]):
                                

                                d[vr][vl] = "#"
                                anti.add((vr,vl))
                            else:
                                break

                            k+=1
                    



print(len(anti))
                        

