#part
file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


règle = datalist[0].split("\n")
r = []
for i in règle:
    r.append(i.split("|"))

jour = datalist[1].split("\n")

mj = []
for i in jour:
    mj.append(i.split(","))




def so(a,b):
    for re in r:
        if re[1] == a:
            if re[0] == b :
                return False
    
    
    return True
    

s2=0

for m in mj:
    ok = True
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if not so(m[i],m[j]):
                ok = False
    
    if not ok:
        serted = m[:]
        for i in range(len(serted)):
            for j in range(i+1,len(serted)):

                if not so(serted[i],serted[j]):
                    tmp = serted[i]
                    serted[i] = serted[j]
                    serted[j] = tmp
        
        s2 += int(serted[len(serted)//2])








print(s2)