#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")

licle = []
liser = []

for da in datalist:
    
    obj = da.split("\n")


    clé = True

    listcompt = [-1]*len(obj[0])

    for i in range(len(obj)):
        for j in range(len(obj[i])):
            if i == 0 and obj[i][j] != "#":
                clé = False

            if obj[i][j] == "#":
                listcompt[j] += 1

    
    if clé:
        licle.append(listcompt)
    else:
        liser.append(listcompt)


cpt = 0
for c in licle:
    for s in liser:

        valid = True
        for i in range(len(c)):

            if c[i]+s[i] > 5:
                valid = False
        
        if valid:
            cpt+=1



print(cpt)
            







