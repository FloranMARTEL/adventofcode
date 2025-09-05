#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def dij(graph,start,end):

    view = {start}
    tab = {start : 0}
    parent = {start : None}

    cc = start
    sew = set()

    candidat = None

    while candidat == None or len(candidat) != 0:

        candidat = []

        des = graph[cc]
        for key in des:
            if des[key] not in sew:
                candidat.append((cc,key,des[key]))

        for c in candidat:
            if c[1] not in tab:
                tab[c[1]] = tab[c[0]]+c[2]
                parent[c[1]] = c[0]
            
            elif tab[c[1]] > tab[c[0]]+c[2]:
                tab[c[1]] = tab[c[0]]+c[2]
                parent[c[1]] = c[0]


            view.add(c[1])

        min = None
        e = None
        for elem  in view.difference(sew):
            if min == None or min > tab[elem]:
                min = tab[elem]
                e = elem

        
        if e != None:
            sew.add(e)
            cc = e
        else:
            print("erreur")
            break

    path = [end]
    curent = end

    if end not in parent:
        print("pas bien")
        return None

    while curent != start:
        curent = parent[curent]
        path.append(curent)
    path =  list(reversed(path))
    return path



rows = 71
cols = 71

grid =[]

for i in range(rows):
    grid.append([])
    for j in range(cols):
        grid[i].append(".")





grapj = dict()

dire = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(rows):
    for j in range(cols):
        
        grapj[(i,j)] = dict()

        for d in dire:

            newr = i+d[0]
            newc = j+d[1]



            if newr >= 0 and newr < rows and newc >= 0 and newc < cols:
                if grid[newr][newc] != "#":
                    grapj[(i,j)][(newr,newc)] = 1

da = 0
res = dij(grapj,(0,0),(rows-1,cols-1))
while True:
    print(da)
    co = datalist[da].split(",")
    co = list(map(int,co))

    grid[co[1]][co[0]] = "#"

    for key in grapj:
        if (co[1],co[0]) in grapj[key]:
            del grapj[key][(co[1],co[0])]


    if (co[1],co[0]) in res:
        res = dij(grapj,(0,0),(rows-1,cols-1))
    if res == None:
        break

    da+=1

print(datalist[da])


        





