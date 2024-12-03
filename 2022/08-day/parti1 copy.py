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





cpt = 0

cpl = set()

def rec(ref,i,j):
    global d2

    t= f"{i},{j}"

    if (i >= len(d2) or i < 0 or j < 0 or j >= len(d2[0])) or (t in cpl):
        return



    if (i == len(d2)-1 or i == 0 or j == 0 or j == len(d2[0])-1) or ref < d2[i][j]:

        cpl.add(f"{i},{j}")
        a = d2[i][j]
        d2[i][j] = True

        rec(a,i+1,j)
        rec(a,i-1,j)
        rec(a,i,j+1)
        rec(a,i,j-1)



rec(-1,0,0)

print(len(cpl)) 
            

