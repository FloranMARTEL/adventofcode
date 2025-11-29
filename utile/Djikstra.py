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