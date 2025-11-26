#parti1


def dijmod(graph,start,end):

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
            if True :
                candidat.append((cc,key,des[key]))
                

        for c in candidat:
            if c[1] not in tab:
                tab[c[1]] = tab[c[0]]+c[2]
                parent[c[1]] = {c[0]}
            
            elif tab[c[1]] > tab[c[0]]+c[2]:
                tab[c[1]] = tab[c[0]]+c[2]
                parent[c[1]] = {c[0]}
            elif tab[c[1]] == tab[c[0]]+c[2] :
                parent[c[1]].add(c[0])


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

        

    
    def getss(end,start,path : list,parent):

        path.append(end)

        if end == start:
            return [list(reversed(path))]

        myset = []

        
        for p in parent[end]:
            m = getss(p,start,path[:],parent)
            
            for n in m:
                myset.append(n)


        return myset

    

    return getss(end,start,[],parent)



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

def com2(p):
    some = 0
    rob = (0,2)
    for j in range(len(p)-1):
        d = (p[j+1][0] - p[j][0], p[j+1][1] - p[j][1])
        ar = convarr(d[0],d[1])[:-1]

        cilbe = findindex(directione,ar)

        nul,val = dij(grahedir,rob,cilbe)
        some += val+1

        rob = cilbe
    
    #A
    null,val = dij(grahedir,rob,findindex(directione,"A"))
    some += val+1

    rob = (0,2)
    return some


su = 0
fin = ""
for l in datalist:
    so = 0
    for c in l:
        cible = findindex(paver,c)
        pp = dijmod(grahepav,rob1,cible)
        
        minp = None

        oldb2 = rob2
        v = None
        for p in pp:
            rob2 = oldb2
            some2 = 0

            for i in range(len(p)-1):
                d = (p[i+1][0] - p[i][0], p[i+1][1] - p[i][1])
                ar = convarr(d[0],d[1])[:-1]

                cilbe2 = findindex(directione,ar)

                pp2 = dijmod(grahedir,rob2,cilbe2)

                min3 = None
                for p2 in pp2:
                    
                    res3 = com2(p2)

                    if min3 == None or  min3 > res3:
                        min3 = res3
                
                some2 += min3
                rob2 = cilbe2
            
            #A

            pp2 = dijmod(grahedir,rob2,findindex(directione,"A"))

            min3 = None
            for p2 in pp2:
                res3 = com2(p2)
                
                if min3 == None or  min3 > res3:
                        min3 = res3
                            
            some2 += min3
            rob2 = (0,2)
            
            ####""

            

            if v == None or  v > some2:
                v = some2


        rob1 = cible
        # print(pp)

        # print(v)
        so += v
    print(so, int(l[:-1]))

    su += so * int(l[:-1])
    

    
    # print(r)
    # su += (int(l[:-1]) * r)

print(su)