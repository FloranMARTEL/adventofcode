#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


input = datalist[0].split("\n")

diinput = dict()

for i in input:

    res  = i.split(" ")

    v = res[0].replace(":","")

    diinput[v] = int(res[1])

action = []
gpartent = dict()
for a in datalist[1].split("\n"):

    a = a.split(" ")
    action.append((a[0],a[1],a[2],a[4]))
    gpartent[a[4]] = (a[0],a[1],a[2])

#####

def simulation(action):
        
    i = 0
    while True:
        a = action[i]

        res = 0
        if a[0] in diinput and  a[2] in diinput:
            

            x = diinput[a[0]]
            y = diinput[a[2]]

            if a[1] == "AND":
                res = diinput[a[0]] & diinput[a[2]]
            elif a[1] == "OR":
                res = diinput[a[0]] | diinput[a[2]]
            elif a[1] == "XOR":
                res = diinput[a[0]] ^ diinput[a[2]]

            diinput[a[3]] = res

            del action[i]
        
        i+=1

        if len(action) == 0:
            break

        if i >= len(action):
            i = 0

    
    z = givnum("z")

    return z
    


def givnum(stri):
    reslist = []

    for key in diinput:
        if key.startswith(stri):
            reslist.append((key,diinput[key]))


    reslist.sort(key=lambda x : x[0],reverse=True)

    bit = ""
    for r in reslist:
        bit += str(r[1])

    return int(bit,2)


x = givnum("x")
y = givnum("y")


print(bin(x+y)[2:])

z = simulation(action[:])

print(z)

binz = bin(z)[2:]
binadd = bin(x+y)[2:]

safe = set()

def finderr(val,trueval,p=0):

    c1,op,c2 = gpartent[val]
    v1 = diinput[c1]
    v2 = diinput[c2]

    if op == "AND":

        if trueval == 1:
            if diinput[c1] == 0 and diinput[c2] == 0:
                return val
            elif diinput[c1] == 0:
                safe.add(c2)
                return finderr(c1,1,p)
            elif diinput[c2] == 0:
                safe.add(c1)
                return finderr(c2,1,p)
        
        elif trueval == 0:
            if p == 0: 
                return val
            else:
                if c1 in safe:
                    return finderr(c2,0,p-1)
                elif c2 in safe:
                    return finderr(c1,0,p-1)


    elif op == "OR":

        if trueval == 1:
            if p == 0: 
                return val
            else:
                if c1 in safe:
                    return finderr(c2,1,p-1)
                elif c2 in safe:
                    return finderr(c1,1,p-1)
                return val
                
        
        elif trueval == 0:
            if diinput[c1] == 1 and diinput[c2] == 1:
                return val
            elif diinput[c1] == 1:
                safe.add(c2)
                return finderr(c1,0,p)
            elif diinput[c2] == 1:
                safe.add(c1)
                return finderr(c2,0,p)

    elif op == "XOR":
        if p == 0: 
                    return val
        else:

            if trueval == 0:
                if c1 in safe:
                    return finderr(c2,v1,p-1)
                elif c2 in safe:
                    return finderr(c1,v2,p-1)
                
                return val

            elif trueval == 1:
                if c1 in safe:
                    return finderr(c2,1-v1,p-1)
                elif c2 in safe:
                    return finderr(c1,1-v2,p-1)
                
                return val

def getchild(val):

    if val.startswith("x") or val.startswith("y"):
        return set([val])

    c1,op,c2 = gpartent[val]

    myset = set([c1,c2])
    myset = myset.union(getchild(c1))
    myset = myset.union(getchild(c2))

    return myset

from functools import *


@cache
def pa(val,res):
    pos = [] 
    c1,op,c2 = gpartent[val]

    if op == "AND":

        if res == 1:
            pos.append({c1:1,c2:1})

        else:
            pos.append({c1:0,c2:1})
            pos.append({c1:1,c2:0})
            pos.append({c1:0,c2:0})

    elif op == "OR":

        if res == 1:
            pos.append({c1:1,c2:0})
            pos.append({c1:0,c2:1})
            pos.append({c1:1,c2:1})
        else:
            pos.append({c1:0,c2:0})

    elif op == "XOR":

        if res == 1:
            pos.append({c1:1,c2:0})
            pos.append({c1:0,c2:1})
        else:
            pos.append({c1:1,c2:1})
            pos.append({c1:0,c2:0})
        
    return pos

def check_inco(d1,d2):
    for key2 in d2:
        if key2 in d1 and d2[key2] != d1[key2]:
            return False
    
    return True

curentpos = None
from tqdm import tqdm


binadd
cpt = 0
for i in range(len(binadd)):

    if binadd[i] != binz[i]:
        cpt +=1

print(cpt)

def resolve(val,want):

    c1,op,c2 = gpartent[val]

    if op == "AND":
        if want == 0:
            return [set([c1,c2])]
        elif want == 1:
            if diinput[c1] == 1:
                return [set([c2])]
            elif diinput[c2] == 1:
                return [set([c1])]
            else:
                return [set([c1]),set([c2])]#les deux
    
    elif op == "OR":
        if want == 0:

            if diinput[c1] == 0:
                return [set([c2])]
            elif diinput[c2] == 0:
                return [set([c1])]
            else:
                return [set([c1]),set([c2])]#les deux
            
        elif want == 1:

            return [set([c1,c2])]
    
    elif op == "XOR":

        return [set([c1,c2])]


def ok(val:str):
    if val.startswith('x') or val.startswith('y'):
        return False

    return True 


pos :list[list[set]]= []
for i in range(len(binadd)):

    if binadd[i] != binz[i]:
        valz = "z"+str(len(binadd)-1-i).zfill(2)

        res = resolve(valz,int(binadd[i]))

        print(res)
        pos.append(res)


def app():
    global pos
    print("--------------------------")

    for i in range(len(pos)):
        for j in range(len(pos[i])):
            toadd = []
            for s in pos[i][j]:

                res = resolve(s,1-diinput[s])

                canchange = False
                for r in res:
                    for v in r:
                        if ok(v) == True:
                            canchange = True
                            break

                if canchange == False:
                    pass
                else:
                    toadd.append(res)

                print(res)
            
            #add
            for s in toadd:
                if len(s) == 1:
                    pos[i][j] = pos[i][j].union(s[0])
                else:
                    print("sorry")


app()
app()
app()
app()
app()
app()
app()
app()
app()
app()
app()

compter = dict()

for l in pos:
    for c in l:
        for s in c:

            if s not in compter:
                compter[s] = 1
            else:
                compter[s] += 1

print(compter)

maxval = None
maxid = None
for key in compter:
    
    if maxval == None or maxval < compter[key]:
        maxval = compter[key]
        maxid = key

print(maxid,diinput[maxid])

l = 0
while l < len(pos):

    if maxid in pos[l][0]:
        del pos[l]
        l-=1
    
    l+=1



compter = dict()

for l in pos:
    for c in l:
        for s in c:

            if s not in compter:
                compter[s] = 1
            else:
                compter[s] += 1

print("ici")
           
maxval = None
maxid = None
for key in compter:
    
    if maxval == None or maxval < compter[key]:
        maxval = compter[key]
        maxid = key

print(maxid,diinput[maxid])

#3
l = 0
while l < len(pos):

    if maxid in pos[l][0]:
        del pos[l]
        l-=1
    
    l+=1


compter = dict()

for l in pos:
    for c in l:
        for s in c:

            if s not in compter:
                compter[s] = 1
            else:
                compter[s] += 1

print("ici")


print(0 ^ 0)