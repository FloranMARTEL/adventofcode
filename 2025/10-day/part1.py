#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def app(ch,b):


    ch = list(ch)
    for e in b:
        if ch[e] == "#":
            ch[e] = "."
        else:
            ch[e] = "#"
    
    return tuple(ch)

cpt = 0
for l in datalist:

    l = l.split(" ")

    ch = tuple([a for a in l[0][1:-1]])
    ex = list(map(int,l[-1][1:-1].split(",")))

    l = l[1:-1]

    b = list(map(lambda x: x[1:-1].split(","),l))

    for i in range(len(b)):
        b[i] = list(map(int,b[i]))
    

    newnode = [(tuple(["." for i in range(len(ch))]),[])]
    oldnode = set()
    futnode = []
    showstate = set((".",".",".","."))
    p = 0
    while ch not in showstate:

        for n in newnode:
            for bo in b:

                newchar = app(n[0],bo)
                if newchar not in showstate:
                    showstate.add(newchar)
                    action = n[1][:]
                    action.append(bo)
                    futnode.append((newchar,action))
        
        newnode = futnode
        futnode = []

        p+=1
    
    print(p)
    cpt +=p
    # print(ch)
    # print(b)
    # print(ex)

print(cpt)
