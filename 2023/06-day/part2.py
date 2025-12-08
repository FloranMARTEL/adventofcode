#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


t = [int(''.join(datalist[0].split(":")[1].split()))]
d = [int(''.join(datalist[1].split(":")[1].split()))]

print(t)
print(d)
mu = 1
ma = None
mi = None
for c in range(len(t)):
    
    cpt = 0
    for v in range(1,t[c]):

        dist = v*(t[c]-v)

        if dist > d[c]:
            cpt+=1

            if mi == None:
                mi = v
            
            ma = v

    print(cpt)

    mu *= cpt

print(mu)
print("ma : ",ma)
print("mi : ",mi)