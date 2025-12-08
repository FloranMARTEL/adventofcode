#parti2

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



s = set()

pok = []

plage.sort(key=lambda x: x[1]-x[0],reverse=True)

for p in plage:

    (pd,pf) = p

    ok = True
    for po in pok:

        if pd >= po[0] and pd <= po[1]:
            pd = po[1]+1
        
        if pf >= po[0] and pf <= po[1]:
            pf = po[0]-1
        
        if pf < pd:
            ok = False
            break



    if ok == True:
        pok.append((pd,pf))

cpt=0
s2 = set()
for po in pok:
    
    if po[1] in s2 or po[0] in s2:
        print("errer")
    
    s2.add(po[1])
    s2.add(po[0])

    # print((po[1]-po[0])+1)
    cpt += (po[1]-po[0])+1
    
    

print(cpt)




