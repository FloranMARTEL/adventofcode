

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

[pi,mo] = data.split("\n\n")



v = pi.split("\n")
a = v[-1].split("   ")

lipi = [[] for i in range(len(a))]

for j in range(len(lipi)):
    for i in range(len(a)-1,-1,-1):
        
        p = v[i][j*4+1]
        if p == " ":
            break
        else:
            lipi[j].append(p)

##
mo = mo.split("\n")
for m in mo:
    m = m.split(" ")
    for i in range(int(m[1])):

        v = lipi[int(m[3])-1].pop()
        lipi[int(m[5])-1].append(v)


som = ""

for p in lipi:
    som += p.pop()


print(som)