#parti1

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
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


print(r)
print(mj)

s = 0

for m in mj:
    ok = True
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            
            for re in r:
                if re[1] == m[i]:
                    if re[0] == m[j] :
                        ok = False

        for j in range(0,i+1):

            for re in r:
                if re[0] == m[i]:
                    if re[1] == m[j] :
                        ok = False
    
    print(ok)
    if ok:
        print(m[len(m)//2])
        s += int(m[len(m)//2])






print(s)