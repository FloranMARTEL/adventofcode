#parti1

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

for l in datalist[1].split("\n"):

    [s,ds] = l.split("=")

    [da,db] = ds.split(",")


    s = s[:-1]
    da,db = da[2:],db[1:-1]

    chem[s] = (da,db)

    



curent = "AAA"

dirid = 0
cpt = 0
while curent != "ZZZ":

    curent = chem[curent][direc[di[dirid]]]

    cpt +=1
    dirid = (dirid +1 ) % len(di)


print(cpt)

