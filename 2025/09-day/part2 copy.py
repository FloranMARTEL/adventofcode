#parti1

file = open("inputExemple2.txt","r")
file = open("input.txt","r")
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

    while i < len(co):
        
        v2 = co[i]
        if v2[0] == v[0]:
            vs.append(v2)
            i+=1
        else:
            break

    # if i == 192 or i==4:
    #     print("ici")

    vs.sort(key = lambda x:x[1])
    it = []
    for j in range(0,len(vs),2):
        it.append((vs[j],vs[j+1]))

    for iti in it:
        outise = True
        for ii,interi in enumerate(inter):

            if iti[0][1] < iti[1][1] == interi[0][1]:
                zon.append((interi[1],iti[1]))
                inter[ii] = (iti[0],(iti[0][0],interi[1][1]))
                outise = False
            elif iti[1][1] > iti[0][1] == interi[1][1]:
                zon.append((interi[0],iti[0]))
                inter[ii] = ((iti[1][0],interi[0][1]),iti[1])
                outise = False
            
            # elif iti[0][1] < iti[1][1] < interi[0][1]:
            #     zon.append((interi[1],iti[1]))
            #     inter.append(iti)
            #     inter[ii] = (iti[0],(iti[0][0],interi[1][1]))
            # elif iti[1][1] > iti[0][1] > interi[1][1]:
            #     zon.append((interi[0],iti[0]))
            #     inter[ii] = ((iti[1][0],interi[0][1]),iti[1])



            elif (iti[0][1] >= interi[0][1] and iti[1][1] < interi[1][1]):
                zon.append((interi[0],(iti[0][0],interi[1][1])))
                inter[ii] = (iti[1],(iti[1][0],interi[1][1])) 
                outise = False
            elif (iti[0][1] > interi[0][1] and iti[1][1] <= interi[1][1]):
                zon.append((interi[0],(iti[0][0],interi[1][1])))
                inter[ii] = (((iti[0][0],interi[0][1]),iti[0])) 
                outise = False

            
            elif iti[0][1] < interi[0][1] and iti[1][1] > interi[1][1]:
                zon.append((interi[0],(iti[0][0],interi[0][1])))
                inter[ii] = iti
                outise = False
            
            if inter[ii][0][1] > inter[ii][1][1]:
                print("coucou")

            if iti[0][1] == interi[0][1] and iti[1][1] == interi[1][1]:
                zon.append((interi[0],iti[1]))
                del inter[ii]
                outise = False
            
            if outise == False:
                break
        
        if outise == True:
            inter.append(iti)




    #merge inter
    inter.sort(key=lambda x : x[0][1])
    for ii in range(len(inter)-1,-1,-1):
        for jj in range(ii-1,-1,-1):

            it1 = inter[ii]
            it2 = inter[jj]

            if it1[0][1] <= it2[1][1] and it1[0][0] != it2[0][0]:
                zon.append((it1[1],(it2[0][0],it1[0][1])))
                it1 = ((it2[0][0],it1[0][1]),(it2[1][0],it1[1][1]))
                print("ici")


            if it1[0][0] == it2[0][0] and it1[0][1] <= it2[1][1]:
                print("la")
                inter[jj] = (it2[0],it1[1])
                del inter[ii]
                break




    # i+=1



def coinzone(c):

    for z in zon:

        if be2(z[0][0],z[1][0],c[0]) and be2(z[0][1],z[1][1],c[1]):
            return False

    return True

ma = None
m2 = 0
for i in range(len(co)):
    print(i)
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

        # if 4067490575 > a: 
        if ma == None or a > ma:
            m2 = ma
            ma = a
        elif m2 != None and a > m2:
            m2 = a 

print(ma)
print(m2)

4058706852