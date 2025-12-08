#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

cpt = 0
setid = {1:0}
lid = 0
for l in datalist:

    lid +=1
    [d,p] = l.split(":")

    id = int(d.split(" ")[-1])

    [g,m] = p.split("|")

    g = g.split(" ")[:-1]

    sg = set()
    for i in g:
        if i != "":
            sg.add(int(i))

    m = m.split(" ")
    sm = set()
    for i in m:
        if i != "":
            sm.add(int(i))

    f = sg.intersection(sm)
    num = len(f)
    # if len(f) > 0:
    #     num = 2**(len(f)-1)
    
    for v in range(id+1,id+1+num):
        if v == 6:
            print("cic")
        setid[v] = setid.get(v,0) + setid.get(id,0)+1


cpt = 0
for k in range(1,len(datalist)+1):
    print(setid.get(k,0)+1)
    cpt += setid.get(k,0)+1

print(cpt)
