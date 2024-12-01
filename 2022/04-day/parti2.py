

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

cpt = 0
for d in datalist:
    [el1,el2] = d.split(",")

    [mi1,ma1] = el1.split("-")
    [mi2,ma2] = el2.split("-")

    mi1 = int(mi1)
    ma1 = int(ma1)
    mi2 = int(mi2)
    ma2 = int(ma2)

    set1 = set(range(mi1,ma1+1))
    set2 = set(range(mi2,ma2+1))

    if mi1 in set2 or ma1 in set2 or mi2 in set1 or ma2 in set1:
        cpt += 1

print(cpt)
