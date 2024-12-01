

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

cpt = 0
for d in datalist:
    [el1,el2] = d.split(",")

    [mi1,ma1] = el1.split("-")
    [mi2,ma2] = el2.split("-")

    set1 = set(range(int(mi1),int(ma1)+1))
    set2 = set(range(int(mi2),int(ma2)+1))

    if set1.issubset(set2) or set2.issubset(set1):
        cpt += 1

print(cpt)



