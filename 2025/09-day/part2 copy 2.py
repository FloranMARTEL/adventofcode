#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


co = []

cox = set()
coy = set()
for l in datalist:

    c = l.split(",")
    c = list(map(int,c))
    co.append(c)

    cox.add(c[0])
    coy.add(c[1])

co = list(map(lambda x : (x[0],x[1]), co))
co2 = co[:]
co.sort(key=lambda x: x[0])
co2.sort(key=lambda x: x[1])

cox = list(cox)
cox.sort()

coy = list(coy)
coy.sort()

xmi,xma = co[0][0],co[-1][0]
ymi,yma = co2[0][1],co2[-1][1]

# for i in range(len(co)):
#     co[i] = (co[i][0]-xmi,co[i][1]-ymi)

dix = dict()
revdix = dict()
diy = dict()
revdiy = dict()

for i in range(len(cox)):
    index = 2*i
    dix[index] = cox[i]
    revdix[cox[i]] = index
xmaindex = index


for i in range(len(coy)):
    index = 2*i
    diy[index] = coy[i]
    revdiy[coy[i]] = index

ymaindex = (len(coy)-1)*2

cored = []

for c in co2:
    
    cx = revdix[c[0]]
    cy = revdiy[c[1]]
    cored.append((cx,cy))


i = 0

scord = set(cored)


green = False
gm = []
for j in range(ymaindex+1):
    gm.append([])
    for i in range(xmaindex+1):
        if (i,j) in scord:
            gm[j].append("#")

            green = not green

        else:
            if green == False:
                gm[j].append(".")
            else:
                gm[j].append("X")


green = False
for i in range(xmaindex+1):
    for j in range(ymaindex+1):
        if gm[j][i] == "#" :
            green = not green
        else:
            if green:
                gm[j][i] = "X"



##


Dir4 = [
    (1,0),
    (0,-1),
    (-1,0),
    (0,1)
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

###################
cored.sort(key=lambda x : x[0])
minl = [(cored[0][0]+1,cored[0][1]+1),(cored[1][0]+1,cored[1][1]+1)]
start = min(minl,key=lambda x: x[1])

op = [start]

clo = set()

while len(op)!=0:

    cu = op.pop()
    if cu in clo:
        continue

    clo.add(cu)
    gm[cu[1]][cu[0]] = "X"
    

    for d in gendir(cu[0],cu[1],Dir4):
        if inBorder(d[1],d[0],gm):
            if gm[d[1]][d[0]] == ".":
                op.append((d[0],d[1]))



###################

def ok(cr1,cr2):

    p1 = (min(cr1[0],cr2[0]),min(cr1[1],cr2[1]))
    p2 = (max(cr1[0],cr2[0]),max(cr1[1],cr2[1]))
    
    for i in range(p1[0],p2[0]+1,1):
        for j in range(p1[1],p2[1]+1,1):
            if gm[j][i] == ".":
                return False
    
    return True

mm = None
for i in range(len(cored)):
    print(i)
    for j in range(i+1,len(cored)):

        c1 = (dix[cored[i][0]],diy[cored[i][1]])
        c2 = (dix[cored[j][0]],diy[cored[j][1]])

        a = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)

        if mm == None or a > mm:

            if ok(cored[i],cored[j]):
                mm = a


print(mm)