#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def dij(graph,start,end):

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
            # print("erreur")
            break

    path = [end]
    curent = end

    if end not in parent:
        print("pas bien")
        return None,None

    while curent != start:
        curent = parent[curent]
        path.append(curent)
    path =  list(reversed(path))
    return path,tab[end]


paver = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"]
]

directione = [
    [None,"^","A"],
    ["<","v",">"]
]

def convarr(dir,dic):

    text = ""
    if dir < 0:
        text += "^"*abs(dir)
    elif dir > 0:
        text += "v"*abs(dir)
    
    if dic < 0:
        text += "<"*abs(dic)
    elif dic > 0:
        text += ">"*abs(dic)
    

    return text+"A"

def findindex(man,c):
    for i in range(len(man)):
        for j in range(len(man[i])):
            if man[i][j] == c:
                return (i,j)

rob1 = (3,2)
rob2 = (0,2)
rob3 = (0,2)


grahepav = dict()
grahedir = dict()
grahedir2 = dict()

direc = [(0,1),(-1,0),(0,-1),(1,0)]
for i in range(len(directione)):
    for j in range(len(directione[i])):
        if directione[i][j] != None:

            grahedir[(i,j)] = dict()

            for d in direc:
                
                newi = i+d[0]
                newj = j+d[1]

                if newi >= 0 and newi < len(directione) and newj >= 0 and newj < len(directione[i]):
                    if directione[newi][newj] != None:
                        grahedir[(i,j)][(newi,newj)] = 1


for i in range(len(paver)):
    for j in range(len(paver[i])):
        if paver[i][j] != None:

            grahepav[(i,j)] = dict()

            for d in direc:
                
                newi = i+d[0]
                newj = j+d[1]

                if newi >= 0 and newi < len(paver) and newj >= 0 and newj < len(paver[i]):

                    if paver[newi][newj] != None:
                        grahepav[(i,j)][(newi,newj)] = 1






    
#'v<<A^>>AvA^A""v<<""A^>>AAv<A<A^>>AA<Av>AA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A'
#'<A>A""<""AAv<AA^>>AvAA^Av<AAA^>A'
def givepathr1(l,pav,rb):
    fin = ""
    for c in l:

        pasc = findindex(pav,c)

        dir = pasc[0] - rb[0]
        dic = pasc[1] - rb[1]

        ar = convarr(dir,dic)
        fin +=ar
        rb = pasc
    
    return fin,rb

su = 0
fin = ""
for l in datalist:
    r = 0
    for c in l:
        pasc = findindex(paver,c)
        a,val = dij(grahepav,rob1,pasc)

        for i in range(len(a)-1):
            dir = a[i+1][0] - a[i][0]
            dic = a[i+1][1] - a[i][1]
            ar = convarr(dir,dic)[:-1]
            pasc2 = findindex(directione,ar)
            a2,val = dij(grahedir,rob2,pasc2)

            for j in range(len(a2)-1):
                dir2 = a2[j+1][0] - a2[j][0]
                dic2 = a2[j+1][1] - a2[j][1]
                ar2 = convarr(dir2,dic2)[:-1]
                pasc3 = findindex(directione,ar2)
                a3,val = dij(grahedir,rob3,pasc3)
                r += val+1
                rob3 = pasc3

            pasc3 = findindex(directione,"A")
            a3,val = dij(grahedir,rob3,pasc3)
            r += val+1
            rob3 = pasc3


            rob2 = pasc2

        ####

        pasc2 = findindex(directione,"A")
        a2,val = dij(grahedir,rob2,pasc2)

        for j in range(len(a2)-1):
            dir2 = a2[j+1][0] - a2[j][0]
            dic2 = a2[j+1][1] - a2[j][1]
            ar2 = convarr(dir2,dic2)[:-1]
            pasc3 = findindex(directione,ar2)
            a3,val = dij(grahedir,rob3,pasc3)
            r += val+1
            rob3 = pasc3

        pasc3 = findindex(directione,"A")
        a3,val = dij(grahedir,rob3,pasc3)
        r += val+1
        rob3 = pasc3


        rob2 = pasc2

        rob1 = pasc







    # newl,rob1 = givepathr1(l,paver,rob1)
    # newl,rob2 = givepathr1(newl,directione,rob2)
    # newl,rob3 = givepathr1(newl,directione,rob3)

    # print(len(newl))
    print(r)
    su += (int(l[:-1]) * r)

print(su)