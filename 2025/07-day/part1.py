#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

ss = None
m = []
for l in range(len(datalist)):
    m.append([])
    for c in range(len(datalist[l])):
        if datalist[l][c] == "S":
            ss = (l,c)
        m[l].append(datalist[l][c])


f = set([ss])
cpt = 0
l = 0
while l < len(m)-1:
    newf = set()
    for fi in f:

        v = m[fi[0]+1][fi[1]]
        if v == "^":
            newf.add((fi[0]+1,fi[1]-1))
            newf.add((fi[0]+1,fi[1]+1))
            cpt += 1
        else:
            newf.add((fi[0]+1,fi[1]))
    
    f = newf
    
    l+=1

print(cpt)
