#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

[p,ids] = data.split("\n\n")


p = p.split("\n")
ids = ids.split("\n")

print(p)
print(ids)

plage = []
for o in p:

    [d,f] = o.split("-")
    plage.append((int(d),int(f)))

cpt = 0
for id in ids:

    i = int(id)

    for p in plage:

        if i >= p[0] and i <= p[1]:
            cpt+=1
            break


print(cpt)




