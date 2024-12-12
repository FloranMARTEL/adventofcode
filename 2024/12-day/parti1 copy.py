#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")



region = []

dire = [(1,0),(-1,0),(0,1),(0,-1)]

def rec(i,j,s :set = set()):
    val = datalist[i][j]
    
    s.add((i,j,val))

    for d in dire:
        if i+d[0] >= 0 and i+d[0] < len(datalist) and j+d[1] >= 0 and j+d[1] < len(datalist[0]):
            if datalist[i+d[0]][j+d[1]] == val and (i+d[0],j+d[1],val) not in s:
                s.union(rec(i+d[0],j+d[1],s))
    
    return s


for i in range(len(datalist)):
    for j in range(len(datalist[i])):

        c = True
        for r in region:
            if (i,j,datalist[i][j]) in r:
                c = False
                break
        
        if c:
            region.append(rec(i,j,set()))

for r in region:
    print(len(r), r)


def cptclot(o,s):

    if o[2] in ((-1,0),(1,0)):
        d = (o[0],o[1]+1,o[2])
        cptd = 0
        if d in s:
            s.remove(d)
            cptd = cld(d,s)
        
        g = (o[0],o[1]-1,o[2])
        cptg = 0
        if g in s:
            s.remove(g)
            cptg = clg(d,s)
        
        return 1
    
    elif o[2] in ((0,-1),(0,1)):
        d = (o[0]+1,o[1],o[2])
        cptd = 0
        if d in s:
            s.remove(d)
            cptd = cld(d,s)
        
        g = (o[0]-1,o[1],o[2])
        cptg = 0
        if g in s:

            s.remove(g)
            cptg = clg(d,s)
        
        return 1

    return 1
    
def cld(o,s):

    if o[2] in ((-1,0),(1,0)):
        d = (o[0],o[1]+1,o[2])
        cptd = 0
        if d in s:
            cptd = cld(d,s)
        
        return 1
    
    elif o[2] in ((0,-1),(0,1)):
        d = (o[0]+1,o[1],o[2])
        cptd = 0
        if d in s:
            s.remove(d)
            cptd = cld(d,s)
        
        return 1

    return 1


def clg(o,s):
    if o[2] in ((-1,0),(1,0)):

        g = (o[0],o[1]-1,o[2])
        cptg = 0
        if g in s:
            s.remove(g)
            cptg = clg(d,s)
        
        return 1
    
    elif o[2] in ((0,-1),(0,1)):
        
        g = (o[0]-1,o[1],o[2])
        cptg = 0
        if g in s:
            s.remove(g)
            cptg = clg(d,s)
        
        return 1

    return 1




dir2 = [(1,0),(-1,0),(0,1),(0,-1)]
su = 0
for r in region:
    cl = 0
    setcl = set()
    for co in r:

        for d in dir2:

            if co[0]+d[0] >= 0 and co[0]+d[0] < len(datalist) and co[1]+d[1] >= 0 and co[1]+d[1] < len(datalist[0]):
                if datalist[co[0]+d[0]][co[1]+d[1]] != co[2]:
                    setcl.add((co[0]+d[0],co[1]+d[1],d))
            else:
                setcl.add((co[0]+d[0],co[1]+d[1],d))
    
    while len(setcl) > 0:
        c = setcl.pop()
        cl += cptclot(c,setcl)

    

    print(cl,len(r))

    su += (cl * len(r))

print(su)




        