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


def moddij(graph,start):

    view = {start}
    tab = {start : 0}
    parent = {start : None}

    cc = start
    sew = set()

    candidat = None

    while True or candidat == None or len(candidat) != 0:

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
    
    return parent


def findpath(parent,start,end):
    path = [end]
    curent = end

    if end not in parent:
        # print("pas bien")
        return None

    while curent != start:
        curent = parent[curent]
        path.append(curent)
    path =  list(reversed(path))
    return path


dir = [(0,1),(-1,0),(0,-1),(1,0)]
start = None
end = None

graph = dict()

grapvide = dict()
for i in range(len(datalist)):
    for j in range(len(datalist[i])):
        if datalist[i][j] != "#":
            grapvide[(i,j)] = dict()
            graph[(i,j)] = dict()
            

            for d in dir:

                newi = i+d[0]
                newj = j+d[1]

                if newi >= 0 and newi < len(datalist) and newj >= 0 and newj < len(datalist[i]):
                    
                    if datalist[newi][newj] != "#":

                        graph[(i,j)][(newi,newj)] = 1

        else:
            grapvide[(i,j)] = dict()

            for d in dir:

                newi = i+d[0]
                newj = j+d[1]

                if newi >= 0 and newi < len(datalist) and newj >= 0 and newj < len(datalist[i]):
                    
                    grapvide[(i,j)][(newi,newj)] = 1



        
        if datalist[i][j] == "E":
            end = (i,j)
        elif datalist[i][j] == "S":
            start = (i,j)


pa = dij(graph,start,end)

print(pa)
print(len(pa))
from tqdm import tqdm
cpt = 0
for ip in tqdm(range(len(pa)-2)):
    par = []

    for d in dir:

        newi = pa[ip][0]+d[0]
        newj = pa[ip][1]+d[1]

        if newi >= 0 and newi < len(datalist) and newj >= 0 and newj < len(datalist[i]):
            if datalist[newi][newj] == "#":
                par.append(((newi,newj),moddij(grapvide,(newi,newj))))


    for jp in range(ip+2,len(pa)):

        if pa[jp][0] == 7 and pa[jp][1] == 3:
            print("ici")

        a = pa[ip]
        b = pa[jp]

        for p in par:
            chepath = findpath(p[1],p[0],pa[jp])
            if chepath != None and len(chepath) <= 20:
                m = (jp-ip-1)-len(chepath)
                co = len(pa)-(jp-ip-1) + len(chepath)

                if 100-1 <= (jp-ip-1)-len(chepath):
                    cpt+=1
                    break

        
        # difr = abs(pa[ip][0] - pa[jp][0])
        # difc = abs(pa[ip][1] - pa[jp][1])

        # su = difr+difc

        # if su <= 20: #(difr == 2 and difc == 0 ) or (difc == 2 and difr == 0 ):
            
        #     m = jp-ip
        #     co = len(pa)-(jp-ip-1) + 1

        #     if 76 == (jp-ip-1)-1:
        #         cpt+=1


print(cpt)