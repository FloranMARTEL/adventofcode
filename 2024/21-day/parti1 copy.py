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
grahedir1 = dict()
grahedir2 = dict()

direc = [(0,1),(-1,0),(0,-1),(1,0)]
for i in range(len(directione)):
    for j in range(len(directione[i])):
        if directione[i][j] != None:

            grahedir1[(i,j)] = dict()

            for d in direc:
                
                newi = i+d[0]
                newj = j+d[1]

                if newi >= 0 and newi < len(directione) and newj >= 0 and newj < len(directione[i]):
                    if directione[newi][newj] != None:
                        grahedir1[(i,j)][(newi,newj)] = 1

def gendir2(rob):
    grahedir2 = dict()
    for i in range(len(directione)):
        for j in range(len(directione[i])):
            if directione[i][j] != None:
                grahedir2[(i,j)] = dict()

                for d in direc:
                    
                    newi = i+d[0]
                    newj = j+d[1]

                    if newi >= 0 and newi < len(directione) and newj >= 0 and newj < len(directione[i]):
                        if directione[newi][newj] != None:
                            dircar = convarr(d[0],d[1])[:-1]
                            id = findindex(directione,dircar)
                            a,val = dij(grahedir1,rob,id)
                            val+=1

                            grahedir2[(i,j)][(newi,newj)] = val

    return grahedir2




def genpre(rob,g2):
    for i in range(len(paver)):
        for j in range(len(paver[i])):
            if paver[i][j] != None:

                grahepav[(i,j)] = dict()

                for d in direc:
                    
                    newi = i+d[0]
                    newj = j+d[1]

                    if newi >= 0 and newi < len(paver) and newj >= 0 and newj < len(paver[i]):

                        if paver[newi][newj] != None:
                            dircar = convarr(d[0],d[1])[:-1]
                            id = findindex(directione,dircar)
                            a,val = dij(g2,rob,id)
                            a,val2 = dij(g2,id,rob) #A
                            #val2+=1
                            grahepav[(i,j)][(newi,newj)] = val+val2






    
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

    for c in l:

        g2 = gendir2(rob3)
        g1 = genpre(rob2,g2)


    

    
    print(r)
    su += (int(l[:-1]) * r)

print(su)