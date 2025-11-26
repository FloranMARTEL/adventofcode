#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

connection :dict[str,set]= dict()

tset = set()

allset :list[set]= []

for da in datalist:
    ords = da.split("-")



    if ords[0].startswith("t"):
        tset.add(ords[0])
    if ords[1].startswith("t"):
        tset.add(ords[1])
    
    if ords[0] not in connection:
        connection[ords[0]] = set([ords[1]])
    else:
        connection[ords[0]].add(ords[1])

    

    if ords[1] not in connection:
        connection[ords[1]] = set([ords[0]])
    else:
        connection[ords[1]].add(ords[0])

    allset.append(set(ords))



def merge(s1:set,s2:set):

    res = s1.union(s2)

    con : set = None
    for s in s1:
        if con == None:
            con = connection[s].union(set([s]))
        else:
            con = con.intersection(connection[s].union(set([s])))

    for s in s2:
        if con == None:
            con = connection[s].union(set([s]))
        else:
            con = con.intersection(connection[s].union(set([s])))

    return res.issubset(con)
    

        



# ne = []
# for da in datalist:

#     ord = da.split("-")

#     inter = connection[ord[0]].intersection(connection[ord[1]])

#     for i in inter:
#         if set([ord[0],ord[1],i]) not in ne:
#             ne.append(set([ord[0],ord[1],i]))


                
fin = False
while fin == False:
    fin = True
    id1 = 0
    while id1 < len(allset):
        id2 = id1+1
        while id2 < len(allset):
            if id1 != id2 and merge(allset[id1],allset[id2]):
                m = allset[id1]
                n = allset[id2]
                o = merge(allset[id1],allset[id2])
                allset[id1] = allset[id1].union(allset[id2])
                del allset[id2]
                fin = False
                id2 -=1
            
            id2 += 1
        id1 += 1


maxset = None
maxlen = None
for aset in allset:
    
    if maxlen == None or len(aset) > maxlen:
        maxlen = len(aset)
        maxset = aset

l = list(maxset)

l.sort()

print(",".join(l))
