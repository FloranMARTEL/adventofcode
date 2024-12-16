#parti1

from copy import deepcopy

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

dada = []
for i in range(len(datalist)):
    dada.append([])
    for j in range(len(datalist[i])):
        dada[i].append(datalist[i][j])

datalist = dada

class chemian:

    def __init__(self,view,tab,parent,cc,sew):
        self.view = view
        self.tab = tab
        self.parent = parent
        self.cc = cc
        self.sew =sew

        


def dij(graph,start,end):

    listchem = [chemian({start},{start : 0},{start : None},start,set())]
    chhhe = []

    # view = {start}
    # tab = {start : 0}
    # parent = {start : None}

    # cc = start
    # sew = set()


    for chem in listchem:
        candidat = None

    
        while candidat == None or len(candidat) != 0:

            candidat = []

            des = graph[chem.cc]
            for key in des:
                if des[key] not in chem.sew:
                    candidat.append((chem.cc,key,des[key]))

            for c in candidat:
                if c[1] not in chem.tab:
                    chem.tab[c[1]] = chem.tab[c[0]]+c[2]
                    chem.parent[c[1]] = c[0]
                
                elif chem.tab[c[1]] > chem.tab[c[0]]+c[2]:
                    chem.tab[c[1]] = chem.tab[c[0]]+c[2]
                    chem.parent[c[1]] = c[0]

                #del graph[c[0]][c[1]]

                chem.view.add(c[1])

            min = None
            e = None
            for elem  in chem.view.difference(chem.sew):
                if min == None or min > chem.tab[elem]:
                    min = chem.tab[elem]
                    e = elem
            
            for elem in chem.view.difference(chem.sew):
                if chem.tab[elem] == min and elem != e :
                    newsew = chem.sew.copy()
                    newsew.add(elem)
                    listchem.append(chemian(chem.view,chem.tab,chem.parent,elem,newsew))
                elif chem.tab[elem] == min and elem == e:
                    chem.sew.add(e)
                    chem.cc = e


            # if e != None:
            #     chem.sew.add(e)
            #     chem.cc = e
            # else:
            #     print("erreur")
            #     break

        path = [end]
        curent = end
        while curent != start:
            curent = chem.parent[curent]
            path.append(curent)
        path =  list(reversed(path))
        chhhe.append(path)

    return chhhe


g = { (1,1,(-1,0)) : {(0,1,(-1,0)) : 1},
     (0,1,(-1,0)) : {(-1,1,(-1,0)) : 1}}
        
graph={
  's':{'a':2,'b':4},
  'a':{'b':2},
  'b':{'a':3,'c':2,'d':5},
  'c':{'d':2},
  'd':{}
}

r = dij(graph,'s','b')



direction =[(1,0),(0,1),(-1,0),(0,-1)]

di = dict()

source = (None,None)
end = (None,None)

for i in range(len(datalist)):
    for j in range(len(datalist[i])):

        if datalist[i][j] == "S":
            source = (i,j,direction[1])
        if datalist[i][j] == "E":
            end = (i,j,direction[2])

        if datalist[i][j] != "#":
            for idd in range(len(direction)):

                d = direction[idd]
                
                di[(i,j,d)] = dict()
                if i+d[0] >= 0 and i+d[0] < len(datalist) and j+d[1] >= 0 and j+d[1] < len(datalist[i]):
                    if datalist[i+d[0]][j+d[1]] != "#":
                        di[(i,j,d)][(i+d[0],j+d[1],d)] = 1
                
                di[(i,j,d)][(i,j,direction[(idd+1)%4])] = 1000
                di[(i,j,d)][(i,j,direction[(idd-1)%4])] = 1000




import time

res = dij(deepcopy(di),source,end)
# res2 = dij(deepcopy(di),source,(end[0],end[1],direction[1]))
su = 0
da = datalist
for i in range(len(res)-1):
    v = di[res[i]][res[i+1]]
    su += di[res[i]][res[i+1]]
    da[res[i][0]][res[i][1]] = "S"

    # text = "\n".join(list(map(lambda x : "".join(x),da)))

    # print(text)
    # print(v)
    # f = open("test.txt","w")

    # f.write(f"{v}\n{text}")
    # f.close()

    # time.sleep(0.25)





print(len(res))

print(su)
