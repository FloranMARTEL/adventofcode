#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


t = list(map(int,datalist[0].split(":")[1].split()))
d = list(map(int,datalist[1].split(":")[1].split()))

print(t)
print(d)
mu = 1
for c in range(len(t)):
    
    cpt = 0
    for v in range(1,t[c]):

        dist = v*(t[c]-v)

        if dist > d[c]:
            cpt+=1
    print(cpt)

    mu *= cpt

print(mu)