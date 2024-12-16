#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

l = 101#11
h = 103#7

class rob:
    
    def __init__(self,r,l,vr,vl):
        self.r = r
        self.l = l
        self.vr = vr
        self.vl = vl

    def move(self):
        self.r = (self.r + self.vr)%h
        self.l = (self.l + self.vl)%l


lirob :list[rob] = []
for li in datalist:

    o = li.split(" ")
    k = o[0].split("=")[1]
    pos = k.split(",")

    k = o[1].split("=")[1]
    vi = k.split(",")

    lirob.append(rob(int(pos[1]),int(pos[0]),int(vi[1]),int(vi[0])))


for i in range(100):

    for r in lirob:
        r.move()


grid = []

for i in range(h):
    grid.append([])
    for j in range(l):
        grid[i].append(0)


for r in lirob:
    grid[r.r][r.l] += 1

g1 = 0
for i in range(h//2):
    for j in range(l//2):
        g1+=grid[i][j]
    
g2 = 0
for i in range(h//2):
    for j in range((l//2)+1,l):
        g2+=grid[i][j]

g3 = 0
for i in range(h//2+1,h):
    for j in range(l//2+1,l):
        g3+=grid[i][j]
g4 = 0
for i in range(h//2+1,h):
    for j in range(l//2):
        g4+=grid[i][j]

print(g1*g2*g3*g4)