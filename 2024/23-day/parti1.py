#parti1

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

tset = set()
allset = []
for da in datalist:
    ords = da.split("-")
    find = False

    if ords[0].startswith("t"):
        tset.add(ords[0])
    if ords[1].startswith("t"):
        tset.add(ords[1])

    for aset in allset:
        if ords[0] in aset or ords[1] in aset:
            find = True
            aset.add(ords[0])
            aset.add(ords[1])
            break
    
    if find==False:
        ns = set(ords)
        print(ns)
        allset.append(ns)

cpt=0
for aset in allset:
    if len(aset) == 3:
        val = False
        for s in aset:
            if s in tset:
                val = True
                break
        
        if val:
            cpt+=1

print(cpt)