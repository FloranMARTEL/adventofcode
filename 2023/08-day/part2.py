#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")




direc = {
    "R" : 1,
    "L" : 0,
}

di = datalist[0]

chem = dict()
currents = []
for l in datalist[1].split("\n"):

    [s,ds] = l.split("=")

    [da,db] = ds.split(",")


    s = s[:-1]
    da,db = da[2:],db[1:-1]

    chem[s] = (da,db)

    if s[-1] == "A":
        currents.append(s)


currents2 = currents[:]
info = []
dmax = 0
for i,cu in enumerate(currents):
    dirid = 0
    cpt = 0

    debut = None
    ch = []
    renc = 0
    while renc != 2 or currents[i][-1] != "Z":

        if renc == 1:
            # ch+=1
            ch.append(currents[i])

        currents[i] = chem[currents[i]][direc[di[dirid]]]

        cpt +=1
        dirid = (dirid +1 ) % len(di)

        if currents[i][-1] == "Z":
            renc+=1
            if renc == 1:
                debut = cpt
    
    if dmax < debut:
        dmax = debut

    info.append((debut,ch))



cm = []
info.sort(key=lambda x:x[0])

ido = 0
for i,inf in enumerate(info):
    cm.append((inf[1][0],0))
    ida = inf[0]
    for j in range(i):
        p = (cm[j][1]+(ida-ido))%info[j][0]
        newcu = info[j][1][p]
        cm[j] = (newcu,p)
    
    ido=ida


suinc = dmax
import pulp
cm2 = cm[:]
for i,cu in enumerate(cm[:-1]):
    cu = cm[i]
    k = 0
    a = cu[1]
    while a != 0:
        a = (cu[1]+dmax*k)%info[i][0]

        
        k+=1
    
    inc = dmax*(k-1)
    suinc += inc
    for j in range(len(cm)):
        p = (cm[j][1]+(inc))%info[j][0]
        newcu = info[j][1][p]
        cm[j] = (newcu,p)


    # dmax = 6
    # info[i][0] = 4
    prob = pulp.LpProblem("IntegerSystemMinSum", pulp.LpMinimize)

    b,c = [pulp.LpVariable(ii,lowBound=1,cat="Integer") for ii in ["b","c"]]

    prob += c
    # prob += 6*b == 4*c
    prob += dmax*b == info[i][0]*c


    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    r = [int(ii.value()) for ii in [b,c] ]
    r = dmax * int(b.value())
    r2 = dmax*info[i][0]
    dmax = dmax * int(b.value())
    
print(suinc)
