#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


co = []
for l in datalist:

    c = l.split(",")
    c = list(map(int,c))
    co.append(c)


ma = None
for i in range(len(co)):
    for j in range(i+1,len(co)):

        c1 = co[i]
        c2 = co[j]

        if c1 == [11,1] and c2 == [2,5]:
            print("ici")
        
        a = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)

        if ma == None or a > ma:
            ma = a

print(ma)

