#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

Dir8 = [
    (1,0),
    (1,-1),
    (0,-1),
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
]

def gendir(i,j,dir):
    l = []
    for d in dir:
        newi = i+d[1]
        newj = j+d[0]
        l.append((newi,newj))

    return l

def inBorder(i,j,l):
    return i >= 0 and i < len(l) and j >= 0 and j < len(l[i])

m = []
for l in range(len(datalist)):
    m.append([])
    for c in range(len(datalist[l])):
        m[l].append(datalist[l][c])


print(m)

def find(i,l,li):

    if i >= 0 and i<len(l) and l[i].isnumeric():
        v,s = find(i+1,l,li)
        return l[i]+v,set([(li,i)]).union(s)
    else:
        return "",set()

def find2(i,l,li):

    if i >= 0 and i<len(l) and l[i].isnumeric():
        v,s = find2(i-1,l,li)

        return v+l[i],set([(li,i)]).union(s)
    else:
        return "",set()

cpt=0
cover = set()
for r in range(len(m)):
    for c in range(len(m[r])):
        v = m[r][c]
        if v == "*":

            val = [None,None]
            nid = 0
            
            for (nr,nc) in gendir(r,c,Dir8):
                    
                if inBorder(nr,nc,m) and (not (nr,nc) in cover):
                    vc = m[nr][nc]
                    if vc.isnumeric():
                        num1,co1 = find2(nc-1,m[nr],nr)
                        num2,co2 = find(nc+1,m[nr],nr)
                        cover = cover.union(co1)
                        cover = cover.union(co2)
                        cover.add((nr,nc))
                        
                        num = num1 + vc + num2

                        val[nid] = int(num)
                        nid +=1

                        print(num)

            if nid == 2:
                cpt += val[0]*val[1]



            
print(cpt)