#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


seeds = list(map(int,datalist[0].split(":")[1].split(" ")[1:]))

print(seeds)
m = None
for s in seeds:
    for l in datalist[1:]:

        inter = l.split("\n")[1:]

        for i in inter:
            i = i.split(" ")
            i = list(map(int,i))

            if s >= i[1] and s < i[1]+i[2]:
                s = s-i[1]+i[0]
                break
    
    if m == None or m > s:
        m = s
    print(s)

print("m : ",m)





