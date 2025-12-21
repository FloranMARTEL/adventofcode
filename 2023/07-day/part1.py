#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

valeur = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
valeur = valeur[::-1]
valeurdi = dict()

for i in range(len(valeur)):
    valeurdi[valeur[i]] = i

elems = []

for l in datalist:

    [jeux,mul] = l.split()
    mul = int(mul)

    cptdi = dict()

    jocker = 0
    for c in jeux:
        cptdi[c] = cptdi.get(c,0)+1
    
    ma1 = 0
    ma2 = 0
    for k in cptdi:
        if cptdi[k] >= ma2:
            ma2 = cptdi[k]

        if cptdi[k] >= ma1:
            ma2 = ma1
            ma1 = cptdi[k]

    elems.append((jeux,(ma1,ma2),mul))


def key_func(elem):
    jeux = elem[0]
    return (
        elem[1][0],
        elem[1][1],
        [valeurdi[c] for c in jeux]
    )



elems.sort(key=key_func)

su = 0
for i,e in enumerate(elems):
    print(e[2],(i+1))

    su += e[2]*(i+1)

print(su)




