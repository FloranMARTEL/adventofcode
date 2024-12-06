#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
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


place = set()
end = False
while end == False:

    place.add((gar[0],gar[1]))

    r = gar[0]+durection[id][0]
    c = gar[1]+durection[id][1]

    if r < 0 or r >=len(tab) or c < 0 or c >= len(tab[0])  :
        break
    
    front = tab[r][c]

    if front == "#":
        id = (id+1)%4
    else:
        gar = [r,c]


print(len(place))






