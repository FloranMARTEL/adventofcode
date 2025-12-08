#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

cpt = 0
for l in datalist:

    [d,p] = l.split(":")
    
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
    if len(f) > 0:
        cpt += 2**(len(f)-1)

print(cpt)

