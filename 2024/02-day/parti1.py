#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


cpt = 0
for ligne in datalist:

    l = [int(a) for a in ligne.split(" ")]
    inf = True
    aug = True
    dif = True
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            inf = False

        if l[i] >= l[i+1]:
            aug = False

        if not(1 <= abs(l[i] - l[i+1]) <= 3):
            dif = False
    
    if (inf or aug) and dif:
        cpt+=1


print(cpt)

