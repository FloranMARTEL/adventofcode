from copy import deepcopy

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

d2 = []

for i in range(len(datalist)):
    d2.append([])
    for j in range(len(datalist[i])):
        d2[i].append(int(datalist[i][j]))




####################
res = []
for lArb in range(len(d2)):
    for cArb in range(len(d2[lArb])):
        Carbre = d2[lArb][cArb]

        d=0
        lmax = -1
        for i in range(cArb+1,len(d2)):
            

            d +=1# abs(cArb-i)
            if d2[lArb][i] >= Carbre:
                break
        

        g=0
        lmax = -1
        for i in range(cArb-1,-1,-1):
            

            g +=1# abs(cArb-i)
            if d2[lArb][i] >= Carbre:
                break
        
        b=0
        lmax = -1
        for i in range(lArb+1,len(d2)):
            

            b +=1# abs(lArb-i)

            if d2[i][cArb] >= Carbre:
                break

        h=0
        lmax = -1
        for i in range(lArb-1,-1,-1):
            

            h +=1# abs(lArb-i)
            if d2[i][cArb] >= Carbre:
                break


        print(d2[lArb][cArb],lArb,cArb , g*d*b*h)
        res.append(g*d*b*h)


print(max(res))

            

