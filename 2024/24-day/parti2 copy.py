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

print("----")
print(binz)
print(binadd)
print("----")
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
        return set() #set([val])

    c1,op,c2 = gpartent[val]

    myset = set([val])
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

def ok(val:str):
    if val.startswith('x') or val.startswith('y'):
        return False

    return True


uni = set()
for i in range(len(binadd)):

    if binadd[i] != binz[i]:
        valz = "z"+str(len(binadd)-1-i).zfill(2)
        childs = getchild(valz)
        uni = uni.union(childs)

print(childs)

for k in tqdm(childs):
    if ok(k):
        child = getchild(k)
        posibiL = childs.difference(child)
        for l in posibiL:
            if l != k and k not in getchild(l):
                for m in childs:
                    if m!=k and m!=l and ok(m):
                        child = getchild(m)
                        posibiO = childs.difference(child)
                        for o in posibiO:
                            if o!=k and o!=l and o!=m and m not in getchild(o):
                                for p in childs:
                                    if p!=k and p!=l and p!=m and p!=o and ok(p):
                                        child = getchild(p)
                                        posibiQ = childs.difference(child)
                                        for q in posibiQ:
                                            if q!=k and q!=l and q!=m and q!=o and q!=p and p not in getchild(q):
                                                for r in childs:
                                                    if r!=k and r!=l and r!=m and r!=o and r!=p and r!=q and ok(r):
                                                        child = getchild(r)
                                                        posibiS = childs.difference(child)
                                                        for s in posibiQ:
                                                            if  s!=k and s!=l and s!=m and s!=o and s!=p and s!=q and s!=r and r not in getchild(s):
                                                                pass
                                                                #print(k,l,m,o,p,q,r,s)

           
                    


print(0 ^ 0)