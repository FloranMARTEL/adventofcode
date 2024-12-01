

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()

""
priorite = dict()

for i,l in enumerate(alphabet):
    priorite[l] = i+1


score = 0
for IDgroupe in range(len(datalist)//3):
    
    l1 = set(datalist[IDgroupe*3+0])
    l2 = set(datalist[IDgroupe*3+1])
    l3 = set(datalist[IDgroupe*3+2])


    g = l1.intersection(l2.intersection(l3))

    score += priorite[g.pop()]

print(score)