#parti2
from copy import deepcopy

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


cpt = 0
for ligne in datalist:

    l = [int(a) for a in ligne.split(" ")]
    sec = False

    for o in range(len(l)+1):
        
        l2 = deepcopy(l)
        if o != len(l):
            del l2[o]

        inf = True
        aug = True
        dif = True
        for i in range(len(l2)-1):
            if l2[i] <= l2[i+1]:
                inf = False

            if l2[i] >= l2[i+1]:
                aug = False

            if not(1 <= abs(l2[i] - l2[i+1]) <= 3):
                dif = False
        
        if (inf or aug) and dif:
            sec = True
    
    if sec:
        cpt+=1


print(cpt)