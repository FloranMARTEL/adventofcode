class Djikstra:

    def dij(graph,start,end):

        view = {start}
        tab = {start : 0}
        parent = {start : None}

        cc = start
        sew = set()

        candidat = None

        while candidat == None or len(candidat) != 0:

            candidat = []

            des = graph[cc]
            for key in des:
                if des[key] not in sew:
                    candidat.append((cc,key,des[key]))

            for c in candidat:
                if c[1] not in tab:
                    tab[c[1]] = tab[c[0]]+c[2]
                    parent[c[1]] = c[0]
                
                elif tab[c[1]] > tab[c[0]]+c[2]:
                    tab[c[1]] = tab[c[0]]+c[2]
                    parent[c[1]] = c[0]

                #del graph[c[0]][c[1]]

                view.add(c[1])

            min = None
            e = None
            for elem  in view.difference(sew):
                if min == None or min > tab[elem]:
                    min = tab[elem]
                    e = elem

            
            if e != None:
                sew.add(e)
                cc = e
            else:
                print("erreur")
                break
                
            path = [end]
            curent = end
            while curent != start:
                curent = parent[curent]
                path.append(curent)
            path =  list(reversed(path))
            return path


    def dijAll(graph,start,end):

        view = {start}
        tab = {start : 0}
        parent = {start : None}

        cc = start
        sew = set()

        candidat = None

        while candidat == None or len(candidat) != 0:

            candidat = []

            des = graph[cc]
            for key in des:
                if True :
                    candidat.append((cc,key,des[key]))
                    

            for c in candidat:
                if c[1] not in tab:
                    tab[c[1]] = tab[c[0]]+c[2]
                    parent[c[1]] = {c[0]}
                
                elif tab[c[1]] > tab[c[0]]+c[2]:
                    tab[c[1]] = tab[c[0]]+c[2]
                    parent[c[1]] = {c[0]}
                elif tab[c[1]] == tab[c[0]]+c[2] :
                    parent[c[1]].add(c[0])


                view.add(c[1])

            min = None
            e = None
            for elem  in view.difference(sew):
                if min == None or min > tab[elem]:
                    min = tab[elem]
                    e = elem

            
            if e != None:
                sew.add(e)
                cc = e
            else:
                print("erreur")
                break

            

        
        def getss(end,start,parent):

            if end == (7,5,(0,1)):
                print('ici')

            if end == start:
                return {(end[0],end[1])}

            myset = {(end[0],end[1])}
            for p in parent[end]:
                
                myset = myset.union(getss(p,start,parent))

            return myset

        

        return getss(end,start,parent)
##########################


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