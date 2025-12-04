#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


mol = list(range(0,99+1))
print(mol)

dir = {
    "L":-1,
    "R" : 1
}

cur = 50

cpt = 0

for l in datalist:

    num = l[1:]
    co = dir[l[0]]

    val = int(num)*co

    cur += val
    cur = cur % 100

    if cur == 0:
        cpt+=1
    



print(cur)
print(cpt)

