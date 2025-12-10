file = open("t2.txt","r")
data = file.read()

datalist = data.split("\n")
l = []
for i in range(len(datalist)):
    for j in range(len(datalist[i])):
        v = datalist[i][j] 
        if v == "#":
            l.append(f"{j},{i}")

print("\n".join(l))

