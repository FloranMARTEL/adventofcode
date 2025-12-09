#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


co = []
for l in datalist:

    c = l.split(",")
    c = list(map(int,c))
    co.append(c)

co = list(map(lambda x : (x[0],x[1]), co))
sco = set(co)

co.sort(key=lambda x: x[0])
zon = []

co2 = co[:]

def be(a,b,v):

    if a < b:
        return a < v < b
    else:
        return a > v > b

def be2(a,b,v):

    if a < b:
        return a <= v <= b
    else:
        return a >= v >= b



i = 0
inter = []
while i < len(co):

    v = co[i]

    vs = []

    while True:
        
        v2 = co[i]
        if v2[0] == v[0]:
            vs.append(v2)
            i+=1
        else:
            break

    
    vs.sort(key = lambda x:x[1])

    

    i+=1



def coinzone(c):

    for z in zon:

        if be2(z[0][0],z[1][0],c[0]) and be2(z[0][1],z[1][1],c[1]):
            return False

    return True

ma = None
for i in range(len(co)):
    # print(i)
    for j in range(i+1,len(co)):

        c1 = co[i]
        c2 = co[j]


        if c1 == [9,5] and c2 == [2,3]:
            print("ici")

        er = False
        for o in range(len(co)):
            c3 = co[o]

            if c3 != c1 and c3 != c2:

                if be(c1[0],c2[0],c3[0]) and be(c1[1],c2[1],c3[1]):
                    er = True
                    break
        
        if er == True:
            continue
                
        
        pos = [c1,c2,(c1[0],c2[1]),(c2[0],c1[1])]
        oo = True
        for p in pos:
            if coinzone(p):
                oo = False
                break
        
        if oo == False:
            continue
        
        a = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)

        if ma == None or a > ma:
            ma = a

print(ma)

