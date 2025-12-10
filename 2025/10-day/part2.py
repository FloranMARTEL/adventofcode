#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

import math

def h(v,goal):

    dif = 0
    for i in range(len(v)):
        d = (goal[i] - v[i])
        # if d < 0:
        #     return 100000
        
        dif += d*d
    return dif
    # return math.sqrt(dif)

def gen_node(curent):

    chi = []
    for bo in b:
        chi.append(app(curent,bo))
    
    return chi

import heapq

def myas(start,end):

    parent = {start : None}
    coup = {start : 0}

    openlist = [start]

    openheap = []
    heapq.heappush(openheap, (0, 0, start))
    closed = set()
    cpt = 0
    while openheap:
        cpt+=1
        # print(cpt,len(parent))
        f, current_g, current = heapq.heappop(openheap)

        if current in closed:
            continue
        closed.add(current)

        if current == end:
            # Reconstituer le chemin
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            return path[::-1]


        neighbor = gen_node(current)


        for n in neighbor:

            cost = current_g + 1

            if n not in coup or cost < coup[n]:
                coup[n] = cost
                parent[n] = current
                f_cost = cost + h(n,end)
                heapq.heappush(openheap, (f_cost, cost, n))

    
    return []


####

def app(ch,b,x=1):


    ch = list(ch)
    for e in b:
        ch[e] += x
    
    return tuple(ch)

def valid(ch,ob):
    for i in range(len(ch)):
        if ch[i] > ob[i]:
            return False
    return True

def parprfo(val,cptb):
    
    if val == ex:
        return cptb

    mi = None
    for i in range(len(b)):
        newval = app(val,b[i])
        if valid(newval,ex):
            newcptb = cptb[:]
            newcptb[i] += 1
            return parprfo(newval,newcptb)
            if mi == None or v < mi:
                mi = v
    
    return mi
    


    



cpt = 0
for l in datalist:

    l = l.split(" ")

    ch = tuple([a for a in l[0][1:-1]])
    ex = tuple(map(int,l[-1][1:-1].split(",")))

    l = l[1:-1]

    b = list(map(lambda x: x[1:-1].split(","),l))

    for i in range(len(b)):
        b[i] = list(map(int,b[i]))
    
    newnode = [(tuple([0 for i in range(len(ch))]),[])]
    oldnode = set()
    futnode = []
    showstate = set(newnode[0][0])
    p = 0
    # while ex not in showstate:

    #     for n in newnode:
    #         if valid(n[0],ex):
    #             for bo in b:

    #                 newchar = app(n[0],bo)
    #                 if newchar not in showstate:
    #                     showstate.add(newchar)
    #                     action = n[1][:]
    #                     action.append(bo)
    #                     futnode.append((newchar,action))
        
    #     newnode = futnode
    #     futnode = []

    #     p+=1

    curelem = tuple([0 for i in range(len(ch))])

    b.sort(key=lambda x:len(x),reverse=True)

    # m = min(ex)
    # cptb = [0 for i in range(len(b))]
    # cptb[0] = m
    # curelem = app(curelem,b[0],m)

    # p = len(parprfo(curelem,cptb))

    pa = myas(curelem,ex) 
    
    p = len(pa)-2
    print(p)
    cpt +=p
    # print(ch)
    # print(b)
    # print(ex)

print(cpt)
