#parti2

from copy import deepcopy

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

gar = [None,None]

durection = [(-1,0),(0,1),(1,0),(0,-1)]
id = 0

tab = []
for i in range(len(datalist)):
    tab.append([])
    for j in range(len(datalist[i])):
        tab[i].append(datalist[i][j])
        if datalist[i][j] in ["^",">","<","v"]:
            gar = [i,j]

            if datalist[i][j] ==  "^":
                id=0
            elif datalist[i][j] ==  ">":
                id=1
            elif datalist[i][j] ==  "v":
                id=2
            elif datalist[i][j] ==  "<":
                id=3


boucle = 0
garsource = gar[:]
ds = id
for i in range(len(tab)):
    for j in range(len(tab[i])):
        print((i,j))
        if i == 6 and j == 3:
            print("ici")

        newtab = deepcopy(tab)

        if newtab[i][j] == ".":
            newtab[i][j] = "#"
            gar = garsource[:]
            id = ds


            # place = set()
            placeb = set()
            end = False
            while end == False:

                # place.add((gar[0],gar[1]))

                if (gar[0],gar[1],id) in placeb:
                    print("block:")
                    print((i,j))
                    boucle+=1
                    break
                else:
                    placeb.add((gar[0],gar[1],id))

                r = gar[0]+durection[id][0]
                c = gar[1]+durection[id][1]

                if r < 0 or r >=len(newtab) or c < 0 or c >= len(newtab[0])  :
                    break
                
                front = newtab[r][c]
                newtab[gar[0]][gar[1]] = "x"


                if front == "#":
                    id = (id+1)%4
                else:
                    gar = [r,c]


print(boucle)






